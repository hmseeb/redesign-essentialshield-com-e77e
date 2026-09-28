#!/usr/bin/env python3
"""Compose the static Essential Shield pages from a shared shell + page bodies.

Run:  python3 tools/build_pages.py
Output: services.html, products.html, faq.html, contact.html, quote.html,
        policies.html  (index.html is hand-maintained)
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEAD = """<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="Essential Shield">
<meta name="theme-color" content="#0d2a20">
<link rel="canonical" href="https://www.essentialshield.com/{slug}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/Essential+Shield+Mould+Removal+-+Australia+%281%29+%281%29-1920w.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/favicon.svg">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar">
  <div class="wrap topbar__inner">
    <p style="margin:0">17 years servicing the Queensland community &mdash; naturally.</p>
    <ul class="topbar__list" style="list-style:none;margin:0;padding:0">
      <li><a href="tel:0411750250">0411&nbsp;750&nbsp;250</a></li>
      <li><a href="mailto:naturally@essentialshield.com">naturally@essentialshield.com</a></li>
    </ul>
  </div>
</div>

<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="index.html" aria-label="Essential Shield home">
      <img src="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/ES+logo-132w.png" alt="Essential Shield logo — green and grey shield">
      <span class="brand__text">
        <span class="brand__name">Essential Shield</span>
        <span class="brand__tag">Naturally Clean</span>
      </span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Toggle navigation menu"><span></span></button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
      <ul class="nav__list">
        <li><a href="index.html"{a_home}>Home</a></li>
        <li><a href="services.html"{a_services}>Services</a></li>
        <li><a href="products.html"{a_products}>Store</a></li>
        <li><a href="faq.html"{a_faq}>FAQs</a></li>
        <li><a href="contact.html"{a_contact}>Contact</a></li>
      </ul>
      <a class="btn btn--primary" href="quote.html">Get a Quote</a>
    </nav>
  </div>
</header>

<main id="main">

  <section class="page-hero">
    <div class="wrap">
      <p class="crumbs"><a href="index.html">Home</a><span>/</span>{crumb}</p>
      <h1>{h1}</h1>
      <p>{intro}</p>
    </div>
  </section>
