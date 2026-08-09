# content_demo.py - The public demo dashboard. Fictional store, fully generated data.
# Build note per SB-WEB-001 section 5: a static generated dataset is shipped with the page.
# No live database, no real store codes, no client connection, non-SA fictional identity,
# currency in dollars. Nothing here is a real system, a real product or a real trading figure.
import json, math, random
from datetime import date, timedelta

RND = random.Random(20260718)
LAST_DAY = date(2026, 7, 18)
DAYS = 168
SM, LQ = "sm", "lq"

STORES = [
    {"v": "all", "t": "All stores"},
    {"v": SM, "t": "Fairview SuperMart"},
    {"v": LQ, "t": "Fairview Liquor"},
]
PERIODS = [
    {"v": "30", "t": "Last 30 days"},
    {"v": "90", "t": "Last 90 days"},
    {"v": "all", "t": "Full season"},
]


# ---------------------------------------------------------------- daily series
def series():
    labels, iso, sm, lq, bsm, blq = [], [], [], [], [], []
    for i in range(DAYS):
        d = LAST_DAY - timedelta(days=DAYS - 1 - i)
        dow = d.weekday()
        wk_s = [0.96, 0.92, 0.97, 1.05, 1.24, 1.30, 0.60][dow]
        wk_l = [0.70, 0.68, 0.78, 0.98, 1.48, 1.64, 0.40][dow]
        dom = d.day
        rhythm = 1.0
        if 24 <= dom <= 28:
            rhythm = 1.34
        elif 1 <= dom <= 6:
            rhythm = 1.19
        elif 12 <= dom <= 15:
            rhythm = 1.07
        elif 8 <= dom <= 11:
            rhythm = 0.89
        season = 1.0 + 0.055 * math.sin((i / DAYS) * 3.14159)
        s = round(15800 * wk_s * rhythm * season * RND.uniform(0.94, 1.06))
        l = round(6900 * wk_l * (rhythm * 1.10 if rhythm > 1.2 else rhythm) * season * RND.uniform(0.93, 1.07))
        labels.append(d.strftime("%d %b"))
        iso.append(d.isoformat())
        sm.append(s)
        lq.append(l)
        bsm.append(round(s / RND.uniform(17.4, 19.6)))
        blq.append(round(l / RND.uniform(24.5, 28.5)))
    return {"labels": labels, "iso": iso, "sm": sm, "lq": lq, "bsm": bsm, "blq": blq}


# ---------------------------------------------------------------- departments
DEPTS = [
    {"st": SM, "n": "Grocery",         "sh": .265, "ly": {"30": 3.4,   "90": 2.1,   "all": 1.6}},
    {"st": SM, "n": "Butchery",        "sh": .142, "ly": {"30": 8.9,   "90": 6.2,   "all": 5.1}},
    {"st": SM, "n": "Dairy",           "sh": .118, "ly": {"30": -1.8,  "90": -0.9,  "all": 0.4}},
    {"st": SM, "n": "Household",       "sh": .115, "ly": {"30": -6.2,  "90": -4.4,  "all": -3.1}},
    {"st": SM, "n": "Bakery",          "sh": .092, "ly": {"30": 11.6,  "90": 9.4,   "all": 7.8}},
    {"st": SM, "n": "Beverages",       "sh": .091, "ly": {"30": 2.2,   "90": 3.6,   "all": 4.0}},
    {"st": SM, "n": "Fruit and veg",   "sh": .089, "ly": {"30": -32.7, "90": -24.1, "all": -18.6}},
    {"st": SM, "n": "Frozen",          "sh": .088, "ly": {"30": 5.3,   "90": 4.1,   "all": 2.9}},
    {"st": LQ, "n": "Beer",            "sh": .452, "ly": {"30": 6.8,   "90": 5.5,   "all": 4.7}},
    {"st": LQ, "n": "Spirits",         "sh": .268, "ly": {"30": -9.4,  "90": -7.2,  "all": -5.8}},
    {"st": LQ, "n": "Wine",            "sh": .142, "ly": {"30": 1.4,   "90": 0.8,   "all": 2.2}},
    {"st": LQ, "n": "Ready to drink",  "sh": .092, "ly": {"30": 14.2,  "90": 11.8,  "all": 9.6}},
    {"st": LQ, "n": "Mixers",          "sh": .046, "ly": {"30": -2.6,  "90": -1.9,  "all": -0.7}},
]
DEPT_WHY = {
    "Fruit and veg": "Down hard on last year. Two of the three top lines were out of stock across the payday window, and a shelf with a gap does not argue its case.",
    "Bakery": "Up on last year on the back of the in-store bake plan. Volume, not price. The made-in-store lines earn their space here.",
    "Butchery": "Payday protein carried the month. The build before the wage window did the work, not the promotion after it.",
    "Household": "Softer than last year. Bulk shoppers moved a slice of this basket out of town. It is a trip problem, not a price problem.",
    "Spirits": "Off last year. Part real, part ledger: two high value claims on this department are under count and have not sold in months.",
    "Beer": "The engine of the liquor store. Weekend and payday led, and the pack family reads as one product where it should.",
    "Grocery": "The biggest department and the flattest. It grows on availability rather than on ideas, which is why the staples here are the ones protected from the budget fit.",
    "Dairy": "Marginally behind last year on a department that cannot afford a gap. Two short deliveries in the month explain most of it, and both are ordering decisions rather than shopper decisions.",
    "Frozen": "Ahead of last year and cheap to hold. Freezer space, not demand, is what caps this department, so depth goes to the lines that turn rather than the lines that fill.",
    "Beverages": "Steady growth, weather led at the edges. It behaves like a staple department in the wage window and like a treat department in the third week.",
    "Wine": "Flat against last year in a category that holds well. That combination makes it the natural place to stand still for a delivery when a route runs tight.",
    "Ready to drink": "The fastest growing shelf in the group and the youngest habit. Depth follows it up in steps, because a trend bought as a certainty is how dead stock is born.",
    "Mixers": "Small, slightly behind, and tied to the spirits shelf next to it. It is read alongside spirits rather than judged on its own line.",
}


