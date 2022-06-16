const play = () => {

    let word = promptWord();
    let wordArr = Array.from('*'.repeat(word.length)); // Create an array equal to word.length containing * elements
    let guessCount = 0;

    while (guessCount < 10) {
        guessCount++;
        let letter = promptLetter();

        for (let i = 0; i < word.length; i++){

            // Check if the letter is present in the word
            if (word.charAt(i) === letter){
                console.log('Correct!');
                wordArr[i] = letter; // If present, add the letter to index i of wordArr, replacing the *
                console.log(wordArr.join('')); // show the user the partial word.
            }
        }

        // Break out of the loop when the correct word was found.
        if (wordArr.join('') === word) {
            console.log(`You win!\nThe correct word is: ${word}`);
            break;
        }
    }

    // end the game on 10 attempts
    if (guessCount >= 10) {
        console.log(`You Lose!\nThe correct word was ${word}`)
    }
}

const promptWord = () => {
    let word = null;
    do
        word = prompt('Enter a word of minimum 8 letters: ');
    while
        (word.length < 8);

    return word;
}


const promptLetter = () => {
    let letter = null;
    do
        letter = prompt('Guess a letter in the word: ');
    while
    (letter === null || letter === '' || !isNaN(letter));

    return letter;
}


play();