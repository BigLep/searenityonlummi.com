# Site plan

What Dave wants searenityonlummi.com to be, gathered by interviewing him. Update this as decisions are made.

## Scope

- The site is about **Searenity on Lummi**, a property on Lummi Island, Washington, co-owned by Dave, his sisters Trish and Verna, and his wife Sharon.
- The property is where friends and family gather: weekends, holidays, Thanksgiving, and many other occasions.
- **Migley** is the adjoining property, owned by Dave and Sharon. The new septic system serves both Searenity and Migley (confirmed by Dave).
- Planned sections:
  1. **Calendar**
  2. **Favorite pictures**
  3. **Property logistics**
  4. **Projects**: the new septic system is the first. More to come, such as a fence and a beach trail.

## Audience

- Mainly friends and family who come to the property. Tone can be warm and personal; projects told as stories more than technical manuals.

## Calendar

- The family already keeps a Google Calendar of scheduled activity at Searenity.
- **Decision:** the Calendar page links to the private Google Calendar rather than embedding it. Only people it is shared with in Google can see it; strangers get "no access". The calendar stays private (making it public would show when the house is empty).
- Needed when building: the calendar's link from Dave. Its ID may contain an email address, which would then be public; check with Dave before publishing.

## Property logistics

- A map of how to get there.
- Light and heat instructions.
- Garbage instructions.
- How to leave the place (closing-up checklist).
- Keep off the public site: door or lockbox codes, Wi-Fi passwords, alarm details.
- **Map decision:** show only the route to the Lummi Island ferry and the general area of the island. Do not pin the house or publish the street address; family share the final directions privately.

## Favorite pictures

- Dave's idea: a place where family and friends can post their favourite pictures of their time at Searenity.
- The site is static (GitHub Pages), so visitors cannot upload to it directly.
- **Decision:** a shared Google Photos album (for example "Searenity Favourites") where anyone with the link can add photos. Dave shares the album link privately by text or email; it does not go on the public site, since anyone with it can view and add. From time to time Dave picks favourites and Claude adds them to a gallery page on the site (resized, metadata stripped, with alt text).

## Look and layout

- **Decision (approved by Dave):** a welcoming home page with a big photo of Searenity, a short welcome line, and four large tiles that open their own pages. Project pages are told as scrolling photo stories, one photo and a few lines at a time, with videos along the way.
- Home page photo: `originals/Searenity Home Page .heic` (lawn running down to the water, the big fir, the rock islet offshore).
- Colours: keep the sand and sea blue-grey of the original placeholder page (Dave did not ask for a change; revisit if he does).
- Works on phones first, since links will often arrive by text.

## Page outline

| Page | File | Contents |
| --- | --- | --- |
| Home | `site/index.html` | Photo, welcome line, four tiles |
| Calendar | `site/calendar.html` | Short note and a button to the private Google Calendar |
| Favorite Pictures | `site/pictures.html` | Gallery of Dave's picks from the shared album; how to add yours (ask Dave for the album link) |
| Getting Here and Staying | `site/staying.html` | Getting there (route to the ferry), lights and heat, garbage, leaving the place |
| Projects | `site/projects.html` | One card per project: septic first, fence and beach trail later |
| Septic project | `site/projects/septic.html` | Scrolling photo story from the PDF, photos, and videos (once the material arrives) |

## Source material

- In `originals/`: the septic writeup as a Pages document and a 29-page PDF ("Searenity and Migley New Septic - 2024 to 2026"), 77 original photos (iPhone HEIC and JPEG, plus 4 drone stills named `dji_fly_…`), and 10 videos.
- Videos (length, size): IMG_9308 14s 51 MB; IMG_3782 15s 81 MB; IMG_3775 18s 96 MB; IMG_9322 36s 159 MB; IMG_9396 40s 161 MB; IMG_4245 44s 177 MB; IMG_9409 53s 186 MB; IMG_4243 57s 192 MB; IMG_4244 88s 417 MB; drone video 101s 1.2 GB. All are over the 25 MB limit as they are.
- The PDF links to its 10 videos in a shared Google Photos album (plus one link to glendon.com).

## Septic story outline (proposed, awaiting Dave's OK)

Follows the PDF's own steps, in Dave's words, lightly edited for the web:

1. **Why a new septic?** Old non-conforming systems, the 150 ft shoreline setback, Searenity entirely inside it, a small corner of Migley outside it.
2. **The design (Summer 2024).** Engineer Mike Eaton of On Site Septic; one shared 7-bedroom system on Migley; soil tests lead to a Glendon bio-filter; the well-setback variance and the easement.
3. **Clearing the trees (Fall 2025).** Dan Dittrich and his son Robin; twelve trees; five videos.
4. **The build begins.** Rich and Britta Hudson of Island Excavation; Baker Septic pumps out the old tanks.
5. **Searenity's new tank.** The three-vault combo tank, the crane, the lid, Sharon "testing the system", the control box, and the kitchen-sink mystery.
6. **Migley's new tank.** Delivery and install videos; the three old pipes.
7. **The dosing pump tank.** The system's "capacitor": two 1,250-gallon tanks working as one.
8. **Connecting it all, and power.** Trenches, lines, and the alarm panel on the Migley garage.
9. **Building the bio-filters.** Layer by layer: frame, sand, liner, Glendon pellets, netting, gravel, sand, straw blanket.
10. **Finishing up.** New fence, the lids, the drone views, and the drone video.
11. **Conclusion.** "All this for 2 toilets!"

## Open questions

- Videos: link to the existing Google Photos album, or upload to unlisted YouTube so they play on the page? Linking makes that album viewable by anyone who finds the page.
- PDF page 1 (property map) and page 4 (design drawing) look like they come from the survey or permit and may show parcel details. Proposed: leave them out and draw a simple diagram instead.
- Drone photos and video show the houses from above, and parts of neighbouring properties. OK to use?
- Sharon is named and shown in the writeup (and videos). OK on the public site?
- The writeup mentions the possible future "Fellow-Shop Hall" on Migley. OK to mention publicly?

## Privacy

Everything on the site and in this repo is public. Decisions so far:

- No street address, house number, or map pin on the house.
- No door or lockbox codes, Wi-Fi passwords, or alarm details.
- The Google Calendar and the shared photo album links are shared privately, not on the site.
- Contractors and suppliers **can be named**.
- **No permit or inspection documents** (they show the address and parcel number). Also check photos for visible permit cards or signs.
- **No costs.** Leave prices, quotes, and invoices out of text and crop them out of photos.
- **Gallery: faces are fine, no names.** Captions describe the moment ("Thanksgiving 2025 on the deck"), never who is in the photo. Alt text likewise describes people generically.
- Neighbours' houses or people visible in photos: Claude flags these when going through photos, and Dave decides whether to crop or skip.
