(function () {
  "use strict";

  var STORE = "wte-lang";
  var LANGS = ["th", "en", "zh"];
  var HTML_LANG = { th: "th", en: "en", zh: "zh-Hans" };

  function safeGet() { try { return localStorage.getItem(STORE); } catch (e) { return null; } }
  function safeSet(v) { try { localStorage.setItem(STORE, v); } catch (e) { /* private mode */ } }

  /* ---------- Language ---------- */
  // Thai is the source text in the HTML; remember it so we can switch back.
  document.querySelectorAll("[data-i18n]").forEach(function (el) { el.setAttribute("data-th", el.innerHTML); });
  document.querySelectorAll("[data-i18n-alt]").forEach(function (el) { el.setAttribute("data-th-alt", el.getAttribute("alt") || ""); });

  function setLang(lang) {
    if (LANGS.indexOf(lang) < 0) lang = "th";
    var dict = (window.WTE_I18N || {})[lang];
    document.documentElement.lang = HTML_LANG[lang];
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      var text = lang === "th" || !dict || dict[key] == null ? el.getAttribute("data-th") : dict[key];
      if (el.tagName === "TITLE") document.title = text; else el.innerHTML = text;
    });
    document.querySelectorAll("[data-i18n-alt]").forEach(function (el) {
      var key = el.getAttribute("data-i18n-alt");
      el.setAttribute("alt", lang === "th" || !dict || dict[key] == null ? el.getAttribute("data-th-alt") : dict[key]);
    });
    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-lang") === lang ? "true" : "false");
    });
    safeSet(lang);
  }

  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.getAttribute("data-lang")); });
  });
  var saved = safeGet();
  if (saved && saved !== "th") setLang(saved);

  /* ---------- Nav ---------- */
  var nav = document.getElementById("nav");
  function onScroll() { nav.classList.toggle("scrolled", window.scrollY > 8); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  var burger = document.getElementById("burger");
  var menu = document.getElementById("menu");
  function closeMenu() { menu.classList.remove("open"); burger.setAttribute("aria-expanded", "false"); document.body.style.overflow = ""; }
  burger.addEventListener("click", function () {
    var open = !menu.classList.contains("open");
    menu.classList.toggle("open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
  });
  menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });
  window.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMenu(); });
  window.addEventListener("resize", function () { if (window.innerWidth > 640) closeMenu(); });

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Sub-navigation (business page): scroll-spy + reliable anchors ---------- */
  var sub = document.getElementById("subnav");
  if (sub) {
    var secs = Array.prototype.slice.call(document.querySelectorAll(".biz"));
    var tabs = Array.prototype.slice.call(sub.querySelectorAll("a"));
    var spyTick = false;
    var spy = function () {
      spyTick = false;
      var line = window.innerHeight * 0.35, cur = secs[0];
      secs.forEach(function (s) { if (s.getBoundingClientRect().top <= line) cur = s; });
      tabs.forEach(function (a) {
        var on = a.getAttribute("href") === "#" + cur.id;
        a.classList.toggle("on", on);
        if (on && sub.scrollWidth > sub.clientWidth) { sub.scrollLeft = a.offsetLeft - 24; }
      });
    };
    window.addEventListener("scroll", function () { if (!spyTick) { spyTick = true; requestAnimationFrame(spy); } }, { passive: true });
    spy();
  }

  // Jump to #section after fonts and layout settle, and mark everything above it as revealed.
  function goHash() {
    if (!location.hash) return;
    var t = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (t) t.scrollIntoView({ behavior: "instant", block: "start" });
  }
  if (location.hash && "scrollRestoration" in history) history.scrollRestoration = "manual";
  window.addEventListener("load", function () { goHash(); setTimeout(goHash, 250); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(goHash);
  window.addEventListener("hashchange", goHash);

  /* ---------- Projects filter ---------- */
  var chips = document.querySelectorAll(".chip[data-filter]");
  if (chips.length) {
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var f = chip.getAttribute("data-filter");
        chips.forEach(function (c) { c.classList.toggle("on", c === chip); });
        document.querySelectorAll(".pcard").forEach(function (card) {
          card.classList.toggle("hide", f !== "all" && card.getAttribute("data-cat") !== f);
        });
      });
    });
  }

  /* ---------- Contact form: opens the visitor's mail app ---------- */
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements;
      if (!f.name.value.trim() || !f.email.validity.valid || !f.message.value.trim()) {
        (f.name.value.trim() ? (f.email.validity.valid ? f.message : f.email) : f.name).focus();
        return;
      }
      var body = f.message.value.trim() + "\n\n— " + f.name.value.trim() +
        (f.phone.value.trim() ? "\n" + f.phone.value.trim() : "") + "\n" + f.email.value.trim();
      var subject = f.subject.value.trim() || "WTE Corporation website enquiry";
      window.location.href = "mailto:info@wtecorporation.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
