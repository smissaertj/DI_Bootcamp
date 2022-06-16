let bottles = 99;
let counter = 0;

for (let i = bottles; i > 0; i--) {
    if (bottles === 1){
        console.log(`${bottles} bottle of beer\n`);
    } else {
        console.log(`${bottles} bottles of beer\n`);
    }

    counter++;
    bottles--;

    if (counter === 1){
        console.log(`We take ${counter} down, pass it around\n${bottles} bottles of beer on the wall\n`);
    } else {
        console.log(`We take ${counter} down, pass them around\n${bottles} bottles of beer on the wall\n`);
    }
}