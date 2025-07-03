// vista principal

const nombre_receta = document.getElementById('nombre').value.trim();

const descripcion = document.getElementById('descripcion').value.trim();

const instrucciones =  document.getElementById('instrucciones').value.trim();

const ingredientes = document.getElementById('ingredientes').value.trim();

const porcion = document.getElementById('porcion').value.trim();
let mensaje = document.getElementById('message');



const formValidate = document.getElementById("dialog");
formValidate.addEventListener('submit', function(evento){
    evento.preventDefault();
    

let warning = validarForm()

mensaje.textContent = warning
mensaje.style.color = 'red'

});

function validarForm(){
    if(nombre_receta === '' || descripcion ==='' || instrucciones === '' || ingredientes === '' || porcion ===""){
        return 'El campo no debe quedar vacio.'
    }

    if(isNaN(porcion)){
        return "Las porciones deben ser expresadas en numeros"
    }

    

}
// hasta aca

// login validaciones

const userName = document.getElementById('user');
const contrasena = document.getElementById('password');

const formLogin = document.getElementById('formLogin');

const message = document.getElementById('validatep');

formLogin.addEventListener('submit', function(evento){
    evento.preventDefault();

let error = validateLogin()

message.textContent = error
message.style.color = "red"
})

function validateLogin(){
    if(userName.value.length < 5){
        return "El nombre de usuario debe ser mayor a 5 caracteres"
    }
    else if(userName.value.length > 30){
        return "El nombre de usuario debe ser menor a 30 caracteres"
    }

}



