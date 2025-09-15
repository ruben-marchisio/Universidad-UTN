<script setup>
// Importamos el componente de la barra de navegación
// Ajustá la ruta según tu estructura real (components/NavBar.vue)
import NavBar from './components/NavBar.vue';
import DatosPersonales from './components/DatosPersonales.vue';
</script>

<template>

  <header>
      <!-- Encabezado con la barra de navegación -->
    <NavBar />
    <!-- Componente de datos personales -->
    <DatosPersonales />
  </header>

  <!-- Contenido principal con secciones -->
  <main>
    <section id="sobre-mi"><h2>Conóceme</h2></section>
    <section id="educacion"><h2>Educación</h2></section>
    <section id="proyectos"><h2>Proyectos</h2></section>
    <section id="contacto"><h2>Contacto</h2></section>
  </main>
</template>

<style scoped>
/* ======== Secciones del contenido ======== */
section {
  padding: 60px 20px;
  text-align: center;
  background-color: #f9f9f9; /* Fondo uniforme, look minimalista */
  border-bottom: 1px solid #ddd;
}

section h2 {
  margin: 0;
  font-size: 1.8rem;
  color: #333;
}
</style>

<!-- 💡 TIP recomendado:
Agregá en tu CSS global:
:root { scroll-behavior: smooth; }
para que el scroll hacia las secciones sea suave al hacer clic en los enlaces -->