"""

FOOT = """
  <section class="section--tight">
    <div class="wrap">
      <div class="cta-band">
        <div>
          <h2>Ready for a healthier, mould-free home?</h2>
          <p>Talk to the Essential Shield team about a natural treatment plan that suits your property and your budget.</p>
        </div>
        <div class="btn-row">
          <a class="btn btn--primary" href="quote.html">Get a Quote</a>
          <a class="btn btn--ghost" href="tel:0411750250">Call 0411 750 250</a>
        </div>
      </div>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/ES+logo-132w.png" alt="Essential Shield logo">
        <p>100% natural mould remediation, restoration and cleaning &mdash; 17 years servicing the Queensland community.</p>
        <p style="margin-bottom:0"><strong style="color:#fff">ABN:</strong> 84683314566</p>
        <div class="socials">
          <a href="https://facebook.com/Essentialshield" aria-label="Essential Shield on Facebook" rel="noopener" target="_blank"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.1h-3.1V8.9c0-.9.25-1.5 1.55-1.5H16.7V4.6c-.3 0-1.3-.1-2.45-.1-2.4 0-4.05 1.5-4.05 4.2v2.2H7.5V14h2.7v8h3.3z"/></svg></a>
          <a href="https://twitter.com/EssentialShield" aria-label="Essential Shield on X (Twitter)" rel="noopener" target="_blank"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.5 3h3l-6.6 7.5L21.8 21h-5.9l-4.3-5.6L6.4 21H3.3l7-8L2.6 3h6l3.9 5.2L17.5 3zm-1.1 16.1h1.7L7.7 4.8H5.9l10.5 14.3z"/></svg></a>
          <a href="https://instagram.com/essentialshield" aria-label="Essential Shield on Instagram" rel="noopener" target="_blank"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.06 1.8.25 2.2.42.6.22 1 .48 1.4.9.43.42.7.82.92 1.4.17.42.36 1.04.42 2.2.06 1.3.07 1.7.07 4.9s0 3.6-.07 4.9c-.06 1.2-.25 1.8-.42 2.2-.22.6-.5 1-.92 1.4-.42.43-.8.7-1.4.92-.42.17-1 .36-2.2.42-1.3.06-1.7.07-4.9.07s-3.6 0-4.9-.07c-1.2-.06-1.8-.25-2.2-.42-.6-.22-1-.5-1.4-.92-.43-.42-.7-.8-.92-1.4-.17-.42-.36-1-.42-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.07-4.9c.06-1.2.25-1.8.42-2.2.22-.6.5-1 .92-1.4.42-.43.8-.7 1.4-.92.42-.17 1-.36 2.2-.42C8.4 2.2 8.8 2.2 12 2.2zm0 3.2A6.6 6.6 0 1 0 18.6 12 6.6 6.6 0 0 0 12 5.4zm0 10.9A4.3 4.3 0 1 1 16.3 12 4.3 4.3 0 0 1 12 16.3zm6.9-11.1a1.55 1.55 0 1 1-1.55-1.55A1.55 1.55 0 0 1 18.9 5.2z"/></svg></a>
          <a href="https://youtube.com/essentialshield" aria-label="Essential Shield on YouTube" rel="noopener" target="_blank"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.76-1.77C18.25 5 12 5 12 5s-6.25 0-7.84.43A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.76 1.77C5.75 19 12 19 12 19s6.25 0 7.84-.43a2.5 2.5 0 0 0 1.76-1.77A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8zM10 15.1V8.9l5.2 3.1z"/></svg></a>
          <a href="https://wa.me/0411750250" aria-label="Message Essential Shield on WhatsApp" rel="noopener" target="_blank"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.4 14.1c-.23.64-1.34 1.25-1.85 1.29-.5.05-.95.23-3.2-.67-2.7-1.06-4.4-3.8-4.5-4-.14-.2-1.08-1.44-1.08-2.74s.68-1.94.92-2.2a1 1 0 0 1 .7-.33h.5c.16 0 .38-.06.59.45l.8 1.95c.07.14.11.3.02.48l-.3.46-.44.48c-.14.14-.29.3-.12.58.16.28.73 1.2 1.57 1.95 1.08.96 2 1.26 2.27 1.4.28.14.44.12.6-.07l.87-1c.2-.25.38-.2.63-.11l1.8.85c.25.12.42.18.48.28.06.1.06.6-.17 1.24z"/></svg></a>
        </div>
      </div>

      <div>
        <h4>Menu</h4>
        <ul class="footer__list">
          <li><a href="index.html">Home</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="products.html">Store</a></li>
          <li><a href="faq.html">FAQs</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="quote.html">Get a Quote</a></li>
        </ul>
      </div>

      <div>
        <h4>Our Services</h4>
        <ul class="footer__list">
          <li><a href="services.html#mould">Mould Remediation</a></li>
          <li><a href="services.html#restoration">Restoration</a></li>
          <li><a href="services.html#cleaning">Cleaning</a></li>
          <li><a href="services.html#pressure">Pressure Washing</a></li>
          <li><a href="products.html#stockists">Stockists</a></li>
        </ul>
      </div>

      <div>
        <h4>Contact Us</h4>
        <ul class="footer__list">
          <li><a href="tel:+61411750250">0411 750 250</a></li>
          <li><a href="mailto:naturally@essentialshield.com">naturally@essentialshield.com</a></li>
          <li>Servicing Queensland, Australia</li>
          <li>Mon&ndash;Fri, 9:00 am &ndash; 5:00 pm</li>
          <li>Australian shipping only &mdash; free over $100.00</li>
        </ul>

        <h4 style="margin-top:1.6rem">Natural cleaning tips</h4>
        <form class="newsletter-form" method="POST" action="https://vision.leadrai.com/api/forms/4dfea5213f838b89b8fd940221481367" data-leadr novalidate>
          <div class="form-status" aria-live="polite"></div>
          <input type="hidden" name="_form" value="Newsletter">
          <input type="hidden" name="_page" value="">
          <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none">
          <label for="nl-email-{key}" style="font-size:.86rem">Get seasonal mould prevention advice by email.</label>
          <div class="newsletter">
            <input id="nl-email-{key}" type="email" name="email" placeholder="you@example.com" autocomplete="email" required>
            <button class="btn btn--primary" type="submit">Subscribe</button>
          </div>
        </form>
      </div>
    </div>

    <div class="footer__bottom">
      <p style="margin:0">Essential Shield &mdash; All Rights Reserved &copy; <span data-year>2026</span></p>
      <div class="footer__legal">
        <a href="policies.html#terms">Terms &amp; Conditions</a>
        <a href="policies.html#privacy">Privacy Policy</a>
        <a href="policies.html#shipping">Shipping &amp; Payment</a>
        <a href="policies.html#returns">Return Policy</a>
      </div>
      <img src="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/Payment-4553da06-408w.png" alt="Accepted payments: Visa, Mastercard, American Express, Discover, PayPal and Klarna" loading="lazy">
    </div>
  </div>
</footer>

<div class="callbar">
  <a class="btn btn--dark" href="tel:0411750250">Call now</a>
  <a class="btn btn--primary" href="quote.html">Get a Quote</a>
</div>

