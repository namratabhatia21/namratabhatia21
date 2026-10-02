"""Generates the profile README panels. Usage: python3 assets/generate.py <theme> <outdir>"""
import base64, math, os, sys
FD = os.environ.get('FD', 'node_modules/@fontsource')  # npm i @fontsource/comfortaa @fontsource/fira-code
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
FONTS = {
 'c7': f"@font-face{{font-family:'Comfortaa';font-weight:700;src:url(data:font/woff2;base64,{b64(FD+'/comfortaa/files/comfortaa-latin-700-normal.woff2')}) format('woff2')}}",
 'c4': f"@font-face{{font-family:'Comfortaa';font-weight:400;src:url(data:font/woff2;base64,{b64(FD+'/comfortaa/files/comfortaa-latin-400-normal.woff2')}) format('woff2')}}",
 'f5': f"@font-face{{font-family:'Fira Code';font-weight:500;src:url(data:font/woff2;base64,{b64(FD+'/fira-code/files/fira-code-latin-500-normal.woff2')}) format('woff2')}}",
}
THEMES = {
 # a = main accent, b = second accent, c = third accent, tint = light accent, sub = small mono text
 'crimson': dict(a='#ff3b3b', b='#ff8a65', c='#ff5c8a', tint='#ffd0cc', sub='#ff8a80', txt='#e8e3e3', white='#fff5f5',
                 bg1='#151515', bg2='#221416', card1='#2a1a1c', card2='#191214', m1='#ff6b5b', m2='#c62828', m3='#8e1b1b', mouth='#5c0f0f', pupil='#1a0a0a'),
 'ocean':   dict(a='#22d3ee', b='#34d399', c='#60a5fa', tint='#cffafe', sub='#67e8f9', txt='#dbe7f0', white='#f0fbff',
                 bg1='#0a1520', bg2='#0f2233', card1='#13293d', card2='#0b1824', m1='#2dd4bf', m2='#0e7490', m3='#0b5566', mouth='#063341', pupil='#04141c'),
 'gold':    dict(a='#fbbf24', b='#fb923c', c='#facc15', tint='#fde68a', sub='#fcd34d', txt='#ece6da', white='#fffaf0',
                 bg1='#121110', bg2='#1d1a14', card1='#29241a', card2='#17140f', m1='#fcd34d', m2='#d97706', m3='#92400e', mouth='#5a2a06', pupil='#1a1206'),
 'redblue': dict(a='#ff3b5c', b='#58a6ff', c='#a371f7', tint='#ffd1da', sub='#ff8fa3', txt='#e6edf3', white='#ffffff',
                 bg1='#0d1117', bg2='#161b22', card1='#1c2230', card2='#11161f', m1='#ff5c7a', m2='#c9184a', m3='#8b1034', mouth='#4a0a1c', pupil='#0d1117'),
}
T = THEMES[sys.argv[1] if len(sys.argv) > 1 else 'crimson']
OUT = sys.argv[2] if len(sys.argv) > 2 else 'assets'
A, B, C, TINT, SUB, TXT, WH = T['a'], T['b'], T['c'], T['tint'], T['sub'], T['txt'], T['white']

def svg(w, h, body, fonts=('c7','c4'), css=''):
    ff = ''.join(FONTS[f] for f in fonts)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
