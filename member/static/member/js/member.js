// Gets the delete modal working


const modal_buttons = document.getElementById('delete-modal-buttons');
const delete_buttons = document.querySelectorAll('.delete-button');
let modal = document.querySelector('#delete-modal')

if (delete_buttons.length !== 0) {
delete_buttons.forEach((button) => {
    button.addEventListener('click', function () {
    const document_id = button.getAttribute('data-name');
    let modalButton = document.querySelector('#modal-delete-button')

    modal.addEventListener('shown.bs.modal', function () {
        modalButton.setAttribute('href', `/member/delete/${document_id}`);
    });
});
})};