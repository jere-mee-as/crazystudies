# Brief: "Studies that lead you down the wrong path"

A website listing REAL, published studies whose headline findings sound outrageous ("Did you know… power posing raises testosterone?"). Each is shown deadpan, with a short verdict saying what became of it. Tone: deadpan, straight-faced. No snark, no exclamation marks.

## Scope: include only these three kinds
- **dead**: honest research (no fraud) that failed to replicate or was overturned by better evidence.
- **shaky**: contested; replications mixed, or a serious critique is unresolved.
- **misread**: the data are real, but the obvious causal reading is wrong (confounding, reverse causation, selection, collider bias, regression to the mean).
- **standing**: weird findings that have HELD UP, which is a needed contrast.

EXCLUDE fraud and fabrication cases (Stapel, Wakefield, Gino, Hwang, Schön, LaCour, Wansink, etc.) and deliberate hoaxes (e.g. Bohannon's chocolate study, Sokal).

## Hard rules on accuracy
- Every study must be real. Use WebSearch/WebFetch to confirm author, year, and venue for EVERY citation before you include it. If you can't confirm it, drop it.
- The verdict must reflect the current state of evidence (replications, meta-analyses, retractions-for-error, corrections). Cite nothing you have not checked.
- Don't overclaim deadness. If it's contested, say "shaky".

## Output
Write a JSON file (path given below) holding a list of 9–13 claims:

```json
[{
  "field": "<your field>",
  "trap": "one of: Small samples & p-hacking | Confounding | Reverse causation | Selection & survivorship | Regression to the mean | Many comparisons | Measurement & proxies | Publication bias | Analysis error | None, it held up",
  "verdict": "dead | shaky | misread | standing",
  "claim": "Did you know… <the outrageous claim, as the study's headline would put it, ≤14 words>?",
  "studies": [{
     "cite": "Surname et al. (YEAR), Journal",
     "finding": "One deadpan sentence: what this study reported. ≤25 words.",
     "verdict": "Short verdict ≤14 words, e.g. 'Registered Replication Report, 23 labs: effect ≈ 0.'",
     "url": "a DOI or stable link you actually confirmed"
  }]
}]
```
1–3 studies per claim (the original, plus the replication or debunking when that is itself a study). Every study object needs all four fields. Write in your own words, with no quotes over 10 words. Aim for variety and surprise. At least 2 claims should be "standing".

When done, reply with just the file path and the number of claims.
