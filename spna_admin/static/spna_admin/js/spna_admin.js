let selectButtons = document.querySelectorAll('.select-box')
let emailField = document.querySelector('#id_email_to')
let emailList = []

selectButtons.forEach((person) => {
    person.addEventListener('change', function () {
        if (person.checked) {
            let addy = person.getAttribute('value')
            emailList.push(addy);
            console.log(emailList)
        } else {
            emailList.pop(-1)
        }
        emailField.value = emailList
    })
})