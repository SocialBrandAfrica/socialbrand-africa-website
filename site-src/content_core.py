# content_core.py - Home, About, Contact, Pricing, 404
# Truth gate: every claim below traces to a ruled fact in SB-WEB-002/003/004.

def build(render, SITE):
    pages = []

    # ---------- HOME ----------
    home_body = '''
<section class="hero"><div class="stars" aria-hidden="true"></div>
  <svg class="hero-illo" viewBox="0 0 480 380" fill="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
    <circle cx="366" cy="98" r="36" fill="var(--accent-2)" opacity=".85"/>
    <g stroke="var(--accent)" stroke-width="3" stroke-linecap="round" opacity=".7">
      <path d="M366 40v-20"/><path d="M366 176v20"/><path d="M304 98h-20"/><path d="M448 98h20"/>
      <path d="M323 55l-14-14"/><path d="M409 141l14 14"/><path d="M409 55l14-14"/><path d="M323 141l-14 14"/>
    </g>
    <path d="M0 296 Q120 250 262 288 T480 268 V380 H0 Z" fill="var(--accent-2)" opacity=".10"/>
    <path d="M0 330 Q160 294 322 320 T480 312 V380 H0 Z" fill="var(--accent)" opacity=".16"/>
    <polyline points="52,252 122,214 186,228 250,172 322,150" stroke="var(--accent-2)" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M322 150l-17 3M322 150l-3 17" stroke="var(--accent-2)" stroke-width="3.5" stroke-linecap="round"/>
    <g stroke="var(--accent-2)" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
      <path d="M146 296h164l-11-26H157l-11 26Z" fill="var(--accent-2)" opacity=".85"/>
      <rect x="152" y="296" width="152" height="70" rx="6" fill="rgba(255,255,255,.10)"/>
      <path d="M152 322h152"/><path d="M152 344h152"/>
      <rect x="216" y="330" width="26" height="36" rx="3" fill="none"/>
    </g>
  </svg>
  <div class="wrap">
    <div class="hero-in">
      <span class="kicker">Retail turnaround &middot; Operations &middot; Analytics</span>
      <h1>We turn retail businesses around. <em>Then we run them right.</em></h1>
      <p class="slogan">The shelf sells the hype. <b>The system wins the war.</b></p>
      <p class="lead">SocialBrand is the retail practice of PG van der Westhuizen. More than three decades of store operations, backed by an analytics capability most operators have never had access to.</p>
      <div class="hero-sub">
        <a class="btn" href="/audit/">Book a Store Health Audit</a>
        <a class="btn btn-o" href="/demo/">See the live demo</a>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-sky">
  <div class="wrap">
    <div class="proof">
      <div class="rv"><div class="n"><span data-count="0.03" data-suffix="%">0.03%</span></div><p class="l">Shrinkage held below 0.03% of turnover, down from 1.8%, over four years at a Checkers branch</p></div>
      <div class="rv"><div class="n"><span data-count="20" data-prefix="+" data-suffix="%">+20%</span></div><p class="l">Stock turn improvement, with staff turnover down 25% and turnover up 15% year on year</p></div>
      <div class="rv"><div class="n"><span data-count="1000" data-suffix="+">1,000+</span></div><p class="l">Deliveries picked daily at the Checkers Sixty60 dark store pilot in Cape Town</p></div>
      <div class="rv"><div class="n"><span data-count="98" data-suffix="%">98%</span></div><p class="l">Of those orders fulfilled and delivered within the hour</p></div>
    </div>
    <p class="attr">The career record of founder PG van der Westhuizen, built across three decades of South African retail. Career results, stated as career results. Never invented, never borrowed.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h rv">
      <span class="kicker">What we do</span>
      <h2>Three legs. One practice.</h2>
      <p>Operations lead. The data work is the edge inside them, never the headline over them.</p>
    </div>
    <div class="grid g3">
      <a class="card flag rv" href="/turnaround/">
        <span class="num">01</span>
        <h3>Retail Turnaround</h3>
        <p>The lead engagement. We take an underperforming store or group back to sustainable month-to-month profit, and stay until the trend holds.</p>
        <span class="more">The turnaround method &rarr;</span>
      </a>
      <a class="card rv" href="/operations/">
        <span class="num">02</span>
        <h3>Operations &amp; Training</h3>
        <p>The ongoing management service. Standards held daily, merchandising, workforce training and compliance. Our people execute on your floor.</p>
        <span class="more">How we run stores &rarr;</span>
      </a>
      <a class="card rv" href="/analytics/">
        <span class="num">03</span>
        <h3>Analytics &amp; Intelligent Ordering</h3>
        <p>The edge. We measure the truth of your stock, capital and demand, then rebuild ordering on demonstrated demand and automate it.</p>
        <span class="more">The intelligence layer &rarr;</span>
      </a>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="grid g2" style="align-items:center">
      <div class="rv">
        <span class="kicker">Why owners call us</span>
        <h2>Knowing your stores without standing in them</h2>
        <div class="story" style="margin-top:26px">
          <p>A store owner stands at his son&rsquo;s rugby match on a Saturday morning. His phone is in his pocket. He already knows the soup got made. He knows the 2-litre Coke is out at one store, and he has arranged the fix, without a single call to plead for information.</p>
          <p>That is operational freedom. It is not a dashboard feature. It is what happens when the numbers in your business are true, and someone has done the work to make them true.</p>
        </div>
      </div>
      <div class="rv">
        <div class="card">
          <h3>What we are doing right now</h3>
          <p style="margin-top:8px">An independent retail group engaged us to take it from losses back to sustainable profit. The engagement moved from no trusted stock data, riddled with phantom and negative stock lines, to a reconciled data platform, live generated ordering on the major supply routes and a prediction engine in build.</p>
          <p style="margin-top:12px">The same discipline is in the <a href="/demo/">live demo</a>, running on generated data for a fictional store.</p>
          <a class="more" style="display:inline-block;margin-top:14px;font-weight:600;color:var(--accent-ink)" href="/turnaround/">How a turnaround runs &rarr;</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec-sky">
  <div class="wrap">
    <div class="sec-h rv">
      <span class="kicker">The proof</span>
      <h2>Retail with no forgiveness</h2>
      <p>PG van der Westhuizen ran the Checkers Sixty60 dark store pilot in Cape Town. No walk-in customers. A full store built purely to fulfil app orders, where a customer orders against the ledger&rsquo;s claim, so a phantom stock record becomes a failed order inside the hour. Measured.</p>
      <p style="margin-top:14px">His record there: the highest-turnover Sixty60 store on the continent at the time, north of 1,000 deliveries picked per day at about 98% fulfilled and delivered within the hour. The systems came with the model. The result came from three decades of floor operations and his own analytics discipline, applied hour by hour.</p>
    </div>
    <a class="btn" href="/analytics/">Read the dark store story</a>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-h rv">
      <span class="kicker">The Method Library</span>
      <h2>Named methods, published thinking</h2>
      <p>The thinking is the marketing. The mechanics are the moat. Each method carries a name, a definition and its author, so you know exactly how we think before you pay us anything.</p>
    </div>
    <div class="chips rv">
      <a class="chip" href="/method/presence-law/">The Presence Law</a>
      <a class="chip" href="/method/8-step-ordering-recipe/">The 8-Step Ordering Recipe</a>
      <a class="chip" href="/method/community-rhythm/">Community Rhythm Ordering</a>
      <a class="chip" href="/method/capital-velocity/">Capital Velocity</a>
      <a class="chip" href="/method/story-test/">The Story Test</a>
      <a class="chip" href="/method/two-worlds/">The Two Worlds</a>
      <a class="chip" href="/method/daily-count-law/">The Daily Count Law</a>
      <a class="chip" href="/method/drop-cover/">Drop Cover</a>
      <a class="chip" href="/method/base-rate-rule/">The Base-Rate Rule</a>
      <a class="chip" href="/method/fit-to-budget/">Fit-to-Budget with KVI Floors</a>
      <a class="chip" href="/method/production-yield-models/">Production Yield: Three Models</a>
    </div>
    <p style="margin-top:26px" class="rv"><a class="more" style="font-weight:600;color:var(--accent-ink)" href="/method/">Browse the full library &rarr;</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta-band rv">
      <div>
        <h2>Start with the truth about one store</h2>
        <p>The Store Health Audit is a fixed-fee diagnostic. Two to three weeks, one store, findings in rand, an action plan you own either way.</p>
      </div>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a class="btn" href="/audit/">Book the audit</a>
        <a class="btn btn-o" href="/pricing/">See pricing</a>
      </div>
    </div>
  </div>
</section>
'''
    pages.append(render("/", "SocialBrand | Retail turnaround and operations consulting, South Africa",
        "SocialBrand turns retail businesses around and runs them right. More than three decades of store operations, backed by an analytics capability most operators have never had access to.",
        home_body,
        extra_schema={"@type": "WebSite", "name": "SocialBrand", "url": SITE["url"], "publisher": {"@id": SITE["url"] + "/#org"}}))

    # ---------- ABOUT / FOUNDERS ----------
    about_body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / About</p>
  <span class="kicker">About the founders</span>
  <h1>PG van der Westhuizen &amp; Lizeka Mgodeli</h1>
  <p class="lead">PG van der Westhuizen and Lizeka Mgodeli co-founded SocialBrand, the practice of Social Brands Investments (Pty) Ltd. PG runs the operational and analytics side of every engagement, built on more than three decades of South African retail. Lizeka is majority shareholder and owns the people side, the part that decides whether a turnaround survives once the consultants leave.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">The philosophy</span><h2>The shelf sells the hype. The system wins the war.</h2>
  <p>Retail is two battles, not one. The first is attracting the customer: the theatre of a full shelf, a sharp promotion, a well-run front end. The second is keeping the margin: the stock that is actually there, the order that matches real demand, the paperwork that cannot be gamed. Most independent stores fight the first battle brilliantly and lose the second quietly.</p>
  <p style="margin-top:14px">We do not build stores that depend on one exceptional manager. We build a system that ordinary people can run flawlessly, every day, whether the owner is standing in the store or not.</p></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Founder</span><h2>PG van der Westhuizen &middot; three decades on the floor</h2></div>
  <div class="grid g2">
    <div class="card rv"><span class="num">Shoprite</span><h3>Where the discipline started</h3><p>Store operations from the ground up, and the early data work: database development and availability rules, holding in-store availability at 98%. The lesson carried ever since is the same one the practice sells today. Availability is measured, never assumed.</p></div>
    <div class="card rv"><span class="num">Nestlé</span><h3>The supplier side</h3><p>The view from the other end of the supply chain. How national brands plan, how DCs behave and what a store looks like to the people who fill it.</p></div>
    <div class="card rv"><span class="num">Build it &amp; BUCO</span><h3>Hard retail, big format</h3><p>Building-material retail across formats. Store revamps, store openings and high-turnover stores rebuilt, then turnaround strategies across multiple business units at consortium level.</p></div>
    <div class="card rv"><span class="num">Checkers</span><h3>The dark store chapter</h3><p>PG ran the Checkers Sixty60 dark store pilot in Cape Town, the store the model was proven in before scaling nationally. His attested record: the highest-turnover Sixty60 store on the continent at the time, north of 1,000 deliveries picked per day at about 98% fulfilled and delivered within the hour. He also built Sixty60 in-store from zero to 25 to 30% participation, growing 50% in its first year. The model and systems were the group&rsquo;s. The result was his: three decades of floor knowledge and his own analytics discipline, applied hour by hour, in arguably the fastest grocery delivery service on the planet.</p></div>
  </div>
  <div class="proof" style="margin-top:26px">
    <div class="rv"><div class="n">1.8% → 0.03%</div><p class="l">Shrinkage as a share of turnover, held over four years at a Checkers branch</p></div>
    <div class="rv"><div class="n">+20%</div><p class="l">Stock turn improvement</p></div>
    <div class="rv"><div class="n">−25%</div><p class="l">Staff turnover reduction</p></div>
    <div class="rv"><div class="n">+15%</div><p class="l">Turnover growth year on year</p></div>
  </div>
  <p class="note rv" style="margin-top:14px">PG&rsquo;s personal career record, achieved in management roles across three decades of South African retail, stated as exactly that. SocialBrand publishes no client statistics without the client&rsquo;s consent, and it never invents any.</p>
