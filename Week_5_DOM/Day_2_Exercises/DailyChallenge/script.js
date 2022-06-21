let formElements = document.getElementById('libform').elements;
let btn = document.getElementById('lib-button');


for(let element of formElements){
    if (element.type === 'text'){
        element.required = true;
    }
}


btn.addEventListener('submit', (e) =>{
    e.preventDefault();
    let words = [];
    let formElements = document.getElementById('libform').elements;

    for (let element of formElements){
        words.push(element.value);
    }

    let libs = `Be kind to your ${words[0]} 
                Be kind to your ${words[1]} in ${words[4]}
                Where the weather is always ${words[3]}.
                You may think that this is the ${words[2]},
                Well it is.`

    let spanStory = document.getElementById('story');
    spanStory.textContent = libs;
})
