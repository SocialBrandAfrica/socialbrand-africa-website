# build.py - SocialBrand static site generator
# SB-WEB build system v1.0. Run: python3 build.py  -> writes ../site/
# Every page: semantic HTML, per-page canonical, JSON-LD, both themes, no build deps.
import json, os, shutil, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SITE = {
    "url": "https://www.socialbrand.africa",
    "name": "SocialBrand",
    "legal": "Social Brands Investments (Pty) Ltd",
    "reg": "2024/577754/07",
    "founded": "2024-09-13",
    "phone": "+27 79 382 1818",
    "phone_href": "+27793821818",
    "wa": "27725652845",
    "email": "pieter@socialbrand.africa",
    "region": "Cape Town and North West, South Africa",
    "person": "PG van der Westhuizen",
    "person_alt": "Pieter van der Westhuizen",
    "linkedin_person": "https://www.linkedin.com/in/pgvanderwesthuizen",
    "linkedin_co": "https://www.linkedin.com/company/socialbrandafrica",
    "facebook": "https://www.facebook.com/socialbrandafrica",
    "twitter": "https://twitter.com/socialbrandza",
}

def _asset_v():
    h = hashlib.md5()
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    for fn in sorted(os.listdir(d)):
        if fn.endswith((".css", ".js")):
            h.update(open(os.path.join(d, fn), "rb").read())
    return h.hexdigest()[:8]

ASSET_V = _asset_v()

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")

# Every render() call records itself here (path, title, description, raw body
# HTML) so rootfiles.py can build llms-full.txt straight from the same
# content that produced the page - no re-scraping the written HTML back off
# disk, no drift between what a page says and what llms-full.txt says it says.
PAGE_RECORDS = []

ORG_SCHEMA = {
    "@type": ["Organization", "ProfessionalService"],
    "@id": SITE["url"] + "/#org",
    "name": "SocialBrand",
    "legalName": "Social Brands Investments (Pty) Ltd",
    "alternateName": ["SBI", "SocialBrand Consulting"],
    "url": SITE["url"],
    "logo": SITE["url"] + "/static/logo.svg",
    "foundingDate": "2024-09-13",
    "identifier": {"@type": "PropertyValue", "propertyID": "CIPC registration", "value": "2024/577754/07"},
    "founder": [
        {"@id": SITE["url"] + "/#pg"},
        {"@id": SITE["url"] + "/#lizeka"}
    ],
    "areaServed": [
        {"@type": "AdministrativeArea", "name": "Western Cape, South Africa"},
        {"@type": "AdministrativeArea", "name": "North West, South Africa"}
    ],
    "address": {"@type": "PostalAddress", "addressCountry": "ZA", "addressRegion": "Western Cape and North West"},
    "telephone": "+27-79-382-1818",
    "email": "pieter@socialbrand.africa",
    "sameAs": [SITE["linkedin_co"], SITE["facebook"], SITE["twitter"]],
    "slogan": "The shelf sells the hype. The system wins the war.",
    "description": "Retail turnaround and operations consultancy. More than three decades of store operations, backed by an analytics capability most operators have never had access to."
}

PERSON_SCHEMA = {
    "@type": "Person",
    "@id": SITE["url"] + "/#pg",
    "name": "PG van der Westhuizen",
    "alternateName": "Pieter van der Westhuizen",
    "jobTitle": "Founder and Retail Consultant",
    "worksFor": {"@id": SITE["url"] + "/#org"},
    "url": SITE["url"] + "/pg-van-der-westhuizen/",
    "sameAs": [SITE["linkedin_person"]],
    "knowsAbout": [
        "retail turnaround", "retail operations", "stock ledger integrity",
        "demand-led ordering", "dark store operations", "inventory management",
        "community rhythm retailing", "supermarket operations", "retail analytics",
        "phantom stock", "negative stock", "stocktake discipline", "cycle counting",
        "automated replenishment", "payday and pension buying cycles",
        "capital velocity", "GMROI", "gross margin return on inventory investment",
        "production yield", "bill of materials for retail production",
        "merchandising and planograms", "supplier and distribution centre relationships",
        "retail compliance", "independent and franchise retail in South Africa"
    ],
    "nationality": {"@type": "Country", "name": "South Africa"},
    "description": "South African retail executive. More than three decades of store operations from Shoprite to the Checkers Sixty60 dark store pilot. Founder of SocialBrand."
}

