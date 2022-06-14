// Back to top button
let btt = document.getElementById('btt-link')

btt.addEventListener('click', function(){
    window.scrollTo(0,0)
})

$(document).ready(function() {
  jQuery.fn.carousel.Constructor.TRANSITION_DURATION = 5000  // 5 seconds
});

function alerts() {
  setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    if (messages) {
      messages.classList.remove('show');
    }
  }, 4000);
}

document.addEventListener('DOMContentLoaded', alerts())
