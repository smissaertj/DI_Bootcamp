// declare object
/*
let x = {
  property: value,
  property: value,
  method: function(){}
};
*/

// Declare empty object :
let objName = {};

let students = {
  student_1: 'Joeri',
  student_2: 'Ally',
  student_3: 'Shivastav',
  student_4: 'Kadeer',
  student_5: 'Laurent',
  student_6: 'Angkush',
  student_7: 'Bruno'
}

console.log(students);

// Access value of a key/property inside an object
console.log(students.student_1); // can not be a variable
console.log(students['student_7']); // can contain a variable if the key is unknown

let a = 'student_2';
console.log(students[a]);

let database = {
  student_1: {
    name: 'Joeri',
    surname: 'Smissaert',
    age: 35
  },
  student_2: {
    name: 'Ally',
    surname: 'Baubooa',
    age: 24
  },
  student_3: {
    name: 'Shivastav',
    surname: 'Juggoo',
    age: 24
  },
  student_4: {
    name: 'Laurent',
    surname: 'Hannelas',
    age: 34
  },
  student_5: {
    name: 'Bruno',
    surname: 'Beche',
    age: 50
  }
}

console.log(database.student_2.age);

// adding or changing properties
database.student_2.age = 20;
console.log(database.student_2.age);

database.student_2.laptop = 'Asus Vivobook';
console.log(database.student_2);

// deleting properties
delete database.student_2.laptop;
console.log(database.student_2);

// functions as a method
database.student_1.hello = console.log('Hi there!');
database.student_1.hello; // returns Hi there! to the console.


// Exercise 1

let myObject = {
  username: 'myUsername',
  password: 'myPassword'
}

let myArray = [myObject];

let newsfeed = [{
  object1: {
    username: '',
    timeline: ''
  },
  object2: {
    username: '',
    timeline: ''
  },
  object3: {
    username: '',
    timeline: ''
  }
}]
