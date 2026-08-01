/**
 * RelayRuntime landing page interactions
 * Nav · FAQ · Lightbox (focus trap) · Reveal · Header scroll · Year
 */

(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var body = document.body;

  /* Year */
  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  /* Sticky header elevation */
  var header = document.querySelector("[data-header]");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Mobile nav */
  var toggle = document.querySelector(".nav__toggle");
  var menu = document.getElementById("nav-menu");
  var backdrop = document.getElementById("nav-backdrop");

  function setMenuOpen(open) {
    if (!menu || !toggle) return;
    menu.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
    body.classList.toggle("nav-open", open);
    if (backdrop) backdrop.hidden = !open;

    if (open) {
      var firstLink = menu.querySelector("a");
      if (firstLink) firstLink.focus();
    }
  }

  function closeMenu() {
    setMenuOpen(false);
  }

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      setMenuOpen(!menu.classList.contains("is-open"));
    });

    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });

    if (backdrop) {
      backdrop.addEventListener("click", closeMenu);
    }

    window.addEventListener("resize", function () {
      if (window.innerWidth > 768) closeMenu();
    });
  }

  /* FAQ accordion */
  document.querySelectorAll(".faq__trigger").forEach(function (button) {
    button.addEventListener("click", function () {
      var expanded = button.getAttribute("aria-expanded") === "true";
      var panelId = button.getAttribute("aria-controls");
      var panel = panelId ? document.getElementById(panelId) : null;

      document.querySelectorAll(".faq__trigger").forEach(function (other) {
        if (other === button) return;
        other.setAttribute("aria-expanded", "false");
        var otherPanel = document.getElementById(other.getAttribute("aria-controls"));
        if (otherPanel) otherPanel.hidden = true;
      });

      button.setAttribute("aria-expanded", expanded ? "false" : "true");
      if (panel) panel.hidden = expanded;
    });
  });

  /* Lightbox with basic focus trap */
  var lightbox = document.getElementById("lightbox");
  var lightboxImg = lightbox ? lightbox.querySelector(".lightbox__image") : null;
  var lightboxClose = lightbox ? lightbox.querySelector(".lightbox__close") : null;
  var lastFocus = null;

  function getFocusable(container) {
    return Array.prototype.slice.call(
      container.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')
    ).filter(function (el) {
      return !el.hasAttribute("disabled") && !el.hidden;
    });
  }

  function openLightbox(src, alt) {
    if (!lightbox || !lightboxImg) return;
    lastFocus = document.activeElement;
    lightboxImg.src = src;
    lightboxImg.alt = alt || "";
    lightbox.hidden = false;
    lightbox.setAttribute("aria-hidden", "false");
    body.classList.add("lightbox-open");
    if (lightboxClose) lightboxClose.focus();
  }

  function closeLightbox() {
    if (!lightbox || !lightboxImg || lightbox.hidden) return;
    lightbox.hidden = true;
    lightbox.setAttribute("aria-hidden", "true");
    lightboxImg.removeAttribute("src");
    lightboxImg.alt = "";
    body.classList.remove("lightbox-open");
    if (lastFocus && typeof lastFocus.focus === "function") lastFocus.focus();
  }

  document.querySelectorAll(".lightbox-trigger").forEach(function (trigger) {
    trigger.addEventListener("click", function () {
      openLightbox(trigger.getAttribute("data-lightbox"), trigger.getAttribute("data-alt"));
    });
  });

  if (lightboxClose) {
    lightboxClose.addEventListener("click", closeLightbox);
  }

  if (lightbox) {
    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox) closeLightbox();
    });

    lightbox.addEventListener("keydown", function (event) {
      if (event.key !== "Tab" || lightbox.hidden) return;
      var focusable = getFocusable(lightbox);
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  }

  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    if (lightbox && !lightbox.hidden) {
      closeLightbox();
      return;
    }
    if (menu && menu.classList.contains("is-open")) {
      closeMenu();
      if (toggle) toggle.focus();
    }
  });

  /* Reveal on scroll */
  var reveals = document.querySelectorAll(".reveal");

  if (reduceMotion || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) {
      el.classList.add("is-visible");
    });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.1, rootMargin: "0px 0px -48px 0px" }
  );

  reveals.forEach(function (el) {
    observer.observe(el);
  });
})();
