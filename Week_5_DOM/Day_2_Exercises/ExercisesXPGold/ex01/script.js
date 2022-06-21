let selectField = document.getElementById('genres');
console.log(selectField.value);

let selectOptions = selectField.children;
for (let option of selectOptions){
  option.selected = option.value === 'classic';
}
