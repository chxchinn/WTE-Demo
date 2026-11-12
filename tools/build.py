# -*- coding: utf-8 -*-
import re, json, sys, os, time
VER = str(int(time.time()))
sys.path.insert(0, os.path.dirname(__file__))
from content import T

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# people keep their Thai names in every language
for i in range(1, 8):
    th = T[f"p.n{i}"][0]
    T[f"p.n{i}"] = (th, th, th)

ICON_ENERGY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/></svg>'
ICON_FUEL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>'
ICON_ENG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
ICON_SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.900 4.900l1.400 1.400M17.700 17.700l1.400 1.400M2 12h2M20 12h2M4.900 19.100l1.400-1.400M17.700 6.300l1.400-1.400"/></svg>'
ICON_PLUG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8ZM12 18v4"/></svg>'
ICON_BATT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="18" height="10" rx="2"/><path d="M22 11v2M6 11v2M10 11v2"/></svg>'
ICON_WATER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11Z"/><path d="M9 15a3 3 0 0 0 3 3"/></svg>'
ICON_NET = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 10v11M8 21h8"/><circle cx="12" cy="8" r="2"/><path d="M7.8 3.8a6 6 0 0 0 0 8.4M16.2 3.8a6 6 0 0 1 0 8.4M5 1.5a9.5 9.5 0 0 0 0 13M19 1.5a9.5 9.5 0 0 1 0 13"/></svg>'
ICON_DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6Z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>'

