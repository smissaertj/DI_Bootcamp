let allBooks = [
  {
    title: 'A Brief History of Time',
    author: 'Stephen Hawking',
    image: 'https://images-na.ssl-images-amazon.com/images/I/81pQPZAFWbL.jpg',
    alreadyRead: true,
  },
  {
    title: 'The Three-Body Problem',
    author: 'Cixin Liu',
    image: 'https://images-na.ssl-images-amazon.com/images/I/919XM42JQlL.jpg',
    alreadyRead: true,
  },
];

let div = document.getElementsByTagName('div')[0];
let table = document.createElement('table');

for (let i = 0; i < allBooks.length; i++){
  let row = table.insertRow(i);

  for (let j = 0; j < Object.keys(allBooks[i]).length; j++){
    let newCell = row.insertCell(j);
    let cellValue = Object.values(allBooks[i])[j];
    console.log(cellValue);
    let newText = '';

    console.log(Object.keys(allBooks[i])[j]);
    if (Object.keys(allBooks[i])[j] === 'image'){
      newCell.innerHTML = `<img alt=\"book cover\" width=\"100px\" src=\"${cellValue}\"/>`;
    } else {
      newText = document.createTextNode(cellValue);
      newCell.appendChild(newText);
    }
    if (cellValue === true){
      row.style.color = 'red';
    }
  }
}

div.appendChild(table);