<script src="assets/js/main.js"></script>
</body>
</html>
"""


def shell(page, body):
    active = {k: "" for k in ("home", "services", "products", "faq", "contact")}
    if page["key"] in active:
        active[page["key"]] = ' aria-current="page"'
    head = HEAD.format(
        title=page["title"],
        description=page["description"],
        slug=page["slug"],
        crumb=page["crumb"],
        h1=page["h1"],
        intro=page["intro"],
        a_home=active["home"],
        a_services=active["services"],
        a_products=active["products"],
        a_faq=active["faq"],
        a_contact=active["contact"],
    )
    return head + body + FOOT.format(key=page["key"])


# --------------------------------------------------------------- services ---
SERVICES_BODY = """
  <section class="section">
    <div class="wrap">
      <div class="grid grid--3">
        <article class="card reveal">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg></span>
          <h3>Mould Remediation</h3>
          <p>Our 100% natural 4 step process treats mould on ceilings, walls, bathrooms, wardrobes and soft furnishings &mdash; then leaves a protective essential oil barrier.</p>
          <a class="card__link" href="#mould">See the detail</a>
        </article>
        <article class="card reveal">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5S6 9.3 6 13.5a6 6 0 0 0 12 0C18 9.3 12 2.5 12 2.5z"/><path d="M9.5 14a2.5 2.5 0 0 0 2.5 2.5"/></svg></span>
          <h3>Restoration</h3>
          <p>Structural drying and complete reconstruction after a flood, storm or burst pipe &mdash; stopping the damage cycle before mould takes hold.</p>
          <a class="card__link" href="#restoration">See the detail</a>
        </article>
        <article class="card reveal">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3l7 7-9 9H5v-7l9-9z"/><path d="M11 6l7 7"/><path d="M3 21h18"/></svg></span>
          <h3>Cleaning</h3>
          <p>Bond and end of lease cleans, plus pressure washing for driveways, patios and exteriors &mdash; all with natural, family-safe products.</p>
          <a class="card__link" href="#cleaning">See the detail</a>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--sand" id="mould">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Service 01</p>
        <h2>Mould Remediation</h2>
        <p class="lead">Protect your health with our 100% Natural Mould Remediation 4 Step process. Mould thrives in warm, humid and moist environments &mdash; exactly the Queensland climate &mdash; so we treat both the growth and the conditions that feed it.</p>
        <ul class="ticks">
          <li><strong>Inspect</strong> &mdash; identify affected areas and the moisture source behind them.</li>
          <li><strong>Treat</strong> &mdash; apply our blend of five therapeutic-grade essential oils.</li>
          <li><strong>Clean</strong> &mdash; lift residue and staining with a coconut-derived cleaning agent.</li>
          <li><strong>Protect</strong> &mdash; leave an essential oil barrier that helps retard the return of mould.</li>
        </ul>
        <p>Bleach and chlorine do not kill mould &mdash; they simply bleach it so it cannot be seen. Clove oil only impacts about 10% of mould species, which is why we use five oils to cover a far wider spectrum of the 8,500+ species known today.</p>
        <div class="btn-row">
          <a class="btn btn--primary" href="quote.html">Get a mould quote</a>
          <a class="btn btn--ghost" href="tel:0411750250">Call 0411 750 250</a>
        </div>
      </div>
      <div>
        <figure class="ba" data-ba style="margin:0">
          <img src="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/Essential+Shield+Mould+Removal+-+Australia+%282%29+%281%29-1920w.jpg" alt="Before treatment: heavy mould and water staining on a ceiling treated by Essential Shield">
          <img class="ba__after" src="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/Essential+Shield+Mould+Removal+-+Australia+%281%29+%281%29-1920w.jpg" alt="After treatment: the same ceiling clean and mould free following natural mould remediation">
          <span class="ba__tag ba__tag--before">Before</span>
          <span class="ba__tag ba__tag--after">After</span>
          <span class="ba__handle" aria-hidden="true"></span>
          <span class="ba__arrows" aria-hidden="true">&#9664; &#9654;</span>
          <input class="ba__range" type="range" min="0" max="100" value="50" aria-label="Drag to compare the ceiling before and after mould remediation">
        </figure>
      </div>
    </div>
  </section>

  <section class="section" id="restoration">
    <div class="wrap">
      <div class="split">
        <div>
          <p class="eyebrow">Service 02</p>
          <h2>Water Damage Restoration</h2>
          <p class="lead">Stop the damage cycle by scheduling structural drying and complete reconstruction to fully recover your property after a flood or leak.</p>
          <p>Water that sits inside cavities, carpet underlay and plasterboard becomes a mould problem within days. We dry the structure properly, then rebuild what cannot be saved &mdash; finishing with a natural mould treatment so the repaired areas stay healthy.</p>
        </div>
        <div>
          <div class="grid grid--2">
            <article class="card card--num reveal"><span class="num" aria-hidden="true">01</span><h3>Make safe</h3><p>Rapid response to contain the water and protect what can still be saved.</p></article>
            <article class="card card--num reveal"><span class="num" aria-hidden="true">02</span><h3>Structural drying</h3><p>Controlled drying of floors, walls and cavities so moisture does not stay trapped.</p></article>
            <article class="card card--num reveal"><span class="num" aria-hidden="true">03</span><h3>Reconstruction</h3><p>Complete repairs and reinstatement of damaged surfaces and fittings.</p></article>
            <article class="card card--num reveal"><span class="num" aria-hidden="true">04</span><h3>Natural treatment</h3><p>A final essential-oil treatment to guard the restored areas against mould.</p></article>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--forest" id="cleaning">
    <div class="wrap">
      <p class="eyebrow">Service 03</p>
      <h2>Cleaning &amp; Pressure Washing</h2>
      <p class="lead measure">Natural products, meticulous work &mdash; whether you are handing back keys or bringing an exterior back to life.</p>
      <div class="grid grid--2" style="margin-top:2.25rem">
        <article class="card reveal" id="pressure">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><path d="M6 20V9l7-5 5 4v12"/><path d="M10 20v-5h4v5"/></svg></span>
          <h3>Pressure Washing</h3>
          <p>Restore the curb appeal and value of your property by safely eliminating tough dirt, algae, and grime from driveways, patios, and house exteriors.</p>
          <ul class="ticks" style="margin-top:1rem;margin-bottom:0">
            <li>Driveways, paths and patios</li>
            <li>House exteriors, eaves and fencing</li>
            <li>Roofs, shade sails and outdoor living areas</li>
          </ul>
        </article>
        <article class="card reveal">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7H4a1 1 0 0 1-1-1V4h18v2a1 1 0 0 1-1 1z"/><path d="M5 7v13h14V7"/><path d="M9 11h6"/></svg></span>
          <h3>Bond &amp; End of Lease Cleans</h3>
          <p>Guarantee your full security bond return with a detailed, agent-approved clean that covers every requirement of your tenancy agreement.</p>
          <ul class="ticks" style="margin-top:1rem;margin-bottom:0">
            <li>Kitchens, ovens, range hoods and cupboards</li>
            <li>Bathrooms, tiles, grout and mould-prone wet areas</li>
            <li>Walls, skirtings, windows, tracks and fly screens</li>
          </ul>
        </article>
      </div>
      <div class="btn-row" style="margin-top:2.25rem">
        <a class="btn btn--primary" href="quote.html">Request a cleaning quote</a>
        <a class="btn btn--ghost" href="products.html">Shop our natural products</a>
      </div>
    </div>
  </section>
