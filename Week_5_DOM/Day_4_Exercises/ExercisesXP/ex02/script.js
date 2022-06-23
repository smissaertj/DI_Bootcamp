
let outer = document.getElementById('container');
let inner = document.getElementById('animate');

let outer_width = outer.getBoundingClientRect().width;
let inner_width = inner.getBoundingClientRect().width;

let position = 0;
function myMove(){
  let interval = setInterval(function(){
    inner.style.left = position + 'px';
    // inner.style.top = inner.style.left;
    position++;

    if (position > (outer_width - inner_width)){
      clearInterval(interval);
    }
  }, 1)
};