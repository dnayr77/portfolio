////  Page-scoped globals  ////


const KEYS = {
  left: 37,
  up: 38,
  right: 39,
  down: 40,
  shift: 16,
  spacebar: 32
};


var photoIndex = {"mde": 0, "insta": 0, "budget": 0, "bio": 0, "thrive": 0};

////  Functional Code  ////

// Main
$(document).ready( function() {
  console.log("Ready!");
  $("#intro").hide();
  $("#intro").fadeIn(2000);
});


// Next/previous controls
function plusSlides(n, gallery) {
  showSlides(photoIndex[gallery] += n, gallery);
  if(gallery == "bio") {
    showText(gallery);
  }
}

// Thumbnail image controls
function currentSlide(n, gallery) {
  showSlides(photoIndex[gallery] = n, gallery);
  if(gallery == "bio") {
    showText(gallery);
  }
}

function showText(gallery) {
  var i;
  var slides = document.getElementsByName(gallery + "_text");
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[photoIndex[gallery]].style.display = "block";
}

function showSlides(n, gallery) {
  var i;
  var slides = document.getElementsByName(gallery + "_image");
  var dots = document.getElementsByName(gallery + "_dot");
  if (n >= slides.length) {photoIndex[gallery] = 0;}
  if (n < 0) {photoIndex[gallery] = slides.length-1;}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[photoIndex[gallery]].style.display = "block";
  dots[photoIndex[gallery]].className += " active";
}
