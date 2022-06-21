let body = document.body;

const button_click = () => {
    console.log('clicked');
    let h1 = document.createElement('h1');
    h1.textContent = 'Button Clicked!';
    body.appendChild(h1);
}

// Add an event to a button
let btn2 = document.getElementById('btn-2');
// btn2.setAttribute('onclick', 'button_click()');
// btn2.onclick = button_click; // name of the function, NOT a function call e.g. button_click();

// Create profiles
const createProfiles = () => {
    console.log('Creating Profiles...');

    let py_pt_class = [
        {
            id: 1,
            user: 'Bruno',
            email: 'bruno@coolascode.com'
        },
        {
            id: 2,
            user: 'Joeri',
            email: 'joeri@coolascode.com'
        },
        {
            id: 3,
            user: 'Laurent',
            email: 'laurent@westtech.com'
        },
        {
            id: 4,
            user: 'Angkush',
            email: 'angkush@westtech.com'
        },
        {
            id: 5,
            user: 'Ally',
            email: 'ally@web.com'
        },
        {
            id: 6,
            user: 'Shivastav',
            email: 'shivastav@saweb.com'
        },
        {
            id: 7,
            user: 'Kadeer',
            email: 'kadeer@ghost.com'
        },
        {
            id: 8,
            user: 'Damien',
            email: 'damien@developers.institute'
        }
    ]

    let container = document.createElement('div');
    container.className = 'main';

    for (let person of py_pt_class){

        let div = document.createElement('div');
        div.classList.add('profiles');

        let img = document.createElement('img');
        img.setAttribute('src', `https://robohash.org/${person.id}?size=200x200`);
        div.appendChild(img);

        let h3 = document.createElement('h3');
        h3.textContent = person.user
        div.appendChild(h3);
        body.appendChild(div);

        let h4 = document.createElement('h4');
        h4.textContent = person.email
        div.appendChild(h4);
        container.appendChild(div);
    }

    body.appendChild(container);
}

let btnProfiles = document.getElementById('btn-3');
btnProfiles.onclick = createProfiles;

// Event Listener
btn2.addEventListener('click', (ev) => {
    console.log(ev);
    ev.stopPropagation(); // Stop Event Bubbling: The Event Is First Captured And Handled By The Innermost Element And Then Propagated To Outer Elements.
})

let div1 = document.getElementById('div1');
div1.addEventListener('click', (ev) => {
    console.log('div was clicked');
})


// Exercise 1
// const insertRow = () => {
//     let table = document.getElementById('sampleTable')
//     let row = table.insertRow(0);
//     let cell = row.insertCell(0);
//     let cellValue = document.createTextNode('Test')
//     cell.appendChild(cellValue);
// }

let rowCount = 2;
const insertRow = () => {
    rowCount++;

    let table = document.getElementById('sampleTable')
    let row = document.createElement('tr');

    let cell1 = document.createElement('td');
    cell1.textContent = `Row${rowCount} Cell1`;
    row.appendChild(cell1);

    let cell2 = document.createElement('td');
    cell2.textContent = `Row${rowCount} Cell2`;
    row.appendChild(cell2);

    table.appendChild(row);
}