"use strict";

(function (_jQuery) {
  const $ = _jQuery, jQuery = _jQuery;
  if (window.dbdpInitialized) return;
  window.dbdpInitialized = true;
  /**
   * @typedef {object} WidgetInstance
   * @property {WidgetInputConfig} config
   * @property {jQueryElement} $element
   * @property {DateTimePickerData} dateTimePickerData
   *
   * @typedef {object} DateTimePickerData
   * @property {Function} date
   *
   * @typedef {object} WidgetOptions
   * @property {string | undefined} minDate
   * @property {string | undefined} maxDate
   * @property {object} icons
   *
   * @typedef {object} WidgetInputConfig
   * @property {string} variant
   * @property {string} backend_date_format
   * @property {WidgetOptions} options
   * @property {string} range_from
   */

  const inputWrapperClass = "dbdp";
  /** @type {WeakMap<HTMLInputElement, WidgetInstance>} */
  const widgetInstances = new WeakMap();
  /** @type {WidgetOptions} */
  const defaultWidgetOptions = {
    icons: {
      time: 'bi-clock',
      date: 'bi-calendar',
      up: 'bi-chevron-up',
      down: 'bi-chevron-down',
      previous: 'bi-chevron-left',
      next: 'bi-chevron-right',
      today: 'bi-record-circle',
      clear: 'bi-trash',
      close: 'bi-x-lg'
    }
  }

  document.addEventListener('DOMContentLoaded', function (event) {
    setTimeout(() => findAndProcessInputs(document));
    const observer = new MutationObserver((mutationsList, observer) => {
      for (const mutation of mutationsList) {
        if (mutation.type === 'childList') {
          const addedNodes = Array.from(mutation.addedNodes);
          addedNodes.forEach(node => {
            if (node.querySelectorAll) {
              findAndProcessInputs(node);
            }
          });
        }
      }
    });
    observer.observe(document, { childList: true, subtree: true });
  });

  /**
   * @param {HTMLElement} htmlElement
   */
  function findAndProcessInputs(htmlElement) {
    /** @type {NodeListOf<HTMLInputElement>} */
    const inputElements = htmlElement.querySelectorAll('[data-dbdp-config]:not([disabled])')
    for (const inputElement of inputElements) {
      try {
        if (!jQuery) throw new DisplayError("You have to load jQuery before form.media");
        if (!("moment" in window)) throw new DisplayError("momentjs was not loaded, is your momentjs_url valid?");
        if (!("datetimepicker" in jQuery.fn)) throw new DisplayError("datetimepicker js was not loaded, is your datetimepicker_js_url valid?");
        processInputElement(inputElement);
      } catch (err) {
        handleErrorAndThrow(err, inputElement);
      }
    }
  }

  /**
   * @param {HTMLInputElement} inputElement
   */
  function processInputElement(inputElement) {
    const initialValue = inputElement.value;
    const config = getConfig(inputElement);
    const inputWrapper = inputElement.closest(`.${inputWrapperClass}`);
    if (!inputWrapper) throw Error(`input must have a parent with class="${inputWrapperClass}"`)
    createAltInputElement(inputElement, inputWrapper);

    if (!config.options.format) config.options.format = config.backend_date_format.replace(/-01/g, "")
    if (config.range_from) config.options.useCurrent = false; // based on https://github.com/Eonasdan/tempus-dominus/issues/1075
    const widgetInstance = createWidgetInstance(inputWrapper, inputElement, config);
    widgetInstances.set(inputElement, widgetInstance);

    const form = inputElement.closest("form");
    form?.addEventListener("reset", () => {
      setTimeout(() => {
        widgetInstance.dateTimePickerData.date(initialValue ? moment(initialValue, config.backend_date_format) : null);
      });
    })

    if (config.range_from) {
      const widgetRangeFromInstance = getRangeFromInputElement(inputElement, config);
      if (widgetRangeFromInstance) {
        configureRangeSelection(widgetRangeFromInstance, widgetInstance);
      }
    }
  }

  /**
   * @param {HTMLInputElement} inputElement
   * @param {HTMLInputElement} inputWrapper
   */
  function createAltInputElement(inputElement, inputWrapper) {
    const altInputElement = document.createElement("input");
    const skipAttrs = ["name", "type", "value", "data-dbdp-config", "data-dbdp-debug"];
    for (const attrName of inputElement.getAttributeNames()) {
      if (skipAttrs.includes(attrName)) continue;
      altInputElement.setAttribute(attrName, inputElement.getAttribute(attrName));
      inputElement.removeAttribute(attrName);
    }
    altInputElement.dataset.name = inputElement.getAttribute("name");
    inputElement.setAttribute("type", "hidden");
    inputElement.after(altInputElement);
    inputWrapper.after(inputElement);
    return altInputElement;
  }

  /**
   * @param {HTMLElement} inputWrapper
   * @param {HTMLInputElement} inputElement
   * @param {WidgetInputConfig} config
   */
  function createWidgetInstance(inputWrapper, inputElement, config) {
    const $inputWrapper = jQuery(inputWrapper).datetimepicker(config.options);
    /** @type {WidgetInstance} */
    const widgetInstance = { config, $element: $inputWrapper, dateTimePickerData: $inputWrapper.data("DateTimePicker") }
    widgetInstance.dateTimePickerData.date(moment(inputElement.value, config.backend_date_format));
    widgetInstance.$element.on("dp.change", function (e) {
      inputElement.value = e.date ? e.date.format(config.backend_date_format) : null;
    });
    for (let [eventName, handler] of Object.entries(config.events)) {
      widgetInstance.$element.on(eventName, handler);
    }
    return widgetInstance;
  }

  /**
   * @param {HTMLInputElement} inputElement
   */
  function getConfig(inputElement) {
    let /** @type {WidgetInputConfig} */ config;
    try {
      config = JSON.parse(inputElement.dataset.dbdpConfig);
    }
    catch (err) { throw Error("Invalid input config") }
    const optionKeyName = inputElement.name.replace(/^(.*-)?/, "dbdpOptions_")
    config.options = { ...defaultWidgetOptions, ...window.dbdpOptions, ...window[optionKeyName], ...config.options };
    config.events = { ...window.dbdpEvents, ...window[optionKeyName.replace("dbdpOptions_", "dbdpEvents_")] };
    return config;
  }

  /**
   * @param {HTMLInputElement} inputElement
   * @param {WidgetInputConfig} config
   */
  function getRangeFromInputElement(inputElement, config) {
    const rangeFromInputName = inputElement.name.replace(/[^-]+$/, config.range_from);
    let fromInputElement = inputElement.form?.elements.namedItem(rangeFromInputName);
    if (!fromInputElement) {
      const elements = document.querySelectorAll(`input[name="${config.range_from}"]`);
      if (elements.length == 0) throw Error("range_from not found");
      if (elements.length > 1) throw Error("Multiple range_from found");
      fromInputElement = elements[0];
    }
    if (widgetInstances.has(fromInputElement)) {
      return widgetInstances.get(fromInputElement);
    } else {
      throw Error(`range_from "${config.range_from}" is not a widget input`);
    }
  }

  /**
   * @param {WidgetInstance} fromInstance
   * @param {WidgetInstance} toInstance
   */
  function configureRangeSelection(fromInstance, toInstance) {
    const initialFromInstanceMaxMoments = fromInstance.config.options.maxDate ? [moment(fromInstance.config.options.maxDate)] : [];
    const initialToInstanceMinMoments = toInstance.config.options.minDate ? [moment(toInstance.config.options.minDate)] : [];
    const toCurrentDate = toInstance.dateTimePickerData.date();
    const fromCurrentDate = fromInstance.dateTimePickerData.date();
    const fromInstanceMaxMoments = initialFromInstanceMaxMoments.concat(toCurrentDate ? [toCurrentDate] : []);
    const toInstanceMinMoments = initialToInstanceMinMoments.concat(fromCurrentDate ? [fromCurrentDate] : []);
    fromInstance.dateTimePickerData.maxDate(fromInstanceMaxMoments.length ? moment.min(fromInstanceMaxMoments) : false);
    toInstance.dateTimePickerData.minDate(toInstanceMinMoments.length ? moment.max(toInstanceMinMoments) : false);

    fromInstance.$element.on("dp.change", function (e) {
      const toInstanceMinMoments = initialToInstanceMinMoments.concat(e.date ? [e.date] : []);
      toInstance.dateTimePickerData.minDate(toInstanceMinMoments.length ? moment.max(toInstanceMinMoments) : false);
    });

    toInstance.$element.on("dp.change", function (e) {
      const fromInstanceMaxMoments = initialFromInstanceMaxMoments.concat(e.date ? [e.date] : []);
      fromInstance.dateTimePickerData.maxDate(fromInstanceMaxMoments.length ? moment.min(fromInstanceMaxMoments) : false);
    });
  }

  class DisplayError extends Error { }
  class WidgetError extends Error {
    /**
     * @param {HTMLInputElement} inputElement
     * @param {string} message
     * @param {boolean} shouldDisplay
     */
    constructor(inputElement, message) {
      super(`input name: ${inputElement.name || inputElement.dataset.name}; ${message}`);
      this.name = "django-bootstrap-datepicker-plus error";
    }
  }

  /**
   * @param {Error} error
   * @param {HTMLInputElement?} inputElement
   */
  function handleErrorAndThrow(error, inputElement) {
    if (inputElement.dataset.dbdpDebug !== undefined) {
      const errorMessage = error instanceof DisplayError ? error.message : "Something went wrong! Check browser console for errors.";
      const errorDisplay = document.createElement("div");
      errorDisplay.className = "alert alert-danger"
      errorDisplay.innerHTML = `${errorMessage}. This message is only visible when DEBUG=True`;
      inputElement.closest(`.${inputWrapperClass}`).after(errorDisplay);
    }
    throw new WidgetError(inputElement, error.message);
  }

  if ("bootstrap" in window) { // if bootstrap version >= 4
    $('body').on("dp.show", `.${inputWrapperClass}`, function (e) {
      $(e.target).find('.collapse.in').addClass('show');
    });
    $('body').on('show.bs.collapse', '.bootstrap-datetimepicker-widget .collapse', function (e) {
      $(e.target).addClass('in');
    });
    $('body').on('hidden.bs.collapse', '.bootstrap-datetimepicker-widget .collapse', function (e) {
      $(e.target).removeClass('in');
    });
  }
})(window.jQuery);
