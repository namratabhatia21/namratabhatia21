import base64, math, os
FD = 'node_modules/@fontsource'  # npm i @fontsource/comfortaa @fontsource/fira-code
OUT = 'assets'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
FONTS = {
 'c7': f"@font-face{{font-family:'Comfortaa';font-weight:700;src:url(data:font/woff2;base64,{b64(FD+'/comfortaa/files/comfortaa-latin-700-normal.woff2')}) format('woff2')}}",
 'c4': f"@font-face{{font-family:'Comfortaa';font-weight:400;src:url(data:font/woff2;base64,{b64(FD+'/comfortaa/files/comfortaa-latin-400-normal.woff2')}) format('woff2')}}",
 'f5': f"@font-face{{font-family:'Fira Code';font-weight:500;src:url(data:font/woff2;base64,{b64(FD+'/fira-code/files/fira-code-latin-500-normal.woff2')}) format('woff2')}}",
}
PINK, LPINK, VIOLET, RED, TXT = '#ff2fb3', '#ffd1ef', '#c77dff', '#ff3b5c', '#ecd9f7'

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
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-8px)}}}}
.tw{{transform-box:fill-box;transform-origin:center;animation:tw 2.4s ease-in-out infinite}}
@keyframes tw{{0%,100%{{opacity:.2;transform:scale(.6)}}50%{{opacity:1;transform:scale(1)}}}}
{css}</style>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glow2" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1c0630"/><stop offset="1" stop-color="#2b0a40"/></linearGradient>
<radialGradient id="rg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{PINK}" stop-opacity=".22"/><stop offset="1" stop-color="{PINK}" stop-opacity="0"/></radialGradient>
</defs>
{body}
</svg>'''

def panel(w, h, r=18):
    return (f'<rect x="1.5" y="1.5" width="{w-3}" height="{h-3}" rx="{r}" fill="url(#bg)" stroke="{PINK}" stroke-opacity=".55" stroke-width="2"/>')

def star(x, y, s, c, d):
    return (f'<path class="tw" style="animation-delay:{d}s" d="M{x} {y-s} Q{x} {y} {x+s} {y} Q{x} {y} {x} {y+s} Q{x} {y} {x-s} {y} Q{x} {y} {x} {y-s}Z" fill="{c}"/>')

# ---------- jigsaw edge ----------
TPL = [((0.36,0),(0.42,0),(0.43,0.08)), None]
CURVES = [((0.42,0),(0.43,0.08),(0.40,0.14)), ((0.35,0.24),(0.42,0.36),(0.50,0.36)),
          ((0.58,0.36),(0.65,0.24),(0.60,0.14)), ((0.57,0.08),(0.58,0),(0.64,0))]
def edge(x0,y0,x1,y1,s,depth=82):
    """path commands from (x0,y0) to (x1,y1); s=0 flat, +1 bump inward(normal), -1 outward"""
    if s == 0: return f'L{x1:.1f} {y1:.1f}'
    dx,dy = x1-x0, y1-y0; L = math.hypot(dx,dy); nx,ny = -dy/L, dx/L
    P = lambda u,v: (x0+u*dx+v*depth*s*nx, y0+u*dy+v*depth*s*ny)
    out = ['L%.1f %.1f' % P(0.36,0)]
    for c in CURVES:
        out.append('C' + ' '.join('%.1f %.1f' % P(*p) for p in c))
    out.append(f'L{x1:.1f} {y1:.1f}')
    return ' '.join(out)
def piece(x,y,w,h,top,right,bottom,left,depth=82):
    return (f'M{x} {y} ' + edge(x,y,x+w,y,top,depth) + ' ' + edge(x+w,y,x+w,y+h,right,depth) + ' ' +
            edge(x+w,y+h,x,y+h,bottom,depth) + ' ' + edge(x,y+h,x,y,left,depth) + 'Z')

# ---------- header ----------
def header():
    W,H = 830,210
    pcs = ''
    for (x,y,sz,c,d) in [(70,60,34,PINK,0),(760,140,40,VIOLET,-5),(130,165,22,RED,-9),(700,45,24,PINK,-3)]:
        pcs += f'<path class="spin" style="animation-delay:{d}s" d="{piece(x,y,sz,sz,-1,-1,1,0,sz*0.9)}" fill="none" stroke="{c}" stroke-width="2" filter="url(#glow)" opacity=".8"/>'
    body = panel(W,H) + f'''