"""

# --------------------------------------------------------------- products ---
PRODUCTS = [
    ("Mr Mould Natural Mould Killer 750ml", "Mould killer",
     "The signature ready-to-use spray. Five therapeutic-grade essential oils plus a coconut-derived cleaner that leaves a moisture barrier to help retard the return of mould."),
    ("Mr Mould Combo", "Mould killer",
     "The Mr Mould pack that pairs the ready-to-use spray with a refill so you can treat the whole property and top up later."),
    ("Mr Mould 2 Litre Refill", "Refill",
     "A 2 litre refill of Mr Mould for households treating larger or recurring mould-prone areas."),
    ("Naturamax 750ml", "Everyday clean",
     "Naturamax harnesses the full cleaning potential of Mr Mould while using half the essential oils &mdash; made to thoroughly clean and sanitise."),
    ("Naturamax Combo", "Everyday clean",
     "The Naturamax value pack for whole-of-home natural cleaning, indoors and out."),
    ("Naturamax 2 Litre Refill", "Refill",
     "Keep your Naturamax spray bottles topped up with a 2 litre refill &mdash; less packaging, better value."),
    ("Naturamax 2 Litre Super Concentrate", "Concentrate",
     "A super concentrate for high-use households, trades and stockists who dilute to suit the job."),
    ("Mr Mould Odour Blocks", "Odour control",
     "Natural odour blocks that keep wardrobes, bathrooms, boats and caravans smelling fresh between cleans."),
    ("Mr Mould Odour Combo", "Odour control",
     "The odour control pack &mdash; ideal for caravans, campervans, boats and closed-up holiday homes."),
    ("Premium Essential Oils &mdash; 10ml", "Essential oils",
     "Premium 10ml therapeutic-grade essential oils from the same family of oils we use in our professional treatments."),
]


def products_body():
    cards = []
    for name, tag, desc in PRODUCTS:
        alt = " product__tag--alt" if tag in ("Refill", "Concentrate") else ""
        cards.append(
            '        <article class="product reveal">\n'
            '          <span class="product__tag{alt}">{tag}</span>\n'
            '          <h3>{name}</h3>\n'
            '          <p>{desc}</p>\n'
            '          <a class="card__link" href="contact.html">Enquire or order</a>\n'
            '        </article>'.format(alt=alt, tag=tag, name=name, desc=desc)
        )
    return """
  <section class="section">
    <div class="wrap split split--narrow">
      <div class="split__media reveal" style="background:#fff">
        <img src="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/Essential+shield+product+group+shot-1077w.png" alt="The full Mr Mould and Naturamax natural cleaning range from Essential Shield" loading="lazy">
      </div>
      <div>
        <p class="eyebrow">Mr Mould &amp; Naturamax</p>
        <h2>Order our natural cleaning products for a healthier home</h2>
        <p class="lead">The quality of the air we breathe and the cleanliness of our homes are of utmost importance for our health and wellbeing. With that in mind, it&rsquo;s time to consider making the switch to natural cleaning products like the Mr Mould or Naturamax range.</p>
        <p>Use Mr Mould or Naturamax on your property, boats, caravans, campervans, canvas, shade sails, and any other indoor or outdoor surface for a powerful and effective cleaning solution.</p>
        <ul class="ticks">
          <li>Safe for children and pets &mdash; no bleach, no chlorine</li>
          <li>Australian shipping only &mdash; free shipping on orders over $100.00</li>
          <li>Pay with Visa, Mastercard, American Express, Discover, PayPal or Klarna</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="wrap">
      <div class="center" style="margin-bottom:2.5rem">
        <p class="eyebrow">All products</p>
        <h2>The full natural range</h2>
        <p class="lead measure">Every product is built around the same idea: real cleaning power from natural ingredients, with nothing in your home you would not want your family breathing.</p>
      </div>
      <div class="grid grid--3">
{cards}
      </div>
      <p class="center" style="margin-top:2.5rem"><a class="btn btn--primary" href="contact.html">Enquire about pricing &amp; orders</a></p>
    </div>
  </section>

  <section class="section" id="stockists">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Stockists</p>
        <h2>Find Mr Mould &amp; Naturamax near you</h2>
        <p class="lead">Our natural range is carried by stockists across Queensland as well as shipped direct from us. If you would like to buy locally &mdash; or stock Mr Mould and Naturamax in your own store &mdash; get in touch and we will point you to the nearest option.</p>
        <div class="btn-row">
          <a class="btn btn--dark" href="contact.html">Ask about stockists</a>
          <a class="btn btn--ghost" href="tel:0411750250">Call 0411 750 250</a>
        </div>
      </div>
      <div class="grid" style="gap:.9rem">
        <div class="info-tile">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18l-1.5 12.2A2 2 0 0 1 17.5 21h-11a2 2 0 0 1-2-1.8L3 7z"/><path d="M8 7V5a4 4 0 0 1 8 0v2"/></svg></span>
          <div><h4>Shipping</h4><p>Australian shipping only. Free shipping on orders over $100.00.</p></div>
        </div>
        <div class="info-tile">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg></span>
          <div><h4>Payment</h4><p>Visa, Mastercard, American Express, Discover, PayPal and Klarna.</p></div>
        </div>
        <div class="info-tile">
          <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span>
          <div><h4>Orders &amp; enquiries</h4><p>Monday to Friday, 9:00 am &ndash; 5:00 pm. Call <a href="tel:0411750250">0411 750 250</a>.</p></div>
        </div>
      </div>
    </div>
  </section>
