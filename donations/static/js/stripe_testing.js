// Creates an instance of the stripe object
var stripe = Stripe(
  "pk_test_51HTs1OH4cLdMvnO91CZWJGqJvVXZx3t1TGW6KJoJCY9GZ1m6pQg665wwdlCgpPn1w1hhfuWjMXVjVSb58RjTz0j6008Fjw8TwM"
);

//  Creates an Elements instance, which manages a group of elements.
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
  base: {
    color: "#32325d",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#fa755a",
    iconColor: "#fa755a",
  },
};

// Test payment request
var paymentRequest = stripe.paymentRequest({
  country: "US",
  currency: "usd",
  total: {
    label: "Demo total",
    amount: 1000,
  },
  requestPayerName: true,
  requestPayerEmail: true,
});

// Create instances of the Element.
var card = elements.create("card", { style: style });


var applePayElement = elements.create("paymentRequestButton", {
  paymentRequest: paymentRequest,
  style: {
    paymentRequestButton: {
      theme: "light",
    },
  },
});

// Add an instance of the card Element into the `card-element` <div>.
card.mount("#card-element");
applePayElement.mount("#apple-pay-element");

// LISTENERS
elements.on(ready, function () {});

// Handle real-time validation errors from the card Element.
card.on("change", function (event) {
  console.log("Changes")
  var displayError = document.getElementById("card-errors");
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = "";
  }
});

// Handle form submission.
var form = document.getElementById("payment-form");
var client_secret = document.getElementById("client_secret");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  console.log("Form Submitted")
  console.log(form["first_name"])

  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: form["first_name"],
        },
      },
    })
    .then(function (result) {
      if (result.error) {
        // Show error to your customer (e.g., insufficient funds)
        console.log(result.error.message);
      } else {
        // The payment has been processed!
        if (result.paymentIntent.status === "succeeded") {
          // Show a success message to your customer
          // There's a risk of the customer closing the window before callback
          // execution. Set up a webhook or plugin to listen for the
          // payment_intent.succeeded event that handles any business critical
          // post-payment actions.
        }
      }
    });

  stripe.createToken(card).then(function (result) {
    if (result.error) {
      // Inform the user if there was an error.
      var errorElement = document.getElementById("card-error");
      errorElement.textContent = result.error.message;
    } else {
      // Send the token to your server.
      stripeTokenHandler(result.token);
    }
  });
});

// Submit the form with the token ID.
function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server
  var form = document.getElementById("payment-form");
  var hiddenInput = document.createElement("input");
  hiddenInput.setAttribute("type", "hidden");
  hiddenInput.setAttribute("name", "stripeToken");
  hiddenInput.setAttribute("value", token.id);
  form.appendChild(hiddenInput);
  alert(token.id)
  // Submit the form
  form.submit();
}
