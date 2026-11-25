# What the Top Entries Look Like — news-image-20261125

Rewritten v7: 25 Nov 2026 ~15:00 WIB, after Goldfish round 6 cleared
the v6 entry for submission. The facts below are the same ones the
earlier analysis recorded; only the wording and the arrangement are
new. Sources: RULES.txt and competition.yaml for this contest, the
judge setup (z-ai/glm-5.3-flash, head-to-head 2v2), the verified
winning pictures from news-image-20261124 round 1 (winner images for
rounds 1, 2, 3 and 5 read directly on 25 Nov ~02:45 WIB), and our
own entry as it stands in v6.

## Where the contest stands right now

This contest runs blind rounds: no rival ranks, scores or entries
are visible before a round is judged. Round 1 closes today,
25 Nov at 19:00 WIB. The ni24 rhythm was 07:00 / 19:00 /
07:00 / 19:00 / final, and ni25 is expected to follow it.

Because round 1 has not been judged yet, nothing in this note quotes
a rival entry from today. Every pattern below comes from ni24
round 1 winners instead. Once round 1 is judged at 19:00 WIB, this
note has to be refreshed against the real board before the
one-third checkpoint (~26 Nov 23:00 WIB).

## The money and the bar

Fifty paid places share $100: $20 for 1st, $12 for 2nd, $6 for 3rd,
$2 each for 4th–10th, $1.20 each for 11th–50th. The aim is the top
10; rank 25 is the floor we will not go below; outside the top 50
the prize is $0. The final heat is a Swiss stage plus a playoff
for the top 52, so reaching the top 52 in the Swiss is the first
line that has to be crossed.

How hard the line is can be read off ni24 round 1: rank 1 scored
863,545, rank 10 scored 803,073, and rank 50 — the last paid place
— scored 654,221. Our own ni24 round 1 entry, a plain-text grid,
landed at rank 4,805 of 7,302 with a score of 458,194. A grid with
no pictures loses badly to an illustrated newspaper; that gap is
the whole reason this entry is built the way it is.

## What the ni24 round 1 winners actually did

Reading the winning pictures, five habits recur, and they recur
together — no winner has only some of them:

- **A newspaper, not a list.** A giant serif masthead with the
  full date ("TUESDAY 24 NOVEMBER 2026" in ni24), a strip stating
  how many stories, regions and fields are inside, a region bar
  whose numbers add up exactly to the story count, a UTC timeline
  strip, and a "THE DAY IN NUMBERS" strip.
- **Three big illustrated leads**, each with headline, deck,
  source and a status badge (CLAIM / CONFIRMED / OFFICIAL /
  REPORTED), plus about ten smaller illustrated panels, a numbered
  "ALSO ON" list, and a world map carrying numbered pins.
- **A DATE CHECK footer that tells the truth**, naming the date
  claim in plain words and then listing the stories that were
  deliberately left out because they happened the day before.
- **Breadth of 34–40 stories** across 9–10 regions and several
  beats. The ni24 rank 1 also carried 34 stories, so the count
  itself is not what separates winners — the visual craft and
  the structure do.
- **Readable when shrunk to about 300 px, faithful, with no
  garbled or overlapping text.** The judge punishes a wrong date
  claim and a number it knows to be wrong.

## Our entry, measured against those habits

