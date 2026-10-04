import { waLink, clean, lower, list, showSent, persist } from "./whatsapp.js";

const form = document.querySelector("[data-qform]");
const kind = form.dataset.qform;
const required = form.dataset.required.split(",");
const send = form.querySelector("[data-send]");
const hint = form.querySelector("[data-hint]");
const sent = form.querySelector("[data-sent]");

const LABELS = { tipo: "o tipo de PC", orcamento: "o orçamento", equip: "o equipamento", problema: "o problema", uso: "o uso" };
const known = (v) => v && v !== "Não sei";
const sentence = (t) => (/[.!?]$/.test(t) ? t : `${t}.`);

const greet = (f) => {
  const nome = clean(f.get("nome"), 60);
  return nome ? `Oi, tudo bem? Meu nome é ${nome}.` : "Oi, tudo bem?";
};
const orc = (f, extra) =>
  f.get("orcamento") === "Ainda não sei"
    ? `Ainda não defini o orçamento, ${extra}.`
    : `Meu orçamento é de aproximadamente ${lower(f.get("orcamento"))}.`;
const tail = (f) => {
  const out = [];
  if (f.get("entrega")) out.push(sentence(f.get("entrega")));
  const obs = clean(f.get("obs"), 400);
  if (obs) out.push(sentence(obs));
  return out;
};

const BUILDERS = {
  upgrade(f) {
    const tipo = { "PC montado (gabinete)": "PC", "PC de marca": "PC de marca", Notebook: "notebook" }[f.get("tipo")] || "computador";
    const p = [greet(f), `Vim pelo site da TR Gamers e queria fazer um upgrade no meu ${tipo}.`];
    const specs = [];
    const cpu = clean(f.get("cpu"), 60), gpu = clean(f.get("gpu"), 60);
    if (known(cpu)) specs.push(`processador ${cpu}`);
    if (known(f.get("ram"))) specs.push(`${f.get("ram")} de memória`);
    if (known(gpu)) specs.push(`placa de vídeo ${gpu}`);
    if (known(f.get("disco"))) specs.push(`armazenamento ${f.get("disco")}`);
    if (specs.length) p.push(`Hoje ele tem ${list(specs)}.`);
    if (f.getAll("melhorar").length) p.push(`Queria melhorar: ${f.getAll("melhorar").map(lower).join(", ")}.`);
    if (f.getAll("pecas").length) p.push(`Tinha pensado em trocar: ${f.getAll("pecas").map(lower).join(", ")}.`);
    p.push(orc(f, "queria ajuda para ver o que vale mais a pena"), ...tail(f), "Podem me ajudar a ver o que compensa mais? Obrigado!");
    return p.join("\n\n");
  },
  manutencao(f) {
    const eq = { "PC montado (gabinete)": "no meu PC", "PC de marca": "no meu PC de marca", Notebook: "no meu notebook", Outro: "no meu equipamento" }[f.get("equip")] || "no meu equipamento";
    const p = [greet(f), `Vim pelo site da TR Gamers e preciso de manutenção ${eq}.`];
    const modelo = clean(f.get("modelo"), 60);
    if (modelo) p.push(`É um ${modelo}.`);
    p.push(`O que está acontecendo: ${f.getAll("problema").map(lower).join(", ")}.`);
    if (f.get("urgencia")) p.push(`Urgência: ${lower(f.get("urgencia"))}.`);
    p.push(...tail(f), "Podem me passar um orçamento? Obrigado!");
    return p.join("\n\n");
  },
  notebook(f) {
    const p = [greet(f), "Vim pelo site da TR Gamers e estou procurando um notebook."];
    p.push(`Vou usar principalmente para ${lower(f.get("uso"))}.`);
    p.push(orc(f, "queria ajuda para ver o que cabe"));
    if (f.getAll("extras").length) p.push(`Para mim é importante: ${f.getAll("extras").map(lower).join(", ")}.`);
    if (f.get("condicao")) p.push(`Pode ser: ${lower(f.get("condicao"))}.`);
    p.push(...tail(f), "Quais opções vocês têm? Obrigado!");
    return p.join("\n\n");
  },
};

const has = (f, k) => f.getAll(k).some((v) => v && String(v).trim());
const missing = () => { const f = new FormData(form); return required.filter((k) => !has(f, k)); };

function update() {
  const f = new FormData(form);
  const miss = missing();
  const ok = miss.length === 0;
  send.href = ok ? waLink(BUILDERS[kind](f)) : "#";
  send.setAttribute("aria-disabled", String(!ok));
  hint.textContent = ok
    ? "Tudo certo. O WhatsApp abre com a mensagem pronta, e você decide se envia."
    : `Falta informar ${miss.map((k) => LABELS[k]).join(" e ")}.`;
}

const store = persist(`trg:${kind}`, form);
form.addEventListener("input", () => { sent.hidden = true; update(); store.write(); });
form.addEventListener("submit", (e) => e.preventDefault());

send.addEventListener("click", (e) => {
  if (send.getAttribute("aria-disabled") === "true") {
    e.preventDefault();
    const block = form.querySelector(`[data-field="${missing()[0]}"]`);
    if (block) {
      block.scrollIntoView({ behavior: "smooth", block: "center" });
      block.classList.remove("is-missing");
      void block.offsetWidth;
      block.classList.add("is-missing");
    }
    return;
  }
  showSent(sent, send.href);
  try { sessionStorage.removeItem(`trg:${kind}`); } catch {}
});

store.restore();
update();