def i(key, tag="span", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-i18n="{key}"{extra}></{tag}>'

NAV = [("index.html", "nav.home"), ("about.html", "nav.about"), ("business.html", "nav.business"), ("projects.html", "nav.projects"),
       ("sustainability.html", "nav.sus"), ("investors.html", "nav.inv"), ("news.html", "nav.news")]

def nav(active):
    links = "".join(f'<a href="{h}"{" class=active aria-current=page" if h == active else ""} data-i18n="{k}"></a>' for h, k in NAV)
    return f'''<header class="nav" id="nav"><div class="container nav-in">
<a class="brand" href="index.html" aria-label="WTE Corporation"><img src="assets/img/logo.png" alt="WTE Corporation" width="94" height="46"></a>
<nav class="menu" id="menu" aria-label="Main">{links}<a class="menu-contact" href="contact.html" data-i18n="nav.contact"></a></nav>
<div class="nav-tools"><a class="btn btn-cta" href="contact.html" data-i18n="nav.contact"></a><div class="lang" role="group" aria-label="Language">
<button type="button" data-lang="th" aria-pressed="true">ไทย</button><button type="button" data-lang="en" aria-pressed="false">EN</button><button type="button" data-lang="zh" aria-pressed="false">中文</button></div>
<button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button></div>
</div></header>'''

FOOT = '''<footer class="footer"><div class="container">
<div class="cols">
<div><a class="logo-tile" href="index.html"><img src="assets/img/logo.png" alt="WTE Corporation" width="106" height="52"></a>
<p style="margin-top:18px;max-width:320px" data-i18n="f.tag"></p></div>
<div><h4 data-i18n="f.nav"></h4><ul>
<li><a href="index.html" data-i18n="nav.home"></a></li><li><a href="about.html" data-i18n="nav.about"></a></li><li><a href="projects.html" data-i18n="nav.projects"></a></li><li><a href="sustainability.html" data-i18n="nav.sus"></a></li><li><a href="investors.html" data-i18n="nav.inv"></a></li><li><a href="news.html" data-i18n="nav.news"></a></li><li><a href="contact.html" data-i18n="nav.contact"></a></li></ul></div>
<div><h4 data-i18n="f.biz"></h4><ul>
<li><a href="business.html#energy" data-i18n="b.nav1"></a></li><li><a href="business.html#fuel" data-i18n="b.nav2"></a></li><li><a href="business.html#plastic" data-i18n="b.nav3"></a></li><li><a href="business.html#engineering" data-i18n="b.nav4"></a></li></ul></div>
<div><h4 data-i18n="f.contact"></h4><ul>
<li><a href="tel:020775504">02-077-5504</a> · <a href="tel:0828326244">082-832-6244</a></li>
<li><a href="mailto:info@wtecorporation.com">info@wtecorporation.com</a></li>
<li data-i18n="c.office.addr"></li></ul></div>
</div>
<div class="legal"><span>© 2026 <span data-i18n="c.company"></span> <span data-i18n="c.rights"></span></span><span data-i18n="c.regno"></span></div>
</div></footer>'''

def page(fname, meta, active, body):
    return f'''<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-i18n="{meta}"></title>
<meta name="description" content="WTE Corporation — renewable energy, waste-to-energy and EPC engineering in Thailand. บริษัท ดับบลิวทีอี คอร์ปอเรชั่น จำกัด">
<meta name="theme-color" content="#0d2d4d">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v={VER}">
</head>
<body>
<a class="sr" href="#main" data-i18n="nav.skip" style="position:absolute;left:-999px"></a>
{nav(active)}
<main id="main">
{body}
</main>
{FOOT}
<script src="js/i18n.js?v={VER}"></script>
<script src="js/main.js?v={VER}"></script>
</body>
</html>
'''

BC = {"About Us": ("about.html", "nav.about"), "Our Business": ("business.html", "nav.business"), "Our Work": ("projects.html", "nav.projects"),
      "Sustainability": ("sustainability.html", "nav.sus"), "Investor Relations": ("investors.html", "nav.inv"),
      "News": ("news.html", "nav.news"), "Contact": ("contact.html", "nav.contact")}

def page_hero(h1, sub, kicker, crumbs=None):
    bc = BC[kicker]
    mid = crumbs or f'<span data-i18n="{bc[1]}"></span>'
    return f'''<section class="page-hero"><div class="orb o1"></div><div class="container">
<nav class="crumbs" aria-label="Breadcrumb"><a href="index.html" data-i18n="bc.home"></a><span>/</span>{mid}</nav>
<span class="kicker">{kicker}</span><h1 data-i18n="{h1}" class="reveal"></h1><p data-i18n="{sub}" class="reveal d1"></p></div></section>'''

def cta():
    return '''<section class="cta-band"><div class="container cta-in">
<div><h2 data-i18n="h.cta.h"></h2><p data-i18n="h.cta.p"></p></div>
<a class="btn btn-cta" href="contact.html" data-i18n="c.contactus"></a></div></section>'''

def timeline():
    rows = "".join(f'<div class="tl reveal"><div class="y" data-i18n="ms.y{n}"></div><h3 data-i18n="ms.{n}h"></h3><p data-i18n="ms.{n}p"></p></div>' for n in (1, 2, 3))
    return f'''<section class="pad"><div class="container"><span class="kicker">Company Milestone</span>
<h2 class="display" data-i18n="h.ms.h"></h2><div class="timeline">{rows}</div></div></section>'''


def docs():
    rows = "".join(f'<li class="doc reveal"><span class="di">{ICON_DOC}</span><span class="dt" data-i18n="d.{n}"></span><span class="ds" data-i18n="d.soon"></span></li>' for n in (1, 2, 3))
    return f'<ul class="docs">{rows}</ul>'

# ================= HOME =================
def tile(cls, icon, h, items, href, fact):
    lis = "".join(f'<li data-i18n="{k}"></li>' for k in items)
    return f'''<a class="tile {cls} reveal" href="{href}"><span class="ico">{icon}</span><h3 data-i18n="{h}"></h3><p class="fact" data-i18n="{fact}"></p><ul>{lis}</ul><span class="more arrow" data-i18n="c.more"></span> </a>'''

home = f'''
<section class="hero">
<div class="orb o1"></div><div class="orb o2"></div>
<div class="container">
<div><h1 data-i18n="h.h1" style="margin-top:0"></h1>
<p class="sub" data-i18n="c.slogan"></p>
<div class="actions"><a class="btn btn-cta arrow" href="business.html" data-i18n="h.cta1"></a><a class="btn btn-ghost" href="projects.html" data-i18n="h.cta.btn2"></a></div></div>
</div></section>

<section class="container stats-wrap"><div class="stats">
<div class="stat reveal"><b data-i18n="s.1"></b><span data-i18n="s.1l"></span></div>
<div class="stat reveal d1"><b>10+</b><span data-i18n="s.2l"></span></div>
<div class="stat reveal d2"><b>20+</b><span data-i18n="s.3l"></span></div>
<div class="stat reveal d3"><b>3</b><span data-i18n="s.4l"></span></div>
</div></section>

<section class="pad svc-sec"><div class="container">
<div class="section-head"><div><span class="kicker">Our Services</span><h2 class="display" data-i18n="h.svc.h"></h2></div><p class="lead" style="margin:0" data-i18n="h.svc.p"></p></div>
<div class="svc-list">
<article class="svc reveal"><div class="svc-head"><span class="svc-no">01</span><span class="svc-ico g">{ICON_SUN}</span><h3 data-i18n="a.g1"></h3></div>
<ul class="svc-subs">
<li><a href="business.html#fuel"><span data-i18n="a.g1.1"></span><i aria-hidden="true">→</i></a></li>
<li><a href="business.html#fuel"><span data-i18n="a.g1.2"></span><i aria-hidden="true">→</i></a></li>
<li><a href="business.html#plastic"><span data-i18n="a.g1.3"></span><i aria-hidden="true">→</i></a></li>
<li><a href="business.html#energy"><span data-i18n="a.g1.4"></span><i aria-hidden="true">→</i></a></li>
<li><a href="business.html#energy"><span data-i18n="a.g1.5"></span><i aria-hidden="true">→</i></a></li>
</ul></article>
<article class="svc reveal"><div class="svc-head"><span class="svc-no">02</span><span class="svc-ico b">{ICON_WATER}</span><h3 data-i18n="a.g2"></h3></div>
<div class="svc-subs svc-empty"><a class="more arrow" href="contact.html" data-i18n="svc.ask"></a></div></article>
<article class="svc reveal"><div class="svc-head"><span class="svc-no">03</span><span class="svc-ico o">{ICON_NET}</span><h3 data-i18n="a.g3"></h3></div>
<div class="svc-subs svc-empty"><a class="more arrow" href="contact.html" data-i18n="svc.ask"></a></div></article>
</div></div></section>

<section class="pad"><div class="container"><div class="split">
<div class="duo"><div class="sec-title"><span class="kicker">Our Story</span>
<h2 class="display reveal" data-i18n="h.about.h"></h2></div>
<div class="sec-body"><p class="lead reveal d1" data-i18n="h.w2e.p"></p>
<ul class="checks reveal d2"><li data-i18n="h.w2e.1"></li><li data-i18n="h.w2e.2"></li><li data-i18n="h.w2e.3"></li></ul>
<p style="margin-top:32px" class="reveal d3"><a class="btn btn-line arrow" href="about.html" data-i18n="nav.about"></a></p></div></div>
</div></div></section>


<section class="pad"><div class="container">
<div class="section-head"><div><span class="kicker">Feature Stories</span><h2 class="display" data-i18n="h.st.h"></h2></div><p class="lead" style="margin:0" data-i18n="h.st.p"></p></div>
<div class="grid-3">
<a class="card story reveal" href="business.html#fuel"><span class="num">01</span><h3 data-i18n="st.1h"></h3><p data-i18n="st.1p"></p><span class="more arrow" data-i18n="c.read"></span></a>
<a class="card story reveal d1" href="business.html#fuel"><span class="num">02</span><h3 data-i18n="st.2h"></h3><p data-i18n="st.2p"></p><span class="more arrow" data-i18n="c.read"></span></a>
<a class="card story reveal d2" href="business.html#energy"><span class="num">03</span><h3 data-i18n="st.3h"></h3><p data-i18n="st.3p"></p><span class="more arrow" data-i18n="c.read"></span></a>
</div></div></section>

<section class="pad dark-sec on-dark"><div class="container">
<span class="kicker">Our Goals</span><h2 class="display" data-i18n="h.goal.h"></h2>
<div class="goals">
<div class="goal reveal"><div class="yr">3<small data-i18n="h.goal.y"></small></div><p data-i18n="h.goal.1"></p></div>
<div class="goal reveal d1"><div class="yr">5<small data-i18n="h.goal.y"></small></div><p data-i18n="h.goal.2"></p></div>
</div></div></section>

{timeline()}

<section class="pad soft"><div class="container"><div class="grid-2" style="gap:48px;align-items:start">
<div><span class="kicker">Latest News</span><h2 class="display" data-i18n="h.news.h"></h2>
<a class="news-card reveal" href="news.html" style="margin-top:32px"><div class="body"><div class="meta"><b data-i18n="n.tag"></b><time datetime="2023-02-06" data-i18n="n.date"></time></div><h3 data-i18n="n.title" style="font-size:22px"></h3><span class="more arrow" style="margin-top:20px;font-weight:600;color:var(--green-d)" data-i18n="c.all"></span></div></a></div>
<div><span class="kicker">Key Documents</span><h2 class="display" data-i18n="h.doc.h"></h2><div style="margin-top:32px">{docs()}</div></div>
</div></div></section>
{cta()}
'''

def _n(k, cls=""): return f'<div class="onode {cls}" data-i18n="{k}"></div>'
cmt = "".join(_n(f"g.o.c{n}", "cm") for n in range(1, 5))
stf = "".join(_n(f"g.o.s{n}", "st") for n in range(1, 5))
dep = {1: 3, 2: 3, 3: 3, 4: 3, 5: 2}
cols = "".join(f'''<div class="ocol"><div class="onode dv d{n}" data-i18n="g.d{n}"></div><ul>{"".join(f'<li data-i18n="g.d{n}.{m}"></li>' for m in range(1, dep[n] + 1))}</ul></div>''' for n in range(1, 6))
ORG = f'''<div class="org reveal" role="group" aria-labelledby="org-h">
<div class="olevel">{_n("g.o.board", "top")}</div>
<div class="olevel wrap">{cmt}</div>
<div class="olevel">{_n("g.o.ceo", "top ceo")}</div>
<div class="olevel wrap">{stf}</div>
<div class="ocols">{cols}</div></div>'''


# ================= ABOUT =================
def _p(n, tag, cls=""):
    return f'''<div class="pnode {cls}"><small>{tag}</small><h3 data-i18n="p.n{n}"></h3><p data-i18n="p.r{n}"></p></div>'''
people = f'''<div class="ptree reveal">
<div class="olevel">{_p(1, "EXECUTIVE CHAIRMAN", "top")}</div>
<div class="olevel">{_p(2, "CEO", "ceo")}</div>
<div class="olevel pcols">{_p(3, "COO")}{_p(4, "CSO")}{_p(5, "CCSO")}{_p(6, "CFO")}{_p(7, "CBO")}</div></div>'''

grp1 = "".join(f'<li data-i18n="a.g1.{n}"></li>' for n in range(1, 6))
about = f'''
{page_hero("a.h1", "a.sub", "About Us")}
<section class="pad"><div class="container"><div class="split">
<div class="duo"><div class="sec-title"><span class="kicker">Our Story</span><h2 class="display reveal" data-i18n="a.story.h"></h2></div>
<div class="sec-body"><p class="lead reveal d1" data-i18n="a.story.p1"></p><p class="lead reveal d2" data-i18n="a.story.p2"></p></div></div>
</div></div></section>

<section class="pad soft"><div class="container">
<h2 class="display" data-i18n="a.groups.h"></h2>
<div class="grid-3" style="margin-top:48px">
<div class="card reveal"><span class="num">01</span><h3 data-i18n="a.g1"></h3><ul class="checks" style="margin-top:20px;gap:10px;font-size:15px;color:var(--muted)">{grp1}</ul></div>
<div class="card reveal d1"><span class="num">02</span><h3 data-i18n="a.g2"></h3></div>
<div class="card reveal d2"><span class="num">03</span><h3 data-i18n="a.g3"></h3></div>
</div></div></section>

<section class="pad"><div class="container">
<span class="kicker">Leadership</span><h2 class="display" data-i18n="a.team.h"></h2>
{people}</div></section>

<section class="pad soft"><div class="container">
<span class="kicker">Structure</span><h2 class="display" data-i18n="g.org.h"></h2><p class="lead" data-i18n="g.org.p"></p>
{ORG}</div></section>
{timeline()}
{cta()}
'''

# ================= BUSINESS =================
solar = "".join(f'''<div class="card reveal d{n-1}"><span class="num" data-i18n="sol.{n}"></span><h3 data-i18n="sol.{n}h"></h3><p data-i18n="sol.{n}p"></p></div>''' for n in (1, 2, 3))
leds = "".join(f'<li data-i18n="led.{n}"></li>' for n in range(1, 6))
crops = "".join(f'<div class="card reveal d{n-1}"><h3 data-i18n="crop.{n}"></h3><p data-i18n="crop.{n}p"></p></div>' for n in (1, 2, 3))
steps = "".join(f'<li data-i18n="py.{n}"></li>' for n in range(1, 5))
uses = "".join(f'<li data-i18n="use.{n}"></li>' for n in range(1, 6))
epc = "".join(f'<div class="card reveal d{n-1}"><span class="num">0{n}</span><h3 data-i18n="b4.{n}"></h3></div>' for n in (1, 2, 3, 4))
business = f'''
{page_hero("b.h1", "b.sub", "Our Business")}
<div class="subnav"><div class="container" id="subnav">
<a href="#energy" data-i18n="b.nav1"></a><a href="#fuel" data-i18n="b.nav2"></a><a href="#plastic" data-i18n="b.nav3"></a><a href="#engineering" data-i18n="b.nav4"></a></div></div>

<section class="pad biz" id="energy"><div class="container">
<span class="kicker">Renewable Energy</span><h2 class="display" data-i18n="b1.h"></h2>
<p style="margin-top:20px"><a class="btn btn-line arrow" href="projects-energy.html" data-i18n="c.viewwork"></a></p>
<div class="split sub-block"><div><h3 data-i18n="b1.msw.h"></h3><p class="lead" data-i18n="b1.msw.p"></p></div>
</div>
<div class="sub-block"><h3 data-i18n="b1.solar.h"></h3><p class="lead" style="margin:0 0 28px" data-i18n="b1.solar.p"></p>
<div class="grid-3">{solar}</div></div>
<div class="split flip sub-block"><div><h3 data-i18n="b1.led.h"></h3><p class="lead" style="margin-top:0" data-i18n="b1.led.p"></p><ul class="checks">{leds}</ul></div>
</div>
</div></section>

<section class="pad soft biz" id="fuel"><div class="container">
<span class="kicker">Fuel</span><h2 class="display" data-i18n="b2.h"></h2><p class="lead" data-i18n="b2.p"></p>
<p style="margin-top:20px"><a class="btn btn-line arrow" href="projects-fuel.html" data-i18n="c.viewwork"></a></p>
<div class="sub-block"><h3 data-i18n="b2.crop.h"></h3><p class="lead" style="margin:0 0 28px" data-i18n="b2.crop.p"></p><div class="grid-3">{crops}</div></div>
<div class="split sub-block"><div><h3 data-i18n="b2.rdf.h"></h3><p class="lead" style="margin-top:0" data-i18n="b2.rdf.p"></p></div>
</div>
<div class="sub-block"><h3 data-i18n="b2.py.h"></h3><ol class="steps" style="max-width:760px">{steps}</ol></div>
</div></section>

<section class="pad biz" id="plastic"><div class="container">
<span class="kicker">Recycling</span><h2 class="display" data-i18n="b3.h"></h2><p class="lead" data-i18n="b3.p"></p>
<p style="margin-top:20px"><a class="btn btn-line arrow" href="projects-recycling.html" data-i18n="c.viewwork"></a></p>
<p class="lead" style="margin-top:36px;color:var(--ink);font-weight:600" data-i18n="b3.use"></p>
<ul class="pill-tags">{uses}</ul></div></section>

<section class="pad dark-sec on-dark biz" id="engineering"><div class="container">
<span class="kicker">Engineering</span><h2 class="display" data-i18n="b4.h"></h2>
<p class="lead" data-i18n="b4.p1"></p><p class="lead" data-i18n="b4.p2"></p>
<p style="margin-top:24px"><a class="btn btn-ghost arrow" href="projects-engineering.html" data-i18n="c.viewwork"></a></p>
<div class="grid-4" style="margin-top:48px">{epc}</div></div></section>
{cta()}
'''

pill3 = "".join(f'<div class="card reveal d{n-1}"><span class="num">0{n}</span><h3 data-i18n="g.p{n}"></h3></div>' for n in (1, 2, 3))
pol = "".join(f'<li data-i18n="g.pol{n}"></li>' for n in (1, 2, 3))
sustain = f'''
{page_hero("s.h1", "s.sub", "Sustainability")}
<section class="pad"><div class="container">
<span class="kicker">CSR</span><h2 class="display" data-i18n="g.csr.h"></h2><p class="lead" data-i18n="g.csr.p"></p>
<p style="margin-top:40px;font-weight:600" data-i18n="g.csr.sub"></p>
<div class="grid-3" style="margin-top:20px">{pill3}</div></div></section>

<section class="pad soft"><div class="container"><div class="split">
<div class="duo"><div class="sec-title"><span class="kicker">Sustainability</span><h2 class="display reveal" data-i18n="g.sus.h"></h2></div>
<div class="sec-body"><p class="lead reveal d1" data-i18n="g.sus.p"></p></div></div>
</div>
<p class="lead" style="margin-top:56px" data-i18n="g.pol.p"></p><ul class="pill-tags">{pol}</ul></div></section>
{cta()}
'''

cm4 = "".join(f'<div class="card reveal d{n-1}"><span class="num">0{n}</span><h3 data-i18n="g.o.c{n}"></h3></div>' for n in (1, 2, 3, 4))
investors = f'''
{page_hero("i.h1", "i.sub", "Investor Relations")}
<section class="pad"><div class="container">
<span class="kicker">Overview</span><h2 class="display" data-i18n="g.ir.h"></h2><p class="lead" data-i18n="g.ir.p"></p>
<div class="grid-3" style="margin-top:48px">
<div class="card reveal"><span class="ico">{ICON_PLUG}</span><span class="num" data-i18n="g.ir.1"></span><h3 data-i18n="g.ir.1p"></h3></div>
<div class="card reveal d1"><span class="ico">{ICON_BATT}</span><span class="num" data-i18n="g.ir.2"></span><h3 data-i18n="g.ir.2p"></h3></div>
<div class="card reveal d2"><span class="ico">{ICON_DOC}</span><span class="num" data-i18n="g.ir.3"></span><h3 data-i18n="g.ir.3p"></h3></div>
</div></div></section>

<section class="pad soft"><div class="container">
<span class="kicker">Governance</span><h2 class="display" data-i18n="i.gov.h"></h2><p class="lead" data-i18n="i.gov.p"></p>
<div class="grid-4" style="margin-top:48px">{cm4}</div></div></section>

<section class="pad"><div class="container">
<span class="kicker">Documents</span><h2 class="display" data-i18n="h.doc.h"></h2><p class="lead" data-i18n="i.doc.p"></p>
<div style="margin-top:40px;max-width:820px">{docs()}</div>
<p style="margin-top:36px;color:var(--muted)"><span data-i18n="g.ir.note"></span> <a href="mailto:info@wtecorporation.com" style="color:var(--green-d);font-weight:600">info@wtecorporation.com</a></p>
</div></section>
{cta()}
'''


# ================= PROJECTS =================
ICON_LEAF = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 19C5 10 11 4 20 4c0 9-6 15-15 15Z"/><path d="M5 19c3-5 6-8 11-11"/></svg>'
ICON_COG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.2"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M18.4 5.6l-1.8 1.8M7.4 16.6l-1.8 1.8"/></svg>'
ICON_LOOP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h8a4 4 0 0 1 3.5 6M17 17H9a4 4 0 0 1-3.5-6"/><path d="M14 4l3 3-3 3M10 20l-3-3 3-3"/></svg>'
ICON_IMG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="1.8"/><path d="M21 16l-5-5-8 9"/></svg>'

def ph(extra=""):
    return f'<div class="imgph {extra}"><span class="imgph-ico">{ICON_IMG}</span><small data-i18n="pj.ph"></small></div>'

cards = [("rdf", "pj.frdf", "pj.c1", "projects-fuel.html"), ("epcm", "pj.fepcm", "pj.c2", "projects-engineering.html"),
         ("rec", "pj.frec", "pj.c3", "projects-recycling.html"), ("rdf", "pj.frdf", "pj.c4", "projects-fuel.html"),
         ("epcm", "pj.fepcm", "pj.c5", "projects-engineering.html"), ("rec", "pj.frec", "pj.c6", "projects-recycling.html")]
pcards = "".join(f'''<a class="pcard reveal" data-cat="{cat}" href="{href}">{ph("sm")}<div class="pbody"><span class="pcat" data-i18n="{ck}"></span><h3 data-i18n="{tk}"></h3><span class="more arrow" data-i18n="c.more"></span></div></a>''' for cat, ck, tk, href in cards)

projects = f'''
{page_hero("pj.h1", "pj.sub", "Our Work")}
<section class="pad" style="padding-bottom:0"><div class="container">
<span class="kicker">Featured Concept</span><h2 class="display" data-i18n="pj.feat.h"></h2>
<div class="feature reveal">{ph("lg")}
<div class="fpanel"><span class="ftag">RDF</span><h3 data-i18n="pj.feat.t"></h3><p data-i18n="pj.feat.s"></p>
<ul class="frows"><li><span>{ICON_LEAF}</span><b data-i18n="pj.f1"></b></li><li><span>{ICON_COG}</span><b data-i18n="pj.f2"></b></li><li><span>{ICON_LOOP}</span><b data-i18n="pj.f3"></b></li></ul>
<a class="btn btn-cta" href="projects-fuel.html" data-i18n="c.viewwork"></a></div></div>
</div></section>

<section class="pad"><div class="container">
<div class="section-head" style="margin-bottom:28px"><div><span class="kicker">Explore Our Work</span><h2 class="display" data-i18n="pj.exp.h"></h2><p class="lead" style="margin-top:12px" data-i18n="pj.exp.p"></p></div>
<div class="chips" role="group" aria-label="Filter">
<button type="button" class="chip on" data-filter="all" data-i18n="pj.fall"></button><button type="button" class="chip" data-filter="rdf" data-i18n="pj.frdf"></button>
<button type="button" class="chip" data-filter="epcm" data-i18n="pj.fepcm"></button><button type="button" class="chip" data-filter="rec" data-i18n="pj.frec"></button></div></div>
<p class="pnote" data-i18n="pj.note"></p>
<div class="grid-3" id="pgrid">{pcards}</div></div></section>
{cta()}
'''


# ================= PER-SERVICE PROJECT PAGES =================
import json as _json
_pf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "projects.json")
PROJECTS = _json.load(open(_pf, encoding="utf8")) if os.path.exists(_pf) else []
for _p in PROJECTS:
    for _f in ("title", "location", "summary"):
        T[f"proj.{_p['id']}.{_f}"] = tuple(_p.get(l, {}).get(_f, _p.get("th", {}).get(_f, "")) for l in ("th", "en", "zh"))

