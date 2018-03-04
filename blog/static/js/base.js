function toggleMobileNav() {
  var mobileNav = document.
    getElementsByClassName('mobile-site-nav')[0].children[0];
  if (mobileNav.className === "nav-items") {
    mobileNav.className += "-toggle";
  } else {
    mobileNav.className = "nav-items";
  }
}
