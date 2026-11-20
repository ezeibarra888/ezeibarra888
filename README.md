<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:0d1117,100:000000&height=200&section=header&text=EZE%20IBARRA&fontSize=64&fontColor=00ff9c&fontAlignY=40&animation=fadeIn&desc=%5B%20fullstack%20%C2%B7%20devsecops%20%C2%B7%20security%20%5D&descSize=16&descAlignY=62" width="100%" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&duration=3200&pause=900&color=00FF9C&center=true&vCenter=true&width=820&lines=%3E+establishing+secure+channel...;%3E+identity+verified+%E2%80%94+access+granted;%3E+el+c%C3%B3digo+que+nadie+audita+no+es+seguro;%3E+build+%E2%86%92+break+%E2%86%92+harden+%E2%86%92+repeat" alt="typing" />

<br/>

![](https://img.shields.io/badge/clearance-AUTHORIZED-00ff9c?style=flat-square&labelColor=0d1117)
![](https://img.shields.io/badge/status-ONLINE-00ff9c?style=flat-square&labelColor=0d1117)
![](https://img.shields.io/badge/location-AR-00ff9c?style=flat-square&labelColor=0d1117)
[![](https://komarev.com/ghpvc/?username=ezeibarra888&style=flat-square&color=00ff9c&label=traces)](https://github.com/ezeibarra888)

</div>

---

## `$ whoami`

```yaml
operador:
  nombre:     Ezequiel Ibarra
  alias:      ezedev
  rol:        Fullstack Developer / DevSecOps
  base:       Argentina
  idiomas:    [ es, en ]

mision:
  - construir software de gestion que corre en produccion, no en slides
  - automatizar el deploy hasta que apretar un boton sea aburrido
  - tratar la seguridad como requisito, no como parche final

principios:
  - shift_left: "la vulnerabilidad mas barata es la que nunca se mergeo"
  - least_privilege: true
  - logs: "si no se observa, no existe"
  - secrets_en_el_repo: never
```

---

## `$ cat arsenal.txt`

<table>
<tr>
<td valign="top" width="50%">

**Backend & Datos**

![](https://img.shields.io/badge/C%23-0d1117?style=for-the-badge&logo=csharp&logoColor=00ff9c)
![](https://img.shields.io/badge/.NET%209-0d1117?style=for-the-badge&logo=dotnet&logoColor=00ff9c)
![](https://img.shields.io/badge/EF%20Core-0d1117?style=for-the-badge&logo=nuget&logoColor=00ff9c)
![](https://img.shields.io/badge/SQL%20Server-0d1117?style=for-the-badge&logo=microsoftsqlserver&logoColor=00ff9c)
![](https://img.shields.io/badge/Node.js-0d1117?style=for-the-badge&logo=nodedotjs&logoColor=00ff9c)

</td>
<td valign="top" width="50%">

**Frontend**

![](https://img.shields.io/badge/TypeScript-0d1117?style=for-the-badge&logo=typescript&logoColor=00ff9c)
![](https://img.shields.io/badge/React-0d1117?style=for-the-badge&logo=react&logoColor=00ff9c)
![](https://img.shields.io/badge/Vue%203-0d1117?style=for-the-badge&logo=vuedotjs&logoColor=00ff9c)
![](https://img.shields.io/badge/Vite-0d1117?style=for-the-badge&logo=vite&logoColor=00ff9c)
![](https://img.shields.io/badge/Electron-0d1117?style=for-the-badge&logo=electron&logoColor=00ff9c)

</td>
</tr>
<tr>
<td valign="top" width="50%">

**Infra & Pipeline**

![](https://img.shields.io/badge/Docker-0d1117?style=for-the-badge&logo=docker&logoColor=00ff9c)
![](https://img.shields.io/badge/Jenkins-0d1117?style=for-the-badge&logo=jenkins&logoColor=00ff9c)
![](https://img.shields.io/badge/Traefik-0d1117?style=for-the-badge&logo=traefikproxy&logoColor=00ff9c)
![](https://img.shields.io/badge/Linux-0d1117?style=for-the-badge&logo=linux&logoColor=00ff9c)
![](https://img.shields.io/badge/Cloudflare-0d1117?style=for-the-badge&logo=cloudflare&logoColor=00ff9c)

</td>
<td valign="top" width="50%">

**Observabilidad & Defensa**

![](https://img.shields.io/badge/Zabbix-0d1117?style=for-the-badge&logo=zabbix&logoColor=00ff9c)
![](https://img.shields.io/badge/Grafana-0d1117?style=for-the-badge&logo=grafana&logoColor=00ff9c)
![](https://img.shields.io/badge/Sentry-0d1117?style=for-the-badge&logo=sentry&logoColor=00ff9c)
![](https://img.shields.io/badge/Wireshark-0d1117?style=for-the-badge&logo=wireshark&logoColor=00ff9c)
![](https://img.shields.io/badge/Kali-0d1117?style=for-the-badge&logo=kalilinux&logoColor=00ff9c)

</td>
</tr>
</table>

---

## `$ trace --pipeline`

```mermaid
%%{init: {'theme':'dark','themeVariables':{'primaryColor':'#0d1117','primaryTextColor':'#00ff9c','primaryBorderColor':'#00ff9c','lineColor':'#00ff9c','fontFamily':'monospace'}}}%%
flowchart LR
    A([commit]) --> B[lint + tests]
    B --> C{secret scan}
    C -- leak --> X([build abortado])
    C -- clean --> D[analisis estatico]
    D --> E{deps con CVE?}
    E -- si --> X
    E -- no --> F[imagen firmada]
    F --> G[deploy]
    G --> H[[observabilidad]]
    H -. alerta .-> A
```

> El pipeline no esta para pasar, esta para frenar lo que no deberia salir.

---

## `$ ls -la proyectos/`

| | proyecto | descripcion | stack |
|---|---|---|---|
| `>` | **[EZEDEV · portfolio](https://github.com/ezeibarra888/portfolio)** | Portfolio con tematica cybersec: boot sequence, terminal interactiva, glitch text y easter eggs | `Vue 3` `TypeScript` `GSAP` |
| `>` | **[ezeibarra888.github.io](https://github.com/ezeibarra888/ezeibarra888.github.io)** | Landing personal, deploy continuo sobre GitHub Pages | `HTML` `CSS` |
| `>` | **[Alquila](https://github.com/ezeibarra888/Alquila_app)** | Gestion de alquileres: contratos, vencimientos y cobros | `TypeScript` |
| `#` | *clasificado* | Plataforma de gestion interna en produccion: API .NET 9, cliente React, app de escritorio Electron, sync con sistema legacy y alertas por Telegram | `.NET 9` `React` `SQL Server` |

<sub>Lo que mas me divierte vive en repos privados. Si queres ver el detalle, preguntame.</sub>

---

## `$ systemctl status actividad`

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=ezeibarra888&show_icons=true&count_private=true&hide_border=true&bg_color=0d1117&title_color=00ff9c&text_color=c9d1d9&icon_color=00ff9c&ring_color=00ff9c" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=ezeibarra888&layout=compact&langs_count=8&hide_border=true&bg_color=0d1117&title_color=00ff9c&text_color=c9d1d9" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=ezeibarra888&hide_border=true&background=0d1117&stroke=00ff9c&ring=00ff9c&fire=00ff9c&currStreakLabel=00ff9c&sideLabels=c9d1d9&dates=8b949e&currStreakNum=c9d1d9&sideNums=c9d1d9" />

</div>

---

## `$ ping ezeibarra888`

<div align="center">

[![](https://img.shields.io/badge/Portfolio-0d1117?style=for-the-badge&logo=firefoxbrowser&logoColor=00ff9c)](https://ezeibarra888.github.io/portfolio/)
[![](https://img.shields.io/badge/LinkedIn-0d1117?style=for-the-badge&logo=linkedin&logoColor=00ff9c)](https://www.linkedin.com/in/ezequiel-ybarra-bba3a6375/)
[![](https://img.shields.io/badge/Email-0d1117?style=for-the-badge&logo=gmail&logoColor=00ff9c)](mailto:ezeibarra888@gmail.com)
[![](https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=00ff9c)](https://github.com/ezeibarra888)

</div>

---

<div align="center">

```
[ sesion finalizada ]  ·  no dejes puertos abiertos  ·  _
```

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:000000,50:0d1117,100:000000&height=90&section=footer&text=exit%200&fontSize=28&fontColor=00ff9c&fontAlignY=55" width="100%" />

</div>
