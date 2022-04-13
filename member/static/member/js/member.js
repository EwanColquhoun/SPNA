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
function card(stripe_publishable_key, customer_email) {
    document.addEventListener("DOMContentLoaded", function(event){
    // var stripePublicKey = document.querySelector('#stripe_public_key').value;
    // var customer_email = document.querySelector('#customer_email').value;
    // var form = document.getElementById('payment-form');
    var stripe = Stripe(stripe_publishable_key);
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
        var errorDiv = document.getElementById('card-errors');
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

    // Handle form submission.
           
    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
     
        stripe.createToken(card).then(function(result) {
        if (result.error) {
            // Inform the user if there was an error.
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // hides card and shows spinner
            let spinner = document.getElementById('loading-overlay')
            form.classList.add('fade-payment');
            spinner.style.display = 'block'
            // Create Payment Method BEGIN
            console.log('paymentmethod')
            stripe.createPaymentMethod({
                type: 'card',
                card: card,
                billing_details: {
                    email: customer_email,
                    name: fullname,
            },
            }).then(function(payment_method_result){ 
            if (payment_method_result.error) {
                 // hides spinner and shows card
                spinner.stlye.display = "none"
                form.classList.remove('fade-payment')
                form.classList.add('show-payment')
                console.log(payment_method_result, 'PMR')
                var errorElement = document.getElementById('card-errors');
                errorElement.textContent = payment_method_result.error.message;
            } else {
                console.log(payment_method_result, 'PMR')
                var form = document.getElementById('payment-form');
                
                var hiddenInput = document.createElement('input');

                hiddenInput.setAttribute('type', 'hidden');
                hiddenInput.setAttribute('name', 'payment_method_id');
                hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id);

                form.appendChild(hiddenInput);
                // Submit the form
                form.submit();
            };
            });
            // Create Payment Method END
        }
        }); // createToken

    }); // form.addEventListener(..)
})
};

