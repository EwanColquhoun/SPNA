
/**
 * @jest-environment jsdom
*/

import * as spna from "../member.js";

describe("Password match test", () => {
    beforeAll(() => {
        document.body.innerHTML = `
            <input type="password" name="password1" placeholder="Password" autocomplete="new-password" required id="id_password1">
            <input type="password" name="password2" placeholder="Password Again" autocomplete="new-password" required id="id_password2">`
    })

    test("Check passwords match", () => {
        let password1 = document.getElementById('id_password1')
        let password2 = document.getElementById('id_password2')
        password1.value = 'testpassword'
        password2.value = 'testpassword'
        const spy = jest.spyOn(spna, 'passwordMatch')
        spna.passwordMatch();
        expect(spy).toHaveBeenCalled();
        expect(spy).toHaveBeenCalled();
        expect(spna.passwordMatch).toBeTruthy()
    })

})
