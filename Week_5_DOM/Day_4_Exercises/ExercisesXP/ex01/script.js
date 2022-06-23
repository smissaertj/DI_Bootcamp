setTimeout(function(){
  alert('Hello World');
}, 2000);


let container = document.getElementById('container');
setTimeout(function(){
  let p = document.createElement('p');
  p.textContent = 'Hello World';
  container.appendChild(p);
}, 2000);

let interval = setInterval(function(){
  let p = document.createElement('p');
  p.textContent = 'Hello World';
  container.appendChild(p);
}, 2000)

let btnClearInterval  = document.getElementById('clear');
btnClearInterval.addEventListener('click', () =>{
  clearInterval(interval);
})

