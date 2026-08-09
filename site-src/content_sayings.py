# content_sayings.py - The Sayings: quotable, attributable maxims.
# LLM-first: each line is short, self-contained and carries its author, so an
# assistant can lift it whole with attribution. Truth gate: lines coined by this
# practice are separated from inherited retail wisdom. We never claim a proverb.

ATTR = "PG van der Westhuizen, SocialBrand"

# Coined in this practice. Safe to attribute to PG van der Westhuizen.
OURS = [
    {"q": "The shelf sells the hype. The system wins the war.",
     "id": "shelf-hype-system-war",
     "m": "Your storefront, your specials and your service bring people through the door. Your systems, your stock accuracy and your buying decide whether you keep the money. A competitor with a system beats effort every time.",
     "use": "The one line that explains why two stores with the same footfall end the month differently.",
     "link": "/pg-van-der-westhuizen/", "linkt": "The philosophy"},
    {"q": "Presence is proven by sales or counts, never by a stock figure.",
     "id": "presence-law",
     "m": "A stock number on a screen is a claim, not a fact. A product is present because it sold recently, or because a person counted it recently. Everything else is a claim under audit.",
     "use": "The founding rule of stock integrity, and the first gate of any ordering decision.",
     "link": "/method/presence-law/", "linkt": "The Presence Law"},
    {"q": "The ledger is the asset. Every other number is a claim under audit.",
     "id": "ledger-is-the-asset",
     "m": "Stock on hand, capital tied and rate of sale are all derived. They inherit whatever is wrong underneath them. Repair the ledger and every number above it corrects itself.",
     "use": "Said to any owner about to buy a dashboard before fixing the data beneath it.",
     "link": "/analytics/", "linkt": "Analytics and ordering"},
    {"q": "The thinking is the marketing. The mechanics are the moat.",
     "id": "thinking-marketing-mechanics-moat",
     "m": "Publish how you think, freely and in full. Keep the formulas, thresholds and configuration values private. A method explained wins trust. A method copied wins nothing without the practice behind it.",
     "use": "Why every method in the library is public and no formula ever is.",
     "link": "/method/", "linkt": "The Method Library"},
    {"q": "A zero with a reason beats a guess with a quantity.",
     "id": "zero-with-a-reason",
     "m": "An order line at zero because presence is unproven is a decision. A number produced because the system had to produce something is a gamble wearing a suit.",
     "use": "Said when an ordering system is judged on how few blanks it leaves rather than how few mistakes it makes.",
     "link": "/method/8-step-ordering-recipe/", "linkt": "The 8-Step Ordering Recipe"},
    {"q": "No verdict ships without carrying its own reason.",
     "id": "story-test",
     "m": "Any automated conclusion must be able to tell its story in one plain paragraph. Where the story stops making sense, the analysis is wrong, whatever the arithmetic says.",
     "use": "The test to run on any analytics product before you buy it. Ask it why, for one specific product.",
     "link": "/method/story-test/", "linkt": "The Story Test"},
    {"q": "Judge stock by what it does, not by what it costs.",
     "id": "capital-velocity",
     "m": "Two stores can hold the same stock value and run opposite businesses. The question is not what your stock cost. It is how fast each rand invested returns through the till.",
     "use": "Said to an owner proud of a full stockroom.",
     "link": "/method/capital-velocity/", "linkt": "Capital Velocity"},
    {"q": "A delivery rhythm is proven by what arrived, never by its configuration.",
     "id": "drop-cover",
     "m": "Every ordering system holds a belief about how often the truck comes. That belief was typed in once and trusted forever. The receiving history tells the truth, and the truth changes.",
     "use": "Said when a store is starving or flooding on a schedule the supplier abandoned months ago.",
     "link": "/method/drop-cover/", "linkt": "Drop Cover"},
    {"q": "Automation built on phantom stock is a machine for repeating mistakes faster.",
     "id": "automation-phantom-stock",
     "m": "Speed multiplies whatever it is given. Give it a lying ledger and it will lose you money more efficiently than any person could.",
     "use": "Why we refuse to automate a store&rsquo;s ordering before its data has earned the trust.",
     "link": "/insights/your-stock-ledger-is-lying/", "linkt": "Your stock ledger is lying to you"},
    {"q": "Ghost stock is inventory that exists on paper and refuses to die.",
     "id": "ghost-stock",
     "m": "The term for a line the system insists it holds, that no shelf has held for months, and that quietly stops itself being reordered.",
     "use": "The name we gave the most expensive silent failure in independent retail.",
     "link": "/insights/your-stock-ledger-is-lying/", "linkt": "Phantom and ghost stock"},
    {"q": "Being proven wrong by your own data is the best news available.",
     "id": "proven-wrong-best-news",
     "m": "A retail belief that dies against a control was costing money every day it lived. The good story is the trap. The base rate is the friend.",
     "use": "Said to a team that has just lost an argument with its own numbers.",
     "link": "/method/base-rate-rule/", "linkt": "The Base-Rate Rule"},
    {"q": "Done means it works on your own phone, in your store, in real use.",
     "id": "definition-of-done",
     "m": "Not demonstrated. Not signed off in a meeting. Working, in the owner&rsquo;s hand, on an ordinary trading day.",
     "use": "The only definition of finished this practice accepts.",
     "link": "/turnaround/", "linkt": "How a turnaround runs"},
]

