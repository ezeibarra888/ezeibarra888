# -*- coding: utf-8 -*-
import io, os, sys, math
D = sys.argv[1]
MONO = "ui-monospace,SFMono-Regular,'JetBrains Mono',Menlo,Consolas,monospace"
W, H = 470, 442
CX, CY, R = 235, 212, 132

AXES = [
    (".NET / C#",      0.95),
    ("React / TS",     0.86),
    ("SQL / datos",    0.90),
    ("observabilidad", 0.78),
    ("seguridad",      0.76),
    ("CI/CD / Docker", 0.84),
]
N = len(AXES)

def pt(i, f):
    a = -math.pi / 2 + 2 * math.pi * i / N
    return (CX + math.cos(a) * R * f, CY + math.sin(a) * R * f)

rings = []
for f in (0.25, 0.5, 0.75, 1.0):
    p = " ".join("%.1f,%.1f" % pt(i, f) for i in range(N))
    rings.append('<polygon points="%s" fill="none" stroke="#12382c" stroke-width="1" opacity="%s"/>'
                 % (p, "0.95" if f == 1.0 else "0.6"))

spokes, labels, dots = [], [], []
for i, (name, v) in enumerate(AXES):
    ex, ey = pt(i, 1.0)
    spokes.append('<path d="M%d %d L%.1f %.1f" stroke="#12382c" stroke-width="1" opacity="0.7"/>' % (CX, CY, ex, ey))
    lx, ly = pt(i, 1.26)
    anchor = "middle"
    if lx > CX + 12: anchor = "start"
    elif lx < CX - 12: anchor = "end"
    labels.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="11.5" fill="#8fb3a6">%s</text>'
                  % (lx, ly + 4, anchor, name))
    labels.append('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="10" fill="#2f6b55">%d%%</text>'
                  % (lx, ly + 17, anchor, int(v * 100)))
    dx, dy = pt(i, v)
    dots.append('<circle class="dot" style="animation-delay:%ss" cx="%.1f" cy="%.1f" r="3.4" fill="#00ff9c"/>'
                % (round(0.9 + i * 0.12, 2), dx, dy))

poly = " ".join("%.1f,%.1f" % pt(i, v) for i, (_, v) in enumerate(AXES))

svg = u'''<svg xmlns="http://www.w3.org/2000/svg" width="%(W)d" height="%(H)d" viewBox="0 0 %(W)d %(H)d" role="img" aria-labelledby="t d">
<title id="t">Radar de habilidades</title>
<desc id="d">Radar hexagonal con barrido rotatorio. Niveles aproximados: .NET y C# 95 por ciento, React y TypeScript 86, SQL y datos 90, observabilidad 78, seguridad 76, CI CD y Docker 84.</desc>
<defs>
  <linearGradient id="pan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%%" stop-color="#0b1014"/><stop offset="100%%" stop-color="#05070a"/>
  </linearGradient>
  <radialGradient id="fill" cx="50%%" cy="50%%" r="50%%">
    <stop offset="0%%" stop-color="#00ff9c" stop-opacity="0.42"/>
    <stop offset="100%%" stop-color="#00ff9c" stop-opacity="0.1"/>
  </radialGradient>
  <linearGradient id="wedge" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%%" stop-color="#00ff9c" stop-opacity="0.34"/>
    <stop offset="100%%" stop-color="#00ff9c" stop-opacity="0"/>
  </linearGradient>
  <filter id="gl" x="-80%%" y="-80%%" width="260%%" height="260%%">
    <feGaussianBlur stdDeviation="2.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="pc"><rect x="1" y="1" width="%(W2)d" height="%(H2)d" rx="12"/></clipPath>
</defs>
<style>
  text{font-family:%(MONO)s}
  @keyframes spin{to{transform:rotate(360deg)}}
  .sweep{transform-origin:%(CX)dpx %(CY)dpx;animation:spin 4.6s linear infinite}
  @keyframes grow{from{transform:scale(.05);opacity:0}to{transform:scale(1);opacity:1}}
  .shape{transform-origin:%(CX)dpx %(CY)dpx;animation:grow 1.5s cubic-bezier(.2,.8,.2,1) both}
  @keyframes pop{from{opacity:0}to{opacity:1}}
  .dot{opacity:0;animation:pop .5s ease-out both}
  @keyframes bp{0%%,100%%{opacity:.25}50%%{opacity:1}}
  .bp{animation:bp 2.2s ease-in-out infinite}
  @keyframes blink{0%%,49%%{opacity:1}50%%,100%%{opacity:0}}
  .cur{animation:blink 1.05s step-end infinite}
</style>
<g clip-path="url(#pc)">
  <rect x="1" y="1" width="%(W2)d" height="%(H2)d" rx="12" fill="url(#pan)"/>
  <text x="22" y="30" font-size="12" fill="#7f9aa8">
    <tspan fill="#00ff9c">scan</tspan><tspan>@stack:~$ </tspan><tspan fill="#9affd8">radar</tspan><tspan class="cur" fill="#00ff9c">&#9608;</tspan>
  </text>
  <g text-anchor="end">
    <text x="%(RX)d" y="30" font-size="11" fill="#4b6b7a">6 vectores</text>
    <circle class="bp" cx="%(DX)d" cy="25" r="3.6" fill="#00ff9c" filter="url(#gl)"/>
  </g>
  <g class="sweep">
    <path d="M%(CX)d %(CY)d L%(CX)d %(TOPY)d A %(R)d %(R)d 0 0 1 %(AX).1f %(AY).1f Z" fill="url(#wedge)"/>
  </g>
  %(RINGS)s
  %(SPOKES)s
  <g class="shape">
    <polygon points="%(POLY)s" fill="url(#fill)" stroke="#00ff9c" stroke-width="2.2" filter="url(#gl)"/>
  </g>
  %(DOTS)s
  <circle cx="%(CX)d" cy="%(CY)d" r="2.6" fill="#9affd8"/>
  %(LABELS)s
  <text x="%(CXT)d" y="%(BY)d" text-anchor="middle" font-size="10.5" fill="#2f6b55">valores autoevaluados &#183; se ajustan</text>
</g>
<rect x="0.5" y="0.5" width="%(W1)d" height="%(H1)d" rx="12" fill="none" stroke="#174a3a"/>
</svg>
''' % dict(W=W, H=H, W1=W-1, H1=H-1, W2=W-2, H2=H-2, MONO=MONO, CX=CX, CY=CY, R=R,
           TOPY=CY-R, AX=CX+math.cos(-math.pi/2+math.pi/3)*R, AY=CY+math.sin(-math.pi/2+math.pi/3)*R,
           RINGS="\n  ".join(rings), SPOKES="\n  ".join(spokes), DOTS="\n  ".join(dots),
           LABELS="\n  ".join(labels), POLY=poly, RX=W-38, DX=W-22, CXT=CX, BY=H-16)

io.open(os.path.join(D, "assets", "radar.svg"), "w", encoding="utf-8").write(svg)
print("radar.svg", len(svg), "bytes")
