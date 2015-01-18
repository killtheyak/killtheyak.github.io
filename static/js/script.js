(function() {
  $('.dep-code-container').toggle();

  $('a.dep-name').on('click', function(e) {
    e.preventDefault();
    return $(this).siblings().siblings('.dep-code-container').fadeToggle(200);
  });

}).call(this);
