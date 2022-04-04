window.addEventListener('DOMContentLoaded', function() {
    checkAllContacts()
    checkAllMembers()
    selectButton()
    console.log('ready')
})


function selectButton() {
    let selectButtons = document.querySelectorAll('.select-box')
    let emailField = document.querySelector('#id_email_to')
    let emailList = []

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

let msa = document.getElementById('members-select-all')
msa.addEventListener('change', checkAllMembers)

let csa = document.getElementById('contacts-select-all')
csa.addEventListener('change', checkAllContacts)

function checkAllMembers() {
    var cbs = document.querySelectorAll('.member-select-box');

    for(var i=0; i < cbs.length; i++) {

        if(cbs[i].type == 'checkbox') {
            cbs[i].checked = this.checked;
        };
    };
};


function checkAllContacts() {
    var cbs = document.querySelectorAll('.contact-select-box');

    for(var i=0; i < cbs.length; i++) {
        if(cbs[i].type == 'checkbox') {
        cbs[i].checked = this.checked;
        }
    }
}
