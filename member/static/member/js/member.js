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

// stripe
var stripePublicKey = document.querySelector('#stripe_public_key').value;
var clientSecret = document.querySelector('#client_secret').value;
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
console.log('card', card)
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-error');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});