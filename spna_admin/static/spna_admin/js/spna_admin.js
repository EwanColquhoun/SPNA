
window.addEventListener('DOMContentLoaded', function() {
    selectButton();
    let csa = document.getElementById('contacts-select-all');
    csa.addEventListener('change', checkAllContacts);
    let msa = document.getElementById('members-select-all');
    msa.addEventListener('change', checkAllMembers);
});
// Variables
let emailList = [];

// Activated the individual checkbox to autopopulate email_to field
function selectButton() {
    let emailField = document.querySelector('#id_email_to');
    let selectButtons = document.querySelectorAll('.select-box');

    selectButtons.forEach((person) => {
        let addy = person.getAttribute('value');
        person.addEventListener('change', function () {
            if (person.checked) {
                emailList.push(addy);
            } else {
                emailList.shift(addy);
            }
            emailField.value = emailList;
        });
    });
}

// select all from: https://stackoverflow.com/questions/7251005/javascript-select-all-checkboxes-in-a-table

// Select box for all members
function checkAllMembers() {
    var mbs = document.querySelectorAll('.member-select-box');
    let emailField = document.querySelector('#id_email_to');

    for(var i=0; i < mbs.length; i++) {
        if(mbs[i].type == 'checkbox') {
            mbs[i].checked= this.checked;
            let addy = mbs[i].getAttribute('value');
            if (mbs[i].checked) {
                emailList.push(addy);
            } else {
                emailList.shift(addy);
            }
        }
        emailField.value = emailList;
    }
}

// Selectbox for all contacts
function checkAllContacts() {
    var cbs = document.querySelectorAll('.contact-select-box');
    let emailField = document.querySelector('#id_email_to');

    for(var i=0; i < cbs.length; i++) {
        if(cbs[i].type == 'checkbox') {
            cbs[i].checked = this.checked;
            let addy = cbs[i].getAttribute('value');
            if (cbs[i].checked) {
                emailList.push(addy);
            } else {
                emailList.shift(addy);
            }
        }
        emailField.value = emailList;
        }
}

// Bootstrap tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

// Gets the delete modal working
const delete_buttons = document.querySelectorAll('.delete-cont-button');
let modal = document.querySelector('#delete-cont-modal');

if (delete_buttons.length !== 0) {
delete_buttons.forEach((button) => {
    button.addEventListener('click', function () {
    const contact_id = button.getAttribute('data-name');
    let modalButton = document.querySelector('#cont-modal-delete-button');

    modal.addEventListener('shown.bs.modal', function () {
        modalButton.setAttribute('href', `/spna_admin/delete/contact/${contact_id}`);
    });
	});
})};

export {selectButton, checkAllContacts, checkAllMembers};