$('.dep-code-container').toggle() # Hide all dependency code blocks

$('a.dep-name').on('click', (e) ->
    e.preventDefault()
    console.log $(this).siblings('.dep-code-container')
    $(this).siblings().siblings('.dep-code-container').fadeToggle()
)
