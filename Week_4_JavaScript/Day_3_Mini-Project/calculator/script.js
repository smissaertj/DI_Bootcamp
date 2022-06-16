let display = document.getElementById('display');

let number = (num) => {
    display.value += num;
}

let operator = (operator) => {
    display.value += operator;
}

let equal = () => {
    display.value = eval(display.value);
}

let reset = () => {
    display.value = '';
}

let clearDisplay = () => {
    let text = display.value;
    text = text.replace(text.charAt(text.length - 1), '');
    display.value = text;
}
