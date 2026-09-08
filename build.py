#!/usr/bin/env python3
"""Generates the static pages. Run: python3 build.py  →  writes *.html in this folder."""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE_DISPLAY = "602-702-6689"
PHONE_TEL = "+16027026689"
AREA = "the Phoenix metro area"
YEAR = "2026"

LOGO = """<svg viewBox="0 0 64 64" aria-hidden="true">
<defs><linearGradient id="rg{u}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9A13B"/><stop offset=".45" stop-color="#DE5F26"/><stop offset="1" stop-color="#A32A1E"/></linearGradient></defs>
<g fill="none" stroke="url(#rg{u})" stroke-width="1.6"><circle cx="32" cy="32" r="21"/><circle cx="32" cy="32" r="25.5" opacity=".55"/></g>
<g fill="url(#rg{u})"><path d="M32 2 L35 20 L32 26 L29 20 Z"/><path d="M32 62 L35 44 L32 38 L29 44 Z"/><path d="M2 32 L20 29 L26 32 L20 35 Z"/><path d="M62 32 L44 29 L38 32 L44 35 Z"/></g>
<circle cx="32" cy="32" r="17" fill="url(#rg{u})"/>
<g stroke="#FBFAF8" stroke-width="1.5" stroke-linecap="round" opacity=".95"><path d="M32 20v3"/><path d="M23.5 23.5l2 2"/><path d="M40.5 23.5l-2 2"/></g>
<path d="M17 39 q6-1 9-5 t7 4 t7-3 q3 2 7 2" fill="none" stroke="#FBFAF8" stroke-width="1.6" stroke-linecap="round" opacity=".95"/>
<path d="M15 44 q10-3 17 0 t17-1" fill="none" stroke="#FBFAF8" stroke-width="1.4" stroke-linecap="round" opacity=".8"/>
</svg>"""

def head(title, desc, path):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://REPLACE-WITH-YOUR-DOMAIN.com{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#FBFAF8">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"LocalBusiness","name":"On Time Maintenance LLC","description":"Premium property care for Arizona homes and investment properties — routine maintenance, urgent repairs, renovations, and property management.","telephone":"{PHONE_TEL}","areaServed":"Phoenix, Arizona","address":{{"@type":"PostalAddress","addressLocality":"Phoenix","addressRegion":"AZ","addressCountry":"US"}},"url":"https://REPLACE-WITH-YOUR-DOMAIN.com/"}}
</script>
</head>
<body>
"""

HEADER = f"""<header id="hdr">
  <div class="bar">
    <a class="brand" href="/" aria-label="On Time Maintenance, home">
      {LOGO.format(u='h')}
      <span><b>On Time Maintenance</b><span>Premium Property Care</span></span>
    </a>
    <div class="bar-right">
      <a class="tel" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <button class="burger" id="burger" aria-expanded="false" aria-controls="menu" aria-label="Open menu"><span><i></i><i></i><i></i></span></button>
    </div>
  </div>
</header>
<div class="scrim" id="scrim" hidden></div>
<nav class="panel" id="menu" role="dialog" aria-modal="true" aria-label="Main menu" hidden>
  <div class="panel-head"><button class="burger" id="closeBtn" aria-label="Close menu"><span><i></i><i></i><i></i></span></button></div>
  <div class="panel-nav">
    <a href="/about"><em>About Us</em><small>Who you're handing it to</small></a>
    <a href="/properties"><em>Our Properties</em><small>What we look after</small></a>
    <a href="/faq"><em>FAQ</em><small>How this works</small></a>
    <a href="/request"><em>Submit Work Request</em><small>Start a request</small></a>
    <a href="/connect"><em>Connect With Us</em><small>Call or email</small></a>
  </div>
  <div class="panel-foot">
    <a class="btn btn--primary btn--full" href="/request">Submit a work request</a>
    <a class="contact-row" href="tel:{PHONE_TEL}"><small>Call</small><b>{PHONE_DISPLAY}</b></a>
    <a class="contact-row" href="#" data-email><small>Email</small><b></b></a>
    <p class="panel-note">Serving {AREA}<br>On Time Maintenance LLC · Phoenix, Arizona</p>
  </div>
</nav>
<main id="top">
"""

FOOTER = f"""</main>
<footer id="connect-footer">
  <div class="wrap foot-grid">
    <div>
      <a class="brand" href="/" style="margin-bottom:var(--s3)">
        {LOGO.format(u='f')}
        <span><b>On Time Maintenance</b><span>Premium Property Care</span></span>
      </a>
      <p style="font-size:15px;max-width:36ch">Preventative care, fast repairs, renovations, and property management for Arizona homes and investment properties.</p>
    </div>
    <div>
      <p class="foot-label">Reach us</p>
      <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <a href="#" data-email></a>
      <a href="/request">Submit a work request</a>
    </div>
    <div>
      <p class="foot-label">Site</p>
      <a href="/about">About Us</a><a href="/properties">Our Properties</a>
      <a href="/faq">FAQ</a><a href="/connect">Connect With Us</a>
    </div>
  </div>
  <div class="wrap"><p class="foot-legal">
    Serving {AREA}<br>
    © {YEAR} On Time Maintenance LLC · <a href="/privacy">Privacy</a> · <a href="/terms">Terms</a>
  </p></div>
