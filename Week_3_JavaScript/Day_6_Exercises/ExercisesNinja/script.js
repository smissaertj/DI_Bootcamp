/*
Exercise 1 : Checking The BMI
Hint:
- You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

Create two objects, each object should hold a person’s details. Here are the details:
FullName
Mass
Height

Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person

Outside the objects, create a JS function that compares the BMI of both objects.

Display the name of the person who has the largest BMI.
 */

let personOne = {
  fullName: 'John Doe',
  mass: 65, // kilograms
  height: 1.8, // meters
  bmi: function() {
    return this.mass / (this.height ** 2);
  }
};

let personTwo = {
  fullName: 'Jane Doe',
  mass: 48, // kilograms
  height: 1.5, // meters
  bmi: function() {
    return this.mass / (this.height ** 2);
  }
};

const compareBMI = (a, b) => {
  if (a.bmi() > b.bmi()){
    return a.fullName;
  } else {
    return b.fullName;
  }
}

console.log(`The person with the largest BMI is ${compareBMI(personOne, personTwo)}.`);


/*
Exercise 2 : Grade Average
- This Exercise is trickier then the others. You have to think about its structure before you start coding.
- You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.

Create a function called findAvg(gradesList) that takes an argument called gradesList.

Your function must calculate and console.log the average.

If the average is above 65 let the user know they passed

If the average is below 65 let the user know they failed and must repeat the course.
Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
Hint One function must call the other.
*/

let grades = [40, 50, 70, 80, 90, 35, 65, 75, 85];

const passFail = (averageGrade) => {
  if (averageGrade > 65){
    return 'Pass';
  } else {
    return 'Fail';
  }
}

const findAvg = (gradeList) => {
  sum = 0
  averageGrade = sum / gradeList.length;
  for (grade of gradeList) {
    sum += grade;
  }
  return passFail(averageGrade);
}

console.log(findAvg(grades));