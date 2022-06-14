/*
Exercise 1 : Is_Blank
Instructions
Write a program to check whether a string is blank or not.

console.log(isBlank('')); --> true
console.log(isBlank('abc')); --> false
*/

const isBlank = (string) => {
    return string === ''
}

console.log(isBlank(''));
console.log(isBlank('asdf'));

/*
Exercise 2 : Abbrev_name
Instructions
Write a JavaScript function to convert a string into an abbreviated form.

console.log(abbrevName("Robin Singh")); --> "Robin S."
*/

const abbrevName = (fullName) => {
    let arr = fullName.split(' ');
    return `${arr[0]} ${arr[1][0]}.`;
}

console.log(abbrevName('Joeri Smissaert'));


/*
Exercise 3 : SwapCase
Instructions
Write a JavaScript function which takes a string as an argument and swaps the case of each character.
For example :

if you input 'The Quick Brown Fox'
the output should be 'tHE qUICK bROWN fOX'.
*/

const swapCase = (string) => {
    let arr = string.split(' ');
    let newString = '';

    for (let i of string){
        if (i !== i.toUpperCase()) {
            newString += i.toUpperCase();
        } else {
            newString += i.toLowerCase();
        }
    }

    return newString;

}

console.log(swapCase('The Quick Brown Fox'));


/*
Exercise 4 : Omnipresent Value

Create a function that determines whether an argument is omnipresent for a given array.
A value is omnipresent if it exists in every subarray inside the main array.

[[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// 3 exists in every element inside this array, so is omnipresent.

isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false
*/

let arr = [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];

const omniPresent = (arr, value) => {
    for (let i = 0; i < arr.length; i++) { // loop over the nested arrays
        if (!arr[i].includes(value)) { // check if value is NOT included in nested array i:
            return false              // We only need to know if it's NOT there, we can return False as soon as 1 nested
                                    // array doesn't have the value
        }
    }
    return true
}

console.log(omniPresent(arr, 3));