# ---------------------------------------------------------------- product universe
def P(n, d, st, pk, c, marg, r, cov, nm=0):
    price = round(c * (1 + marg), 2)
    return {"n": n, "d": d, "st": st, "pk": pk, "c": c, "p": price, "r": r,
            "oh": round(r * cov) if r > 0 else round(cov), "nm": nm,
            "mx": [round(RND.uniform(.86, 1.18), 3), 1.0, round(RND.uniform(.9, 1.08), 3)]}


PRODUCTS = [
    P("White bread 700g",              "Bakery",        SM, "700 g loaf",     8.10,  .38, 64.0, 1.4),
    P("Brown bread 700g",              "Bakery",        SM, "700 g loaf",     7.90,  .36, 31.5, 1.6),
    P("Long-life milk 1L",             "Dairy",         SM, "6 x 1 L",        9.40,  .27, 38.2, 2.5),
    P("Fresh milk 2L",                 "Dairy",         SM, "6 x 2 L",       17.20,  .24, 26.4, 1.8),
    P("Large eggs 18s",                "Dairy",         SM, "tray of 18",    33.10,  .23, 14.2, 2.2),
    P("Rice 5kg",                      "Grocery",       SM, "4 x 5 kg",      42.50,  .21,  9.1, 3.0),
    P("Sunflower cooking oil 2L",      "Grocery",       SM, "6 x 2 L",       31.20,  .19, 12.4, 2.4),
    P("White sugar 2.5kg",             "Grocery",       SM, "6 x 2.5 kg",    19.80,  .17, 15.3, 2.1),
    P("Pasta 500g",                    "Grocery",       SM, "20 x 500 g",     7.80,  .30, 18.6, 3.4),
    P("Baked beans 410g",              "Grocery",       SM, "24 x 410 g",     6.20,  .32, 22.8, 2.8),
    P("Tinned tuna 170g",              "Grocery",       SM, "24 x 170 g",    11.40,  .29,  9.7, 3.1),
    P("Instant coffee 200g",           "Grocery",       SM, "6 x 200 g",     34.60,  .26,  6.4, 3.6),
    P("Tea bags 100s",                 "Grocery",       SM, "12 x 100s",     15.10,  .28,  4.9, 4.2),
    P("Breakfast cereal 750g",         "Grocery",       SM, "10 x 750 g",    24.90,  .25,  7.2, 3.2),
    P("Beef mince 1kg",                "Butchery",      SM, "10 x 1 kg",     62.40,  .22, 11.8, 1.2),
    P("Chicken breast fillets 1kg",    "Butchery",      SM, "8 x 1 kg",      58.90,  .21,  9.4, 1.3),
    P("Pork sausages 500g",            "Butchery",      SM, "12 x 500 g",    24.30,  .26,  7.6, 1.5),
    P("Bananas per kg",                "Fruit and veg", SM, "18 kg carton",  12.60,  .34, 21.3, 0.9),
    P("Potatoes 7kg",                  "Fruit and veg", SM, "7 kg pocket",   48.00,  .24,  6.8, 1.4),
    P("Tomatoes 1kg",                  "Fruit and veg", SM, "6 x 1 kg",      14.90,  .31, 12.1, 1.1),
    P("Frozen chicken portions 2kg",   "Frozen",        SM, "6 x 2 kg",      54.20,  .20, 11.4, 1.7),
    P("Frozen mixed vegetables 1kg",   "Frozen",        SM, "12 x 1 kg",     16.40,  .27,  8.3, 2.6),
    P("Ice cream 2L",                  "Frozen",        SM, "6 x 2 L",       28.70,  .29,  6.1, 2.9),
    P("Washing powder 3kg",            "Household",     SM, "4 x 3 kg",      56.80,  .18,  5.9, 2.7),
    P("Toilet rolls 9s",               "Household",     SM, "6 x 9s",        41.30,  .22,  8.7, 2.3),
    P("Dishwashing liquid 750ml",      "Household",     SM, "12 x 750 ml",   12.40,  .30,  6.2, 3.3),
    P("Bar soap 175g",                 "Household",     SM, "24 x 175 g",     4.90,  .33,  9.8, 3.8),
    P("Cola 2L",                       "Beverages",     SM, "6 x 2 L",       17.60,  .23, 19.4, 2.0),
    P("Sparkling water 500ml",         "Beverages",     SM, "24 x 500 ml",    5.30,  .35, 17.8, 2.4),
    P("Fruit juice 1.5L",              "Beverages",     SM, "6 x 1.5 L",     21.40,  .26,  8.6, 2.8),
    P("Imported olive tapenade 200g",  "Grocery",       SM, "6 x 200 g",     26.40,  .42, 0.10, 270, 1),
    P("Speciality rice vinegar 500ml", "Grocery",       SM, "6 x 500 ml",    19.80,  .40, 0.06, 168, 1),
    P("Lager 440ml case",              "Beer",          LQ, "24 x 440 ml",  236.00,  .14,  4.1, 1.9),
    P("Lager 330ml 6-pack",            "Beer",          LQ, "4 x 6 x 330",   71.50,  .16,  9.8, 1.8),
    P("Premium lager 660ml",           "Beer",          LQ, "12 x 660 ml",   19.40,  .19,  6.3, 2.2),
    P("Cider 500ml",                   "Ready to drink",LQ, "12 x 500 ml",   18.90,  .21,  7.4, 2.5),
    P("Rum and cola cans 6-pack",      "Ready to drink",LQ, "4 x 6 x 440",   62.80,  .20,  5.5, 2.6),
    P("Dry white wine 750ml",          "Wine",          LQ, "6 x 750 ml",    42.00,  .23,  5.2, 3.0),
    P("Red blend wine 750ml",          "Wine",          LQ, "6 x 750 ml",    46.50,  .22,  6.0, 2.7),
    P("Blended whisky 750ml",          "Spirits",       LQ, "6 x 750 ml",   152.00,  .17,  2.4, 3.5),
    P("Vodka 750ml",                   "Spirits",       LQ, "6 x 750 ml",   118.00,  .18,  2.1, 3.9),
    P("Brandy 750ml",                  "Spirits",       LQ, "6 x 750 ml",   134.00,  .17,  1.8, 4.4),
    P("Premium gin 750ml",             "Spirits",       LQ, "6 x 750 ml",   178.00,  .25, 0.60,  68, 1),
    P("Single malt whisky 750ml",      "Spirits",       LQ, "6 x 750 ml",   386.00,  .28, 0.00,  60, 1),
]