SERVICES = [("energy", "b.nav1", "t1.f", "business.html#energy"), ("fuel", "b.nav2", "t2.f", "business.html#fuel"),
            ("recycling", "b.nav3", "b3.use", "business.html#plastic"), ("engineering", "b.nav4", "t3.f", "business.html#engineering")]
for _k, _nk, _fk, _link in SERVICES:
    _h = T[f"pj.s.{_k}.h"]
    T[f"meta.pj.{_k}"] = tuple(re.sub(r"</?em>", "", _h[i]) + " | WTE Corporation" for i in range(3))

def project_card(p):
    img = f'<img src="{p["image"]}" alt="" loading="lazy" style="width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:16px">' if p.get("image") else ph("sm")
    meta = p.get("year", "")
    meta_html = f'<span class="pnote" style="margin:0">{meta}</span>' if meta else ""
    loc = f'<span class="pcat" data-i18n="proj.{p["id"]}.location"></span>' if p.get("th", {}).get("location") else ""
    return (f'<article class="pcard reveal">{img}<div class="pbody">{loc}<h3 data-i18n="proj.{p["id"]}.title"></h3>'
            f'<p style="color:var(--muted);font-size:15px" data-i18n="proj.{p["id"]}.summary"></p>{meta_html}</div></article>')

