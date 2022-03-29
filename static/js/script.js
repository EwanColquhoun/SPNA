// Back to top button
$('.btt-link').click(function(e) {
    window.scrollTo(0,0)
})

// Alerts
var alertList = document.querySelectorAll('.alert')
var alerts =  [].slice.call(alertList).map(function (element) {
  return new bootstrap.Alert(element)
})

var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'))
var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
  return new bootstrap.Dropdown(dropdownToggleEl)
})

// setTimeout(function () {
//     let messages = document.getElementById('msg');
//     let alert = new bootstrap.Alert(messages);
//     if (messages) {
//     messages.classList.remove('show');
//     }
// }, 5000);

