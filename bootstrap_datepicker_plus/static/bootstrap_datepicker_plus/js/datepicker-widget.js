(function (factory) {
  if (typeof define === 'function' && define.amd)
  define(['jquery'], factory)
  else if (typeof module === 'object' && module.exports)
  module.exports = factory(require('jquery'))
  else
  factory(jQuery)
}(function ($) {
  var datepickerDict = {};
  const bootstrapVersion = (window.bootstrap?.Collapse||$.fn.collapse.Constructor).VERSION;
  var isBootstrap4 = bootstrapVersion.split('.').shift() === "4";
  var isBootstrap5 = bootstrapVersion.split('.').shift() === "5";
  function fixMonthEndDate(e, picker) {
    e.date && picker.val().length && picker.val(e.date.endOf('month').format('YYYY-MM-DD'));
  }
  function initOnePicker(element, options) {
    var $element = $(element), data = {};
    try {
      data = JSON.parse($element.attr('data-dp-config'));
    }
    catch (x) { }
    $.extend(1, data.options, options);
    if (data.id && data.options) {
      data.$element = $element.datetimepicker(data.options);
      data.datepickerdata = $element.data("DateTimePicker");
      data.$element.next('.input-group-addon').on('click', function() {
        data.datepickerdata.show();
      });
      if (isBootstrap4 || isBootstrap5) {
        data.$element.on("dp.show", function(e) {
          $('.collapse.in').addClass('show');
        });
      }
    }
    return data;
  };
  function initLinkedPickers(to_picker) {
    var from_picker = datepickerDict[to_picker.linked_to];
    from_picker.datepickerdata.maxDate(to_picker.datepickerdata.date() || false);
    to_picker.datepickerdata.minDate(from_picker.datepickerdata.date() || false);
    from_picker.$element.on("dp.change", function (e) {
      to_picker.datepickerdata.minDate(e.date || false);
    });
    to_picker.$element.on("dp.change", function (e) {
      if (to_picker.picker_type == 'MONTH') fixMonthEndDate(e, to_picker.$element);
      from_picker.datepickerdata.maxDate(e.date || false);
    });
    if (to_picker.picker_type == 'MONTH') {
      to_picker.$element.on("dp.hide", function (e) {
        fixMonthEndDate(e, to_picker.$element);
      });
      fixMonthEndDate({ date: to_picker.datepickerdata.date() }, to_picker.$element);
    }
  };
  $.fn.djangoDatetimePicker = function(options){
    options = options || {};
    var newPickers = {};
    $.each(this, function (i, element) {
      var picker = initOnePicker($(element), options);
      newPickers[picker.id] = picker;
    });
    $.extend(datepickerDict, newPickers);
    $.each(newPickers, function (i, picker) {
      if (picker.linked_to)
        initLinkedPickers(picker);
    });
    return this;
  }
  $(function(){
    $("[data-dp-config]:not([disabled])").djangoDatetimePicker();
    if (isBootstrap4 || isBootstrap5) {
      $('body').on('show.bs.collapse','.bootstrap-datetimepicker-widget .collapse',function(e){
        $(e.target).addClass('in');
      });
      $('body').on('hidden.bs.collapse','.bootstrap-datetimepicker-widget .collapse',function(e){
        $(e.target).removeClass('in');
      });
    }
    if(isBootstrap5){
      $('.input-group-addon[data-target="#datetimepicker1"]').each(function (){
        $(this).attr('data-bs-target','#datetimepicker1').removeAttr('data-target')
        $(this).attr('data-bs-toggle','datetimepickerv').removeAttr('data-toggle')
      })
    }
  });
}));
