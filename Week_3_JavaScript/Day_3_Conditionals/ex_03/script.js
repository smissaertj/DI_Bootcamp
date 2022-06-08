/*
Write as comments the steps of the resolution of this piece of code
Guess what will be the result before checking it
 */

let a = 2 + 2; // a is assigned the value 4

switch (a) {
  case 4: // a is equal to 4, the code is executed and the break statement ends the switch.
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}