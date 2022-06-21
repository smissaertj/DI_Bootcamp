let allBoldItems = [];
let paragraph = document.getElementsByTagName('p')[0];
console.log(paragraph)

const getBoldItems = () => {
    for (let childNode of paragraph.children){
        allBoldItems.push(childNode.textContent)
    }
}


const highlight = () => {
    for (let childNode of paragraph.children){
        childNode.style.color = 'blue';
    }
}


const return_normal = () => {
    for (let childNode of paragraph.children){
        childNode.style.color = 'black';
    }
}


getBoldItems();
console.log(allBoldItems);

paragraph.addEventListener('mouseover', highlight);
paragraph.addEventListener('mouseout', return_normal);