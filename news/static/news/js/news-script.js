// // News modals



$( document ).ready( function(){

    var articleModal = document.getElementById('articleModal')

    articleModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget
        var title = button.querySelector('.title').innerText
        var content = button.querySelector('.content').innerText

        let modalTitle = document.getElementById('modalTitle')
        let modalBody = document.getElementById('modalBody')

        modalTitle.innerText = title
        modalBody.innerText = content
        console.log(content, 'title')
    })

    // $('#articleModal').on('show', function(event){
    //     // event.preventDefault();
    //     var e = $(this);
    //     var title = e.find('.title').html();
    //     var content = e.find('.content');
    //     $('#articleModal').modal('show');
    //     $('#modalTitle').replaceWith(title);
    //     $('#modalBody').replaceWith(content);
    
    // });
//     closeModal();
//     $.when("click", "hide").then(removeText());
//     // removeText();
} );



// function removeText() {
//     $('.modal').change('hide', function() {
//         $('#modalTitle').text("Title");
//         $('#modalBody').text("Content");
//         console.log('click!');
//         console.log('hide!');
//     });
// };

// function closeModal() {
//     $('.art-modal-close-button').click(function(){
//         $('#articleModal').modal('hide');
//     })
// }