</div></section>

<section class="sec sec-sky"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Co-founder and majority shareholder</span><h2>Lizeka Mgodeli &middot; owns the people side</h2>
  <p>Lizeka Mgodeli is co-founder, director and majority shareholder of Social Brands Investments. If a turnaround changes how people work, it goes through her. An audit finds what is broken. Much of what it finds is a person doing a job nobody ever defined properly, with no tool to do it and no standard to hold. Lizeka turns those findings into the roles, training and systems that make a turnaround survive after the consultants leave.</p></div>
  <div class="grid g2">
    <div class="card rv"><span class="num">Design</span><h3>Job descriptions &amp; role definitions</h3><p>Written from what the audit actually found in a store, never from a template. Names the daily routine, what the person owns, the standard they are held to, and where an exception escalates.</p></div>
    <div class="card rv"><span class="num">Train</span><h3>Training needs analysis &amp; libraries</h3><p>A needs analysis per client before anything is taught, then a training library Lizeka builds herself so what a store learns matches how that store actually runs.</p></div>
    <div class="card rv"><span class="num">Implement</span><h3>In-store implementation &amp; the tools each role needs</h3><p>Delivered on the floor with supervisors and staff on live work, until the routine runs without prompting. Each role gets the checklist and the tool it needs to hold its own standard after we leave.</p></div>
    <div class="card rv"><span class="num">Run</span><h3>Client operations, compliance &amp; publishing</h3><p>Onboarding, scheduling, follow-up, accounts and compliance for every engagement, plus SocialBrand&rsquo;s own online publishing and social media.</p></div>
  </div>
  <div class="proof" style="margin-top:26px">
    <div class="rv"><div class="n">51%</div><p class="l">Majority shareholder of Social Brands Investments</p></div>
    <div class="rv"><div class="n">Level 2</div><p class="l">B-BBEE Contributor status</p></div>
    <div class="rv"><div class="n">125%</div><p class="l">Procurement recognition</p></div>
    <div class="rv"><div class="n">4</div><p class="l">Domains owned end to end, from design through to delivery</p></div>
  </div>
  <p class="bbbee note rv" style="margin-top:14px"><b>Level 2 B-BBEE Contributor</b> &middot; 51% black-woman-owned &middot; 125% procurement recognition</p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="grid g2" style="align-items:start">
    <div class="card rv"><span class="num">Founded</span><h3>SocialBrand, the practice</h3><p>Social Brands Investments (Pty) Ltd was registered in 2024, co-founded by PG van der Westhuizen and Lizeka Mgodeli. The practice serves independent retail owners from Cape Town and North West: turnaround, operations and training, and the analytics and intelligent ordering work most operators have never had access to. The current mandate is a live turnaround, from losses back to sustainable profit, with the group&rsquo;s ordering rebuilt on demonstrated demand instead of guesswork.</p></div>
    <div class="card rv"><h3>How we work</h3>
      <ul class="tick-list" style="margin-top:14px">
        <li>Every number we publish is true, attributed and approved. The old marketing habit of invented testimonials is the exact disease we cure in stores. We do not carry it ourselves.</li>
        <li>Client identities stay private. Methods are published as thinking, never as formulas.</li>
        <li>Done means it works on your phone, in your store, in real use.</li>
      </ul>
    </div>
  </div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-h rv"><span class="kicker">Subject areas</span><h2>What we are asked about</h2>
  <p>Owners, managers and journalists come to this practice with a fairly consistent set of questions. These are the subjects we are a source on, meaning we have done the work in a store rather than read about it. Each one links to where we have published our thinking on it.</p></div>
  <div class="rv" style="max-width:78ch">
    <p style="color:var(--fg-muted)">The core of it is retail turnaround and supermarket operations for independent and franchise stores in South Africa. Underneath that sits the stock work: ledger integrity, phantom and negative stock, stocktake discipline and the daily counting that replaces the annual big bang. Out of clean stock data comes the buying work: true demand, demand-led and automated ordering, community rhythm and payday cycles, supplier and DC relationships, plus capital velocity as the measure of whether stock is earning or resting.</p>
    <p style="margin-top:14px;color:var(--fg-muted)">Alongside the numbers sits the floor: merchandising and planograms, retail compliance, dark store operations and online fulfilment, production yield and bill of materials for what a store makes rather than buys, plus the people work of job design, role definition, retail training and skills development that decides whether any of it holds.</p>
  </div>
  <div class="chips rv" style="margin-top:26px">
    <a class="chip" href="/turnaround/">Retail turnaround</a>
    <a class="chip" href="/operations/">Supermarket operations</a>
    <a class="chip" href="/method/presence-law/">Stock ledger integrity</a>
    <a class="chip" href="/insights/your-stock-ledger-is-lying/">Phantom and negative stock</a>
    <a class="chip" href="/method/daily-count-law/">Stocktake discipline</a>
    <a class="chip" href="/method/8-step-ordering-recipe/">Demand-led and automated ordering</a>
    <a class="chip" href="/method/community-rhythm/">Community rhythm and payday cycles</a>
    <a class="chip" href="/method/capital-velocity/">Capital velocity and GMROI</a>
    <a class="chip" href="/analytics/">Dark store operations and fulfilment</a>
    <a class="chip" href="/method/production-yield-models/">Production yield and bill of materials</a>
    <a class="chip" href="/operations/">Retail training and skills development</a>
    <a class="chip" href="/operations/">Job design and role definition</a>
    <a class="chip" href="/operations/">Merchandising and planograms</a>
    <a class="chip" href="/method/drop-cover/">Supplier and DC relationships</a>
    <a class="chip" href="/operations/">Retail compliance</a>
    <a class="chip" href="/pricing/">Independent and franchise retail in South Africa</a>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>Talk to us</h2><p>One conversation about your store costs nothing. Bring your numbers, or bring your doubts about them.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/contact/">Get in touch</a></div>
  </div>
