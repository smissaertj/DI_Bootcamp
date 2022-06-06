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