# ---------------------------------------------------------------- stock health
STOCK = [
    {"c": "10412", "n": "White bread 700g", "d": "Bakery", "pk": "700 g loaf", "st": SM,
     "qty": -142, "val": 0, "tag": "neg", "pill": ["red", "Negative"],
     "story": "Sells every day, yet the book shows minus 142. Receipts post to a different product code than the one the till sells. One receiving fix at source ends it. Until then the ledger is what is broken, not the shelf."},
    {"c": "10486", "n": "Brown bread 700g", "d": "Bakery", "pk": "700 g loaf", "st": SM,
     "qty": -78, "val": 0, "tag": "neg", "pill": ["red", "Negative"],
     "story": "The same receiving break, one code along. Two lines failing the same way is a process telling on itself. Fixing the pair at source clears both without a single adjustment."},
    {"c": "88451", "n": "Single malt whisky 750ml", "d": "Spirits", "pk": "6 x 750 ml", "st": LQ,
     "qty": 60, "val": 23160, "tag": "phantom", "pill": ["red", "Phantom"],
     "story": "Claims 60 units and has sold nothing in 214 days, while its twin code sells a few a week and claims one. The quiet twin is indicted, not confirmed, by the selling sibling. Count the live code, then zero the ghost once the count proves it."},
    {"c": "50318", "n": "Premium gin 750ml", "d": "Spirits", "pk": "6 x 750 ml", "st": LQ,
     "qty": 41, "val": 7298, "tag": "count", "pill": ["amber", "Count first"],
     "story": "High value, no sale in 47 days, and the last count is old enough that the claim has aged out of proof. It goes onto tomorrow's count list ahead of any order, ranked by the money at risk."},
    {"c": "33108", "n": "Paper cups 250ml sleeve", "d": "Household", "pk": "20 sleeves", "st": SM,
     "qty": 2844, "val": 28700, "tag": "cost", "pill": ["red", "Cost error"],
     "story": "A carton cost captured as a unit cost. The line claims $28,700 of capital on stock worth about a thousand. That capital is fiction created by arithmetic. Fix the cost and the capital view corrects itself."},
    {"c": "33240", "n": "Disposable serviettes 200s", "d": "Household", "pk": "12 x 200s", "st": SM,
     "qty": 640, "val": 9120, "tag": "cost", "pill": ["amber", "Cost error"],
     "story": "Same shape of error, smaller money. Captured off a supplier line that priced by carton while the store buys by pack. It inflates capital and quietly suppresses the margin the department reports."},
    {"c": "20871", "n": "Bread flour 12.5kg", "d": "Bakery", "pk": "12.5 kg bag", "st": SM,
     "qty": 388, "val": 11640, "tag": "phantom", "pill": ["amber", "Production ghost"],
     "story": "Received as an ingredient, consumed by the bake, never sold on its own code. The bread it became sold fine. This is the made-in-store world wearing a buy-and-sell code. It routes to production rules, not to an adjustment."},
    {"c": "45220", "n": "Lager 440ml case", "d": "Beer", "pk": "24 x 440 ml", "st": LQ,
     "qty": 0, "val": 0, "tag": "clean", "pill": ["amber", "Family split"],
     "story": "The case code reads zero while singles sell all day. Demand rolls up the pack family, so the case's share hides inside the singles. Ordering already reads the family as one product, so no action is needed here."},
    {"c": "77645", "n": "Returnable crates (deposit)", "d": "Grocery", "pk": "crate", "st": SM,
     "qty": -1893, "val": 0, "tag": "neg", "pill": ["amber", "Deposit line"],
     "story": "A negative on a deposit line is real money moving through the crate cycle, not an error. It is protected from automatic correction. Reconcile the deposit account, never zero it."},
    {"c": "61003", "n": "Long-life milk 1L", "d": "Dairy", "pk": "6 x 1 L", "st": SM,
     "qty": 214, "val": 2012, "tag": "clean", "pill": ["green", "Proven"],
     "story": "Counted six days ago, sells 38 a day, claim and behaviour agree. Known present, and nothing to do. Most of a healthy ledger should read exactly this dull."},
    {"c": "61077", "n": "Fresh milk 2L", "d": "Dairy", "pk": "6 x 2 L", "st": SM,
     "qty": 48, "val": 826, "tag": "clean", "pill": ["green", "Proven"],
     "story": "Short shelf life, high turn, counted into the last cycle. The number is small because the line is working, not because it is missing."},
    {"c": "92210", "n": "Imported olive tapenade 200g", "d": "Grocery", "pk": "6 x 200 g", "st": SM,
     "qty": 27, "val": 713, "tag": "count", "pill": ["amber", "Count first"],
     "story": "One sale in the last two months against 27 on the book. The claim is not obviously wrong, it is simply unproven, and the exit plan cannot be priced until the count says what is actually there."},
    {"c": "45702", "n": "Vodka 750ml", "d": "Spirits", "pk": "6 x 750 ml", "st": LQ,
     "qty": -12, "val": 0, "tag": "neg", "pill": ["red", "Negative"],
     "story": "Sold twelve more than it ever received. Either a delivery never captured or a code mixed up at receiving. High value, so it is counted this week rather than next."},
    {"c": "39114", "n": "Frozen mixed vegetables 1kg", "d": "Frozen", "pk": "12 x 1 kg", "st": SM,
     "qty": 74, "val": 1214, "tag": "clean", "pill": ["green", "Proven"],
     "story": "Steady seller, counted inside the cycle, claim consistent with the till. It appears here only because the department was reviewed, and it passed."},
]

