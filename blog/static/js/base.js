// Utility method to add and remove toggle to element's class name
function addRemoveToggle(inputElement) {
  switch(inputElement.className) {
    case 'nav-items':
      inputElement.className += '-toggle';
      break;
    case 'nav-items-toggle':
      inputElement.className = 'nav-items';
      break;
    case 'contact-modal':
      inputElement.className += '-toggle';
      break;
  }
}

var mobileNavButton = document.getElementById('mobile-nav-button');
mobileNavButton.addEventListener('click', function(e) {
  let mobileNav = document.getElementsByClassName(
    'mobile-site-nav')[0].children[0];
  e.preventDefault();
  addRemoveToggle(mobileNav);
});

var contactElement = document.getElementById('contact-button');
contactElement.addEventListener('click', function(e) {
  addRemoveToggle(contactModal);
  e.preventDefault();
});

var contactModal = document.getElementById('contact-modal-wrapper');
var modalCloseButton = document.getElementById('modal-close');


function clickHandler(e) {
  if(e.target.tagName == "DIV") {
    if(e.target.id != "contact-modal-content")
      closeModal(e);
  }
  else if(e.target.id == "modal-close") {
    closeModal(e);
  }
}
function keyHandler(e) {
  if(e.keyCode == 27)
    closeModal(e);
}
function closeModal(e) {
  contactModal.className = "contact-modal";
}

document.addEventListener('click', clickHandler, false);
document.addEventListener('click', keyHandler, false);
