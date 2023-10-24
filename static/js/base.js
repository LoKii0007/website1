
// ---------------navabar------------------

const menuBtn = document.querySelector(".menu-icon");
const cancelBtn = document.querySelector(".cancel-icon");
const items = document.querySelector(".nav-item2");
const nav2 = document.querySelector(".box2");
const nav1 = document.querySelector(".navbar1");


menuBtn.onclick = () => {
  items.classList.add("active2");
  menuBtn.classList.add("hide2");
  cancelBtn.classList.add("show2");
  nav2.classList.add("navbar2");
  nav1.classList.add("navcol");
}

cancelBtn.onclick = () => {
  items.classList.remove("active2");
  menuBtn.classList.remove("hide2");
  cancelBtn.classList.remove("show2");
  // nav2.classList.remove("navbar2");
  cancelBtn.style.color = "#ff3d00";
  nav1.classList.remove("navcol");

}

/* ------------------reveal animation----------------- */

window.addEventListener('scroll', reveal);

function reveal() {
  var reveals = document.querySelectorAll('.reveal');

  for (var i = 0; i < reveals.length; i++) {
    var windowheight = window.innerHeight;
    var revealtop = reveals[i].getBoundingClientRect().top;
    var revealpoint = 50;

    if (revealtop < windowheight - revealpoint) {
      reveals[i].classList.add('active1');
    }
    else {
      reveals[i].classList.remove('active1');
    }
  }
}