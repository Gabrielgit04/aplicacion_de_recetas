fetch("http://127.0.0.1:5000/api/crear_usuario_nuevo", {
    method : 'POST',
    headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "user": 'no www',
        "email": 'epaas',
        "passw": '230904'
      })
    })
      .then(response => response.status)
      .then(data => {
          if (data == 201){
            console.log("se ha registrado con exito")
          }
          else if(data == 456){
            console.log("ya existe un usuario con ese nombre")
          }
          else if(data == 457){
            console.log("el email ya esta registrado")
          }
      })
      .catch(error => {
        console.error('Error al agregar receta:', error);
      });