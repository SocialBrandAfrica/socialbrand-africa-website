# content_insights.py - Insights index + Article 1.
# Article examples are anonymised and perturbed per the Fiction Key convention.

def build(render, SITE):
    pages = []
    A1 = "/insights/your-stock-ledger-is-lying/"

    article_body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / <a href="/insights/">Insights</a> / Your stock ledger is lying to you</p>
  <span class="kicker">Stock ledger integrity</span>
  <h1>Your stock ledger is lying to you</h1>
  <p class="byline" style="color:var(--sky-muted)">By <b style="color:#fff">PG van der Westhuizen</b> · SocialBrand · 19 July 2026 · 7 minute read</p>
</div></div></section>
<article class="sec"><div class="wrap"><div class="prose">

<p class="defn"><strong>Phantom stock</strong> is inventory existing on paper only: a stock figure the system displays for units no shelf holds. Its mirror is negative stock, units the system says cannot exist while customers keep buying them. Both come from the same disease, a ledger recording movements it never understood, and both quietly decide what your store orders next.</p>

<p>Walk into any supermarket back office and ask for the stock report on one product. The system answers instantly, with confidence, to the exact unit. Twenty-four units of long-grain rice. Now walk to the shelf. Count. There are nine.</p>

<p>Nobody stole fifteen bags of rice. Nobody is incompetent. The ledger is doing exactly what ledgers do when nobody audits their claims: it kept the arithmetic and lost the truth.</p>

<h2>How a ledger learns to lie</h2>

<p>A stock ledger has one job. Yesterday&rsquo;s stock, plus what arrived, minus what sold, equals today&rsquo;s stock. Simple. Except a real store breaks the equation a dozen ways before lunch.</p>

<p>Receipts land on one product code while sales ring on another. The same bottle lives on two barcodes, one selling, one hoarding claims. The bakery receipts flour and sells bread, so the flour code grows a mountain of stock it never sold and the bread code sells stock it never received. A case cost gets captured as a unit cost and one shelf of paper cups becomes a small fortune on paper. A barcode gets recycled and inherits a stranger&rsquo;s history.</p>

<p>None of this looks like a crisis. Each error is one line among thousands. The ledger swallows them all and keeps answering to the exact unit.</p>

<p>We have stood in stores where a single bread line ran more than eleven thousand units negative while the shelves sold out every morning. We have found a packaging code carrying close to four hundred thousand units of printed bread bags on the books, received over years and never scanned out. We have watched a water line sell fifty thousand units without a single receipt ever touching its code. Every one of those stores had ordered off those numbers the day before.</p>

<h2>The lie that costs the most is the quiet one</h2>

<p>Negative stock at least announces itself. A minus on a report looks wrong, someone eventually asks about it and the trail leads somewhere useful.</p>

<p>Phantom stock is worse, because it fails silently. A line claiming stock it does not have never triggers a reorder. The ordering system looks at the claim, sees plenty, and moves on. The shelf sits empty. The customer reaches, finds nothing, buys it at the store down the road and tells no one. No report anywhere records the sale you lost, because as far as the system knows, you had stock the whole time.</p>

<p>Multiply one phantom line by a few hundred, which is what a neglected ledger accumulates, and a store is bleeding turnover through holes no report will ever show. The report is the hole.</p>

<h2>Presence is proven by sales or counts. Nothing else.</h2>

<p>The way out starts with one rule, and it is the founding rule of how we work: a product is present because it sold recently or because a person counted it recently. A stock figure on a screen proves nothing. It is a claim, and claims get audited.</p>

<p>This sounds obvious and changes everything. It means the age of a stock figure matters as much as its value. It means a quiet line with a fat claim is not an asset, it is a question. It means the annual stocktake, that heroic weekend of chaos and casual labour, is eleven months too late for most of the errors it finds.</p>

<h2>What to do about it, starting Monday</h2>

<p>You do not need a platform to start. You need a different habit.</p>

<ol>
<li><b>Rank your claims.</b> Pull your stock report sorted by value. The top of the list is where fiction costs most. For each of the top twenty lines ask one question: when did this last sell, or when was it last counted? A big claim with no recent proof goes on tomorrow&rsquo;s count list.</li>
<li><b>Count a little every day.</b> Thirty well-chosen lines inside a normal shift. Value first, oldest proof first. A store doing this proves thousands of lines a quarter, concentrated exactly where the money and the doubt overlap, and errors get caught in days instead of at year-end.</li>
<li><b>Fix receiving at source.</b> When a count exposes a break, chase the movement, not the number. If receipts post to a different code than sales, correcting the quantity tonight buys you a clean number until next week&rsquo;s delivery breaks it again. The receiving fix ends it permanently.</li>
<li><b>Respect the two worlds.</b> Anything made in store, bakery, butchery, deli, will never obey buy-and-sell arithmetic on its ingredient codes. Those lines need production rules, not adjustment journals. Stop punishing fresh departments for a ledger design problem.</li>
<li><b>Only then, trust the number.</b> Once a line&rsquo;s claim is proven, ordering off it stops being gambling. This is why we refuse to automate a store&rsquo;s ordering before its ledger earns it. Automation built on phantom stock is a machine for repeating mistakes faster.</li>
</ol>