<ellipse cx="415" cy="95" rx="330" ry="80" fill="url(#rg)"/>
{pcs}
{star(230,40,7,LPINK,0)}{star(610,170,6,LPINK,1.1)}{star(560,32,5,VIOLET,.6)}{star(280,180,5,PINK,1.7)}
<g class="flick">
<text x="415" y="112" text-anchor="middle" class="t" font-weight="700" font-size="76" fill="#fff2fb" stroke="{PINK}" stroke-width="2" filter="url(#glow2)">Namrata</text>
</g>
<text x="415" y="160" text-anchor="middle" class="m" font-weight="500" font-size="17" fill="#ff9ad5" letter-spacing="1">problem solver · puzzle lover · builder</text>'''
    css = '.flick{animation:flick 5s linear infinite}@keyframes flick{0%,18%,22%,25%,53%,57%,100%{opacity:1}20%,24%,55%{opacity:.35}}'
    return svg(W,H,body,('c7','f5'),css)

# ---------- mascot ----------
def mascot(cx, cy, s=1.0):
    x0,y0,sz = -85,-85,170
    body = piece(x0,y0,sz,sz,-1,-1,0,1,78)
    return f'''<g transform="translate({cx} {cy}) scale({s})"><g class="float">
<ellipse cx="0" cy="118" rx="95" ry="12" fill="{PINK}" opacity=".25" filter="url(#glow)"/>
<ellipse cx="-38" cy="100" rx="24" ry="12" fill="#c2187a" stroke="{LPINK}" stroke-width="2"/>
<ellipse cx="38" cy="100" rx="24" ry="12" fill="#c2187a" stroke="{LPINK}" stroke-width="2"/>
<path d="M-82 15 Q-120 30 -128 -5" fill="none" stroke="{LPINK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="-129" cy="-10" r="11" fill="#ff5ac8" stroke="{LPINK}" stroke-width="2"/>
<g class="wave"><path d="M82 20 Q125 10 135 -35" fill="none" stroke="{LPINK}" stroke-width="9" stroke-linecap="round"/>
<circle cx="136" cy="-42" r="12" fill="#ff5ac8" stroke="{LPINK}" stroke-width="2"/></g>
<path d="{body}" fill="url(#mg)" stroke="{LPINK}" stroke-width="3" filter="url(#glow)"/>
<ellipse cx="-50" cy="25" rx="14" ry="8" fill="#ff9ad5" opacity=".7"/><ellipse cx="50" cy="25" rx="14" ry="8" fill="#ff9ad5" opacity=".7"/>
<g class="blink">
<ellipse cx="-30" cy="-8" rx="20" ry="24" fill="#fff"/><ellipse cx="30" cy="-8" rx="20" ry="24" fill="#fff"/>
<circle cx="-26" cy="-4" r="11" fill="#1a0629"/><circle cx="34" cy="-4" r="11" fill="#1a0629"/>
<circle cx="-22" cy="-9" r="4" fill="#fff"/><circle cx="38" cy="-9" r="4" fill="#fff"/></g>
<path d="M-20 35 Q0 55 20 35" fill="#7a0d4a" stroke="#1a0629" stroke-width="4" stroke-linecap="round"/>
</g></g>'''
MASCOT_CSS = ('.blink{transform-box:fill-box;transform-origin:center;animation:blink 4s infinite}'
 '@keyframes blink{0%,92%,100%{transform:scaleY(1)}95%{transform:scaleY(.1)}}'
 '.wave{transform-box:fill-box;transform-origin:0% 100%;animation:wave 1.6s ease-in-out infinite}'
 '@keyframes wave{0%,100%{transform:rotate(0)}50%{transform:rotate(-18deg)}}')
MG = f'<linearGradient id="mg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff5ac8"/><stop offset="1" stop-color="#b0126e"/></linearGradient>'

def hero(lines, sign):
    W,H = 830,340
    tl = ''.join(f'<text x="250" y="{118+i*38}" text-anchor="middle" class="t" font-weight="700" font-size="26" fill="#fff2fb">{l}</text>' for i,l in enumerate(lines))
    body = panel(W,H) + f'''
