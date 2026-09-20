# ATS Rules

Applicant Tracking Systems (ATS) parse resumes into structured fields before
a human ever sees them. A resume that looks beautiful in Word can come out
of an ATS as gibberish. This file is the checklist the skill runs during
**step 2 (formatting)** and **step 3 (ATS)** of the workflow.

The rules are conservative on purpose. The cost of a "stricter than needed"
rule is mild ugliness; the cost of a parsing failure is silent rejection.

---

## Hard rules — break parsing if violated

1. **No tables or multi-column layouts for content.** ATS parsers read
   top-to-bottom, left-to-right. A two-column layout interleaves text from
   both columns and corrupts every field.
2. **No text boxes.** Most parsers drop their contents entirely.
3. **No images of text.** A skills badge image is invisible to the ATS.
4. **No icons replacing words.** "📧 user@example.com" → many parsers see
   garbage where the email should be. Use the literal word `Email:`.
5. **Contact info in the body, not the header/footer.** A meaningful
   percentage of parsers ignore header/footer regions.
6. **Standard section headings only.** Use `Experience`, `Work Experience`,
   `Education`, `Skills`, `Projects`, `Publications`. Avoid creative names
   like "My Journey" or "What I've Built" — the ATS won't categorize them.
7. **One column for the main body.** A sidebar is a two-column layout in
   disguise.

## Soft rules — degrade parsing quality

8. **Dates in a single consistent format.** Prefer `May 2023 — Aug 2024`.
   Avoid `5/23 - 8/24`, `Spring '23`, or season-only ranges.
9. **Standard bullet glyphs.** Use `•` or `-`. Avoid `→`, `✓`, `★`, emoji.
10. **No ligatures or fancy quotes** in skills or job titles. `fi`, `fl`,
    smart quotes, and em-dashes inside ATS fields can split tokens.
11. **No vertical text, rotated text, or watermarks.**
12. **PDF only when the posting accepts it.** Many ATS still parse `.docx`
    more reliably. If the posting says "PDF accepted", PDF is fine.
13. **Embed fonts** if exporting PDF — and prefer common ones (Calibri,
    Arial, Helvetica, Times, Georgia, Garamond). Decorative fonts can break
    text extraction.
14. **No password protection.** Some ATS will silently fail; some humans
    will fail more loudly.

## Content rules — about what's inside the parseable text

15. **Job titles that exist.** Match the title to LinkedIn and to titles a
    recruiter would search. "Software Engineer" beats "Code Wizard".
16. **Spell out acronyms on first use** when the acronym is industry-internal
    or company-specific. Universal ones (`AWS`, `API`, `SQL`) are fine bare.
17. **Skills written as searchable terms.** The exact noun the recruiter
    types into the ATS search bar. "React" not "ReactJS framework usage".
18. **Don't keyword-stuff.** White text, 1pt-font keyword blocks, hidden
    skill lists — ATS systems flag this and recruiters reject it.
19. **File name**: `FirstLast_Resume.pdf` or `FirstLast_Resume_Role.docx`.
    No spaces, no version numbers (`v3_final_FINAL`).

---

## Risk ranking (use in the report)

When listing findings under step 3, classify each as:

- **High** — parsing is likely to fail. Rules 1–7.
- **Medium** — parsing degrades or recruiter friction. Rules 8–14, 17.
- **Low** — cosmetic, but worth fixing. Rules 15, 16, 18, 19.

A resume with any **High** finding is not ATS-ready, regardless of content
quality. Fix the High items before scoring (step 4).

---

## Common false alarms

These look like ATS problems but aren't:

- **Two-line bullets** are fine.
- **A clean horizontal rule** between sections is fine.
- **Bold within a bullet** is fine and helps human scanning.
- **Em-dashes between words** (`Senior Engineer — Acme`) are fine; only
  em-dashes *inside dates* cause parsing issues.
- **A skills section with subcategories** (Languages: …, Tools: …) is fine
  as long as it's not in a table.
