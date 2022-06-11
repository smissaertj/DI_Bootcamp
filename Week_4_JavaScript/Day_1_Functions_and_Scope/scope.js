/*
A variable has global scope if it is declared outside a function, block… scope. It can be accessed from anywhere in your program.
*/
var a = 10;
let b = 100;

function globalScope(){
  console.log(a);
  console.log(b);
}

globalScope();
//console.log(c); /* ReferenceError: c is not defined */

/*
var, let and const have function scope:
They can't be accessed from outside the function
*/

function functionScope() {
  var x = 3;
  let y = 2;
  const z = 1;
}

functionScope();
//console.log(x); /* ReferenceError: y is not defined */
//console.log(y); /* ReferenceError: y is not defined */
//console.log(z); /* ReferenceError: z is not defined */

/*
only let and const have block scope:
They can't be accssed from outside the block they are declared in, in contrast to var
*/

function blockScope() {
  if (true) {
    let fruit1 = 'apple'; // let: block scope
    const fruit2 = 'pear'; // const: block scope
    var fruit3 = 'orange'; // var: function scope
  }
  // console.log(fruit1);
  // console.log(fruit2);
  console.log(fruit3); // referencing a function scope variable inside a block
}

blockScope();



/*
var vs let vs const
- All can be used to declare global scoped variabled
- var: Function scoped, can be redeclared
- let: Block scoped, cannot be redeclared in the same scope
- const: Block scoped, cannot be reassigned
*/

// Function Scope
function func() {
  // x is known here but not defined.
  console.log('value of x here: ', x)
  {
    var x = 10;
    x = x + 5;
  }
  // x is still known here and has a value.
  console.log('value of x after for block: ', x)
}
// x is NOT known here.
func()


function func() {
  // x is NOT known here. Try uncommenting the line below.
  // console.log('value of x here: ', x)
  {
    let x = 10;
    x = x + 5;
  }
  // x is NOT known here. Try uncommenting the line below.
  // console.log('value of x after for block: ', x)
}
// x is NOT known here.
func()


// Block Scope
var i = 10;
if (true) {
  var i = 100;
  console.log(i);
}
console.log(i); // var was redeclared ans now has 100 as the value

let j = 100;
if (true) {
  let j = 1000; // j is redeclared in a different scope
  //let j = 10000;  /* j cannot be redeclared in the same scope */
  console.log(j); // j has the block scope value
}
console.log(j); // j has the globale scope value

const k = 1000;
if (true) {
  const k = 10000;
  //k = 1; /*  TypeError: Assignment to constant variable. */
  console.log(k);
}
//k = 1; /*  TypeError: Assignment to constant variable. */