STOCK_FILTERS = [
    {"v": "all", "t": "All"},
    {"v": "neg", "t": "Negatives"},
    {"v": "phantom", "t": "Phantom"},
    {"v": "cost", "t": "Cost errors"},
    {"v": "count", "t": "Count first"},
]


# ---------------------------------------------------------------- capital
CAPITAL = {
    "raw": {"total": 412480, "working": 268400, "slow": 71180, "dead": 72900,
            "label": "Raw ledger claim",
            "why": "What the ledger claims before anyone tests the claims. This is where most owners stop reading. It is also the least true number on the page."},
    "pure": {"total": 318290, "working": 226140, "slow": 56010, "dead": 36140,
             "label": "Purified capital",
             "why": "The raw claim with invented cost, unproven records and deposit lines taken out. Only purified capital is allowed to steer a decision."},
    "gap": [
        {"n": "Cost captured against the wrong pack", "v": 37820,
         "why": "Two lines carry a carton cost on a single unit. The stock is real, the money is not. Fix the cost at source and the capital falls without a single unit moving."},
        {"n": "Claims that cannot prove they exist", "v": 30760,
         "why": "High value lines with no sale and no recent count. They are not written off, they are counted. A claim under audit is not capital until it is proven."},
        {"n": "Deposit and crate balances", "v": 25610,
         "why": "Money in the crate cycle, sitting in the stock number where it does not belong. It is reconciled against the deposit account, never adjusted away."},
    ],
    "offenders": [
        {"n": "Single malt whisky 750ml", "d": "Spirits", "pk": "6 x 750 ml", "v": 23160, "days": 214,
         "why": "The largest single unproven claim in the group. No sale in seven months, and the count that would settle it is scheduled ahead of every other line by value at risk."},
        {"n": "Speciality rice vinegar 500ml", "d": "Grocery", "pk": "6 x 500 ml", "v": 3326, "days": 186,
         "why": "Bought for a range that never found its shopper. Dead capital does not get company: no reorder, and an exit plan with a date on it."},
        {"n": "Imported olive tapenade 200g", "d": "Grocery", "pk": "6 x 200 g", "v": 713, "days": 61,
         "why": "Nine months of stock on hand at the rate it actually sells. Small money, but it is the shape of the mistake that matters, repeated across a range."},
        {"n": "Brandy 750ml", "d": "Spirits", "pk": "6 x 750 ml", "v": 4288, "days": 38,
         "why": "Slow rather than dead. It still sells, just far more slowly than it was bought. It orders again only once the shelf has earned it."},
        {"n": "Speciality preserves range", "d": "Grocery", "pk": "assorted", "v": 5940, "days": 92,
         "why": "Eleven codes, each too small to notice on its own, one number worth noticing together. Ranged out as a block, cleared as a block."},
    ],
}


