/*
Exercise 1 : Divisible By Three
Loop through the array below and determine whether each number is divisible by three.
Each time you loop console.log true or false.
*/
let numbers = [123, 8409, 100053, 333333333, 7]

for (let number of numbers){
  if (number % 3 === 0){
    console.log(true);
  } else {
    console.log(false);
  }
}

/*
Exercise 2 : Attendance
Given the object below where the name is the student’s name and the value is the country they are from.

Prompt the student for their name.
If the name is in the object, console.log the name of the student and the country they come from.
For example: "Hi! I'm [name], and I'm from [country]."
Hint: You don’t need to use a for loop, just look up the statement if ... in
If the name is not in the object, console.log: "Hi! I'm a guest."
 */

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let name = prompt('Enter you\'re name: ');
if (name in guestList){
  console.log(`Hi! I'm ${name}, and I'm from ${guestList[name]}`);
} else {
  console.log('Hi! I\'m a guest.');
}

/*
Exercise 3 : Playing With Numbers
Requirements : Don’t use built-in Javascript methods to answer the following questions.
You have to create the logic by yourself. Use simple for loops.

1. Console.log the sum of all the numbers in the age array.
2. Console.log the highest age in the array.
*/
let age = [20,5,12,43,98,55];

let sum = 0;
let maxAge = age.sort()[age.length - 1];
for (let el of age) {
  sum += el;
}
console.log(`Sum: ${sum}`);
console.log(`maxAge: ${maxAge}`);