<defs>{MG}</defs>
<ellipse cx="620" cy="190" rx="220" ry="150" fill="url(#rg)"/>
{star(470,60,8,LPINK,0)}{star(780,90,6,VIOLET,.8)}{star(520,290,5,PINK,1.4)}{star(60,300,6,LPINK,.4)}{star(780,280,7,PINK,1.9)}
<path d="M60 60 h380 a26 26 0 0 1 26 26 v80 l40 22 -40 6 v16 a26 26 0 0 1 -26 26 h-380 a26 26 0 0 1 -26 -26 v-124 a26 26 0 0 1 26 -26z" fill="#260838" stroke="{PINK}" stroke-width="3" filter="url(#glow)" class="pulse"/>
{tl}
<text x="250" y="290" text-anchor="middle" class="m" font-weight="500" font-size="15" fill="#ff9ad5">{sign}</text>
{mascot(640,170)}'''
    return svg(W,H,body,('c7','f5'),MASCOT_CSS)

# ---------- board ----------
ICONS = {
 'book': lambda c: f'<path d="M-24 -14 q12 -6 24 0 q12 -6 24 0 v30 q-12 -6 -24 0 q-12 -6 -24 0z M0 -14 v30" fill="none" stroke="{c}" stroke-width="3" stroke-linejoin="round"/>',
 'bulb': lambda c: f'<path d="M-9 12 q-15 -9 -15 -24 a24 24 0 0 1 48 0 q0 15 -15 24z M-8 18 h16 M-5 24 h10" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(0 -2)"/>',
 'git': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3"><circle cx="-12" cy="-16" r="5"/><circle cx="-12" cy="18" r="5"/><circle cx="14" cy="-4" r="5"/><path d="M-12 -11 v24 M14 1 q0 10 -22 14"/></g>',
 'sys': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3"><rect x="-26" y="-22" width="18" height="14" rx="3"/><rect x="8" y="-22" width="18" height="14" rx="3"/><rect x="-9" y="10" width="18" height="14" rx="3"/><path d="M-17 -8 v8 h34 v-8 M0 0 v10"/></g>',
 'tree': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3"><circle cx="0" cy="-18" r="6"/><circle cx="-16" cy="4" r="6"/><circle cx="16" cy="4" r="6"/><circle cx="-24" cy="24" r="4"/><circle cx="-8" cy="24" r="4"/><path d="M-4 -13 l-8 12 M4 -13 l8 12 M-19 9 l-3 11 M-13 9 l3 11"/></g>',
 'bars': lambda c: f'<g fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round"><path d="M-26 24 h52"/><rect x="-20" y="4" width="9" height="20" rx="2"/><rect x="-5" y="-12" width="9" height="36" rx="2"/><rect x="10" y="-4" width="9" height="28" rx="2"/><path d="M-22 -6 l14 -12 l14 6 l16 -12" /></g>',
}
PIECES = [('Learning','always chasing','the next piece','book',PINK),
          ('Creating','turning ideas','into real things','bulb',RED),
          ('Open Source','building the big','picture together','git',VIOLET),
          ('System Design','how the big','pieces connect','sys',VIOLET),
          ('Algorithms','the cleverest way','to make it fit','tree',PINK),
          ('Data','the picture hidden','in the noise','bars',RED)]
def board():
    W,H = 830,600
    cw,ch,ox,oy = 230,215,70,105
    vt = {(0,0):1,(0,1):0,(1,0):0,(1,1):1}   # (row,k) tab goes right?
    ht = {0:1,1:0,2:1}                       # col: tab goes down?
    out = ''
    for i,(t,a,b,ic,c) in enumerate(PIECES):
        r,cc = divmod(i,3); x,y = ox+cc*cw, oy+r*ch
        top = 0 if r==0 else (1 if ht[cc] else -1)
        bottom = 0 if r==1 else (-1 if ht[cc] else 1)
        left = 0 if cc==0 else (1 if vt[(r,cc-1)] else -1)
        right = 0 if cc==2 else (-1 if vt[(r,cc)] else 1)
        d = piece(x,y,cw,ch,top,right,bottom,left,80)
        mx,my = x+cw/2, y+ch/2 + (10 if top==1 else 0) - (10 if bottom==1 else 0)
        sx,sy,rot = [(-60,-40,-14),(0,-70,9),(60,-40,-8),(-60,40,10),(0,70,-12),(60,40,13)][i]
        out += f'''<g class="p{i}">
