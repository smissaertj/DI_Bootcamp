let h1 = document.getElementsByTagName('h1')[0];

h1.addEventListener('click', () =>{
    h1.style.fontSize = '50px';
});


h1.addEventListener('mouseover', () =>{
    h1.style.color = 'red';
});


h1.addEventListener('mouseout', () =>{
    h1.style.textAlign = 'center';
});


h1.addEventListener('dblclick', () =>{
      h1.style.border = '2px solid black';
});