</div></section>
'''
    pages.append(render("/pg-van-der-westhuizen/",
        "About | PG van der Westhuizen and Lizeka Mgodeli, SocialBrand founders",
        "SocialBrand was co-founded by PG van der Westhuizen, more than three decades on the South African retail floor, and Lizeka Mgodeli, who owns the people side of every engagement: job descriptions, training and client operations.",
        about_body,
        extra_schema={"@type": "ProfilePage", "mainEntity": [{"@id": SITE["url"] + "/#pg"}, {"@id": SITE["url"] + "/#lizeka"}], "url": SITE["url"] + "/pg-van-der-westhuizen/"}))

    # ---------- PRICING ----------
    pricing_body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Pricing</p>
  <span class="kicker">Pricing</span>
  <h1>Real prices, published</h1>
  <p class="lead">Hidden pricing wastes your time and ours. These are the actual figures, in South African rand. If a number below does not fit your store yet, start with the audit and decide from evidence.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="grid g3" style="align-items:start">
    <div class="card price-card hero-p rv"><span class="badge">Start here</span>
      <h3>Store Health Audit</h3>
      <p class="amount">R35,000</p>
      <p class="terms">Fixed fee · one store · 2 to 3 weeks</p>
      <ul>
        <li>Data health, stock integrity, capital and availability, tested against your own till and ledger data</li>
        <li>Findings quantified in rand, each with its evidence</li>
        <li>A prioritised action plan you own, whether you hire us or not</li>
        <li>50% of the fee credits toward your first month of Virtual Retail Direction, if ordered within 30 days</li>
      </ul>
      <a class="btn" href="/audit/">Book the audit</a>
      <p class="note" style="margin-top:10px;font-size:.85rem"><a href="/audit/sample-findings/">See a sample finding &rarr;</a></p>
    </div>
    <div class="card price-card rv">
      <h3>Virtual Retail Direction</h3>
      <p class="amount">R25,000</p>
      <p class="terms">Per month · remote</p>
      <p class="note" style="margin-top:10px">The Store Health Audit is the prerequisite. Direction starts from the audit&rsquo;s findings, never from guesswork.</p>
      <ul>
        <li>The recovery plan and the systems design</li>
        <li>The analytics read on your numbers, every week</li>
        <li>Weekly direction calls with you and your managers</li>
        <li>A monthly owner report in plain language</li>
        <li>Your team executes. We direct.</li>
      </ul>
      <a class="btn btn-o" href="/contact/">Enquire</a>
      <p class="note" style="margin-top:12px;font-size:.85rem">Optional add-ons: the module apps (Bloom, Root, Stem, Rhythm, Mark, Vigil) and custom-built applications, priced on enquiry.</p>
    </div>
    <div class="card price-card rv">
      <h3>Full-Time Operational Management</h3>
      <p class="amount">R100,000</p>
      <p class="terms">Per month · 12-month minimum</p>
      <ul>
        <li>Full operational management of the store or group, on the floor</li>
        <li>The complete turnaround programme, training and standards</li>
        <li>Ordering discipline rebuilt on demonstrated demand</li>
        <li>The ordering automation project included, built to a defined finish line</li>
        <li>Virtual Retail Direction included</li>
      </ul>
      <a class="btn btn-o" href="/contact/">Enquire</a>
      <p class="note" style="margin-top:12px;font-size:.85rem">Optional add-ons: the module apps (Bloom, Root, Stem, Rhythm, Mark, Vigil) and custom-built applications, priced on enquiry.</p>
    </div>
  </div>

  <div class="incl rv" style="margin-top:30px">
    <span class="kicker">Included free in every package</span>
    <h3>Custom-Made Retail Analytics for your store</h3>
    <p>Every engagement above includes Pulse, your own analytics window, at no extra cost. Basic KPIs and daily data intelligence built from your own systems, shaped to your store rather than to a template.</p>
    <ul class="tick-list" style="margin-top:16px">
      <li>Daily KPIs from your own trading data, not a monthly summary written after the fact</li>
      <li>Direct access to the underlying mirrored data, so a question can be answered without waiting for a report to be built</li>
      <li>Reports you can export in the format you actually use, or read in the browser on your phone</li>
      <li>Ledger, stocktake and budgeting logic, covering both budgets</li>
    </ul>
    <p class="note" style="margin-top:14px">See the thinking at work in the <a href="/demo/">live demo</a>, running on generated data for a fictional store.</p>
  </div>

  <div class="grid g2" style="margin-top:22px">
    <div class="card rv"><h3>Training programmes</h3><p>Workforce training and development, QCTO-accredited through our training partner, plus on-floor coaching. Quoted per programme, because cohort size and content vary too much for one honest figure.</p></div>
    <div class="card rv"><h3>Group, DC and franchise work</h3><p>Multi-store groups, distribution centre work and franchise programmes are scoped against what the estate actually needs, then quoted. The audit is still the sensible first step, on one representative store.</p></div>
  </div>

  <div class="sec-h rv" style="margin-top:56px;margin-bottom:26px">
    <span class="kicker">Beyond the analytics window</span>
    <h2>Additional packages</h2>
    <p>Pulse is the window included with every engagement. The rest of the suite sits on the same backbone and is released as separate packages. None of these carry a published price yet. Cost is on enquiry, and we would rather scope one honestly than print a figure we cannot stand behind.</p>
  </div>
  <div class="grid g3">
    <div class="card rv"><h3>Bloom</h3><p class="pk">Ordering</p><p>The ordering desk. Orders generated from demonstrated demand, shaped by your community&rsquo;s rhythm and fitted to the buying budget, with every line able to explain itself.</p></div>
    <div class="card rv"><h3>Root</h3><p class="pk">Suppliers</p><p>The supplier view. Delivery rhythm proven from receipts, route performance and the supplier positions that decide what a store can actually hold.</p></div>
    <div class="card rv"><h3>Stem</h3><p class="pk">Finance</p><p>Money in both directions. The finance view over trading, buying and the budgets that govern them.</p></div>
    <div class="card rv"><h3>Rhythm</h3><p class="pk">People</p><p>The people view. Scheduling, workforce and the payroll-adjacent admin a store carries whether it plans for it or not.</p></div>
    <div class="card rv"><h3>Mark</h3><p class="pk">Pricing</p><p>The pricing view. What a line costs, what it earns and what a price change does before you make it.</p></div>
    <div class="card rv"><h3>Vigil</h3><p class="pk">Live monitoring</p><p>Live till monitoring. What is happening at the front end now, rather than what a report says about it tomorrow.</p></div>
  </div>
  <p class="note rv" style="margin-top:24px">Each package is a window on the same platform. They share one data backbone, so adding one later does not mean rebuilding anything. Ask us what a package would cost for your store and we will scope it.</p>

  <p class="note rv" style="margin-top:26px">All amounts in South African rand.</p>
</div></section>

<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>Not sure which one fits?</h2><p>Send one line about your store and its biggest worry. You will get a straight answer about which engagement fits, or whether none does.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/contact/">Ask Pieter</a></div>
  </div>
</div></section>
'''
    offers_schema = {
        "@type": "OfferCatalog", "name": "SocialBrand services",
        "itemListElement": [
            {"@type": "Offer", "price": "35000", "priceCurrency": "ZAR",
             "itemOffered": {"@type": "Service", "name": "Store Health Audit", "description": "Fixed-fee retail diagnostic: data health, stock integrity, capital and availability, findings quantified in rand with an action plan. One store, two to three weeks."}},
            {"@type": "Offer", "price": "25000", "priceCurrency": "ZAR",
             "itemOffered": {"@type": "Service", "name": "Virtual Retail Direction", "description": "Monthly remote retail direction: recovery plan, systems design, weekly analytics read and direction calls, monthly owner report."}},
            {"@type": "Offer", "price": "100000", "priceCurrency": "ZAR",
             "itemOffered": {"@type": "Service", "name": "Full-Time Operational Management", "description": "Full operational management of a store or group with the turnaround programme, training, ordering discipline and the ordering automation project included. 12-month minimum."}}
        ]}
    pages.append(render("/pricing/", "Pricing | SocialBrand retail consulting, South Africa",
        "Published consulting prices in rand: Store Health Audit R35,000 fixed, Virtual Retail Direction R25,000 per month, Full-Time Operational Management R100,000 per month.",
        pricing_body, extra_schema=offers_schema))

    # ---------- CONTACT ----------
    contact_body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Contact</p>
  <span class="kicker">Contact</span>
  <h1>Talk to us</h1>
  <p class="lead">One conversation about your store costs nothing. WhatsApp is the fastest way to reach Pieter directly.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="grid g2" style="align-items:start">
    <div class="rv">
      <h2 style="margin-bottom:20px">Send a message</h2>
      <form class="form" action="https://formsubmit.co/pieter@socialbrand.africa" method="POST">
        <input type="hidden" name="_subject" value="Website enquiry - socialbrand.africa">
        <input type="hidden" name="_next" value="https://www.socialbrand.africa/contact/thanks/">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
        <div><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></div>
        <div><label for="f-biz">Store or business</label><input id="f-biz" name="business" autocomplete="organization"></div>
        <div><label for="f-email">Email</label><input id="f-email" type="email" name="email" required autocomplete="email"></div>
        <div><label for="f-phone">Phone</label><input id="f-phone" type="tel" name="phone" autocomplete="tel"></div>
        <div><label for="f-msg">What is going on in your store?</label><textarea id="f-msg" name="message" rows="5" required></textarea></div>
        <button class="btn" type="submit">Send message</button>
        <p class="note">Your message goes straight to Pieter&rsquo;s inbox. No mailing list, no follow-up sequence.</p>
      </form>
    </div>
    <div class="rv">
      <div class="card" style="margin-bottom:18px">
        <h3>Direct lines</h3>
        <ul style="list-style:none;margin-top:14px;display:grid;gap:12px">
          <li><a class="btn btn-w" href="https://wa.me/{wa}?text=Hi%20Pieter%2C%20I%20found%20SocialBrand%20online%20and%20want%20to%20talk%20about%20my%20store.">WhatsApp Pieter</a></li>
          <li>Phone: <a href="tel:{phone_href}"><b>{phone}</b></a></li>
          <li>Email: <a href="mailto:{email}"><b>{email}</b></a></li>
        </ul>
      </div>
      <div class="card">
        <h3>Where we work</h3>
        <p style="margin-top:10px">Based in Cape Town and North West, South Africa. Engagements run wherever the store is, through our appointed agents across South Africa with hubs in Cape Town and Johannesburg.</p>
      </div>
    </div>
  </div>
