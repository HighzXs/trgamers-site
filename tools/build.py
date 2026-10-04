"""Gera as páginas estáticas do site (header/footer compartilhados).
Uso: python tools/build.py   (rodar na raiz do projeto; o serve.py faz isso sozinho)
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://trgamersinformatica.com.br"
MAPS = "https://maps.app.goo.gl/6mG3vqccFq88WbRX6"
MAPS_EMBED = "https://www.google.com/maps?q=R.+Salima+Mussi+Pedro,+3098,+Franca+-+SP,+14403-664&output=embed"
WA = "https://wa.me/5516992076444"
WA_MSG = "Oi, tudo bem? Vim pelo site da TR Gamers e gostaria de fazer um orçamento."


def ico(name, cls=""):
    return f'<svg class="ico {cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


ICON_WA = '<svg aria-hidden="true"><use href="#i-wa"/></svg>'
SPRITE = '''<svg class="sprite" width="0" height="0" aria-hidden="true">
  <symbol id="i-wa" viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.8.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.4-2.3-1.4-.8-.7-1.4-1.6-1.6-1.9-.2-.3 0-.4.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15L2 22l5.1-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/></symbol>
  <symbol id="i-pc" viewBox="0 0 24 24"><rect x="7" y="3" width="10" height="18" rx="2"/><circle cx="12" cy="8" r="1.5"/><path d="M10 16h4"/></symbol>
  <symbol id="i-up" viewBox="0 0 24 24"><path d="M12 19V5M5 12l7-7 7 7"/></symbol>
  <symbol id="i-tool" viewBox="0 0 24 24"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.1L3 17.7 6.3 21l6.3-6.3a4 4 0 0 0 5.1-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/></symbol>
  <symbol id="i-laptop" viewBox="0 0 24 24"><rect x="4" y="5" width="16" height="11" rx="1"/><path d="M2 19h20"/></symbol>
  <symbol id="i-fan" viewBox="0 0 24 24"><circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 1-6 3-6s2 3-3 6zM14 12c4 0 6 1 6 3s-3 2-6-3zM12 14c0 4-1 6-3 6s-2-3 3-6zM10 12c-4 0-6-1-6-3s3-2 6 3z"/></symbol>
  <symbol id="i-cpu" viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></symbol>
  <symbol id="i-ram" viewBox="0 0 24 24"><rect x="2" y="8" width="20" height="8" rx="1"/><path d="M6 16v2M10 16v2M14 16v2M18 16v2M6 12h2M11 12h2M16 12h2"/></symbol>
  <symbol id="i-mouse" viewBox="0 0 24 24"><rect x="7" y="3" width="10" height="18" rx="5"/><path d="M12 7v4"/></symbol>
  <symbol id="i-cable" viewBox="0 0 24 24"><path d="M4 9h5v6H4zM15 9h5v6h-5zM9 12h6"/></symbol>
  <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12l4 4 10-10"/></symbol>
  <symbol id="i-truck" viewBox="0 0 24 24"><path d="M2 6h12v10H2zM14 10h4l3 3v3h-7"/><circle cx="6" cy="17" r="1.8"/><circle cx="17" cy="17" r="1.8"/></symbol>
</svg>'''

NAV = [
    ("/montagem/", "PC Gamer"),
    ("/upgrade/", "Upgrade"),
    ("/manutencao/", "Manutenção"),
    ("/notebooks/", "Notebooks"),
    ("/produtos/", "Produtos"),
    ("/sobre/", "Sobre"),
    ("/contato/", "Contato"),
]

PRODUCTS = [  # (nome, ícone, categoria)  ->  README: produtos da loja presencial
    ("Memória RAM HyperX Fury DDR4 8GB", "ram", "Memória"),
    ("Air Cooler CPU Rise Mode Z3 Universal", "cpu", "Refrigeração"),
    ("Mouse Gamer Hayom 6 botões USB LED RGB", "mouse", "Periféricos"),
    ("Kit 3 Fans 120mm LED Verde", "fan", "Refrigeração"),
    ("Kit 2 Fans 120mm LED Azul", "fan", "Refrigeração"),
    ("Fan Rise Mode Wind 120mm LED", "fan", "Refrigeração"),
    ("Cooler de gabinete Rise Mode Wind W1", "fan", "Refrigeração"),
    ("Fan Rise Mode Wind Rainbow", "fan", "Refrigeração"),
    ("Cooler Fan RGB 80mm para gabinete", "fan", "Refrigeração"),
    ("Cabo conversor DisplayPort macho", "cable", "Cabos"),
]
HOME_PRODUCTS = [0, 1, 2, 3]

REVIEWS = [
    ("Hugo Garcia", "Desde o início buscaram equilibrar o melhor orçamento e condições de pagamento. Atendimento muito rápido, montagem rápida e muita competência."),
    ("Heitor P. Marks", "Preços mais do que justos, cumprem o prazo prometido além de buscar e entregar o equipamento. Vou levar novamente para manutenção."),
    ("Ana Luiza F. Ribeiro", "Atenciosos desde a primeira mensagem pelo WhatsApp até os cuidados pós-venda. Muito satisfeita com minha máquina nova!"),
]

HOURS = [(1, "Segunda", "09:00–18:00"), (2, "Terça", "09:00–18:00"), (3, "Quarta", "09:00–18:00"),
         (4, "Quinta", "09:00–18:00"), (5, "Sexta", "09:00–18:00"), (6, "Sábado", "08:00–12:00"), (0, "Domingo", "Fechado")]


def wa(msg=WA_MSG):
    return f'data-wa="{msg}" href="{WA}"'


def header(active):
    cur = ' aria-current="page"'
    links = "\n      ".join('<a href="%s"%s>%s</a>' % (h, cur if h == active else "", t) for h, t in NAV)
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="header">
  <div class="container header__in">
    <a href="/" class="brand" aria-label="TR Gamers Informática - início">
      <img src="/assets/img/logo-mark.webp" alt="" height="36" width="74">
      <span>TR Gamers<small>Informática</small></span>
    </a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false"><span></span></button>
    <nav class="nav" aria-label="Principal">
      {links}
      <a class="btn nav__wa" {wa()}>{ICON_WA}Falar no WhatsApp</a>
      <a class="btn btn--primary btn--sm" href="/monte-seu-pc/">Monte seu PC</a>
    </nav>
  </div>
</header>'''


FOOTER = f'''<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <a href="/" class="brand brand--foot"><img src="/assets/img/logo-mark.webp" alt="" height="36" width="74"><span>TR Gamers<small>Informática</small></span></a>
        <p>Vendas, montagem, manutenção, assistência e acessórios.</p>
      </div>
      <div>
        <h3>Serviços</h3>
        <ul><li><a href="/montagem/">PC Gamer</a></li><li><a href="/upgrade/">Upgrade</a></li><li><a href="/manutencao/">Manutenção</a></li><li><a href="/notebooks/">Notebooks</a></li><li><a href="/produtos/">Produtos</a></li></ul>
      </div>
      <div>
        <h3>Horário</h3>
        <ul><li>Seg–Sex: 09:00–18:00</li><li>Sábado: 08:00–12:00</li><li>Domingo: fechado</li><li><span class="status"></span></li></ul>
      </div>
      <div>
        <h3>Contato</h3>
        <ul>
          <li>R. Salima Mussi Pedro, 3098<br>Franca-SP · 14403-664</li>
          <li><a data-wa href="{WA}">WhatsApp (16) 99207-6444</a></li>
          <li><a href="https://www.instagram.com/trgamersinformatica/" target="_blank" rel="noopener noreferrer">@trgamersinformatica</a></li>
          <li><a href="{MAPS}" target="_blank" rel="noopener noreferrer">Ver no Google Maps</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom"><span>© 2026 TR Gamers Informática</span><span>Orçamentos sem compromisso</span></div>
  </div>
</footer>
<a class="wa-float" {wa()} aria-label="Falar no WhatsApp">{ICON_WA}</a>'''


def page(path, active, title, desc, body, hero_preload=False, noindex=False):
    url = DOMAIN + path
    preload = '<link rel="preload" as="image" href="/assets/img/hero.webp">\n' if hero_preload else ""
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    canon = "" if noindex else f'<link rel="canonical" href="{url}">\n'
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0b0b0c">
{robots}{canon}<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="TR Gamers Informática">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/banner.webp">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
{preload}<script src="/js/boot.js"></script>
<link rel="stylesheet" href="/css/tokens.css">
<link rel="stylesheet" href="/css/base.css">
<link rel="stylesheet" href="/css/layout.css">
<link rel="stylesheet" href="/css/components.css">
<script type="module" src="/js/main.js"></script>
</head>
<body>
{SPRITE}
{header(active)}
<main id="conteudo" tabindex="-1">
{body}
</main>
{FOOTER}
</body>
</html>
'''


# ---------- blocos ----------
def page_hero(crumb, h1, lead, cta_label, msg, extra="", primary=None):
    if primary:
        btns = (f'<a class="btn btn--primary" href="{primary[0]}">{primary[1]}</a>'
                f'<a class="btn" {wa(msg)}>{ICON_WA}{cta_label}</a>')
    else:
        btns = f'<a class="btn btn--primary" {wa(msg)}>{ICON_WA}{cta_label}</a>'
    return f'''  <section class="page-hero">
    <div class="container">
      <p class="crumbs"><a href="/">Início</a> / {crumb}</p>
      <h1>{h1}</h1>
      <p>{lead}</p>
      <div class="hero__cta">
        {btns}{extra}
      </div>
    </div>
  </section>'''


def section(inner, alt=False, sid=""):
    idattr = f' id="{sid}"' if sid else ""
    return f'  <section class="section{" section--alt" if alt else ""}"{idattr}>\n    <div class="container">\n{inner}\n    </div>\n  </section>'


def head(eyebrow, h2, p=""):
    extra = f"<p>{p}</p>" if p else ""
    return f'      <div class="section__head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{extra}</div>'


def cards(items, n=4):
    return f'      <div class="cards cards--{n}">\n' + "\n".join(items) + "\n      </div>"


def link_card(href, icon, title, text, more="Saiba mais →"):
    return f'''        <a class="card reveal" href="{href}">{ico(icon, "ico--red")}<h3>{title}</h3><p>{text}</p><span class="card__more">{more}</span></a>'''


def info_card(title, text, icon=None, num=None):
    top = ico(icon, "ico--red") if icon else (f'<span class="card__n">{num}</span>' if num else "")
    return f'        <div class="card card--hover reveal">{top}<h3>{title}</h3><p>{text}</p></div>'


def product_card(i):
    name, icon, cat = PRODUCTS[i]
    return (f'        <article class="card prod card--hover reveal" data-name="{name}" data-cat="{cat}"><img class="prod__img" src="/assets/img/placeholder.webp" alt="" width="400" height="400" loading="lazy">'
            f'<div class="prod__top">{ico(icon)}<span class="prod__tag">{cat}</span></div><h3>{name}</h3>'
            f'<button type="button" class="btn btn--sm" data-prod="{name}" aria-pressed="false">Adicionar à consulta</button></article>')


def search_block():
    cats = sorted({c for _, _, c in PRODUCTS})
    chips_ = '<label class="chip"><input type="radio" name="cat" value="" checked><span>Todos</span></label>' + "".join(
        f'<label class="chip"><input type="radio" name="cat" value="{c}"><span>{c}</span></label>' for c in cats)
    return f'''      <div class="search" data-search>
        <div class="search__box">
          <svg class="ico search__ico" aria-hidden="true"><use href="#i-search"/></svg>
          <label class="sr-only" for="busca">Buscar produtos</label>
          <input id="busca" type="search" placeholder="Buscar produto (ex.: cooler, memória, mouse)" autocomplete="off" maxlength="60">
          <button type="button" class="search__clear" data-clear-search aria-label="Limpar busca" hidden>×</button>
        </div>
        <div class="chips" role="radiogroup" aria-label="Categoria">{chips_}</div>
        <p class="search__count" data-count aria-live="polite"></p>
      </div>'''


def review_card(name, text):
    return f'''        <figure class="card review reveal"><div class="stars" aria-label="5 estrelas">★★★★★</div><blockquote>“{text}”</blockquote><cite>{name} · avaliação no Google</cite></figure>'''


def checks(items):
    li = "".join(f'<li>{ico("check")}<span>{t}</span></li>' for t in items)
    return f'      <ul class="checks">{li}</ul>'


def cta_band(h2, label="Pedir orçamento no WhatsApp", msg=WA_MSG, primary=None):
    if primary:
        btns = f'<a class="btn btn--primary" href="{primary[0]}">{primary[1]}</a> <a class="btn" {wa(msg)}>{ICON_WA}{label}</a>'
    else:
        btns = f'<a class="btn btn--primary" {wa(msg)}>{ICON_WA}{label}</a>'
    return section(f'''      <div class="cta-final reveal"><h2>{h2}</h2>
      <div class="hero__cta hero__cta--center">{btns}</div></div>''')


def reviews_section(alt=False):
    return section(head("Avaliações", "Quem comprou, recomenda") + cards([review_card(n, t) for n, t in REVIEWS], 3), alt=alt, sid="avaliacoes")


# ---------- campos ----------
def opt(name, value, title, small=""):
    s = f"<small>{small}</small>" if small else ""
    return f'<label class="opt"><input type="radio" name="{name}" value="{value}"><span><b>{title}</b>{s}</span></label>'


def chip(name, value):
    return f'<label class="chip"><input type="checkbox" name="{name}" value="{value}"><span>{value}</span></label>'


def opts(name, items):
    return '<div class="opts">' + "".join(opt(name, *i) if isinstance(i, tuple) else opt(name, i, i) for i in items) + "</div>"


def chips(name, items):
    return '<div class="chips">' + "".join(chip(name, i) for i in items) + "</div>"


def select(name, label, options):
    o = "".join(f'<option value="{x}">{x}</option>' for x in ["Não sei"] + options)
    return f'<div class="field"><label for="{name}">{label}</label><select id="{name}" name="{name}"><option value="">Selecione</option>{o}</select></div>'


def field_text(id_, label, ph="", tag="input"):
    if tag == "textarea":
        return f'<div class="field"><label for="{id_}">{label}</label><textarea id="{id_}" name="{id_}" rows="2" maxlength="400" placeholder="{ph}"></textarea></div>'
    return f'<div class="field"><label for="{id_}">{label}</label><input id="{id_}" name="{id_}" maxlength="60" placeholder="{ph}"{" autocomplete=given-name" if id_ == "nome" else ""}></div>'


def block(n, title, inner, key=""):
    k = f' data-field="{key}"' if key else ""
    return f'        <fieldset class="qform__block"{k}><legend><span class="qform__n">{n}</span>{title}</legend>{inner}</fieldset>'


def qform(kind, required, blocks):
    return f'''      <form class="qform" data-qform="{kind}" data-required="{required}" novalidate>
{chr(10).join(blocks)}
        <div class="qform__send">
          <a class="btn btn--primary" data-send href="#" target="_blank" rel="noopener noreferrer" aria-disabled="true">{ICON_WA}Enviar no WhatsApp</a>
          <p class="note" data-hint aria-live="polite"></p>
        </div>
        <p class="sent" data-sent hidden>Abrimos o WhatsApp com a mensagem pronta. É só apertar enviar lá. Não abriu? <a data-sent-link href="#" target="_blank" rel="noopener noreferrer">Toque aqui</a>.</p>
      </form>'''


def entrega_block(n):
    return block(n, "Como prefere ser atendido?", opts("entrega", [("Vou levar na loja", "Levo na loja"), ("Quero que busquem em casa", "Busquem em casa", "Busca e entrega")])
                 + '<div class="qform__row">' + field_text("nome", "Seu nome (opcional)") + field_text("obs", "Observações (opcional)", "Ex.: tenho pressa, o PC está fora da garantia", "textarea") + "</div>")


def upgrade_form():
    return qform("upgrade", "tipo,orcamento", [
        block(1, "Selecione sua configuração",
              opts("tipo", [("PC montado (gabinete)", "PC montado", "Gabinete com peças separadas"), ("PC de marca", "PC de marca", "Dell, HP, Lenovo, Positivo..."),
                            ("Notebook", "Notebook", "Gamer ou comum"), ("Não sei ao certo", "Não sei ao certo", "A gente identifica juntos")])
              + '<div class="qform__row">' + field_text("cpu", "Processador", "Ex.: Ryzen 5 3600, i5-10400 ou não sei")
              + field_text("gpu", "Placa de vídeo", "Ex.: GTX 1650, RX 580 ou não sei")
              + select("ram", "Memória RAM", ["4 GB", "8 GB", "16 GB", "32 GB ou mais"]) + select("disco", "Armazenamento", ["HD", "SSD", "HD + SSD"]) + "</div>", "tipo"),
        block(2, "O que você quer melhorar?", chips("melhorar", ["Jogar com mais FPS", "Abrir programas mais rápido", "Fazer várias coisas ao mesmo tempo",
                                                                  "Editar vídeo / renderizar", "O PC está lento", "Esquenta ou faz barulho", "Não sei, quero um diagnóstico"])),
        block(3, "Já pensou em trocar alguma peça?", chips("pecas", ["Memória RAM", "SSD", "Placa de vídeo", "Processador", "Cooler e fans", "Fonte", "Gabinete", "Não sei"])),
        block(4, "Qual seria seu orçamento para o upgrade?", opts("orcamento", ["Até R$ 500", "R$ 500 a R$ 1.000", "R$ 1.000 a R$ 2.000", "Acima de R$ 2.000", ("Ainda não sei", "Ainda não sei", "Me ajudem a definir")]), "orcamento"),
        entrega_block(5),
    ])


def manutencao_form():
    return qform("manutencao", "equip,problema", [
        block(1, "Qual equipamento?",
              opts("equip", [("PC montado (gabinete)", "PC montado"), ("PC de marca", "PC de marca"), "Notebook", "Outro"])
              + '<div class="qform__row">' + field_text("modelo", "Marca ou modelo (opcional)", "Ex.: Dell Inspiron, Positivo Master") + "</div>", "equip"),
        block(2, "O que está acontecendo?", chips("problema", ["Não liga", "Está lento", "Trava ou reinicia sozinho", "Tela azul ou erros", "Esquenta ou faz barulho",
                                                              "Precisa formatar", "Vírus ou propagandas", "Tela quebrada", "Não sei explicar"]), "problema"),
        block(3, "Qual a urgência?", opts("urgencia", ["O quanto antes", "Nesta semana", "Sem pressa"])),
        entrega_block(4),
    ])


def notebook_form():
    return qform("notebook", "uso,orcamento", [
        block(1, "Para que vai usar?", opts("uso", [("Jogos", "Jogos"), ("Trabalho e estudo", "Trabalho e estudo"), ("Edição e criação", "Edição e criação"), ("Uso básico", "Uso básico", "Internet, vídeos, Office")]), "uso"),
        block(2, "Qual o orçamento?", opts("orcamento", ["Até R$ 3.000", "R$ 3.000 a R$ 5.000", "R$ 5.000 a R$ 8.000", "Acima de R$ 8.000", ("Ainda não sei", "Ainda não sei", "Me ajudem a definir")]), "orcamento"),
        block(3, "O que é importante?", chips("extras", ["Leve e fácil de carregar", "Bateria que dure", "Tela grande", "Placa de vídeo dedicada", "SSD rápido", "Poder fazer upgrade depois"])),
        block(4, "Novo ou usado?", opts("condicao", ["Novo", "Seminovo", "Tanto faz"])),
        entrega_block(5),
    ])


# ---------- MONTADOR ----------
def wizard():
    usos = opts("uso", [("Jogos", "Jogos", "Competitivos ou pesados"), ("Trabalho e escritório", "Trabalho e escritório", "Planilhas, sistemas, multitarefa"),
                        ("Edição e criação", "Edição e criação", "Vídeo, foto, design, 3D"), ("Estudo", "Estudo", "Aulas, pesquisa, programação"), ("Uso misto", "Uso misto", "Um pouco de tudo")])
    progs = chips("programas", ["Jogos competitivos (CS2, Valorant, LoL)", "Jogos pesados (GTA V, Cyberpunk)", "Minecraft / Roblox",
                                "Streaming / gravação", "Edição de vídeo", "Photoshop / design", "Render 3D", "Programação", "Office e navegação"])
    orcs = opts("orcamento", [("Até R$ 3.000", "Até R$ 3.000", "Entrada"), ("R$ 3.000 a R$ 5.000", "R$ 3.000 a R$ 5.000", "Intermediário"),
                              ("R$ 5.000 a R$ 8.000", "R$ 5.000 a R$ 8.000", "Alta performance"), ("Acima de R$ 8.000", "Acima de R$ 8.000", "Topo de linha"),
                              ("Ainda não sei", "Ainda não sei", "Me ajudem a definir")])
    sil = opts("silencio", [("Sim, é importante", "Sim, quero silencioso", "Foco em baixo ruído"), ("Tanto faz", "Tanto faz", "Prioridade é desempenho")])
    extras = chips("extras", ["Visual com RGB", "Gabinete compacto", "Wi-Fi integrado", "Preciso de monitor", "Preciso de teclado e mouse", "Quero aproveitar peças que já tenho"])
    labels = ["Uso", "Detalhes", "Orçamento", "Preferências", "Finalizar"]
    prog = "".join(f'<li><button type="button" data-label="{l}">{i}. {l}</button></li>' for i, l in enumerate(labels, 1))
    return f'''      <div class="wizard" data-wizard>
        <div class="wiz__main">
          <ol class="wiz__progress" aria-label="Etapas">{prog}</ol>
          <p class="wiz__count" data-step-count aria-live="polite"></p>
          <form novalidate>
            <fieldset class="wiz__step is-active"><legend tabindex="-1">Para que você vai usar?</legend><p class="wiz__hint">Escolha o uso principal.</p>{usos}</fieldset>
            <fieldset class="wiz__step"><legend tabindex="-1">O que vai rodar?</legend><p class="wiz__hint">Marque quantos quiser. Pode pular.</p>{progs}</fieldset>
            <fieldset class="wiz__step"><legend tabindex="-1">Qual o orçamento?</legend><p class="wiz__hint">Valor aproximado, só para direcionar as peças. O valor final a gente confirma com você.</p>{orcs}</fieldset>
            <fieldset class="wiz__step"><legend tabindex="-1">Preferências</legend>
              <div class="wiz__group"><p>Quer um PC silencioso?</p>{sil}</div>
              <div class="wiz__group"><p>Mais alguma coisa?</p>{extras}</div>
            </fieldset>
            <fieldset class="wiz__step"><legend tabindex="-1">Quase lá</legend><p class="wiz__hint">Opcional. Ajuda a gente a te atender melhor.</p>
              {field_text("nome", "Seu nome")}
              {field_text("obs", "Observações", "Ex.: já tenho monitor, preciso para o fim do mês", "textarea")}
            </fieldset>
          </form>
          <p class="wiz__why" data-why aria-live="polite"></p>
          <div class="wiz__nav">
            <button type="button" class="btn" data-prev hidden>← Voltar</button>
            <button type="button" class="btn btn--primary" data-next>Continuar →</button>
            <a class="btn btn--primary" data-send href="#" target="_blank" rel="noopener noreferrer" hidden>{ICON_WA}Enviar orçamento no WhatsApp</a>
          </div>
          <p class="sent" data-sent hidden>Abrimos o WhatsApp com a mensagem pronta. É só apertar enviar lá. Não abriu? <a data-sent-link href="#" target="_blank" rel="noopener noreferrer">Toque aqui</a>.</p>
          <noscript><p class="note">Ative o JavaScript ou <a href="{WA}">chame direto no WhatsApp</a>.</p></noscript>
        </div>
        <aside class="wiz__sum" aria-live="polite">
          <h3>Seu orçamento</h3>
          <dl>
            <div><dt>Uso</dt><dd data-sum="uso"></dd></div>
            <div><dt>Jogos / programas</dt><dd data-sum="programas"></dd></div>
            <div><dt>Orçamento</dt><dd data-sum="orcamento"></dd></div>
            <div><dt>PC silencioso</dt><dd data-sum="silencio"></dd></div>
            <div><dt>Preferências</dt><dd data-sum="extras"></dd></div>
          </dl>
          <a class="btn btn--primary" data-send href="#" target="_blank" rel="noopener noreferrer" aria-disabled="true">{ICON_WA}Enviar no WhatsApp</a>
          <p class="hint">Nada é enviado sozinho: o WhatsApp abre com a mensagem pronta e você decide se envia.</p>
        </aside>
      </div>'''


pages = {}

# ---------- HOME ----------
home = f'''  <section class="hero" id="inicio">
    <div class="container hero__in">
      <span class="eyebrow">Franca-SP</span>
      <h1>Performance que você sente. <em>Montagem</em> em que confia.</h1>
      <p>PCs gamer, upgrades e manutenção feitos por quem entende de hardware.</p>
      <div class="hero__cta">
        <a class="btn btn--primary" href="/monte-seu-pc/">Monte seu PC</a>
        <a class="btn" {wa()}>{ICON_WA}Falar no WhatsApp</a>
      </div>
      <p class="hero__proof"><b>★★★★★</b> Avaliações no Google · Busca e entrega · Prazo cumprido</p>
    </div>
  </section>

  <div class="trust">
    <ul class="container">
      <li><a href="/montagem/">Montagem</a></li><li><a href="/upgrade/">Upgrade</a></li><li><a href="/manutencao/">Manutenção</a></li><li><a href="/notebooks/">Notebooks</a></li>
    </ul>
  </div>
''' + "\n".join([
    section(head("Serviços", "O que você precisa?") + cards([
        link_card("/montagem/", "pc", "PC Gamer sob medida", "Peças certas para o seu uso e orçamento.", "Montar o meu →"),
        link_card("/upgrade/", "up", "Upgrade", "Mais desempenho sem trocar o PC inteiro.", "Preencher upgrade →"),
        link_card("/manutencao/", "tool", "Manutenção", "Limpeza, formatação e reparo. Buscamos e entregamos.", "Descrever o problema →"),
        link_card("/notebooks/", "laptop", "Notebooks", "Gamer e de trabalho, com assistência.", "Escolher o meu →"),
    ]), alt=True, sid="servicos"),
    section(f'''      <div class="band reveal">
        <div>
          <span class="eyebrow">Monte seu computador</span>
          <h2>Escolha. Nós montamos.</h2>
          <ul><li>{ico("check")}Em 1 minuto</li><li>{ico("check")}Sem cadastro</li><li>{ico("check")}Você revisa antes de enviar</li></ul>
        </div>
        <a class="btn btn--primary" href="/monte-seu-pc/">Começar agora →</a>
      </div>'''),
    section(head("Em estoque", "Produtos em destaque", "Marque o que interessa e envie tudo de uma vez.") + cards([product_card(i) for i in HOME_PRODUCTS])
            + '\n      <p class="cta-row"><a class="btn" href="/produtos/">Ver todos os produtos</a></p>', alt=True),
    reviews_section(),
    cta_band("Seu próximo PC começa aqui.", "Falar no WhatsApp", WA_MSG, ("/monte-seu-pc/", "Monte seu PC")),
])
pages["/"] = ("/", "TR Gamers Informática | PCs Gamer, Montagem e Upgrade em Franca-SP",
              "PCs gamer, notebooks, montagem, upgrade e manutenção em Franca-SP. Monte seu computador e receba o orçamento no WhatsApp.",
              home, True)


# ---------- SERVIÇOS ----------
def service(path, crumb, h1, lead, cta, msg, title, desc, blocks, primary):
    body = (page_hero(crumb, h1, lead, "Prefiro falar no WhatsApp", msg, primary=primary) + "\n" + "\n".join(blocks) + "\n"
            + cta_band("Prefere conversar? Sem problema.", "Falar no WhatsApp", msg, primary))
    pages[path] = (path, title, desc, body, False)


service("/montagem/", "PC Gamer", "PC Gamer sob medida", "Peças certas para o seu uso e orçamento. Montagem com acabamento e testes antes da entrega.",
        "", "Oi, tudo bem? Vim pelo site e queria um orçamento de PC Gamer. Podem me ajudar?",
        "PC Gamer sob medida em Franca-SP | TR Gamers", "Montagem de PC gamer sob medida em Franca-SP. Peças certas para o seu uso e orçamento.",
        [section(head("Como funciona", "Do pedido à bancada") + cards([
            info_card("Conversa", "Você conta o uso e o orçamento.", num="01"),
            info_card("Orçamento", "Montamos opções de peças e condições de pagamento.", num="02"),
            info_card("Montagem", "Montagem e testes na nossa bancada.", num="03"),
            info_card("Entrega", "Retire na loja ou receba em casa.", num="04")]), alt=True),
         section(head("Perfis", "Qual o seu?") + cards([
            info_card("Entrada", "Jogos leves, estudo e trabalho. Bom custo-benefício.", "pc"),
            info_card("Intermediário", "Jogos atuais em boa qualidade e multitarefa.", "pc"),
            info_card("Alta performance", "Jogos pesados, edição e render.", "pc")], 3)
            + '\n      <p class="cta-row"><a class="btn btn--primary" href="/monte-seu-pc/">Monte o seu agora →</a></p>')],
        ("/monte-seu-pc/", "Monte seu PC"))
service("/upgrade/", "Upgrade", "Upgrade do seu PC", "Mais desempenho sem trocar tudo. Conte o que você tem e o que quer melhorar.",
        "", "Oi, tudo bem? Vim pelo site e queria fazer um upgrade no meu PC. Podem me ajudar?",
        "Upgrade de PC em Franca-SP | TR Gamers", "Upgrade de memória, SSD, placa de vídeo e processador em Franca-SP. Diagnóstico e orçamento no WhatsApp.",
        [section(head("Monte seu upgrade", "Conte o que você tem", "Responda o que souber. O resto a gente descobre junto no WhatsApp.") + upgrade_form(), alt=True, sid="upgrade-form"),
         section(head("O que atualizamos", "Peças que mais rendem") + cards([
            info_card("Memória RAM", "Mais fôlego para multitarefa e jogos.", "ram"),
            info_card("SSD", "Sistema e jogos carregando muito mais rápido.", "cpu"),
            info_card("Placa de vídeo", "Mais quadros por segundo e qualidade gráfica.", "pc"),
            info_card("Refrigeração", "Cooler e fans para temperatura e silêncio.", "fan")]))],
        ("#upgrade-form", "Preencher meu upgrade"))
service("/manutencao/", "Manutenção", "Manutenção e assistência", "Limpeza, formatação e reparo de PCs e notebooks. Buscamos e entregamos o equipamento.",
        "", "Oi, tudo bem? Vim pelo site e preciso de um orçamento de manutenção. Podem me ajudar?",
        "Manutenção de computadores em Franca-SP | TR Gamers", "Manutenção, limpeza, formatação e assistência técnica de PCs e notebooks em Franca-SP, com busca e entrega.",
        [section(head("Descreva o problema", "O que está acontecendo?", "Quanto mais detalhe, mais rápido o orçamento.") + manutencao_form(), alt=True, sid="manutencao-form"),
         section(head("Serviços", "Resolvemos") + cards([
            info_card("Limpeza e pasta térmica", "Temperatura sob controle e menos ruído.", "fan"),
            info_card("Formatação", "Sistema limpo, drivers e programas instalados.", "cpu"),
            info_card("Reparo", "Diagnóstico e troca de peças.", "tool"),
            info_card("Busca e entrega", "Levamos e trazemos o equipamento.", "truck")]))],
        ("#manutencao-form", "Descrever o problema"))
service("/notebooks/", "Notebooks", "Notebooks", "Notebooks gamer e de trabalho, com upgrade e assistência.",
        "", "Oi, tudo bem? Vim pelo site e queria um orçamento de notebook. Podem me ajudar?",
        "Notebooks em Franca-SP | TR Gamers", "Venda, upgrade e assistência de notebooks gamer e de trabalho em Franca-SP.",
        [section(head("Encontre o seu", "Qual notebook combina com você?", "Responda rápido e a gente indica as opções.") + notebook_form(), alt=True, sid="notebook-form"),
         section(head("Opções", "Para cada uso") + cards([
            info_card("Gamer", "Desempenho para jogos e criação.", "laptop"),
            info_card("Trabalho e estudo", "Leves, rápidos e confiáveis.", "laptop"),
            info_card("Upgrade e assistência", "Memória, SSD, limpeza e reparo.", "tool")], 3))],
        ("#notebook-form", "Escolher meu notebook"))

# ---------- PRODUTOS ----------
pages["/produtos/"] = ("/produtos/", "Produtos de informática em Franca-SP | TR Gamers",
    "Fans, coolers, memória RAM, mouse gamer e acessórios em estoque na loja. Consulte disponibilidade no WhatsApp.",
    page_hero("Produtos", "Em estoque na loja", "Marque o que interessa e envie a consulta de uma vez. Valor e disponibilidade a gente confirma com você.",
              "Perguntar no WhatsApp", "Oi, tudo bem? Vim pelo site e queria consultar um produto. Podem me ajudar?", primary=("#catalogo", "Ver produtos"))
    + "\n" + section(search_block() + cards([product_card(i) for i in range(len(PRODUCTS))])
                     + '\n      <div class="empty" data-empty hidden><p><b>Nenhum produto encontrado.</b></p><p class="note">Pode ser que a loja tenha. Pergunte direto:</p>'
                     '<a class="btn btn--primary" data-empty-wa href="#" target="_blank" rel="noopener noreferrer">' + ICON_WA + 'Perguntar no WhatsApp</a></div>'
                     + '\n      <p class="note">O estoque varia. Tem muito mais na loja: peças, periféricos e acessórios. Se não achou, pergunte no WhatsApp.</p>', alt=True, sid="catalogo")
    + "\n" + cta_band("Não achou o que procura?", "Perguntar no WhatsApp", "Oi, tudo bem? Procurei no site e não achei um produto que preciso. Vocês teriam?"), False)

# ---------- MONTE SEU PC ----------
pages["/monte-seu-pc/"] = ("/monte-seu-pc/", "Monte seu PC | TR Gamers Informática",
    "Escolha uso, orçamento e preferências e receba o orçamento do seu PC no WhatsApp.",
    page_hero("Monte seu PC", "Monte seu computador", "Responda em 1 minuto. Você revisa tudo antes de enviar para o WhatsApp.", "Prefiro falar direto",
              "Oi, tudo bem? Vim pelo site e quero montar um PC. Podem me ajudar?", primary=("#montador", "Começar agora"))
    + "\n" + section(wizard(), alt=True, sid="montador"), False)

# ---------- SOBRE ----------
pages["/sobre/"] = ("/sobre/", "Sobre a TR Gamers Informática | Franca-SP",
    "Loja de computadores referência em Franca-SP. Qualidade, confiança e performance.",
    '''  <section class="section sobre">
    <div class="container">
      <h1 class="sr-only">Sobre a TR Gamers Informática</h1>
      <img class="sobre__banner" src="/assets/img/banner.webp" alt="TR Gamers: a loja de computadores referência na cidade" width="2000" height="889">
      <p class="sobre__cta"><a class="btn btn--primary" ''' + wa("Oi, tudo bem? Vim pelo site e gostaria de falar com a loja.") + '>' + ICON_WA + '''Falar com a loja</a></p>
    </div>
  </section>''', False)

# ---------- CONTATO ----------
rows = "".join(f'<tr data-day="{d}"><td>{n}</td><td>{h}</td></tr>' for d, n, h in HOURS)
pages["/contato/"] = ("/contato/", "Contato e endereço | TR Gamers Informática",
    "R. Salima Mussi Pedro, 3098, Franca-SP. Seg a Sex 9h às 18h, sábado 8h às 12h. Orçamentos pelo WhatsApp.",
    page_hero("Contato", "Fale com a loja", "Resposta rápida pelo WhatsApp ou venha até nós.", "Chamar no WhatsApp", WA_MSG,
              f'\n        <a class="btn" href="{MAPS}" target="_blank" rel="noopener noreferrer">Abrir no Maps</a>')
    + "\n" + section(head("Atalhos", "Prefere resolver pelo site?", "Responda algumas perguntas e a mensagem vai pronta para o WhatsApp.") + cards([
        link_card("/monte-seu-pc/", "pc", "Montar um PC", "Uso, orçamento e preferências.", "Começar →"),
        link_card("/upgrade/", "up", "Upgrade", "Informe sua configuração atual.", "Preencher →"),
        link_card("/manutencao/", "tool", "Manutenção", "Descreva o problema.", "Descrever →"),
        link_card("/produtos/", "cpu", "Produtos", "Marque o que quer consultar.", "Ver produtos →"),
    ]))
    + "\n" + section(f'''      <div class="contact">
        <div class="map" data-map="{MAPS_EMBED}">
          <div class="map__ph">
            <p><b>Mapa do Google</b></p>
            <small>O mapa só carrega se você quiser. Ao carregar, o Google recebe seu IP.</small>
            <div class="hero__cta hero__cta--center"><button type="button" class="btn" data-load-map>Carregar mapa</button><a class="btn btn--sm" href="{MAPS}" target="_blank" rel="noopener noreferrer">Abrir no Maps</a></div>
          </div>
        </div>
        <div class="panel">
          <h3>Endereço</h3><p>R. Salima Mussi Pedro, 3098<br>Franca-SP · 14403-664</p>
          <h3>Horário</h3><table class="hours">{rows}</table><span class="status"></span>
          <a class="btn btn--primary" {wa()}>{ICON_WA}WhatsApp (16) 99207-6444</a>
          <a class="btn" href="tel:+5516992076444">Ligar agora</a>
          <a class="btn" href="https://www.instagram.com/trgamersinformatica/" target="_blank" rel="noopener noreferrer">Instagram</a>
        </div>
      </div>''', alt=True), False)

# ---------- ESCREVER ----------
for key, (path, title, desc, body, preload) in pages.items():
    active = path if path != "/" else ""
    out = ROOT / "index.html" if path == "/" else ROOT / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(path, active, title, desc, body, preload), encoding="utf-8")
    print("ok", out.relative_to(ROOT))

# 404 (Netlify serve automaticamente)
nf = section('''      <div class="cta-final"><span class="eyebrow">Erro 404</span><h1>Página não encontrada</h1>
      <p class="note">O endereço pode ter mudado. Escolha um caminho:</p>
      <div class="hero__cta hero__cta--center"><a class="btn btn--primary" href="/">Ir para o início</a><a class="btn" href="/monte-seu-pc/">Monte seu PC</a><a class="btn" ''' + wa() + '>' + ICON_WA + '''Falar no WhatsApp</a></div></div>''')
(ROOT / "404.html").write_text(page("/404.html", "", "Página não encontrada | TR Gamers Informática", "Página não encontrada.", nf, False, True), encoding="utf-8")

urls = "\n".join(f"  <url><loc>{DOMAIN}{p}</loc></url>" for p in pages)
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
