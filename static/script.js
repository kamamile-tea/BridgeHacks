// news
function imagess(props1, props2, props3) {
  console.log(typeof props1);
  console.log(props2);
  console.log(props3);
  $(".newsbackground1").css("background-image","url("+props1+")");

  $(".newsbackground2").css("background-image","url("+props2+")");

  $(".newsbackground3").css("background-image","url("+props3+")");
  
  return 0;
}

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-100%";
  }
  prevScrollpos = currentScrollPos;
}

/* Open when someone clicks on the span element */
function openNav() {
  document.getElementById("donation").style.width = "100%";
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
  document.getElementById("donation").style.width = "0%";
}


//Bot POPUP

var bot = document.getElementById("poptext");

bot.onclick = function() {
   modal.style.display = "popuptext";
 }


// donation POPUP
var modal = document.getElementById("myModal2");

var btn = document.getElementById("myBtn2");


var span = document.getElementsByClassName("close2")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}


// test
function openForm() {
  document.getElementById("botHelp").style.display = "block";
}

function closeForm() {
  document.getElementById("botHelp").style.display = "none";
}
