$(document).ready(() => {
  // Reoccuring Payments Checkbox
  $(".reoccuring-check").click((e) => {
    if ($(e.target).hasClass("checked")) {
      $(e.target).removeClass("checked");
    } else {
      $(e.target).addClass("checked");
    }
  });

  // Card Body Display (Type & Item)
  $(".arrow-large, .arrow-small").click((e) => {
    // console.log($(e.target.parentElement.nextElementSibling).css("display"))
    // console.log($(e.target).find(':nth-child(2)')) Header as button
    if ($(e.target).hasClass("left")) {
      $(e.target).removeClass("left");
      $(e.target).addClass("down");
      // Show Body
      $(e.target.parentElement.nextElementSibling).css("display", "block");
      if ($(e.target).hasClass("arrow-small")) {
        $(e.target.parentElement.parentElement).css("display", "block"); // Item
      }
      // $(e.target.parentElement).css("display","block");
    } else if ($(e.target).hasClass("down")) {
      $(e.target).removeClass("down");
      $(e.target).addClass("left");
      // Hide Body
      $(e.target.parentElement.nextElementSibling).css("display", "none");
    }
  });
  // Select Giving Option(s)
  $(".amount-checkbox, .remainder-checkbox, .full-amount-checkbox").click(
    (e) => {
      let isChecked = $(e.target).prop("checked");
      let donationInput = $(e.target.nextElementSibling.nextElementSibling);
      if (isChecked) {
        donationInput.prop("disabled", false);
      } else {
        donationInput.prop("disabled", true);
      }
    }
  );

  // Add to Cart
});