</footer>
<div class="sticky" id="sticky">
  <a class="btn btn--primary" href="/request">Submit request</a>
  <a class="btn btn--secondary" href="tel:{PHONE_TEL}">Call</a>
</div>
<script src="/js/site.js"></script>
</body>
</html>
"""

def page_hero(eyebrow, h1, lead=None, cls=""):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<section class="page-hero {cls}"><div class="wrap">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  {lead_html}
</div></section>
<div class="wrap"><hr class="rule"></div>
"""

CTA = f"""<div class="wrap"><hr class="rule"></div>
<section class="cta-block"><div class="wrap">
  <p class="eyebrow">Next step</p>
  <h2 class="h2-gap">Tell us what's going on.</h2>
  <p class="lead">Describe the issue in your own words. We'll come back with next steps and a timeline. Intake takes about two minutes.</p>
  <div class="hero-cta">
    <a class="btn btn--primary" href="/request">Submit a work request</a>
    <a class="btn btn--secondary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
  </div>
  <p class="mt3" style="font-size:var(--step--1)">For anything actively leaking, sparking, or flooding, call rather than submit.</p>
</div></section>
"""

# ---------------------------------------------------------------- HOME
HOME = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Premium Property Care · Arizona</p>
      <h1>Your property,<br>on a care plan.</h1>
      <p class="lead">On Time Maintenance is the standing care team for Arizona homes and investment properties — routine upkeep, urgent repairs, and full renovations, run by people who answer, show up, and tell you exactly what happened.</p>
      <div class="hero-cta">
        <a class="btn btn--primary" href="/request">Submit a work request</a>
        <a class="btn btn--secondary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>
      </div>
    </div>
    <div class="chart" aria-label="Illustrative property care record">
      <div class="chart-top"><b>Property Care Record</b><i>Example</i></div>
      <div class="legend"><b><span class="dot"></span>Current</b><b><span class="dot dot--watch"></span>Watch</b><b><span class="dot dot--due"></span>Due</b></div>
      <div class="chart-row"><span class="dot" aria-hidden="true"></span><span>Roof &amp; drainage</span><time>Current · Apr</time></div>
      <div class="chart-row"><span class="dot dot--due" aria-hidden="true"></span><span>HVAC</span><time>Due · pre-summer</time></div>
      <div class="chart-row"><span class="dot" aria-hidden="true"></span><span>Plumbing</span><time>Current · Jun</time></div>
      <div class="chart-row"><span class="dot dot--watch" aria-hidden="true"></span><span>Exterior &amp; paint</span><time>Watch · south wall</time></div>
      <div class="chart-row"><span class="dot" aria-hidden="true"></span><span>Electrical</span><time>Current · Feb</time></div>
      <div class="chart-row"><span class="dot dot--watch" aria-hidden="true"></span><span>Irrigation &amp; landscape</span><time>Watch · zone 3</time></div>
      <div class="chart-foot">Illustrative example — your record starts at intake</div>
    </div>
  </div>
</section>
<div class="wrap"><hr class="rule"></div>

<section>
  <div class="wrap split">
    <p class="eyebrow">The problem</p>
    <div class="prose">
      <h2>Most property problems aren't emergencies until nobody answers.</h2>
      <p class="mt3">A slow leak is a $200 fix in March and a $9,000 fix in July. The difference is almost never skill — it's attention. Whether you own the home you live in or a portfolio you've never walked through, the failure mode is the same: small things go unnoticed, then unreported, then unanswered.</p>
      <p>On Time Maintenance exists to close that gap. We take the whole category of <em>property stuff</em> off your desk — the inspections, the vendors, the scheduling, the follow-up, the paperwork — and hand back a clear record of what was checked, what was fixed, and what's coming next.</p>
    </div>
  </div>
</section>

