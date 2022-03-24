$('#contact-button').click('shown.bs.modal', function() {
    console.log('button press')
})

let button = document.getElementById('contact-button')
let modal = document.getElementById('myModal')

button.addEventListener('click', function() {
    modal.classList.add('show')
    modal.style.display = 'block'
    console.log('show')
})
    
modal.addEventListener('shown.bs.modal', function () {
    button.focus()
    console.log('focus')
  })
