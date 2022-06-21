let form = document.forms[0];
console.log(form);

console.log(form.elements.fname);
console.log(form.elements.lname);
console.log(form.elements.submit);


let userAnswers = document.getElementsByClassName('usersAnswer')[0];

for(let element of form.elements){
    if (element.type === 'text'){
        element.required = true;
    }
}

form.addEventListener('submit', (e) =>{
    e.preventDefault();

    for (let element of form.elements){
        if (element.type === 'text'){
            let li = document.createElement('li');
            li.textContent = element.value;
            userAnswers.appendChild(li);
        }
    }
})
