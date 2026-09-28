const root = document.documentElement;
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// ───────── Dark / light toggle (remembers your choice) ─────────
const media = window.matchMedia("(prefers-color-scheme: dark)");
document.querySelector(".theme-toggle")?.addEventListener("click", () => {
  const current = root.getAttribute("data-theme") || (media.matches ? "dark" : "light");
  const next = current === "dark" ? "light" : "dark";
  root.setAttribute("data-theme", next);
  try { localStorage.setItem("theme", next); } catch (e) {}
});

// ───────── Fade sections in as they scroll into view ─────────
const revealEls = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  revealEls.forEach((el) => io.observe(el));
} else {
  revealEls.forEach((el) => el.classList.add("is-visible"));
}

// ───────── Highlight the current section in the sidebar nav ─────────
const navLinks = [...document.querySelectorAll(".toc a")];
const sections = navLinks.map((a) => document.getElementById(a.dataset.section)).filter(Boolean);

function updateActive() {
  const atBottom = window.innerHeight + window.scrollY >= document.body.scrollHeight - 4;
  let current = sections[0];
  if (atBottom) {
    current = sections[sections.length - 1];
  } else {
    for (const s of sections) {
      if (s.getBoundingClientRect().top <= window.innerHeight * 0.35) current = s;
    }
  }
  navLinks.forEach((a) => a.classList.toggle("active", a.dataset.section === current?.id));
}
window.addEventListener("scroll", updateActive, { passive: true });
updateActive();

// ───────── Project filters (the SQL line above the heading follows along) ─────────
const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const filterBtns = [...document.querySelectorAll(".filter")];
const projectCards = [...document.querySelectorAll(".project")];
const projectsQuery = document.getElementById("projects-query");

filterBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const f = btn.dataset.filter;
    filterBtns.forEach((b) => {
      b.classList.toggle("is-active", b === btn);
      b.setAttribute("aria-pressed", String(b === btn));
    });
    projectCards.forEach((card) => {
      const show = f === "all" || card.dataset.category === f;
      card.hidden = !show;
      if (show) {
        card.classList.remove("is-visible");
        requestAnimationFrame(() => requestAnimationFrame(() => card.classList.add("is-visible")));
      }
    });
    if (projectsQuery) {
      projectsQuery.innerHTML = f === "all"
        ? '<span class="kw">SELECT</span> * <span class="kw">FROM</span> projects;'
        : `<span class="kw">SELECT</span> * <span class="kw">FROM</span> projects <span class="kw">WHERE</span> category = <span class="str">'${esc(f)}'</span>;`;
    }
  });
});
