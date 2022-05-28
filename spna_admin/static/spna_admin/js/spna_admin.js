window.addEventListener('DOMContentLoaded', function() {
    checkAllContacts()
    checkAllMembers()
    selectButton()
    console.log('ready')
})

let msa = document.getElementById('members-select-all')
msa.addEventListener('change', checkAllMembers)

let csa = document.getElementById('contacts-select-all')
csa.addEventListener('change', checkAllContacts)


// Variables
let emailField = document.querySelector('#id_email_to');
let emailList = [];
let selectButtons = document.querySelectorAll('.select-box');

// Activated the checkbox to autopopulate email_to field
function selectButton() {
    selectButtons.forEach((person) => {
        person.addEventListener('change', function () {
            if (person.checked) {
                let addy = person.getAttribute('value')
                emailList.push(addy);
            } else {
                emailList.pop(-1)
            }
            emailField.value = emailList
        });
    });
};

// select all from: https://stackoverflow.com/questions/7251005/javascript-select-all-checkboxes-in-a-table

// Select box for all members
function checkAllMembers() {
    var cbs = document.querySelectorAll('.member-select-box');
    // let emailField = document.querySelector('#id_email_to')
    // let emailList = []

    for(var i=0; i < cbs.length; i++) {

        if(cbs[i].type == 'checkbox') {
            cbs[i].checked = this.checked;
             if (cbs[i].checked) {
                let addy = cbs[i].getAttribute('value')
                console.log(addy)
                emailList.push(addy);
            } else {
                emailList.pop(-1)
            }
        };
        emailField.value = emailList
    };
};

// Selectbox for all contacts
function checkAllContacts() {
    var cbs = document.querySelectorAll('.contact-select-box');

    for(var i=0; i < cbs.length; i++) {
        if(cbs[i].type == 'checkbox') {
        cbs[i].checked = this.checked;
         if (cbs[i].checked) {
                let addy = cbs[i].getAttribute('value')
                console.log(addy)
                emailList.push(addy);
            } else {
                emailList.pop(-1)
            }
        };
        emailField.value = emailList
        }
};

// Bootstrap tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Gets the delete modal working
const modal_buttons = document.getElementById('delete-cont-modal-buttons');
const delete_buttons = document.querySelectorAll('.delete-cont-button');
let modal = document.querySelector('#delete-cont-modal')

if (delete_buttons.length !== 0) {
delete_buttons.forEach((button) => {
    button.addEventListener('click', function () {
    const contact_id = button.getAttribute('data-name');
    let modalButton = document.querySelector('#cont-modal-delete-button')

    modal.addEventListener('shown.bs.modal', function () {
        modalButton.setAttribute('href', `/spna_admin/delete/contact/${contact_id}`);
    });
});
})};

export {selectButton, checkAllContacts, checkAllMembers}