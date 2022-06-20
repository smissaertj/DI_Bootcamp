console.log("Intro to DOM")

/*
element.getElementById()
element.getElementsByClassName()
element.getElementsByTagName()
element.querySelector()
 */

let body = document.body;
console.log(body);

let title = document.getElementById('title');
console.log(title);

title.style.color = 'red';
title.style.backgroundColor = 'blue';
title.innerText = 'Welcome to DOM!';


console.log(body.firstChild); // returns first child node
console.log(body.firstElementChild.textContent); // returns first HTML element
console.log(body.childNodes); // retrieve all nodes
console.log(body.children); // retrieve all html elements
console.log(body.children[0]); // retrieve 1st html element
console.log(body.childNodes[1]);

console.log(body.children[1].firstElementChild);

let div1p1 = document.getElementById('div1-p1');
console.log(div1p1);

let divs = document.getElementsByTagName('div');
for (let div of divs){
    console.log(div);
}

let reds = document.getElementsByClassName('red');
console.log(reds)
for (let red of reds){
    console.log(red);
}

let h1 = document.querySelector('h1');
console.log(h1);

let div_query = document.querySelectorAll('div p');
console.log(div_query);
for (let div of div_query){
    console.log(div);
}


// getElementById('id')
document.getElementById('demo');

// getElementsByClassName('class')
document.getElementsByClassName('demo');

// getElementsByTagName('tag')
document.getElementsByTagName('p');

// querySelector('css selector')
document.querySelector('#demo-query');

// querySelectorAll('css selector')
let demoQueryAll = document.querySelectorAll('.demo-query-all');

demoQueryAll.forEach(query => {
  query.style.border = '1px solid green';
});

/*
CreateElement()
CreateTextNode()
AppendChild()
RemoveChild()
innerText
InnerHTML
*/
let elem_h2 = document.createElement('h2');
elem_h2.textContent = 'It is very cold at night lately';
div1p1.appendChild(elem_h2);
    // body.appendChild(elem_h2);

// see dom.css
for (let i = 0; i < 5; i++) {
    let new_div = document.createElement('div');
    new_div.setAttribute('class', 'yellow_box');
    body.appendChild(new_div);
}


let elem_txt = document.querySelector('#div2');
elem_txt.innerText = '<h3>Inner HTML</h3>';
elem_txt.innerHTML = '<h3>Inner HTML</h3>';

let parentElem = document.getElementById("main");
let childElem = document.getElementById("hint");
// parentElem.removeChild(childElem);



/*
Matches()
The elem.matches(css) does not look for anything; it only checks if an
element matches the given CSS-selector. It returns true or false.
 */
for (let elem of document.body.children) {
    if (elem.matches('a[href$="zip"]')) {
      // check if it ends with "zip"
      alert("The archive reference: " + elem.href );
    }
}

/*
Closest()
Ancestors of an element are the parent, grandparent, great grandparent, and so on.
The ancestors together form the chain of parents from the component to the top.

<h1>Contents</h1>

<div class="contents">
  <ul class="book">
    <li class="chapter">Chapter 1</li>
    <li class="chapter">Chapter 1</li>
  </ul>
</div>

<script>
  let chapter = document.querySelector('.chapter'); // LI

  alert(chapter.closest('.book')); // UL
  alert(chapter.closest('.contents')); // DIV

  alert(chapter.closest('h1')); // null (because h1 is not an ancestor)
</script>
*/

// Attributes
console.log(elem_txt.hasAttributes('id'));
console.log(elem_txt.getAttribute('id'));
elem_txt.setAttribute('id', 'div2-2');
elem_txt.removeAttribute('id');
console.log(elem_txt.getAttribute('id'));

elem_txt.setAttribute('class', 'class_1');

// Class
elem_txt.className = 'class_2';
elem_txt.classList.add('class_3');
elem_txt.classList.remove('class_2');
elem_txt.classList.replace('class_3', 'class_1');
console.log(elem_txt.classList.contains('class_1'));


/*
classList.toggle
Toggles between adding and removing the class
The first parameter removes the specified class from an element,
and returns false. If the class does not exist, it is added to the element,
and the return value is true.

The optional second parameter is a Boolean value that forces the class
 to be added or removed, regardless of whether it already exists or not.
 */
elem_txt.classList.toggle('class_1');