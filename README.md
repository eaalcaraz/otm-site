# On Time Maintenance — website

Static site. No build step required to deploy — the HTML is already generated.
(`build.py` regenerates the pages from one template if you edit copy; run `python3 build.py`.)

## Go live in 5 steps (about 30 minutes)

1. **Form backend (5 min).** Go to formspree.io → New form → name it "OTM work requests" →
   set the notification email to the address you check. Copy the endpoint
   (looks like `https://formspree.io/f/abcdwxyz`). Paste it into `js/site.js`, line 3.
   Free tier handles 50 submissions/month; upgrade when you outgrow it.
   Every submission arrives with a subject like `Work request OTM-0908-4821 — Jane Doe`;
   emergencies are prefixed `EMERGENCY —`.

2. **Email address (1 min).** `js/site.js`, line 4. Set it to an address you actually own.
   ontime.com is not yours; do not launch with emilio@ontime.com.

3. **Domain (10 min).** Buy one at Cloudflare, Porkbun, or Namecheap. Then find-and-replace
   `REPLACE-WITH-YOUR-DOMAIN.com` across the folder (it appears in `build.py`, `robots.txt`,
   `sitemap.xml`, and the generated HTML — easiest: edit `build.py`, `robots.txt`, `sitemap.xml`,
   then run `python3 build.py`).

4. **Deploy (5 min).** Push this folder to a GitHub repo → vercel.com → Add New Project →
   import the repo → Framework preset: "Other" → Deploy. `vercel.json` already handles
   clean URLs (`/about` not `/about.html`), the 404 page, and security headers.

5. **Connect the domain (5 min).** In the Vercel project → Settings → Domains → add your
   domain → follow the DNS instructions at your registrar. SSL is automatic.

Then: submit one real test request from your phone and confirm the email arrives.

## Things to add as you have them

- **Photos.** `about.html` has two "Photo coming soon" placeholders. Replace each
  `<div class="photo">` with `<img src="/img/emilio.jpg" alt="Emilio Alcaraz" class="photo">`.
- **Projects.** `properties.html` → "Recent work" section. Add before/after pairs once clients
  have signed off on sharing.
- **ROC / insurance.** Deliberately omitted. Add a line to the About page and footer only
  once the number and carrier are documented.
- **Response commitment.** The site describes responsiveness without a number. If you decide
  on a window you can hit 100% of the time ("every request acknowledged same business day"),
  it belongs in the Communication section on the homepage and in the form confirmation.
- **Analytics.** Add Vercel Analytics (one click in the project dashboard) or paste a
  Google Analytics tag into `head()` in `build.py`.
- **Google Business Profile.** Claim it and link this site — it's where most local
  property-care searches actually convert.

## Legal

`privacy.html` and `terms.html` are plain-language drafts covering form data, photos, and SMS
consent. Have someone qualified read them before you rely on them.

## Structure

```
index.html  about.html  properties.html  faq.html  request.html  connect.html
privacy.html  terms.html  404.html
css/site.css   js/site.js   favicon.svg   robots.txt   sitemap.xml   vercel.json
build.py       ← single source of truth for header/footer/copy
```
