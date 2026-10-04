export const WA_NUMBER = "5516992076444";

export function waLink(message = "") {
  const base = `https://wa.me/${WA_NUMBER}`;
  return message ? `${base}?text=${encodeURIComponent(message)}` : base;
}

// Texto digitado pelo usuário: remove caracteres de controle e limita o tamanho.
export const clean = (t, max = 400) =>
  String(t ?? "").replace(/[\u0000-\u001F\u007F]+/g, " ").replace(/\s+/g, " ").trim().slice(0, max);

// "Jogos" -> "jogos", mas preserva siglas ("SSD", "R$ 500", "RGB").
export const lower = (t) => (/^[A-ZÀ-Ú][a-zà-ú]/.test(t) ? t.charAt(0).toLowerCase() + t.slice(1) : t);

// ["a", "b", "c"] -> "a, b e c"
export const list = (a) => (a.length > 1 ? `${a.slice(0, -1).join(", ")} e ${a.at(-1)}` : a[0] || "");

// Mostra o aviso "abrimos o WhatsApp" com link de reserva (caso o pop-up seja bloqueado).
export function showSent(box, href) {
  if (!box) return;
  box.querySelector("[data-sent-link]").href = href;
  box.hidden = false;
}

// Guarda as respostas na aba (sobrevive a recarregar a página; some ao fechar).
export function persist(key, form, extra = {}) {
  const read = () => {
    try { return JSON.parse(sessionStorage.getItem(key)) || {}; } catch { return {}; }
  };
  const write = () => {
    const data = { ...extra.get?.() };
    new FormData(form).forEach((v, k) => { (data.f ||= {}); (data.f[k] ||= []).push(v); });
    try { sessionStorage.setItem(key, JSON.stringify(data)); } catch {}
  };
  const restore = () => {
    const saved = read().f;
    if (!saved) return read();
    [...form.elements].forEach((el) => {
      const vals = saved[el.name];
      if (!vals) return;
      if (el.type === "radio" || el.type === "checkbox") el.checked = vals.includes(el.value);
      else if (el.tagName !== "BUTTON") el.value = vals[0];
    });
    return read();
  };
  form.addEventListener("input", write);
  return { restore, write };
}
