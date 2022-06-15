let display = document.getElementById('display');

let number = (num) => {
    display.textContent += num;
}

let operator = (operator) => {
    display.textContent += operator;
}

let equal = () => {
    display.textContent = eval(display.textContent);
}

let reset = () => {
    display.textContent = '';
}

let clearDisplay = () => {
    let text = display.textContent;
    text = text.replace(text.charAt(text.length -1), '');
    display.textContent = text;
}
