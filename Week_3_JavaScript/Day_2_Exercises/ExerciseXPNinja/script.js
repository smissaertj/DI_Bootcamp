/*
Exercise 1 : Evaluation
For each expression, predict what you think the output will be in a comment (//) without first running the command.
 */
5 >= 1 // true
0 === 1 // false
4 <= 1 // false
1 != 1 // false
"A" > "B" // false
"B" < "C" // true
"a" > "A" // true
"b" < "A" // false
true === false // false
true != true // false

/*
Exercise 2 : Ask For Numbers
Ask the user for a string of numbers separated by commas
Console.log the sum of the numbers.
 */
let numbers = prompt('Provide 2 numbers separated by a comma: ');
let sum = Number(numbers.slice(0,1)) + Number(numbers.slice(2,4));
console.log(sum);
// console.log(numbers_array);


/*
Exercise 3 : Find Nemo
Hint: if statement (tomorrow’s lesson)

Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo"
Find the word “Nemo”
Console.log a string as follows: "I found Nemo at [the position of the word Nemo]".
If you can’t find Nemo, console.log “I can’t find Nemo”.
 */

let sentence = prompt("Provide a sentence with the word 'Nemo': ");
let sentence_array = sentence.split(" ");
let indexNemo = sentence_array.indexOf("Nemo");
if (indexNemo > 0) {
  console.log(`'Nemo' is word number ${indexNemo + 1} in your sentence.`);
} else {
    console.log(`I can't find "Nemo".`)
};

/*
Exercise 4 : Boom
Hint: if statement (tomorrow’s lesson)

Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:

If the number given is less than 2 : return “boom”
If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
If the number given is evenly divisible by 2, add a exclamation mark to the end.
If the number given is evenly divisible by 5, return the string in ALL CAPS.
If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
 */

let number = Number(prompt('Provide a number: '));
let string = 'boom';

if (number < 2) {
    console.log(string);
} else if (number > 2) {
    string = string.replace('oo', 'o'.repeat(number));

    if ((number % 2 === 0) && (number % 5 === 0)) {
        string += '!';
        console.log(string.toUpperCase());

    } else if (number % 2 === 0) {
        string += '!';
        console.log(string);

    } else if (number % 5 === 0) {
        console.log(string.toUpperCase());
    }
}