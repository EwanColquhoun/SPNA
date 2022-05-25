// htmlString = 
//           `<p class="text-danger"><strong>Payment declined.</strong> Please try to sign up again using the button below</p>
//           <div class="text-center p-5">
//       <a id="redirect-button" href="/member/subscribe" class="btn spna-btn">Sign Up</a>
//   </div>`
// $("#3ds_result").html(htmlString);
// let res = document.querySelector('#3ds_result')
// res.textContent = htmlString + two
// console.log(res)


function _3dsec(stripe_publishable_key, pi_secret) {
    document.addEventListener("DOMContentLoaded", function(event){
      
      var stripe = Stripe(stripe_publishable_key);
      // let redBut = document.getElementById('redirect-button')
      let spinner = document.getElementById('loading-overlay-secure')
    
      stripe.confirmCardPayment(pi_secret).then(function(result) {
        if (result.error) {
          htmlString = 
            `<p class="text-danger"><strong>Payment declined.</strong> Please try to sign up again using the button below</p>
            <div class="text-center p-5">
              <a id="redirect-button" href="/member/subscribe" class="btn spna-btn">Sign Up</a>
            </div>`
          $("#3ds_result").html(htmlString);
          spinner.style.display = 'none'

        } else {
          // The payment has succeeded. Display a success message.
          htmlString = 
            `<p class="text-success"><strong>Payment accepted.</strong> Please continue to the SPNA site</p>
            <div class="text-center p-5">
              <a id="redirect-button" href="/" class="btn spna-btn">SPNA Home</a>
            </div>`
          $("#3ds_result").html(htmlString);
          spinner.style.display = 'none'
          // window.location.href = 'https://scottishpna.herokuapp.com/accounts/login/'
        }
      });
    }); // DOMContentLoaded
}