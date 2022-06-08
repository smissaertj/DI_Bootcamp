// Array - List of values

let students = ['joeri', 'laurent', 'Shivastav', 'Ally', 'Bruno', 'Angkush', 'Kadeer'];
console.log(students);
console.log(students[0]);
console.log(students[1]);
console.log(students[2]);
console.log(students[3]);
console.log(students[4]);
console.log(students[5]);
console.log(students[6]);

console.log(students.length);

students[1] = 'Yuri'
console.log(students[1]);

students[7] = 'Damien';
console.log(students);

students[students.length] = 'Test';
students[students.length] = 'Test2';
console.log(students);

students[12] = "Emilie";
console.log(students);
console.log(students[10]); // Undefined


// Nested Arrays
let student_array = [
    ['joeri', 35],
    ['laurent', 34, ['Olivier', 'Amelia']],
    ['Shivastav', 24],
    ['Ally', 24],
    ['Bruno', 50],
    ['Angkush', 19],
    ['Kadeer', 24]
];

console.log(student_array);
console.log(student_array[0][0]);
console.log(student_array[0][1]);
console.log(student_array[1][2][0]);

student_array.push(['Hello', 33]);
console.log(student_array)

// Array Methods
// Add an element at the last position
students.push("Ben");
console.log(students);

// Remove element at the last position
students.pop()
console.log(students);

/*
The splice() method changes the contents of an array by removing or replacing existing elements
and/or adding new elements in place.
 */
const months = ['Jan', 'March', 'April', 'June'];
months.splice(1, 0, 'Feb');
// inserts at index 1
console.log(months);
// expected output: Array ["Jan", "Feb", "March", "April", "June"]

months.splice(4, 1, 'May');
// replaces 1 element at index 4
console.log(months);
// expected output: Array ["Jan", "Feb", "March", "April", "May"]

months.splice(2); // Delete everything as from Index 2
console.log(months);


/*
The slice() method returns a shallow copy of a portion of an array into a new array object selected from start to end
(end not included) where start and end represent the index of items in that array.
The original array will not be modified.
 */
const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];

console.log(animals.slice(2));
// expected output: Array ["camel", "duck", "elephant"]

console.log(animals.slice(2, 4));
// expected output: Array ["camel", "duck"]

console.log(animals.slice(1, 5));
// expected output: Array ["bison", "camel", "duck", "elephant"]

console.log(animals.slice(-2));
// expected output: Array ["duck", "elephant"]

console.log(animals.slice(2, -1));
// expected output: Array ["camel", "duck"]

console.log(animals.slice());
// expected output: Array ["ant", "bison", "camel", "duck", "elephant"]

/*
The toString() method returns a string representing the object.
 */
let arr = ['a', 'b', 'c', 'd'];
console.log(arr);
console.log(arr.toString());

/*
The join() method creates and returns a new string by concatenating all the elements in an array
 (or an array-like object), separated by commas or a specified separator string.
 If the array has only one item, then that item will be returned without using the separator.
 */
console.log(arr.join(" "));
console.log(arr.join("-"));

/*
The split() method divides a String into an ordered list of substrings,
puts these substrings into an array, and returns the array.
split() is a String method!
 */
let str = "bruno";
console.log(str.split(""));

let str2 = "bruno beche";
console.log(str2.split(" "));

/*
The JavaScript delete operator removes a property from an object;
 */
console.log(arr);
delete arr[0];
console.log(arr); // There's an empty element at index 0

/*
The shift() method removes the first element from an array and returns that removed element.
This method changes the length of the array.
*/
let arr_2 = [1, 2, 3, 4, 5];
let firstElement = arr_2.shift()
console.log(firstElement);
console.log(arr_2);


/*
The unshift() method adds one or more elements to the beginning of an array and returns the new length of the array.
 */
console.log(arr_2.unshift(0)); // returns new array length
console.log(arr_2);