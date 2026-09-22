(() => {
  "use strict";

  const panels = Array.from(document.querySelectorAll("[data-stage-panel]"));
  const stageButtons = Array.from(document.querySelectorAll("[data-stage-target]"));
  const overview = document.querySelector("#tourOverview");
  const overviewButton = document.querySelector("#overviewButton");
  const startTour = document.querySelector("#startTour");
  const exploreJourney = document.querySelector("#exploreJourney");
  const progress = document.querySelector("#tourProgress");
  const progressText = document.querySelector("#progressText");
  const contextLabel = document.querySelector("#contextLabel");
  const contextTitle = document.querySelector("#contextTitle");
  const rail = document.querySelector("#journeyRail");
  const menuButton = document.querySelector("#menuButton");
  const railBackdrop = document.querySelector("#railBackdrop");
  const toast = document.querySelector("#toast");
  const stageCount = panels.length;
  const mobileNavigation = window.matchMedia("(max-width: 900px)");
  let currentStage = -1;
  let toastTimer;

  const safeStorage = {
    get(storage, key) {
      try {
        return storage.getItem(key);
      } catch (_error) {
        return null;
      }
    },
    set(storage, key, value) {
      try {
        storage.setItem(key, value);
        return true;
      } catch (_error) {
        return false;
      }
    },
    remove(storage, key) {
      try {
        storage.removeItem(key);
        return true;
      } catch (_error) {
        return false;
      }
    },
  };

  const showToast = (message) => {
    if (!toast) return;
    window.clearTimeout(toastTimer);
    toast.textContent = message;
    toast.classList.add("show");
    toastTimer = window.setTimeout(() => toast.classList.remove("show"), 3200);
  };

  const syncRailAccessibility = () => {
    if (!rail) return;
    const hiddenMobileRail = mobileNavigation.matches && !rail.classList.contains("open");
    rail.toggleAttribute("inert", hiddenMobileRail);
    if (hiddenMobileRail) rail.setAttribute("aria-hidden", "true");
    else rail.removeAttribute("aria-hidden");
  };

  const closeRail = () => {
    rail?.classList.remove("open");
    menuButton?.setAttribute("aria-expanded", "false");
    if (railBackdrop) railBackdrop.hidden = true;
    syncRailAccessibility();
  };

  const showOverview = (options = {}) => {
    currentStage = -1;
    if (overview) overview.hidden = false;
    panels.forEach((panel) => { panel.hidden = true; });
    overviewButton?.classList.add("active");
    overviewButton?.setAttribute("aria-current", "page");
    stageButtons.forEach((button) => {
      button.classList.remove("active", "visited");
      button.removeAttribute("aria-current");
    });
    if (progress) {
      progress.value = 0;
      progress.textContent = "Overview";
    }
    if (progressText) progressText.textContent = "Overview";
    if (contextLabel) contextLabel.textContent = "Product experience";
    if (contextTitle) contextTitle.textContent = "What REEF does";
    safeStorage.remove(window.sessionStorage, "reef-tour-stage");
    closeRail();
    if (options.focus) {
      const heading = overview?.querySelector("h1");
      if (heading) {
        heading.setAttribute("tabindex", "-1");
        heading.focus({ preventScroll: true });
      }
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  const showStage = (index, options = {}) => {
    const bounded = Math.max(0, Math.min(index, stageCount - 1));
    currentStage = bounded;
    if (overview) overview.hidden = true;
    overviewButton?.classList.remove("active");
    overviewButton?.removeAttribute("aria-current");
    panels.forEach((panel, panelIndex) => {
      panel.hidden = panelIndex !== bounded;
    });
    stageButtons.forEach((button, buttonIndex) => {
      const active = buttonIndex === bounded;
      button.classList.toggle("active", active);
      button.classList.toggle("visited", buttonIndex <= bounded);
      if (active) button.setAttribute("aria-current", "step");
      else button.removeAttribute("aria-current");
    });
    if (progress) {
      progress.value = bounded + 1;
      progress.textContent = `${bounded + 1} of ${stageCount}`;
    }
    if (progressText) progressText.textContent = `${bounded + 1} of ${stageCount}`;
    if (contextLabel) contextLabel.textContent = "Case Study 001";
    if (contextTitle) contextTitle.textContent = "AI-Native Domain Modernization";
    safeStorage.set(window.sessionStorage, "reef-tour-stage", String(bounded));
    closeRail();
    if (options.focus) {
      const heading = panels[bounded]?.querySelector("h1");
      if (heading) {
        heading.setAttribute("tabindex", "-1");
        heading.focus({ preventScroll: true });
      }
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  };

  overviewButton?.addEventListener("click", () => showOverview({ focus: true }));
  startTour?.addEventListener("click", () => showStage(0, { focus: true }));
  exploreJourney?.addEventListener("click", () => {
    if (mobileNavigation.matches) {
      rail?.classList.add("open");
      menuButton?.setAttribute("aria-expanded", "true");
      if (railBackdrop) railBackdrop.hidden = false;
      syncRailAccessibility();
    }
    stageButtons[0]?.focus();
  });
  stageButtons.forEach((button) => {
    button.addEventListener("click", () => showStage(Number(button.dataset.stageTarget), { focus: true }));
  });
  document.querySelectorAll(".next-button").forEach((button) => {
    button.addEventListener("click", () => showStage(currentStage + 1, { focus: true }));
  });
  document.querySelectorAll(".previous-button").forEach((button) => {
    button.addEventListener("click", () => {
      if (currentStage === 0) showOverview({ focus: true });
      else showStage(currentStage - 1, { focus: true });
    });
  });

  menuButton?.addEventListener("click", () => {
    const open = !rail?.classList.contains("open");
    rail?.classList.toggle("open", open);
    menuButton.setAttribute("aria-expanded", String(open));
    if (railBackdrop) railBackdrop.hidden = !open;
    syncRailAccessibility();
  });
  railBackdrop?.addEventListener("click", closeRail);
  mobileNavigation.addEventListener("change", closeRail);

  document.addEventListener("keydown", (event) => {
    const target = event.target;
    const formControl = target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target instanceof HTMLSelectElement;
    if (formControl || event.altKey || event.ctrlKey || event.metaKey) return;
    if (event.key === "ArrowRight" && currentStage < stageCount - 1) {
      event.preventDefault();
      showStage(currentStage + 1, { focus: true });
    }
    if (event.key === "ArrowLeft" && currentStage === 0) {
      event.preventDefault();
      showOverview({ focus: true });
    } else if (event.key === "ArrowLeft" && currentStage > 0) {
      event.preventDefault();
      showStage(currentStage - 1, { focus: true });
    }
    if (event.key === "Escape") closeRail();
  });

  document.querySelectorAll(".simulation-action").forEach((button) => {
    button.addEventListener("click", () => showToast(button.dataset.message || "Preview only. No data changed."));
  });

  const unknownTitle = document.querySelector("#unknownTitle");
  const unknownImpact = document.querySelector("#unknownImpact");
  const unknownAction = document.querySelector("#unknownAction");
  document.querySelectorAll(".unknown-card").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".unknown-card").forEach((candidate) => candidate.classList.remove("active"));
      button.classList.add("active");
      if (unknownTitle) unknownTitle.textContent = button.dataset.unknownTitle || "";
      if (unknownImpact) unknownImpact.textContent = button.dataset.unknownImpact || "";
      if (unknownAction) unknownAction.textContent = button.dataset.unknownAction || "";
    });
  });

  const latencyRange = document.querySelector("#latencyRange");
  const latencyOutput = document.querySelector("#latencyOutput");
  const latencyEffect = document.querySelector("#latencyEffect");
  const updateLatency = () => {
    if (!latencyRange || !latencyOutput || !latencyEffect) return;
    const days = Number(latencyRange.value);
    latencyOutput.textContent = `${days} working days`;
    latencyEffect.textContent = `Illustrative schedule effect: +${(days / 7).toFixed(1)} weeks. Engineering PH unchanged.`;
  };
  latencyRange?.addEventListener("input", updateLatency);

  const scenarios = {
    traditional: { p50: "5,200 PH", p80: "6,400 PH", duration: "34 weeks", net: "0 PH", detail: "No modeled AI benefit or overhead", benefit: "0 PH", overhead: "0 PH" },
    assisted: { p50: "4,300 PH", p80: "5,500 PH", duration: "29 weeks", net: "−900 PH", detail: "−1,400 gross + 500 overhead", benefit: "−1,400 PH", overhead: "+500 PH" },
    native: { p50: "3,650 PH", p80: "4,900 PH", duration: "25 weeks", net: "−1,550 PH", detail: "−2,300 gross + 750 overhead", benefit: "−2,300 PH", overhead: "+750 PH" },
  };
  const scenarioFields = {
    p50: document.querySelector("#metricP50"),
    p80: document.querySelector("#metricP80"),
    duration: document.querySelector("#metricDuration"),
    net: document.querySelector("#metricNet"),
    detail: document.querySelector("#metricEffectDetail"),
    benefit: document.querySelector("#traceBenefit"),
    overhead: document.querySelector("#traceOverhead"),
  };
  const scenarioRadios = Array.from(document.querySelectorAll("input[name='scenario']"));
  const deliveryRadios = Array.from(document.querySelectorAll("input[name='delivery-mode']"));
  const updateScenario = (name) => {
    const scenario = scenarios[name];
    if (!scenario) return;
    Object.entries(scenarioFields).forEach(([key, element]) => {
      if (element) element.textContent = scenario[key];
    });
    scenarioRadios.forEach((radio) => { radio.checked = radio.value === name; });
    deliveryRadios.forEach((radio) => { radio.checked = radio.value === name; });
  };
  scenarioRadios.forEach((radio) => radio.addEventListener("change", () => updateScenario(radio.value)));
  deliveryRadios.forEach((radio) => radio.addEventListener("change", () => {
    updateScenario(radio.value);
    showToast(`${radio.nextElementSibling?.textContent?.trim()} selected for the illustrative comparison.`);
  }));

  document.querySelectorAll(".finding-action").forEach((button) => {
    button.addEventListener("click", () => {
      const finding = button.closest("article");
      const output = finding?.querySelector("output");
      if (output) output.textContent = button.dataset.resolution || "Updated";
      showToast("Review state changed only in this preview.");
    });
  });

  const commercialViews = {
    tm: { treatment: "Bill observed effort at synthetic role rates", detail: "Client retains volume and productivity variance.", owner: "Client" },
    fixed: { treatment: "Price an accepted scope with explicit contingency", detail: "Supplier accepts defined variance; change control protects boundary changes.", owner: "Supplier within boundary" },
    managed: { treatment: "Separate transition from steady-state service", detail: "Service levels and demand bands replace build-effort billing.", owner: "Shared by service boundary" },
  };
  const treatment = document.querySelector("#commercialTreatment");
  const commercialDetail = document.querySelector("#commercialDetail");
  const commercialOwner = document.querySelector("#commercialOwner");
  const commercialPanel = document.querySelector("#commercialPanel");
  document.querySelectorAll("[data-commercial]").forEach((button) => {
    button.addEventListener("click", () => {
      const view = commercialViews[button.dataset.commercial];
      document.querySelectorAll("[data-commercial]").forEach((candidate) => candidate.setAttribute("aria-selected", String(candidate === button)));
      if (treatment) treatment.textContent = view.treatment;
      if (commercialDetail) commercialDetail.textContent = view.detail;
      if (commercialOwner) commercialOwner.textContent = view.owner;
      if (commercialPanel) commercialPanel.setAttribute("aria-labelledby", button.id);
    });
  });

  const feedbackForm = document.querySelector("#feedbackForm");
  const feedbackStatus = document.querySelector("#feedbackStatus");
  const feedbackKey = "reef-product-experience-feedback";
  const feedbackAsObject = () => {
    if (!feedbackForm) return {};
    const data = new FormData(feedbackForm);
    return {
      confidence: data.get("confidence") || "",
      role: data.get("role") || "",
      valuable: data.get("valuable") || "",
      missing: data.get("missing") || "",
    };
  };
  const feedbackAsText = () => {
    const value = feedbackAsObject();
    return [
      "REEF product experience feedback",
      `Confidence (1-5): ${value.confidence || "Not provided"}`,
      `Role: ${value.role || "Not provided"}`,
      "",
      "Most valuable part:",
      value.valuable || "Not provided",
      "",
      "Confusing or missing:",
      value.missing || "Not provided",
      "",
      "This feedback was exported locally and was not submitted to a server.",
    ].join("\n");
  };
  const restoreFeedback = () => {
    if (!feedbackForm) return;
    const stored = safeStorage.get(window.localStorage, feedbackKey);
    if (!stored) return;
    try {
      const value = JSON.parse(stored);
      const confidence = feedbackForm.querySelector(`input[name='confidence'][value='${value.confidence}']`);
      if (confidence) confidence.checked = true;
      feedbackForm.elements.role.value = value.role || "";
      feedbackForm.elements.valuable.value = value.valuable || "";
      feedbackForm.elements.missing.value = value.missing || "";
      if (feedbackStatus) feedbackStatus.textContent = "Restored locally saved feedback. Nothing has been submitted.";
    } catch (_error) {
      if (feedbackStatus) feedbackStatus.textContent = "Saved feedback could not be restored. Nothing has been submitted.";
    }
  };
  document.querySelector("#saveFeedback")?.addEventListener("click", () => {
    const saved = safeStorage.set(window.localStorage, feedbackKey, JSON.stringify(feedbackAsObject()));
    if (feedbackStatus) feedbackStatus.textContent = saved ? "Saved in this browser. Nothing was submitted." : "Browser storage is unavailable. Nothing was submitted.";
  });
  document.querySelector("#copyFeedback")?.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(feedbackAsText());
      if (feedbackStatus) feedbackStatus.textContent = "Copied locally. Nothing was submitted.";
    } catch (_error) {
      if (feedbackStatus) feedbackStatus.textContent = "Copy was unavailable. You can still download the response.";
    }
  });
  document.querySelector("#downloadFeedback")?.addEventListener("click", () => {
    const blob = new Blob([feedbackAsText()], { type: "text/plain;charset=utf-8" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "reef-product-experience-feedback.txt";
    link.click();
    URL.revokeObjectURL(link.href);
    if (feedbackStatus) feedbackStatus.textContent = "Downloaded locally. Nothing was submitted.";
  });
  document.querySelector("#clearFeedback")?.addEventListener("click", () => {
    const cleared = safeStorage.remove(window.localStorage, feedbackKey);
    feedbackForm?.reset();
    if (feedbackStatus) feedbackStatus.textContent = cleared ? "Local feedback cleared. Nothing was submitted." : "Browser storage is unavailable. Nothing was submitted.";
  });

  restoreFeedback();
  const savedStageValue = safeStorage.get(window.sessionStorage, "reef-tour-stage");
  const savedStage = Number(savedStageValue);
  if (savedStageValue !== null && Number.isInteger(savedStage)) showStage(savedStage);
  else showOverview();
})();
