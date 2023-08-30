// static/formulario_app/script.js
document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".action-button");

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            alert("Botão clicado!");
        });
    });
});
