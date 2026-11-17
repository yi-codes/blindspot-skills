(function () {
  "use strict";

  const payload = window.DESIGN_DATA || { styles: [] };
  const styles = Array.isArray(payload.styles) ? payload.styles : [];
  const bySlug = new Map(styles.map((style) => [style.slug, style]));

  const labels = {
    register: {
      story: "讲故事",
      professional: "讲专业",
      technical: "讲技术",
      tool: "讲工具"
    },
    surface: {
      light: "浅色",
      dark: "深色",
      mixed: "双模"
    },
    density: {
      tight: "紧",
      medium: "中",
      roomy: "松"
    }
  };

  const registerSignals = {
    story: ["品牌", "故事", "作品集", "活动", "营销", "发布", "叙事", "杂志", "创意"],
    professional: ["产品页", "落地页", "案例", "数据看板", "b 端", "官网", "方案", "企业"],
    technical: ["文档", "代码", "日志", "cli", "规范", "技术", "论文", "开发"],
    tool: ["控制台", "工作台", "后台", "面板", "工具", "dashboard", "console", "admin", "任务", "设置", "运维", "监控", "告警"]
  };

  const state = {
    query: "",
    register: "all",
    surface: "all",
    density: "all",
    selected: styles[0] ? styles[0].slug : "",
    compare: []
  };

  const elements = {
    searchForm: document.getElementById("searchForm"),
    query: document.getElementById("query"),
    filterToggle: document.getElementById("filterToggle"),
    resetButton: document.getElementById("resetButton"),
    filterReset: document.getElementById("filterReset"),
    registerFilters: document.getElementById("registerFilters"),
    surfaceFilters: document.getElementById("surfaceFilters"),
    densityFilters: document.getElementById("densityFilters"),
    taskHint: document.getElementById("taskHint"),
    recommendationMeta: document.getElementById("recommendationMeta"),
    resultsTitle: document.getElementById("resultsTitle"),
    visibleCount: document.getElementById("visibleCount"),
    compareCount: document.getElementById("compareCount"),
    styleList: document.getElementById("styleList"),
    emptyState: document.getElementById("emptyState"),
    previewFrame: document.getElementById("previewFrame"),
    previewLabel: document.getElementById("previewLabel"),
    openPreview: document.getElementById("openPreview"),
    styleVersion: document.getElementById("styleVersion"),
    styleDetail: document.getElementById("styleDetail"),
    mobileDetail: document.getElementById("mobileDetail"),
    compareBar: document.getElementById("compareBar"),
    compareBarCount: document.getElementById("compareBarCount"),
    openCompare: document.getElementById("openCompare"),
    compareDialog: document.getElementById("compareDialog"),
    compareGrid: document.getElementById("compareGrid"),
    closeCompare: document.getElementById("closeCompare"),
    buildState: document.getElementById("buildState")
  };

  function escapeHtml(value) {
    return String(value || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function normalize(value) {
    return String(value || "").toLocaleLowerCase("zh-CN").replace(/\s+/g, " ").trim();
  }

  function semanticFragments(value) {
    const normalized = normalize(value);
    const fragments = new Set();
    for (const run of normalized.match(/[\u4e00-\u9fff]+/g) || []) {
      for (const width of [2, 3, 4]) {
        for (let index = 0; index <= run.length - width; index += 1) {
          fragments.add(run.slice(index, index + width));
        }
      }
    }
    for (const word of normalized.match(/[a-z0-9][a-z0-9.+-]+/g) || []) {
      fragments.add(word);
    }
    for (const stop of ["这个", "那个", "需要", "可以", "进行", "以及", "一个", "页面"]) {
      fragments.delete(stop);
    }
    return fragments;
  }

  function allValues(key) {
    return [...new Set(styles.map((style) => style[key]).filter(Boolean))];
  }

  function countBy(key, value) {
    return styles.filter((style) => style[key] === value).length;
  }

  function renderFilter(container, key, current) {
    const values = allValues(key);
    const entries = [["all", "全部", styles.length], ...values.map((value) => [value, labels[key][value] || value, countBy(key, value)])];
    container.innerHTML = entries.map(([value, label, count]) => `
      <label class="filter-option">
        <input type="radio" name="${key}" value="${escapeHtml(value)}" ${current === value ? "checked" : ""}>
        <span>${escapeHtml(label)}</span>
        <span class="filter-count">${count}</span>
      </label>
    `).join("");
  }

  function renderFilters() {
    renderFilter(elements.registerFilters, "register", state.register);
    renderFilter(elements.surfaceFilters, "surface", state.surface);
    renderFilter(elements.densityFilters, "density", state.density);
  }

  function scoreStyle(style, query) {
    if (!query) {
      return { score: 0, reasons: [] };
    }

    const text = normalize(query);
    const queryFragments = semanticFragments(text);
    const reasons = [];
    let score = 0;

    for (const cue of style.cues) {
      const normalizedCue = normalize(cue);
      if (normalizedCue && (text.includes(normalizedCue) || normalizedCue.includes(text))) {
        score += 5;
        reasons.push(`命中场景：${cue}`);
        continue;
      }
      const overlap = [...semanticFragments(cue)].filter((fragment) => queryFragments.has(fragment));
      if (overlap.length) {
        score += Math.min(4, overlap.length);
        reasons.push(`语义相关：${cue}`);
      }
    }

    for (const [register, signals] of Object.entries(registerSignals)) {
      if (signals.some((signal) => text.includes(signal))) {
        if (style.register === register) {
          score += 3;
          reasons.push(`职责匹配：${labels.register[register]}`);
        } else {
          score -= 1;
        }
      }
    }

    for (const avoid of style.avoid) {
      const normalizedAvoid = normalize(avoid);
      if (normalizedAvoid && text.includes(normalizedAvoid)) {
        score -= 8;
        reasons.push(`命中排他：${avoid}`);
      }
    }

    if (/高密度|密集|大量|表格|值班|排障|监控/.test(text) && style.density === "tight") {
      score += 2;
      reasons.push("密度匹配：紧");
    }
    if (/长文|阅读|慢慢|报告|文章/.test(text) && style.density === "roomy") {
      score += 2;
      reasons.push("密度匹配：松");
    }
    if (/深色|夜间|暗色/.test(text) && style.surface === "dark") {
      score += 2;
      reasons.push("明暗匹配：深色");
    }
    if (/浅色|明亮|白天|打印/.test(text) && style.surface === "light") {
      score += 2;
      reasons.push("明暗匹配：浅色");
    }

    return { score, reasons: [...new Set(reasons)].slice(0, 3) };
  }

  function filteredStyles() {
    const scored = styles.map((style, index) => ({
      style,
      index,
      ...scoreStyle(style, state.query)
    }));

    return scored
      .filter(({ style }) => state.register === "all" || style.register === state.register)
      .filter(({ style }) => state.surface === "all" || style.surface === state.surface)
      .filter(({ style }) => state.density === "all" || style.density === state.density)
      .sort((a, b) => {
        if (b.score !== a.score) {
          return b.score - a.score;
        }
        return a.index - b.index;
      });
  }

  function styleRow(scored) {
    const { style, reasons } = scored;
    const selected = state.selected === style.slug;
    const comparing = state.compare.includes(style.slug);
    const atLimit = state.compare.length >= 3 && !comparing;
    const detail = reasons.length ? reasons.join("，") : style.description;
    const specimenStyle = [
      `--mini-bg:${style.canvas}`,
      `--mini-ink:${style.ink}`,
      `--mini-accent:${style.accent || style.ink}`
    ].join(";");

    return `
      <li class="style-row ${selected ? "is-selected" : ""}" data-slug="${escapeHtml(style.slug)}">
        <button class="style-main" type="button" data-select="${escapeHtml(style.slug)}" aria-pressed="${selected}">
          <span class="mini-specimen" style="${escapeHtml(specimenStyle)}" aria-hidden="true"></span>
          <span>
            <span class="style-name">${escapeHtml(style.name)}</span>
            <span class="style-slug">${escapeHtml(style.slug)}</span>
          </span>
        </button>
        <span class="style-description">${escapeHtml(detail)}</span>
        <span class="style-facets">
          <span class="facet">${escapeHtml(labels.register[style.register] || style.register)}</span>
          <span class="facet">${escapeHtml(labels.surface[style.surface] || style.surface)}</span>
          <span class="facet">${escapeHtml(labels.density[style.density] || style.density)}</span>
          <button class="compare-toggle" type="button" data-compare="${escapeHtml(style.slug)}" aria-pressed="${comparing}" aria-label="${comparing ? "移出比较" : "加入比较"}" ${atLimit ? "disabled" : ""}>${comparing ? "−" : "+"}</button>
        </span>
      </li>
    `;
  }

  function renderList(scored) {
    elements.styleList.innerHTML = scored.map(styleRow).join("");
    elements.visibleCount.textContent = scored.length;
    elements.emptyState.hidden = scored.length !== 0;
    elements.styleList.hidden = scored.length === 0;

    const recommended = scored.filter((item) => item.score > 0);
    if (state.query && recommended.length) {
      elements.taskHint.textContent = `按“${state.query}”推荐，先看 ${recommended.slice(0, 3).map((item) => item.style.name).join("、")}。`;
      elements.recommendationMeta.innerHTML = recommended.slice(0, 3).map((item) =>
        `<span>${escapeHtml(item.style.name)}：${escapeHtml(item.reasons[0] || "综合匹配")}</span>`
      ).join("");
      elements.resultsTitle.textContent = "推荐风格";
    } else if (state.query) {
      elements.taskHint.textContent = `没有风格直接命中“${state.query}”。下面保留筛选结果，先看排他条件或考虑新增风格。`;
      elements.recommendationMeta.innerHTML = "";
      elements.resultsTitle.textContent = "无直接匹配";
    } else {
      elements.taskHint.textContent = "还没有任务描述。浏览全部风格，或在上方输入具体场景。";
      elements.recommendationMeta.innerHTML = "";
      elements.resultsTitle.textContent = "全部风格";
    }
  }

  function detailMarkup(style) {
    if (!style) {
      return "<p>选择一个风格查看详情。</p>";
    }
    const importCode = `<link rel="stylesheet" href="styles/${style.slug}/tokens.css">\n<div class="${style.className || `ds-${style.slug}`}">…</div>`;
    const cues = style.cues.map((item) => `<li>${escapeHtml(item)}</li>`).join("");
    const avoid = style.avoid.map((item) => `<li>${escapeHtml(item)}</li>`).join("");

    return `
      <h2 class="style-title">${escapeHtml(style.name)}</h2>
      <p class="style-summary">${escapeHtml(style.description)}</p>
      <div class="meta-line">
        <span>${escapeHtml(labels.register[style.register] || style.register)}</span>
        <span>${escapeHtml(labels.surface[style.surface] || style.surface)}</span>
        <span>${escapeHtml(labels.density[style.density] || style.density)}</span>
        <span>${escapeHtml(style.status || "stable")}</span>
      </div>
      <section class="detail-section">
        <h3>什么时候用</h3>
        <ul class="detail-list">${cues}</ul>
      </section>
      <section class="detail-section">
        <h3>绝对别用</h3>
        <ul class="detail-list">${avoid}</ul>
      </section>
      <section class="detail-section">
        <h3>接入</h3>
        <pre class="code-block">${escapeHtml(importCode)}</pre>
        <div class="detail-actions">
          <button class="button button-primary" type="button" data-copy="${escapeHtml(importCode)}">复制代码</button>
          <a class="button" href="../styles/${escapeHtml(style.slug)}/DESIGN.md">读 DESIGN.md</a>
        </div>
        <p class="copy-state" role="status" aria-live="polite"></p>
      </section>
    `;
  }

  function renderDetail() {
    const style = bySlug.get(state.selected) || styles[0];
    if (!style) {
      elements.styleDetail.innerHTML = "<p>没有可显示的风格。</p>";
      elements.mobileDetail.innerHTML = "";
      return;
    }

    const markup = detailMarkup(style);
    elements.styleDetail.innerHTML = markup;
    elements.mobileDetail.innerHTML = markup;
    elements.previewFrame.src = `../${style.previewUrl}`;
    elements.previewFrame.title = `${style.name} 预览`;
    elements.previewLabel.textContent = style.slug;
    elements.openPreview.href = `../${style.previewUrl}`;
    elements.styleVersion.textContent = `v${style.version || "1"} · ${style.status || "stable"}`;
  }

  function renderCompareState() {
    elements.compareCount.textContent = state.compare.length;
    elements.compareBarCount.textContent = state.compare.length;
    elements.compareBar.hidden = state.compare.length === 0;
  }

  function syncUrl() {
    const params = new URLSearchParams();
    if (state.query) params.set("q", state.query);
    if (state.register !== "all") params.set("register", state.register);
    if (state.surface !== "all") params.set("surface", state.surface);
    if (state.density !== "all") params.set("density", state.density);
    if (state.selected) params.set("style", state.selected);
    history.replaceState(null, "", `${location.pathname}${params.size ? `?${params}` : ""}`);
  }

  function render() {
    const scored = filteredStyles();
    if (!scored.some((item) => item.style.slug === state.selected)) {
      state.selected = scored[0] ? scored[0].style.slug : "";
    }
    renderList(scored);
    renderDetail();
    renderCompareState();
    renderFilters();
    syncUrl();
  }

  function setFilter(key, value) {
    state[key] = value;
    render();
  }

  function toggleCompare(slug) {
    const active = state.compare.includes(slug);
    if (active) {
      state.compare = state.compare.filter((item) => item !== slug);
    } else if (state.compare.length < 3) {
      state.compare = [...state.compare, slug];
    }
    render();
  }

  async function copyText(text, status) {
    try {
      await navigator.clipboard.writeText(text);
      status.textContent = "已复制接入代码。";
    } catch (error) {
      const area = document.createElement("textarea");
      area.value = text;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.append(area);
      area.select();
      const copied = document.execCommand("copy");
      area.remove();
      status.textContent = copied ? "已复制接入代码。" : "复制失败，请手动选择代码。";
    }
  }

  function openComparison() {
    if (state.compare.length < 2) {
      return;
    }
    const columns = state.compare.map((slug) => bySlug.get(slug)).filter(Boolean);
    elements.compareGrid.style.setProperty("--compare-count", String(columns.length));
    elements.compareGrid.innerHTML = columns.map((style) => `
      <section class="compare-column">
        <header>
          <h3>${escapeHtml(style.name)}</h3>
          <p>${escapeHtml(labels.register[style.register] || style.register)}，${escapeHtml(labels.surface[style.surface] || style.surface)}，${escapeHtml(labels.density[style.density] || style.density)}</p>
        </header>
        <iframe title="${escapeHtml(style.name)} 比较预览" src="../${escapeHtml(style.previewUrl)}"></iframe>
      </section>
    `).join("");
    elements.compareDialog.showModal();
  }

  function bindEvents() {
    elements.searchForm.addEventListener("submit", (event) => {
      event.preventDefault();
      state.query = elements.query.value.trim();
      state.selected = "";
      render();
    });

    elements.query.addEventListener("input", () => {
      state.query = elements.query.value.trim();
      state.selected = "";
      render();
    });

    function reset() {
      state.query = "";
      state.register = "all";
      state.surface = "all";
      state.density = "all";
      state.selected = "";
      state.compare = [];
      elements.query.value = "";
      render();
    }

    elements.resetButton.addEventListener("click", reset);
    elements.filterReset.addEventListener("click", reset);
    elements.filterToggle.addEventListener("click", () => {
      const open = !document.body.classList.contains("filters-open");
      document.body.classList.toggle("filters-open", open);
      elements.filterToggle.setAttribute("aria-expanded", String(open));
    });

    for (const container of [elements.registerFilters, elements.surfaceFilters, elements.densityFilters]) {
      container.addEventListener("change", (event) => {
        const input = event.target.closest("input[name]");
        if (input) {
          setFilter(input.name, input.value);
        }
      });
    }

    elements.styleList.addEventListener("click", (event) => {
      const selectButton = event.target.closest("[data-select]");
      if (selectButton) {
        state.selected = selectButton.dataset.select;
        render();
        return;
      }
      const compareButton = event.target.closest("[data-compare]");
      if (compareButton) {
        toggleCompare(compareButton.dataset.compare);
      }
    });

    document.addEventListener("click", (event) => {
      const copyButton = event.target.closest("[data-copy]");
      if (copyButton) {
        const status = copyButton.closest(".detail-section").querySelector(".copy-state");
        copyText(copyButton.dataset.copy, status);
      }
    });

    elements.openCompare.addEventListener("click", openComparison);
    elements.closeCompare.addEventListener("click", () => elements.compareDialog.close());
    elements.compareDialog.addEventListener("click", (event) => {
      if (event.target === elements.compareDialog) {
        elements.compareDialog.close();
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "/" && document.activeElement !== elements.query) {
        event.preventDefault();
        elements.query.focus();
      }
    });
  }

  function hydrateFromUrl() {
    const params = new URLSearchParams(location.search);
    state.query = params.get("q") || "";
    state.register = params.get("register") || "all";
    state.surface = params.get("surface") || "all";
    state.density = params.get("density") || "all";
    state.selected = params.get("style") || state.selected;
    elements.query.value = state.query;
  }

  function boot() {
    elements.buildState.textContent = `${styles.length} 个风格 · ${payload.generatedAt || "未注明构建时间"}`;
    hydrateFromUrl();
    bindEvents();
    render();
  }

  boot();
})();