<style>{ff}
.t{{font-family:'Comfortaa',Verdana,sans-serif}} .m{{font-family:'Fira Code',Consolas,monospace}}
.pulse{{animation:pulse 3s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.55}}}}
.spin{{transform-box:fill-box;transform-origin:center;animation:spin 14s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.float{{animation:float 4s ease-in-out infinite}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-6px)}}}}
.tw{{transform-box:fill-box;transform-origin:center;animation:tw 2.4s ease-in-out infinite}}
@keyframes tw{{0%,100%{{opacity:.2;transform:scale(.6)}}50%{{opacity:1;transform:scale(1)}}}}
{css}</style>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glow2" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{T['bg1']}"/><stop offset="1" stop-color="{T['bg2']}"/></linearGradient>
<radialGradient id="rg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{A}" stop-opacity=".14"/><stop offset="1" stop-color="{A}" stop-opacity="0"/></radialGradient>
<linearGradient id="mg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{T['m1']}"/><stop offset="1" stop-color="{T['m2']}"/></linearGradient>
<linearGradient id="pf0" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{T['card1']}"/><stop offset="1" stop-color="{T['card2']}"/></linearGradient>
<linearGradient id="pf1" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{T['card1']}"/><stop offset="1" stop-color="{T['card2']}"/></linearGradient>
</defs>
{body}
</svg>'''

def panel(w, h, r=14):
    return f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{r}" fill="url(#bg)" stroke="{A}" stroke-opacity=".4" stroke-width="1.5"/>'

def star(x, y, s, c, d):
    return f'<path class="tw" style="animation-delay:{d}s" d="M{x} {y-s} Q{x} {y} {x+s} {y} Q{x} {y} {x} {y+s} Q{x} {y} {x-s} {y} Q{x} {y} {x} {y-s}Z" fill="{c}"/>'

CURVES = [((0.42,0),(0.43,0.08),(0.40,0.14)), ((0.35,0.24),(0.42,0.36),(0.50,0.36)),
          ((0.58,0.36),(0.65,0.24),(0.60,0.14)), ((0.57,0.08),(0.58,0),(0.64,0))]
def edge(x0,y0,x1,y1,s,depth):
    """Jigsaw edge from (x0,y0) to (x1,y1). Clockwise traversal: s=+1 blank (inward), -1 tab (outward), 0 flat."""
    if s == 0: return f'L{x1:.1f} {y1:.1f}'
    dx,dy = x1-x0, y1-y0; L = math.hypot(dx,dy); nx,ny = -dy/L, dx/L
    P = lambda u,v: (x0+u*dx+v*depth*s*nx, y0+u*dy+v*depth*s*ny)
    return ' '.join(['L%.1f %.1f' % P(0.36,0)] + ['C' + ' '.join('%.1f %.1f' % P(*p) for p in c) for c in CURVES] + [f'L{x1:.1f} {y1:.1f}'])
def piece(x,y,w,h,top,right,bottom,left,depth):
    return (f'M{x} {y} ' + edge(x,y,x+w,y,top,depth) + ' ' + edge(x+w,y,x+w,y+h,right,depth) + ' ' +
            edge(x+w,y+h,x,y+h,bottom,depth) + ' ' + edge(x,y+h,x,y,left,depth) + 'Z')
def mini(x, y, sz, c, d=0, cls='spin'):
    return f'<path class="{cls}" style="animation-delay:{d}s" d="{piece(x,y,sz,sz,-1,-1,1,0,sz*0.9)}" fill="none" stroke="{c}" stroke-width="1.6" filter="url(#glow)" opacity=".75"/>'

def header():
    W,H = 830,130
    body = panel(W,H) + f'''
<ellipse cx="415" cy="62" rx="280" ry="55" fill="url(#rg)"/>
{mini(70,40,24,A,0)}{mini(755,78,28,B,-5)}{mini(140,86,15,C,-9)}{mini(690,28,16,A,-3)}
{star(230,30,5,TINT,0)}{star(600,108,5,TINT,1.1)}{star(560,24,4,B,.6)}{star(270,110,4,A,1.7)}
<text x="415" y="74" text-anchor="middle" class="t flick" font-weight="700" font-size="52" fill="{WH}" stroke="{A}" stroke-width="1.4" filter="url(#glow2)">Namrata</text>
<text x="415" y="106" text-anchor="middle" class="m" font-weight="500" font-size="14" fill="{SUB}" letter-spacing="1">problem solver · puzzle lover · builder</text>'''
    css = '.flick{animation:flick 5s linear infinite}@keyframes flick{0%,18%,22%,25%,53%,57%,100%{opacity:1}20%,24%,55%{opacity:.4}}'
    return svg(W,H,body,('c7','f5'),css)

def mascot(cx, cy, s):
    body = piece(-85,-85,170,170,-1,-1,0,1,78)
    L = TINT
    return f'''<g transform="translate({cx} {cy}) scale({s})"><g class="float">