# ---------------------------------------------------------------- ordering desk
DESKS = [
    {"v": "dry",    "t": "Dry grocery route",  "st": SM},
    {"v": "fresh",  "t": "Perishables route",  "st": SM},
    {"v": "frozen", "t": "Frozen route",       "st": SM},
    {"v": "house",  "t": "Household route",    "st": SM},
    {"v": "liq",    "t": "Liquor route",       "st": LQ},
]

DELIVERY_DATES = [
    {"v": "2026-07-20", "t": "Mon 20 Jul"},
    {"v": "2026-07-22", "t": "Wed 22 Jul"},
    {"v": "2026-07-24", "t": "Fri 24 Jul"},
    {"v": "2026-07-27", "t": "Mon 27 Jul"},
    {"v": "2026-07-29", "t": "Wed 29 Jul"},
]

PRESETS = [
    {"v": "standard",  "t": "Standard"},
    {"v": "essential", "t": "Order essentials"},
    {"v": "catchup",   "t": "Catch-up"},
]
PRESET_WHY = {
    "standard": "The full shelf. Every line the route carries, ordered to the demand it has actually demonstrated.",
    "essential": "A short week. The lines the town judges the store by keep their depth, the comfortable extras stand still for one delivery.",
    "catchup": "Coming off a run of gaps. Depth steps up on the lines that ran empty, so the shelf recovers before the next window rather than after it.",
}
BASES = [
    {"v": "normal", "t": "Normal"},
    {"v": "geared", "t": "Geared"},
]
BASIS_WHY = {
    "normal": "Ordered to the rate the line sells on an ordinary week.",
    "geared": "Geared to the wage window. The lines this town buys on payday get their build before the money lands, not after it.",
}


def L(n, d, desk, pk, cs, c, r, cov, klass, story, payday=0, floor=0):
    return {"n": n, "d": d, "desk": desk, "pk": pk, "cs": cs, "c": c, "r": r,
            "oh": round(r * cov), "k": klass, "pd": payday, "fl": floor, "story": story}


