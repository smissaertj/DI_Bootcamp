/*
Exercise 1 : Information
Part I : function with no parameters

Create a function called infoAboutMe() that takes no parameter.
The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
Call the function.
 */

const infoAboutMe = () => console.log('My name is Joeri')
infoAboutMe();

/*
Part II : function with three parameters

Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
Call the function twice with the following arguments:
infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")
*/

const infoAboutPerson = (personName, personAge, personFavoriteColor) => {
    console.log(`You're name is ${personName}, you are ${personAge} years old, you're favourite color is ${personFavoriteColor}`);
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

/*
Exercise 2 : Tips
John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

Create a function named calculateTip() that takes no parameter.

Inside the function, ask John for the amount of the bill.

Here are the rules
If the bill is less than $50, tip 20%.
If the bill is between $50 and $200, tip 15%.
If the bill is more than $200, tip 10%.

Console.log the tip amount and the final bill (bill + tip).

Call the calculateTip() function.
*/

const calculateTip = () => {
    let billTotal = Number(prompt('Total bill amount: '));
    let tipPercentage = 0;
    let tipAmount = 0;
    let finalBill = 0;

    if (billTotal < 50) {
        tipPercentage = 20;
    } else if (billTotal >= 50 && billTotal < 200) {
        tipPercentage = 15;
    } else {
        tipPercentage = 10;
    }

    tipAmount = billTotal * (tipPercentage / 100);
    finalBill = billTotal + tipAmount;
    console.log(`Tip amount: ${tipAmount}\nFinal Bill: ${finalBill}`);
}

calculateTip()


/*
Exercise 3 : Find The Numbers Divisible By 23

Create a function call isDivisible() that takes no parameter.
In the function, loop through numbers 0 to 500.
Console.log all the numbers divisible by 23.
At the end, console.log the sum of all numbers that are divisible by 23.
Bonus: Add a parameter divisor to the function.
 */

const isDivisible = (divisor) => {
    let outcome = [];
    let sum = 0;
    for (let i = 0; i < 501; i++){
        if (i % divisor === 0){
            outcome.push(i);
            sum += i;
        }
    }
    console.log(`Outcome: ${outcome.join(' ')}\nSum: ${sum}`);1
}

isDivisible(23);


/*
Exercise 4 : Shopping List
Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have
1 banana, 1 orange and 1 apple in your cart.

Create a function called myBill() that takes no parameters.

The function should return the total price of your shoppingList. In order to do this you must follow these rules:
The item must be in stock. (Hint : check out if .. in)
If the item is in stock find out the price in the prices object.

Call the myBill() function.

Bonus: If the item is in stock, decrease the item’s stock by 1
*/

let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppingList = ['banana', 'orange', 'apple'];

const myBill = () => {
    let billAmount = 0;
    for (let item of shoppingList){
        if (item in stock && stock[item] > 0) {
            billAmount += prices[item];
            stock[item] -= 1;
        }
    }
   return billAmount;
}

console.log(myBill());
console.log(stock);


/*
Exercise 5 : What’s In My Wallet ?

Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
an item price
and an array representing the amount of change in your pocket.

In the function, determine whether you can afford the item.
If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false


Change will always be represented in the following order: quarters, dimes, nickels, pennies.
A quarters is 0.25
A dimes is 0.10
A nickel is 0.05
A penny is 0.01

After you created the function, invoke it like this:
changeEnough(4.25, [25, 20, 5, 0])

The value 4.25 represents the item’s price
The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you
6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

Examples
changeEnough(14.11, [2,100,0,0]) => returns false
changeEnough(0.75, [0,0,20,5]) => returns true
*/

const changeEnough = (itemPrice, amountOfChange) => {
    let totalQuarters = amountOfChange[0] * 0.25;
    let totalDimes = amountOfChange[1] * 0.10;
    let totalNickels = amountOfChange[2] * 0.05;
    let totalPennies = amountOfChange[3] * 0.01;

    let totalChange = totalQuarters + totalDimes + totalNickels + totalPennies;

    return totalChange > itemPrice;
}

console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));


/*
Exercise 6 : Vacations Costs

Define a function called hotelCost().
It should ask the user for the number of nights they would like to stay in the hotel.
If the user doesn't answer or if the answer is not a number, ask again.
The hotel costs $140 per night. The function should return the total price of the hotel.

Define a function called planeRideCost().
It should ask the user for their destination.
If the user doesn't answer or if the answer is not a string, ask again.
The function should return a different price depending on the location.
“London”: 183$
“Paris” : 220$
All other destination : 300$

Define a function called rentalCarCost().
It should ask the user for the number of days they would like to rent the car.
If the user doesn't answer or if the answer is not a number, ask again.
Calculate the cost to rent the car. The car costs $40 every day.
If the user rents a car for more than 10 days, they get a 5% discount.
The function should return the total price of the car rental.

Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the
3 functions that you created above.
Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function
totalVacationCost().

Call the function totalVacationCost()

Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost()
function. You need to change the 3 first functions, accordingly.
*/

const hotelCost = () => {
    let nights = 0;
    while (nights === 0 || nights === '' || isNaN(nights)) {
        nights = Number(prompt('Number of nights in hotel: '));
    }

    return 140 * nights;
}


const planeRideCost = () => {
    let destination = '';
    let priceList = {
        london: 183,
        paris: 220
    }
    let price = 0;

    while (destination === '' || typeof destination !== 'string') {
        destination = prompt('Destination: ');
    }

    if (destination.toLowerCase() in priceList) {
        price = priceList[destination];
    } else {
        price = 300;
    }

    return price;
}


const rentalCarCost = () => {
    let days = 0;
    let pricePerDay = 40;
    let discount = 5;
    let totalPrice = 0;

    while (days === 0 || days === '' || isNaN(days)) {
        days = Number(prompt('Number of days to rent a car: '));
    }

    if (days > 10) {
        totalPrice = (pricePerDay * days) - (pricePerDay * days * (discount / 100));
    } else {
        totalPrice = pricePerDay * days;
    }

    return totalPrice;
}


const totalVacationCost = () => {
    return `The car cost: ${rentalCarCost()}\nThe hotel cost: ${hotelCost()}\nThe plane tickets cost: ${planeRideCost()}`
}

console.log(totalVacationCost());