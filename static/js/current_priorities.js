console.log("JS is working");

// Button Listeners

$("#pay-with-card").click(function(event){
  console.log('You Clicked Me!')
  $("#payment-form").css("display", "inline-block");
})

document.getElementById("pay-with-card").addEventListener("click",function(){
  
});


// Amount Listeners
var giveAmount;
giveAmountDisplay = document.getElementById("giveAmount");
give500 = document.getElementById("give500");
give500.addEventListener("click", function () {
  giveAmountDisplay.value = 500;
});

give250 = document.getElementById("give250");
give250.addEventListener("click", function () {
  giveAmountDisplay.value = 250;
});

give100 = document.getElementById("give100");
give100.addEventListener("click", function () {
  giveAmountDisplay.value = 100;
});

give50 = document.getElementById("give50");
give50.addEventListener("click", function () {
  giveAmountDisplay.value = 50;
});


// Create instance of stripe object
var stripe = Stripe(
  "pk_test_51HTs1OH4cLdMvnO91CZWJGqJvVXZx3t1TGW6KJoJCY9GZ1m6pQg665wwdlCgpPn1w1hhfuWjMXVjVSb58RjTz0j6008Fjw8TwM"
);

// Create Elements instance: Manages a group of elements
var elements = stripe.elements();

// Create a card element
var card = elements.create("card");

// Mount Card element
card.mount("#card-element");

// Real time card errors
card.on("change", function (event) {
  var displayError = document.getElementById("card-errors");
  if (event.error) {
    displayError.textContent = event.error.message;
  } 
});

// Form Submission
var form = document.getElementById("payment-form");
var clientSecret = document.getElementById("clientSecret").value;
const csrftoken = document.cookie.slice(10);
form.addEventListener("submit", function (event) {
  event.preventDefault();
  const amount = document.getElementById("giveAmount").value


  stripe.createToken(card).then(function (result) {
    if (result.error) {
      var errorElement = document.getElementById("card-error");
      errorElement.textContent = result.error.message;
    } else {
      stripeTokenHandler(result.token)
    }
  });
  console.log("Form Submitted");
});



function stripeTokenHandler(token) {
  var form = document.getElementById("payment-form");
  var hiddenInput = document.createElement("input");
  hiddenInput.setAttribute("type", "hidden");
  hiddenInput.setAttribute("name", "stripeToken");
  hiddenInput.setAttribute("value", token.id);
  form.appendChild(hiddenInput)
  tokenInput = document.getElementsByName("stripeToken")
  console.log(tokenInput)
  form.submit();
}

