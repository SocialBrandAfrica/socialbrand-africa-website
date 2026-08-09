# content_audit.py - SB-WEB-011 Part B: /audit/, the Store Health Audit order page
# Copy is final text per SB-WEB-011 (2026-08-09), reproduced verbatim below except where
# DEV NOTEs in the brief called for developer judgement on markup/wiring only.


def build(render, SITE):
    pages = []

    body = '''
<style>
.audit-form fieldset{border:1.5px solid var(--line-2);border-radius:11px;padding:16px 18px;margin:0}
.audit-form legend{font-weight:600;font-size:.92rem;padding:0 6px}
.audit-form .radio-opt{display:flex;align-items:flex-start;gap:10px;font-weight:400;margin-top:10px;cursor:pointer}
.audit-form .radio-opt:first-of-type{margin-top:0}
.audit-form input[type=radio],.audit-form input[type=checkbox]{width:auto;flex:none}
.audit-form h3{margin-top:36px;padding-top:20px;border-top:1px solid var(--line-2)}
.audit-form h3:first-of-type{margin-top:6px;padding-top:0;border-top:none}
@media print {
  header.hdr, footer.ftr, .cmdk, .audit-noprint { display:none !important; }
}
</style>
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Pricing / Order the audit</p>
  <span class="kicker">Store Health Audit</span>
  <h1>Order the Store Health Audit</h1>
  <p class="lead">The audit is the door. One store, a fixed fee of R35,000, two to three weeks, findings in rand. This page is the whole deal: the process, what you get, what we need from you, the lane we work in, the terms and the order form. It is a working agreement between two businesses, written in plain language, not a legal contract drafted by an attorney. If you want yours to look at it before you submit, that is sensible, download it below and we will wait. Read it once and you know everything.</p>
  <div class="audit-noprint" style="margin-top:20px"><button type="button" class="btn btn-o" onclick="window.print()">Download / print this page</button></div>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The process</span><h2>How it works, step by step</h2></div>
  <ol class="tick-list rv">
    <li>Complete the questionnaire on this page and submit. Your submission is your acceptance of the terms below, the day it lands is your commencement date, and your booking is payable as set out in the terms. Nothing moves out of your account yet.</li>
    <li>We read every line before we speak to you, so the first call starts where it should, not at the beginning. We contact you within two working days to arrange access to your numbers.</li>
    <li>We connect your data and build the first version of your live dashboard, a standard build fed from your own database, typically up within a day or two of access being granted: your turnover, your departments, what is moving and what has stopped, on your own phone, without waiting for anyone to phone you with figures. The first 50% falls due at that live dashboard, and that payment is the booking of your audit. You pay nothing before you can see your own numbers working.</li>
    <li>The audit runs, two to three weeks from commencement. Findings reach you in pieces as they are proven, not in one book at the end, because three weeks is too short to find everything first and act afterwards. Whatever we find, you can act on in the same week. While the audit runs you have us in your corner: two calls a week, short written updates on the other days, questions answered, quick fixes handed over as they land. That handholding period is a deliverable of the audit itself, not a courtesy.</li>
    <li>The audit is presented: the findings, the plan and everything behind them, in one book. The remaining 50% is due on that date. If it is not paid immediately, it remains due and payable from that date. Everything is yours to keep whether we ever work together again or not.</li>
    <li>You choose the road, or no road at all. No lock-in past the audit.</li>
  </ol>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Scope</span><h2>What the audit covers</h2></div>
  <p class="rv" style="max-width:78ch"><b>Your money:</b> where your sales go, your real gross profit and how cash moves through the month. <b>Your stock:</b> how much cash sits on your shelves, what sells and what is dead weight you pay to hold. <b>Your ledger:</b> whether the figures your system shows you deserve trust. <b>Your ordering:</b> buying to demand or buying to habit, and what the gap costs weekly. <b>Your leaks:</b> shrinkage, waste, pricing errors and margin lost at the till. Everything tested against your own till and ledger data, nothing quoted to you until it has passed that test.</p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The deliverables</span><h2>What you get, and keep</h2></div>
  <div class="grid g2" style="align-items:start">
    <div class="card rv"><h3>1. The live dashboard</h3><p>A standard build fed from your own database, up within the first days and running right through the audit. It is a window on your business and our progress report to you in one place: you watch the store and you watch us working. It stays up after the audit, indefinitely, as long as the installations on your server that feed it are left undisturbed.</p></div>
    <div class="card rv"><h3>2. The handholding period</h3><p>Direct access to us for the duration: two calls a week, one to report what has been found and one to ask what only you can answer, with short written updates in between. Interim findings and quick fixes handed over the week they are proven.</p></div>
    <div class="card rv"><h3>3. The findings</h3><p>What is happening in your store, each finding stated in rand, with the arithmetic shown and the source named. A short read for your phone, the full findings for your desk and the working papers behind every figure.</p>
      <p style="margin-top:10px"><a class="more" style="font-weight:600;color:var(--accent-ink)" href="/audit/sample-findings/">See a sample finding &rarr;</a></p></div>
    <div class="card rv"><h3>4. The plan</h3><p>What to do, in what order, ranked by what each move puts back in your pocket, with owners and dates against every action.</p></div>
    <div class="card rv" style="grid-column:1/-1"><h3>5. The book</h3><p>The whole audit compiled into one document at the end: findings, plan, systems notes, the record of what was found and what was already acted on. It closes the audit, it is not the first time you see any of it.</p></div>
  </div>
  <p class="rv" style="margin-top:20px;color:var(--fg-muted)">All five are yours to keep, use and act on, whether or not you ever work with us again.</p>
</div></section>

<section class="sec sec-sky"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Scope of advice</span><h2>The lane. What we advise on, and what we do not</h2>
  <p>The mandate is one thing: turn the business around. Every recommendation is measured against that and nothing else.</p></div>
  <p class="rv" style="max-width:78ch">We advise on where money goes into the business. Which stock to buy first, which lines to carry, which suppliers to protect, where margin leaks, what the range should be. The bias is stated openly: toward the trading business, toward turnover and toward margin. Paying the supplier who keeps your shelves full is a buying decision, so trade creditors sit inside the lane.</p>
  <p class="rv" style="margin-top:14px;max-width:78ch">Your debt sits outside the lane and stays outside. We are not financiers, bankers or financial advisors. We will not tell you how to restructure a loan, who to settle with or how to raise money. What we will do is show you what the trading business can carry, honestly and in your own numbers, so you and the people qualified for those decisions can make them on real information. Also outside: tax, statutory accounting, labour law and legal opinion. For those, use a registered professional, and we gladly work alongside yours.</p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Consent</span><h2>Permission. Nothing happens without yours</h2></div>
  <p class="rv" style="max-width:78ch">Nothing is done with your data or inside your business without your express permission first. That covers what we may copy from your system and what we may do with it, any new use of your data beyond what was agreed, any instruction reaching your staff (we advise you, you mandate them, we do not issue instructions in your business), any approach to a supplier, landlord, bank or other third party on your behalf, and any use of your business name anywhere. You may withdraw any permission at any time.</p>
  <p class="rv" style="margin-top:14px;max-width:78ch">Two permissions make the audit work. Your submission of this page grants the first: permission to read and analyse the business data you share with us, read-only, for this audit. The second is a separate short authorisation letter, signed when we connect your dashboard: it lets us collect, each night, the backup copy your system already writes on its own. Nothing is installed on your machine, nothing changes on it and nothing is ever written back to your system. Not a price, not a stock figure, not a correction. Your database is read, never touched, and your tills are never slowed because collection happens hours after they stop.</p>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">What we need</span><h2>What we need from you and your team</h2>
  <p>The audit fails without these, said plainly so there is no surprise later.</p></div>
  <ol class="tick-list rv">
    <li><b>Your people take it seriously.</b> This is the one that decides whether any of it works. An action plan nobody implements returns nothing, and it will still have cost you the fee. Your manager and your buyers need to hear from you, not from us, that this is not optional.</li>
    <li><b>You back it publicly.</b> If the floor believes you are only half behind it, they will wait it out. Half a mandate is worse than none.</li>
    <li><b>Somebody answers within a working day.</b> Usually you or your manager. Name that person on the form.</li>
    <li><b>Documents arrive when asked for.</b> Management accounts, supplier statements, a recent stock take, till reports, whatever exists. Photos of printed pages are fine. If something does not exist, say so. A missing report is a finding, not a failure.</li>
    <li><b>The authorisations above, when we ask for them.</b></li>
    <li><b>Honest answers, including uncomfortable ones.</b> We will find what is there. Being told first is always cheaper.</li>
  </ol>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Timing</span><h2>The clock, in plain terms</h2></div>
  <p class="rv" style="max-width:78ch">Your commencement date is the day your submission lands, and the two to three week count to your delivered audit runs from that day. Delays on access, paperwork or answers do not pause the clock, they eat into it. The same goes for what we hand you during the handholding period: what you implement immediately starts paying immediately, what waits costs you. Move fast and the audit starts paying for itself before it is even delivered.</p>
  <p class="rv" style="margin-top:14px;max-width:78ch">If a payment that has fallen due is withheld, the handholding stops until the account is right, and the clock keeps counting. It is your audit and your weeks, spend them well. If the timing of a payment is difficult, say so and we stagger it. That is a conversation, not a concession, and better had before than after.</p>
</div></section>

<section class="sec sec-sky"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">How findings move</span><h2>The audit changes as we learn, the deal does not</h2></div>
  <p class="rv" style="max-width:78ch">We do not yet know everything about your business, and neither do you. That is the point of the work. Each finding changes what is worth doing next: a week on availability may show the real problem is buying. When that happens we say so and agree the new direction with you before following it. What never changes is the fee, the mandate and the lane. What changes is where the effort points.</p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">On projections</span><h2>What a number is worth</h2></div>
  <p class="rv" style="max-width:78ch">Numbers about the past are measurements from your own system, reconciled against your own reports, and we stand behind them. Numbers about the future are best estimates on the facts of the day, never a promise or a guarantee. Context moves: a competitor opens, a supplier stops, weather kills a weekend. So every projection comes with its assumptions written next to it, and when an assumption breaks we tell you the number changed rather than let you plan against it.</p>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Read this before you submit</span><h2>The terms</h2></div>
  <ol class="tick-list rv" style="max-width:80ch">
    <li><b>Service:</b> Store Health Audit, one store, fixed fee R35,000. Fixed means fixed, it does not move with the hours. No VAT is charged at present.</li>
    <li><b>Ordering:</b> the audit is ordered by submitting this page, or by a verbal go-ahead, or by written email confirmation. Any of the three brings these terms into force, and the date of that order is the commencement date. Where the order is verbal or by email, this page is sent to you as the record of the terms.</li>
    <li><b>Payment:</b> the audit is payable on ordering, in two halves. The first R17,500 falls due when the first version of your live dashboard is up, built from your own data, typically a day or two after access is granted. That payment is the booking of your audit. The remaining R17,500 falls due on the date the audit is ready and presented. If it is not paid immediately, it remains due and payable from that date.</li>
    <li><b>Timeline:</b> two to three weeks from the commencement date.</li>
    <li><b>Handholding:</b> consultant access, interim findings and quick fixes for the duration are a deliverable of the audit. Withheld due payment suspends this deliverable until settled. The timeline does not pause.</li>
    <li><b>The Virtual Retail Direction option:</b> the Store Health Audit is a prerequisite of Virtual Retail Direction, direction is only sold on the back of a completed or running audit. Within 30 days of commencement you may indicate, agree or order Virtual Retail Direction (R25,000 a month). The audit&rsquo;s second R17,500 is then reallocated to your first month of direction, which is the second month of the relationship. If you have already paid it, your first direction month reads as R17,500 paid upfront and the remaining R7,500 is due on the first of that month. If you have not yet paid it, it stands as a discount on the audit and the full R25,000 for the first direction month is due on the first of that month. Either way the total is the same: the audit plus your first month of direction comes to R42,500. If you stop at the audit, the balance is simply the balance and nothing else happens.</li>
    <li><b>The dashboard stays, indefinitely.</b> The initial dashboard is a generic build, fed from your database. Whatever you decide after the audit, it stays up indefinitely at no further charge, on one condition: the installations on your server that feed it are not disrupted or deleted. No maintenance is guaranteed. If the feed breaks, the machine changes or the installations are removed, restoring it is new work by arrangement, not a standing obligation.</li>
    <li><b>Your data stays yours.</b> Never sold, never shared, never shown to another retailer, never used to benchmark you to anyone by name. Want it deleted, it is deleted. Want it handed over, it is handed over.</li>
    <li><b>Confidentiality runs both ways.</b> Neither side discusses the other&rsquo;s business, terms or findings with anyone outside it without written permission. Naming you as a client anywhere requires your agreement first. A signed mutual confidentiality agreement is available on request, same day. Our methods and tools stay ours.</li>
    <li><b>The work is recorded.</b> Every hour is logged on the day against what it produced. Ask for the log at any time and it is given without editing. The fee is fixed and the hours do not change it.</li>
    <li><b>Advisory basis:</b> findings and rand figures are our best estimates from the data and access you provide, and depend on that data being accurate and complete. Where a gap limits us we say so plainly rather than guess.</li>
    <li><b>No guaranteed result.</b> We do not guarantee a financial outcome. Results depend on execution, market conditions and factors outside anyone&rsquo;s control.</li>
    <li><b>Not professional advice:</b> Nothing in the audit is financial, legal, tax or accounting advice.</li>
    <li><b>We never touch your money.</b> We do not access, move or change funds. We advise. You decide and you act.</li>
    <li><b>Agreement:</b> your order, whether by submitting this page, by verbal go-ahead or by written email confirmation, is your acceptance of these terms and forms the working agreement between you and Social Brands Investments (Pty) Ltd, commencing on the date of that order. Keep the downloaded copy for your records.</li>
  </ol>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">What happens next</span><h2>After the audit: the road</h2>
  <p>Three options, and the plan works with all of them. You own it either way, that is deliberate, and it is why the audit is worth buying on its own. What the plan will not do is manage itself: a recovery plan in a folder returns nothing.</p></div>
  <div class="grid g3">
    <div class="card rv"><span class="num">1</span><h3>Do it yourself</h3><p>Take the plan, run it with your own team.</p></div>
    <div class="card flag rv"><span class="num">2</span><h3>Virtual Retail Direction</h3><p>R25,000 a month, remote. The month-to-month work of pointing at the right thing, checking it happened and adjusting when the store or the town moves. Your database read every night with exception checks run before you are awake, weekly analytics, weekly direction calls with you and your managers, a monthly owner report in plain language. Your team executes, we direct. Month to month, billed on the first, thirty days notice either way, no lock-in. Recommended for three months, because a store does not turn in four weeks. Order it within 30 days of your audit&rsquo;s commencement and the audit&rsquo;s second R17,500 goes toward your first month, as set out in the terms above.</p></div>
    <div class="card rv"><span class="num">3</span><h3>Full operational management</h3><p>R100,000 a month, twelve month minimum. We run the turnaround for you, on the floor, ordering discipline and systems work included. Virtual Retail Direction is included.</p></div>
  </div>
  <p class="rv" style="margin-top:20px;max-width:78ch">Optional add-ons to either road, priced on enquiry: the module apps (Bloom for ordering, Root for suppliers, Stem for finance, Rhythm for people, Mark for pricing, Vigil for live monitoring) and custom-built applications where a tool will pay for itself. The clearest example is a production costing engine, a bill of materials for your butchery, bakery and deli, scoped after the audit shows where it earns its keep.</p>
  <p class="rv" style="margin-top:14px;max-width:78ch">Decide all of this after the audit, on the findings, not now. Nothing about the credit should push the decision.</p>
</div></section>

<section class="sec sec-alt" id="questionnaire"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Start here</span><h2>The questionnaire</h2>
  <p>This is the start of your audit, not admin. We read every line before we speak to you. About twenty minutes, no preparation needed. There are no wrong answers. Where you are not sure, give your best estimate or write &ldquo;not sure&rdquo;. Rough is fine. We would rather have your honest guess than a blank.</p></div>

  <form class="form audit-form" id="auditForm" action="https://formsubmit.co/pieter@socialbrand.africa" method="POST">
    <input type="hidden" name="_subject" value="New Store Health Audit order - socialbrand.africa">
    <input type="hidden" name="_next" value="https://www.socialbrand.africa/audit/thanks/">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_autoresponse" value="Thank you. This confirms your Store Health Audit has commenced today. You will receive a copy of the order page and your answers by email within minutes, and hear from Pieter within two working days. Nothing is due until your live dashboard is up. Questions first? Call Pieter on 079 382 1818 or Lizeka Mgodeli on 068 113 7584, or email pieter@socialbrand.africa.">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">

    <h3 style="margin-top:6px">Section 1. About you and your store</h3>
    <div><label for="q1-1">Your name and your role in the business</label><input id="q1-1" name="q1_name_role" required></div>
    <div><label for="q1-2">Store name and town</label><input id="q1-2" name="q1_store_town" required></div>
    <div class="grid g2"><div><label for="q1-3a">Phone number</label><input id="q1-3a" type="tel" name="q1_phone" required autocomplete="tel"></div>
      <div><label for="q1-3b">Email</label><input id="q1-3b" type="email" name="email" required autocomplete="email"></div></div>
    <div><label for="q1-4">Who answers our questions within a working day (name and number, may be you)</label><input id="q1-4" name="q1_contact_person" required></div>
    <div><label for="q1-5">What kind of store is it (grocery, butchery, liquor, a combination, something else)</label><input id="q1-5" name="q1_store_type" required></div>
    <div><label for="q1-6">What do you actually spend most of your working hours doing day to day</label><textarea id="q1-6" name="q1_your_time" rows="2" required></textarea></div>
    <div><label for="q1-7">How long have you owned or run it</label><input id="q1-7" name="q1_tenure" required></div>
    <div><label for="q1-8">Roughly how many staff do you have</label><input id="q1-8" name="q1_staff" required></div>
    <div><label for="q1-9">How big is the store, in whatever terms you know (floor size, number of tills, aisles)</label><input id="q1-9" name="q1_store_size" required></div>

    <h3>Section 2. The problem, in your own words</h3>
    <div><label for="q2-1">In a sentence or two, what made you reach out now</label><textarea id="q2-1" name="q2_why_now" rows="2" required></textarea></div>
    <div><label for="q2-2">When did you first notice things turning</label><input id="q2-2" name="q2_when_noticed" required></div>
    <div><label for="q2-3">What do you think is causing it</label><textarea id="q2-3" name="q2_cause" rows="2" required></textarea></div>
    <div><label for="q2-4">What have you already tried, and did it help</label><textarea id="q2-4" name="q2_tried" rows="2" required></textarea></div>

    <h3>Section 3. The competition</h3>
    <div><label for="q3-1">Has a new competitor opened near you recently. Who are they and how far away</label><textarea id="q3-1" name="q3_competitor" rows="2" required></textarea></div>
    <div><label for="q3-2">What do you think they do better than you (price, range, parking, hours, freshness, marketing or something else)</label><textarea id="q3-2" name="q3_competitor_better" rows="2" required></textarea></div>
    <div><label for="q3-3">What do you still do better than them</label><textarea id="q3-3" name="q3_you_better" rows="2" required></textarea></div>

    <h3>Section 4. Your numbers (estimates are fine)</h3>
    <div><label for="q4-1">Roughly what does the store take per month now</label><input id="q4-1" name="q4_turnover_now" required></div>
    <div><label for="q4-2">Roughly what did it take per month a year ago</label><input id="q4-2" name="q4_turnover_last_year" required></div>
    <div><label for="q4-3">Right now, are you making a profit, breaking even or losing money</label><input id="q4-3" name="q4_profit_state" required></div>
    <div><label for="q4-4">If you are losing money, roughly how much per month (optional)</label><input id="q4-4" name="q4_loss_amount"></div>
    <div><label for="q4-5">At the current rate, how many months can the business hold on. Your honest estimate</label><input id="q4-5" name="q4_runway" required></div>
    <div><label for="q4-6">Roughly what is your gross profit percentage, if you know it (optional)</label><input id="q4-6" name="q4_gp_percent"></div>

    <h3>Section 5. Stock and buying</h3>
    <div><label for="q5-1">Roughly how much stock is sitting in the store right now, at cost</label><input id="q5-1" name="q5_stock_value" required></div>
    <div><label for="q5-2">Do you count your stock, and how often</label><input id="q5-2" name="q5_stocktake_freq" required></div>
    <div><label for="q5-3">Do you trust the stock figures your system shows you</label><input id="q5-3" name="q5_trust_stock" required></div>
    <div><label for="q5-4">Who does your buying, and do they follow a written system you have agreed on, or mostly instinct and experience</label><textarea id="q5-4" name="q5_buying" rows="2" required></textarea></div>
    <div><label for="q5-5">Do you run out of popular items often</label><input id="q5-5" name="q5_stockouts" required></div>

    <h3>Section 6. Your systems</h3>
    <div><label for="q6-1">What till or point of sale system do you use</label><input id="q6-1" name="q6_pos" required></div>
    <div><label for="q6-2">Does it give you reports you actually use (if yes, which ones and how often)</label><textarea id="q6-2" name="q6_reports" rows="2" required></textarea></div>
    <div><label for="q6-3">Does your system make an automatic backup, if you know (optional)</label><input id="q6-3" name="q6_backup"></div>
    <div><label for="q6-4">Day to day, how do you know whether you had a good day or a bad one</label><textarea id="q6-4" name="q6_good_day" rows="2" required></textarea></div>
    <div><label for="q6-5">Do you have written, step-by-step checklists for things like receiving stock, cashing up, opening or closing that a new person could follow without asking you</label><input id="q6-5" name="q6_checklists" required></div>

    <h3>Section 7. The customer and the shelf</h3>
    <div><label for="q7-1">When a regular walks out of your store, what feeling do you think they leave with (convenience, trust, a bargain, community, something else)</label><input id="q7-1" name="q7_feeling" required></div>
    <div><label for="q7-2">Why do your best customers choose you instead of the competitor down the road</label><textarea id="q7-2" name="q7_why_you" rows="2" required></textarea></div>

    <h3>Section 8. You and the business</h3>
    <div><label for="q8-1">If this store was working perfectly and did not need you there day to day, what would you spend your time doing instead</label><textarea id="q8-1" name="q8_free_time" rows="2" required></textarea></div>
    <fieldset><legend>If you had to step away for a month and could not check your phone, what would the store look like when you came back</legend>
      <label class="radio-opt"><input type="radio" name="q8_month_away" value="It would run smoothly" required> It would run smoothly</label>
      <label class="radio-opt"><input type="radio" name="q8_month_away" value="It would survive but with damage" required> It would survive but with damage</label>
      <label class="radio-opt"><input type="radio" name="q8_month_away" value="It would be in serious trouble" required> It would be in serious trouble</label>
    </fieldset>
    <div><label for="q8-3">Do you have an organisation chart, even a simple one, or does the work mostly get done by whoever is available</label><input id="q8-3" name="q8_org_chart" required></div>

    <h3>Section 9. Your goal</h3>
    <div><label for="q9-1">If we fixed one thing first, what would you want it to be</label><input id="q9-1" name="q9_fix_first" required></div>
    <div><label for="q9-2">Where do you want the business to be in twelve months</label><textarea id="q9-2" name="q9_12mo_goal" rows="2" required></textarea></div>
    <div><label for="q9-3">Is selling, closing or holding on until it recovers on your mind. An honest answer helps us help you</label><textarea id="q9-3" name="q9_exit_thoughts" rows="2" required></textarea></div>

    <h3>Section 10. Commitment</h3>
    <fieldset><legend>If we asked you to step off the shop floor for ninety days to build the systems behind the store, would you be willing to do that. There is no wrong answer, we just need to know how to help you best</legend>
      <label class="radio-opt"><input type="radio" name="q10_commitment" value="Yes, I will make the time" required> Yes, I will make the time</label>
      <label class="radio-opt"><input type="radio" name="q10_commitment" value="I would like to, but I am not sure how the store would manage" required> I would like to, but I am not sure how the store would manage</label>
      <label class="radio-opt"><input type="radio" name="q10_commitment" value="No, the business needs me on the floor right now" required> No, the business needs me on the floor right now</label>
    </fieldset>

    <h3 style="margin-top:34px">Submission</h3>
    <div class="card" style="margin-top:14px">
      <label class="radio-opt" style="align-items:flex-start"><input type="checkbox" name="accepted_terms" value="yes" required style="margin-top:4px">
      <span>I have read this page. I am entitled to grant access to this business&rsquo;s data. My submission is my acceptance of the terms above and the working agreement commences today.</span></label>
    </div>
    <div><label for="sub-name">Full name of the person accepting</label><input id="sub-name" name="acceptance_full_name" required></div>
    <div><label for="sub-biz">Business name</label><input id="sub-biz" name="business_name" required autocomplete="organization"></div>

    <button class="btn" type="submit" id="auditSubmit" style="margin-top:18px" disabled>Start my audit</button>
    <p class="note" style="margin-top:14px">You will receive a copy of this page and your answers by email within minutes, and hear from us within two working days. Nothing is due until your live dashboard is up. Questions first? Call Pieter on <a href="tel:+27793821818">079 382 1818</a> or Lizeka Mgodeli on <a href="tel:+27681137584">068 113 7584</a>, or email <a href="mailto:pieter@socialbrand.africa">pieter@socialbrand.africa</a>.</p>
  </form>
</div></section>

<script>
(function(){
  var form = document.getElementById("auditForm");
  if (!form) return;
  var btn = document.getElementById("auditSubmit");
  function check(){ btn.disabled = !form.checkValidity(); }
  form.addEventListener("input", check);
  form.addEventListener("change", check);
  check();
})();
</script>
'''
    audit_offer_schema = {
        "@type": "Offer", "price": "35000", "priceCurrency": "ZAR", "url": SITE["url"] + "/audit/",
        "itemOffered": {"@type": "Service", "name": "Store Health Audit",
            "provider": {"@id": SITE["url"] + "/#org"}, "areaServed": "South Africa",
            "description": "Fixed-fee retail diagnostic: data health, stock integrity, capital and availability, tested against a store's own till and ledger data. Findings quantified in rand with a prioritised action plan. One store, two to three weeks."}}
    pages.append(render("/audit/", "Order the Store Health Audit | SocialBrand",
        "Order the R35,000 fixed-fee Store Health Audit: the process, what you get, the terms and the order questionnaire, one page, two to three weeks to findings in rand.",
        body, extra_schema=audit_offer_schema))

    thanks_body = '''
<section class="sec" style="min-height:55vh"><div class="wrap" style="text-align:center;max-width:640px">
  <span class="kicker">Order received</span>
  <h1 style="font-size:clamp(2rem,4vw,3rem)">Your audit has commenced</h1>
  <p style="margin:18px auto 30px;color:var(--fg-muted)">Your submission is in. A copy of the order page and your answers is on its way to your inbox, and to Pieter&rsquo;s. Nothing is due until your live dashboard is up. We will be in touch within two working days to arrange access to your numbers.</p>
  <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
    <a class="btn btn-w" href="https://wa.me/27725652845">WhatsApp Pieter</a>
    <a class="btn btn-o" href="/">Back to the site</a>
  </div>
</div></section>
'''
    pages.append(render("/audit/thanks/", "Audit commenced | SocialBrand",
        "Your Store Health Audit order has been received.", thanks_body))

    # ---------- SAMPLE FINDINGS (illustrative, fictional store, no real client data) ----------
    sample_body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / <a href="/audit/">Order the audit</a> / Sample finding</p>
  <span class="kicker">See the format</span>
  <h1>What an audit finding looks like</h1>
  <p class="lead">Four findings from a fictional store, shown in the same shape a real finding reaches you: the number, the evidence, the action. This is what R35,000 buys: not a slide deck of opinions, arithmetic you can check.</p>
