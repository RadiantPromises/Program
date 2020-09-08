$(document).ready(() => {


  // Reoccuring Payments Checkbox
  $(".reoccuring-check").click((e) => {
    if ($(e.target).hasClass("checked")) {
      $(e.target).removeClass("checked");
    } else {
      $(e.target).addClass("checked");
    }
  });

  // Donation Type Drop Down Menus
  $(".arrow-large").click((e) => {
    if ($(e.target).hasClass("left")) {
      $(e.target).removeClass("left");
      $(e.target).addClass("down");
      console.log($(e.target.parentElement.parentElement))
    } else if ($(e.target).hasClass("down")) {
      $(e.target).removeClass("down");
      $(e.target).addClass("left");
    }
  });

// Item Drop Down Menus
  $(".arrow-small").click((e) => {
    if ($(e.target).hasClass("left")) {
      $(e.target).removeClass("left");
      $(e.target).addClass("down");
    } else if ($(e.target).hasClass("down")) {
      $(e.target).removeClass("down");
      $(e.target).addClass("left");
    }
  });
});
