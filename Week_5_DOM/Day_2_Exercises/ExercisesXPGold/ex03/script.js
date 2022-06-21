let shoppingList = [];

let form = document.createElement('form');
let inputField = document.createElement('input');
inputField.setAttribute('type', 'text');

let addItemBtn = document.createElement('button');
addItemBtn.setAttribute('type', 'button');
addItemBtn.textContent = 'Add Item';

let clearAllBtn = document.createElement('button');
clearAllBtn.setAttribute('type', 'button');
clearAllBtn.textContent = 'Clear All';

form.appendChild(inputField);
form.appendChild(addItemBtn);
form.appendChild(clearAllBtn);

let div = document.getElementById('root');
div.appendChild(form);

const addItem = () => {
  shoppingList.push(inputField.value);
  console.log(shoppingList);
};

const clearAll = () => {
  shoppingList = [];
  console.log(shoppingList);
};

addItemBtn.addEventListener('click', addItem);
clearAllBtn.addEventListener('click', clearAll);

