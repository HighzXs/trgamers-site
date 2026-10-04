import { waLink } from "./whatsapp.js";

// Links de WhatsApp: <a data-wa="mensagem opcional">
document.querySelectorAll("[data-wa]").forEach((a) => {
  a.href = waLink(a.dataset.wa);
  a.target = "_blank";
  a.rel = "noopener noreferrer";
});

// Menu mobile (fecha com Esc, clique fora ou ao escolher um link)
const header = document.querySelector(".header");
const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector(".nav");
nav?.querySelectorAll("a:not(.btn)").forEach((a, i) => a.style.setProperty("--i", i));
const closeMenu = () => {
  nav.classList.remove("is-open");
  menuBtn.setAttribute("aria-expanded", "false");
  document.body.classList.remove("menu-open");
};
menuBtn?.addEventListener("click", () => {
  const open = nav.classList.toggle("is-open");
  menuBtn.setAttribute("aria-expanded", open);
  document.body.classList.toggle("menu-open", open);
  header.classList.remove("is-hidden");
});
nav?.addEventListener("click", (e) => e.target.closest("a") && closeMenu());
document.addEventListener("keydown", (e) => e.key === "Escape" && closeMenu());
document.addEventListener("click", (e) => {
  if (nav?.classList.contains("is-open") && !e.target.closest(".header")) closeMenu();
});

// Header: sombra ao rolar, recolhe ao descer e volta ao subir; barra de progresso da página
const bar = document.createElement("div");
bar.className = "progress";
document.body.prepend(bar);
let lastY = scrollY, ticking = false;
const onScroll = () => {
  const y = scrollY;
  header.classList.toggle("is-scrolled", y > 8);
  const max = document.documentElement.scrollHeight - innerHeight;
  bar.style.setProperty("--p", max > 0 ? Math.min(y / max, 1).toFixed(3) : 0);
  const menuOpen = nav?.classList.contains("is-open");
  if (!menuOpen && Math.abs(y - lastY) > 6) header.classList.toggle("is-hidden", y > lastY && y > 140);
  if (y < 80) header.classList.remove("is-hidden");
  lastY = y;
  ticking = false;
};
addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
header.addEventListener("focusin", () => header.classList.remove("is-hidden"));
onScroll();

// Aberto agora / Fechado (horário de Franca-SP)
const HOURS = { 0: null, 1: [9, 18], 2: [9, 18], 3: [9, 18], 4: [9, 18], 5: [9, 18], 6: [8, 12] };
const nowSP = () => new Date(new Date().toLocaleString("en-US", { timeZone: "America/Sao_Paulo" }));
function updateStatus() {
  const now = nowSP();
  const range = HOURS[now.getDay()];
  const h = now.getHours() + now.getMinutes() / 60;
  const open = !!range && h >= range[0] && h < range[1];
  document.querySelectorAll(".status").forEach((el) => {
    el.dataset.open = open;
    el.textContent = open ? "Aberto agora" : "Fechado agora";
  });
}
updateStatus();
document.querySelector(`.hours tr[data-day="${nowSP().getDay()}"]`)?.classList.add("today");

// Revelar ao rolar (com pequeno atraso em cascata dentro de cada grade)
document.querySelectorAll(".section__head, .trust li, .sobre__banner, .sobre__cta, .checks li, .contact > *, .search").forEach((el) => el.classList.add("reveal"));
document.querySelectorAll(".cards, .photos, .trust ul, .checks").forEach((g) =>
  [...g.querySelectorAll(":scope > .reveal")].forEach((el, i) => el.style.setProperty("--d", `${Math.min(i, 5) * 70}ms`))
);
const reveals = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  reveals.forEach((el) => io.observe(el));
} else {
  reveals.forEach((el) => el.classList.add("is-in"));
}

// Mapa só carrega se o usuário pedir (privacidade + velocidade)
document.querySelector("[data-load-map]")?.addEventListener("click", () => {
  const box = document.querySelector("[data-map]");
  const f = document.createElement("iframe");
  f.title = "Mapa da TR Gamers Informática";
  f.src = box.dataset.map;
  f.referrerPolicy = "no-referrer";
  f.setAttribute("sandbox", "allow-scripts allow-same-origin allow-popups");
  box.replaceChildren(f);
});

// Módulos por página
if (document.querySelector("[data-wizard]")) import("./builder.js");
if (document.querySelector("[data-qform]")) import("./qform.js");
if (document.querySelector("[data-prod]")) import("./products.js");
if (document.querySelector("[data-search]")) import("./search.js");

// Imagens aparecem suavemente ao carregar
document.querySelectorAll(".prod__img, .sobre__banner").forEach((img) => {
  const ok = () => img.classList.add("is-loaded");
  img.complete && img.naturalWidth ? ok() : img.addEventListener("load", ok, { once: true });
});

// Telas com barra fixa embaixo: esconde o botão flutuante do WhatsApp
if (document.querySelector("[data-wizard], [data-qform]")) document.body.classList.add("has-sticky");

// Vibração leve ao escolher uma opção (só em celular)
if (matchMedia("(pointer: coarse)").matches && navigator.vibrate) {
  document.addEventListener("change", (e) => e.target.matches?.("input[type=radio], input[type=checkbox]") && navigator.vibrate(8));
}
