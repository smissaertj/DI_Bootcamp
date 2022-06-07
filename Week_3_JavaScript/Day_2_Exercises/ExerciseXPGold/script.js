/*
Exercise 1 : Favorite Color
let sentence = ["my","favorite","color","is","blue"];
Write some simple Javascript code that will join all the items in the array above, and console.log the result.
 */
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(''))

/*
Exercise 2 : Mixup
1. Create 2 variables. The values should be strings. For example:
2. Slice out and swap the first 2 characters of the two strings from part 1.
3. Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).
4. Finally, console.log the new concatenated string.
 */

let str1 = "mix";
let str2 = "pod";
let slice1 = str1.slice(0,2);
let slice2 = str2.slice(0,2);
let str3 = `${str1.replace('mi', slice2)} ${str2.replace('po', slice1)}`
console.log(str3);

/*
Exercise 3 : Calculator
Make a Calculator. Follow the instructions:

Prompt the user for the first number.
Store the first number in a variable called num1.
Hint : console.log the type of the variable num1. What should you do to convert it to a number ?
Prompt the user for the second number.
Store the second number in a variable called num2.
Create an Alert where the value is the SUM of num1 and num2.
 */

let num1 = Number(prompt('Please provide the first number: '));
let num2 = Number(prompt('Please provide the second number: '));
alert(`Sum of first number and second number is: ${num1 + num2}`);

