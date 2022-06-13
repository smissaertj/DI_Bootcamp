/*
Instructions
Write a JavaScript program that recreates the pattern below.
Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).
Do this Daily Challenge by yourself, without looking at the answers on the internet.

*
* *
* * *
* * * *
* * * * *
* * * * * *
*/

let rows = Number(prompt('Rows: '));

for (let i = 0; i < rows; i++){
  console.log('*'.repeat(i + 1));
}

let row = '';
for (let i = 0; i <= rows; i++){ // for each row in rows create a new line
  for (let j = 0; j < i; j++){ // on each new line, create J number of stars where J equals the i (row number)
    row += '*';
  }
  row += '\n';
}
console.log(row);





