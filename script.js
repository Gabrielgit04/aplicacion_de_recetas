fetch("http://127.0.0.1:5000/api/crear_usuario_nuevo", {
    method : 'POST',
    headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "user": 'Fabricio',
        "email": 'sfdiegoaborges@gmail.com',
        "passw": '230904'
      })
    })
      .then(response => response.status)
      .then(data => {
        console.log('Receta agregada:', data);
      })
      .catch(error => {
        console.error('Error al agregar receta:', error);
      });