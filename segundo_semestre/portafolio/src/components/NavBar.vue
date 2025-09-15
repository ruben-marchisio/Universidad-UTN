<script setup>
// Definimos un arreglo con los enlaces de navegación
// Cada objeto tiene un nombre (texto a mostrar) y un enlace (id de la sección)
const navegacion = [
  { nombre: "Sobre mí", enlace: "#sobre-mi" },
  { nombre: "Educación", enlace: "#educacion" },
  { nombre: "Proyectos", enlace: "#proyectos" },
  { nombre: "Contacto", enlace: "#contacto" },
];
</script>

<template>
  <!-- Barra de navegación principal -->
  <nav class="navbar" role="navigation" aria-label="Principal">
    <div class="navbar-container">
      <ul class="navbar-menu">
        <!-- Render dinámico de los ítems del menú -->
        <li v-for="(item, index) in navegacion" :key="index">
          <a :href="item.enlace" class="navbar-item">
            {{ item.nombre }}
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
/* ======== Barra de navegación ======== */
.navbar {
  background-color: #618faa; /* Color principal */
  padding: 0.5rem 1rem;
  position: sticky; /* Fija la barra en la parte superior al hacer scroll */
  top: 0;
  z-index: 50; /* Garantiza que quede por encima del contenido */
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
}

/* Lista de enlaces alineada con flexbox */
.navbar-menu {
  list-style: none;
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin: 0;
  padding: 0;
}

/* Estilo base de los ítems */
.navbar-item {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: background 0.3s ease;
}

/* Efecto hover */
.navbar-item:hover {
  background-color: rgba(0, 0, 0, 0.25);
}

/* ======== Responsive ======== */
@media (max-width: 768px) {
  .navbar-menu {
    flex-direction: column; /* En pantallas pequeñas el menú pasa a columna */
    align-items: center;
  }
  .navbar-item {
    width: 100%;
    text-align: center;
  }
}
</style>
