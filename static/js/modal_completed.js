/////////////////////////////////////////////

var modalFinish = document.getElementById("modal-finish");
var btnFinish = document.getElementById("btn-finish");
var closebtnFinish = document.getElementById("close-finish");

btnFinish.onclick = function() {
  modalFinish.style.display = "flex";
}

closebtnFinish.onclick = function() {
  modalFinish.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modalFinish) {
    modalFinish.style.display = "none";
  }
}