<section class="sand">
  <div class="wrap">
    <p class="eyebrow">The care model</p>
    <h2 class="h2-gap">How we look after a property.</h2>
    <p class="lead">Four steps, every time, whether it's a dripping faucet or a full kitchen.</p>
    <div class="cards cards--4">
      <div class="card step"><span class="eyebrow">01 — Intake</span><p>We walk the property and build its record: age and condition of every major system, what's been done, what's overdue, what's about to be. You get the record whether or not you hire us for the work.</p></div>
      <div class="card step"><span class="eyebrow">02 — Diagnosis</span><p>We find the cause, not just the symptom. Stains get moisture-mapped. Short-cycling HVAC gets measured before anyone quotes a replacement. You get the finding in plain language, with photos, and our read on urgency.</p></div>
      <div class="card step"><span class="eyebrow">03 — Treatment</span><p>Scheduled, scoped, and priced before work starts. Licensed trades where trades are required. Site left cleaner than we found it — that isn't a slogan, it's the last item on every job checklist.</p></div>
      <div class="card step"><span class="eyebrow">04 — Follow-up</span><p>Work gets logged to the property record with photos and dates. We tell you what to watch, and we come back for the seasonal items on the calendar instead of waiting for you to remember them.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">What we handle</p>
    <h2 class="h2-gap">Routine care and major work, from the same team.</h2>
    <p class="lead">One point of contact whether it's a filter change or a full remodel — so nothing gets handed off, dropped, or explained twice.</p>
    <div class="cards cards--2">
      <div class="card"><h3>Routine maintenance</h3><p>Seasonal HVAC service, filter and fixture changes, irrigation checks, exterior and roof inspections, pest and drainage prevention, caulking and seals, water heater flushes. The unglamorous list that decides what a property costs over ten years.</p></div>
      <div class="card"><h3>Repairs &amp; urgent response</h3><p>Plumbing, electrical, drywall, doors and locks, appliance issues, roof leaks, water intrusion, damage after a monsoon. You describe it; we diagnose it; you get a timeline before we touch anything.</p></div>
      <div class="card"><h3>Renovations &amp; upgrades</h3><p>Kitchens, baths, flooring, paint, fixtures, exterior refresh, unit turns and full rehabs. Scoped in writing, sequenced on a schedule, and reported on while it's running.</p></div>
      <div class="card"><h3>Property management &amp; turnovers</h3><p>Full management for rental owners under a written agreement — leasing and marketing, tenant screening, rent collection, vendor supervision, and make-readies between tenants. Eyes on the ground for owners who aren't in Arizona.</p></div>
    </div>
    <div class="mt5"><a class="btn btn--primary" href="/request">Submit a work request</a></div>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <p class="eyebrow">Communication</p>
    <h2 class="h2-gap">The maintenance company that answers.</h2>
    <p class="lead" style="color:#B9C0C5">Fast, clear communication isn't a feature we added. It's the thing most property owners are actually shopping for, and it's the thing we organize the company around.</p>
    <div class="cards cards--3">
      <div class="card"><h3>You get a name.</h3><p>One person owns your account and your requests. Not a queue, not a rotating dispatcher, not whoever picks up.</p></div>
      <div class="card"><h3>You get a timeline.</h3><p>Every request gets acknowledged and scheduled with a window — including the ones where the honest answer is "not this week, and here's why."</p></div>
      <div class="card"><h3>You get a record.</h3><p>Photos, findings, what was done, what it cost, and what's next. In writing, every time, so you're never reconstructing history from memory.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <p class="eyebrow">The standard</p>
    <div>
      <h2>Why owners hand it off.</h2>
      <div class="points mt4">
        <p><strong>One team, whole property.</strong> No coordinating four vendors who each blame the other three.</p>
        <p><strong>Preventative by default.</strong> We're paid to keep things from breaking, not to be heroic after they do.</p>
        <p><strong>Written scope before work starts.</strong> You approve the plan and the price. No surprises on the invoice.</p>
        <p><strong>Owner-operated.</strong> On Time Maintenance is owned and run by Emilio and Aaron Alcaraz, father and son. When you call, you're talking to the people whose name is on the company.</p>
      </div>
    </div>
  </div>
</section>

<section class="sand">
  <div class="wrap">
    <p class="eyebrow">Who we care for</p>
    <h2 class="h2-gap">Homes, rentals, and portfolios.</h2>
    <div class="cards cards--3">
      <a class="card card--link" href="/properties"><h3>Homeowners</h3><p>Primary residences, second homes, and properties owned by people who'd rather not manage trades.</p></a>
      <a class="card card--link" href="/properties"><h3>Investors &amp; rentals</h3><p>Single-family rentals, small multifamily, short-term rentals, and out-of-state owners who need eyes on the ground.</p></a>
      <a class="card card--link" href="/properties"><h3>HOA &amp; commercial</h3><p>Common areas, recurring service contracts, and scheduled maintenance programs.</p></a>
    </div>
  </div>
</section>

{CTA}

