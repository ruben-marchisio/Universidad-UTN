<script setup>
// Importamos la barra y tu bloque de datos personales
import NavBar from './components/NavBar.vue'
import DatosPersonales from './components/DatosPersonales.vue'
import Educacion from './components/Educacion.vue'
import Experiencia from './components/Experiencia.vue'
import Proyectos from './components/Proyectos.vue'
import Habilidades from './components/Habilidades.vue'
import Intereses from './components/Intereses.vue'
</script>

<template>
  <!-- Barra de navegación -->
  <NavBar />

  <!-- Ancla para "Sobre mí" -->
  <div id="sobre-mi"></div>

  <!-- Hero / Datos personales -->
  <header class="hero-wrap">
    <DatosPersonales />
  </header>

  <!-- Contenido principal -->
  <main class="container">
    <!-- EDUCACIÓN -->
    <section id="educacion" class="section">
      <h2>Educación</h2>
      <Educacion />
      <p class="placeholder">Pronto: línea de tiempo educativa ✨</p>
    </section>

    <!-- Experiencia -->
<section id="experiencia" class="section">
   <Experiencia />
</section>

    <!-- PROYECTOS -->
     <section id="proyectos" class="section">
  <Proyectos />
</section>

    <!-- HABILIDADES -->
<section id="habilidades" class="section">
  <Habilidades />
</section>

   
<!-- INTERESES -->
<section id="intereses" class="section">
  <Intereses />
</section>
  </main>
</template>

<style scoped>
/* ===== Layout base ===== */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 12px 20px 60px;
}

/* Hero wrapper (separa el hero del resto del contenido) */
.hero-wrap {
  padding: 10px 20px 0;
}

/* ===== Secciones ===== */
.section {
  padding: 70px 10px;
  border-bottom: 1px solid var(--border, rgba(148,163,184,0.2));
  background: transparent;
}

.section h2 {
  margin: 0 0 18px;
  font-size: 2rem;
  color: var(--heading, #f8fafc);
  text-shadow: 0 0 8px rgba(176,38,255,0.30);
}

/* Placeholder temporal */
.placeholder {
  margin: 0;
  color: var(--text-muted, #94a3b8);
}

/* ===== Dark Neon (por si tu global no lo tiene aún) ===== */
:root {
  scroll-behavior: smooth; 
}

:where(html, body) {
  background:
    radial-gradient(1200px 800px at 10% -10%, rgba(176, 38, 255, 0.08), transparent 60%),
    radial-gradient(1000px 700px at 90% 10%, rgba(0, 229, 255, 0.08), transparent 60%),
    var(--bg, #0b0f1a);
  color: var(--text, #e2e8f0);
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .section {
    padding: 56px 8px;
  }
  .section h2 {
    font-size: 1.7rem;
  }
}
</style>
