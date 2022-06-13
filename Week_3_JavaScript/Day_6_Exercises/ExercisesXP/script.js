/*
Exercise 1 : List Of People

Part I - Review About Arrays
Write code to remove “Greg” from the people array.
Write code to replace “James” to “Jason”.
Write code to add your name to the end of the people array.
Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
Write code to make a copy of the people array using the slice method.
The copy should NOT include “Mary” or your name.
Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
Hint: Check out the documentation for the slice method
Write code that gives the index of “Foo”. Why does it return -1 ?
Create a variable called last which value is the last element of the array.
Hint: What is the relationship between the index of the last element in the array and the length of the array?
*/
let people = ["Greg", "Mary", "Devon", "James"];

people.shift();
people[2] = 'Jason';
people.push('Joeri');
console.log(people.indexOf('Mary'));
new_arr = people.slice(1, 3);
console.log(people.indexOf('Foo')) // returns -1 because Foo is not an array element.
let last = people[people.length - 1];

console.log(people);
console.log(new_arr);
console.log(last);
/*
Part II - Loops

Using a loop, iterate through the people array and console.log each person.

Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
Hint: take a look at the break statement in the lesson.
*/

for (let name of people) {
    if (people.indexOf(name) === people.indexOf('Jason') + 1) {
        break;
    }
    console.log(name);
}

/*
Exercise 2 : Your Favorite Colors
Create an array called colors where the value is a list of your five favorite colors.
Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
Hint : create an array of suffixes to do the Bonus
*/

let colors = ['blue', 'black', 'red', 'yellow', 'green'];
let suffix = ['st', 'nd', 'rd', 'th', 'th'];

for (let color of colors) {
    console.log(`My #${colors.indexOf(color) + 1}${suffix[colors.indexOf(color)]} is ${color}`)
}


/*
Exercise 3 : Repeat The Question
Prompt the user for a number.
Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

While the number is smaller than 10 continue asking the user for a new number.
Tip : Which while loop is more relevant for this situation?
*/

let number = 0;
do
    number = Number(prompt('Provide a number: '))
while (number < 10);

/*
Exercise 4 : Building Management

Console.log the number of floors in the building.
Console.log how many apartments are on the floors 1 and 3.
Console.log the name of the second tenant and the number of rooms he has in his apartment.
Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.
 */

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);
console.log(`${building.nameOfTenants[1]}: ${building.numberOfRoomsAndRent.dan[0]}`)

if ( building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log(building.numberOfRoomsAndRent.dan[1]);


/*
Exercise 5 : Family
Create an object called family with a few key value pairs.
Using a for in loop, console.log the keys of the object.
Using a for in loop, console.log the values of the object.
 */

let family = {
    parents: 2,
    children: 4
}

for (let key in family){
    console.log(key);
}

for (let key in family){
    console.log(family[key]);
}


/*
Exercise 6
Given the object below and using a for loop, console.log “my name is Rudolf the raindeer”
 */
let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

let sentence = '';
for (let item in details) {
    sentence += item + ' ' + details[item] + ' ';
}

console.log(sentence);


/*
Exercise 7 : Secret Group
A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
Hint: a string is an array of letters
Console.log the name of their secret society. The output should be “ABJKPS”
 */

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let result = '';

for (let name of names.sort()) {
    result += name[0];
}

console.log(result);