def service_page(k, nk, fk, link):
    mine = [p for p in PROJECTS if p.get("service") == k]
    if mine:
        grid = f'<div class="grid-3">{"".join(project_card(p) for p in mine)}</div>'
    else:
        grid = f'''<div class="empty reveal"><span class="imgph-ico">{ICON_IMG}</span><h3 data-i18n="pj.empty.h"></h3><p data-i18n="pj.empty.p"></p>
<a class="btn btn-cta" href="contact.html" data-i18n="c.contactus"></a></div>'''
    others = "".join(f'<a class="card reveal" href="projects-{ok}.html"><span class="num" data-i18n="pj.other"></span><h3 data-i18n="{onk}"></h3><span class="more arrow" style="margin-top:14px;display:inline-flex;gap:8px;font-weight:600;color:var(--green-d)" data-i18n="c.viewwork"></span></a>' for ok, onk, _a, _b in SERVICES if ok != k)
    crumbs = f'<a href="projects.html" data-i18n="nav.projects"></a><span>/</span><span data-i18n="{nk}"></span>'
    hero = page_hero(f"pj.s.{k}.h", f"pj.s.{k}.p", "Our Work", crumbs)
    body = f'''{hero}
<section class="pad"><div class="container">
<div class="section-head" style="margin-bottom:32px"><div><span class="kicker">Projects</span><h2 class="display" data-i18n="pj.list"></h2></div>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-line" href="{link}" data-i18n="pj.svc"></a><a class="btn btn-line" href="projects.html" data-i18n="pj.back"></a></div></div>
{grid}</div></section>
<section class="pad soft"><div class="container"><h2 class="display" style="font-size:clamp(24px,3vw,34px)" data-i18n="pj.other"></h2>
<div class="grid-3" style="margin-top:32px">{others}</div></div></section>
{cta()}
'''
    return (f"projects-{k}.html", f"meta.pj.{k}", "projects.html", body)