<h2>The uncomfortable question</h2>

<p>Here is the test worth running this week. Pick the ten highest-value stock claims in your business and stand in front of each one. If more than one of the ten is fiction, your ledger is lying to you at the top of the range, where it hurts most, and it is lying further down too.</p>

<p>We built a free, twenty-question checklist for exactly this walk: the <a href="/resources/data-health-checklist/">Store Data Health Checklist</a>. It takes an hour and tells you whether your numbers deserve your trust. If the answer is no, that is not bad news. It is the first true number your store has produced in a while, and everything we do starts from there.</p>

<p><b>PG van der Westhuizen</b> is the founder of SocialBrand and has run South African retail floors for more than three decades, including the Checkers Sixty60 dark store pilot in Cape Town, where a phantom stock record becomes a failed customer order inside the hour. SocialBrand rebuilds stores&rsquo; profitability at <a href="/turnaround/">socialbrand.africa</a>.</p>

</div></div></article>
<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>Is your ledger telling the truth?</h2><p>The Store Health Audit answers it with evidence. Fixed fee, one store, findings in rand.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/audit/">See the audit</a><a class="btn btn-o" href="/resources/data-health-checklist/">Free checklist</a></div>
  </div>
</div></section>
'''
    a1_schema = [
        {"@type": "Article", "headline": "Your stock ledger is lying to you",
         "description": "Phantom stock and negative stock come from the same disease: a ledger recording movements it never understood. Why presence is proven by sales or counts, never by a stock figure, and what to do about it starting Monday.",
         "author": {"@id": SITE["url"] + "/#pg"}, "publisher": {"@id": SITE["url"] + "/#org"},
         "datePublished": "2026-07-19", "mainEntityOfPage": SITE["url"] + A1,
         "about": ["phantom stock", "stock ledger integrity", "negative stock", "retail inventory management"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Insights", "item": SITE["url"] + "/insights/"},
            {"@type": "ListItem", "position": 2, "name": "Your stock ledger is lying to you", "item": SITE["url"] + A1}]}
    ]
    pages.append(render(A1, "Your stock ledger is lying to you | SocialBrand Insights",
        "Phantom stock, negative stock and why presence is proven by sales or counts, never by a stock figure. A practical guide to stock ledger integrity by PG van der Westhuizen.",
        article_body, extra_schema=a1_schema))

    index_body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Insights</p>
  <span class="kicker">Insights</span>
  <h1>Written from the floor</h1>
  <p class="lead">Long-form pieces on retail turnaround, stock integrity and demand-led ordering, grounded in real practice with every client detail anonymised. New pieces land fortnightly.</p>
</div></div></section>
<section class="sec"><div class="wrap">
  <div class="grid g2">
    <a class="card flag rv" href="''' + A1 + '''">
      <span class="tag">Stock ledger integrity</span>
      <h3 style="margin-top:14px">Your stock ledger is lying to you</h3>
      <p>Phantom stock never announces itself. It sits on the report looking like an asset while the shelf sits empty and the customer walks. Why presence is proven by sales or counts, never by a stock figure.</p>
      <p class="byline">By <b>PG van der Westhuizen</b> · 19 July 2026</p>
      <span class="more">Read the article →</span>
    </a>
    <div class="card rv" style="display:flex;flex-direction:column;justify-content:center">
      <h3>Coming next</h3>
      <p style="margin-top:10px">The dark store story: what running the continent&rsquo;s highest-turnover Sixty60 store taught us about ledgers with no forgiveness. Then the payday rhythm, and why national averages lie to rural stores.</p>
      <p style="margin-top:14px;font-size:.9rem;color:var(--fg-muted)">Follow along on <a href="''' + SITE["linkedin_co"] + '''" rel="noopener">LinkedIn</a>.</p>
    </div>
  </div>
</div></section>
'''
    pages.append(render("/insights/", "Insights | Retail turnaround and stock integrity articles, SocialBrand",
        "Articles on retail turnaround, stock ledger integrity, payday-rhythm ordering and capital velocity, by PG van der Westhuizen of SocialBrand.",
        index_body))
    return pages
