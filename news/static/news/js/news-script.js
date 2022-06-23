
// News modals
// Gets the modal
var articleModal = document.getElementById('articleModal');

// Listens for it's activation
articleModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;

    // Gets article content
    var title = button.querySelector('#title').innerText;
    var content = button.querySelector('#content-holder').innerHTML;
    var image = button.querySelector('#news-image-holder').innerHTML;
    
    // Changes modal content
    let modalTitle = document.getElementById('newsModalTitle');
    let modalBody = document.getElementById('newsModalBody');
    let modalImage = document.getElementById('newsModalImage');

    modalTitle.innerText = title;
    modalBody.innerHTML = content;
    modalImage.innerHTML = image;

});