""".replace("{cards}", "\n".join(cards))


# -------------------------------------------------------------------- faq ---
FAQS = [
    ("What causes mould growth?",
     "Mould thrives in warm, humid, and moist environments. Common causes of mould growth include water leaks, condensation, high humidity, and poor ventilation."),
    ("Is mould dangerous?",
     "Yes, mould can cause a range of health problems, especially for people with respiratory issues, allergies, or weakened immune systems. Mould can also damage your home&rsquo;s structure and belongings."),
    ("Can I remove mould myself?",
     "While some minor mould problems can be DIY-ed, it&rsquo;s best to hire a professional mould removal service."),
    ("Why is Mr Mould so effective?",
     "Mr Mould harnesses the powerful unique blend of five therapeutic grade essential oils to create the time-proven perfect &ldquo;natural&rdquo; storm against mould and mildew. The cleaning component of the product is derived from coconut &mdash; the residual coating left on the surface creates somewhat of a moisture barrier that assists in retarding the return of mould."),
    ("What&rsquo;s the difference between Mr Mould and Naturamax?",
     "Naturamax harnesses the full cleaning potential of Mr Mould while utilizing only half the amount of Essential Oils. Its purpose is to thoroughly clean and sanitise, rather than solely addressing mould remediation."),
    ("Does bleach and chlorine kill mould?",
     "No. It just bleaches it so it can not be seen."),
    ("Does clove oil kill mould?",
     "Yes, but clove oil only impacts about 10% of mould species. There are over 8,500 mould species we are currently aware of, which is why we employ 5 therapeutic-grade essential oils to assist in addressing this spectrum of mould."),
    ("Are your natural cleaning products safe for children and pets?",
     "Yes."),
]


def faq_body():
    items = []
    for i, (q, a) in enumerate(FAQS):
        open_attr = " open" if i == 0 else ""
        items.append(
            '        <details{o}>\n'
            '          <summary>{q}</summary>\n'
            '          <div class="faq__body"><p>{a}</p></div>\n'
            '        </details>'.format(o=open_attr, q=q, a=a)
        )
    schema_items = ",\n".join(
        '    {{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'.format(
            q=q.replace("&rsquo;", "'").replace("&ldquo;", "").replace("&rdquo;", ""),
            a=a.replace("&rsquo;", "'").replace("&ldquo;", "").replace("&rdquo;", "").replace("&mdash;", "-"),
        )
        for q, a in FAQS
    )
    return """
  <section class="section">
    <div class="wrap">
      <div class="faq">
{items}
      </div>
      <div class="center" style="margin-top:2.5rem">
        <p class="lead">Still have a question? We&rsquo;re happy to talk it through.</p>
        <div class="btn-row" style="justify-content:center">
          <a class="btn btn--primary" href="contact.html">Contact the team</a>
          <a class="btn btn--ghost" href="tel:0411750250">Call 0411 750 250</a>
        </div>
      </div>
    </div>
  </section>
  <script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{schema}
]}
  </script>