<section class="sand">
  <div class="wrap split">
    <p class="eyebrow">Common questions</p>
    <div>
      <div class="acc">
        <div><button aria-expanded="false">What areas do you serve?<span class="plus"></span></button>
          <div class="body"><p>We serve {AREA}. If you're just outside it, submit a request anyway — we'll tell you straight whether we can take it on.</p></div></div>
        <div><button aria-expanded="false">Do you handle one-off jobs, or only ongoing care?<span class="plus"></span></button>
          <div class="body"><p>Both. Many clients start with a single repair and move to ongoing care once they've seen the work.</p></div></div>
        <div><button aria-expanded="false">How does pricing work?<span class="plus"></span></button>
          <div class="body"><p>Every job is scoped and quoted in writing before work begins, so you approve the plan and the price before anyone starts. Property management is billed under a written management agreement.</p></div></div>
        <div><button aria-expanded="false">What if it's an emergency?<span class="plus"></span></button>
          <div class="body"><p>Call rather than submitting a form — anything actively leaking, sparking, or flooding needs a person, not an inbox.</p></div></div>
      </div>
      <p class="mt4"><a class="inline" href="/faq">All questions</a></p>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- ABOUT
ABOUT = page_hero("About Us", "Who you're handing it to.",
  "On Time Maintenance is a Phoenix property care company owned and run by Emilio and Aaron Alcaraz. Here's what that means for you.") + f"""
<section>
  <div class="wrap split">
    <p class="eyebrow">Why we exist</p>
    <div class="prose">
      <h2>We started this because of the phone calls that never came back.</h2>
      <p class="mt3">Everyone who owns property has the same story. You call about a leak. Someone says they'll come by. They don't. You call again. The problem gets bigger, the bill gets bigger, and nobody can tell you what actually happened or what it cost.</p>
      <p>We built On Time Maintenance around the opposite experience. You hand a property to us and you get a named person, a timeline, and a written record. The name of the company is the standard we're judged against, and we chose it on purpose.</p>
      <p>We're a father-and-son company. That isn't a marketing line — it's why the standard holds. There's no franchise office, no rotating dispatcher, and no one to pass a problem to. When something isn't right, the people fixing it are the people who own the business.</p>
    </div>
  </div>
</section>

<section class="sand">
  <div class="wrap">
    <p class="eyebrow">The people</p>
    <h2 class="h2-gap">Two owners. One point of contact.</h2>
    <div class="people">
      <div class="person">
        <div class="photo" role="img" aria-label="Photo of Emilio Alcaraz coming soon">Photo coming soon</div>
        <h3>Emilio Alcaraz</h3><small>Owner</small>
        <p>Runs client relationships, intake, and scheduling. Emilio is the person you'll talk to about your property and the person accountable for the timeline you're given.</p>
      </div>
      <div class="person">
        <div class="photo" role="img" aria-label="Photo of Aaron Alcaraz coming soon">Photo coming soon</div>
        <h3>Aaron Alcaraz</h3><small>Co-owner</small>
        <p>Oversees property management and the work itself. Aaron is the named agent on OTM management agreements and the one who makes sure what was promised is what got done.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <p class="eyebrow">How we work</p>
    <div>
      <h2>The rules we hold ourselves to.</h2>
      <div class="points mt4">
        <p><strong>Every request gets a response and a window.</strong> Sometimes the answer is "not this week" — but you'll always get the answer, and the reason.</p>
        <p><strong>Scope and price in writing before work starts.</strong> You approve the plan. Changes get approved the same way. Nothing lands on an invoice that you didn't see coming.</p>
        <p><strong>Diagnosis before quotes.</strong> We find the cause before we price the fix. A stain gets moisture-mapped before anyone talks about a new roof.</p>
        <p><strong>A record for every property.</strong> Photos, findings, dates, and what's next, logged and shared with you — so the history lives somewhere other than your memory.</p>
        <p><strong>Licensed trades where the law requires them.</strong> We supervise and coordinate the specialists; you don't have to.</p>
        <p><strong>Cleaner than we found it.</strong> It's the last item on every job checklist, and it's checked every time.</p>
      </div>
    </div>
  </div>
</section>
{CTA}
"""