</div></section>
'''.format(wa=SITE["wa"], phone=SITE["phone"], phone_href=SITE["phone_href"], email=SITE["email"])
    pages.append(render("/contact/", "Contact SocialBrand | Retail consulting, South Africa",
        "Talk to PG van der Westhuizen about your store. WhatsApp, phone or email SocialBrand, the South African retail turnaround practice.",
        contact_body,
        extra_schema={"@type": "ContactPage", "url": SITE["url"] + "/contact/"}))

    thanks_body = '''
<section class="sec" style="min-height:55vh"><div class="wrap" style="text-align:center;max-width:600px">
  <span class="kicker">Message sent</span>
  <h1 style="font-size:clamp(2rem,4vw,3rem)">Thank you</h1>
  <p style="margin:18px auto 30px;color:var(--fg-muted)">Your message is in Pieter&rsquo;s inbox. If it is urgent, WhatsApp is faster.</p>
  <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
    <a class="btn btn-w" href="https://wa.me/{wa}">WhatsApp Pieter</a>
    <a class="btn btn-o" href="/">Back to the site</a>
  </div>
</div></section>
'''.format(wa=SITE["wa"])
    pages.append(render("/contact/thanks/", "Message sent | SocialBrand",
        "Your message has been sent to SocialBrand.", thanks_body))

    return pages