""".replace("{items}", "\n".join(items)).replace("{schema}", schema_items)


# ---------------------------------------------------------------- contact ---
CONTACT_BODY = """
  <section class="section">
    <div class="wrap split">
      <div>
        <p class="eyebrow">Get in touch</p>
        <h2>We&rsquo;re here Monday to Friday</h2>
        <p class="lead">Call for anything urgent, or send the form and we&rsquo;ll come back to you &mdash; usually the same business day.</p>
        <div class="grid" style="gap:.9rem;margin-top:1.75rem">
          <div class="info-tile">
            <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg></span>
            <div><h4>Phone</h4><p><a href="tel:0411750250">0411 750 250</a></p></div>
          </div>
          <div class="info-tile">
            <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg></span>
            <div><h4>Email</h4><p><a href="mailto:naturally@essentialshield.com">naturally@essentialshield.com</a></p></div>
          </div>
          <div class="info-tile">
            <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg></span>
            <div><h4>Service area</h4><p>Servicing the Queensland community, Australia &mdash; on-site services across QLD, products shipped Australia-wide.</p></div>
          </div>
          <div class="info-tile">
            <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span>
            <div><h4>Trading hours</h4><p>Monday to Friday, 9:00 am &ndash; 5:00 pm</p></div>
          </div>
          <div class="info-tile">
            <span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z"/><path d="M8 9h8M8 13h5"/></svg></span>
            <div><h4>ABN</h4><p>84683314566</p></div>
          </div>
        </div>
      </div>

      <div class="form-card">
        <h3>Send us a message</h3>
        <p style="font-size:.95rem">Mould, restoration, cleaning, products or stockists &mdash; ask away.</p>
        <form method="POST" action="https://vision.leadrai.com/api/forms/4dfea5213f838b89b8fd940221481367" data-leadr novalidate>
          <div class="form-status" aria-live="polite"></div>
          <input type="hidden" name="_form" value="Contact">
          <input type="hidden" name="_page" value="">
          <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none">

          <div class="field-row">
            <div class="field">
              <label for="c-name">Name <span class="req">*</span></label>
              <input id="c-name" type="text" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="c-phone">Phone <span class="req">*</span></label>
              <input id="c-phone" type="tel" name="phone" autocomplete="tel" required>
            </div>
          </div>
          <div class="field">
            <label for="c-email">Email <span class="req">*</span></label>
            <input id="c-email" type="email" name="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="c-suburb">Suburb</label>
            <input id="c-suburb" type="text" name="Suburb" autocomplete="address-level2">
          </div>
          <div class="field">
            <label for="c-topic">Enquiry about</label>
            <select id="c-topic" name="Enquiry about">
              <option>Mould remediation</option>
              <option>Water damage restoration</option>
              <option>Pressure washing</option>
              <option>Bond &amp; end of lease clean</option>
              <option>Mr Mould / Naturamax products</option>
              <option>Becoming a stockist</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="field">
            <label for="c-message">Message <span class="req">*</span></label>
            <textarea id="c-message" name="Message" required placeholder="Tell us what you need help with."></textarea>
          </div>
          <button class="btn btn--primary btn--block" type="submit">Send message</button>
          <p class="form-note">We reply during trading hours, Monday to Friday 9:00 am &ndash; 5:00 pm.</p>
        </form>
      </div>
    </div>
  </section>
