# -*- coding: utf-8 -*-
import io, os, sys
D = sys.argv[1]
MONO = "ui-monospace,SFMono-Regular,'JetBrains Mono',Menlo,Consolas,monospace"
W, H = 960, 260
CY = 7.6  # duracion del ciclo del paquete

NODES = [
    ("commit",        "\u2387"),
    ("lint + tests",  "\u2713"),
    ("secret scan",   "\u26bf"),
    ("SAST",          "\u2318"),
    ("deps / CVE",    "\u2691"),
    ("firma + SBOM",  "\u2713"),
    ("deploy",        "\u25b6"),
]
BW, BH, CYL = 118, 48, 112
x0, step = 24 + BW / 2.0, (W - 48 - BW) / float(len(NODES) - 1)
cx = [x0 + i * step for i in range(len(NODES))]
GATES = [2, 4]  # secret scan y deps/CVE pueden abortar

boxes, labels = [], []
for i, (name, ico) in enumerate(NODES):
    x, t = cx[i] - BW / 2.0, round((cx[i] - cx[0]) / (cx[-1] - cx[0]) * CY, 2)
    stroke = "#ff7a8f" if i in GATES else "#174a3a"
    boxes.append(
        '<g class="nd" style="animation-delay:%ss">'
        '<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="9" fill="#0a1016" stroke="%s"/>'
        '<rect class="hl" x="%.1f" y="%.1f" width="%d" height="%d" rx="9" fill="none" stroke="#00ff9c" stroke-width="1.8"/>'
        '</g>' % (t, x, CYL - BH / 2.0, BW, BH, stroke, x, CYL - BH / 2.0, BW, BH)
    )
    col = "#ff9fb0" if i in GATES else "#6ee7b7"
    labels.append(
        '<g class="nd" style="animation-delay:%ss" text-anchor="middle">'
        '<text x="%.1f" y="%.1f" font-size="15" fill="%s" opacity="0.9">%s</text>'
        '<text x="%.1f" y="%.1f" font-size="11.5" fill="#c9d1d9">%s</text></g>'
        % (t, cx[i], CYL - 6, col, ico, cx[i], CYL + 13, name)
    )

aborts = []
for i in GATES:
    t = round((cx[i] - cx[0]) / (cx[-1] - cx[0]) * CY, 2)
    aborts.append(
        '<path class="ab" style="animation-delay:%ss" d="M%.1f %d V 176 H 470" fill="none" stroke="#ff3b5c" '
        'stroke-width="1.6" stroke-dasharray="5 5"/>' % (t, cx[i], CYL + 24)
    )

