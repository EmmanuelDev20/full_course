document.addEventListener("DOMContentLoaded", (event) => {
  // Clases
  // document.querySelector(".thinking")
  // Id
  // document.querySelector("#thinking")
  // Etiqueta
  // document.querySelector("input")

  // document.querySelector("#thinking")
  // Variable
  // let thinking = document.getElementById("thinking")
  // Constante

  // let numero = 2;
  // numero = 8;
  // numero = 8;
  // numero = 8;
  // numero = 8;
  // numero = 878;

  // const pi = 3.1416

  // console.log(pi)


  // Funciones en js
  // function saludar(nombre, edad) {
  //   console.log('Hola mi gente', nombre, edad)
  // }

  // saludar("Emmanuel", 30)


  // thinking.addEventListener("click", abrirModal)

  // function abrirModal() {
  //   console.log('Hola')
  // }




  // Cambio en tabs
  const home = document.getElementById("home");
  const games = document.getElementById("games");
  const videos = document.getElementById("videos");
  const store = document.getElementById("store");
  const friends = document.getElementById("friends");

  home.addEventListener("click", function () {
    home.classList.add("active");
    videos.classList.remove("active");
    store.classList.remove("active");
    friends.classList.remove("active");
    games.classList.remove("active");
  });
  
  games.addEventListener("click", function () {
    games.classList.add("active");
    videos.classList.remove("active");
    store.classList.remove("active");
    friends.classList.remove("active");
    home.classList.remove("active");
  });

  videos.addEventListener("click", function () {
    videos.classList.add("active");
    home.classList.remove("active");
    store.classList.remove("active");
    friends.classList.remove("active");
    games.classList.remove("active");
  });

  store.addEventListener("click", function () {
    store.classList.add("active");
    videos.classList.remove("active");
    home.classList.remove("active");
    friends.classList.remove("active");
    games.classList.remove("active");
  });

  friends.addEventListener("click", function () {
    friends.classList.add("active");
    videos.classList.remove("active");
    store.classList.remove("active");
    home.classList.remove("active");
    games.classList.remove("active");
  });

  const modal = document.getElementById("modal");
  modal.addEventListener("click", function(eventoNuevo) {
    if (eventoNuevo.target === modal) {
      modal.classList.add("dnone")
      modal.classList.remove("dflex")
    }
  })

  const thinking = document.getElementById("thinking");

  thinking.addEventListener("click", function abrirModal() {
     modal.classList.remove("dnone")
     modal.classList.add("dflex")
  });

});
