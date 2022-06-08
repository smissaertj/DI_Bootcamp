let str = "Happy BirthDay";
let patt = /birthday/i;
let result = str.match(patt);
console.log(result); //returns true

if (result){
    console.log('Yes')
} else{
    console.log('No');
}


let regex = /^.+@.+\..+$/;
console.log(regex.test('johndoe@gmail.com')); //returns true