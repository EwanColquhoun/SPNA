function _3dsec(stripe_publishable_key, pi_secret) {
    document.addEventListener("DOMContentLoaded", function(event){
      var stripe = Stripe(stripe_publishable_key);
      // let redBut = document.getElementById('redirect-button')
      let spinner = document.getElementById('loading-overlay-secure')
    
      stripe.confirmCardPayment(pi_secret).then(function(result) {
        if (result.error) {
          // Display error.message in your UI.
          htmlString = `
            <p class="text-danger">Error! Please try to sign up again using the button below</p>
            <div class="text-center p-5">
                <a id="redirect-button" href="{% url 'subscribe' %}" class="btn spna-btn">Enter the SPNA</a>
            </div>`
          $("#3ds_result").text(htmlString);
          // $("#3ds_result").addClass("text-danger");
          // $("#3ds_result").html("text-danger");
          spinner.style.display = 'none'


        } else {
          // The payment has succeeded. Display a success message.
          window.location.href = 'https://8000-ewancolquhoun-spna-jrhwr7uwb6e.ws-eu39b.gitpod.io/accounts/login/'
        }
      });
    }); // DOMContentLoaded
}