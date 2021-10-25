let task  = document.querySelector('.task-sort');


var select = document.querySelector('select');

select.onchange = function() {
    var indexSelected = select.selectedIndex,
        option = select.querySelectorAll('option')[indexSelected];
        
    var selectedId = option.getAttribute('id');

/*
select.addEventListener('change', () => {
    alert(select.value);
*/
  if (selectedId == '1') {

    let task  = document.querySelector('.task-sort');
    for (let i = 0; i < task.children.length; i++) {
        for (let j = i; j < task.children.length; j++) {
            if (task.children[i].getAttribute('date-end') < task.children[j].getAttribute('date-end')) {
                replaceNode = task.replaceChild(task.children[j], task.children[i]);
                insertAfter(replaceNode, task.children[i]);
            }
        }
    }

  }

  if (select.value == '2') {

    let task  = document.querySelector('.task-sort');
    for (let i = 0; i < task.children.length; i++) {
        for (let j = i; j < task.children.length; j++) {
            if (task.children[i].getAttribute('date-end') > task.children[j].getAttribute('date-end')) {
                replaceNode = task.replaceChild(task.children[j], task.children[i]);
                insertAfter(replaceNode, task.children[i]);
            }
        }
    }

  }

if (select.value == '3') {

    let task  = document.querySelector('.task-sort');
    for (let i = 0; i < task.children.length; i++) {
        for (let j = i; j < task.children.length; j++) {
            if (task.children[i].getAttribute('date-start') < task.children[j].getAttribute('date-start')) {
                replaceNode = task.replaceChild(task.children[j], task.children[i]);
                insertAfter(replaceNode, task.children[i]);
            }
        }
    }

  }

  if (select.value == '4') {

    let task  = document.querySelector('.task-sort');
    for (let i = 0; i < task.children.length; i++) {
        for (let j = i; j < task.children.length; j++) {
            if (task.children[i].getAttribute('date-start') > task.children[j].getAttribute('date-start')) {
                replaceNode = task.replaceChild(task.children[j], task.children[i]);
                insertAfter(replaceNode, task.children[i]);
            }
        }
    }

  }

};


function insertAfter(elem,refElem) {
    return refElem.parentNode.insertBefore(elem,refElem.nextSibling);
}