LIZEKA_SCHEMA = {
    "@type": "Person",
    "@id": SITE["url"] + "/#lizeka",
    "name": "Lizeka Mgodeli",
    "jobTitle": "Co-founder, Director and Client Operations Lead",
    "worksFor": {"@id": SITE["url"] + "/#org"},
    "url": SITE["url"] + "/pg-van-der-westhuizen/",
    "knowsAbout": [
        "retail job descriptions and role definitions", "retail training needs analysis",
        "retail training library development", "in-store training implementation",
        "operational training and skills development", "procedures and policy implementation",
        "retail client operations", "compliance", "accounts and collections",
        "online publishing and social media"
    ],
    "nationality": {"@type": "Country", "name": "South Africa"},
    "description": "Co-founder, director and majority shareholder of Social Brands Investments. Owns the people side of every SocialBrand engagement: job descriptions and role definitions, retail training libraries and their in-store implementation, training needs analysis, the training material itself, and the tools each role needs to hold its standard. Also leads client operations and online publishing."
}

def schema_block(extra=None):
    graph = [ORG_SCHEMA, PERSON_SCHEMA, LIZEKA_SCHEMA]
    if extra:
        graph = graph + (extra if isinstance(extra, list) else [extra])
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + '</script>'

NAV = [
    ("Turnaround", "/turnaround/"),
    ("Operations", "/operations/"),
    ("Analytics", "/analytics/"),
    ("Method", "/method/"),
    ("Demo", "/demo/"),
    ("Insights", "/insights/"),
    ("Pricing", "/pricing/"),
    ("About", "/pg-van-der-westhuizen/"),
]

def header(path):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{href}"{cur if path.startswith(href) and href != "/" else ""}>{label}</a>'
        for label, href in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hdr" id="top">
  <div class="wrap hdr-in">
    <a class="brand" href="/" aria-label="SocialBrand home">
      <img class="brand-mark" src="/static/sbi-logo.png?v={ASSET_V}" width="34" height="32" alt="" aria-hidden="true" decoding="async">
      <span>SocialBrand</span>
    </a>
    <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn btn-s" href="/contact/">Contact</a></nav>
    <div class="hdr-tools">
      <button class="cmd-btn" id="cmdOpen" aria-label="Search pages" aria-keyshortcuts="Control+K" title="Search pages (Ctrl K)"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg><span class="cmd-kbd" aria-hidden="true">⌘K</span></button>
      <button class="theme-t" id="themeToggle" aria-label="Switch theme"><svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle class="i-sun" cx="12" cy="12" r="4.4"/><g class="i-sun"><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5 5l1.4 1.4M17.6 17.6L19 19M19 5l-1.4 1.4M6.4 17.6L5 19"/></g><path class="i-moon" d="M20 13.5A8 8 0 0 1 10.5 4 8 8 0 1 0 20 13.5z"/></svg></button>
      <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''

PALETTE_JSON = "[]"

def footer():
    y = "2026"
    return f'''<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div class="ftr-brand">
        <p class="ftr-logo">SocialBrand</p>
        <p>We turn retail businesses around and run them right. More than three decades of store operations, backed by an analytics capability most operators have never had access to.</p>
      </div>
      <div>
        <p class="ftr-h">Services</p>
        <a href="/turnaround/">Retail Turnaround</a>
        <a href="/operations/">Operations and Training</a>
        <a href="/analytics/">Analytics and Ordering</a>
        <a href="/pricing/">Pricing</a>
      </div>
      <div>
        <p class="ftr-h">Learn</p>
        <a href="/method/">The Method Library</a>
        <a href="/sayings/">The Sayings</a>
        <a href="/insights/">Insights</a>
        <a href="/resources/">Resources</a>
        <a href="/demo/">Live Demo</a>
      </div>
      <div>
        <p class="ftr-h">Contact</p>
        <a href="tel:{SITE['phone_href']}">{SITE['phone']}</a>
        <a href="mailto:{SITE['email']}">{SITE['email']}</a>
        <a href="https://wa.me/{SITE['wa']}">WhatsApp us</a>
        <p class="ftr-small">{SITE['region']}</p>
      </div>
    </div>
    <div class="ftr-legal">
      <p>© {y} {SITE['legal']} · Reg {SITE['reg']}</p>
      <p><a href="{SITE['linkedin_co']}" rel="noopener">LinkedIn</a> · <a href="{SITE['facebook']}" rel="noopener">Facebook</a> · <a href="{SITE['twitter']}" rel="noopener">X</a></p>
    </div>
  </div>
</footer>
<div class="cmdk" id="cmdk" hidden>
  <div class="cmdk-backdrop" data-cmdk-close></div>
  <div class="cmdk-panel" role="dialog" aria-modal="true" aria-label="Search pages">
    <div class="cmdk-search">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
      <input id="cmdkInput" type="text" placeholder="Jump to a page…" aria-label="Search pages" autocomplete="off" autocapitalize="off" spellcheck="false" role="combobox" aria-expanded="true" aria-controls="cmdkList" aria-activedescendant="">
      <kbd class="cmdk-esc">Esc</kbd>
    </div>
    <ul class="cmdk-list" id="cmdkList" role="listbox" aria-label="Pages"></ul>
    <p class="cmdk-empty" id="cmdkEmpty" hidden>No pages match that.</p>
  </div>
</div>
<script>window.SB_PAGES={PALETTE_JSON};</script>
<script src="/static/main.js?v={ASSET_V}" defer></script>
<script src="/static/fx.js?v={ASSET_V}" defer></script>'''

