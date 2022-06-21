/*
Volume of a sphere = 4/3 πr3

Check with the radius of the given sphere. If the diameter of the sphere is known, then divide it by 2, to get the radius
Find the cube of the radius r3
Now multiply it with (4/3)π
The final answer will be the volume of sphere

*/
let btn = document.forms.MyForm.submit;
const PI = Math.PI;

const calculateVolume = (radius) => {
    let volume = (radius ** 3) * (4/3 * PI);
    let volumeField = document.getElementById('volume');
    volumeField.value = volume;
}

btn.addEventListener('click', (e) =>{
    e.preventDefault();
    let radiusField = document.getElementById('radius');
    let radiusValue = radiusField.value;
    calculateVolume(Number(radiusValue));
})
