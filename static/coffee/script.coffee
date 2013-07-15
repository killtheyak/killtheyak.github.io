$('.dep-code-container').toggle() # Hide all dependency code blocks

$('a.dep-name').on('click', (e) ->
    e.preventDefault()
    $(this).siblings().siblings('.dep-code-container').fadeToggle()
)
