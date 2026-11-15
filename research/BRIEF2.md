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
  "kind": "one of: Tiny trick, huge effect | You’re not in control | Your senses lie | Hidden destiny | Vices are good for you | Everyday killers | The miracle pill | Backwards medicine | Mind over matter | Impossible senses | Spooky correlations | One lever moves society | Justice isn’t blind | Rewrite physics | Life finds a way  (you may coin ONE new kind if nothing fits several of your claims; keep it short and deadpan like these)",
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


## Already on the site — do NOT repeat these
- Did you know… countries that eat more chocolate win more Nobel Prizes?
- Did you know… coffee drinking was once linked to a doubled risk of pancreatic cancer?
- Did you know… taking vitamin E supplements cut women's heart disease risk by a third?
- Did you know… a compound in red wine helps mice live longer?
- Did you know… eating breakfast is linked to a healthier weight?
- Did you know… sitting for long periods raises the risk of early death?
- Did you know… coffee drinkers die less often, even from accidents?
- Did you know… every half egg per day was tied to higher mortality?
- Did you know… a Mediterranean diet study was retracted and republished, and still held?
- Did you know… neutrinos travelled faster than the speed of light?
- Did you know… telescope data at the South Pole revealed gravitational waves from the Big Bang?
- Did you know… a jar of palladium and heavy water produced nuclear fusion at room temperature?
- Did you know… a bacterium in Mono Lake builds its DNA from arsenic?
- Did you know… a dead salmon in a brain scanner responded to photographs of human emotions?
- Did you know… one gene variant decides whether stress makes you depressed?
- Did you know… scientists discovered a stable polymer form of water?
- Did you know… a new kind of invisible radiation makes sparks and screens glow brighter?
- Did you know… mice inherit a fear of cherry blossom smell from their fathers?
- Did you know… pea plants learn to link a fan breeze with light?
- Did you know… your brain decides to move before you know you have decided?
- Did you know… microscopic animals can survive in the vacuum of outer space?
- Did you know… distant particles stay correlated in ways no hidden variable can explain?
- Did you know… smokers are less likely to get Parkinson’s disease?
- Did you know… overweight people die less often than people of normal weight?
- Did you know… low-birth-weight babies of smokers survive better than those of nonsmokers?
- Did you know… hormone therapy protects women from heart disease?
- Did you know… beta-carotene pills protect smokers from lung cancer?
- Did you know… light drinkers outlive people who never drink?
- Did you know… strangers' prayers helped heart patients leave hospital healthier?
- Did you know… praying in 2000 shortened hospital stays from the 1990s?
- Did you know… placebos work even when patients are told they are placebos?
- Did you know… transplanting donor feces cures recurrent C. difficile better than antibiotics?
- Did you know… stomach ulcers are caused by bacteria, not stress?
- Did you know… feeding infants peanuts prevents peanut allergy?
- Did you know… people respond to stimuli that have not yet been shown?
- Did you know… volunteers can receive images telepathically while sensory-deprived?
- Did you know… human intention can bias random number generators?
- Did you know… random number generators worldwide drift during major world events?
- Did you know… a dog can sense when its owner starts heading home?
- Did you know… government-funded psychics described hidden targets better than chance?
- Did you know… the body reacts a few seconds before a random event?
- Did you know… astrologers can match a birth chart to a personality profile?
- Did you know… the full moon drives up births, crime and psychiatric trouble?
- Did you know… dog bites surge when the moon is full?
- Did you know… one identical personality sketch fits every student, rated 4.26 of 5?
- Did you know… healthy people can be made to feel outside their bodies?
- Did you know… standing like Wonder Woman for two minutes raises your testosterone?
- Did you know… resisting a plate of cookies leaves you with less willpower afterward?
- Did you know… reading words about old age makes you walk more slowly?
- Did you know… holding a pen in your teeth makes cartoons funnier?
- Did you know… hurricanes with feminine names kill more people than masculine-named ones?
- Did you know… people named Dennis are disproportionately likely to become dentists?
- Did you know… a four-year-old's wait for a marshmallow predicts later achievement?
- Did you know… basketball's hot hand is a statistical illusion that fools fans?
- Did you know… students role-playing prison guards spontaneously turned cruel?
- Did you know… listening to Mozart makes you smarter?
- Did you know… a random number shifts your guess of Chicago's population?
- Did you know… most ordinary people will give painful shocks when an experimenter insists?
- Did you know… national debt above 90% of GDP sharply cuts economic growth?
- Did you know… legalizing abortion in the 1970s cut crime two decades later?
- Did you know… parole judges grant far fewer requests just before lunch?
- Did you know… storks deliver babies, according to a statistical test?
- Did you know… offering shoppers more jam flavors made them buy less?
- Did you know… factory workers produced more simply because they were being watched?
- Did you know… Houston police were no more likely to shoot Black suspects than white ones?
- Did you know… a short online lesson on brain plasticity raises student grades?
- Did you know… raising the minimum wage did not cost fast-food jobs?
- Did you know… identical résumés get more callbacks with white-sounding names?
- Did you know… more income stops making people happier beyond $75,000?
