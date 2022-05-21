// Gets the delete modal working


const modal_buttons = document.getElementById('delete-modal-buttons');
const delete_buttons = document.querySelectorAll('.delete-doc-button');
let modal = document.querySelector('#delete-doc-modal')

if (delete_buttons.length !== 0) {
delete_buttons.forEach((button) => {
    button.addEventListener('click', function () {
    let document_id = button.getAttribute('data-name');
    let modalButton = document.querySelector('#doc-modal-delete-button')

    modal.addEventListener('shown.bs.modal', function () {
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
                // payWithCard(stripe, card, clientSecret);
            }
            });
              // Create Payment Method END
        }
      });
    });
    });
}


// var payWithCard = function(stripe, card, clientSecret) {
//   loading(true);
//   stripe
//     .confirmCardPayment(clientSecret, {
//       payment_method: {
//         card: card
//       },
//       billing_details: {
//                     email: customer_email,
//                     name: fullname,
//                 },
//     })
//     .then(function(result) {
//       if (result.error) {
//         spinner.style.display = 'none'
//         // Show error to your customer
//         showError(result.error.message);
//       } else {
//         // The payment succeeded!
//         orderComplete();
//       }
//     });
// };

/* ------- UI helpers ------- */

// Shows a success message when the payment is complete
// var orderComplete = function() {
//     loading(false);
//     spinner.style.display = 'none'
//     document.querySelector("#submit-button").disabled = true;
//     // window.location.assign("https://8000-ewancolquhoun-spna-jrhwr7uwb6e.ws-eu39b.gitpod.io/accounts/login/")
//     customAlert = document.createElement('div')
//     customAlert.setAttribute('class', 'alert alert-success alert-dismissible fade show')
//     customAlert.innerHTML = `
//         Thank you for your payment. Please visit the members area for more information.
//         <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>`
//     document.appendChild(customAlert)
    
// };

// Show the customer the error from Stripe if their card fails to charge
// var showError = function(errorMsgText) {
//   loading(false);
//   var errorMsg = document.querySelector("#card-error");
//   errorMsg.textContent = errorMsgText;
//   setTimeout(function() {
//     errorMsg.textContent = "";
//   }, 4000);
// };

// Show a spinner on payment submission
// var loading = function(isLoading) {
//   if (isLoading) {
//     // Disable the button and show a spinner
//     document.querySelector("button").disabled = true;
//     document.querySelector("#spinner").classList.remove("hidden");
//     document.querySelector("#button-text").classList.add("hidden");
//   } else {
//     document.querySelector("button").disabled = false;
//     document.querySelector("#spinner").classList.add("hidden");
//     document.querySelector("#button-text").classList.remove("hidden");
//   }
// };

// Stripe token handler
// function stripeTokenHandler(token) {
//     var form = document.getElementById('payment-form');
//     var hiddenInput = document.createElement('input');
//     hiddenInput.setAttribute('type', 'hidden');
//     hiddenInput.setAttribute('name', 'stripeToken');
//     hiddenInput.setAttribute('id', 'stripeToken');
//     hiddenInput.setAttribute('value', token.id);
//     form.appendChild(hiddenInput);
//     form.submit();
// }

// create customer and subscription 
// function createCustomerAndSubscription(customerEmail, stripeToken, planId) {
//     return stripe.customers.create({
//         source: stripeToken,
//         email: customerEmail
//     }).then(customer => {
//         stripe.subscriptions.create({
//         customer: customer.id,
//         items: [
//             {
//             plan: planId
//             }
//         ]
//         });
//     });
// }

// ORIGINALFORM SUBMIT 

    // Handle form submission.
           
    // var form = document.getElementById('payment-form');
    // form.addEventListener('submit', function(event) {
    //     event.preventDefault();
        
    //     stripe.createToken(card).then(function(result) {
    //     if (result.error) {
    //         // Inform the user if there was an error.
    //         var errorElement = document.getElementById('card-errors');
    //         errorElement.textContent = result.error.message;
    //     } else {
    //         // hides card and shows spinner
    //         let spinner = document.getElementById('loading-overlay')
    //         form.classList.add('fade-payment');
    //         spinner.style.display = 'block'
    //         // Create Payment Method BEGIN
    //         console.log('paymentmethod')
    //         stripe.createPaymentMethod({
    //             type: 'card',
    //             card: card,
    //             billing_details: {
    //                 email: customer_email,
    //                 name: fullname,
    //             },
    //         }).then(function(payment_method_result){ 
    //         if (payment_method_result.error) {
    //              // hides spinner and shows card
    //             var form = document.getElementById('payment-form');
    //             spinner.style.display = "none"
    //             form.classList.remove('fade-payment')
    //             form.classList.add('show-payment')
    //             console.log(payment_method_result, 'PMR')
    //             var errorElement = document.getElementById('card-errors');
    //             errorElement.textContent = payment_method_result.error.message;
    //         } else {
    //             console.log(payment_method_result, 'PMR')
    //             var form = document.getElementById('payment-form');
                
    //             var hiddenInput = document.createElement('input');

    //             hiddenInput.setAttribute('type', 'hidden');
    //             hiddenInput.setAttribute('name', 'payment_method_id');
    //             hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id);

    //             form.appendChild(hiddenInput);
    //             // Submit the form
    //             // if (result.paymentIntent.status === 'succeeded') {
    //             //     form.submit();
    //             // }
    //             form.submit();
    //         };
    //         });
    //         // Create Payment Method END
    //     }
    //     }); // createToken

    // }); // form.addEventListener(..)
// })
// };