SERVICE_PAGES = [service_page(*s_) for s_ in SERVICES]

# ================= NEWS =================
news = f'''
{page_hero("n.h1", "n.sub", "News")}
<section class="pad"><div class="container">
<article class="news-card reveal">
<div class="body"><div class="meta"><b data-i18n="n.tag"></b><time datetime="2023-02-06" data-i18n="n.date"></time></div>
<h3 data-i18n="n.title"></h3></div></article>
</div></section>
{cta()}
'''

# ================= CONTACT =================
contact = f'''
{page_hero("ct.h1", "ct.sub", "Contact")}
<section class="pad"><div class="container"><div class="contact-grid">
<div><span class="kicker">WTE Corporation</span><h2 class="display" data-i18n="ct.info"></h2>
<div class="info-list">
<div><h4 data-i18n="c.company"></h4><p data-i18n="c.regno"></p></div>
<div><h4 data-i18n="c.hq"></h4><p data-i18n="c.hq.addr"></p></div>
<div><h4 data-i18n="c.office"></h4><p data-i18n="c.office.addr"></p>
<p style="margin-top:8px"><a class="arrow" style="color:var(--green-d);font-weight:600" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query=77%2F5+Ramintra+40+Bueng+Kum+Bangkok+10230" data-i18n="ct.map"></a></p></div>
<div><h4 data-i18n="c.phone"></h4><p><a href="tel:020775504">02-077-5504</a><br><a href="tel:0828326244">082-832-6244</a></p></div>
<div><h4 data-i18n="c.email"></h4><p><a href="mailto:info@wtecorporation.com">info@wtecorporation.com</a><br><a href="mailto:wte.corporation@gmail.com">wte.corporation@gmail.com</a></p></div>
<div><h4 data-i18n="ct.join"></h4><p data-i18n="ct.join.p"></p></div>
</div></div>
<form class="form reveal" id="contact-form" novalidate>
<h3 style="font-size:24px;margin-bottom:24px" data-i18n="ct.form.h"></h3>
<div class="row2"><div class="field"><label for="f-name" data-i18n="ct.name"></label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-email" data-i18n="ct.email"></label><input id="f-email" name="email" type="email" autocomplete="email" required></div></div>
<div class="row2"><div class="field"><label for="f-phone" data-i18n="ct.phone"></label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
<div class="field"><label for="f-subject" data-i18n="ct.subject"></label><input id="f-subject" name="subject"></div></div>
<div class="field"><label for="f-msg" data-i18n="ct.msg"></label><textarea id="f-msg" name="message" required></textarea></div>
<button class="btn btn-cta" type="submit" data-i18n="ct.send"></button>
<p class="form-note" data-i18n="ct.note"></p>
</form>
</div></div></section>
'''

