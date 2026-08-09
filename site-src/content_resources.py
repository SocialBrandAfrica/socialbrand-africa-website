# content_resources.py - Resources hub + five guides.
# Deviation from SB-WEB-001 section 7, recorded in the build record: guide content is fully
# public (LLM-first ruling A13b outranks gating), with an email capture for the printable
# versions and updates. Lead capture without content blocking.

CAPTURE = '''<div class="card" style="margin-top:40px"><h3>Get the printable pack</h3>
<p style="margin-top:8px;color:var(--fg-muted)">Leave your email and we send the print-ready versions of all five guides, plus new ones as they publish. Straight from Pieter, no sequence, unsubscribe any time.</p>
<form class="form" style="margin-top:16px" action="https://formsubmit.co/pieter@socialbrand.africa" method="POST" data-gate="pack">
  <input type="hidden" name="_subject" value="Resource pack request - socialbrand.africa">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
  <div style="display:flex;gap:10px;flex-wrap:wrap"><input type="email" name="email" required placeholder="you@yourstore.co.za" style="flex:1;min-width:220px"><button class="btn" type="submit">Send me the pack</button></div>
</form>
<p id="pack-ok" hidden style="margin-top:12px;color:var(--accent-ink);font-weight:600">Thank you. The pack is on its way to your inbox.</p></div>'''

