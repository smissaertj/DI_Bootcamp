let div = document.querySelector('div');
div.style.backgroundColor = 'lightblue';
div.style.padding = '10px';

let ul = document.querySelector('ul');
let john = ul.firstElementChild;
john.style.visibility = 'hidden';

let pete = ul.lastElementChild;
pete.style.border = '1px solid black';

let body = document.body;
body.style.fontSize = '1.5em';

if (div.style.backgroundColor == 'lightblue') {
  alert(`Hi ${john.textContent} & ${pete.textContent}`);
}