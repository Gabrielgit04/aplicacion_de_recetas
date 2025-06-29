
// variables
const formValidate = document.getElementsByClassName(".dialog");
formValidate.addEventListener('submit', function(evento){
    evento.preventDefault();
})

const nombre_receta = formValidate.elements['nombre'].value;

const instrucciones = formValidate.elements['instrucciones'].value;

const ingredientes = formValidate.elements['ingredientes'].value;

const porcion = document.getElementById('porcion');

porcion.addEventListener('input', (event) =>{
    const textValue = event.currentTarget.value;

    if (!isNaN(textInvalid(textValue))){
        return formValidate.innerHtml = "Este campo debe contener valores numericos.";
    }

});

function textInvalid(text){
    return /["0-9"]/.test(text);
}

// funciones
function validarFormulario() {
    if (nombre_receta.value.trim() === "" || ingredientes.value.trim() === "" || instrucciones.value.trim() === "") {
        return formValidate.innerHtml('El campo es obligatorio, por favor, rellenalo.');
    }

    if(!formValidate.checkValidity()){
        alert("Formulario invalido.")
    }

}

alert(nombre_receta)