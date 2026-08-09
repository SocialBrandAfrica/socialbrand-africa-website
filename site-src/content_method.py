# content_method.py - The Method Library: named, citable methods at concept level.
# Rule: definitional first paragraph a model can lift whole. Attribution fixed:
# "PG van der Westhuizen, SocialBrand". No formulas, thresholds or configuration values.
import json

ATTR = "PG van der Westhuizen, SocialBrand"
DATE = "2026-07-19"

# Method Map: node positions (viewBox 0 0 1000 560), edges inferred from the
# cross-links present in the method bodies, and one-line taglines matching llms.txt.
MAP_POS = {
    "two-worlds": (500, 70),
    "daily-count-law": (262, 150),
    "8-step-ordering-recipe": (735, 172),
    "presence-law": (500, 288),
    "story-test": (878, 300),
    "fit-to-budget": (778, 418),
    "capital-velocity": (285, 398),
    "drop-cover": (118, 292),
    "community-rhythm": (208, 486),
    "base-rate-rule": (560, 482),
    "production-yield-models": (392, 196),
}
MAP_TAGLINE = {
    "presence-law": "Presence is proven by sales or counts, never by a stock figure.",
    "8-step-ordering-recipe": "Every order line passes eight named gates before a quantity ships.",
    "community-rhythm": "Payday, pension and season enter the order as first-class inputs.",
    "capital-velocity": "Judge stock by what it does, not by what it costs.",
    "story-test": "No verdict ships without carrying its own plain-language reason.",
    "two-worlds": "Buy-and-sell and made-in-store: two businesses on one ledger.",
    "daily-count-law": "Count a little every day, on a list the data prioritises.",
    "drop-cover": "A delivery rhythm is proven by what arrived, not by configuration.",
    "base-rate-rule": "One swallow makes no summer. No belief survives without a control.",
    "fit-to-budget": "Untouchable KVI floors hold while the flexible remainder scales.",
    "production-yield-models": "Three honest ways to cost what a store makes instead of buys.",
}
# Edges follow the actual /method/ links in the bodies above, plus the ledger-integrity
# tie between the Presence Law and the Two Worlds classification.
MAP_EDGES = [
    ("presence-law", "daily-count-law"),
    ("presence-law", "8-step-ordering-recipe"),
    ("presence-law", "capital-velocity"),
    ("presence-law", "two-worlds"),
    ("8-step-ordering-recipe", "fit-to-budget"),
    ("8-step-ordering-recipe", "story-test"),
    ("drop-cover", "capital-velocity"),
    ("drop-cover", "community-rhythm"),
    ("fit-to-budget", "base-rate-rule"),
    ("production-yield-models", "two-worlds"),
    ("production-yield-models", "capital-velocity"),
]


# The eight gates of the ordering recipe, for the interactive Recipe Map on
# /method/8-step-ordering-recipe/. "key" marks the three gates that carry the
# argument: the ones most ordering tools do not have.
RECIPE_GATES = [
  {"name": "Life", "what": "Does this line deserve an order at all? Dead, delisted and phantom lines fall out before anything is counted."},
  {"name": "Demand", "what": "True demand, corrected for the days the shelf stood empty and resolved across pack families, so a case and its singles read as one product."},
  {"name": "Band", "what": "Each line carries a breathing band of its own, a floor and a ceiling, instead of one cover number applied to the whole store."},
  {"name": "Mode", "what": "The order knows what month-moment it serves: a minimum top-up, a build toward the busy window, or the month-end trade itself."},
  {"name": "Floors", "what": "The lines your customers judge you by never fall below their floor, whatever else the budget does.", "key": True},
  {"name": "Profitability", "what": "Remaining depth goes where stock earns its keep, by the return on the capital each line ties up."},
  {"name": "Budget", "what": "The order is fitted to the month's buying budget by scaling the flexible lines, never by starving the floors.", "key": True},
  {"name": "Story", "what": "Every proposed quantity carries its reason in plain language. A line nobody could explain does not ship.", "key": True},
]