LINES = [
    # ---- dry grocery route
    L("Long-life milk 1L", "Dairy", "dry", "6 x 1 L", 6, 9.40, 38.2, 2.1, "kvi",
      "Flat staple, same rate all month. Demand read from what sold, never from what the book claims. Filled to its working depth, the cheapest availability insurance in the store.", 0, 138),
    L("White bread 700g", "Bakery", "dry", "700 g loaf", 12, 8.10, 64.0, 0.6, "kvi",
      "A line this town judges the store by. Its floor is protected and the budget fit is not allowed to touch it. The negative book quantity is a ledger repair, not a reason to under-order bread.", 0, 360),
    L("Rice 5kg", "Grocery", "dry", "4 x 5 kg", 4, 42.50, 9.1, 2.2, "core",
      "Bulk staple with a hard payday shape. Ordered to demonstrated rate, with the window in mind rather than the calendar month.", 1),
    L("Sunflower cooking oil 2L", "Grocery", "dry", "6 x 2 L", 6, 31.20, 12.4, 1.9, "core",
      "Moves with the protein lines. When mince builds, oil builds, and the two are read together rather than as strangers.", 1),
    L("White sugar 2.5kg", "Grocery", "dry", "6 x 2.5 kg", 6, 19.80, 15.3, 2.0, "core",
      "Steady, predictable, and heavily bought in the wage window. Depth follows the window, not a flat weekly average.", 1),
    L("Pasta 500g", "Grocery", "dry", "20 x 500 g", 20, 7.80, 18.6, 2.6, "core",
      "High units, low value, cheap to hold. It is ordered deep because running out costs more than the stock ever will."),
    L("Baked beans 410g", "Grocery", "dry", "24 x 410 g", 24, 6.20, 22.8, 2.4, "core",
      "Fast tinned line with a long life. Case size does the rounding, so the order lands in whole cases the supplier will actually pick."),
    L("Tinned tuna 170g", "Grocery", "dry", "24 x 170 g", 24, 11.40, 9.7, 2.9, "flex",
      "Comfortable line, flexible depth. It flexes so the protected lines never have to."),
    L("Instant coffee 200g", "Grocery", "dry", "6 x 200 g", 6, 34.60, 6.4, 3.1, "flex",
      "Slower, higher value, forgiving on availability. First to give ground when the route is tight, and it gives it without hurting the shopper."),
    L("Breakfast cereal 750g", "Grocery", "dry", "10 x 750 g", 10, 24.90, 7.2, 2.8, "flex",
      "Range line rather than a destination line. It earns its depth in a normal week and gives it back in a short one."),
    L("Imported olive tapenade 200g", "Grocery", "dry", "6 x 200 g", 6, 26.40, 0.10, 270, "dead",
      "Nine months of stock on hand at the rate it sells. Dead capital does not get company. This line gets an exit plan, not another order."),
    # ---- perishables route
    L("Fresh milk 2L", "Dairy", "fresh", "6 x 2 L", 6, 17.20, 26.4, 1.5, "kvi",
      "Short life, daily delivery, no tolerance for a gap. Its floor holds whatever else happens on the route.", 0, 96),
    L("Large eggs 18s", "Dairy", "fresh", "tray of 18", 6, 33.10, 14.2, 1.8, "kvi",
      "A price-watched line. Shoppers check it on the way in, and an empty rail here is read as a store in trouble.", 0, 60),
    L("Beef mince 1kg", "Butchery", "fresh", "10 x 1 kg", 10, 62.40, 11.8, 1.1, "core",
      "Payday protein. This is the second of the deliveries before the wage window, so the build steps up now. Ordering after payday is ordering for a party already over.", 1),
    L("Chicken breast fillets 1kg", "Butchery", "fresh", "8 x 1 kg", 8, 58.90, 9.4, 1.2, "core",
      "Follows mince by a day. Fresh, so depth is bought in what the counter can actually sell before it ages.", 1),
    L("Pork sausages 500g", "Butchery", "fresh", "12 x 500 g", 12, 24.30, 7.6, 1.4, "flex",
      "Supporting line in the counter mix. Useful, not decisive, so it carries the flex for the department."),
    L("Bananas per kg", "Fruit and veg", "fresh", "18 kg carton", 18, 12.60, 21.3, 0.8, "core",
      "The department is down on last year mostly because this line kept running out. Depth here is a recovery decision, not an optimism decision."),
    L("Potatoes 7kg", "Fruit and veg", "fresh", "7 kg pocket", 10, 48.00, 6.8, 1.3, "core",
      "Bulk vegetable that carries the basket on payday weekends. Ordered in pockets the store can turn before they sprout.", 1),
    L("Tomatoes 1kg", "Fruit and veg", "fresh", "6 x 1 kg", 6, 14.90, 12.1, 1.0, "flex",
      "Perishable and volatile. Depth is deliberately short here, because waste on this line costs more than a thin afternoon does."),
    # ---- frozen route
    L("Frozen chicken portions 2kg", "Frozen", "frozen", "6 x 2 kg", 6, 54.20, 11.4, 1.5, "core",
      "Runs hot in the wage window and holds well in the freezer. That combination is what makes an early build safe here.", 1),
    L("Frozen mixed vegetables 1kg", "Frozen", "frozen", "12 x 1 kg", 12, 16.40, 8.3, 2.4, "core",
      "Long life, steady rate, no drama. Ordered to rate and left alone."),
    L("Ice cream 2L", "Frozen", "frozen", "6 x 2 L", 6, 28.70, 6.1, 2.7, "flex",
      "Weather led and freezer space bound. It flexes with the route rather than fighting for depth it cannot store."),
    # ---- household route
    L("Washing powder 3kg", "Household", "house", "4 x 3 kg", 4, 56.80, 5.9, 2.5, "core",
      "Bulk household bought in the wage window and nowhere else. Depth before the window, quiet after it.", 1),
    L("Toilet rolls 9s", "Household", "house", "6 x 9s", 6, 41.30, 8.7, 2.0, "kvi",
      "Watched as closely as bread and milk. An empty bay here gets talked about in town, so its floor is protected.", 0, 48),
    L("Dishwashing liquid 750ml", "Household", "house", "12 x 750 ml", 12, 12.40, 6.2, 3.0, "flex",
      "Long life, low value, easy to hold. Ideal flex line, and it is used as one."),
    L("Bar soap 175g", "Household", "house", "24 x 175 g", 24, 4.90, 9.8, 3.4, "flex",
      "Cheap, fast and forgiving. Ordered in full cases because the handling cost of anything else is worse than the stock cost."),
    # ---- liquor route
    L("Lager 440ml case", "Beer", "liq", "24 x 440 ml", 1, 236.00, 4.1, 1.6, "core",
      "Cases ordered on family demand, read across the case and the singles together. The case code's own zero would have starved the shelf.", 1),
    L("Lager 330ml 6-pack", "Beer", "liq", "4 x 6 x 330", 4, 71.50, 9.8, 1.6, "core",
      "The weekend engine of the liquor store. Depth is built on Thursday, because Friday afternoon is too late to be right.", 1),
    L("Premium lager 660ml", "Beer", "liq", "12 x 660 ml", 12, 19.40, 6.3, 2.0, "core",
      "Higher price point, loyal buyer, low volatility. Ordered to its own rate rather than to the department's average."),
    L("Cider 500ml", "Ready to drink", "liq", "12 x 500 ml", 12, 18.90, 7.4, 2.3, "flex",
      "Growing on last year, and still treated as flexible until the growth proves it is a habit rather than a summer."),
    L("Rum and cola cans 6-pack", "Ready to drink", "liq", "4 x 6 x 440", 4, 62.80, 5.5, 2.4, "flex",
      "The fastest growing shelf in the store and the least proven. Depth follows it up in steps, not in leaps."),
    L("Dry white wine 750ml", "Wine", "liq", "6 x 750 ml", 6, 42.00, 5.2, 2.8, "flex",
      "Wine holds. That makes it the natural place to take a week off when the route budget is tight."),
    L("Red blend wine 750ml", "Wine", "liq", "6 x 750 ml", 6, 46.50, 6.0, 2.5, "core",
      "The one wine that behaves like a staple in this town. Treated accordingly."),
    L("Blended whisky 750ml", "Spirits", "liq", "6 x 750 ml", 6, 152.00, 2.4, 3.2, "core",
      "Slow, valuable and heavily payday led. Small quantities, timed well, beat big quantities timed badly.", 1),
    L("Premium gin 750ml", "Spirits", "liq", "6 x 750 ml", 6, 178.00, 0.60, 68, "count",
      "The book claims 41, and the claim is old with no recent sale behind it. Counting before ordering beats ordering onto a phantom. Zero here is a decision, not a miss."),
    L("Single malt whisky 750ml", "Spirits", "liq", "6 x 750 ml", 6, 386.00, 0.0, 60, "count",
      "The largest unproven claim in the group sits on this line. Nothing gets ordered against a number that cannot prove itself."),
]