svg = u'''<svg xmlns="http://www.w3.org/2000/svg" width="%(W)d" height="%(H)d" viewBox="0 0 %(W)d %(H)d" role="img" aria-labelledby="t d">
<title id="t">Pipeline seguro</title>
<desc id="d">Diagrama animado de un pipeline DevSecOps: commit, lint y tests, escaneo de secretos, analisis estatico, revision de dependencias con CVE, firma con SBOM y deploy. Las compuertas de secretos y dependencias pueden abortar el build. La observabilidad retroalimenta al commit.</desc>
<defs>
  <linearGradient id="pan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%%" stop-color="#0b1014"/><stop offset="100%%" stop-color="#05070a"/>
  </linearGradient>
  <filter id="gl" x="-120%%" y="-120%%" width="340%%" height="340%%">
    <feGaussianBlur stdDeviation="3.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="pc"><rect x="1" y="1" width="%(W2)d" height="%(H2)d" rx="12"/></clipPath>
  <path id="track" d="M%(X0).1f %(CYL)d H %(XN).1f"/>
</defs>
<style>
  text{font-family:%(MONO)s}
  @keyframes flow{to{stroke-dashoffset:-320}}
  .wire{animation:flow 6s linear infinite}
  @keyframes on{0%%{opacity:0}4%%{opacity:1}16%%{opacity:.55}26%%{opacity:0}100%%{opacity:0}}
  .hl{opacity:0;animation:on %(CY)ss linear infinite}
  @keyframes lab{0%%{opacity:.45}4%%{opacity:1}30%%{opacity:1}60%%{opacity:.45}100%%{opacity:.45}}
  .nd{animation:lab %(CY)ss linear infinite}
  @keyframes abf{0%%,100%%{opacity:0}5%%{opacity:.95}14%%{opacity:.2}22%%{opacity:.8}34%%{opacity:0}}
  .ab{opacity:0;animation:abf %(CY)ss linear infinite}
  @keyframes abx{0%%,100%%{opacity:.18}6%%{opacity:1}30%%{opacity:.18}}
  .abox{animation:abx %(CY)ss linear infinite;animation-delay:2.1s}
  @keyframes blink{0%%,49%%{opacity:1}50%%,100%%{opacity:0}}
  .cur{animation:blink 1.05s step-end infinite}
  @keyframes bp{0%%,100%%{opacity:.25}50%%{opacity:1}}
  .bp{animation:bp 2.2s ease-in-out infinite}
</style>
<g clip-path="url(#pc)">
  <rect x="1" y="1" width="%(W2)d" height="%(H2)d" rx="12" fill="url(#pan)"/>

  <text x="24" y="32" font-size="12.5" fill="#7f9aa8">
    <tspan fill="#00ff9c">pipeline</tspan><tspan>@secnode:~$ </tspan><tspan fill="#9affd8">build --break --harden --ship</tspan><tspan class="cur" fill="#00ff9c">&#9608;</tspan>
  </text>
  <g text-anchor="end">
    <text x="%(RX)d" y="32" font-size="11.5" fill="#4b6b7a">gates: 2 activos</text>
    <circle class="bp" cx="%(DX)d" cy="27" r="4" fill="#00ff9c" filter="url(#gl)"/>
  </g>

  <path class="wire" d="M%(X0).1f %(CYL)d H %(XN).1f" fill="none" stroke="#1b5a44" stroke-width="2" stroke-dasharray="7 7"/>
  %(BOXES)s
  %(ABORTS)s

  <g class="abox">
    <rect x="382" y="176" width="176" height="34" rx="8" fill="#17060b" stroke="#ff3b5c" stroke-width="1.4"/>
    <text x="470" y="198" text-anchor="middle" font-size="11.5" fill="#ff8fa3">exit 1 &#183; build abortado</text>
  </g>

  <path class="wire" d="M%(XN).1f 150 V 232 H %(X0).1f V 150" fill="none" stroke="#1b5a44" stroke-width="1.4" stroke-dasharray="4 8" opacity="0.8"/>
  <rect x="%(TBX).1f" y="214" width="250" height="18" rx="4" fill="#05070a"/>
  <text x="%(MID).1f" y="227" text-anchor="middle" font-size="11" fill="#4b6b7a">observabilidad &#8594; feedback al commit</text>

  <circle r="5.5" fill="#00ff9c" filter="url(#gl)">
    <animateMotion dur="%(CY)ss" repeatCount="indefinite" rotate="auto"><mpath href="#track"/></animateMotion>
  </circle>
  <circle r="3" fill="#9affd8" opacity="0.65">
    <animateMotion dur="%(CY)ss" begin="-0.16s" repeatCount="indefinite"><mpath href="#track"/></animateMotion>
  </circle>
  <circle r="2" fill="#9affd8" opacity="0.35">
    <animateMotion dur="%(CY)ss" begin="-0.32s" repeatCount="indefinite"><mpath href="#track"/></animateMotion>
  </circle>

  %(LABELS)s
</g>
<rect x="0.5" y="0.5" width="%(W1)d" height="%(H1)d" rx="12" fill="none" stroke="#174a3a"/>
</svg>
''' % dict(W=W, H=H, W1=W-1, H1=H-1, W2=W-2, H2=H-2, MONO=MONO, CY=CY, CYL=CYL,
           X0=cx[0], XN=cx[-1], MID=(cx[0]+cx[-1])/2.0, TBX=(cx[0]+cx[-1])/2.0-125, RX=W-44, DX=W-26,
           BOXES="\n  ".join(boxes), LABELS="\n  ".join(labels), ABORTS="\n  ".join(aborts))

io.open(os.path.join(D, "assets", "pipeline.svg"), "w", encoding="utf-8").write(svg)
print("pipeline.svg", len(svg), "bytes")
