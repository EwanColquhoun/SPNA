let articleModal = document.getElementById('articleModal')
let articleButton = document.querySelectorAll('.modal-button')
let newsCloseBtn = document.querySelectorAll('.modal-close-button')
let title = document.querySelector('news-modal-title')
let body = document.getElementsByClassName('news-modal-body')
let cardTitle = document.getElementsByClassName('card-title')
let cardBody = document.getElementsByClassName('card-body')

console.log(articleButton)

articleButton.forEach((button) => 
    button.addEventListener('click', function(event) {
        let info = event.button.firstChild.value
        console.log(info, 'info')
// trying to get modal to show the news article that was clicked on in the modal.
        close()
        articleModal.classList.add('show')
        articleModal.style.display = 'block'
        title.innerText = text
    }));
    
   
function close() {
    newsCloseBtn.forEach((close) => 
        close.addEventListener('click', function() {
            articleModal.style.display = 'none'
            articleModal.classList.remove('show')
        }));
};

articleModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var recipient = button.getAttribute('data-bs-whatever')
    // If necessary, you could initiate an AJAX request here
    // and then do the updating in a callback.
    //
    // Update the modal's content.
    var modalTitle = exampleModal.querySelector('.modal-title')
    var modalBodyInput = exampleModal.querySelector('.modal-body input')
  
    modalTitle.textContent = 'New message to ' + recipient
    modalBodyInput.value = recipient
  })