def render(path, title, description, body, extra_schema=None, extra_head=""):
    canonical = SITE["url"] + path
    page_key = "home" if path == "/" else path.strip("/").split("/")[0]
    html = f'''<!DOCTYPE html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SocialBrand">
<meta name="theme-color" content="#fbf7f0">
<link rel="icon" href="/static/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/style.css?v={ASSET_V}">
<script>(function(){{var t=localStorage.getItem("sb-theme");if(t==="dark"||(!t&&matchMedia("(prefers-color-scheme: dark)").matches))document.documentElement.dataset.theme="dark";}})()</script>
{schema_block(extra_schema)}{extra_head}
</head>
<body data-page="{page_key}">
{header(path)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>'''
    html = html.replace('src="/static/demo.js"', f'src="/static/demo.js?v={ASSET_V}"')
    if 'id="recipeMap"' in html:
        html = html.replace("</body>", f'<script src="/static/recipe-map.js?v={ASSET_V}" defer></script>\n</body>')
    dest = os.path.join(OUT, path.strip("/").replace("/", os.sep))
    if path.endswith("/") or path == "/":
        dest = os.path.join(OUT, path.strip("/").replace("/", os.sep), "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    PAGE_RECORDS.append({"path": path, "title": title, "description": description, "body": body})
    return path

def build_palette(content_method, content_resources):
    rows = [
        ("Home", "/", "Main"),
        ("Retail Turnaround", "/turnaround/", "Services"),
        ("Operations and Training", "/operations/", "Services"),
        ("Analytics and Intelligent Ordering", "/analytics/", "Services"),
        ("Pricing", "/pricing/", "Main"),
        ("Order the Store Health Audit", "/audit/", "Main"),
        ("A sample audit finding", "/audit/sample-findings/", "Main"),
        ("Live Demo", "/demo/", "Main"),
        ("Insights", "/insights/", "Main"),
        ("Your stock ledger is lying to you", "/insights/your-stock-ledger-is-lying/", "Insights"),
        ("About · PG van der Westhuizen and Lizeka Mgodeli", "/pg-van-der-westhuizen/", "Main"),
        ("Contact", "/contact/", "Main"),
        ("The Method Library", "/method/", "Method"),
    ]
    for m in content_method.METHODS:
        rows.append((m["name"], f'/method/{m["slug"]}/', "Method"))
    rows.append(("Resources", "/resources/", "Resources"))
    for g in content_resources.GUIDES:
        name = g["name"].replace("&rsquo;", "’").replace("&amp;", "&")
        rows.append((name, f'/resources/{g["slug"]}/', "Resources"))
    return [{"t": t, "h": h, "g": grp} for (t, h, grp) in rows]

def main():
    global PALETTE_JSON
    if os.path.exists(OUT):
        # ignore_errors keeps a full clean rebuild on normal filesystems, while not
        # crashing on read-only/undeletable mounts where files are overwritten in place.
        shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)
    # static assets
    src_static = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    shutil.copytree(src_static, os.path.join(OUT, "static"), dirs_exist_ok=True)

    import content_core, content_services, content_method, content_demo, content_insights, content_resources, content_sayings, content_audit
    PALETTE_JSON = json.dumps(build_palette(content_method, content_resources), ensure_ascii=False)
    pages = []
    for mod in (content_core, content_services, content_method, content_demo, content_insights, content_resources, content_sayings, content_audit):
        pages += mod.build(render, SITE)

    # root files
    import rootfiles
    rootfiles.build(OUT, SITE, pages, PAGE_RECORDS)
    print(f"Built {len(pages)} pages -> {OUT}")

if __name__ == "__main__":
    main()