PAGES = [
    *SERVICE_PAGES,
    ("index.html", "meta.home", "index.html", home),
    ("about.html", "meta.about", "about.html", about),
    ("business.html", "meta.business", "business.html", business),
    ("projects.html", "meta.proj", "projects.html", projects),
    ("sustainability.html", "meta.sus", "sustainability.html", sustain),
    ("investors.html", "meta.inv", "investors.html", investors),
    ("news.html", "meta.news", "news.html", news),
    ("contact.html", "meta.contact", "contact.html", contact),
]

used = set()
def fill(html):
    # fill Thai text into empty data-i18n elements (SEO / no-JS fallback)
    def rep(m):
        key = m.group(3)
        used.add(key)
        return f'{m.group(1)}{T[key][0]}{m.group(4)}'
    html = re.sub(r'(<(\w+)[^>]*data-i18n="([^"]+)"[^>]*>)(</\2>)', rep, html)
    def rep_alt(m):
        used.add(m.group(1)); return f'alt="{T[m.group(1)][0]}"'
    html = re.sub(r'data-i18n-alt="([^"]+)" alt=""', lambda m: f'data-i18n-alt="{m.group(1)}" alt="{T[m.group(1)][0]}"', html)
    return html

for fname, meta, active, body in PAGES:
    html = fill(page(fname, meta, active, body))
    open(f"{OUT}/{fname}", "w", encoding="utf8").write(html)

# i18n.js — Thai is the HTML default, so the dictionary only carries EN and ZH
dic = {"en": {k: v[1] for k, v in T.items()}, "zh": {k: v[2] for k, v in T.items()}}
open(f"{OUT}/js/i18n.js", "w", encoding="utf8").write(
    "/* Generated copy for EN / ZH. Thai lives in the HTML. */\nwindow.WTE_I18N = " + json.dumps(dic, ensure_ascii=False, indent=1) + ";\n")

# favicon
open(f"{OUT}/assets/img/favicon.svg", "w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1e5fae"/><stop offset=".6" stop-color="#2f9e44"/><stop offset="1" stop-color="#f26a21"/></linearGradient></defs><rect width="64" height="64" rx="16" fill="url(#g)"/><path d="M12 20l8 26 8-18 8 18 8-26" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>''')

unused = set(T) - used
print("keys:", len(T), "used:", len(used), "unused:", sorted(unused))