<path d="{d}" fill="url(#pf{i%2})" stroke="{c}" stroke-width="2.5" stroke-linejoin="round" filter="url(#glow)"/>
<g transform="translate({mx} {my-38})" filter="url(#glow)">{ICONS[ic](c)}</g>
<text x="{mx}" y="{my+20}" text-anchor="middle" class="t" font-weight="700" font-size="21" fill="#fff2fb">{t}</text>
<text x="{mx}" y="{my+44}" text-anchor="middle" class="t" font-weight="400" font-size="14" fill="{TXT}">{a}</text>
<text x="{mx}" y="{my+63}" text-anchor="middle" class="t" font-weight="400" font-size="14" fill="{TXT}">{b}</text>
</g>'''
    css = ''.join(f'.p{i}{{transform-box:view-box;animation:in{i} 1.1s cubic-bezier(.2,.9,.25,1.15) {0.25+i*0.18:.2f}s both}}'
                  f'@keyframes in{i}{{0%{{opacity:0;transform:translate({sx}px,{sy}px) rotate({rot}deg)}}100%{{opacity:1;transform:none}}}}'
                  for i,(sx,sy,rot) in enumerate([(-80,-50,-14),(0,-90,9),(80,-50,-8),(-80,50,10),(0,90,-12),(80,50,13)]))
    body = panel(W,H) + f'''
<defs><linearGradient id="pf0" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a0d52"/><stop offset="1" stop-color="#22072f"/></linearGradient>
<linearGradient id="pf1" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a0d52"/><stop offset="1" stop-color="#22072f"/></linearGradient></defs>
<ellipse cx="415" cy="300" rx="380" ry="230" fill="url(#rg)"/>
{star(40,40,7,LPINK,0)}{star(795,60,6,VIOLET,.9)}{star(30,560,5,PINK,1.5)}{star(800,560,7,LPINK,.5)}
<text x="415" y="62" text-anchor="middle" class="t" font-weight="700" font-size="28" fill="#fff2fb" filter="url(#glow)">the pieces that make me</text>
{out}'''
    return svg(W,H,body,('c7','c4'),css)

# ---------- cards ----------
def card(title, lines, btn, icon, c):
    W,H = 405,230
    tl = ''.join(f'<text x="28" y="{108+i*24}" class="t" font-weight="400" font-size="15" fill="{TXT}">{l}</text>' for i,l in enumerate(lines))
    bt = (f'''<g class="pulse"><rect x="{W-28-len(btn)*11-30}" y="178" width="{len(btn)*11+30}" height="34" rx="9" fill="none" stroke="{c}" stroke-width="2" filter="url(#glow)"/>