"""

# ------------------------------------------------------------------ quote ---
QUOTE_BODY = """
  <section class="section">
    <div class="wrap split split--narrow">
      <div>
        <p class="eyebrow">How it works</p>
        <h2>A fair, upfront quote &mdash; no mystery chemicals</h2>
        <p class="lead">At Essential Shield we believe in transparency and peace of mind. That&rsquo;s why we tell you upfront exactly what we&rsquo;ll be using in your home.</p>
        <div class="grid" style="gap:.9rem;margin-top:1.5rem">
          <div class="info-tile"><span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></span><div><h4>1. Tell us about the job</h4><p>Share the property type, the areas affected and any photos you can describe.</p></div></div>
          <div class="info-tile"><span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></span><div><h4>2. We respond promptly</h4><p>Our team comes back with a clear scope and a fair price &mdash; the thing clients tell us they value most.</p></div></div>
          <div class="info-tile"><span class="card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></span><div><h4>3. Natural treatment, done right</h4><p>Our technicians treat, clean and protect &mdash; leaving an essential oil barrier behind.</p></div></div>
        </div>
        <p style="margin-top:1.5rem">Prefer to talk? Call <a href="tel:0411750250"><strong>0411 750 250</strong></a>, Monday to Friday 9:00 am &ndash; 5:00 pm.</p>
      </div>

      <div class="form-card">
        <h3>Request your quote</h3>
        <p style="font-size:.95rem">The more detail you give us, the more accurate the quote.</p>
        <form method="POST" action="https://vision.leadrai.com/api/forms/4dfea5213f838b89b8fd940221481367" data-leadr novalidate>
          <div class="form-status" aria-live="polite"></div>
          <input type="hidden" name="_form" value="Quote request">
          <input type="hidden" name="_page" value="">
          <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="display:none">

          <div class="field-row">
            <div class="field">
              <label for="g-name">Name <span class="req">*</span></label>
              <input id="g-name" type="text" name="name" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="g-phone">Phone <span class="req">*</span></label>
              <input id="g-phone" type="tel" name="phone" autocomplete="tel" required>
            </div>
          </div>
          <div class="field">
            <label for="g-email">Email <span class="req">*</span></label>
            <input id="g-email" type="email" name="email" autocomplete="email" required>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="g-service">Service needed <span class="req">*</span></label>
              <select id="g-service" name="Service needed" required>
                <option value="">Please choose&hellip;</option>
                <option>Mould remediation</option>
                <option>Water damage restoration</option>
                <option>Pressure washing</option>
                <option>Bond &amp; end of lease clean</option>
                <option>Product order or stockist enquiry</option>
              </select>
            </div>
            <div class="field">
              <label for="g-property">Property type</label>
              <select id="g-property" name="Property type">
                <option>House</option>
                <option>Unit or apartment</option>
                <option>Rental property</option>
                <option>Commercial premises</option>
                <option>Boat, caravan or campervan</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="g-suburb">Suburb</label>
              <input id="g-suburb" type="text" name="Suburb" autocomplete="address-level2">
            </div>
            <div class="field">
              <label for="g-date">Preferred date</label>
              <input id="g-date" type="date" name="Preferred date">
            </div>
          </div>
          <div class="field">
            <label for="g-details">Job details</label>
            <textarea id="g-details" name="Job details" placeholder="Which rooms or surfaces are affected? How long has it been there? Any access notes?"></textarea>
          </div>
          <label class="check">
            <input type="checkbox" name="Happy to be contacted by phone" value="Yes">
            <span>I&rsquo;m happy to be contacted by phone or SMS about this quote.</span>
          </label>
          <button class="btn btn--primary btn--block" type="submit">Request my quote</button>
          <p class="form-note">No obligation. We never share your details with anyone else.</p>
        </form>
      </div>
    </div>
  </section>
"""

# --------------------------------------------------------------- policies ---
POLICIES_BODY = """
  <section class="section">
    <div class="wrap" style="max-width:860px">
      <article id="terms" style="margin-bottom:3rem">
        <h2>Terms &amp; Conditions</h2>
        <p>These terms apply to services carried out by Essential Shield (ABN 84683314566) and to products purchased from our online store.</p>
        <ul>
          <li>Quotes are based on the information you provide and on the areas we are able to inspect. If the scope changes on site, we will confirm any variation with you before proceeding.</li>
          <li>Bookings are scheduled during trading hours, Monday to Friday, 9:00 am to 5:00 pm.</li>
          <li>Our treatments use natural products. Results depend on ongoing moisture control &mdash; mould returns where leaks, condensation, high humidity or poor ventilation are not addressed.</li>
          <li>Product descriptions are provided in good faith. Always follow the directions and safety information on the label.</li>
          <li>Prices are in Australian dollars and include GST where applicable.</li>
        </ul>
        <p>Questions about these terms? Email <a href="mailto:naturally@essentialshield.com">naturally@essentialshield.com</a> or call <a href="tel:0411750250">0411 750 250</a>.</p>
      </article>

      <article id="privacy" style="margin-bottom:3rem">
        <h2>Privacy Policy</h2>
        <p>We collect only the information needed to quote, deliver and support our services &mdash; typically your name, phone number, email address, suburb and the details of your enquiry.</p>
        <ul>
          <li>We use your information to respond to enquiries, prepare quotes, schedule work and fulfil product orders.</li>
          <li>We do not sell your personal information, and we do not share it with third parties except where it is necessary to deliver your order or service.</li>
          <li>If you subscribe to our natural cleaning tips, you can unsubscribe at any time by replying to any email or contacting us.</li>
          <li>You may ask us to access, correct or delete the personal information we hold about you at any time.</li>
        </ul>
        <p>Privacy requests can be sent to <a href="mailto:naturally@essentialshield.com">naturally@essentialshield.com</a>.</p>
      </article>

      <article id="shipping" style="margin-bottom:3rem">
        <h2>Shipping &amp; Payment</h2>
        <ul>
          <li><strong>Australian shipping only.</strong> We do not ship internationally.</li>
          <li><strong>Free shipping on orders over $100.00.</strong> Orders below that value are charged standard delivery.</li>
          <li>Orders are processed during trading hours, Monday to Friday, 9:00 am to 5:00 pm.</li>
          <li>We accept Visa, Mastercard, American Express, Discover, PayPal and Klarna.</li>
          <li>Prefer to buy locally? Ask us about stockists carrying Mr Mould and Naturamax near you.</li>
        </ul>
        <p style="margin-top:1.5rem"><img src="https://irp.cdn-website.com/32d4e7bd/dms3rep/multi/opt/Payment-4553da06-408w.png" alt="Accepted payment methods: Visa, Mastercard, American Express, Discover, PayPal and Klarna" loading="lazy" style="max-width:320px"></p>
      </article>

      <article id="returns">
        <h2>Return Policy</h2>
        <p>If something isn&rsquo;t right with your order, contact us as soon as possible so we can put it right.</p>
        <ul>
          <li>Contact us with your order details and a description of the issue before returning anything.</li>
          <li>Products that arrive damaged, faulty or incorrectly supplied will be replaced or refunded.</li>
          <li>Unused products in their original, sealed packaging may be returned by arrangement.</li>
          <li>Nothing in this policy limits your rights under Australian Consumer Law.</li>
        </ul>
        <p>Start a return by emailing <a href="mailto:naturally@essentialshield.com">naturally@essentialshield.com</a> or calling <a href="tel:0411750250">0411 750 250</a>.</p>
      </article>
    </div>
  </section>