# ---------------------------------------------------------------- PROPERTIES
PROPERTIES = page_hero("Our Properties", "What we look after.",
  "Homes, rentals, and portfolios across the Phoenix metro area. Here's how care looks for each — and what a maintained property's record looks like over a year.") + f"""
<section>
  <div class="wrap">
    <div class="cards cards--3" style="margin-top:0">
      <div class="card"><h3>Homeowners</h3><p>Primary residences and second homes. Seasonal maintenance handled on a calendar, repairs diagnosed before they're quoted, renovations scoped in writing. For people who'd rather not be their own general contractor.</p></div>
      <div class="card"><h3>Investors &amp; rentals</h3><p>Single-family rentals, small multifamily, and short-term rentals. Full property management under a written agreement — leasing and marketing, tenant screening, rent collection with monthly owner draws, vendor supervision, emergency repairs, and turnovers between tenants. Owner approval required above an agreed repair threshold, so you stay in control without being on call.</p></div>
      <div class="card"><h3>HOA &amp; commercial</h3><p>Common areas, scheduled maintenance programs, and recurring service contracts. One accountable contact for the board or the facilities lead, with the same written scope and record-keeping as every other property we care for.</p></div>
    </div>
  </div>
</section>

<section class="sand">
  <div class="wrap hero-grid">
    <div class="prose">
      <p class="eyebrow">A year of care</p>
      <h2 class="h2-gap">What a maintained property looks like on paper.</h2>
      <p>This is an illustrative record for a single-family home in the Phoenix area. The point isn't the specific dates — it's that every system has a last-attended date, a status, and a next step, and the owner never had to remember any of it.</p>
      <p>Your record starts at intake, whether or not you hire us for the work that follows.</p>
    </div>
    <div class="chart">
      <div class="chart-top"><b>Property Care Record</b><i>Single-family · illustrative</i></div>
      <div class="legend"><b><span class="dot"></span>Current</b><b><span class="dot dot--watch"></span>Watch</b><b><span class="dot dot--due"></span>Due</b></div>
      <div class="chart-row"><span class="dot" aria-hidden="true"></span><span>HVAC — pre-summer service</span><time>Done · Apr</time></div>
      <div class="chart-row"><span class="dot" aria-hidden="true"></span><span>Roof &amp; drainage — pre-monsoon</span><time>Done · Jun</time></div>
      <div class="chart-row"><span class="dot dot--watch" aria-hidden="true"></span><span>Exterior stucco — south wall</span><time>Watch · hairline crack</time></div>
      <div class="chart-row"><span class="dot" aria-hidden="true"></span><span>Water heater — flush</span><time>Done · Feb</time></div>
      <div class="chart-row"><span class="dot dot--due" aria-hidden="true"></span><span>Irrigation — winter schedule</span><time>Due · Oct</time></div>
      <div class="chart-row"><span class="dot" aria-hidden="true"></span><span>Smoke &amp; CO detectors</span><time>Done · Jan</time></div>
      <div class="chart-foot">Illustrative example — not a client record</div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <p class="eyebrow">Recent work</p>
    <div class="prose">
      <h2>Project photos are being documented now.</h2>
      <p class="mt3">We'd rather show you three real jobs than nine padded ones. Before-and-after pairs from completed work are added here as each client signs off on sharing them. If you want to see examples relevant to your property before then, ask — we'll walk you through what we've done.</p>
    </div>
  </div>
</section>
{CTA}
"""

# ---------------------------------------------------------------- FAQ
def qa(q, a):
    return f'<div><button aria-expanded="false">{q}<span class="plus"></span></button><div class="body"><p>{a}</p></div></div>'

FAQ = page_hero("FAQ", "How this works.",
  "Plain answers to the questions we get before the first visit. If yours isn't here, call or submit a request — we answer.") + f"""
<section>
  <div class="wrap" style="max-width:860px">
    <div class="faq-group" style="margin-top:0">
      <h2>Getting started</h2>
      <div class="acc">
        {qa("What areas do you serve?", f"We serve {AREA}. If you're just outside it, submit a request anyway — we'll tell you straight whether we can take it on.")}
        {qa("How do I start?", f"Submit a work request or call {PHONE_DISPLAY}. Describe the issue in your own words; we'll come back with next steps and a timeline. For ongoing care or property management, the first step is an intake walkthrough where we build your property's record.")}
        {qa("What happens at the first visit?", "We walk the property, look at the issue you called about, and note the condition of the major systems while we're there. You get the findings in plain language with photos, and a written scope and price for anything we recommend.")}
        {qa("Do you handle one-off jobs, or only ongoing care?", "Both. Many clients start with a single repair and move to ongoing care once they've seen the work. There's no obligation either way.")}
      </div>
    </div>
    <div class="faq-group">
      <h2>Pricing &amp; scope</h2>
      <div class="acc">
        {qa("How does pricing work?", "Every job is scoped and quoted in writing before work begins. You approve the plan and the price before anyone starts, and changes get approved the same way.")}
        {qa("How is property management priced?", "Property management is billed under a written management agreement as a percentage of rent, with the full terms — owner draws, approval thresholds, and notice periods — spelled out before you sign. Ask and we'll walk you through it.")}
        {qa("What if the job turns out bigger than expected?", "We stop and tell you. You get the new finding, the revised scope, and the revised price in writing, and nothing proceeds until you approve it.")}
      </div>
    </div>
    <div class="faq-group">
      <h2>Ongoing care</h2>
      <div class="acc">
        {qa("What does ongoing care include?", "A property record built at intake, seasonal maintenance handled on a calendar (HVAC before summer, roof and drainage before monsoon, irrigation schedule changes, water heater service, detector checks), and a named contact for anything that comes up in between.")}
        {qa("Do I have to be there?", "No. Many of our clients are out of state. We coordinate access, send photos and findings after every visit, and keep the record current so you can see the property's condition without walking it.")}
      </div>
    </div>
    <div class="faq-group">
      <h2>Renovations</h2>
      <div class="acc">
        {qa("Do you do full renovations?", "Yes — kitchens, baths, flooring, paint, fixtures, exterior refresh, unit turns, and full rehabs. Every renovation is scoped in writing, sequenced on a schedule, and reported on while it's running.")}
        {qa("Who does the work?", "Our crew handles general work. Licensed trades handle what the law requires them to — electrical, plumbing, HVAC — and we supervise and coordinate them so you have one point of contact throughout.")}
        {qa("Can I stay in the house during a renovation?", "Usually, depending on scope. We'll tell you at the planning stage which phases affect which rooms, and what the daily schedule looks like, so you can decide.")}
      </div>
    </div>
    <div class="faq-group">
      <h2>Rentals &amp; out-of-state owners</h2>
      <div class="acc">
        {qa("How do you handle tenant requests?", "Tenants reach us directly for maintenance. We diagnose, handle anything under your approval threshold, and bring anything above it to you with a finding and a price before proceeding.")}
        {qa("How do I know what's going on with my property?", "Every visit is logged with photos and findings. You get the record, and for management clients, monthly reporting with your owner draw.")}
      </div>
    </div>
    <div class="faq-group">
      <h2>Emergencies</h2>
      <div class="acc">
        {qa("What if it's an emergency?", f"Call {PHONE_DISPLAY} rather than submitting a form. Anything actively leaking, sparking, or flooding needs a person, not an inbox. If there's an immediate safety hazard — gas, fire, electrical — call 911 first.")}
      </div>
    </div>
  </div>
</section>
{CTA}
"""

