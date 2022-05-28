
/**
 * @jest-environment jsdom
*/

import * as spna from "../spna_admin.js";

// describe("Select box test", () => {
//     // beforeAll(() => {
//     //     document.body.innerHTML = `
//     //         <input type="password" name="password1" placeholder="Password" autocomplete="new-password" required id="id_password1">
//     //         <input type="password" name="password2" placeholder="Password Again" autocomplete="new-password" required id="id_password2">`
//     // })

//     beforeAll(() => {
//         let fs = require("fs");
//         let fileContents = fs.readFileSync("spna_admin/templates/spna_admin/spna_admin.html", "utf-8");
//         document.open();
//         document.write(fileContents);
//         document.close();
//     });

describe("Select box test", () => {
    // Below html mocked as Jest doesn't recognise the email form where the id_email_to element lives.
    beforeAll(() => {
        document.body.innerHTML = `
            <tr>
                <td>
                    <input id="members-select-all" type="checkbox" >
                </td>
                <td>
                    <input id="contacts-select-all" type="checkbox" >
                </td>
                <td>
                    <input type="checkbox" id="select1" class="member-select-box select-box" name="email" value="testemail@email.com">
                </td>
                <td>
                    <input type="checkbox" id="select2" class="member-select-box select-box" name="email" value="allemails@email.com">
                </td>
                  <td>
                    <input type="checkbox" id="select3" class="contact-select-box member-select-box select-box" name="email" value="third@email.com">
                </td>
                <td>
                    <input type="checkbox" id="select4" class="contact-select-box member-select-box select-box" name="email" value="fourth@email.com">
                </td>
            </tr>
            <div class="text-center">
                <h2 id="id_email_to" value=''>Email To</h2>
            </div>
            `
    })

    test("Check Select All boxes", () => {
        const spy = jest.spyOn(spna, 'selectButton')
        let emailField = document.querySelector('#id_email_to');

        var cbs = document.querySelectorAll('.contact-select-box');
        var mbs = document.querySelectorAll('.member-select-box');
    
        spna.selectButton()
        mbs[0].click()
        cbs[0].click()
        let attr = mbs[0]['checked']
        let attr2 = cbs[0]['checked']
        expect(spy).toHaveBeenCalled();
        expect(attr).toBeTruthy();
        expect(attr2).toBeTruthy();
        // let emailList = spna.selectButton.emailList
        let emailList = emailField.value;
        let mail = emailList.toString(emailList)
        expect(mail).toMatch("testemail@email.com,third@email.com")
    })

    test("Check Contact select boxes", () => {
        const spy = jest.spyOn(spna, 'checkAllContacts')
        let emailField = document.querySelector('#id_email_to');
        let selectAll = document.getElementById('contacts-select-all')

        selectAll.addEventListener('change', spna.checkAllContacts)
        spna.checkAllContacts()
        selectAll.click()
        let attr = selectAll['checked']
        expect(spy).toHaveBeenCalled();
        expect(attr).toBeTruthy();
        let emailList = emailField.value;
        let mail = emailList.toString(emailList)
        expect(mail).toMatch("third@email.com,fourth@email.com")
    })

    test("Check Member select boxes", () => {
        const spy = jest.spyOn(spna, 'checkAllMembers')
        let emailField = document.querySelector('#id_email_to');
        let selectAll = document.getElementById('members-select-all')
        selectAll.addEventListener('change', spna.checkAllMembers)

        spna.checkAllMembers()
        selectAll.click()
        let attr = selectAll['checked']
        expect(spy).toHaveBeenCalled();
        expect(attr).toBeTruthy();
        let emailList = emailField.value;
        let mail = emailList.toString(emailList)
        expect(mail).toMatch("testemail@email.com")
    })

})