GUIDES = [
{
 "slug": "data-health-checklist", "name": "The Store Data Health Checklist",
 "tag": "Free · start here",
 "teaser": "Twenty questions an owner answers in an hour to find out whether the store&rsquo;s numbers deserve trust. No software needed, only honesty and a walk to the shelf.",
 "body": """
<p class="defn"><strong>How to use this.</strong> Answer yes or no. Do it honestly, in the store, not from memory. Every no is a place your numbers are guessing, and every guess feeds your orders. Fifteen or more yes answers: your data is ahead of most independents. Ten to fourteen: the ledger needs a programme, not a patch. Below ten: stop trusting reports until the foundations are fixed. Your instinct is currently beating your system, which is why everything feels like firefighting.</p>

<h2>Sales data</h2>
<ol>
<li>Do yesterday&rsquo;s till totals reach you every morning without you asking anyone?</li>
<li>Do you compare weeks against the same week of the pay cycle, never against last week blindly?</li>
<li>Could you name your twenty highest-turnover lines from a report, and would the floor agree?</li>
<li>When a line stops selling, does anything in your business notice within a week?</li>
</ol>

<h2>Stock claims</h2>
<ol start="5">
<li>Pick five big-value lines on the stock report. Does the shelf plus stockroom count match the screen within a unit or two?</li>
<li>Is every negative stock figure in the business explained, or at least being worked?</li>
<li>Do quiet lines with large stock claims get physically checked before anyone orders against them?</li>
<li>Would you bet a week&rsquo;s profit on the accuracy of your top ten stock claims?</li>
</ol>

<h2>Receiving</h2>
<ol start="9">
<li>Is every delivery captured against the exact product codes on the invoice, same day?</li>
<li>Do case sizes and pack sizes get checked at capture, not discovered at stocktake?</li>
<li>When receipts and sales disagree on a line for the second time, does someone chase the movement rather than correct the number?</li>
</ol>

<h2>Counting</h2>
<ol start="12">
<li>Does somebody count something every single trading day?</li>
<li>Are counts chosen by value and doubt, rather than by whatever aisle is convenient?</li>
<li>Are made-in-store departments counted by their own rules, instead of being forced through barcode arithmetic?</li>
<li>After a count corrects the system, does anyone ask why the system was wrong?</li>
</ol>

<h2>Costs and capital</h2>
<ol start="16">
<li>Are unit costs on your top hundred lines current, checked against recent invoices?</li>
<li>Would a case cost captured as a unit cost be caught in your business within a month?</li>
<li>Do you know what share of your stock value sold nothing in the last quarter?</li>
<li>Do deposit lines, crates and returnables live on their own codes, reconciled and never zeroed?</li>
<li>If a report and the floor disagree, does your team believe the floor and fix the report?</li>
</ol>
"""},
{
 "slug": "stocktake-discipline", "name": "The Stocktake Discipline Guide",
 "tag": "Counting",
 "teaser": "Why counting a little every day beats the annual big bang, and how to run a daily count programme inside a normal shift.",
 "body": """
<p class="defn"><strong>The principle.</strong> The annual stocktake is a snapshot of chaos taken by tired people and reconciled too late to teach anyone anything. A daily count programme proves a store&rsquo;s stock continuously: a short, prioritised list every day, completed inside a normal shift, concentrated where value and doubt overlap.</p>
<h2>Why the big bang fails</h2>
<p>An error born in January lives eleven months before the December count finds it, feeding wrong orders the whole time. By the time the variance report prints nobody remembers the delivery that caused it. The count closes the store, burns the team and produces a write-off nobody traces. Then the ledger starts drifting again on 2 January.</p>
<h2>The daily discipline</h2>
<ol>
<li><b>Size it honestly.</b> Twenty to forty lines a day per store is enough. The point is rhythm, not heroics.</li>
<li><b>Choose by value and doubt.</b> Big claims with old proof lead the list. A line counted last week does not need counting again this week, whatever the aisle walk suggests.</li>
<li><b>Count against the claim, blind.</b> The counter records what the shelf holds. Compare to the system afterwards. A counter who knows the expected number finds the expected number.</li>
<li><b>Chase the movement, not the variance.</b> A wrong number is a symptom. The cause lives in receiving, production or a twin code, and fixing the cause is the only fix that lasts.</li>
<li><b>Log every correction.</b> Corrections per hundred lines counted is your ledger&rsquo;s health score. Watch it fall as the causes get fixed.</li>
</ol>
<h2>What changes after ninety days</h2>
<p>Thousands of lines proven, concentrated at the top of the value range. Shrinkage patterns visible in weeks instead of years. Orders leaning on numbers a person recently proved. The stocktake stops being an event and becomes a heartbeat.</p>
"""},
{
 "slug": "ordering-readiness", "name": "The Ordering Readiness Self-Assessment",
 "tag": "Ordering",
 "teaser": "Is your store ordering from data or from habit? Twelve questions to place your store on the ladder from gut ordering to generated ordering.",
 "body": """
<p class="defn"><strong>The ladder.</strong> Every store orders on one of four rungs: gut, where the person orders what feels right. Rep, where the supplier decides. Report, where a system suggests off numbers nobody audits. Or truth, where orders generate from demonstrated demand on a ledger somebody proves daily. Most independents live on the first two rungs and pay for it in both directions, empty shelves and dead stock at once.</p>
<h2>The twelve questions</h2>
<ol>
<li>Does anyone in the business know each top line&rsquo;s true rate of sale, corrected for the days it stood empty?</li>
<li>Do your orders change when the shelf was empty half of last week, or does the system read the low sales as low demand?</li>
<li>Does the order build ahead of payday, or react after it?</li>
<li>Do pack families read as one product, so the case and the single stop hiding each other&rsquo;s demand?</li>
<li>Are there lines a rep decides for you, and could you say what they cost you last quarter?</li>
<li>Does your ordering respect each supplier&rsquo;s real delivery rhythm as the receipts prove it, or a schedule someone typed in years ago?</li>
<li>When money is tight, do your must-have lines keep their depth while the flexible lines scale?</li>
<li>Can you see tomorrow&rsquo;s suggested order before it is placed, line by line, with a reason per line?</li>
<li>Is dead stock excluded from reordering automatically, or does it depend on someone remembering?</li>
<li>Does a new line get a fair trial with a review date, or does it drift into the range forever?</li>
<li>Did your last stock reduction come from a plan, or from running out?</li>
<li>If your best orderer left tomorrow, would the ordering survive?</li>
</ol>
<h2>Reading your score</h2>
<p>Count your yes answers. Nine or more: you are close to the top rung, and automation would compound what already works. Five to eight: the pieces exist and the discipline is partial, start with demand truth and delivery rhythm. Under five: do not automate anything yet. Automation built on an unproven ledger repeats mistakes faster. Fix presence first, then demand, then let the machine help.</p>
"""},
{
 "slug": "negative-stock-triage", "name": "The Negative Stock Triage Guide",
 "tag": "Ledger repair",
 "teaser": "What a minus on the stock ledger actually means, the three causes behind almost every negative, and the first three actions to take.",
 "body": """
<p class="defn"><strong>What a negative means.</strong> A negative stock figure is the ledger confessing. It says: I recorded more going out than I ever recorded coming in. The units were real, customers bought them. What is broken is the paper trail, and the minus is your best clue to where. Never zero a negative to make a report look clean. You are deleting the confession and keeping the crime.</p>
<h2>The three causes</h2>
<ol>
<li><b>The receipting break.</b> Deliveries post to one code, sales ring on another. Twins, recycled barcodes, a new pack size on an old code. The negative grows a little with every delivery cycle. The tell: a healthy-selling line, deeply negative, with a sibling code hoarding stock that never sells.</li>
<li><b>The production line.</b> Ingredients arrive on one code and leave as something else. Flour becomes bread, a carcass becomes mince and steak. The product codes go negative while the ingredient codes grow ghosts. The tell: fresh departments, and the negative roughly mirrors a fat claim nearby.</li>
<li><b>The uncaptured movement.</b> Returns, transfers between branches, deposits and crate cycles, wastage never written off. The tell: irregular jumps rather than steady growth, and deposit or returnable lines deep in the minus.</li>
</ol>
<h2>The first three actions</h2>
<ol>
<li><b>Rank by value, not by count.</b> Multiply each negative by its cost and work the rand list top down. Twenty lines usually carry most of the money.</li>
<li><b>Read each line&rsquo;s story before touching it.</b> What arrives on this code, what leaves on it, which sibling could be its twin? The pattern names the cause, and the cause names the fix: receiving correction, production rules or a reconciliation.</li>
<li><b>Count the family, fix the source, then correct the number.</b> A physical count of the live code and its twins sets the true position. The source fix stops the bleed. Only then does the correction hold. A number corrected before the cause is fixed is broken again by the next delivery.</li>
</ol>
<p>One exception is sacred: deposit and returnable lines. Those negatives are real money circulating in crates and bottles. Reconcile them, never zero them.</p>
"""},
{
 "slug": "owners-morning-questions", "name": "The Owner&rsquo;s Morning Questions",
 "tag": "Operational freedom",
 "teaser": "The ten questions a store should answer for its owner before 08:00, without a phone call. How far is your store from answering them?",
 "body": """
<p class="defn"><strong>The standard.</strong> A well-run store answers its owner&rsquo;s ten questions by 08:00, from systems, without anyone being phoned, wherever the owner is standing. Every question below that needs a phone call marks a place where the business depends on a person&rsquo;s memory instead of a process. That dependence is what keeps owners trapped in their own stores.</p>
<h2>The ten questions</h2>
<ol>
<li>What did each store sell yesterday, and how does it sit against the same day of the pay cycle?</li>
<li>What is today, in this town? Payday build, grant window, school event, weather turning. What does the town need the store to be today?</li>
<li>Which of the lines this community judges us by are out of stock right now, and when does each come back?</li>
<li>What arrived yesterday, and did every delivery land on the right codes at the right costs?</li>
<li>What gets counted today, and what did yesterday&rsquo;s counts correct?</li>
<li>What is being made in the fresh departments today, and does it match what this week actually sells?</li>
<li>Which orders leave today, and could each line say why it was ordered?</li>
<li>Where did we give money away yesterday? Wastage, markdowns, refunds, voids, and which of them repeat?</li>
<li>Who is on the floor today, and is anyone about to become the single point of failure?</li>
<li>What one thing, fixed this week, would this whole list feel first?</li>
</ol>
<h2>The test behind the test</h2>
<p>Read the list again and mark each question your business answers today without a call. Six or more: your systems are carrying you, well done, tighten the rest. Three to five: the store runs on heroics, and heroics do not scale and do not take leave. Two or fewer: you do not own a store so much as a job with stock. That is fixable, and the fix is a sequence, data truth first, then discipline, then automation.</p>
<p>The owner at the rugby field on a Saturday morning, phone in pocket, already knowing the soup got made, is not a fantasy. It is what these ten questions look like once systems answer them. That is the operational freedom the whole method serves.</p>
"""},
]