<ellipse cx="0" cy="118" rx="95" ry="12" fill="{A}" opacity=".2"/>
<ellipse cx="-38" cy="100" rx="24" ry="12" fill="{T['m3']}" stroke="{L}" stroke-width="2"/>
<ellipse cx="38" cy="100" rx="24" ry="12" fill="{T['m3']}" stroke="{L}" stroke-width="2"/>
<path d="M-82 15 Q-120 30 -128 -5" fill="none" stroke="{L}" stroke-width="9" stroke-linecap="round"/>
<circle cx="-129" cy="-10" r="11" fill="{T['m1']}" stroke="{L}" stroke-width="2"/>
<g class="wave"><path d="M82 20 Q125 10 135 -35" fill="none" stroke="{L}" stroke-width="9" stroke-linecap="round"/>
<circle cx="136" cy="-42" r="12" fill="{T['m1']}" stroke="{L}" stroke-width="2"/></g>
<path d="{body}" fill="url(#mg)" stroke="{L}" stroke-width="3" filter="url(#glow)"/>
<ellipse cx="-50" cy="25" rx="14" ry="8" fill="{WH}" opacity=".25"/><ellipse cx="50" cy="25" rx="14" ry="8" fill="{WH}" opacity=".25"/>
<g class="blink">
<ellipse cx="-30" cy="-8" rx="20" ry="24" fill="#fff"/><ellipse cx="30" cy="-8" rx="20" ry="24" fill="#fff"/>
<circle cx="-26" cy="-4" r="11" fill="{T['pupil']}"/><circle cx="34" cy="-4" r="11" fill="{T['pupil']}"/>
<circle cx="-22" cy="-9" r="4" fill="#fff"/><circle cx="38" cy="-9" r="4" fill="#fff"/></g>
<path d="M-20 35 Q0 55 20 35" fill="{T['mouth']}" stroke="{T['pupil']}" stroke-width="4" stroke-linecap="round"/>
</g></g>'''
MASCOT_CSS = ('.blink{transform-box:fill-box;transform-origin:center;animation:blink 4s infinite}'
 '@keyframes blink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(.1)}}'
 '.wave{transform-box:fill-box;transform-origin:0% 100%;animation:wave 1.6s ease-in-out infinite}'
 '@keyframes wave{0%,100%{transform:rotate(0)}50%{transform:rotate(-18deg)}}')

def hero(lines):
    W,H = 830,210
    tl = ''.join(f'<text x="230" y="{76+i*27}" text-anchor="middle" class="t" font-weight="700" font-size="19" fill="{WH}">{l}</text>' for i,l in enumerate(lines))
    bubble = 'M80 36 h300 a20 20 0 0 1 20 20 v30 l32 14 -32 6 v14 a20 20 0 0 1 -20 20 h-300 a20 20 0 0 1 -20 -20 v-64 a20 20 0 0 1 20 -20z'
    body = panel(W,H) + f'''
