// Generated by CoffeeScript 1.4.0
(function() {

  $('.dep-code-container').toggle();

  $('a.dep-name').on('click', function(e) {
    e.preventDefault();
    console.log($(this).siblings('.dep-code-container'));
    return $(this).siblings().siblings('.dep-code-container').fadeToggle();
  });

}).call(this);
