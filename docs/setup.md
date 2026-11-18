# How searenityonlummi.com is hosted

This is the one-time infrastructure, maintained by Steve. Dave does not need any of it.

## Domain and DNS (AWS)

- The domain is registered with Route 53 Domains in Steve's AWS account, with auto-renew on. The current registration runs to 2027-10-08.
- DNS is the public hosted zone `Z03278562EKNCL6Y73ZQH`, and the domain's nameservers point at it: `ns-571.awsdns-07.net`, `ns-1530.awsdns-63.org`, `ns-171.awsdns-21.com`, `ns-1717.awsdns-22.co.uk`.
- Records for GitHub Pages ([GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)):
  - `searenityonlummi.com` `A`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
  - `searenityonlummi.com` `AAAA`: 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153
  - `www.searenityonlummi.com` `CNAME`: `biglep.github.io` (GitHub redirects `www` to the bare domain)
  - `_github-pages-challenge-BigLep.searenityonlummi.com` `TXT`: the domain verification code from GitHub (see below)

## Hosting (GitHub Pages)

- Repo: https://github.com/BigLep/searenityonlummi.com (public). Dave (`davidloeppky`) has Write access and pushes to `main` directly.
- Pages source is GitHub Actions: [.github/workflows/pages.yml](../.github/workflows/pages.yml) checks `site/` (no image metadata, no file over 25 MB) and publishes only `site/`. Custom domain `searenityonlummi.com`, HTTPS enforced.
- The domain is verified for the `BigLep` account in GitHub settings (Settings > Pages > Verified domains), which stops any other GitHub account from serving the domain. GitHub has no API for this, so it is done in the web UI: add the domain there, create the `TXT` record it shows in the hosted zone, then click Verify.

## Claude access for Dave

Dave uses his own claude.ai account with the Claude desktop app's Code tab, which needs a paid plan. He starts on a 7-day Pro guest pass from Steve (sent with `/passes` in Claude Code, or from Claude settings) and then subscribes himself if he keeps going.
