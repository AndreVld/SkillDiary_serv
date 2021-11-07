///////////////////////////

// Получить модальный
var modalReturn = document.getElementById("modal-return");

// Получить кнопку, которая открывает модальный
var btnReturn = document.getElementById("btn-return");

// Получить элемент <span>, который закрывает модальный
var closebtnReturn = document.getElementById("close-return");

// Когда пользователь нажимает на кнопку, откройте модальный
btnReturn.onclick = function() {
  modalReturn.style.display = "flex";
}

// Когда пользователь нажимает на <span> (x), закройте модальное окно
closebtnReturn.onclick = function() {
  modalReturn.style.display = "none";
}

// Когда пользователь щелкает в любом месте за пределами модального, закройте его
window.onclick = function(event) {
  if (event.target == modalReturn) {
    modalReturn.style.display = "none";
  }
}
