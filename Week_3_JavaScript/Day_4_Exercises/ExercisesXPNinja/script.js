/*
Exercise 1 : Age Difference
Instruction
Given the years two people were born, find the date when the younger one is exactly half the age of the older.
Notes: The dates are given in the format YYYY
 */

let year1 = Number(prompt('Provide year 1:'));
let year2 = Number(prompt('Provide year 2'));
let result = 0;

if (year1 > year2){
    result = ((year1 - year2) * 2) + year2;
} else {
    ageDifference = year2 - year1;
  	result = ((year2 - year1) * 2) + year1;
}

alert(`The year that the younger one is exactly half of the older is ${result}.`)



/*
Exercise 2 : Zip Codes
Instruction
Harder exercise
Hint : This exercise has 2 parts. First, do this exercise without Regular Expressions, then do it using Regular Expressions

While working in a Post Office you must have the clients’ zip code in order to send them their letters.
Ask the client for their zip code and console.log “success” or “error” based on the following rules.
Zip codes consists of 5 numbers
Must only contain numbers
Must not contain any whitespace (spaces)
Must not be greater than 5 digits in length
 */

let zipCode = prompt('Please provide a Zip Code:');

// No RegEx
let numbers = '123456789';
for (let i = 0; i < zipCode.length; i++){
    if (!zipCode[i].match(numbers)) {

    }
}

// RegEx
let regexPattern = /^\d+$/g;

if (zipCode.match(regexPattern) && zipCode.length <= 5) {
    console.log('success');
} else {
    console.log('error');
}


/*
Exercise 3 : Secret Word
Instruction
Harder exercise
Hint : Use Regular Expressions

Prompt the user for a word and save it to a variable.
Delete all the vowels of the word and console.log the result.
Bonus: Replace the vowels with another character and console.log the result
 */
let word = 'aeiou';
let regexPattern = /[aeiou]/g;
let newWord = word.replaceAll(regexPattern, '*');
console.log(newWord);