# ------------------------------------------------- budget calibration (build time only)
def _std_total(desk, horizon=6):
    tot = 0.0
    for l in LINES:
        if l["desk"] != desk:
            continue
        if l["k"] in ("count", "dead"):
            continue
        oh = max(0, l["oh"])
        need = l["r"] * horizon - oh
        qty = max(0, math.ceil(need / l["cs"]) * l["cs"]) if need > 0 else 0
        if l["k"] == "kvi":
            qty = max(qty, l["fl"])
        tot += qty * l["c"]
    return tot


def desks_with_budgets():
    out = []
    for d in DESKS:
        t = _std_total(d["v"])
        out.append(dict(d, budget=int(round(t * 0.87 / 50.0) * 50)))
    return out


def payload():
    s = series()
    return {
        "meta": {
            "last": LAST_DAY.strftime("%d %b %Y"),
            "snapshots": 25,
            "stores": STORES,
            "periods": PERIODS,
            "basket": {"sm": 18.4, "lq": 26.5},
            "margin": {"sm": 21.4, "lq": 16.8, "smly": 0.6, "lqly": -0.4},
        },
        "sales": s,
        "depts": DEPTS,
        "deptWhy": DEPT_WHY,
        "prods": PRODUCTS,
        "stock": STOCK,
        "stockFilters": STOCK_FILTERS,
        "capital": CAPITAL,
        "order": {
            "desks": desks_with_budgets(),
            "dates": DELIVERY_DATES,
            "presets": PRESETS,
            "presetWhy": PRESET_WHY,
            "bases": BASES,
            "basisWhy": BASIS_WHY,
            "lines": LINES,
        },
    }


