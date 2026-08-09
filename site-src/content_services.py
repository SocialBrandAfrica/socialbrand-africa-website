# content_services.py - The three legs: Turnaround, Operations & Training, Analytics & Ordering
# The "Questions owners ask us" blocks are written as a person phrases a question to an
# assistant. One source of truth per block: the same list renders the HTML and the
# FAQPage JSON-LD, so the visible answer and the marked-up answer can never drift.
import html as _html
import re as _re


def _plain(s):
    """HTML fragment -> plain sentence text for JSON-LD."""
    return _html.unescape(_re.sub(r"<[^>]+>", "", s)).strip()


def faq_block(kicker, heading, intro, qas, page_url, cls="sec sec-alt"):
    """Return (html_section, faqpage_schema) from one list of (question, answer_html)."""
    cards = "".join(
        f'<div class="card rv"><h3>{q}</h3><p>{a}</p></div>' for q, a in qas)
    html_section = f'''
<section class="{cls}"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">{kicker}</span><h2>{heading}</h2>
  <p>{intro}</p></div>
  <div class="grid g2">{cards}</div>
</div></section>
'''
    schema = {
        "@type": "FAQPage",
        "@id": page_url + "#faq",
        "url": page_url,
        "name": _plain(heading),
        "mainEntity": [
            {"@type": "Question", "name": _plain(q),
             "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}}
            for q, a in qas
        ]}
    return html_section, schema


def build(render, SITE):
    pages = []

    # ---------- TURNAROUND (the lead) ----------
    body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Services / Retail Turnaround</p>
  <span class="kicker">Leg 01 · The lead engagement</span>
  <h1>Retail Turnaround</h1>
  <p class="lead">Taking an underperforming store or group back to sustainable month-to-month profit. Not a report. A recovery, executed with you, until the trend holds.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The shape of it</span><h2>How a turnaround runs</h2>
  <p>Every troubled store tells the same lie in a different accent: the numbers say one thing, the floor says another. The turnaround starts by finding out which one is lying, and it is usually both.</p></div>
  <div class="grid g4">
    <div class="card rv"><span class="num">Step 1</span><h3>Diagnose</h3><p>The numbers and the floor, together. Trading position, supplier and creditor position, availability, stock integrity, the departments bleeding and the departments carrying them. Findings in rand, each with its evidence.</p></div>
    <div class="card rv"><span class="num">Step 2</span><h3>Stabilise</h3><p>Stop the bleeding first. The creditor conversation, the availability recovery on the lines your customers judge you by, budget discipline the whole team understands.</p></div>
    <div class="card rv"><span class="num">Step 3</span><h3>Rebuild</h3><p>Ordering rebuilt on demonstrated demand and your community&rsquo;s cycle. Standards on the floor. Training for the team holding them. The disciplines wired in so they survive without us.</p></div>
    <div class="card rv"><span class="num">Step 4</span><h3>Hold</h3><p>A turnaround is done when the trend holds month after month, on your own numbers, verified to source. Not when the consultant leaves.</p></div>
  </div>
</div></section>

<section class="sec sec-sky"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Live now</span><h2>The current mandate</h2>
  <p>An independent retail group engaged us to take it from losses back to sustainable profit. The engagement moved from no trusted stock data, riddled with phantom and negative stock lines, to a reconciled data platform, live generated ordering on the major supply routes and a prediction engine in build. The operational work runs alongside every day: availability, standards, supplier positions, the floor.</p>
  <p style="margin-top:14px">We name no clients and publish no client figures without consent. The method itself is public, in the <a href="/method/" style="color:var(--accent-2)">Method Library</a>.</p></div>
</div></section>
<!--FAQ-->
<section class="sec"><div class="wrap">
  <div class="grid g2" style="align-items:start">
    <div class="rv"><span class="kicker">The door</span><h2>Start with the Store Health Audit</h2>
    <p style="margin-top:14px;color:var(--fg-muted)">Fixed fee, one store, two to three weeks. We test your data health, stock integrity, capital and availability against your own till and ledger data, quantify the findings in rand and hand you a prioritised action plan. You own the plan whether you hire us or not. 50% of the fee credits toward your first month of Virtual Retail Direction, if ordered within 30 days of commencement.</p>
    <div style="display:flex;gap:14px;margin-top:24px;flex-wrap:wrap"><a class="btn" href="/audit/">Book the audit · R35,000</a><a class="btn btn-o" href="/pricing/">All pricing</a></div>
    </div>
    <div class="card rv"><h3>Signs you need this</h3>
      <ul class="tick-list" style="margin-top:14px">
        <li>The stock figure on screen and the shelf disagree, and orders ride the screen</li>
        <li>Month-end is a surprise, in either direction</li>
        <li>Suppliers are tightening terms while shelves run empty on the lines everyone asks for</li>
        <li>You are in the store every day, and it still needs you every day</li>
      </ul>
    </div>
  </div>
</div></section>
'''
    turnaround_qas = [
        ("How do I turn around a failing supermarket?",
         "Start with the truth, not the plan. Find out what the store actually sells, what stock is really on the shelf and where the money leaves, then stop the bleeding before you rebuild anything. The order that works is diagnose, stabilise, rebuild, hold. Stabilising means the creditor conversation and availability on the lines your customers judge you by. Rebuilding means ordering on demonstrated demand and standards your team can hold without you."),
        ("What is the first thing you fix in a struggling store?",
         "Availability on the lines people came for. Nothing else you do matters if a customer cannot buy the bread, the milk and the beer they walked in for, and a recovering shelf is the fastest signal a community reads. In parallel we test whether the stock ledger deserves trust, because ordering off a lying ledger keeps the shelf empty however hard the team works. That is <a href=\"/method/presence-law/\">the Presence Law</a>."),
        ("Why is my store busy but not profitable?",
         "Busy counts customers. Profit counts what you keep. The usual leaks are stock you paid for and cannot sell, gaps on the lines that carry the basket, buying that follows habit instead of demand and a gross profit that is wrong because the costs or the yields behind it are wrong. Every one of those is measurable in rand. Measuring them is what a <a href=\"/pricing/\">Store Health Audit</a> does before anybody recommends anything."),
        ("How long does a retail turnaround take?",
         "Stabilising is quick. Holding is not. Supplier pressure and availability move first because they answer to discipline rather than to time. Rebuilding ordering, standards and training takes longer, because it changes how people work. A turnaround is finished when the profit trend holds month after month on your own numbers, verified to source. It is not finished on the day the consultant leaves."),
        ("What does a retail consultant actually do?",
         "That depends who you hire. Most write a report. We work the floor. A SocialBrand engagement quantifies the problem in rand, then executes the fix alongside your team: supplier positions, availability, receiving discipline, ordering, standards and training. There is one useful question to ask anyone you are considering. What will you do in my store on a Tuesday morning? If the answer is a meeting, keep looking."),
        ("How much does retail consulting cost in South Africa?",
         "Ours is published rather than quoted on request. A Store Health Audit is R35,000, fixed fee, one store, two to three weeks, and half of that credits against a retainer signed within 30 days. Virtual Retail Direction is R25,000 a month, where your team executes and we direct. Full-Time Operational Management is R100,000 a month on a 12-month minimum. The detail sits on the <a href=\"/pricing/\">pricing page</a>."),
        ("My suppliers are tightening terms, what do I do?",
         "Talk to them early, because silence costs more than the conversation. Suppliers tighten when they cannot predict you, so bring a position they can read: what you owe, what you will pay and when, plus what you need on the shelf meanwhile. Then fix the buying that got you there. Fit the order to the money you actually have by scaling the flexible lines and holding the <a href=\"/method/fit-to-budget/\">known-value floors</a> untouched."),
        ("How do I know if my store can be saved?",
         "Ask whether the town still walks in. A store losing money with customers still coming through the door usually has a systems problem, and systems problems are fixable. A store the community has stopped visiting is a harder question. After that, test three things: whether the gross profit is real, whether the stock on the balance sheet still sells and whether you have the appetite for a few hard months."),
    ]
    faq_html, faq_schema = faq_block(
        "Straight answers", "Questions owners ask us",
        "The questions that come up in the first conversation, answered the way we would answer them on the phone.",
        turnaround_qas, SITE["url"] + "/turnaround/")
    body = body.replace("<!--FAQ-->", faq_html)
    pages.append(render("/turnaround/", "Retail Turnaround Consulting | SocialBrand South Africa",
        "Retail turnaround for independent stores and groups: diagnosis, stabilisation, rebuilt ordering and daily execution until the profit trend holds. Fixed-fee Store Health Audit as the entry point.",
        body, extra_schema=[{"@type": "Service", "name": "Retail Turnaround Consulting", "provider": {"@id": SITE["url"] + "/#org"}, "areaServed": "South Africa", "description": "Taking underperforming retail stores and groups back to sustainable month-to-month profit through diagnosis, stabilisation, rebuilt ordering and hands-on execution."}, faq_schema]))

    # ---------- OPERATIONS & TRAINING ----------
    body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Services / Operations &amp; Training</p>
  <span class="kicker">Leg 02 · The ongoing service</span>
  <h1>Retail Operations &amp; Training</h1>
  <p class="lead">We do not advise from a distance. Our people work on your floor, hold your standards daily and train the team who will hold them after us.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The work</span><h2>What we hold on your floor</h2>
  <p>Six areas of work, bought as work performed rather than as advice given. Each one is a routine somebody owns, holds and is checked on.</p></div>
  <div class="grid g3">
    <div class="card rv"><h3>Operational standards</h3><p>Daily standards held and audited: receiving discipline, back-door control, floor and fridge standards, department management and the morning routines a store lives or dies by.</p>
      <p style="margin-top:12px">Held means a person walks the routine, records what they found and closes it the same day. The back door gets the hardest attention, because that is where most stock losses are born. What arrived is checked against what was ordered and what was invoiced before the truck pulls away, and it is booked in that day. A store that receives loosely will never own a ledger worth ordering from.</p></div>
    <div class="card rv"><h3>Merchandising &amp; activations</h3><p>Planograms, category layouts, promotional execution and in-store activations including hot demos. The shelf a customer sees is the strategy, executed or not.</p>
      <p style="margin-top:12px">A planogram settles space, facings and margin once, so the shelf is not reinvented every night by whoever packs it. It also turns a gap into an obvious fault instead of a matter of opinion. Promotions get checked on the floor rather than assumed from the leaflet, and activations put the theatre where it earns its keep, on the days the community has money.</p></div>
    <div class="card rv"><h3>Workforce training</h3><p>Training and skills development, QCTO-accredited through our training partner, plus on-floor coaching. Led by co-founder Lizeka Mgodeli. She runs the training needs analysis, writes the job descriptions and role definitions the audit shows are missing, builds the retail training libraries and implements them on the floor with supervisors and staff.</p>
      <p style="margin-top:12px">Coaching happens in the aisle, in the receiving bay and at the till, on the work itself. A classroom teaches a person about the job. The floor teaches them the job. More on this below.</p></div>
    <div class="card rv"><h3>Compliance</h3><p>Health, safety and industry compliance held as a daily standard rather than an annual scramble.</p>
      <p style="margin-top:12px">The requirements that apply to your departments and your licences are written into the daily routine and checked with everything else, so the record is a by-product of the work rather than a project before an inspection. Lizeka Mgodeli carries compliance on the client operations side, alongside onboarding, scheduling and accounts.</p></div>
    <div class="card rv"><h3>Procurement &amp; supply</h3><p>Supplier negotiation, order discipline and stock flow, connected to the analytics leg so buying follows demonstrated demand rather than habit.</p>
      <p style="margin-top:12px">In practice that is supplier and DC positions kept current, order discipline that survives a busy week and delivery rhythms read from what actually arrived rather than from what somebody configured years ago. The thinking is published as <a href="/method/drop-cover/">Drop Cover</a>. When the truck comes twice a week the store holds less and the capital goes to work elsewhere.</p></div>
    <div class="card rv"><h3>Community marketing</h3><p>Local marketing in step with your town&rsquo;s rhythm: payday, pension days, season and school calendar. National campaigns miss rural tills.</p>
      <p style="margin-top:12px">The same calendar that decides when your town has money decides what it buys with that money, so local activity and the buying plan are set against one calendar rather than two. The stock lands as the money arrives, not after it has been spent somewhere else. See <a href="/method/community-rhythm/">Community Rhythm Ordering</a>.</p></div>
  </div>
</div></section>

<section class="sec sec-sky"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The people side</span><h2>Roles, training and the tools that hold a standard</h2>
  <p>An audit finds what is broken. A great deal of what it finds is not a lazy person. It is a person doing a job nobody ever defined properly, with no tool to do it and no standard to be held to. Co-founder Lizeka Mgodeli owns that side of every engagement, and it is the part that decides whether a turnaround survives our departure.</p></div>
  <div class="grid g2" style="align-items:start">
    <div class="rv">
      <div class="card" style="margin-bottom:22px"><h3>Job descriptions and role definitions</h3>
        <p>Written from what the audit actually found in your store, never from a template. A useful role definition names the daily routine, what the person owns, the standard they are held to, the tool they use to meet it and where an exception escalates. Most retail job descriptions list duties and stop, which is why they never settle an argument on a Saturday morning.</p></div>
      <div class="card"><h3>Training needs analysis</h3>
        <p>Lizeka runs a needs analysis per client before anything is taught. It compares what each role is meant to deliver against what the store is actually getting, department by department, then separates the three causes. The person was never taught. The job was never defined. The tool does not exist. Only the first is a training problem, and fixing the other two first is what makes training stick.</p></div>
    </div>
    <div class="rv">
      <div class="card" style="margin-bottom:22px"><h3>The training library, built for your store</h3>
        <p>Lizeka builds the material herself so what a store is taught matches how that store actually runs. Generic retail courses teach a generic store. The library covers the roles your departments really have, in the language your team really uses, and it stays with you as the reference a new hire is trained against next year.</p></div>
      <div class="card"><h3>Implementation and the tools per role</h3>
        <p>Material that stays in a folder changes nothing. Implementation happens on the floor with supervisors and staff, on live work, until the routine runs without prompting. Each role then gets the tool it needs to hold its standard on its own: the checklist, the routine, the record. That is what a store keeps after we leave, and keeping it is the whole point.</p></div>
    </div>
  </div>
  <p class="rv" style="margin-top:26px;color:var(--sky-muted);max-width:72ch">Formal training and skills development runs QCTO-accredited through our training partner. Programmes are quoted per cohort, because size and content vary too much for one honest figure. More about Lizeka is on the <a href="/pg-van-der-westhuizen/" style="color:var(--accent-2)">about page</a>.</p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The test</span><h2>What makes a standard hold</h2>
  <p>Standards do not decay because people stop caring. They decay because one of three conditions quietly went missing. Every routine we put into a store is built to satisfy all three, and audited against them.</p></div>
  <div class="grid g3">
    <div class="card rv"><span class="num">One</span><h3>It is written and specific</h3><p>A standard nobody wrote down is an opinion, and opinions lose arguments to whoever speaks loudest. Written means specific enough that two people inspecting the same shelf reach the same verdict.</p></div>
    <div class="card rv"><span class="num">Two</span><h3>The person has the tool and the time</h3><p>A standard that cannot be met inside a normal shift with the tools on hand is a standard the store has already agreed to break. If the routine does not fit the day, the routine is wrong, not the person.</p></div>
    <div class="card rv"><span class="num">Three</span><h3>Somebody checks it on a known routine</h3><p>Unchecked standards fade within weeks. Checked ones hold. We hold and audit them daily while training your supervisors to run the same check, because a store that needs us to hold its standards has not been turned around yet.</p></div>
  </div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="grid g2" style="align-items:center">
    <div class="rv"><span class="kicker">Reach</span><h2>On the floor, wherever the floor is</h2>
    <p style="margin-top:14px;color:var(--fg-muted)">The practice works through appointed agents across South Africa, with hubs in Cape Town and Johannesburg. Engagements run on site, with remote direction between visits through the Virtual Retail Direction service.</p></div>
    <div class="card rv"><h3>What this leg is not</h3><p>It is not a slide deck about excellence. Every service above is bought as work performed in your store, measured against standards you can inspect. If we cannot execute it, we do not sell it.</p></div>
  </div>
</div></section>
<!--FAQ-->
<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>Put standards on your floor</h2><p>Start with a conversation about your store, or start with the audit and let the findings set the priorities.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/contact/">Talk to us</a><a class="btn btn-o" href="/pricing/">Pricing</a></div>
  </div>
</div></section>
'''
    operations_qas = [
        ("How do I stop my store needing me every day?",
         "Write the job down. Most stores depend on the owner because the standard lives in the owner&rsquo;s head, so every exception has to come to you. Put it on paper as role definitions, daily routines and a tool each role uses to hold its standard, then train people to it and check it on a known cycle. The store stops needing you when an ordinary person can run the routine flawlessly on an ordinary day."),
        ("How do I train retail staff properly?",
         "Start with a training needs analysis, not a course catalogue. Find out which roles are failing and why, because a great deal of what looks like a training problem is a job nobody defined or a tool nobody built. Then teach material that matches how your store actually runs, on the floor, in live work. Our training is led by co-founder Lizeka Mgodeli and runs QCTO-accredited through our training partner."),
        ("What should a retail job description include?",
         "The daily routine, what the person owns, the standard they are held to, the tool they use to meet it and where an exception escalates. Most retail job descriptions list duties and stop there, which is why they never settle an argument on a busy Saturday. Ours are written from what the audit found in that specific store, by Lizeka Mgodeli, rather than downloaded and renamed."),
        ("How do I do a training needs analysis for a store?",
         "Watch the work before you ask about it. Compare what each role is meant to deliver against what the store is actually getting, department by department, then sort every gap into one of three causes. The person was never taught. The job was never defined. The tool does not exist. Only the first is a training problem. Fixing the other two first is cheaper and it makes the training stick."),
        ("What is a retail planogram and do I need one?",
         "A planogram is a plan of what sits where on a shelf, by position and number of facings. Yes, you need one, and not because head office asked. It settles space, availability and margin once instead of nightly by whoever packs the shelf. It also turns an empty spot into an obvious fault rather than a matter of opinion, which is what makes gaps get fixed."),
        ("How do I get my team to hold standards without me?",
         "Three conditions have to be true together. The standard is written and specific enough that two people reach the same verdict. The person has the tool and the time to meet it inside a normal shift. Somebody checks it on a known routine. Drop any one and the standard fades within weeks. We hold and audit standards daily while training your supervisors to run the same check."),
        ("What compliance does a South African supermarket need?",
         "Health and safety, food handling and the requirements that attach to your specific departments and licences. The practical answer matters more than the list. Compliance fails when it becomes an annual scramble before an inspection. Build the checks into the daily routine and the record becomes a by-product of the work. Lizeka Mgodeli holds compliance on the client operations side of every engagement."),
        ("How do I fix receiving at the back door?",
         "Treat the back door as a controlled area with one routine and one accountable person. Check what arrived against what was ordered and what was invoiced before the truck pulls away, then book it in the same day. Most stock loss is born here, and it is invisible later because the paperwork already agreed with itself. A store that receives loosely will never own a ledger worth ordering from."),
    ]
    faq_html, faq_schema = faq_block(
        "Straight answers", "Questions owners ask us",
        "What owners and managers ask us about running the floor, holding standards and getting a team trained.",
        operations_qas, SITE["url"] + "/operations/", cls="sec")
    body = body.replace("<!--FAQ-->", faq_html)
    pages.append(render("/operations/", "Retail Operations and Training | SocialBrand South Africa",
        "In-house retail operations executed on your floor: standards, merchandising and activations, QCTO-accredited workforce training through our partner, compliance and community marketing.",
        body, extra_schema=[{"@type": "Service", "name": "Retail Operations and Training", "provider": {"@id": SITE["url"] + "/#org"}, "areaServed": "South Africa", "description": "Ongoing retail operations management: daily standards, department management, merchandising, workforce training and compliance, executed in-store."}, faq_schema]))

    # ---------- ANALYTICS & INTELLIGENT ORDERING ----------
    body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Services / Analytics &amp; Intelligent Ordering</p>
  <span class="kicker">Leg 03 · The edge</span>
  <h1>Discovery, Analytics &amp; Intelligent Ordering</h1>
  <p class="lead">We measure the truth of your business. Then we rebuild ordering on that truth and automate it. Built by someone who has done the ordering himself for decades, and could also build the engine.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The value chain</span><h2>Trusted data first. Then answers. Then automation.</h2>
  <p>Most retail analytics fails for one reason: it decorates numbers nobody verified. We work in the opposite order.</p></div>
  <div class="grid g3">
    <div class="card rv"><span class="num">First</span><h3>One trusted dataset</h3><p>We mirror your store&rsquo;s own till and ledger data into one dataset and test every stock claim against actual movement behaviour. Presence is proven by sales or counts, never by the number on the screen.</p></div>
    <div class="card rv"><span class="num">Then</span><h3>Answers with reasons</h3><p>Stock health, capital working versus capital dead, true rates of sale, your community&rsquo;s buying rhythm. Every verdict carries its own reason in plain language. A number you cannot interrogate is a number you cannot trust.</p></div>
    <div class="card rv"><span class="num">Finally</span><h3>Ordering, automated</h3><p>Orders generated from demonstrated demand, shaped by payday and season, fitted to your budget, with every line able to explain itself. The discipline is public in the <a href="/method/8-step-ordering-recipe/">8-Step Ordering Recipe</a>.</p></div>
  </div>
</div></section>

<section class="sec sec-sky"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The proof</span><h2>The dark store story</h2></div>
  <div class="story scrolly" data-scrolly>
    <p>A dark store is retail with no forgiveness. The customer orders against the ledger&rsquo;s claim. If the ledger says three and the shelf holds none, the failure is measured inside the hour, on somebody&rsquo;s phone, with a refund attached.</p>
    <p>PG van der Westhuizen ran the Checkers Sixty60 dark store pilot in Cape Town, the first of its kind for the model, opened on Bree Street in the CBD. No walk-in customers. A full store existing purely to fulfil app orders. The model was scaled nationally after the pilot.</p>
    <p>His attested record there: the highest-turnover Sixty60 store on the continent at the time, north of 1,000 deliveries picked per day, about 98% fulfilled and delivered within the hour, in arguably the fastest grocery delivery service on the planet. Shoprite&rsquo;s own published group figures, 94% on time and 96.8% picked as placed, sit below the pilot&rsquo;s record. The group supplied the model and the systems. The margin above the fleet average is the measure of what his management added: three decades of floor operations plus an analytics discipline applied hour by hour.</p>
    <p>Every method in that discipline now works for independent stores, through SocialBrand.</p>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="grid g2" style="align-items:center">
    <div class="rv"><span class="kicker">See it</span><h2>The demo dashboard</h2>
    <p style="margin-top:14px;color:var(--fg-muted)">A fictional store, fully generated data, the real thinking. Watch a trading week move with payday, see phantom stock surfaced with its story, change a control on the order desk and watch the order rewrite itself line by line. Real clients see their own stores.</p>
    <a class="btn" style="margin-top:22px" href="/demo/">Open the live demo</a></div>
    <div class="card rv"><h3>What we never publish</h3><p>Formulas, thresholds, configuration values and client data. The thinking is public in the <a href="/method/">Method Library</a>. The mechanics are the moat, and your data stays yours: the platform runs on your own store&rsquo;s data, for your eyes.</p></div>
  </div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Made in store</span><h2>How we cost what your store makes</h2>
  <p>The moment your store makes something instead of buying it, most retail systems go blind. A boerewors batch, a bread run, a deli tray. You buy the inputs, you sell the outputs, and in between the true cost and the true yield are usually a guess. We close that gap with a bill of materials, and there is more than one honest way to build it. Which one fits you depends on your setup and the data you can produce.</p></div>
  <div class="grid g3">
    <div class="card rv"><span class="num">Model 1</span><h3>The block test</h3>
      <p>A controlled, physical test. You take a known raw input, cut or produce it under proper conditions, and weigh every sellable output and every offcut. That gives you a yield table you can trust as a standard.</p>
      <p style="margin-top:12px;font-size:.9rem"><b>Best for:</b> a store starting from scratch, or one that needs a benchmark to measure its people against.<br><b>Strength:</b> the cleanest measure of what your product should deliver, independent of bad habits.<br><b>Limit:</b> it describes perfect conditions. Real floors are not perfect, so it tells you the target, not the reality.</p>
    </div>
    <div class="card rv"><span class="num">Model 2</span><h3>Historical yield, from your own sales</h3>
      <p>Instead of testing, we read what your store has already done. Over a long enough period, what you bought in and what you sold out reveal the yield you are actually achieving, including the everyday waste and trim a block test excludes.</p>
      <p style="margin-top:12px;font-size:.9rem"><b>Best for:</b> an established store with a reliable sales history and no appetite for stopping production to run tests.<br><b>Strength:</b> it reflects your real world, not a laboratory.<br><b>Limit:</b> it inherits whatever is wrong in your history, which is why the data health work comes first.</p>
    </div>
    <div class="card flag rv"><span class="num">Model 3</span><h3>Live yield, from the ledger</h3>
      <p>The advanced version. Every receipt and every sale is mirrored into a clean data layer, and the yield recalculates continuously against what is actually moving. Costs update as supplier prices move, and a drift in yield shows up as it happens rather than at year end.</p>
      <p style="margin-top:12px;font-size:.9rem"><b>Best for:</b> a store or group with trustworthy transaction data and enough volume that a small yield drift is real money.<br><b>Strength:</b> self-correcting. It turns yield from an annual argument into a daily number.<br><b>Limit:</b> it demands a clean ledger. This is the model our own platform runs, and the destination we build clients toward.</p>
    </div>
  </div>
  <p class="rv" style="margin-top:26px;color:var(--fg-muted);max-width:70ch">Most stores start on model one or two and grow into model three. We scope which one fits you during the audit, because the honest answer depends on what your data can carry. The thinking behind all three is in <a href="/method/production-yield-models/">the Method Library</a>.</p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Also in this leg</span><h2>Human-led automation</h2>
  <p>Automation that answers to a person, not the other way around. Every automation we build has a human owner, a reason it exists and a point where it hands back to someone who can overrule it. A machine that cannot be questioned is not an improvement on a clerk who can.</p></div>
  <div class="grid g3">
    <div class="card rv"><h3>AI reception</h3><p>An AI receptionist answering calls and messages after hours, taking orders and bookings your store would otherwise miss. Anything it cannot answer goes to a person by name, not into a queue.</p></div>
    <div class="card rv"><h3>Website voice agents</h3><p>A voice agent on your website answering the questions customers actually ask: hours, stock, specials, directions. It says it does not know rather than guessing, because a wrong answer costs more than no answer.</p></div>
    <div class="card rv"><h3>Collections support</h3><p>Automated, polite and persistent follow-up on outstanding accounts, run under the client operations discipline of co-founder Lizeka Mgodeli. The tone stays yours and a person decides when to stop.</p></div>
  </div>
  <div class="card rv" style="margin-top:26px">
    <h3>Why we insist on the human in the loop</h3>
    <p style="margin-top:10px">Retail automation fails in one of two ways. It runs on numbers nobody checked, so it repeats a mistake faster than a person ever could. Or it becomes a black box, and the team stops arguing with it long before it stops being wrong. We build against both. Every automated verdict carries its reason in plain language, so the person reading it can disagree, and the person who owns the process stays accountable for the outcome. That is <a href="/method/story-test/">the Story Test</a>, and it is why we will not automate a store&rsquo;s ordering before its ledger has earned the trust.</p>
  </div>
</div></section>
<!--FAQ-->
<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>Find out what your numbers are hiding</h2><p>The Store Health Audit tests your data against your own tills. Findings in rand, two to three weeks, fixed fee.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/audit/">Book the audit</a><a class="btn btn-o" href="/demo/">See the demo first</a></div>
  </div>
</div></section>
'''
    analytics_qas = [
        ("Why does my stock system say I have stock when the shelf is empty?",
         "Because a stock number on a screen is a claim, not a fact. Receipts land on one product code while sales drain a twin. Production consumes ingredients the ledger never releases. Barcodes get recycled. The arithmetic stays consistent while the truth walks away. Under <a href=\"/method/presence-law/\">the Presence Law</a> a line counts as present only if it sold recently or was counted recently. Everything else goes to a count, not to an order."),
        ("What is phantom stock?",
         "Phantom stock is stock your system says you have and your shelf does not. It costs more than it looks, because a line that claims stock never reorders itself, so the gap never shows up anywhere as a lost sale. The shelf sits empty while the screen reads healthy. You find it by testing every stock claim against actual movement behaviour, then proving the doubtful ones with a physical count."),
        ("How do I calculate true rate of sale?",
         "Not by dividing units sold by days elapsed. That method counts the days the shelf stood empty as days of weak demand, so a line that ran out looks slow and gets ordered thinner still. True rate of sale corrects for the days the product was not there to sell, and it resolves pack families so a case and its singles read as one product. It must also respect the pay cycle, because a payday week and a mid-month week are not comparable."),
        ("Should I automate my store&rsquo;s ordering?",
         "Yes, once your data has earned it. Automation applied to a ledger you cannot trust only makes wrong orders faster. Fix stock integrity first, then automate. When we do, every proposed line has to explain itself in plain language before it ships, so you can overrule it with a reason rather than a feeling. The discipline is published as the <a href=\"/method/8-step-ordering-recipe/\">8-Step Ordering Recipe</a>."),
        ("How do I order for payday in a rural store?",
         "Order for the week your town is about to have, not for an average week that never happens. Money arrives on knowable days: salaries near month-end, pensions and grants early in the month, with season and the school calendar on top. Every line follows that calendar differently. Staples sell flat and want steady depth. Payday proteins spike and must be built into the window on the deliveries before it."),
        ("What is a dark store?",
         "A dark store is a retail store with no walk-in customers. It exists purely to pick and fulfil online orders. It is retail with no forgiveness, because the customer buys against the ledger&rsquo;s claim, so a phantom stock record becomes a failed order inside the hour with a refund attached. PG van der Westhuizen ran the Checkers Sixty60 dark store pilot in Cape Town, the first of its kind for that model."),
        ("How do I cost what my store makes in-house?",
         "You need a bill of materials, and there is more than one honest way to build one. A block test measures yield under controlled conditions and gives you a target. Historical yield reads what your store has already achieved, everyday waste and trim included. Live yield recalculates from the ledger as receipts and sales move, so drift surfaces in days rather than at year end. Which one fits depends on what your data can carry. See <a href=\"/method/production-yield-models/\">the three models</a>."),
        ("What is GMROI and does it matter?",
         "GMROI is gross margin return on inventory investment. It asks how much gross profit each rand tied up in stock returns over a period. It matters because stock value on its own tells you nothing. Two stores can hold the same rand of stock and run opposite businesses, one turning it steadily and one aging half of it in a stockroom. We judge stock by what it does rather than what it costs, and call that <a href=\"/method/capital-velocity/\">capital velocity</a>."),
    ]
    faq_html, faq_schema = faq_block(
        "Straight answers", "Questions owners ask us",
        "The stock, ordering and data questions that come up most often, answered without the vendor language.",
        analytics_qas, SITE["url"] + "/analytics/")
    body = body.replace("<!--FAQ-->", faq_html)
    pages.append(render("/analytics/", "Retail Analytics and Intelligent Ordering | SocialBrand",
        "Discovery, analytics and intelligent ordering for independent retail: one trusted dataset from your own tills, answers with reasons, and ordering automated on demonstrated demand.",
        body, extra_schema=[{"@type": "Service", "name": "Retail Analytics and Intelligent Ordering", "provider": {"@id": SITE["url"] + "/#org"}, "areaServed": "South Africa", "description": "Retail data discovery, analytics and automated ordering built on demonstrated demand, stock ledger integrity and community buying rhythm."}, faq_schema]))

    return pages
