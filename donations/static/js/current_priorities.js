console.log("JS is working")

// Create instance of stripe object
var stripe = Stripe(
  "pk_test_51HTs1OH4cLdMvnO91CZWJGqJvVXZx3t1TGW6KJoJCY9GZ1m6pQg665wwdlCgpPn1w1hhfuWjMXVjVSb58RjTz0j6008Fjw8TwM"
);

// Create Elements instance: Manages a group of elements
var elements = stripe.elements();

// Create a card element
var card = elements.create("card")

// Mount Card element
card.mount("#card-element")