# Infrastructure: domain, DNS, and hosting

This is the runbook for the infrastructure behind https://searenityonlummi.com. It is written so a maintainer or coding agent (Claude Code, Codex, or similar) can inspect, fix, or rebuild the setup from this file alone. Dave never needs any of it; his work is all in [site/](../site/), guided by [AGENTS.md](../AGENTS.md).

Infrastructure changes are made on Steve's machine with Steve's credentials. An agent working in Dave's session must not attempt anything in this file; tell Dave to ask Steve instead.

## Overview

| Piece | Where | Identifier |
| --- | --- | --- |
| Domain registration | AWS Route 53 Domains in Steve's AWS account, region `us-east-1` | `searenityonlummi.com`, auto-renew on, expires 2027-10-08 |
| DNS | Route 53 public hosted zone, same account | `Z03278562EKNCL6Y73ZQH` |
| Source repo | GitHub, public | `BigLep/searenityonlummi.com`, default branch `main` |
| Hosting | GitHub Pages, built by GitHub Actions | workflow [pages.yml](../.github/workflows/pages.yml), publishes `site/` only |
| HTTPS certificate | Issued and renewed automatically by GitHub Pages | covers the bare domain and `www` |
| Collaborator | GitHub user `davidloeppky` (Dave) | Write access, pushes straight to `main` |
| Claude access for Dave | Dave's own claude.ai account, Claude desktop app, Code tab | started on a 7-day Pro guest pass from Steve |

Request flow: the browser resolves `searenityonlummi.com` through Route 53 to GitHub Pages' IPs; GitHub serves the latest artifact uploaded by the `Publish site` workflow; `http://` and `www.` redirect to `https://searenityonlummi.com/`.

## Access

- **AWS**: credentials for the AWS account that holds the domain, set as `AWS_PROFILE` (or the default credentials) before running the commands below. Ask Steve which profile that is. Confirm you have the right account before changing anything: the health check's first command must return the domain's details, not a "Domain ... not found in account" error.
- **GitHub**: `gh` authenticated as `BigLep` (repo owner, admin). Confirm with `gh auth status`.

The AWS account also holds unrelated resources. Only touch the resources listed in the overview.

## Configuration

### DNS records (hosted zone `Z03278562EKNCL6Y73ZQH`)

| Name | Type | Value |
| --- | --- | --- |
| `searenityonlummi.com` | `A` | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 |
| `searenityonlummi.com` | `AAAA` | 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153 |
| `www.searenityonlummi.com` | `CNAME` | `biglep.github.io` |
| `_github-pages-challenge-BigLep.searenityonlummi.com` | `TXT` | domain verification code from GitHub (see below) |

The `A`/`AAAA` values are GitHub Pages' published addresses ([GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)). The domain's registered nameservers must match the zone's: `ns-571.awsdns-07.net`, `ns-1530.awsdns-63.org`, `ns-171.awsdns-21.com`, `ns-1717.awsdns-22.co.uk`.

### GitHub Pages

- Source: GitHub Actions (`build_type: workflow`), not a branch.
- Custom domain: `searenityonlummi.com`, set in the repo's Pages settings. There is no `CNAME` file in `site/`; with Actions-based Pages the domain lives in settings only.
- HTTPS enforced.
- Workflow [.github/workflows/pages.yml](../.github/workflows/pages.yml) runs on push to `main` (check, then deploy), on pull requests (check only), and on manual dispatch. The check job fails if any image in `site/` still has metadata ([tools/strip-metadata.py](../tools/strip-metadata.py) `--check site`) or any file is over 25 MB.

### Domain verification

The domain is verified for the `BigLep` GitHub account (github.com > Settings > Pages > Verified domains) so no other GitHub account can serve it. GitHub has no API for this, so a human does it in the web UI: add the domain, create the `TXT` record GitHub shows (name `_github-pages-challenge-BigLep.searenityonlummi.com`), wait for DNS, click Verify. Keep the `TXT` record afterwards; GitHub re-checks it.

## Health check

Run all of these; each line says what to expect.

```sh
# Registered nameservers match the hosted zone (expect the four ns-* names above)
aws route53domains get-domain-detail --region us-east-1 \
  --domain-name searenityonlummi.com --query '{ns:Nameservers[].Name,autoRenew:AutoRenew,expires:ExpirationDate}'

# Records in the zone (expect the table above, plus NS and SOA)
aws route53 list-resource-record-sets --hosted-zone-id Z03278562EKNCL6Y73ZQH \
  --query 'ResourceRecordSets[].[Name,Type,join(`,`,ResourceRecords[].Value)]' --output text

# Public DNS (expect the four GitHub IPs)
dig +short A searenityonlummi.com @8.8.8.8

# Pages settings (expect cname searenityonlummi.com, build_type workflow, https_enforced true, certificate state approved)
gh api repos/BigLep/searenityonlummi.com/pages \
  --jq '{cname,build_type,https_enforced,cert:.https_certificate.state,cert_expires:.https_certificate.expires_at}'

# Recent publishes (expect success)
gh run list -R BigLep/searenityonlummi.com --workflow pages.yml --limit 5

# Live responses (expect 200, then 301s to https://searenityonlummi.com/)
curl -sI https://searenityonlummi.com/ | head -1
curl -sI http://searenityonlummi.com/ | grep -iE '^(HTTP|location)'
curl -sI https://www.searenityonlummi.com/ | grep -iE '^(HTTP|location)'

# Collaborators (expect davidloeppky with push) and pending invitations
gh api repos/BigLep/searenityonlummi.com/collaborators --jq '.[] | {login, push: .permissions.push}'
gh api repos/BigLep/searenityonlummi.com/invitations --jq '.[] | {invitee: .invitee.login, permissions}'
```

