
// variables
const formValidate = document.getElementsByClassName(".dialog");
formValidate.addEventListener('submit', function(evento){
    evento.preventDefault();
})

const nombre_receta = formValidate.elements['nombre'].value;

const instrucciones = formValidate.elements['instrucciones'].value;

const ingredientes = formValidate.elements['ingredientes'].value;

console.log(`Nombre de receta: ${nombre_receta}\nIngredientes:${ingredientes}\nIntrucciones:${instrucciones}`)
// funciones
function validarFormulario() {
    if (nombre_receta.value.trim() === "" || ingredientes.value.trim() === "" || instrucciones.value.trim() === "") {
        alert('El campo es obligatorio, por favor, rellenalo.');
        return false;
    }

    if(!formValidate.checkValidity()){
        alert("Formulario invalido.")
    }

}

alert(nombre_receta)