TABS = [
    ("rhythm", "Sales rhythm"),
    ("movers", "Top movers"),
    ("stock", "Stock health"),
    ("capital", "Capital"),
    ("orders", "Ordering"),
]


def build(render, SITE):
    data = json.dumps(payload(), ensure_ascii=False, separators=(",", ":"))
    tabs = "".join(
        f'<button role="tab" id="tab-{k}" aria-controls="dashBody" '
        f'aria-selected="{"true" if i == 0 else "false"}" tabindex="{"0" if i == 0 else "-1"}" '
        f'data-view="{k}">{label}</button>'
        for i, (k, label) in enumerate(TABS))

    body = '''
<section class="hero-page"><div class="wrap"><div class="hero-in">
  <p class="crumbs" style="color:var(--sky-muted)"><a href="/">Home</a> / Live Demo</p>
  <span class="kicker">Live demo &middot; generated data</span>
  <h1>Fairview SuperMart &amp; Liquor</h1>
  <p class="lead">A fictional independent supermarket and liquor store in the fictional town of Fairview. Every number below is generated. What is real is the thinking: each figure carries the reason it exists, and the controls recompute the answer in front of you. Real clients see their own stores.</p>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="dash rv">
    <div class="dash-top">
      <p class="t">Fairview group <small>Data to close of trade ''' + LAST_DAY.strftime("%d %b %Y") + ''' &middot; read-only demo on generated data</small></p>
      <div class="dash-tabs" role="tablist" aria-label="Dashboard views">''' + tabs + '''</div>
    </div>
    <div class="dash-body" id="dashBody" role="tabpanel" aria-labelledby="tab-rhythm" tabindex="0"></div>
    <div class="dash-note"><b>Generated demonstration data.</b> Fairview SuperMart and Fairview Liquor do not exist, and no figure on this page comes from a real store. Any resemblance to a real business is coincidental. The platform behind this demo runs on a client&rsquo;s own till and ledger data, privately, and is never published.</div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="grid g3">
    <div class="card rv"><h3>Why every number has a &ldquo;why&rdquo;</h3><p>Analytics you cannot interrogate is decoration. Every figure above can be opened and read in plain language. That is the <a href="/method/story-test/">Story Test</a>, and no verdict ships without passing it.</p></div>
    <div class="card rv"><h3>What the demo shows</h3><p>The payday rhythm, the lines actually carrying the store, phantom stock surfaced with its biography, capital split into working, slow and dead, and an order desk where changing a control changes the order in front of you.</p></div>
    <div class="card rv"><h3>What your store would see</h3><p>The same views on your own data, fed daily from your own tills, after the integrity work makes the numbers worth looking at. Start with the <a href="/pricing/">Store Health Audit</a>.</p></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>Want this for a real store?</h2><p>The audit is the door. Fixed fee, two to three weeks, findings in rand.</p></div>
    <div style="display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="/audit/">Book the audit</a><a class="btn btn-o" href="/audit/sample-findings/">See a sample finding</a></div>
  </div>
</div></section>
<script>window.DEMO_DATA = ''' + data + ''';</script>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>
<script src="/static/demo.js" defer></script>
'''
    return [render("/demo/", "Live Demo | The SocialBrand retail data platform on a fictional store",
        "An interactive demo of the SocialBrand retail data platform: sales rhythm, top movers, stock health, capital and a working order desk for a fictional store on fully generated data. Every number carries its reason.",
        body)]
