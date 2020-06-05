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

////  Functional Code  ////

// Main
$(document).ready( function() {
  console.log("Ready!");
  $("#intro").hide();
  $("#intro").fadeIn(2000);


});
