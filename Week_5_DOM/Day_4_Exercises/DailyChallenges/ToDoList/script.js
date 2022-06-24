let listTasks = [];
let listTasksDiv = document.querySelectorAll('.listTasks')[0];
let addTaskBtn = document.getElementById('addTaskBtn');
listTasksDiv.innerHTML = `<ul class="list-group rounded"></ul>`


const addTask = () => {
  let addTaskInput = document.getElementById('addTaskInput');
  if (addTaskInput.value !== '') {
    let task = {
      id: listTasks.length,
      description: addTaskInput.value,
      done: false,
    }
    listTasks.push(task);
    addTaskInput.value = '';

    let newTask = document.createElement('li');
    newTask.setAttribute('id', task.id);
    newTask.className = 'list-group-item text-start';
    newTask.innerHTML = `<button type="button" class="btn-close" aria-label="Close" id="btn-${task.id}"
                          onclick="deleteTask(${task.id})"></button>
                         <label class="form-check-label" for="${task.id}" id="label-${task.id}">
                         <input class="form-check-input mx-2" type="checkbox" value="${task.id}" 
                         id="checkbox-${task.id}" onclick="doneTask(${task.id})">
                         ${task.description}
                         </label>`
    listTasksDiv.appendChild(newTask);
  }
}


const doneTask = (id) => {
  let taskLabel = document.getElementById('label-'+id);
  taskLabel.classList.toggle('text-decoration-line-through')
}


const deleteTask = (id) => {
  let task = document.getElementById(id);
  task.remove();
  listTasks.splice(id,1);
}

addTaskBtn.addEventListener('click', addTask);

