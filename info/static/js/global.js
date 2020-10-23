console.log("JS is working");

$(document).ready(function () {
  console.log("Document is ready");

  // Color Navbar link to current page
  let page = $("#Page").val();
  let pageId = '#' + page
  $(pageId).css("color", "#EC5E86");
  console.log($('.menu-toggle').css("display"))
  console.log($('.nav-links').css("display"))
  $('.menu-toggle').click(function(){
    console.log('Menu Clicked');
  //   console.log($('.menu-toggle').css("display"))
    if ($('.nav-links').css("display")=="flex"){
      console.log('Nav links are flexing!!')
      $('.nav-links').css("display","none")
    }
    else if($('.nav-links').css("display")=="none"){
      $('.nav-links').css("display","flex")
    }
  })
});