</div></div></section>

<section class="sec sec-sky"><div class="wrap">
  <div class="dash-note rv"><b>Generated, illustrative example.</b> Fairview SuperMart and Fairview Liquor are the same fictional stores used in the <a href="/demo/">live demo</a>. They do not exist, and no figure below comes from a real store or a real client. Any resemblance to a real business is coincidental. Real clients&rsquo; findings are never published, named or shown to anyone outside their own business.</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="grid g2" style="align-items:start">
    <div class="card rv"><span class="tag">Ledger</span><h3 style="margin-top:12px">Phantom stock, 200g Rooibos Twin-Pack</h3>
      <p class="amount" style="font-size:1.6rem;margin-top:8px">R38,400</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Evidence:</b> 14 lines flagged store-wide, led by this one. Ledger shows 40 units on hand. Last recorded sale was 71 days ago, and the last physical count was never done. Under the Presence Law, a line with no recent sale and no recent count is a claim, not a fact.</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Action:</b> Physical count of the 14 flagged lines, week 1. Receiving code fixed at source so the twin-pack stops posting to the single-unit code. Owner: stock controller, by Friday.</p></div>

    <div class="card rv"><span class="tag">Availability</span><h3 style="margin-top:12px">Stockouts on the top 20 lines</h3>
      <p class="amount" style="font-size:1.6rem;margin-top:8px">R61,000 / month</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Evidence:</b> True rate of sale, corrected for the days each line stood empty, shows six of the top 20 sellers running out an average of 4.2 days a month. At current margin, that is the estimated monthly sale lost while the shelf sat empty.</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Action:</b> Reorder points reset on the six lines to reflect true demand, not the days they were empty. Owner: buyer, live from week 2.</p></div>

    <div class="card rv"><span class="tag">Margin</span><h3 style="margin-top:12px">Till price mismatches on promoted lines</h3>
      <p class="amount" style="font-size:1.6rem;margin-top:8px">R14,200 / month</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Evidence:</b> Nine promoted lines checked against the till file. Three were still charging the pre-promotion price at the till, two had expired promotions still active. Estimate built from actual sales volume at the wrong price, not a sample.</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Action:</b> Weekly promotion-to-till reconciliation added to the Friday routine. Owner: front-end supervisor, starting immediately.</p></div>

    <div class="card rv"><span class="tag">Buying</span><h3 style="margin-top:12px">Capital tied in slow stock, ordered on habit</h3>
      <p class="amount" style="font-size:1.6rem;margin-top:8px">R22,000 tied up</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Evidence:</b> Eleven lines ordered on a fixed weekly quantity regardless of what actually sold. Demonstrated demand supports less than half the ordered volume on eight of them. The rest is capital sitting on a shelf, not working.</p>
      <p style="margin-top:10px;color:var(--fg-muted)"><b>Action:</b> Order quantities on the eleven lines cut to demonstrated demand, phased over two cycles so the shelf never looks empty. Owner: buyer, from week 2.</p></div>
  </div>
  <p class="rv note" style="margin-top:26px">A real audit runs to considerably more findings than four, across money, stock, ledger, ordering and leaks, each backed by its own working papers. This is the format, not the length.</p>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>See the platform behind it</h2><p>These findings come from the same kind of live, generated data as the interactive demo. Explore the fuller breakdown on Fairview&rsquo;s own numbers.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn btn-o" href="/demo/">Open the live demo</a><a class="btn" href="/audit/#questionnaire">Order your own audit</a></div>
  </div>
</div></section>
'''
    pages.append(render("/audit/sample-findings/", "A sample audit finding | SocialBrand",
        "See the format of a Store Health Audit finding: the rand figure, the evidence and the action, illustrated on a fictional store with generated data.",
        sample_body))

    return pages
