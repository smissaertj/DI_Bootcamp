const compareNumbers = (userNumber, computerNumber) => {
    if (userNumber === computerNumber) {
        alert('WINNER');
        return true;
    } else if (userNumber > computerNumber){
        alert('Your number is bigger than the computer\'s number, guess again.')
    } else if (userNumber < computerNumber){
        alert('Your number is smaller then the computer\'s, guess again.')
    }

    return false;

}

const playTheGame = () => {
    let play = confirm('Do you want to play?');
    // console.log(play);

    if (!play) {
        alert('No problem. Goodbye.')
    } else {
        let userNumber = 0;
        let computerNumber = 0;
        let guessCount = 0;

        while (guessCount < 3){
            guessCount++;
            userNumber = prompt('Enter a number between 0 and 10:');

            if (isNaN(userNumber)){
                alert('Sorry, that\'s not a number. Goodbye.')
            } else if (userNumber < 1 || userNumber > 9) {
                alert('Sorry that\'s not a good number. Goodbye.')
            } else {
                let max = 9;
                let min = 0;
                computerNumber = Math.ceil(Math.random() * (max - min) + min);
            }

            // console.log(userNumber);
            // console.log(computerNumber);
            let isWinner = compareNumbers(Number(userNumber), computerNumber); // prompt() returns a string!
            if (isWinner) {
                break; // break out of the loop if the user wins the session.
            }
        }

        if (guessCount === 3) {
            alert('Out of chances.')
        }
    }
}