"""

PAGES = [
    (
        {
            "key": "services",
            "slug": "our-services",
            "title": "Our Services | Essential Shield &mdash; Natural Mould, Restoration &amp; Cleaning",
            "description": "Mould remediation, water damage restoration, pressure washing and bond cleaning across Queensland — all using 100% natural, family-safe products.",
            "crumb": "Services",
            "h1": "Natural services that protect your home and your health",
            "intro": "Mould remediation, water damage restoration, pressure washing and end of lease cleaning &mdash; delivered with 100% natural products by a team that has served Queensland for 17 years.",
        },
        SERVICES_BODY,
    ),
    (
        {
            "key": "products",
            "slug": "essential-shield",
            "title": "Store | Mr Mould &amp; Naturamax Natural Cleaning Products",
            "description": "Shop the Mr Mould and Naturamax natural cleaning range from Essential Shield. Safe for children and pets. Australian shipping only, free over $100.",
            "crumb": "Store",
            "h1": "Mr Mould &amp; Naturamax",
            "intro": "Powerful natural cleaning for your property, boats, caravans, campervans, canvas, shade sails and any other indoor or outdoor surface.",
        },
        products_body(),
    ),
    (
        {
            "key": "faq",
            "slug": "faq",
            "title": "FAQs | Essential Shield Natural Mould Remediation",
            "description": "Answers about mould growth, health risks, DIY removal, bleach and chlorine, Mr Mould vs Naturamax, and whether our natural products are safe for children and pets.",
            "crumb": "FAQs",
            "h1": "Quick answers for your peace of mind",
            "intro": "The questions Queensland homeowners ask us most about mould, natural treatment and our products.",
        },
        faq_body(),
    ),
    (
        {
            "key": "contact",
            "slug": "contact",
            "title": "Contact Essential Shield | Call 0411 750 250",
            "description": "Contact Essential Shield for natural mould remediation, restoration and cleaning in Queensland. Call 0411 750 250 or email naturally@essentialshield.com.",
            "crumb": "Contact",
            "h1": "Contact Essential Shield",
            "intro": "Tell us what you&rsquo;re dealing with &mdash; mould, water damage, a bond clean or a product order &mdash; and we&rsquo;ll point you in the right direction.",
        },
        CONTACT_BODY,
    ),
    (
        {
            "key": "quote",
            "slug": "get-a-quote",
            "title": "Get a Quote | Essential Shield Natural Mould Remediation",
            "description": "Request a free, no-obligation quote for natural mould remediation, water damage restoration, pressure washing or end of lease cleaning in Queensland.",
            "crumb": "Get a Quote",
            "h1": "Get a quote",
            "intro": "Fair pricing, prompt replies and full transparency about exactly what we will use in your home.",
        },
        QUOTE_BODY,
    ),
    (
        {
            "key": "policies",
            "slug": "policies",
            "title": "Policies | Essential Shield",
            "description": "Terms and conditions, privacy policy, shipping and payment details and the return policy for Essential Shield.",
            "crumb": "Policies",
            "h1": "Terms, privacy, shipping &amp; returns",
            "intro": "Everything you need to know about working with us and ordering from our store.",
        },
        POLICIES_BODY,
    ),
]


def main():
    for page, body in PAGES:
        out = os.path.join(ROOT, page["key"] + ".html")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(shell(page, body))
        print("wrote", out)


if __name__ == "__main__":
    main()
