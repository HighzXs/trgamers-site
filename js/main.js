import { waLink } from "./whatsapp.js";

// Links de WhatsApp: <a data-wa="mensagem opcional">
document.querySelectorAll("[data-wa]").forEach((a) => {
  a.href = waLink(a.dataset.wa);
  a.target = "_blank";
  a.rel = "noopener noreferrer";
});

// Menu mobile (fecha com Esc, clique fora ou ao escolher um link)
const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector(".nav");
const closeMenu = () => {
  nav.classList.remove("is-open");
  menuBtn.setAttribute("aria-expanded", "false");
};
menuBtn?.addEventListener("click", () => {
  const open = nav.classList.toggle("is-open");
  menuBtn.setAttribute("aria-expanded", open);
});
nav?.addEventListener("click", (e) => e.target.closest("a") && closeMenu());
document.addEventListener("keydown", (e) => e.key === "Escape" && closeMenu());
document.addEventListener("click", (e) => {
  if (nav?.classList.contains("is-open") && !e.target.closest(".header")) closeMenu();
});

// Sombra no header ao rolar
const header = document.querySelector(".header");
const onScroll = () => header.classList.toggle("is-scrolled", scrollY > 8);
addEventListener("scroll", onScroll, { passive: true });
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
document.querySelectorAll(".cards, .photos").forEach((g) =>
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
