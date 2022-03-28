// // News modals

// $( document ).ready( function(){
// 
    // Gets the modal
    var articleModal = document.getElementById('articleModal')

    // Listens for it's activation
    articleModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget

        // Gets article content
        var title = button.querySelector('.title').innerText
        var content = button.querySelector('.content').innerText
        
        // Changes modal content
        let modalTitle = document.getElementById('modalTitle')
        let modalBody = document.getElementById('modalBody')

        modalTitle.innerText = title
        modalBody.innerText = content
    })
// } );
