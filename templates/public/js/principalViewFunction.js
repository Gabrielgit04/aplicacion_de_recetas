
        // menu de filtrado
        const botones = document.querySelectorAll('.escoger');

        botones.forEach(boton => {boton.addEventListener('click', () => {
            botones.forEach(b => b.classList.remove('activa'));
            boton.classList.add('activa');
        });
        });
        // hasta aca

// dialogshow
function showDialog() {
    
    const verifydialog = document.querySelector('.dialog_add');
    const adddialog = document.querySelector('.agregar');

    adddialog.addEventListener('click', (event) => {
        event.preventDefault(); // Evita que el formulario se envíe
        verifydialog.showModal(); // Muestra el diálogo

    });
    
}

function hideDialog(){
    const dialog = document.querySelector('.dialog_add');
    const closeButton = dialog.querySelector('.cerrar');

    closeButton.addEventListener('click', (event) => {
        event.preventDefault(); // Evita que el formulario se envíe
        dialog.close(); // Cierra el diálogo
});


}