<ellipse cx="580" cy="105" rx="170" ry="100" fill="url(#rg)"/>
{star(440,40,6,TINT,0)}{star(740,60,5,B,.8)}{star(470,180,4,A,1.4)}{star(70,180,5,TINT,.4)}{star(760,175,6,A,1.9)}
<path d="{bubble}" fill="{T['card1']}" stroke="{A}" stroke-width="2" filter="url(#glow)" class="pulse"/>
{tl}
<text x="230" y="182" text-anchor="middle" class="m" font-weight="500" font-size="12" fill="{SUB}">- Puzzle, Namrata's sidekick</text>
{mascot(590,100,0.6)}'''
    return svg(W,H,body,('c7','f5'),MASCOT_CSS)

ICONS = {
 'book': lambda c: f'<path d="M-24 -14 q12 -6 24 0 q12 -6 24 0 v30 q-12 -6 -24 0 q-12 -6 -24 0z M0 -14 v30" fill="none" stroke="{c}" stroke-width="3" stroke-linejoin="round"/>',
 'bulb': lambda c: f'<path d="M-9 12 q-15 -9 -15 -24 a24 24 0 0 1 48 0 q0 15 -15 24z M-8 18 h16 M-5 24 h10" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 -2)"/>',
 'git': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3"><circle cx="-12" cy="-16" r="5"/><circle cx="-12" cy="18" r="5"/><circle cx="14" cy="-4" r="5"/><path d="M-12 -11 v24 M14 1 q0 10 -22 14"/></g>',
 'sys': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3"><rect x="-26" y="-22" width="18" height="14" rx="3"/><rect x="8" y="-22" width="18" height="14" rx="3"/><rect x="-9" y="10" width="18" height="14" rx="3"/><path d="M-17 -8 v8 h34 v-8 M0 0 v10"/></g>',
 'tree': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3"><circle cx="0" cy="-18" r="6"/><circle cx="-16" cy="4" r="6"/><circle cx="16" cy="4" r="6"/><circle cx="-24" cy="24" r="4"/><circle cx="-8" cy="24" r="4"/><path d="M-4 -13 l-8 12 M4 -13 l8 12 M-19 9 l-3 11 M-13 9 l3 11"/></g>',
 'bars': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"><path d="M-26 24 h52"/><rect x="-20" y="4" width="9" height="20" rx="2"/><rect x="-5" y="-12" width="9" height="36" rx="2"/><rect x="10" y="-4" width="9" height="28" rx="2"/><path d="M-22 -6 l14 -12 l14 6 l16 -12" /></g>',
}
PIECES = [('Learning','always chasing','the next piece','book',A),
          ('Creating','turning ideas','into real things','bulb',C),
          ('Open Source','building the big','picture together','git',B),
          ('System Design','how the big','pieces connect','sys',B),
          ('Algorithms','the cleverest way','to make it fit','tree',A),
          ('Data','the picture hidden','in the noise','bars',C)]
def board():
    W,H = 830,430
    cw,ch,ox,oy = 200,165,115,68
    vt = {(0,0):1,(0,1):0,(1,0):0,(1,1):1}
    ht = {0:1,1:0,2:1}
    out = ''
    for i,(t,a,b,ic,c) in enumerate(PIECES):
        r,cc = divmod(i,3); x,y = ox+cc*cw, oy+r*ch
        top = 0 if r==0 else (1 if ht[cc] else -1)
        bottom = 0 if r==1 else (-1 if ht[cc] else 1)
        left = 0 if cc==0 else (1 if vt[(r,cc-1)] else -1)
        right = 0 if cc==2 else (-1 if vt[(r,cc)] else 1)
        d = piece(x,y,cw,ch,top,right,bottom,left,66)
        mx,my = x+cw/2, y+ch/2 + (9 if top==1 else 0) - (9 if bottom==1 else 0)
        out += f'''<g class="p{i}">
<path d="{d}" fill="url(#pf{i%2})" stroke="{c}" stroke-width="2" stroke-linejoin="round" filter="url(#glow)"/>
<g transform="translate({mx} {my-30}) scale(.75)" filter="url(#glow)">{ICONS[ic](c)}</g>
<text x="{mx}" y="{my+14}" text-anchor="middle" class="t" font-weight="700" font-size="17" fill="{WH}">{t}</text>
<text x="{mx}" y="{my+34}" text-anchor="middle" class="t" font-weight="400" font-size="12" fill="{TXT}">{a}</text>
<text x="{mx}" y="{my+50}" text-anchor="middle" class="t" font-weight="400" font-size="12" fill="{TXT}">{b}</text>
</g>'''
    css = ''.join(f'.p{i}{{transform-box:view-box;animation:in{i} 1.1s cubic-bezier(.2,.9,.25,1.15) {0.25+i*0.18:.2f}s both}}'
                  f'@keyframes in{i}{{0%{{opacity:0;transform:translate({sx}px,{sy}px) rotate({rot}deg)}}100%{{opacity:1;transform:none}}}}'
                  for i,(sx,sy,rot) in enumerate([(-70,-40,-14),(0,-70,9),(70,-40,-8),(-70,40,10),(0,70,-12),(70,40,13)]))
    body = panel(W,H) + f'''