If `curl` on the Mac says "Could not resolve host" but `dig @8.8.8.8` works, the Mac is holding a cached negative answer; it clears on its own, or with `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`.

## Common tasks

**Re-run a publish** (for example after a GitHub outage):

```sh
gh workflow run pages.yml -R BigLep/searenityonlummi.com --ref main
gh run watch -R BigLep/searenityonlummi.com
```

**Change or add a DNS record**: write a change batch and apply it. Use `UPSERT` to create or replace, `DELETE` with the exact current values to remove.

```sh
cat > /tmp/change.json <<'EOF'
{"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":"example.searenityonlummi.com","Type":"CNAME","TTL":3600,"ResourceRecords":[{"Value":"target.example.net"}]}}]}
EOF
aws route53 change-resource-record-sets --hosted-zone-id Z03278562EKNCL6Y73ZQH --change-batch file:///tmp/change.json
```

**Add or remove a collaborator**:

```sh
gh api -X PUT repos/BigLep/searenityonlummi.com/collaborators/USERNAME -f permission=push
gh api -X DELETE repos/BigLep/searenityonlummi.com/collaborators/USERNAME
```

**Certificate problems**: GitHub renews automatically while DNS points at Pages. If `https_certificate.state` is not `approved`, check DNS first, then remove and re-add the custom domain to trigger a new certificate. ASSUMPTION: not yet exercised on this site; removing the domain takes the site offline until it is re-added and the certificate is approved.

```sh
gh api -X PUT repos/BigLep/searenityonlummi.com/pages -f cname=
gh api -X PUT repos/BigLep/searenityonlummi.com/pages -f cname=searenityonlummi.com
# wait until the certificate is approved, then:
gh api -X PUT repos/BigLep/searenityonlummi.com/pages -F https_enforced=true
```

**Domain renewal**: automatic (auto-renew is on and billed to the AWS account). Check the expiry date with the health check.

## Rebuild from scratch

The steps that created the current setup, in order. Use them if the hosted zone, repo, or Pages config is lost.

1. **Hosted zone**, then point the registration at its nameservers:

   ```sh
   aws route53 create-hosted-zone --name searenityonlummi.com \
     --caller-reference "searenity-$(date +%s)" --hosted-zone-config Comment="GitHub Pages site"
   # use the four DelegationSet.NameServers from the output:
   aws route53domains update-domain-nameservers --region us-east-1 \
     --domain-name searenityonlummi.com --nameservers Name=NS1 Name=NS2 Name=NS3 Name=NS4
   # track it until Status is SUCCESSFUL:
   aws route53domains get-operation-detail --region us-east-1 --operation-id OPERATION_ID
   ```

   Update the zone ID and nameservers in this file.

2. **Records**: create the `A`, `AAAA`, and `www` `CNAME` records from the table above with a change batch (`"Action":"CREATE"`).

3. **Repo** (from a clone of this repo; skip if it exists):

   ```sh
   gh repo create BigLep/searenityonlummi.com --public --source . --remote origin --push \
     --description "Searenity on Lummi website, built by Dave Loeppky with Claude" --homepage https://searenityonlummi.com
   ```

4. **Pages**: enable with Actions as the source, set the domain, run the workflow, then enforce HTTPS once the certificate is approved (usually minutes after DNS resolves):

   ```sh
   gh api -X POST repos/BigLep/searenityonlummi.com/pages -f build_type=workflow
   gh api -X PUT repos/BigLep/searenityonlummi.com/pages -f cname=searenityonlummi.com
   gh workflow run pages.yml -R BigLep/searenityonlummi.com --ref main
   gh api repos/BigLep/searenityonlummi.com/pages --jq .https_certificate.state   # repeat until "approved"
   gh api -X PUT repos/BigLep/searenityonlummi.com/pages -F https_enforced=true
   ```

5. **Collaborator**: `gh api -X PUT repos/BigLep/searenityonlummi.com/collaborators/davidloeppky -f permission=push` (Dave accepts the emailed invite).

6. **Domain verification**: the manual web-UI step in [Domain verification](#domain-verification).

7. **Health check**: run the commands above and confirm every expectation.
