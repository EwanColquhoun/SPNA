let button = document.getElementById('contact-button')
let modal = document.getElementById('myModal')
let closeButtons = document.querySelectorAll('.modal-close-button')


button.addEventListener('click', function() {
    modal.classList.add('show')
    modal.style.display = 'block'
    close()
});
    
   
function close() {
    closeButtons.forEach((close) => 
        close.addEventListener('click', function() {
            modal.style.display = 'none'
            modal.classList.remove('show')
        }));
};