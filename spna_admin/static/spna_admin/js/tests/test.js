
/**
 * @jest-environment jsdom
*/

import * as spna from "../spna_admin.js";

describe("Select box test", () => {
    // beforeAll(() => {
    //     document.body.innerHTML = `
    //         <input type="password" name="password1" placeholder="Password" autocomplete="new-password" required id="id_password1">
    //         <input type="password" name="password2" placeholder="Password Again" autocomplete="new-password" required id="id_password2">`
    // })

    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("spna_admin/templates/spna_admin/spna_admin.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });

    test("Check members select boxes", () => {
        let selectButtons = document.querySelectorAll('.select-box');
        const spy = jest.spyOn(spna, 'checkAllMembers')
        let cbs = document.querySelectorAll('.member-select-box')[0]

        // Need to 'check' the box here to get the email in the emaillist.

        spna.checkAllMembers()
        expect(spy).toHaveBeenCalled();
        // expect(tfs.passwordMatch).toBeTruthy()
        let emailField = document.querySelector('#id_email_to');
        let emailList = [];
        expect(emailList).toMatch(/{{user.email}}/)

    })

})

