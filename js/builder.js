import { waLink, clean, lower, showSent, persist } from "./whatsapp.js";

const root = document.querySelector("[data-wizard]");
const form = root.querySelector("form");
const steps = [...root.querySelectorAll(".wiz__step")];
const tabs = [...root.querySelectorAll(".wiz__progress li")];
const btnPrev = root.querySelector("[data-prev]");
const btnNext = root.querySelector("[data-next]");
const why = root.querySelector("[data-why]");
const sent = root.querySelector("[data-sent]");
const sendLinks = [...root.querySelectorAll("[data-send]")];
const sum = Object.fromEntries([...root.querySelectorAll("[data-sum]")].map((el) => [el.dataset.sum, el]));

const REQUIRED = { 1: ["uso", "Escolha o uso principal para continuar."], 3: ["orcamento", "Escolha uma faixa de orçamento para continuar."] };
let current = 1;

const read = () => {
  const fd = new FormData(form);
  return {
    nome: clean(fd.get("nome"), 60),
    uso: fd.get("uso") || "",
    programas: fd.getAll("programas"),
    orcamento: fd.get("orcamento") || "",
    silencio: fd.get("silencio") || "",
    extras: fd.getAll("extras"),
    obs: clean(fd.get("obs"), 400),
  };
};

const stepOk = (n, d) => !REQUIRED[n] || !!d[REQUIRED[n][0]];
const canGo = (n, d) => [...Array(n - 1).keys()].every((i) => stepOk(i + 1, d));
const complete = (d) => !!d.uso && !!d.orcamento;

function buildMessage(d) {
  const parts = [d.nome ? `Oi, tudo bem? Meu nome é ${d.nome}.` : "Oi, tudo bem?"];
  parts.push("Vim pelo site da TR Gamers e queria montar um PC.");
  let uso = `Vou usar principalmente para ${lower(d.uso)}.`;
  if (d.programas.length) uso += ` Quero rodar: ${d.programas.join(", ")}.`;
  parts.push(uso);
  parts.push(
    d.orcamento === "Ainda não sei"
      ? "Ainda não defini o orçamento, queria ajuda para ver o que cabe."
      : `Meu orçamento é de aproximadamente ${lower(d.orcamento)}.`
  );
  const prefs = [];
  if (d.silencio === "Sim, é importante") prefs.push("Quero que o PC seja silencioso.");
  if (d.extras.length) prefs.push(`Também quero: ${d.extras.map(lower).join(", ")}.`);
  if (prefs.length) parts.push(prefs.join(" "));
  if (d.obs) parts.push(/[.!?]$/.test(d.obs) ? d.obs : `${d.obs}.`);
  parts.push("Conseguem me passar algumas opções? Obrigado!");
  return parts.join("\n\n");
}

function setSum(key, value) {
  const el = sum[key];
  const text = value || "Não informado";
  if (el.textContent !== text && el.textContent !== "") {
    el.classList.remove("flash");
    void el.offsetWidth;
    el.classList.add("flash");
  }
  el.textContent = text;
  el.classList.toggle("is-empty", !value);
}

const store = persist("trg:montador", form, { get: () => ({ step: current }) });

function update() {
  const d = read();
  setSum("uso", d.uso);
  setSum("programas", d.programas.join(", "));
  setSum("orcamento", d.orcamento);
  setSum("silencio", d.silencio);
  setSum("extras", d.extras.join(", "));
  const ok = complete(d);
  const href = ok ? waLink(buildMessage(d)) : "#";
  sendLinks.forEach((a) => {
    a.href = href;
    a.setAttribute("aria-disabled", String(!ok));
  });
  const blocked = !stepOk(current, d);
  btnNext.disabled = blocked;
  why.textContent = blocked ? REQUIRED[current][1] : "";
  tabs.forEach((li, i) => {
    const n = i + 1;
    li.classList.toggle("is-current", n === current);
    li.classList.toggle("is-done", n < current && stepOk(n, d));
    li.querySelector("button").disabled = !canGo(n, d);
  });
  store.write();
}

const LABELS = ["Uso", "Detalhes", "Orçamento", "Preferências", "Finalizar"];
const countEl = root.querySelector("[data-step-count]");

function go(n, focus = true) {
  const prev = current;
  current = Math.min(Math.max(n, 1), steps.length);
  steps.forEach((s, i) => {
    s.dataset.dir = current < prev ? "back" : "next";
    s.classList.toggle("is-active", i + 1 === current);
  });
  countEl.innerHTML = `Passo <b>${current}</b> de ${steps.length} · ${LABELS[current - 1]}`;
  const last = current === steps.length;
  btnPrev.hidden = current === 1;
  btnNext.hidden = last;
  root.querySelector(".wiz__nav [data-send]").hidden = !last;
  update();
  if (focus) {
    steps[current - 1].querySelector("legend").focus({ preventScroll: true });
    root.scrollIntoView({ block: "start", behavior: "smooth" });
  }
}

form.addEventListener("input", () => { sent.hidden = true; update(); });
form.addEventListener("submit", (e) => e.preventDefault());
btnPrev.addEventListener("click", () => go(current - 1));
btnNext.addEventListener("click", () => go(current + 1));
tabs.forEach((li, i) => li.querySelector("button").addEventListener("click", () => go(i + 1)));

// Enter avança (exceto no campo de observações)
form.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && e.target.tagName === "INPUT" && !btnNext.disabled && !btnNext.hidden) {
    e.preventDefault();
    go(current + 1);
  }
});

sendLinks.forEach((a) =>
  a.addEventListener("click", (e) => {
    if (a.getAttribute("aria-disabled") === "true") {
      e.preventDefault();
      go(!read().uso ? 1 : 3);
      return;
    }
    showSent(sent, a.href);
    try { sessionStorage.removeItem("trg:montador"); } catch {}
  })
);

const saved = store.restore();
go(Math.min(Number(saved.step) || 1, 5), false);
// se o passo salvo exige algo que falta, volta ao primeiro passo possível
for (let n = current; n > 1 && !canGo(n, read()); n--) go(n - 1, false);