def build(render, SITE):
    pages = []
    cards = "".join(f'''<a class="card rv{' flag' if i == 0 else ''}" href="/resources/{g["slug"]}/"><span class="tag">{g["tag"]}</span><h3 style="margin-top:14px">{g["name"]}</h3><p>{g["teaser"]}</p><span class="more">Open the guide →</span></a>''' for i, g in enumerate(GUIDES))
    index_body = f'''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Resources</p>
  <span class="kicker">Resources</span>
  <h1>Tools you use before you pay us anything</h1>
  <p class="lead">Five working guides from the practice. Real value, no fluff, each usable this week in a real store. Read them here, or leave an email for the printable pack.</p>
</div></div></section>
<section class="sec"><div class="wrap">
  <div class="grid g2">{cards}</div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Two minutes, no call</span><h2>Find out where your store stands</h2>
  <p>Eight questions. Answer honestly and you get a straight read on which of the three legs your store needs first, and what the sensible next step costs. Nothing here goes anywhere until you choose to send it.</p></div>
  <div class="quiz rv" id="quiz">
    <form class="quiz-form" id="quizForm" action="https://formsubmit.co/pieter@socialbrand.africa" method="POST">
      <input type="hidden" name="_subject" value="Store readiness questionnaire - socialbrand.africa">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <input type="hidden" name="result" id="quizResult">
      <ol class="quiz-qs">
        <li class="quiz-q" data-leg="analytics"><p>The stock figure on screen and the shelf regularly disagree.</p><div class="quiz-opts" role="group" aria-label="The stock figure on screen and the shelf regularly disagree"><button type="button" data-v="2">Often</button><button type="button" data-v="1">Sometimes</button><button type="button" data-v="0">Rarely</button></div></li>
        <li class="quiz-q" data-leg="turnaround"><p>Month-end profit surprises me, in either direction.</p><div class="quiz-opts" role="group" aria-label="Month-end profit surprises me"><button type="button" data-v="2">Often</button><button type="button" data-v="1">Sometimes</button><button type="button" data-v="0">Rarely</button></div></li>
        <li class="quiz-q" data-leg="operations"><p>If I take two weeks off, standards slip.</p><div class="quiz-opts" role="group" aria-label="If I take two weeks off standards slip"><button type="button" data-v="2">Definitely</button><button type="button" data-v="1">A little</button><button type="button" data-v="0">Not really</button></div></li>
        <li class="quiz-q" data-leg="analytics"><p>Ordering happens on habit or on a rep&rsquo;s suggestion, not on demand.</p><div class="quiz-opts" role="group" aria-label="Ordering happens on habit"><button type="button" data-v="2">Mostly</button><button type="button" data-v="1">Partly</button><button type="button" data-v="0">No</button></div></li>
        <li class="quiz-q" data-leg="turnaround"><p>Suppliers or creditors are putting pressure on the account.</p><div class="quiz-opts" role="group" aria-label="Suppliers are putting pressure on the account"><button type="button" data-v="2">Yes</button><button type="button" data-v="1">Starting to</button><button type="button" data-v="0">No</button></div></li>
        <li class="quiz-q" data-leg="operations"><p>New staff learn the job by watching someone, not from anything written.</p><div class="quiz-opts" role="group" aria-label="New staff learn by watching"><button type="button" data-v="2">Yes</button><button type="button" data-v="1">Some of it is written</button><button type="button" data-v="0">It is all documented</button></div></li>
        <li class="quiz-q" data-leg="analytics"><p>Somebody counts stock every trading day.</p><div class="quiz-opts" role="group" aria-label="Somebody counts stock every trading day"><button type="button" data-v="0">Yes, daily</button><button type="button" data-v="1">Now and then</button><button type="button" data-v="2">Only at stocktake</button></div></li>
        <li class="quiz-q" data-leg="turnaround"><p>I can see yesterday&rsquo;s numbers before 08:00 without phoning anyone.</p><div class="quiz-opts" role="group" aria-label="I can see yesterday numbers before 8am"><button type="button" data-v="0">Yes</button><button type="button" data-v="1">Sometimes</button><button type="button" data-v="2">No</button></div></li>
      </ol>
      <div class="quiz-out" id="quizOut" hidden aria-live="polite"></div>
      <div class="quiz-send" id="quizSend" hidden>
        <p class="note">Want this read on your actual numbers? Send it to Pieter and he will reply himself.</p>
        <div class="quiz-fields">
          <input type="text" name="name" placeholder="Your name" aria-label="Your name" required>
          <input type="email" name="email" placeholder="you@yourstore.co.za" aria-label="Your email" required>
          <input type="text" name="store" placeholder="Store name" aria-label="Store name">
        </div>
        <button class="btn" type="submit">Send my result</button>
      </div>
    </form>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="grid g2" style="align-items:start">
    <div class="card flag rv">
      <span class="tag">Coming soon</span>
      <h3 style="margin-top:14px">The Retailer&rsquo;s Handbook</h3>
      <p style="margin-top:10px">We are writing the book we wanted when we started: how an independent store actually gets its numbers, its shelves and its people under control. Everything the practice has learned, in one place, in plain language.</p>
      <p style="margin-top:12px">It will be free on Amazon Books when it lands. No launch date yet, because we would rather finish it properly than announce a month.</p>
      <form class="form" style="margin-top:18px" action="https://formsubmit.co/pieter@socialbrand.africa" method="POST" data-gate="ebook">
        <input type="hidden" name="_subject" value="Retailers Handbook waitlist - socialbrand.africa">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
        <div style="display:flex;gap:10px;flex-wrap:wrap"><input type="email" name="email" required placeholder="you@yourstore.co.za" aria-label="Your email" style="flex:1;min-width:200px"><button class="btn" type="submit">Tell me when it lands</button></div>
      </form>
      <p id="ebook-ok" hidden style="margin-top:12px;color:var(--accent-ink);font-weight:600">Thank you. We will let you know the day it goes live.</p>
    </div>
    <div class="rv">{CAPTURE}</div>
  </div>
</div></section>
'''
    pages.append(render("/resources/", "Free retail resources | Checklists, guides and the Retailer's Handbook",
        "Five practical retail guides, a two-minute store readiness questionnaire and the Retailer's Handbook, coming free on Amazon Books.",
        index_body))

    for g in GUIDES:
        url = f'/resources/{g["slug"]}/'
        plain_name = g["name"].replace("&rsquo;", "'")
        body = f'''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / <a href="/resources/">Resources</a> / {g["name"]}</p>
  <span class="kicker">{g["tag"]}</span>
  <h1>{g["name"]}</h1>
  <p class="byline" style="color:var(--sky-muted)">From the working practice of <b style="color:#fff">SocialBrand</b> · Print this page, or use it on your phone on the floor</p>
</div></div></section>
<article class="sec"><div class="wrap"><div class="prose">
{g["body"]}
<p><b>What next.</b> If this guide found problems, the <a href="/pricing/">Store Health Audit</a> quantifies them in rand and hands you the plan. If it found none, your store is rarer than you think.</p>
</div>
<div class="prose" style="margin-top:10px">{CAPTURE}</div>
</div></article>
'''
        schema = {"@type": "Article", "headline": plain_name, "description": g["teaser"].replace("&rsquo;", "'"),
                  "author": {"@id": SITE["url"] + "/#pg"}, "publisher": {"@id": SITE["url"] + "/#org"},
                  "datePublished": "2026-07-19", "mainEntityOfPage": SITE["url"] + url}
        pages.append(render(url, f"{plain_name} | SocialBrand Resources",
            g["teaser"].replace("&rsquo;", "'")[:158], body, extra_schema=schema))
    return pages
