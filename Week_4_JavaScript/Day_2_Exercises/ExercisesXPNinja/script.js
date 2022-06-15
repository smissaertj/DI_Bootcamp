/*
Exercise 1: Random Number
Instructions
Get a random number between 1 and 100.
Console.log all even numbers from 0 to the random number.
 */

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random

const logEvenNumbers = (min, max) => {
    min = Math.floor(min + 1);
    max = Math.ceil(max - 1);
    let randomNumber =  Math.floor(Math.random() * (max - min));

    let evenNumbers = [];
    for (let i = min; i < randomNumber; i++){
        if (i % 2 === 0){
            evenNumbers.push(i);
        }
    }

    console.log(`Even Numbers between ${min} and ${randomNumber}:\n${evenNumbers}`);
}

logEvenNumbers(1, 100);


/*
Exercise 2: Capitalized Letters
Instructions
Create a function that takes a string as an argument.
Have the function return:
The string but all letters in even indexes should be capitalized.
The string but all letters in odd indexes should be capitalized.
Note:

Index 0 will be considered even.
The argument of the function should be a lowercase string with no spaces.
For example,

capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']
 */

const capitalizeIndexes = (string) => {
    let stringIndexes = string.length - 1;
    let evenIndexes = [];
    let oddIndexes = [];
    let result = [];

    // Capitalize evenIndexes
    let tmp = '';
    for (let i = 0; i < stringIndexes; i++){
        if (i % 2 === 0){
            tmp += string.charAt(i).toUpperCase();
        } else {
            tmp += string.charAt(i);
        }
    }
    result.push(tmp);

    // Capitalize oddIndexes
    tmp = '';
    for (let i = 0; i < stringIndexes; i++) {
        if (i % 2 !== 0){
            tmp += string.charAt(i).toUpperCase();
        } else {
            tmp += string.charAt(i);
        }
    }
    result.push(tmp);

    return result;
}

console.log(capitalizeIndexes('abcdef'));

/*
Exercise 3 : Is Palindrome?
Instructions
Write a JavaScript function that checks whether a string is a palindrome or not.
Note A palindrome is a word, phrase or sequence that is spelled the same both backwards and forward, e.g., madam, bob or kayak.
*/

const isPalindrome = (string) => {
    let arr = string.split('');
    let arrReversed = [];

    // Reverse the array, iterate from end to beginning
    for (let i = arr.length - 1; i >= 0; i--) {
        arrReversed.push(arr[i]);
    }

    return arr.join('') === arrReversed.join('');
}

console.log(isPalindrome('joeri'));
console.log(isPalindrome('madam'));
console.log(isPalindrome('bob'));
console.log(isPalindrome('kayak'));
console.log(isPalindrome('damien'));

/*
Exercise 4 : Biggest Number
Instructions
Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
Note : This function should work with any array;

const array = [-1,0,3,100, 99, 2, 99] ;// should return 100
const array2 = ['a', 3, 4, 2]; // should return 4
const array3 = []; // should return 0
*/

const biggestNumberInArray = (array) => {
    array = array.sort(function(a, b){ return a - b});
    return array[array.length - 1];
}

console.log(biggestNumberInArray([-1,0,3,100, 99, 2, 99]));


/*
Exercise 5: Unique Elements
Instructions
Write a JS function that takes an array and returns a new array with only unique elements.
*/

const uniqueElements = (array) => {
    let uniqueElements = new Set(array);
    return Array.from(uniqueElements);
}

console.log(uniqueElements([1,2,3,3,3,3,4,5]));