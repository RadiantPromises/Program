console.log("JS is working");

$(document).ready(function () {
  console.log("Document is ready");

  // Color Navbar link to current page
  let page = $("#Page").val();
  let pageId = '#' + page
  $(pageId).css("color", "#EC5E86");
});
