// access the form
let loginForm = document.forms.login;
console.log(loginForm);

console.log(loginForm.childNodes);
console.log(loginForm.children);
console.log(loginForm.elements.username);
console.log(loginForm.elements['username']);
console.log(loginForm.elements.password);

// change the name attribute in the form
loginForm.elements.username.setAttribute('name', 'joeri')

let userName = loginForm.elements.username;
userName.value = 'TEST';

// Stop page from refreshing on submit (when button type = submit)
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
})

const getData = () => {
   let userNameValue = userName.value;
   let passwordValue = loginForm.elements.password.value;
   console.log(userNameValue, passwordValue);
}

// Event lister for input
userName.addEventListener('input', (e) => {
    console.log(userName.value);
})