# ---------------------------------------------------------------- REQUEST
REQUEST = page_hero("Submit a work request", "Tell us what's going on.",
  "Describe the issue in your own words. We'll come back with next steps and a timeline. Intake takes about two minutes.") + f"""
<section style="padding-top:var(--s5)">
  <div class="wrap">
    <form class="form" id="wr" novalidate>
      <fieldset>
        <legend>Your information</legend>
        <div class="duo">
          <div class="field"><label for="name">Full name</label>
            <input id="name" name="name" type="text" autocomplete="name" required>
            <p class="err">Enter your name so we know who we're calling.</p></div>
          <div class="field"><label for="phone">Phone</label>
            <input id="phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(602) 555-0100" required>
            <p class="err">Enter a phone number we can reach you at.</p></div>
        </div>
        <div class="field"><label for="email">Email</label>
          <input id="email" name="email" type="email" inputmode="email" autocomplete="email" required>
          <p class="err">Enter an email address so we can send you a copy of this request.</p></div>
        <div class="field"><label>Preferred contact method</label>
          <div class="choices">
            <label class="choice"><input type="radio" name="contact_method" value="Call" checked><span>Call</span></label>
            <label class="choice"><input type="radio" name="contact_method" value="Text"><span>Text</span></label>
            <label class="choice"><input type="radio" name="contact_method" value="Email"><span>Email</span></label>
          </div></div>
      </fieldset>
      <fieldset>
        <legend>The property</legend>
        <div class="field"><label for="addr">Property address</label>
          <input id="addr" name="address" type="text" autocomplete="street-address" required>
          <p class="err">Enter the address where the work is needed.</p></div>
        <div class="duo">
          <div class="field"><label for="ptype">Property type</label>
            <select id="ptype" name="property_type"><option>Primary residence</option><option>Second home</option><option>Rental</option><option>Multifamily</option><option>HOA or commercial</option><option>Other</option></select></div>
          <div class="field"><label for="role">I am the…</label>
            <select id="role" name="role"><option>Owner</option><option>Property manager</option><option>Tenant</option><option>Agent or representative</option></select></div>
        </div>
        <div class="field"><label for="access">Access notes <span class="opt">— optional</span></label>
          <textarea id="access" name="access_notes" style="min-height:80px" placeholder="Gate code, dogs in the yard, tenant's number, lockbox location"></textarea></div>
      </fieldset>
      <fieldset>
        <legend>The work</legend>
        <div class="field"><label for="desc">What's going on?</label>
          <textarea id="desc" name="description" required placeholder="Water stain on the ceiling in the back bedroom, showed up after the last rain."></textarea>
          <p class="err">Tell us a little more — even one sentence helps us send the right person.</p></div>
        <div class="field"><label>Type of work <span class="opt">— optional</span></label>
          <div class="choices">
            <label class="choice"><input type="checkbox" name="work_type" value="Maintenance"><span>Maintenance</span></label>
            <label class="choice"><input type="checkbox" name="work_type" value="Repair"><span>Repair</span></label>
            <label class="choice"><input type="checkbox" name="work_type" value="Renovation"><span>Renovation</span></label>
            <label class="choice"><input type="checkbox" name="work_type" value="Turnover"><span>Turnover</span></label>
            <label class="choice"><input type="checkbox" name="work_type" value="Property management"><span>Property management</span></label>
            <label class="choice"><input type="checkbox" name="work_type" value="Not sure"><span>Not sure</span></label>
          </div></div>
        <div class="field"><label>Urgency</label>
          <div class="choices">
            <label class="choice"><input type="radio" name="urgency" value="Emergency"><span>Emergency</span></label>
            <label class="choice"><input type="radio" name="urgency" value="Soon - this week" checked><span>Soon — this week</span></label>
            <label class="choice"><input type="radio" name="urgency" value="Scheduled - no rush"><span>Scheduled — no rush</span></label>
          </div></div>
        <div class="field"><label>Best times <span class="opt">— optional</span></label>
          <div class="choices">
            <label class="choice"><input type="checkbox" name="best_times" value="Weekday morning"><span>Weekday morning</span></label>
            <label class="choice"><input type="checkbox" name="best_times" value="Weekday afternoon"><span>Weekday afternoon</span></label>
            <label class="choice"><input type="checkbox" name="best_times" value="Evening"><span>Evening</span></label>
            <label class="choice"><input type="checkbox" name="best_times" value="Weekend"><span>Weekend</span></label>
          </div></div>
        <div class="field"><label for="photos">Photos <span class="opt">— optional, up to 5</span></label>
          <input id="photos" name="photos" type="file" accept="image/*" multiple style="font-family:var(--font-body);font-size:14px;padding:12px"></div>
        <div class="field"><label for="heard">How did you hear about us? <span class="opt">— optional</span></label>
          <select id="heard" name="referral_source"><option value="">—</option><option>Referral</option><option>Search</option><option>Social</option><option>Sign or vehicle</option><option>Existing client</option><option>Other</option></select></div>
      </fieldset>
      <div class="alert" id="emg" role="alert">
        <b>Call us instead.</b>
        <p>If there's active water, fire, gas, or an electrical hazard, don't wait on a form. For an immediate safety hazard, call 911 first.</p>
        <a class="btn btn--primary" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY} now</a>
      </div>
      <div class="field">
        <label class="consent"><input type="checkbox" id="consent" name="consent" value="yes" required>
          <span>I agree to be contacted about this request by phone, text, or email. Message and data rates may apply; reply STOP to opt out of texts.</span></label>
        <p class="err">Please check this box so we're allowed to get back to you.</p>
      </div>
      <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn--primary btn--full" type="submit" id="sub">Submit work request</button>
      <p class="fail" id="fail">That didn't go through. Try again, or call {PHONE_DISPLAY} — we'll take it by phone.</p>
    </form>
    <div class="done" id="done" tabindex="-1" role="status">
      <span class="check"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l6 6L20 6"/></svg></span>
      <h2>Work request submitted.</h2>
      <p id="rid" style="font-family:var(--font-mono);font-size:13px;letter-spacing:.1em;color:var(--signal);margin-bottom:var(--s3)">Request #</p>
      <p>We've got it. You'll hear from us with next steps and a timeline.</p>
      <p class="mt3"><strong style="color:var(--ironwood)">Something urgent?</strong> Call <a href="tel:{PHONE_TEL}" style="color:var(--signal);font-weight:500">{PHONE_DISPLAY}</a>.</p>
      <p class="mt3"><a class="inline" href="/">Back to home</a></p>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- CONNECT
CONNECT = page_hero("Connect With Us", "Call, email, or send a request.",
  "Every path reaches the same two people. Pick whichever is fastest for you.") + f"""
