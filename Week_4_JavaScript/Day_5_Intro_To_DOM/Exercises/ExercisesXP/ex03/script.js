let navbar = document.getElementById('navBar');
navbar.setAttribute('id', 'socialNetworkNavigation');

let newLi = document.createElement('li');
newLi.innerText = 'Logout';

let ul = document.querySelector('ul');
ul.appendChild(newLi);

console.log(ul.firstElementChild.childNodes[0]);
console.log(ul.lastElementChild.childNodes[0]);
