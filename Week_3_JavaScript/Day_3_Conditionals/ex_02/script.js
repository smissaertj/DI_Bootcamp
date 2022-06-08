/*
Write as comments the steps of the resolution of this piece of code
Guess what will be the result before checking it
 */

let a = 2 + 2; // a is assigned the value 4

switch (a) {
  case 3: // a is not equal to 4
    alert( 'Too small' );
    break;
  case 4: // a is equal to 4, code is executed. The break statement ends the switch.
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}