The masthead reads "THE WORLD IN ONE DAY / WEDNESDAY 25 NOVEMBER
2026". The page is an illustrated newspaper: masthead, region bar,
UTC timeline, "THE DAY IN NUMBERS", three heroes, ten secondary
panels, a numbered ALSO ON list (#14–34), a world map with pins,
and a DATE CHECK footer with an honest exclusion list of the big
24 Nov stories deliberately left out. That is the winner's shape,
not the plain grid that lost in ni24 round 1. The three heroes
are: (1) Shenzhou-24 lifting off at 00:18 UTC, with Zeeshan Ali
the first Pakistani in orbit and the first foreigner aboard
Tiangong; (2) Australia and Solomon Islands signing a security
pact in Canberra on 25 Nov; (3) the US Army detonating 68 barrels
of lead azide in Iowa on 25 Nov. The numbers strip reads 4.9% ·
68 · 187 · 25,113 · 2,212. The ten secondary
panels and the 21 ALSO ON rows bring the total to 34 stories; among
the items Goldfish verified in rounds 4–6 are Korea births jumping
12.2% in September (25,113, #16), Korea mortgage rates at a 14-year
high (#26), Seoul weighing tech to stop AI exam cheating (#27),
Hyundai Mobis winning $742M in parts orders (#31), and FM Cho
urging strategic aid at KOICA (#33), alongside the two v6
replacements described below.

The file is entry.png, 1024×1024 JPEG, 325,798 bytes, sha256
4967825d8cf7ba7e29f8f7815c8fc2cda0fc26af27f94cd4d0b705e78b689a7a.
The runner is main.py, standard library only: copy plus a check
of size, SHA-256 and magic bytes, verified byte-identical across
two runs (see build-log.md).

## What changed in v6, and why it matters

Goldfish round 5 had reopened the date blocker: #30 (Blanche
dodging an Nvidia probe) failed — the presser was Tuesday 24 Nov
and the BBC published it at 2026-11-24T21:45:46Z — and #19 (Guam
El Niño drought risk) leaned fail, its substance running 18–24 Nov.
Version 6 replaced both with stories verified from their primary
outlets as first reported on Wednesday 25 Nov: #30 became German
GDP growing just 0.1% in Q3 (Reuters, published
2026-11-25T07:01:40Z; the Destatis detailed release was scheduled
for Wed 25 Nov 08:00 Berlin = 07:00 UTC), and #19 became Japan
services inflation jumping 4.2% (Reuters, URL slug 2026-11-25;
Bank of Japan services PPI, October +4.2% year on year, September
revised to 3.8%). In the same round the #15 headline was softened
— "first in 5 months" was dropped because it is not in the AJP
body — the map pins labelled 9-10 and 4-5 were widened so their
labels fit inside the circles, and the footer exclusions were
updated to open with the two v5 failures plus the v6 rejects (the
UN femicide brief of 24 Nov, the Sarkozy–Bruni trial order of
24 Nov, the North Korea Christians report of 24 Nov). The region
bar was recomputed to APAC 23 · AMERICAS 2 · EUROPE 6 ·
MIDDLE EAST 1 · AFRICA 2, which adds to 34. The numbers strip was
left untouched, because no figure in it came from #19 or #30.

## Where Goldfish round 6 left us

Goldfish's short re-review of v6 (25 Nov ~14:50 WIB) verified
both replacements directly from Reuters and confirmed the
fixer's tally: **32 items clean, 2 grey-leaning-pass (#6 Houthis,
#14 bigeye tuna), 0 failed.** Verdict: LAYAK SUBMIT, before the
round 1 cutoff at 19:00 WIB today. The region bar was recount-checked
from the picture and reconciles; the #15 softening and the wider
9-10 / 4-5 pins were confirmed on the page; the footer reads in
full, compiled ~07:35 UTC, with the German GDP release of 07:01 UTC
inside the compilation window.

Goldfish's honest estimate for v6, modelling a field of roughly
7,000–9,000 entries with hundreds of competent clones of the same
winner template (ni24 round 1 had 7,302 entries), is **rank
~50–150, top-50 chance ~30–40%, top-10 chance ~3–5%**. That is the
chase-top-10 floor, not a promise: the prize line in ni24 round 1
(rank 50 = 654,221) demands a high win rate, and an estimate that
only compares against the top 3 is how ni24 round 1 was misjudged
(estimated top 10–25, landed rank 4,805).

## What still holds the entry back

| Weakness | Why it costs us |
|---|---|
| **APAC/Korea concentration (M6).** APAC is 23 of 34 stories, about 14 of them Korea-themed, across only 5 regions; Latin America has none, and Oceania is not a region of its own | In a 2v2 against a winner spread over 9–10 regions, this can read as "a Korean paper plus the world" |
| **Two grey items left (#6, #14).** Both lean pass and are unchanged since round 4/5, but both are fragile if the judge checks dates strictly | A single date failure is the most heavily punished error class |
| **Compiled ~07:35 UTC — early.** US daytime news on 25 Nov is not in the paper, and the footer says so honestly | Breadth from the later part of the day is missing |
| **Secondary panels carry no illustration; the numbers strip has 5 statistics** (the playbook pattern is 6) | Visual craft trails the ni24 winners by one element each |
| **The field is cloned.** Hundreds of entries now copy the same winner template, so craft alone no longer separates entries the way it did in ni24 | Small date or craft slips decide paid vs unpaid |

None of these is a blocker, and none justifies opening a new fix
round before the 19:00 WIB cutoff: swapping a clean-dated Korean
story for a non-Korean story with a shaky date would reopen the
date blocker that took five rounds to close. The trade-off is
deliberate and recorded — date cleanliness first, regional balance
second.

## Playbook rules this entry follows

- Target top 10, floor rank 25, and treat anything outside the
  top 50 as $0; never inflate an estimate by comparing only
  against the top 3.
- Every story must be first reported on 25 Nov 2026 from its
  primary outlet — the aggregator's re-post stamp does not count,
  and a live-blog page does not prove its contents are from today.
- The region bar must reconcile exactly to 34, and the numbers
  strip must only cite figures from stories still on the page.
- The DATE CHECK footer must name what was excluded and when the
  paper was compiled, in plain words.
- No submit without a Goldfish verdict of LAYAK SUBMIT and a
  byte-identical double run of main.py; the entry is not reported
  ready until the top-10 analysis and Goldfish's verdict are both
  on record.
