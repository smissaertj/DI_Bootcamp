/*
Using the .toString() method convert the array to a string.
Using the .join()method convert the array to a string. Try passing different values into the join.
Eg .join(“+”), .join(” “), .join(“”)
Bonus : To do this Bonus look up how to work with nested for loops
Sort the numbers array in descending order, do so using for loops (Not using built-in sort methods).
The output should be: [9,8,7,6,5,4,3,2,1,0]
Hint: The algorithm is called “Bubble Sort”
Use a temporary variable to swap values in the array.
Use 2 “nested” for loops (Nested means one inside the other).
Add comments and console.log the result for each step, this will help you understand.
Requirement: Don’t copy and paste solutions from Google
*/

const numbers = [5,0,9,1,7,4,2,6,3,8];

let str1 = numbers.toString();
let str2 = numbers.join("");
console.log(str1);
console.log(str2);

for (let i = 0; i < numbers.length; i++) { // iterate over each array element
  for(let j = 0; j < (numbers.length - i - 1); j++) { // for each element that is 1 index smaller that the current element

    if(numbers[j] < numbers[j+1]) { // if the element at the current position is smaller than the next element:
      let tmp = numbers[j]; // store the current element in a temp variable
      numbers[j] = numbers[j+1]; // assign the current element the value of the next one
      numbers[j+1] = tmp; // assign the next element the value of the current one.
    }

  }
}

console.log(numbers)

