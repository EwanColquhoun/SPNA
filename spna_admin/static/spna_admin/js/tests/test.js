
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
                    <input type="checkbox" id="select1" class="member-select-box select-box" name="email" value="testemail@email.com">
                </td>
                <td>
                    <input type="checkbox" id="select2" class="member-select-box select-box" name="email" value="noEmail">
                </td>
            </tr>
            <div class="text-center">
                <h2 id="id_email_to" value=''>Email To</h2>
            </div>
            `
    })

    test("Check members select boxes", () => {
        const spy = jest.spyOn(spna, 'selectButton')
        let emailField = document.querySelector('#id_email_to');
        let selectButtonTest = document.querySelectorAll('.select-box')
        // let emailList = []
        spna.selectButton()
        selectButtonTest[0].click()
        let attr = selectButtonTest[0]['checked']
        expect(spy).toHaveBeenCalled();
        expect(attr).toBeTruthy();
        let emailList = emailField.value;
        let mail = emailList.toString(emailList)
        expect(mail).toMatch("testemail@email.com")
    })

})

