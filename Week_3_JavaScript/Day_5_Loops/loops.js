// Loops
let arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

// For loops
// for (start condition; expression; increment) {
//     // do something
// }

for (let i = 0; i < 10; i++){
    console.log(i);
}

for (let i = 0; i < arr.length; i++){
    console.log(arr[i]);
}

// For In Loop - Arrays & Objects
for (let i in arr) {
    console.log(i); // returns index
    console.log(arr[i]); //returns value
}

let myObject = {
    user: 'Joeri',
    email: 'foo@bar.com',
    phone: 5555858
}

for (let key in myObject) {
    console.log(key, myObject[key]);
}

// For Of -- only on iterables: arrays & strings
for (let val of arr) {
    console.log(val);
}

// Method loops
arr.forEach(i => console.log(i))
Object.keys(myObject) //- used for objects
Object.values(myObject) //- used for objects
Object.entries(myObject) //- used for objects

// While loop
/*
myCondition = true;
while (myCondition) {
 // do something
}
 */

let count = 0;
while (count < arr.length) {
    console.log(arr[count]);
    count++;
}

// Do while loop
// do
// {
//     statements..
// }
// while (condition);
let i = 0;
do {
  console.log("The number is " + i)
  i++;
}
while (i < 10)


// The break statement breaks the loop and continues executing the code after the loop
for (let i = 0; i < 10; i++) {
  if (i === 3) {
      break;
    }
  console.log("The number is " + i); // 0 1 2
}

// The continue statement breaks one iteration (in the loop), and continues with the next iteration.
for (let i = 0; i < 10; i++) {
  if (i === 3) {
      continue;
  }
  console.log("The number is " + i); // 0 1 2 4 5 6 7 8 9
}


/*
Exercise 1
1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen.
Sample Output: //"0 is even" //"1 is odd" //"2 is even"
 */

for (let i = 1; i < 16; i++) {
    if (i % 2 === 0){
        console.log(`${i} is even`)
    } else {
        console.log(`${i} is odd`)
    }
}


/*
Exercise 2
let names= ["john", "sarah", 23, "Rudolf",34]

1. Write a JavaScript for loop that will go through the variable names.
if the item is not a string, pass.
if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.
 */

let names= ["john", "sarah", 23, "Rudolf",34];

for (let val of names) {
    if (typeof(val) === "string") {
        if (val[0] !== val[0].toUpperCase()) {
          val = val.replace(val.charAt(0), val.charAt(0).toUpperCase());
        }
        console.log(val);
    }
}

/*
2. Write a JavaScript for loop that will go through the variable names

if the item is not a string, go out of the loop.
if the item is a string, display it.
*/

for (let val of names) {
    if (typeof(val) === "string") {
        console.log(val);
    } else {
        break;
    }
}


