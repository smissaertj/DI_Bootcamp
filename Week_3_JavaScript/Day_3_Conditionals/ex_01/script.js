/*
Make a keyless car!

This car will only let you drive if you are over 18. Make it do the following:

Using prompt() and alert(), ask a user for their age.

IF they say they are below 18, respond with: "Sorry, you are too young to drive this car. Powering off
IF they say they are 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!
IF they say they are over 18, respond with: "Powering On. Enjoy the ride!"
 */

let age = prompt('What is your age?');
let age_limit = 18;

if (isNaN(age)) {
    alert('Please provide a valid number.');
} else if (age < age_limit) {
    alert('Sorry, you are too young to drive this car. Powering off.')
} else if (age > age_limit) {
    alert('Powering On. Enjoy the ride!')
} else {
    alert('Congratulations on your first year of driving. Enjoy the ride!')
}