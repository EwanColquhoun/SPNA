function _3dsec(stripe_publishable_key, pi_secret) {
    document.addEventListener("DOMContentLoaded", function(event){
      var stripe = Stripe(stripe_publishable_key);
      let redBut = document.getElementById('redirect-button')
      let spinner = document.getElementById('loading-overlay-secure')
    
      stripe.confirmCardPayment(pi_secret).then(function(result) {
        if (result.error) {
          // Display error.message in your UI.
          $("#3ds_result").text("Error! Please try to sign up again.");
          $("#3ds_result").addClass("text-danger");
          spinner.style.display = 'none'

        } else {
          // The payment has succeeded. Display a success message.
          spinner.style.display = 'none'
          $("#3ds_result").text("Thank you for your payment, please log in using the button.");
          $("#3ds_result").addClass("text-success");
          redBut.addEventListener('click', function(){
            window.location.replace("https://8000-ewancolquhoun-spna-jrhwr7uwb6e.ws-eu38.gitpod.io/accounts/login/")
          }
          )
        }
      });
    }); // DOMContentLoaded
}