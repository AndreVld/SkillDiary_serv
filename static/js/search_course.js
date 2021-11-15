function searchCourse() {
    var input = document.getElementById('searchIn');
    var filter = input.value.toUpperCase();
    var div = document.getElementsByClassName("course-title");
    var course = document.getElementsByClassName("course-wrap");
  
    for (i = 0; i < div.length; i++) {
        var txtValue = div[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          course[i].style.display = "";
        } 
        else {
          course[i].style.display = "none";
        }
    }
}


function sortCourse() {
    var select = document.querySelector('.select-sort');

    if (select.value == '1') {
        let course  = document.querySelector('.course-sort');
        for (let i = 0; i < course.children.length; i++) {
            for (let j = i; j < course.children.length; j++) {
                let date_i = new Date(course.children[i].getAttribute('date-end'))
                let date_j = new Date(course.children[j].getAttribute('date-end'))
                if (date_i < date_j) {
                    replaceNode = course.replaceChild(course.children[j], course.children[i]);
                    insertAfter(replaceNode, course.children[i]);
                }
            }
        }
    }
    if (select.value == '2') {
        let course  = document.querySelector('.course-sort');
        for (let i = 0; i < course.children.length; i++) {
            for (let j = i; j < course.children.length; j++) {
                let date_i = new Date(course.children[i].getAttribute('date-end'))
                let date_j = new Date(course.children[j].getAttribute('date-end'))
                if (date_i > date_j) {
                    replaceNode = course.replaceChild(course.children[j], course.children[i]);
                    insertAfter(replaceNode, course.children[i]);
                }
            }
        }
    }
    if (select.value == '3') {
        let course  = document.querySelector('.course-sort');
        for (let i = 0; i < course.children.length; i++) {
            for (let j = i; j < course.children.length; j++) {
                let date_i = new Date(course.children[i].getAttribute('date-start'))
                let date_j = new Date(course.children[j].getAttribute('date-start'))
                if (date_i < date_j) {
                    replaceNode = course.replaceChild(course.children[j], course.children[i]);
                    insertAfter(replaceNode, course.children[i]);
                }
            }
        }
    }
    if (select.value == '4') {
        let course  = document.querySelector('.course-sort');
        for (let i = 0; i < course.children.length; i++) {
            for (let j = i; j < course.children.length; j++) {
                let date_i = new Date(course.children[i].getAttribute('date-start'))
                let date_j = new Date(course.children[j].getAttribute('date-start'))
                if (date_i > date_j) {
                    replaceNode = course.replaceChild(course.children[j], course.children[i]);
                    insertAfter(replaceNode, course.children[i]);
                }
            }
        }
    }
}


function insertAfter(elem,refElem) {
    return refElem.parentNode.insertBefore(elem,refElem.nextSibling);
}