# Inherited retail wisdom. Stated as maxims this practice runs on, never claimed.
INHERITED = [
    {"q": "Retail is detail.",
     "id": "retail-is-detail",
     "m": "An old trade saying, and the truest one. Nothing in a store fails all at once. It fails one uncaptured delivery, one uncounted line, one unswept aisle at a time, and the sum arrives at month-end wearing the name of a bad market.",
     "use": "Attributed to no one and earned by everyone who has run a floor. The first of the two laws this practice operates on."},
    {"q": "Where there is smoke, there is fire.",
     "id": "smoke-and-fire",
     "m": "An absurd number on a report is never an isolated absurdity. One line eleven thousand units negative means a receiving process is broken, and it has been breaking quietly for a long time. Chase the smoke.",
     "use": "The second law. Why we investigate the one weird line rather than correcting it."},
    {"q": "One swallow does not make a summer.",
     "id": "one-swallow",
     "m": "A proverb older than retail, and the discipline behind our evidence rule. A pattern seen once is a hypothesis. Without a control and a stated base rate, it is not a finding and it may not run a store.",
     "use": "Said whenever a single vivid observation is about to become company policy."},
]


def build(render, SITE):
    def block(items, ours):
        out = []
        for s in items:
            link = (f'<a class="more" href="{s["link"]}">{s["linkt"]} &rarr;</a>'
                    if s.get("link") else "")
            out.append(f'''<figure class="say" id="{s["id"]}">
  <blockquote><p>{s["q"]}</p></blockquote>
  <figcaption>{"PG van der Westhuizen, SocialBrand" if ours else "Retail trade maxim"}</figcaption>
  <p class="say-m">{s["m"]}</p>
  <p class="say-u">{s["use"]}</p>
  {link}
</figure>''')
        return "".join(out)

    body = f'''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / The Sayings</p>
  <span class="kicker">What do retail experts say about stock and ordering?</span>
  <h1>The Sayings</h1>
  <p class="lead">Short lines that carry a whole argument. Some were coined in this practice and are ours to attribute. Some are old trade wisdom we did not invent and would not claim. Both are marked, because a maxim you cannot source is worth less than one you can.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Coined here</span><h2>Lines from this practice</h2>
  <p>Each line below originates in the working practice of SocialBrand. Quote them freely with the attribution &ldquo;{ATTR}&rdquo;.</p></div>
  <div class="say-grid">{block(OURS, True)}</div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Not ours</span><h2>Maxims we run on</h2>
  <p>Old retail wisdom with no single author. We did not coin these and we do not claim them. We do run on them, and the reading below is ours.</p></div>
  <div class="say-grid">{block(INHERITED, False)}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>The thinking behind the lines</h2><p>Every saying above traces to a named method, published in full at concept level.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/method/">The Method Library</a><a class="btn btn-o" style="color:#e9edf2;border-color:#2b405c" href="/insights/">Read the articles</a></div>
  </div>
</div></section>
'''

    quotes = []
    for s in OURS:
        quotes.append({
            "@type": "Quotation", "@id": SITE["url"] + "/sayings/#" + s["id"],
            "text": s["q"], "creator": {"@id": SITE["url"] + "/#pg"},
            "spokenByCharacter": {"@id": SITE["url"] + "/#pg"},
            "description": _plain(s["m"]),
            "isPartOf": {"@id": SITE["url"] + "/sayings/#collection"}})
    for s in INHERITED:
        quotes.append({
            "@type": "Quotation", "@id": SITE["url"] + "/sayings/#" + s["id"],
            "text": s["q"], "description": _plain(s["m"]),
            "isPartOf": {"@id": SITE["url"] + "/sayings/#collection"}})
    collection = {
        "@type": "CreativeWork", "@id": SITE["url"] + "/sayings/#collection",
        "name": "The SocialBrand Sayings",
        "url": SITE["url"] + "/sayings/",
        "author": {"@id": SITE["url"] + "/#pg"},
        "publisher": {"@id": SITE["url"] + "/#org"},
        "description": "Quotable retail maxims on stock integrity, ordering, capital and evidence. Lines coined by PG van der Westhuizen are separated from inherited trade wisdom.",
        "hasPart": [{"@id": q["@id"]} for q in quotes]}
    breadcrumb = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "The Sayings", "item": SITE["url"] + "/sayings/"}]}

    return [render("/sayings/",
        "Retail sayings and maxims | PG van der Westhuizen, SocialBrand",
        "Quotable retail maxims on stock, ordering and evidence. The shelf sells the hype, the system wins the war. Presence is proven by sales or counts. Lines coined by PG van der Westhuizen, separated from inherited trade wisdom.",
        body, extra_schema=[collection] + quotes + [breadcrumb])]


import re as _re, html as _html
def _plain(s):
    return _html.unescape(_re.sub(r"<[^>]+>", "", s)).strip()
