/*
Function declaration
 */
function HelloWorld(){
  console.log("Hello World");
}

HelloWorld(); // function call

/*
Function Expression
*/

// Anonymous function
const Hello = function (){
  console.log("Hello");
}

Hello();

// Arrow Function
// const functionName = (parameters) => // function body
/*
const HelloWorld =  () =>
  console.log("Hello World");

HelloWorld();
 */

const HiThere = (name) => console.log(`Hi ${name}`)

HiThere('Joeri');


/*
default parameter values
 */

const Hi = (name = 'Joe') => console.log(`Hi ${name}`)
Hi('Jane');
Hi();

/*
Exercise 1
1. Create a structured html file linked to a js file
2. Write a JS function that takes a parameter: myAge
3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)
4. Call the function
*/

const ParentsAge = (myAge) => {
  ageMum = myAge * 2;
  ageDad = ageMum * 1.2;
  console.log(`My mum is ${ageMum} years old and my dad ${ageDad} years old.`)
}

ParentsAge(35);


/*
Every function in JavaScript returns undefined unless otherwise specified.
When a function returns a value, it’s returning a result.
The return value is “returned” back to the “caller” of the function.

The return statement stops function execution immediately.
It’s possible to use return without a value. That causes the function to exit immediately.
 */

const myNameAge = (name, age) => {
  if (name === 'Joeri') {
    let result = `My name is ${name} and I'm ${age} years old.`
    return result
  } else {
    return 'You\'re not the right person'
  }
}
console.log(myNameAge('Joeri', 35));
console.log(myNameAge('Jane', 35));


/*
Exercise 2
1. Create a structured html file linked to a js file
2. Write a JS function that takes a parameter: myAge
3. Return the age of my mum (my mum is twice my age)
4. Call the function
5. Console.log the age of my mum
 */

const mumsAge = (myAge) => myAge * 2
console.log(mumsAge(35));


/*
Object Methods
Methods are actions stored in properties as function definitions.

The 'this' keyword refers to the object, while this.property is the property of the object
 */
let person= {
    firstName : "Sarah",
    eyeColor: "blue",
    eat : function () {
        console.log(`My name is ${this.firstName} and I love chocolate`)
    }
}
person.eat(); // access the object method