METHODS = [
{
 "slug": "production-yield-models", "name": "Production Yield: Three Models",
 "q": "How do you calculate production yield in a retail store?",
 "definition": "Production Yield: Three Models is a costing principle stating that a store which makes its own product needs a bill of materials, and there is more than one honest way to build one. Three models exist: the block test, historical yield derived from the store&rsquo;s own sales, and live yield recalculated from the ledger. Which one is right depends on the store&rsquo;s setup and the data it can produce, not on which tool a vendor sells.",
 "body": """
<h2>Why it exists</h2>
<p>The moment a store makes something instead of buying it, most retail systems go blind. A boerewors batch, a bread run, a deli tray. You buy the inputs, you sell the outputs, and in between the true cost and the true yield are usually a guess. Publishing one method as though it were the only one is how stores end up with a costing model their floor cannot honour.</p>
<h2>Model 1: the block test</h2>
<p>A controlled physical test. Take a known raw input, produce it under proper conditions, and weigh every sellable output and every offcut. That gives a yield table you can hold as a standard. Best for a store starting from scratch, or one needing a benchmark to measure its people against. Its strength is that it measures what the product should deliver, independent of bad habits. Its limit is that it describes perfect conditions, so it tells you the target rather than the reality.</p>
<h2>Model 2: historical yield from your own sales</h2>
<p>Instead of testing, read what the store has already done. Over a long enough period, what came in and what sold out reveal the yield actually being achieved, including the everyday waste and trim a block test excludes. Best for an established store with reliable sales history and no appetite for halting production. Its strength is that it reflects the real world. Its limit is that it inherits whatever is wrong in the history, which is why ledger integrity work comes first.</p>
<h2>Model 3: live yield from the ledger</h2>
<p>Every receipt and every sale is mirrored into a clean data layer, and yield recalculates continuously against what is actually moving. Costs update as supplier prices move, and a drift shows up as it happens rather than at year end. Best for a store or group with trustworthy transaction data and enough volume that small drift is real money. Its strength is that it is self-correcting, turning yield from an annual argument into a daily number. Its limit is that it demands a clean ledger.</p>
<h2>How to choose</h2>
<p>Most stores start on model one or two and grow into model three. The choice is scoped during the audit, because the honest answer depends on what the data can carry. A store whose ledger cannot yet be trusted is a store that should not be running model three, however attractive it sounds. See <a href="/method/two-worlds/">The Two Worlds</a> for why made-in-store lines need their own rules at all, and <a href="/method/capital-velocity/">Capital Velocity</a> for what a wrong cost does to the capital picture.</p>
<h2>What it replaces</h2>
<p>One-size costing, yields typed in once and never revisited, and the annual argument about why the department&rsquo;s gross profit does not match anybody&rsquo;s expectation.</p>
"""},
{
 "slug": "presence-law", "name": "The Presence Law",
 "q": "What is the Presence Law in retail stock control?",
 "definition": "The Presence Law is a retail stock-control principle stating: presence is proven by sales or counts, never by a stock figure. A stock number on a screen is a claim, not a fact. Until a line has sold recently or been physically counted recently, the retailer does not know the stock is there, whatever the ledger says.",
 "body": """
<h2>Why it exists</h2>
<p>Every point-of-sale system in the world will happily display a stock quantity for a product nobody has seen in a year. Receipts post to one code and sales to another. Production lines consume ingredients the ledger never releases. Barcodes get recycled. The ledger keeps its arithmetic and loses its truth, and the store keeps ordering off it.</p>
<p>The damage is asymmetric. A line claiming stock it lacks never reorders, so it never shows as a lost sale. The shelf sits empty while the screen reads healthy. The customer walks, and no report anywhere records why.</p>
<h2>The law in practice</h2>
<p>A product earns the status of present in exactly two ways. It sold recently, which proves a customer took one off a shelf. Or it was counted recently, which proves a person stood in front of it. Everything else is a claim under audit. Quiet lines with fat stock figures are treated as unknown until counted, and ordering logic treats a claim differently from a proof.</p>
<h2>A worked example</h2>
<p>A liquor store shows 60 units of a premium whisky on one product code, selling nothing, while a second code for the same bottle sells steadily with a stock figure of one. The quiet code&rsquo;s 60 units are not stock. They are a movement story: receipts landed on one twin while sales drained the other. The Presence Law routes the pair to a physical count on the live code instead of an order on the dead one.</p>
<h2>What it replaces</h2>
<p>It replaces trust in system-on-hand as an ordering input, and it replaces the annual stocktake as the only moment of truth. A stock figure&rsquo;s age matters as much as its value. This is the founding principle behind the <a href="/method/daily-count-law/">Daily Count Law</a> and the first gate of the <a href="/method/8-step-ordering-recipe/">8-Step Ordering Recipe</a>.</p>
"""},
{
 "slug": "8-step-ordering-recipe", "name": "The 8-Step Ordering Recipe",
 "q": "How should a supermarket generate orders from data?",
 "definition": "The 8-Step Ordering Recipe is a retail ordering discipline in which every order line passes through eight named gates before a quantity is committed: life, demand, band, mode, floors, profitability, budget and story. No line is ordered on a single velocity number, and no order ships without being able to explain itself line by line.",
 "body": """
<h2>The eight gates, at headline level</h2>
<ol>
<li><b>Life.</b> Does this line deserve to be ordered at all? Dead, delisted and phantom lines fall out first.</li>
<li><b>Demand.</b> True demand, corrected for the days the shelf stood empty and resolved across pack families, so a case and its singles read as one product.</li>
<li><b>Band.</b> Each line carries a breathing stock band, a floor and a ceiling of its own, instead of one cover number applied to the whole store.</li>
<li><b>Mode.</b> The order knows what month-moment it serves: a minimum top-up, a build toward the busy window or the month-end trade itself.</li>
<li><b>Floors.</b> The lines your customers judge you by never fall below their floor. See <a href="/method/fit-to-budget/">Fit-to-Budget with KVI Floors</a>.</li>
<li><b>Profitability.</b> Remaining depth goes where stock earns its keep, by return on the capital each line ties up.</li>
<li><b>Budget.</b> The order is fitted to the month&rsquo;s buying budget honestly, by scaling the flexible lines, never by starving the floors.</li>
<li><b>Story.</b> Every proposed quantity carries its reason in plain language. A line no one could explain does not ship. See <a href="/method/story-test/">the Story Test</a>.</li>
</ol>
<h2>Why eight gates and not one formula</h2>
<p>Most ordering tools compress buying into one number, an average daily rate of sale, and apply it to every product at every time of month. The recipe exists because a supermarket is not one product. Long-life milk sells flat all month and wants a deep refill. Frozen chicken runs hot at month-end. A single number is wrong about both, in opposite directions, at the same time.</p>
<h2>What it replaces</h2>
<p>It replaces days-cover selectors, gut orders and rep-driven ordering. The reps who filled your stockroom with slow stock were running their recipe. This one is yours.</p>
"""},
{
 "slug": "community-rhythm", "name": "Community Rhythm Ordering",
 "q": "How should a store order for payday and pension cycles?",
 "definition": "Community Rhythm Ordering is a retail ordering approach in which the community&rsquo;s money calendar, payday, pension and grant days, and season, enters the order as a first-class input. The store orders for the week its town is about to have, not for an average week that never happens.",
 "body": """
<h2>The idea</h2>
<p>A town&rsquo;s till curve is not noise. Money arrives on knowable days: salaries near month-end, pensions and grants early in the month, school calendars and season on top. Sales follow that calendar line by line, and every line follows it differently. Staples sell flat. Payday proteins spike. Averages smear the two together and lie about both.</p>
<h2>Why national averages fail rural stores</h2>
<p>An ordering system tuned on national averages assumes the demand curve is flat and the truck can come tomorrow. A rural store ordered off that assumption runs empty in the payday window and overstocked in the quiet mid-month. The store that respects its rhythm builds stock into the busy window on the deliveries before it and slows buying as the town&rsquo;s wallet empties.</p>
<h2>A worked example</h2>
<p>Two lines in the same store. Long-life milk sells at nearly the same rate in a quiet week and a payday week. It is a daily anchor and wants depth all month. Frozen chicken portions sell hot at month-end, payday protein. The rhythm approach tags each line with its own shape, so the milk refills deep and steady while the chicken order builds into the payday window. One store, two rhythms, two correct orders.</p>
<h2>What it replaces</h2>
<p>Flat averages, national assumptions and the trailing four-week baseline that quietly compares a payday week with a mid-month week and calls the difference a trend. Baselines must respect the pay cycle or they lie.</p>
"""},
{
 "slug": "capital-velocity", "name": "Capital Velocity",
 "q": "What is capital velocity in retail?",
 "definition": "Capital Velocity is a retail finance principle that judges stock by what it does, not by what it costs. Stock value on a balance sheet says nothing about health. The question is how fast each rand invested in stock returns through the till, line by line, and what share of the stock investment is working at all.",
 "body": """
<h2>The idea</h2>
<p>Two stores hold a million in stock. One turns it every three weeks. The other has half of it sitting in a stockroom aging toward worthless. Same balance sheet line, opposite businesses. Stock is capital wearing a disguise, and most owners can quote the cost of theirs but not its speed.</p>
<h2>Working, slow and dead</h2>
<p>Every line&rsquo;s stock belongs to one of three states. Working capital sells and replaces itself. Slow capital sells, but far below the depth held. Dead capital has stopped selling and is now rent paid on regret. The split matters more than the total, because the cure differs: working capital wants availability protection, slow capital wants shallower buying, dead capital wants an exit plan, not another order.</p>
<h2>The trap inside the number</h2>
<p>Stock value is only as true as the ledger behind it. Phantom records, wrong unit costs and pack errors inflate apparent capital with money that never existed. A case cost captured as a unit cost turns one shelf of stock into a small fortune on paper. Before capital can be managed it must be purified, which is why capital work starts with ledger integrity, not with a spreadsheet of the totals. See <a href="/method/presence-law/">the Presence Law</a>.</p>
<h2>What it replaces</h2>
<p>Judging stock by its total value, celebrating a full stockroom and the fast cheap line subsidising the slow proud one without anyone deciding it should.</p>
"""},
{
 "slug": "story-test", "name": "The Story Test",
 "q": "How do you verify a data-driven decision in retail?",
 "definition": "The Story Test is a data verification discipline stating: no verdict ships without carrying its own reason. For any automated conclusion about a product, you must be able to tell that product&rsquo;s story in one plain-language paragraph, and the story must make sense to a person who knows the floor. Where the story stops making sense, the analysis is wrong, whatever the numbers say.",
 "body": """
<h2>Why stories beat thresholds</h2>
<p>Automated rules fail in ways audits of the rules never catch, because the rule is applied confidently to a situation it never anticipated. Recycled barcodes, twin product codes, production lines wearing retail codes. The arithmetic is right and the conclusion absurd. A human reading the product&rsquo;s biography spots the absurdity in seconds, because a biography has to cohere and a threshold does not.</p>
<h2>The test in practice</h2>
<p>Take any line the system wants to act on. Tell its story: what it is, how it arrives, how it sells, what the ledger claims and why. A beer line about to be flagged as a production error turns out to have fifty recycled codes in its history. The verdict changes because the story would not cohere. Every engine verdict we ship surfaces its reason to the human who acts on it, and the reason travels with the number wherever the number goes.</p>
<h2>Who this is for</h2>
<p>Any retailer buying analytics. Ask one question of any system offered to you: for this specific product, why? If the answer is a score without a story, you are being asked to trust arithmetic you cannot inspect. Insist on the reason, or decline the verdict.</p>
<h2>What it replaces</h2>
<p>Black-box scores, threshold-only audits and the meeting where a printout wins an argument the shelf would have lost.</p>
"""},
{
 "slug": "two-worlds", "name": "The Two Worlds",
 "q": "Why do supermarket stock systems fail on fresh departments?",
 "definition": "The Two Worlds is a retail classification principle stating that every supermarket runs two different businesses on one stock ledger: the buy-and-sell world, where a product arrives and leaves on the same code, and the made-in-store world, where ingredients become products the till has never met. A line&rsquo;s world is determined by its behaviour, not by its department label, and each world needs its own ledger rules.",
 "body": """
<h2>The two worlds</h2>
<p>In the buy-and-sell world a case of soft drinks arrives on a barcode and sells on the same barcode. The ledger&rsquo;s arithmetic has a fair chance. In the made-in-store world flour arrives, bread leaves. A carcass arrives, mince and steak leave. The ingredient code accumulates ghost stock it never sold, while the product codes sell stock the ledger never received. One production event, two absurdities, and both look like errors to a system built for the first world only.</p>
<h2>Behaviour decides, not the label</h2>
<p>Department labels lie. A bakery sells buy-and-sell rusks beside made-on-site bread. A butchery sells vacuum-packed boxes beside block-room cuts. The world a line lives in shows in its movement pattern: what arrives on the code, what leaves on it, and whether the two could belong to the same physical object. Classify by behaviour and the absurdities resolve into one coherent story per family.</p>
<h2>Why owners should care</h2>
<p>Fresh departments are where supermarkets win customers and where ledgers break worst. Negative stock on the mince, ghost stock on the carcass, phantom capital on both. Treat those as one production story instead of two errors and the counts, the costing and the ordering all start working. Treat them as errors and staff learn to distrust every number the system shows.</p>
<h2>What it replaces</h2>
<p>One-size ledger rules, fresh departments written off as uncountable and adjustment journals doing the work classification should do.</p>
"""},
{
 "slug": "daily-count-law", "name": "The Daily Count Law",
 "q": "How often should a store count stock?",
 "definition": "The Daily Count Law is a stocktake discipline stating that a store should count a little every day, on a prioritised list the data generates, rather than everything once a year. The count programme sizes itself from the store&rsquo;s own uncertainty: lines with the most value and the least recent proof of presence rise to the top, and the cycle guarantees every line is proven fresh within its window.",
 "body": """
<h2>Why the annual stocktake fails</h2>
<p>The annual count is a snapshot of chaos taken under time pressure by tired people, reconciled weeks later and stale before the report prints. For eleven months and thirty days it protects nothing. Errors born the day after live a full year, feeding wrong orders the whole time.</p>
<h2>The law in practice</h2>
<p>Each day the data proposes a short count list a person completes inside a normal shift. Selection is not random: value at risk, time since last proof and the line&rsquo;s own instability decide priority. High-value lines with quiet ledgers and fat stock claims lead, because that is where the money and the doubt overlap. Every completed count converts a claim into a proof, per <a href="/method/presence-law/">the Presence Law</a>, and the ordering engine treats it accordingly.</p>
<h2>The compounding effect</h2>
<p>A store counting thirty well-chosen lines a day quietly proves thousands of lines a quarter, concentrated exactly where errors cost most. Shrinkage stops hiding in year-old numbers. The stocktake stops being an event and becomes a heartbeat, and the ledger stops drifting because drift gets caught in days.</p>
<h2>What it replaces</h2>
<p>The annual big bang, the closed store, the casual-labour count teams and the write-off nobody could trace by the time it was found.</p>
"""},
{
 "slug": "drop-cover", "name": "Drop Cover",
 "q": "How should a store measure supplier delivery frequency?",
 "definition": "Drop Cover is a replenishment principle stating that a delivery rhythm is proven by what actually arrived, never by what the system is configured to expect. Supplier cadence is derived from the store&rsquo;s own receiving history, and each order covers the true gap to the next drop, as the receipts prove it, not as the schedule promises it.",
 "body": """
<h2>The idea</h2>
<p>Every ordering system holds a belief about how often the truck comes. Weekly, twice a week, fortnightly. That belief is configuration, typed in once and trusted forever. The receiving history tells the truth, and the truth churns: routes change, reps change, a fortnightly line quietly becomes monthly. A store bank we studied showed hundreds of sustained delivery-day switches in under two years. Order to the configured rhythm and every switch silently starves or floods the shelf.</p>
<h2>The law in practice</h2>
<p>Cadence is read from receipts, per supplier per store, and re-read continuously so a regime change resets the read. The order then buys the gap the evidence supports. When the gap to the next drop is long, depth goes up. When the truck comes twice a week, depth comes down and the capital goes to work somewhere else, per <a href="/method/capital-velocity/">Capital Velocity</a>.</p>
<h2>The month-end connection</h2>
<p>Drop cover is how <a href="/method/community-rhythm/">Community Rhythm</a> lands in practice. The busy window is built on the last deliveries before it. Delivery days anchor the timing, so the stock lands as the money arrives, not after it has been spent somewhere else.</p>
<h2>What it replaces</h2>
<p>Configured lead times nobody re-checks, fixed order days that ignore what arrives and the quiet stockouts caused by a schedule the supplier abandoned months ago.</p>
"""},
{
 "slug": "base-rate-rule", "name": "The Base-Rate Rule",
 "q": "How do you test a retail belief against data?",
 "definition": "The Base-Rate Rule is an evidence discipline for retail stating: one swallow does not make a summer. No belief about a store survives without a control. A pattern observed once is a hypothesis, never a law, and any claimed finding must state the base rate it was measured against, or it is not a finding.",
 "body": """
<h2>Why retail folklore wins arguments and loses money</h2>
<p>Retail runs on confident beliefs. The public holiday kills the Tuesday. This town does not buy premium. The promo always empties the shelf. Each was true once, somewhere, and each is retold as law. Beliefs formed from one vivid observation are the most dangerous kind, because a good story spends better than a good number in any meeting.</p>
<h2>The rule in practice</h2>
<p>Every claimed pattern faces a control before it earns a decision. Compare the holiday week to matched normal weeks, the same week of the pay cycle, before believing the holiday changed anything. We have watched a persuasive delivery-pattern law, confidently drafted, die against its own base rate: the measured difference was a fraction of a percent. The best-narrated finding of the day was the false one. Being proven wrong by your own data is the best news available, because it is the moment the store stops paying for a myth.</p>
<h2>Three grades of evidence</h2>
<p>A claim is true by construction, or it is measured against a stated base rate with a stated sample, or it is a single observation. Only the first two may run a store. The third earns an experiment, never a rule.</p>
<h2>What it replaces</h2>
<p>Folklore ordering, anecdote-driven range decisions and the loudest voice in the Monday meeting.</p>
"""},
{
 "slug": "fit-to-budget", "name": "Fit-to-Budget with KVI Floors",
 "q": "How should a store cut an order to fit its budget?",
 "definition": "Fit-to-Budget with KVI Floors is an ordering principle for fitting an order to a real buying budget without damaging the store: the known-value items your customers judge you by hold untouchable minimum floors, and the budget is met by scaling the flexible remainder. A budget cut spread evenly across all lines is a strategy for running out of exactly the products people came for.",
 "body": """
<h2>The problem it solves</h2>
<p>Every struggling store meets the same moment: the suggested order exceeds the money. The common responses are both wrong. Cut everything by a flat percentage and the bread, milk and beer run out with everything else, which the customer reads as a dying store. Cut whatever the owner feels less attached to and the cut is folklore, per <a href="/method/base-rate-rule/">the Base-Rate Rule</a>.</p>
<h2>The principle</h2>
<p>Known-value items are the short list of lines a community uses to judge a store: price-checked, walked-for, noticed when absent. Those lines carry floors the budget fit is not allowed to breach. The remainder of the order flexes: depth scales, marginal lines wait for the next drop and slow lines wait indefinitely. The store gets smaller for a while without ever getting emptier where it counts.</p>
<h2>The discipline behind it</h2>
<p>A KVI list is earned from the store&rsquo;s own sales behaviour and checked against it continuously. Flags in the system are trusted only when the data agrees with them. Packaging and consumables sell every single day and still never rank, because a carrier bag brings no one through the door.</p>
<h2>What it replaces</h2>
<p>Flat percentage cuts, panic ordering after the payday shelf gap and the slow drift where a budget crisis becomes an availability crisis becomes a customer crisis.</p>
"""},
]

