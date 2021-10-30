// Получить модальный
var modal = document.getElementById("myModal");

// Получить кнопку, которая открывает модальный
var btn = document.getElementById("myBtn");

// Получить элемент <span>, который закрывает модальный
var closebtn = document.getElementById("close");

// Когда пользователь нажимает на кнопку, откройте модальный
btn.onclick = function() {
  modal.style.display = "flex";
}

// Когда пользователь нажимает на <span> (x), закройте модальное окно
closebtn.onclick = function() {
  modal.style.display = "none";
}

// Когда пользователь щелкает в любом месте за пределами модального, закройте его
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


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

