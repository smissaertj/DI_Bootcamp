let container = document.getElementById('container');
console.log(container);

let unorderedLists = document.getElementsByTagName('ul');
let firstList = unorderedLists[0];
firstList.lastElementChild.innerText = 'Richard';
firstList.firstElementChild.innerText = 'Joeri';

let secondList = unorderedLists[1];
secondList.firstElementChild.innerText = 'Joeri';

let secondListChildren = secondList.children;
secondList.removeChild(secondListChildren[1]);

unorderedLists[0].classList.add('student_lists', 'university', 'attendance');
unorderedLists[1].classList.add('student_lists');