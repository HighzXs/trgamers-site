import { waLink, clean } from "./whatsapp.js";

const box = document.querySelector("[data-search]");
const input = box.querySelector("#busca");
const clear = box.querySelector("[data-clear-search]");
const count = box.querySelector("[data-count]");
const empty = document.querySelector("[data-empty]");
const emptyWa = empty.querySelector("[data-empty-wa]");
const items = [...document.querySelectorAll("[data-prod]")].map((b) => b.closest(".prod"));

// sem acento e minúsculo: "Memória" casa com "memoria"
const norm = (t) => t.normalize("NFD").replace(/\p{M}/gu, "").toLowerCase();
const index = items.map((el) => norm(`${el.dataset.name} ${el.dataset.cat}`));

function apply() {
  const terms = norm(clean(input.value, 60)).split(/\s+/).filter(Boolean);
  const cat = box.querySelector("input[name=cat]:checked").value;
  let shown = 0;
  items.forEach((el, i) => {
    const ok = (!cat || el.dataset.cat === cat) && terms.every((t) => index[i].includes(t));
    el.hidden = !ok;
    shown += ok;
  });
  clear.hidden = !input.value;
  empty.hidden = shown > 0;
  count.textContent = shown === items.length ? "" : `${shown} ${shown === 1 ? "produto encontrado" : "produtos encontrados"}`;
  const q = clean(input.value, 60);
  emptyWa.href = waLink(
    q ? `Oi, tudo bem? Procurei "${q}" no site da TR Gamers e não achei. Vocês têm?` : "Oi, tudo bem? Procurei um produto no site e não achei. Vocês têm?"
  );
}

input.addEventListener("input", apply);
box.addEventListener("change", apply);
clear.addEventListener("click", () => { input.value = ""; input.focus(); apply(); });
input.addEventListener("keydown", (e) => e.key === "Escape" && clear.click());
apply();
