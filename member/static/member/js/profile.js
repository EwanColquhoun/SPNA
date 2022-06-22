function cardUpdate(stripe_publishable_key, customer_email) {
    document.addEventListener("DOMContentLoaded", function(event){
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

    var form = document.getElementById('update-payment-form');
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();

        stripe.createToken(card).then(function(result) {
        if (result.error) {
          var errorElement = document.getElementById('card-errors');
          errorElement.textContent = result.error.message;
        } else {
            let pm = stripe.createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
                email: customer_email,
            },
            }).then(function(payment_method_result){ 
            if (payment_method_result.error) {
                spinner.style.display = 'none'
                var errorElement = document.getElementById('card-errors');
                errorElement.textContent = payment_method_result.error.message;
            } else {
                var form = document.getElementById('update-payment-form');
                var hiddenInput = document.createElement('input');

                hiddenInput.setAttribute('type', 'hidden');
                hiddenInput.setAttribute('name', 'payment_method_id');
                hiddenInput.setAttribute('value', payment_method_result.paymentMethod.id);

                form.appendChild(hiddenInput);
                // Submit the form
                form.submit();
            };
            });
          }
        })
    });
    });
};
