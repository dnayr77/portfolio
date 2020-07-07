////  Page-scoped globals  ////


const KEYS = {
  left: 37,
  up: 38,
  right: 39,
  down: 40,
  shift: 16,
  spacebar: 32
};

let createThrowingItemIntervalHandle;
let currentThrowingFrequency = 2000;
var mdeIndex = 1;

////  Functional Code  ////

// Main
$(document).ready( function() {
  console.log("Ready!");
  $("#intro").hide();
  $("#intro").fadeIn(2000);
});

showSlides(mdeIndex);

// Next/previous controls
function plusSlides(n, gallery) {
  if (gallery == 1) {
    showSlides(mdeIndex += n);
  }
}

// Thumbnail image controls
function currentSlide(n, gallery) {
  showSlides(mdeIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mde_image");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {mdeIndex = 1}
  if (n < 1) {mdeIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[mdeIndex-1].style.display = "block";
  dots[mdeIndex-1].className += " active";
}
