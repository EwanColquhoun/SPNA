// // Gets the delete modal working


// const del_modal_buttons = document.getElementById('doc-modal-delete-button');
const delete_buttons = document.querySelectorAll('.delete-doc-button');
let modal = document.querySelector('#delete-doc-modal')
console.log(delete_buttons)

if (delete_buttons.length !== 0) {
    delete_buttons.forEach((button) => {
        button.addEventListener('click', function () {
        let document_id = button.getAttribute('data-name');
        let modalButton = document.getElementById('doc-modal-delete-button')
        console.log(document_id, 'doc.id')

        modal.addEventListener('shown.bs.modal', function () {
            console.log(document_id)
            modalButton.setAttribute('href', `/spna_admin/delete/document/${document_id}`);
        });
    });
})};

// stripe
function card(stripe_publishable_key, customer_email) {
    document.addEventListener("DOMContentLoaded", function(event){
    let cS = document.getElementById('client_secret');
    let clientSecret = cS.getAttribute('value')
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
            },
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };
    var card = elements.create('card', {style: style});
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
            errorDiv.innerHtml(html);
        } else {
            errorDiv.textContent = '';
        }
    });
    var form = document.getElementById('payment-form');

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();

        stripe.createToken(card).then(function(result) {
        if (result.error) {
          var errorElement = document.getElementById('card-errors');
          errorElement.textContent = result.error.message;
        } else {
            let spinner = document.getElementById('loading-overlay');
            spinner.style.display = 'block';
            stripe.createPaymentMethod({
                type: 'card',
                card: card,
                billing_details: {
                    email: customer_email,
            },
            }).then(function(payment_method_result){ 
            if (payment_method_result.error) {
                spinner.style.display = 'none';

                var errorElement = document.getElementById('card-errors');
                errorElement.textContent = payment_method_result.error.message;
            } else {
                var form = document.getElementById('payment-form');
                var hiddenInput = document.createElement('input');

                hiddenInput.setAttribute('type', 'hidden');
                hiddenInput.setAttribute('name', 'payment_method_id');
                hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id);

                form.appendChild(hiddenInput);
                // Submit the form
                form.submit();
            }
            });
              // Create Payment Method END
        }
      });
    });
    });
}