<section style="padding-top:var(--s5)">
  <div class="wrap">
    <div class="contact-cards" style="margin-top:0">
      <a class="contact-card" href="tel:{PHONE_TEL}"><small>Call</small><b>{PHONE_DISPLAY}</b><p>Fastest for anything active or urgent.</p></a>
      <a class="contact-card" href="#" data-email><small>Email</small><b data-email></b><p>Good for documents, photos, and anything that isn't time-sensitive.</p></a>
      <a class="contact-card" href="/request"><small>Work request</small><b>Submit online</b><p>Two-minute intake form. You get a request number and we get everything we need to respond.</p></a>
    </div>
  </div>
</section>
<section class="sand">
  <div class="wrap split">
    <p class="eyebrow">Where we work</p>
    <div class="prose">
      <h2>Serving {AREA}.</h2>
      <p class="mt3">On Time Maintenance LLC is based in Phoenix, Arizona. If your property is just outside the metro, reach out anyway — we'll tell you straight whether we can take it on.</p>
      <p><strong>Emergencies:</strong> call rather than email. For an immediate safety hazard — gas, fire, electrical — call 911 first.</p>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- LEGAL
PRIVACY = page_hero("Privacy", "Privacy policy.", f"Last updated September {YEAR}.") + f"""
<section><div class="wrap prose" style="max-width:760px">
<h3 style="margin-top:0">What we collect</h3>
<p>When you submit a work request or contact us, we collect what you give us: your name, phone number, email address, property address, a description of the work, any photos you attach, and your contact preferences. Our website may also collect standard technical information such as your browser type and pages visited.</p>
<h3>How we use it</h3>
<p>We use this information to respond to your request, schedule and perform work, keep a record of the property's care, and send you copies of your requests and updates about them. If you agreed to be contacted by text, we may text you about your request; reply STOP at any time to opt out.</p>
<h3>Who we share it with</h3>
<p>We share your information only as needed to do the work — for example, with licensed trades we coordinate on your property — and with the service providers that run our website and form processing. We do not sell your information.</p>
<h3>How long we keep it</h3>
<p>We keep property records for as long as we care for the property and for a reasonable period afterward for our business and legal records.</p>
<h3>Your choices</h3>
<p>You can ask us to update or delete your information, or to stop contacting you, by calling {PHONE_DISPLAY} or emailing <a class="inline" href="#" data-email></a>.</p>
<h3>Contact</h3>
<p>On Time Maintenance LLC, Phoenix, Arizona · {PHONE_DISPLAY}</p>
</div></section>
"""

