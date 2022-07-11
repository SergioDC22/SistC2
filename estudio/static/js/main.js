document.addEventListener('DOMContentLoaded',()=>{
    const elementosCarousel= document.querySelectorAll('.carousel');
    M.Carousel.init(elementosCarousel, {
        duration:150,
        dist: -80,
        shift: 5,
        padding: 5,
        numVisible: 3,
        indicators: true,
        noWrap: false
    });
});

function redireccionar(){
    location.href= 'index.html';
}

function validarFormulario(link) {
    let x = document.forms["ingreso"]["usuario"].value;
    let y = document.forms["ingreso"]["contrasenia"].value;
    if (x == "" || y == "") {
      alert("No se puede ingresar con campos vacios");
    }
    if (x != "" && y !="") {
        redireccionar(link);
    }
  }
