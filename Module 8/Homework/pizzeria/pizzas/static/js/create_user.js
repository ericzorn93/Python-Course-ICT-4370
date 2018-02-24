var inputs = document.querySelectorAll('input');

for (var i = 0; i < inputs.length; i++) {
    inputs[i].classList.add('form-control');
}

// Set Input Placeholders
inputs[1].setAttribute('placeholder', 'Please Enter Username Here');
inputs[2].setAttribute('placeholder', 'Please Enter Password Here');
inputs[3].setAttribute('placeholder', 'Please Confirm Password Here');



//check for navigation time API support
if (window.performance) {
  console.info("window.performance work's fine on this browser");
}

if (window.performance.navigation.type == 1) {
    var reloaded = document.getElementById("reloadOutput");
    reloaded.innerHTML = "*Username was Successfully Created. Please Proceed to Login Page Link";
    console.info( "This page is reloaded" );
} else {
    console.info( "This page is not reloaded");
}