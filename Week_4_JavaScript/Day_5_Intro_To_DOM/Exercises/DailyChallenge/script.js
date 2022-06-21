let planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune'
]

let section = document.getElementsByClassName('listPlanets')[0];
console.log(section)

for (let planet of planets){
    let div = document.createElement('div');
    div.className = 'planet';

    let randomColor = Math.floor(Math.random()*16777215).toString(16);
    div.style.backgroundColor = '#' + randomColor;
    section.appendChild(div);
}