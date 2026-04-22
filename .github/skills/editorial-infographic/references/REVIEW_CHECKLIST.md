# REVIEW_CHECKLIST — Ship Criteria

Run this **before** declaring shipped. Failures route back to Phase 2 (panel re-review of the failing region), not patch-in-isolation.

## Source fidelity (Rule 1)

- [ ] Every section name traces to a verbatim phrase or close paraphrase from the source. Cite line numbers in working notes.
- [ ] Every criterion / bullet / definition is **verbatim** or a documented compression. No invented sentences.
- [ ] Role names, team names, framework names match the source taxonomy exactly. (E.g., "Platform Team" vs. "Platform Engineering Team" — pick the one the source uses.)
- [ ] The leave-with quote is verbatim from the source **and** unique to this topic. (Test: would this same quote close *any* infographic? If yes, replace.)
- [ ] No invented vocabulary slipped in via tagline drift ("X succeeded and that's why Y fails" — only if source actually said this).

## Visual discipline (Rule 3)

- [ ] Dark INK background appears in **exactly two places**: masthead, CTA footer. Zero dark slabs in body.
- [ ] All section numbers (01/02/03/...) are INK. No rainbow.
- [ ] Each accent color (RED / GREEN / OCHRE) maps to **content meaning**, not decoration. Verbalize the meaning per use.
- [ ] No two consecutive sections use the same layout pattern (see [LAYOUT_PATTERNS.md](LAYOUT_PATTERNS.md)).
- [ ] Render scale is `SCALE = 2`. Native output is ~2400 × ~5500 px.
- [ ] No PIL primitive called directly in body code; only via helpers (`text`, `hline`, `rect`, etc.).

## Information architecture

- [ ] 3 to 5 sections (4 is sweet spot).
- [ ] Section names are **action verbs** (ASSESS / DEFINE / ROLL OUT / MEASURE / SHIP / AUDIT). No nouns.
- [ ] Each section answers exactly one question.
- [ ] Each section has a one-line **italic tagline** under the section header (the lede). Reads as a complete sentence.
- [ ] Decision-driving sections (matrices, phase bars) end with an explicit verdict / action strip — not just data.

## Conversion (the CTA test)

- [ ] CTA footer is the **loudest element** at a 5-foot view test (squint at the page; the URL should still be readable).
- [ ] CTA footer has all of: ochre kicker · book title in display serif · author byline · format affordance · underlined URL.
- [ ] No "footer under the footer" — author name lives **inside** the dark band, immediately under the book title (cover-style).
- [ ] Masthead's bottom-right tells the bailing reader *where to find this thing* (e.g., "FREE ONLINE · PDF · EPUB"). Not a vanity subtitle.

## Typography

- [ ] Page title in **serif display** (large).
- [ ] Section verbs in **sans bold**.
- [ ] Section numbers + kickers + masthead + URL in **mono**.
- [ ] Taglines + leave-with quote + author byline in **serif italic**.
- [ ] No accidental font fallbacks (e.g., Helvetica showing where Inter should be — check render output, not just code).

## Layout sanity

- [ ] Nothing overlaps. Nothing falls off the page.
- [ ] Margins consistent (`ML = MR = 80`).
- [ ] Long text is wrapped via `wrap()`, not hardcoded line breaks (or hardcoded only with explicit reason).
- [ ] Multi-column rows are aligned to the same x-coordinates as parallel rows below (visual symmetry).

## Final eye test

- [ ] Read the page top-to-bottom out loud. Each section transitions cleanly. No jarring tone shifts.
- [ ] A bailing reader who only sees the masthead + first section gets a complete brand impression (you exist, this is a real book/piece, here's where to find it).
- [ ] The leave-with quote actually feels like a leaving thought — distilled, memorable, topic-specific. If it sounds like LinkedIn-positivity ("believe in your team!"), kill it.

---

## Distribution after ship

Once the PNG ships, leverage it across the growth engine. Tier-1 actions (do all three within 24h):

1. **Set as social/OG card for the source chapter page.** One line of front-matter (`image: /assets/<slug>.png`). Every share of that chapter URL — anywhere, by anyone, forever — now uses this infographic as the preview. Compounding distribution from a 30-second change.
2. **Pin to LinkedIn Featured.** A single LinkedIn post decays in 48h; a Featured pin is permanent and converts profile visitors at a steady rate.
3. **Add as a delivered asset in the welcome email sequence** (~Day 10). Subject: "The 1-pager from Chapter X." Reactivates non-openers and demonstrates quality bar.

Tier-2 (within a week):

4. Embed at the top of the chapter page itself as "Chapter Summary."
5. Embed on the email-gate page (`download.qmd`) above the form — show value, then ask.
6. Cross-post to dev.to / Hashnode as an article.

Tier-3 (strategic):

7. Build a **series**. Same brand chrome, same pipeline, one infographic per chapter. At 4–5 in the same style, you have a recognizable visual brand → talk invitations, podcast asks, citation gravity.
