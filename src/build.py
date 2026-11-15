import os, sys, json, collections
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, 'shell')); import shell

# the studies: research/*.json, one file per field, checked by hand
R = os.path.join(here, '..', 'research')
FIELDS = [('psychology', 'Psychology', 'ψ'), ('medicine', 'Medicine', '⚕'), ('food', 'Food & lifestyle', '⊚'),
          ('society', 'Economics & society', '¤'), ('paranormal', 'The paranormal', '☾'), ('hardsci', 'Physics, biology & brains', '⚛'),
          ('animals', 'Animals', '∾'), ('moneysports', 'Money & sports', '$'), ('space', 'Space & deep time', '✧')]
KINDS = [('Tiny trick, huge effect', '✦'), ('You’re not in control', '⌁'), ('Your senses lie', '◐'), ('Hidden destiny', '∴'),
         ('Vices are good for you', '♠'), ('Everyday killers', '⨯'), ('The miracle pill', '℞'), ('Backwards medicine', '⟲'),
         ('Mind over matter', '◎'), ('Impossible senses', '⊙'), ('Spooky correlations', '∿'), ('One lever moves society', '≡'),
         ('Justice isn’t blind', '⌖'), ('Rewrite physics', 'λ'), ('Life finds a way', '❦'), ('Beasts with brains', '∞'), ('Markets have moods', '≋'), ('Aliens among us', '✶')]
VERD = [('dead', 'Dead', '†'), ('shaky', 'Contested', '≈'), ('misread', 'Real data, wrong conclusion', '⇄'), ('standing', 'Held up, somehow', '✓')]

claims = []
for f, name, _ in FIELDS:
    for fn in (f + '.json', f + '_more.json'):
        p = os.path.join(R, fn)
        if not os.path.exists(p): continue
        for c in json.load(open(p, encoding='utf-8')):
            c['field'] = name; assert c['verdict'] in dict((v[0], 1) for v in VERD), (fn, c['verdict'])
            if c['kind'] not in dict(KINDS): print('NEW KIND', fn, c['kind']); KINDS.append((c['kind'], '·'))
            claims.append(c)

def topic(c):
    t = c['claim'].strip()
    for p in ('Did you know… ', 'Did you know... ', 'Did you know '): t = t[len(p):] if t.startswith(p) else t
    t = t.rstrip('?').strip(); said = t; t = t[0].upper() + t[1:]
    # the copy mark copies: mocking "DiD yOu KnOw...", the claim, the source, then what's wrong with it
    k = [{'q': s['cite'], 'f': s['finding'], 'm': s['verdict'], 'ml': 'Verdict',
          'c': f"DiD yOu KnOw... {said}?\n\n{s['cite']}" + (f"\n{s['url']}" if s.get('url') else '') + f"\n\n{s['verdict']}"} for s in c['studies']]
    return {'t': t, 'k': k, 'said': said}

def tree(l1, l1key, l2, l2key, name=lambda tp: tp['t']):
    """l1/l2 entries are (key, menu name, sigil, heading wording); name(topic) gives a topic's heading wording"""
    """l1 = [(key, name, sigil)], l2 likewise; each claim lands under its l1 and l2"""
    P = []
    for k1, n1, i1, s1 in l1:
        cs = [c for c in claims if c[l1key] == k1]
        if not cs: continue
        ts = [topic(c) for c in cs]
        for tp in ts: tp['s'] = name(tp); del tp['said']
        e = {'n': n1, 's': s1, 'i': i1, 'u': [], 't': ts}
        for k2, n2, i2, s2 in l2:
            ix = [j for j, c in enumerate(cs) if c[l2key] == k2]
            if ix: e['u'].append({'n': n2, 's': s2, 'i': i2, 't': ix})
        P.append(e)
    return P

# the field page reads as one sentence too: "So you read a psychology study, about a tiny trick with a huge effect, saying …?"
FSTUDY = {'Psychology': 'a psychology study', 'Medicine': 'a medical study', 'Food & lifestyle': 'a food & lifestyle study',
          'Economics & society': 'an economics & society study', 'The paranormal': 'a paranormal study', 'Physics, biology & brains': 'a hard-science study',
          'Animals': 'an animal study', 'Money & sports': 'a money & sports study', 'Space & deep time': 'a space & deep time study'}
KABOUT = {'Tiny trick, huge effect': 'about a tiny trick with a huge effect', 'You’re not in control': 'about how you’re not in control',
          'Your senses lie': 'about how your senses lie', 'Hidden destiny': 'about hidden destiny', 'Vices are good for you': 'about vices being good for you',
          'Everyday killers': 'about everyday killers', 'The miracle pill': 'about a miracle pill', 'Backwards medicine': 'about backwards medicine',
          'Mind over matter': 'about mind over matter', 'Impossible senses': 'about impossible senses', 'Spooky correlations': 'about a spooky correlation',
          'One lever moves society': 'about one lever that moves society', 'Justice isn’t blind': 'about how justice isn’t blind',
          'Rewrite physics': 'about rewriting physics', 'Life finds a way': 'about how life finds a way', 'Beasts with brains': 'about beasts with brains',
          'Markets have moods': 'about markets having moods', 'Aliens among us': 'about aliens among us'}
byfield = tree([(n, n, i, FSTUDY[n]) for _, n, i in FIELDS], 'field', [(k, k, i, KABOUT.get(k, 'about ' + k[0].lower() + k[1:])) for k, i in KINDS], 'kind',
               name=lambda tp: 'saying ' + tp['said'])
