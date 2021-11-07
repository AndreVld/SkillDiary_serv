
// Получить модальный
var modalf = document.getElementById("modal-finish-t");

// Получить кнопку, которая открывает модальный
var btnf = document.getElementById("btn-finish-t");

// Получить элемент <span>, который закрывает модальный
var closebtnf = document.getElementById("close-finish-t");

// Когда пользователь нажимает на кнопку, откройте модальный
btnf.onclick = function() {
  modalf.style.display = "flex";
}

// Когда пользователь нажимает на <span> (x), закройте модальное окно
closebtnf.onclick = function() {
  modalf.style.display = "none";
}

// Когда пользователь щелкает в любом месте за пределами модального, закройте его
window.onclick = function(event) {
  if (event.target == modalf) {
    modalf.style.display = "none";
  }
}