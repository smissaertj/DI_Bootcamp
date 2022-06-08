//Empty object :
let objName = {};

/*
let x = {
  property: value,
  property: value,
  method: function(){}
};
*/

let person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};

console.log(person.firstname);
console.log(person["lastName"]);

person.firstName = "Sarah"
person.eyeColor= "blue"
console.log(person)

let person = {
  firstName: "John",
  lastName: "Doe",
};
delete person.firstName
console.log(person)