let div = document.body.firstElementChild;
console.log(div);

div = document.body.getElementsByTagName('div');
console.log(div[0]);

let ul = div[0].nextElementSibling;
console.log(ul);

let ul2 = document.body.children[document.body.children.length - 2];
console.log(ul2);

let li = ul2.lastElementChild;
console.log(li)

li = ul2.children[ul2.children.length - 1]
console.log(li);
