// Gets the delete document modal working
const delete_buttons = document.querySelectorAll('.delete-doc-button');
let modal = document.querySelector('#delete-doc-modal');

if (delete_buttons.length !== 0) {
    delete_buttons.forEach((button) => {
        button.addEventListener('click', function () {
        let document_id = button.getAttribute('data-name');
        let modalButton = document.getElementById('doc-modal-delete-button');

        modal.addEventListener('shown.bs.modal', function () {
            modalButton.setAttribute('href', `/spna_admin/delete/document/${document_id}`);
        });
    });
})}

// Shows the matched passwords as green boxes for enhanced UX
let password = document.querySelectorAll('#id_password1');
 if (password.length >= 1) {
    passwordMatch();
  }
function passwordMatch() {
    let password1 = document.getElementById('id_password1');
    let password2 = document.getElementById('id_password2');

    password2.addEventListener("input", function pMatch() {
        if (password2.value === password1.value) {
            password2.classList.add('matched');
            password1.classList.add('matched');
            return true;
        } else {
            password2.classList.remove('matched');
            password1.classList.remove('matched');
            return false;
        }
    });
}

// stripe
function card(stripe_publishable_key, customer_email) {
    document.addEventListener("DOMContentLoaded", function(event){
    let cS = document.getElementById('client_secret');
    let clientSecret = cS.getAttribute('value');
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
        }
      });
    });
    });
}
