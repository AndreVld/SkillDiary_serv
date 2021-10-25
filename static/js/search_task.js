
function searchFunction() {
  
    var input, filter, txtValue;
    input = document.getElementById('searchInput');
    filter = input.value.toUpperCase();
    div = document.getElementsByClassName("task-title");
    task = document.getElementsByClassName("task");
  
    for (i = 0; i < div.length; i++) {
        var txtValue = div[i].innerText;
        console.log( txtValue);
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          div[i].style.display = "";
          task[i].style.display = "";
        } else {
          div[i].style.display = "none";
          task[i].style.display = "none";

        }
      }
  }

