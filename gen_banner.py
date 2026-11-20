# -*- coding: utf-8 -*-
import io, os, random, sys
from xml.sax.saxutils import escape
D = sys.argv[1]
random.seed(7)
GLYPHS = list(u"01{}[]#$/=+*ABCDEF0xff%@!?;:~^·│░▓")
MONO = "ui-monospace,SFMono-Regular,'JetBrains Mono',Menlo,Consolas,monospace"
W, H = 960, 220

cols = []
x = 14
while x < W:
    dur = round(random.uniform(4.2, 11.0), 2)
    delay = round(-random.uniform(0, 11.0), 2)
    n = random.randint(5, 9)
    op = round(random.uniform(0.14, 0.40), 2)
    glyphs = []
    for i in range(n):
        g = escape(random.choice(GLYPHS))
        o = round(op * (1 - i / float(n + 1)), 3)
        glyphs.append('<text x="0" y="%d" opacity="%s">%s</text>' % (i * 17, o, g))
    cols.append(
        '<g transform="translate(%d,0)"><g class="col" style="animation-duration:%ss;animation-delay:%ss">%s</g></g>'
        % (x, dur, delay, "".join(glyphs))
    )
    x += random.randint(17, 30)

svg = u'''<svg xmlns="http://www.w3.org/2000/svg" width="%(W)d" height="%(H)d" viewBox="0 0 %(W)d %(H)d" role="img" aria-labelledby="t d">
<title id="t">Eze Ibarra</title>
<desc id="d">Banner animado: lluvia de caracteres, titulo con efecto glitch y linea de escaneo sobre fondo oscuro.</desc>
<defs>
  <radialGradient id="vig" cx="50%%" cy="40%%" r="75%%">
    <stop offset="0%%" stop-color="#0b1a16"/>
    <stop offset="65%%" stop-color="#05070a"/>
    <stop offset="100%%" stop-color="#000000"/>
  </radialGradient>
  <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%%" stop-color="#00ff9c" stop-opacity="0"/>
    <stop offset="45%%" stop-color="#00ff9c" stop-opacity="0.5"/>
    <stop offset="55%%" stop-color="#9affd8" stop-opacity="0.75"/>
    <stop offset="100%%" stop-color="#00ff9c" stop-opacity="0"/>
  </linearGradient>
  <filter id="glow" x="-30%%" y="-60%%" width="160%%" height="260%%">
    <feGaussianBlur stdDeviation="3.4" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="soft" x="-30%%" y="-60%%" width="160%%" height="260%%">
    <feGaussianBlur stdDeviation="1.1"/>
  </filter>
  <clipPath id="frame"><rect x="0" y="0" width="%(W)d" height="%(H)d" rx="10"/></clipPath>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="#0d3a2c" stroke-width="1" opacity="0.5"/>
  </pattern>
</defs>
<style>
  .mono{font-family:%(MONO)s}
  .col{font-family:%(MONO)s;font-size:14px;fill:#00ff9c;animation-name:fall;animation-timing-function:linear;animation-iteration-count:infinite}
  @keyframes fall{from{transform:translateY(-150px)}to{transform:translateY(240px)}}
  @keyframes sweep{0%%{transform:translateY(-70px)}100%%{transform:translateY(250px)}}
  .scan{animation:sweep 5.5s linear infinite}
  @keyframes flick{0%%,100%%{opacity:1}42%%{opacity:.92}44%%{opacity:.45}46%%{opacity:1}72%%{opacity:.88}74%%{opacity:.5}76%%{opacity:1}}
  .ttl{animation:flick 6s steps(1,end) infinite}
  @keyframes shiftR{0%%,100%%{transform:translate(0,0);opacity:.0}43%%{transform:translate(-3px,1px);opacity:.55}47%%{transform:translate(2px,-1px);opacity:.35}50%%{opacity:0}73%%{transform:translate(2px,0);opacity:.5}76%%{opacity:0}}
  @keyframes shiftC{0%%,100%%{transform:translate(0,0);opacity:0}44%%{transform:translate(3px,-1px);opacity:.5}48%%{transform:translate(-2px,1px);opacity:.3}51%%{opacity:0}74%%{transform:translate(-3px,1px);opacity:.45}77%%{opacity:0}}
  .gr{animation:shiftR 6s steps(1,end) infinite}
  .gc{animation:shiftC 6s steps(1,end) infinite}
  @keyframes blink{0%%,49%%{opacity:1}50%%,100%%{opacity:0}}
  .cur{animation:blink 1.05s step-end infinite}
  @keyframes dash{to{stroke-dashoffset:-400}}
  .wire{animation:dash 9s linear infinite}
  @keyframes pulse{0%%,100%%{opacity:.35}50%%{opacity:1}}
  .pulse{animation:pulse 2.4s ease-in-out infinite}
</style>
<g clip-path="url(#frame)">
  <rect width="%(W)d" height="%(H)d" fill="url(#vig)"/>
  <rect width="%(W)d" height="%(H)d" fill="url(#grid)" opacity="0.35"/>
  <g filter="url(#soft)">%(COLS)s</g>
  <rect class="scan" x="0" y="0" width="%(W)d" height="70" fill="url(#scan)" opacity="0.13"/>
  <path class="wire" d="M0 196 H %(W)d" stroke="#00ff9c" stroke-width="1" stroke-dasharray="3 9" opacity="0.4" fill="none"/>
  <path class="wire" d="M0 24 H %(W)d" stroke="#00ff9c" stroke-width="1" stroke-dasharray="3 9" opacity="0.25" fill="none"/>

  <g class="mono" text-anchor="middle">
    <text class="gr" x="480" y="104" font-size="54" font-weight="700" letter-spacing="7" fill="#ff3b5c">EZE IBARRA</text>
    <text class="gc" x="480" y="104" font-size="54" font-weight="700" letter-spacing="7" fill="#22d3ee">EZE IBARRA</text>
    <text class="ttl" x="480" y="104" font-size="54" font-weight="700" letter-spacing="7" fill="#00ff9c" filter="url(#glow)">EZE IBARRA</text>
    <text x="480" y="140" font-size="15" letter-spacing="4.5" fill="#6ee7b7" opacity="0.92">[ fullstack &#183; devsecops &#183; security ]</text>
    <text x="480" y="174" font-size="12.5" letter-spacing="1.6" fill="#7f9aa8">
      <tspan fill="#00ff9c">root@secnode</tspan><tspan>:~# ./deploy --signed --audited</tspan><tspan class="cur" fill="#00ff9c"> &#9608;</tspan>
    </text>
  </g>

  <g stroke="#00ff9c" stroke-width="2" fill="none" class="pulse">
    <path d="M16 46 V16 H46"/><path d="M%(X1)d 46 V16 H%(X2)d"/>
    <path d="M16 174 V204 H46"/><path d="M%(X1)d 174 V204 H%(X2)d"/>
  </g>
  <rect x="0.5" y="0.5" width="%(W1)d" height="%(H1)d" rx="10" fill="none" stroke="#124d3a" stroke-width="1"/>
</g>
</svg>
''' % dict(W=W, H=H, W1=W-1, H1=H-1, MONO=MONO, COLS="".join(cols), X1=W-16, X2=W-46)

io.open(os.path.join(D, "assets", "banner.svg"), "w", encoding="utf-8").write(svg)
print("banner.svg", len(svg), "bytes")
