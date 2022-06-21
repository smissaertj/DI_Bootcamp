let h1 = document.getElementsByTagName('h1')[0];
console.log(h1);

let article = document.body.firstElementChild;
let articleLastElement = article.lastElementChild;
article.removeChild(articleLastElement);


let h2 = document.getElementsByTagName('h2')[0];
h2.addEventListener('click', () =>{
    h2.style.backgroundColor = 'red';
});


let h3 = document.getElementsByTagName('h3')[0];
h3.addEventListener('click', () => {
    h3.style.display = 'none';
});


let button = document.getElementById('button');
button.addEventListener('click', () =>{
    let paragraphs = document.getElementsByTagName('p');
    for (let p of paragraphs){
        p.style.fontWeight = 'bold';
    }
});


h1.addEventListener('mouseover', () => {
   let fontSize = Math.random() * 100;
   h1.style.fontSize = `${fontSize}px`;
});


let secondParagraph = document.getElementsByTagName('p')[1];
secondParagraph.addEventListener('mouseover', () =>{
    secondParagraph.classList.add('fadeOut');
})
console.log(h2);

