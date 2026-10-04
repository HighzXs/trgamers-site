import { waLink } from "./whatsapp.js";

const KEY = "trg:produtos";
const buttons = [...document.querySelectorAll("[data-prod]")];
const names = new Set(buttons.map((b) => b.dataset.prod));
let picked = new Set();
try { picked = new Set((JSON.parse(sessionStorage.getItem(KEY)) || []).filter((n) => names.has(n))); } catch {}

const bar = document.createElement("div");
bar.className = "selbar";
bar.hidden = true;
bar.innerHTML = `
  <p class="selbar__txt" aria-live="polite"></p>
  <button type="button" class="btn btn--sm" data-clear>Limpar</button>
  <a class="btn btn--primary btn--sm" target="_blank" rel="noopener noreferrer"></a>`;
const txt = bar.querySelector(".selbar__txt");
const link = bar.querySelector("a");
link.innerHTML = '<svg aria-hidden="true"><use href="#i-wa"/></svg>Enviar consulta';
document.body.append(bar);

function message() {
  const items = [...picked].map((n) => `• ${n}`).join("\n");
  return `Oi, tudo bem? Vi no site da TR Gamers e queria saber se vocês têm em estoque e o valor destes produtos:\n\n${items}\n\nObrigado!`;
}

function render() {
  buttons.forEach((b) => {
    const on = picked.has(b.dataset.prod);
    b.setAttribute("aria-pressed", String(on));
    b.textContent = on ? "✓ Na consulta" : "Adicionar à consulta";
    b.classList.toggle("is-on", on);
  });
  const n = picked.size;
  bar.hidden = n === 0;
  document.body.classList.toggle("has-selbar", n > 0);
  txt.textContent = `${n} ${n === 1 ? "produto" : "produtos"} na consulta`;
  if (n) link.href = waLink(message());
  try { sessionStorage.setItem(KEY, JSON.stringify([...picked])); } catch {}
}

buttons.forEach((b) =>
  b.addEventListener("click", () => {
    const n = b.dataset.prod;
    picked.has(n) ? picked.delete(n) : picked.add(n);
    render();
  })
);
bar.querySelector("[data-clear]").addEventListener("click", () => { picked.clear(); render(); });
render();