def build(render, SITE):
    pages = []
    chips = "".join(f'<a class="chip" href="/method/{m["slug"]}/">{m["name"]}</a>' for m in METHODS)
    cards = "".join(f'''<a class="card rv" href="/method/{m["slug"]}/"><h3>{m["name"]}</h3><p>{m["definition"][:180].rsplit(" ",1)[0]}&hellip;</p><span class="more">Read the method →</span></a>''' for m in METHODS)

    map_nodes = [{"slug": m["slug"], "name": m["name"], "tag": MAP_TAGLINE[m["slug"]],
                  "x": MAP_POS[m["slug"]][0], "y": MAP_POS[m["slug"]][1]} for m in METHODS]
    map_json = json.dumps({"nodes": map_nodes, "edges": [list(e) for e in MAP_EDGES]}, ensure_ascii=False)

    index_body = f'''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Method Library</p>
  <span class="kicker">The Method Library</span>
  <h1>How we think, published</h1>
  <p class="lead">Named methods from the SocialBrand practice, each with a definition, the reasoning and a worked example. The thinking is the marketing. The mechanics, the formulas, thresholds and configuration values, stay our moat and our clients&rsquo; advantage. Author: {ATTR}.</p>
</div></div></section>
<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">How the methods connect</span><h2>The Method Map</h2>
  <p>Ten methods, one discipline. On a wide screen, point at a node to trace what it feeds and what feeds it. On any screen, open a method to read it in full.</p></div>
  <div class="method-map rv" id="methodMap" data-map='{map_json}'>
    <ul class="method-map-list">{chips}</ul>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="grid g2">{cards}</div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>See the methods run</h2><p>The live demo applies these methods to a fictional store with generated data. Every number carries its reason.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/demo/">Open the demo</a></div>
  </div>
</div></section>
<script src="/static/method-map.js" defer></script>
'''
    itemlist = {"@type": "ItemList", "name": "The SocialBrand Method Library",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": m["name"], "url": f'{SITE["url"]}/method/{m["slug"]}/'} for i, m in enumerate(METHODS)]}
    pages.append(render("/method/", "The Method Library | Named retail methods by PG van der Westhuizen, SocialBrand",
        "The SocialBrand Method Library: named, citable retail methods on stock integrity, ordering, capital and evidence, published at concept level by PG van der Westhuizen.",
        index_body, extra_schema=itemlist))

    for m in METHODS:
        url = f'/method/{m["slug"]}/'

        visual = ""
        if m["slug"] == "8-step-ordering-recipe":
            visual = ('<div class="method-map recipe-map" id="recipeMap" data-map=\''
                      + json.dumps(RECIPE_GATES).replace("'", "&#39;") + '\'>'
                      '<ol class="method-map-list"></ol>'
                      '<p class="rm-legend"><span><i></i> Buying any good system does</span>'
                      '<span><i class="key"></i> The gates that make it ours</span></p>'
                      '</div>')
        body = f'''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / <a href="/method/">Method Library</a> / {m["name"]}</p>
  <span class="kicker">{m["q"]}</span>
  <h1>{m["name"]}</h1>
  <p class="byline" style="color:var(--sky-muted)">By <b style="color:#fff">{ATTR}</b> · Published 19 July 2026</p>
</div></div></section>
<article class="sec"><div class="wrap"><div class="prose">
  <p class="defn"><strong>{m["name"]}.</strong> {m["definition"].split(" is ",1)[1] if " is " in m["definition"] else m["definition"]}</p>
</div></div>
<div class="wrap">{visual}</div>
<div class="wrap"><div class="prose">
  {m["body"]}
  <blockquote>&ldquo;The thinking is the marketing. The mechanics are the moat.&rdquo;</blockquote>
  <p><b>Attribution.</b> {m["name"]} is published by {ATTR}, from the working practice of Social Brands Investments (Pty) Ltd, South Africa. Cite it with that attribution. To see it applied, open the <a href="/demo/">live demo</a> or start with a <a href="/pricing/">Store Health Audit</a>.</p>
</div></div></article>
'''
        schema = [
            {"@type": "DefinedTerm", "name": m["name"], "description": m["definition"],
             "url": SITE["url"] + url,
             "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "The SocialBrand Method Library", "url": SITE["url"] + "/method/"}},
            {"@type": "Article", "headline": m["name"], "description": m["definition"],
             "author": {"@id": SITE["url"] + "/#pg"}, "publisher": {"@id": SITE["url"] + "/#org"},
             "datePublished": DATE, "mainEntityOfPage": SITE["url"] + url},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Method Library", "item": SITE["url"] + "/method/"},
                {"@type": "ListItem", "position": 2, "name": m["name"], "item": SITE["url"] + url}]}
        ]
        pages.append(render(url, f'{m["name"]} | The SocialBrand Method Library',
            m["definition"][:158].rsplit(" ", 1)[0] + "…", body, extra_schema=schema))
    return pages
