(function () {
  "use strict";

  const liveStatus = document.getElementById("liveStatus");

  function announce(message) {
    if (!liveStatus) return;
    liveStatus.textContent = "";
    requestAnimationFrame(() => {
      liveStatus.textContent = message;
    });
  }

  const navToggle = document.querySelector("[data-nav-toggle]");
  navToggle?.addEventListener("click", () => {
    const open = !document.body.classList.contains("nav-open");
    document.body.classList.toggle("nav-open", open);
    navToggle.setAttribute("aria-expanded", String(open));
  });

  for (const group of document.querySelectorAll("[data-tabs]")) {
    const tabs = [...group.querySelectorAll('[role="tab"]')];
    const panels = tabs
      .map((tab) => document.getElementById(tab.getAttribute("aria-controls")))
      .filter(Boolean);

    function selectTab(active) {
      for (const tab of tabs) {
        const selected = tab === active;
        tab.setAttribute("aria-selected", String(selected));
        tab.tabIndex = selected ? 0 : -1;
      }
      for (const panel of panels) {
        panel.hidden = panel.id !== active.getAttribute("aria-controls");
      }
    }

    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => selectTab(tab));
      tab.addEventListener("keydown", (event) => {
        if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
        event.preventDefault();
        let next = index;
        if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
        if (event.key === "ArrowLeft") next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === "Home") next = 0;
        if (event.key === "End") next = tabs.length - 1;
        selectTab(tabs[next]);
        tabs[next].focus();
      });
    });
  }

  for (const group of document.querySelectorAll(".segmented:not([data-tabs])")) {
    const buttons = [...group.querySelectorAll("button")];
    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        buttons.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
        announce(`时间窗口已切换为${button.textContent.trim()}，样张数据不变。`);
      });
    });
    group.addEventListener("change", (event) => {
      if (event.target.matches('input[type="radio"]')) {
        announce(`时间窗口已切换为${event.target.nextElementSibling.textContent.trim()}，样张数据不变。`);
      }
    });
  }

  for (const button of document.querySelectorAll("[data-open-dialog]")) {
    button.addEventListener("click", () => {
      const dialog = document.getElementById(button.dataset.openDialog);
      if (dialog && typeof dialog.showModal === "function") {
        dialog.showModal();
      }
    });
  }

  for (const button of document.querySelectorAll("[data-close-dialog]")) {
    button.addEventListener("click", () => {
      button.closest("dialog")?.close();
    });
  }

  for (const dialog of document.querySelectorAll("dialog")) {
    dialog.addEventListener("click", (event) => {
      if (event.target === dialog) dialog.close();
    });
  }

  for (const button of document.querySelectorAll("[data-empty-action]")) {
    button.addEventListener("click", () => {
      announce("这是交互样张，操作没有连接真实系统。");
    });
  }

  for (const button of document.querySelectorAll("[data-copy-summary]")) {
    button.addEventListener("click", async () => {
      const summary = document.querySelector(".signal-heading")?.innerText || "";
      try {
        await navigator.clipboard.writeText(summary);
        announce("摘要已复制。");
      } catch {
        announce("浏览器未允许复制，请手动选择摘要。");
      }
    });
  }

  const stream = document.getElementById("traceStream");
  const range = document.getElementById("traceRange");
  const position = document.getElementById("tracePosition");

  if (stream && range && position) {
    const steps = [...stream.querySelectorAll("[data-step]")];

    function setStep(value) {
      const nextValue = Math.min(steps.length, Math.max(1, Number(value)));
      range.value = String(nextValue);
      position.textContent = String(nextValue);
      steps.forEach((step) => {
        step.classList.toggle("is-hidden", Number(step.dataset.step) > nextValue);
      });
    }

    range.addEventListener("input", () => setStep(range.value));
    document.querySelector('[data-step-action="prev"]')?.addEventListener("click", () => setStep(Number(range.value) - 1));
    document.querySelector('[data-step-action="next"]')?.addEventListener("click", () => setStep(Number(range.value) + 1));
    setStep(range.value);
  }
})();

