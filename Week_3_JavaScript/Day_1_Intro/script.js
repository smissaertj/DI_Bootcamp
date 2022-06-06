console.log("This is from the JavaScript file.");

// declare a variable
let a = 5;
let b = 3;

let first_name = "Joeri"; // snake_case
let firstName = "Joeri"; // camelCase

/*
    Comment block
 */

console.log(a);
console.log(b);
console.log(a + b);
console.log(a - b);

let sum = a + b;
console.log(sum);

// update the value of the variable
a = 2;
console.log(a);
console.log(b);

console.log(sum);

sum = a + b;
console.log(sum);

b = 4;
sum = a + b;
console.log(sum);


// Primitive Datatypes
// string - " " or '' or ` `
// number - digits 0-9
// boolean - True or False (1 or 0)
// undefined - when a variable is declared but not assigned to anything.
// null - special value not belonging to any of the above.


// String
let str = "Today is a great day!"
console.log(str);

let str1 = "Hello";
let str2 = " World ";
console.log(str1 + " " + str2); // Concatenation
console.log(`${str1} ${str2}`) // Template literals/strings

let str3 = "1";
let str4 = "3";
let str5 = "five"

console.log(str3 + str4); // Concatenation
console.log(str3 + 4); // Concatenation
console.log(str3 - str4); // Strings are converted to number and an arithmetic operation is done.

console.log(str3 + str5);
console.log(str3 - str5); // NaN - Not a Number: str5 cannot be converted to a number.

let str6 = 'A quick brown fox';
let array_str6 = str6.split(' ');
console.log(array_str6);

// Convert String to Number
console.log(`${str3} - ${typeof(str3)}`);
str3 = Number(str3);
console.log(`${str3} - ${typeof(str3)}`);

str4 = Number(str4);
console.log(`${str3 + str4} - ${typeof(str3 + str4)}`);


// String Methods - actions that can be performed on objects.
console.log(str1.length);
console.log(str1.indexOf('o')); // index position of character 'o' - counts from 0
console.log(str1.indexOf('l')); // returns first match
console.log(str1.indexOf('w')); // -1: Char is not present in the string / no match
console.log(str1.charAt(1)); // Get character at index 1

console.log(str1.substring(1, 3)); // from index 1 to (but not including) index 3
console.log(str1.substring(1)); // from index 1 until end of string

console.log(str1.substring(str1.indexOf('e'))); // Get the index of letter 'e' and use that index inside substring method.

console.log(str1.toLowerCase());
console.log(str1.toUpperCase());
console.log(str1.replace('o', 'a'));
console.log(str1.replace('l', 't'));
console.log(str1.replaceAll('l', 't'));
console.log(str1.concat(str2));
console.log(str2.trim());
console.log(str2.trimStart());
console.log(str2.trimEnd());


// Number
let num1 = 4; // positive
let num2 = -3; // negative
let num3 = 3.14159265359 // float (decimal)
console.log(num3.toFixed(3)) // ==> STRING

console.log(isNaN(num3)); // is num3 not a number?
console.log(isNaN('number'));

let num4 = 10000000000;
console.log(num4.toLocaleString());


console.log(num1.toString()); // convert number to String


// Boolean
let status = true;
console.log(status);
console.log(Number(status));

let expression = Boolean(10 > 9);
console.log(expression);

// Comparisons
/*
= assign
== compare value only
=== compare value and data type

! - NOT
|| - OR: One of the expressions need to evaluate to True
&& - AND: All expressions need to evaluate to True
 */

let var1 = 5;
let var2 = "5";

console.log(Boolean(var1 == var2)); // True
console.log(Boolean(var1 === var2)); // False
console.log(Boolean(var1 != var2)); // False
console.log(Boolean(var1 !== var2)); // True
console.log(Boolean((var1 > 10) || (var1 === var2))); // False
console.log(Boolean((var1 < 10) || (var1 === var2))); // True
console.log(Boolean((var1 > 0) &&  (var1 === var2))); // False

// Undefined
let z;
console.log(z);

// null
let y = null;
console.log(y);


// User interface functions
alert("Hello");

let age = prompt("How old are you?", 20);
alert(`You are ${age} years old.`)

let isBoss = confirm("Are you the boss?");
alert(isBoss);
