# -*- coding: utf-8 -*-
import io, os, sys
from xml.sax.saxutils import escape
D = sys.argv[1]
MONO = "ui-monospace,SFMono-Regular,'JetBrains Mono',Menlo,Consolas,monospace"
G, DIM, KEY, VAL, STR, CMT, RED = "#00ff9c", "#0f8f63", "#6ee7b7", "#c9d1d9", "#9affd8", "#4b6b7a", "#ff3b5c"

L = [
  [(G, "root@secnode"), (VAL, ":~# "), (STR, "whoami --verbose")],
  [],
  [(KEY, "operador        "), (VAL, ": Ezequiel Ibarra "), (CMT, "<ezedev>")],
  [(KEY, "rol             "), (VAL, ": Fullstack Developer / DevSecOps")],
  [(KEY, "base            "), (VAL, ": Argentina "), (DIM, "\u00b7"), (VAL, " UTC-3")],
  [(KEY, "uptime          "), (VAL, ": sistemas en produccion que no se pueden caer")],
  [],
  [(CMT, "# mision")],
  [(DIM, "  - "), (VAL, "software de gestion que corre en produccion, no en slides")],
  [(DIM, "  - "), (VAL, "automatizar el deploy hasta que apretar el boton sea aburrido")],
  [(DIM, "  - "), (VAL, "tratar la seguridad como requisito, no como parche final")],
  [],
  [(CMT, "# principios")],
  [(KEY, "  shift_left      "), (VAL, ": "), (STR, "\"la vuln mas barata es la que nunca se mergeo\"")],
  [(KEY, "  least_privilege "), (VAL, ": "), (G, "enforced")],
  [(KEY, "  observabilidad  "), (VAL, ": "), (STR, "\"si no se observa, no existe\"")],
  [(KEY, "  secrets_en_repo "), (VAL, ": "), (RED, "never")],
  [],
  [(G, "root@secnode"), (VAL, ":~# "), (None, "CURSOR")],
]

W, PAD, TOP, STEP = 960, 26, 86, 20.5
H = int(TOP + len(L) * STEP + 26)
CYCLE, STAG = 0.55, 0.22

rows = []
for i, parts in enumerate(L):
    y = TOP + i * STEP
    num = '<text x="%d" y="%s" fill="#1d4034" font-size="11">%02d</text>' % (PAD, y, i + 1)
    if not parts:
        rows.append('<g class="ln" style="animation-delay:%ss">%s</g>' % (round(i * STAG, 2), num))
        continue
    spans = []
    for color, txt in parts:
        if txt == "CURSOR":
            spans.append('<tspan class="cur" fill="%s">\u2588</tspan>' % G)
        else:
            spans.append('<tspan fill="%s" xml:space="preserve">%s</tspan>' % (color, escape(txt)))
    rows.append(
        '<g class="ln" style="animation-delay:%ss">%s<text x="%d" y="%s" font-size="13.5">%s</text></g>'
        % (round(i * STAG, 2), num, PAD + 30, y, "".join(spans))
    )

svg = u'''<svg xmlns="http://www.w3.org/2000/svg" width="%(W)d" height="%(H)d" viewBox="0 0 %(W)d %(H)d" role="img" aria-labelledby="t d">
<title id="t">whoami de Ezequiel Ibarra</title>
<desc id="d">Terminal oscura que imprime linea por linea el perfil: Ezequiel Ibarra, Fullstack Developer y DevSecOps en Argentina, su mision y sus principios de seguridad.</desc>
<defs>
  <linearGradient id="pan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%%" stop-color="#0b1014"/><stop offset="100%%" stop-color="#05070a"/>
  </linearGradient>
  <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%%" stop-color="#132029"/><stop offset="100%%" stop-color="#0c141a"/>
  </linearGradient>
  <filter id="gl" x="-50%%" y="-50%%" width="200%%" height="200%%">
    <feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="pc"><rect x="1" y="1" width="%(W2)d" height="%(H2)d" rx="12"/></clipPath>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#00ff9c" opacity="0.045"/>
  </pattern>
</defs>
<style>
  text{font-family:%(MONO)s}
  @keyframes rev{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:translateX(0)}}
  .ln{opacity:0;animation:rev %(CY)ss ease-out both}
  @keyframes blink{0%%,49%%{opacity:1}50%%,100%%{opacity:0}}
  .cur{animation:blink 1.05s step-end infinite}
  @keyframes bp{0%%,100%%{opacity:.3}50%%{opacity:1}}
  .bp{animation:bp 2s ease-in-out infinite}
  @keyframes sweep{0%%{transform:translateY(-40px)}100%%{transform:translateY(%(H)dpx)}}
  .sw{animation:sweep 7s linear infinite}
</style>
<g clip-path="url(#pc)">
  <rect x="1" y="1" width="%(W2)d" height="%(H2)d" rx="12" fill="url(#pan)"/>
  <rect x="1" y="1" width="%(W2)d" height="%(H2)d" fill="url(#scan)"/>
  <rect class="sw" x="1" y="0" width="%(W2)d" height="40" fill="#00ff9c" opacity="0.05"/>
  <rect x="1" y="1" width="%(W2)d" height="42" fill="url(#bar)"/>
  <circle cx="26" cy="22" r="5.5" fill="#ff5f57" opacity="0.85"/>
  <circle cx="46" cy="22" r="5.5" fill="#febc2e" opacity="0.85"/>
  <circle cx="66" cy="22" r="5.5" fill="#28c840" opacity="0.85"/>
  <text x="92" y="27" font-size="12.5" fill="#7f9aa8">ezeibarra888@secnode &#8212; /usr/bin/whoami</text>
  <g text-anchor="end">
    <text x="%(RX)d" y="27" font-size="11.5" fill="#4b6b7a">tls 1.3 &#183; canal cifrado</text>
    <circle class="bp" cx="%(DX)d" cy="22" r="4" fill="#00ff9c" filter="url(#gl)"/>
  </g>
  <path d="M1 43 H %(W1)d" stroke="#1b3a30" stroke-width="1"/>
  %(ROWS)s
</g>
<rect x="0.5" y="0.5" width="%(W1)s" height="%(H1)s" rx="12" fill="none" stroke="#174a3a"/>
</svg>
''' % dict(W=W, H=H, W1=W-1, H1=H-1, W2=W-2, H2=H-2, MONO=MONO, ROWS="\n  ".join(rows),
           CY=CYCLE, RX=W-44, DX=W-26)

io.open(os.path.join(D, "assets", "whoami.svg"), "w", encoding="utf-8").write(svg)
print("whoami.svg", H, "px alto,", len(svg), "bytes")