# the dead page reads as one sentence: "So you read a dead study, in psychology, saying …?"
DEADN = {'dead': 'dead study', 'shaky': 'contested study', 'misread': 'misread study', 'standing': 'study that held up'}
INF = {'Animals': 'about animals'}
bydead = tree([(k, n, i, DEADN[k]) for k, n, i in VERD], 'verdict',
              [(n, n, i, INF.get(n, 'in ' + n[0].lower() + n[1:])) for _, n, i in FIELDS], 'field', name=lambda tp: 'saying ' + tp['said'])

# third view: by issue. "Did you know you’re not in control, say the dead studies, Physics: Your brain decides…?"
KDYK = {'Tiny trick, huge effect': 'a tiny trick has a huge effect', 'You’re not in control': 'you’re not in control', 'Your senses lie': 'your senses lie',
        'Hidden destiny': 'your destiny is already written', 'Vices are good for you': 'vices are good for you', 'Everyday killers': 'everyday things are killing you',
        'The miracle pill': 'there’s a miracle pill', 'Backwards medicine': 'medicine runs backwards', 'Mind over matter': 'mind beats matter',
        'Impossible senses': 'impossible senses are real', 'Spooky correlations': 'spooky correlations are everywhere', 'One lever moves society': 'one lever moves society',
        'Justice isn’t blind': 'justice isn’t blind', 'Rewrite physics': 'physics needs rewriting', 'Life finds a way': 'life finds a way',
        'Beasts with brains': 'beasts have brains', 'Markets have moods': 'markets have moods', 'Aliens among us': 'aliens are among us'}
SHORT = {'Psychology': 'Psychology', 'Medicine': 'Medicine', 'Food & lifestyle': 'Food', 'Economics & society': 'Society', 'The paranormal': 'Paranormal',
         'Physics, biology & brains': 'Physics', 'Animals': 'Animals', 'Money & sports': 'Money', 'Space & deep time': 'Space'}
SAY = {'dead': 'say the dead studies', 'shaky': 'say the contested studies', 'misread': 'say the misread studies', 'standing': 'say the studies that held up'}
_fc = {}
for c in claims: _fc[id(c)] = c['field']
bykind = []
for k, i in KINDS:
    cs = [c for c in claims if c['kind'] == k]
    if not cs: continue
    ts = []
    for c in cs:
        tp = topic(c); tp['t'] = SHORT[c['field']] + ': ' + tp['t']; del tp['said']; ts.append(tp)
    e = {'n': k, 's': KDYK.get(k, k[0].lower() + k[1:]), 'i': i, 'u': [], 't': ts}
    for vk, vn, vi in VERD:
        ix = [j for j, c in enumerate(cs) if c['verdict'] == vk]
        if ix: e['u'].append({'n': vn, 's': SAY[vk], 'i': vi, 't': ix})
    bykind.append(e)

# a subtitle under the opening heading (outline and sentence), hidden once you pick something or search
SUB = ('<style>#outl .okids .okids{margin-left:40px}@media (max-width:760px){#outl .okids .okids{margin-left:30px}}.subt{color:var(--dim);font-size:17px;line-height:1.45;max-width:34em;margin:-14px 0 30px;font-style:italic}</style>'
       '<script>addEventListener("DOMContentLoaded",()=>{const t="Real, peer-reviewed studies with outrageous findings, and what became of them. '
       'Most did not survive. A few, unsettlingly, did.";["oh","sh"].forEach(id=>{const h=document.getElementById(id);if(!h)return;'
       'const s=document.createElement("div");s.className="subt";s.textContent=t;h.after(s);'
       'const f=()=>{s.style.display=h.textContent.trim().endsWith("…")?"":"none"};f();new MutationObserver(f).observe(h,{childList:true,subtree:true,characterData:true})})})</script>')

PAGES = [('index', 'by field'), ('dead', 'by how dead'), ('issues', 'by issue')]
def FOOT(me):
    return ('<style>.foot a{text-decoration:none;color:var(--dim)}.foot a:hover,.foot b{color:var(--ink);font-weight:400}</style><span class="foot">Sort ' +
            ' · '.join(f'<b>{n}</b>' if k == me else f'<a href="{k}.html">{n}</a>' for k, n in PAGES) + '</span>')
common = dict(key='cs', plurals={'study': 'studies', 'kind of crazy': 'kinds of crazy'}, theme='ink')
out = os.path.join(here, '..')
a = shell.build(byfield, os.path.join(out, 'index.html'), title='So you read…', lead='So you read', words=['field', 'kind of crazy', 'claim', 'study'], steps=['field', 'kind of crazy', 'claim', 'studies'],
    foot=FOOT('index') + SUB, **common)
b = shell.build(bydead, os.path.join(out, 'dead.html'), title='So you read a…', lead='So you read a', words=['verdict', 'field', 'claim', 'study'], steps=['verdict', 'field', 'claim', 'studies'],
    foot=FOOT('dead') + SUB, **common)
c3 = shell.build(bykind, os.path.join(out, 'issues.html'), title='Did you know…', lead='Did you know', words=['issue', 'verdict', 'claim', 'study'],
    steps=['issue', 'verdict', 'claim', 'studies'], foot=FOOT('issues') + SUB, **common)
print('built', a, b, c3)
print(len(claims), 'claims,', sum(len(c['studies']) for c in claims), 'studies')
print('by verdict', collections.Counter(c['verdict'] for c in claims))
print('by kind', collections.Counter(c['kind'] for c in claims))
print('dup claims', [x for x, n in collections.Counter(topic(c)['t'] for c in claims).items() if n > 1])
