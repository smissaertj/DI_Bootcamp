let timeout;
function set_timeout() {
    console.log('Setting timeout...');

    timeout = setTimeout(function(){
        // code to be executed after timeout.
        alert('Today is a bit cold!');
    }, 5000) // timeout in milliseconds
}


function clear_timeout() {
    console.log('Clearing timeout');
    clearTimeout(timeout)
}


let interval;
function set_interval() {
    console.log('Setting interval');
    interval = setInterval(function(){
        // run repeatedly at specific interval
        console.log('Please do not forget to send me your project proposal.')
    }, 5000);

    // clear the interval
    setTimeout(function(){
        console.log('Clear interval');
        clearInterval(interval)
    }, 15000);
}


function clear_interval() {
    console.log('Clearing interval');
    clearInterval(interval);
}


// Move the box
function move() {
    let outer = document.getElementById('outer');
    let inner = document.getElementById('inner');

    let outer_width = outer.getBoundingClientRect().width;
    let inner_width = inner.getBoundingClientRect().width;

    let position = 0;
    let interval = setInterval(function(){
        console.log(position);
        if (position > (outer_width - inner_width)){
            clearInterval(interval);
        } else {
            inner.style.left = position + 'px';
            inner.style.top = position + 'px';
        }

        position++;
    }, 10);
}