<ellipse cx="415" cy="230" rx="330" ry="190" fill="url(#rg)"/>
{star(40,36,6,TINT,0)}{star(795,50,5,B,.9)}{star(40,400,4,A,1.5)}{star(795,400,6,TINT,.5)}
<text x="415" y="44" text-anchor="middle" class="t" font-weight="700" font-size="21" fill="{WH}" filter="url(#glow)">the pieces that make me</text>
{out}'''
    return svg(W,H,body,('c7','c4'),css)

def card(title, lines, btn, icon, c):
    W,H = 405,160
    tl = ''.join(f'<text x="24" y="{82+i*20}" class="t" font-weight="400" font-size="13" fill="{TXT}">{l}</text>' for i,l in enumerate(lines))
    bw = len(btn)*9+26
    bt = (f'<g class="pulse"><rect x="{W-24-bw}" y="116" width="{bw}" height="28" rx="8" fill="none" stroke="{c}" stroke-width="1.6" filter="url(#glow)"/>'
          f'<text x="{W-24-bw/2}" y="135" text-anchor="middle" class="m" font-weight="500" font-size="13" fill="{WH}">{btn}</text></g>') if btn else ''
    body = panel(W,H) + f'''
<ellipse cx="330" cy="55" rx="100" ry="60" fill="url(#rg)"/>
<text x="24" y="48" class="t" font-weight="700" font-size="22" fill="{WH}" filter="url(#glow)">{title}</text>
<g transform="translate(360 44) scale(.7)" filter="url(#glow)">{ICONS[icon](c)}</g>
{tl}
{bt}'''
    return svg(W,H,body,('c7','c4','f5'))

def riddle():
    W,H = 830,140
    body = panel(W,H) + f'''
<ellipse cx="415" cy="70" rx="260" ry="60" fill="url(#rg)"/>
{star(60,34,5,TINT,0)}{star(770,110,5,B,1)}
{mini(730,40,28,C,0)}
<text x="415" y="32" text-anchor="middle" class="m" font-weight="500" font-size="12" fill="{SUB}" letter-spacing="2">PUZZLE'S RIDDLE</text>
<text x="415" y="60" text-anchor="middle" class="t" font-weight="700" font-size="16" fill="{WH}">I have keys but open no locks.</text>
<text x="415" y="83" text-anchor="middle" class="t" font-weight="700" font-size="16" fill="{WH}">I have space but no room.</text>
<text x="415" y="106" text-anchor="middle" class="t" font-weight="700" font-size="16" fill="{WH}">You can enter, but you can't go inside.</text>
<text x="415" y="129" text-anchor="middle" class="t" font-weight="700" font-size="16" fill="{A}" filter="url(#glow)">What am I?</text>'''
    return svg(W,H,body,('c7','f5'))

def footer():
    W,H = 830,86
    body = panel(W,H) + f'''
<ellipse cx="415" cy="43" rx="240" ry="40" fill="url(#rg)"/>
{star(120,28,5,TINT,0)}{star(720,60,5,B,.7)}{star(660,22,4,A,1.3)}
{mini(80,30,24,A,0)}{mini(725,24,22,C,-6)}
<text x="415" y="40" text-anchor="middle" class="t" font-weight="700" font-size="19" fill="{WH}" filter="url(#glow)">thanks for stopping by!</text>
<text x="415" y="64" text-anchor="middle" class="m" font-weight="500" font-size="12" fill="{SUB}">building it one piece at a time</text>'''
    return svg(W,H,body,('c7','f5'))

files = {
 'header.svg': header(),
 'hero-dark.svg': hero(['Nice, dark mode!','A true puzzle','solver, I see. hehe']),
 'hero-light.svg': hero(['Light mode, huh?','Bold move.','Puzzle approves!']),
 'pieces.svg': board(),
 'story.svg': card('My story',['Most of my code shipped at work,','in private repos. Now I am','building in public, piece by piece.'],'','sys',A),
 'agentic.svg': card('Agentic',['My experiments with AI agents.','Small pieces that think,','plan and act together.'],'Explore','bulb',C),
 'riddle.svg': riddle(),
 'footer.svg': footer(),
}
os.makedirs(OUT, exist_ok=True)
for n,s in files.items():
    open(os.path.join(OUT,n),'w').write(s)
