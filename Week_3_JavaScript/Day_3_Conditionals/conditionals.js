let a = 1;

// If statement
console.log('Before If statement');
if (a > 0) {
    // if expression is true
    console.log('a is greater than zero.');
}
console.log('After If statement');


// If and Else statement
console.log('Before If Else statement');
if (a > 0) {
    // if expression is true
    console.log('a is greater than zero.');
} else {
    // if expression is false
    console.log('a is not greater than zero.')
}
console.log('After If Else statement');


// If .. Else If .. Else statement
console.log('Before If .. Else If .. Else statement');
if (a > 0) {
    // if expression is true
    console.log('a is greater than zero.');
} else if (a < 0) {
    console.log('a is smaller than zero');
} else if (a === 0) {
    console.log('a is equal to zero');
} else {
    // if expression is false
    if (isNaN(a)){
        console.log(`${a} is not a number.`)
    }
}
console.log('After If .. Else If .. Else statement');


// Switch case - Uses Strict Comparison (===)

let c = 0;

switch (c) {
    case 0:
        console.log(0);
        // break; // leaving out break causes "Fallthrough in switch statement": the next case is executed.
    case 1:
        console.log(1);
        break;
    case 2:
        console.log(2);
        break;
    default:
        console.log('c is none of the above.');
}