TERMS = page_hero("Terms", "Terms of use.", f"Last updated September {YEAR}.") + f"""
<section><div class="wrap prose" style="max-width:760px">
<h3 style="margin-top:0">This website</h3>
<p>This website is operated by On Time Maintenance LLC ("OTM"). By using it you agree to these terms. Content on the site is for general information and does not create a contract for services.</p>
<h3>Requests and quotes</h3>
<p>Submitting a work request asks OTM to contact you about the work described. It is not a booking, and it does not obligate OTM to perform the work. Services are provided only under a written scope, quote, or management agreement approved by you.</p>
<h3>Illustrative content</h3>
<p>Property care records shown on this site are illustrative examples and do not represent actual client properties or work performed.</p>
<h3>No guarantees from the website</h3>
<p>OTM makes reasonable efforts to keep site content accurate but does not guarantee it is complete or current. Warranties, response commitments, and service terms are set out in your written agreement with OTM, not on this site.</p>
<h3>Contact</h3>
<p>Questions about these terms: {PHONE_DISPLAY} or <a class="inline" href="#" data-email></a>.</p>
</div></section>
"""

NOTFOUND = page_hero("404", "That page isn't here.", "The address may be out of date. Everything on the site is one tap away below.") + f"""
<section style="padding-top:var(--s4)"><div class="wrap">
  <div class="hero-cta">
    <a class="btn btn--primary" href="/request">Submit a work request</a>
    <a class="btn btn--secondary" href="/">Back to home</a>
  </div>
</div></section>
"""

PAGES = {
  "index.html":      ("On Time Maintenance — Premium Property Care in Phoenix, Arizona", "Preventative maintenance, fast repairs, renovations, and property management for Arizona homes and investment properties. The maintenance company that answers.", "/", HOME),
  "about.html":      ("About Us — On Time Maintenance", "On Time Maintenance is a Phoenix property care company owned and run by Emilio and Aaron Alcaraz.", "/about", ABOUT),
  "properties.html": ("Our Properties — On Time Maintenance", "Homes, rentals, HOA and commercial properties across the Phoenix metro, cared for on a plan with a written record.", "/properties", PROPERTIES),
  "faq.html":        ("FAQ — On Time Maintenance", "Plain answers on service area, pricing, ongoing care, renovations, rentals, and emergencies.", "/faq", FAQ),
  "request.html":    ("Submit a Work Request — On Time Maintenance", "Describe the issue in your own words and get next steps and a timeline. Two-minute intake.", "/request", REQUEST),
  "connect.html":    ("Connect With Us — On Time Maintenance", "Call, email, or submit a work request. Serving the Phoenix metro area.", "/connect", CONNECT),
  "privacy.html":    ("Privacy — On Time Maintenance", "How On Time Maintenance collects and uses your information.", "/privacy", PRIVACY),
  "terms.html":      ("Terms — On Time Maintenance", "Terms of use for the On Time Maintenance website.", "/terms", TERMS),
  "404.html":        ("Page not found — On Time Maintenance", "That page isn't here.", "/404", NOTFOUND),
}

for fname, (title, desc, path, body) in PAGES.items():
    with open(os.path.join(ROOT, fname), "w") as f:
        f.write(head(title, desc, path) + HEADER + body + FOOTER)
    print("wrote", fname)