<text x="{W-28-(len(btn)*11+30)/2}" y="201" text-anchor="middle" class="m" font-weight="500" font-size="16" fill="#fff2fb">{btn}</text></g>''') if btn else ''
    body = panel(W,H) + f'''
<ellipse cx="330" cy="70" rx="110" ry="80" fill="url(#rg)"/>
<text x="28" y="66" class="t" font-weight="700" font-size="30" fill="#fff2fb" filter="url(#glow)">{title}</text>
<g transform="translate(350 62)" filter="url(#glow)">{ICONS[icon](c)}</g>
{tl}
{bt}'''
    return svg(W,H,body,('c7','c4','f5'))

def riddle():
    W,H = 830,200
    body = panel(W,H) + f'''
<ellipse cx="415" cy="100" rx="300" ry="90" fill="url(#rg)"/>
{star(60,40,6,LPINK,0)}{star(770,160,6,VIOLET,1)}
<path class="spin" d="{piece(735,40,40,40,-1,-1,1,0,36)}" fill="none" stroke="{RED}" stroke-width="2" filter="url(#glow)"/>
<text x="415" y="50" text-anchor="middle" class="m" font-weight="500" font-size="15" fill="#ff9ad5" letter-spacing="2">PUZZLE'S RIDDLE</text>
<text x="415" y="92" text-anchor="middle" class="t" font-weight="700" font-size="20" fill="#fff2fb">I have keys but open no locks.</text>
<text x="415" y="120" text-anchor="middle" class="t" font-weight="700" font-size="20" fill="#fff2fb">I have space but no room.</text>
<text x="415" y="148" text-anchor="middle" class="t" font-weight="700" font-size="20" fill="#fff2fb">You can enter, but you can't go inside.</text>
<text x="415" y="180" text-anchor="middle" class="t" font-weight="700" font-size="20" fill="{PINK}" filter="url(#glow)">What am I?</text>'''
    return svg(W,H,body,('c7','f5'))

def footer():
    W,H = 830,130
    body = panel(W,H) + f'''
<ellipse cx="415" cy="65" rx="300" ry="60" fill="url(#rg)"/>
{star(120,40,6,LPINK,0)}{star(720,90,6,VIOLET,.7)}{star(660,30,5,PINK,1.3)}
<path class="spin" d="{piece(80,55,34,34,-1,-1,1,0,30)}" fill="none" stroke="{PINK}" stroke-width="2" filter="url(#glow)"/>
<path class="spin" style="animation-delay:-6s" d="{piece(715,35,30,30,-1,-1,1,0,27)}" fill="none" stroke="{RED}" stroke-width="2" filter="url(#glow)"/>
<text x="415" y="62" text-anchor="middle" class="t" font-weight="700" font-size="26" fill="#fff2fb" filter="url(#glow)">thanks for stopping by!</text>
<text x="415" y="95" text-anchor="middle" class="m" font-weight="500" font-size="15" fill="#ff9ad5">building it one piece at a time</text>'''
    return svg(W,H,body,('c7','f5'))

files = {
 'header.svg': header(),
 'hero-dark.svg': hero(['Nice, dark mode!','A true puzzle','solver, I see. hehe'], "- Puzzle, Namrata's sidekick"),
 'hero-light.svg': hero(['Light mode, huh?','Bold move.','Puzzle approves!'], "- Puzzle, Namrata's sidekick"),
 'pieces.svg': board(),
 'story.svg': card('My story',['Most of my code shipped at work,','in private repos. Now I am','building in public, piece by piece.'],'','sys',PINK),
 'agentic.svg': card('Agentic',['My experiments with AI agents.','Small pieces that think,','plan and act together.'],'Explore','bulb',RED),
 'riddle.svg': riddle(),
 'footer.svg': footer(),
}
for n,s in files.items():
    open(os.path.join(OUT,n),'w').write(s)
    print(n, len(s)//1024, 'KB')
