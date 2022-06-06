/*
Exercise 1: Your Favorite Food
 */
let favoriteFood = 'pizza';
let favoriteMeal = 'dinner';
console.log(`I eat ${favoriteFood} at every ${favoriteMeal}`);

/*
Exercise 2 : Series
 */
// Part 1
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesSentence = `${myWatchedSeries[0]}, ${myWatchedSeries[1]}, and ${myWatchedSeries[2]}`;
console.log(`I watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}.`);

// Part 2
myWatchedSeries.splice(myWatchedSeries.indexOf('the big bang theory'), 1, 'Friends');
myWatchedSeries.push('Ozark');
myWatchedSeries.unshift('test');
myWatchedSeries.splice(myWatchedSeries.indexOf('black mirror'), 1);
console.log(myWatchedSeries[myWatchedSeries.indexOf('money heist')][2])
console.log(myWatchedSeries);


/*
Exercise 3 : The Temperature Converter
 */

let tempCelsius = 25;
let tempFahrenheit = (tempCelsius * 9/5) + 32;
console.log(`${tempCelsius}C is ${tempFahrenheit}F`);


/*
Exercise 4 : Guess The Answers #1
 */

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55 = 34 + 21
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: 23 = 2 + 21
// Actual: 23


/*
Exercise 5 : Guess The Answers #2
 */
typeof(15)
// Prediction: number
// Actual: number

typeof(5.5)
// Prediction: number
// Actual: number

typeof(NaN)
// Prediction: number
// Actual: number

typeof("hello")
// Prediction: string
// Actual: string

typeof(true)
// Prediction: boolean
// Actual: boolean

typeof(1 != 2)
// Prediction: boolean
// Actual: boolean

"hamburger" + "s"
// Prediction: hamburgers
// Actual: hamburgers

"hamburgers" - "s"
// Prediction: NaN
// Actual: NaN

"1" + "3"
// Prediction: 13
// Actual: 13

"1" - "3"
// Prediction: -2
// Actual: -2

"johnny" + 5
// Prediction: johnny5
// Actual: johnny5

"johnny" - 5
// Prediction: NaN
// Actual: NaN

99 * "hello"
// Prediction: NaN
// Actual: NaN

1 != 1
// Prediction: false
// Actual: false

1 == "1"
// Prediction: true
// Actual: true

1 === "1"
// Prediction: false
// Actual: false


/*
Exercise 6 : Guess The Answers #3
 */
5 + "34"
// Prediction: 534
// Actual: 534

5 - "4"
// Prediction: 1
// Actual: 1

10 % 5
// Prediction: 0
// Actual: 0

5 % 10
// Prediction: 0
// Actual: 5

"Java" + "Script"
// Prediction: JavaScript
// Actual: JavaScript

" " + " "
// Prediction: "  "
// Actual: "  "

" " + 0
// Prediction: " 0"
// Actual: " 0"

true + true
// Prediction: true
// Actual: 2

true + false
// Prediction: true
// Actual: 1

false + true
// Prediction: true
// Actual: 1

false - true
// Prediction: false
// Actual: -1

!true
// Prediction: false
// Actual: false

3 - 4
// Prediction: -1
// Actual: -1

"Bob" - "bill"
// Prediction: NaN
// Actual: NaN
