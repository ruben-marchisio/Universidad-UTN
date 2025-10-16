<script setup>
// import data from './data/personal.js'
// const { nombre, titulo, descripcion1, descripcion2, telefono, ubicacion, redesSociales } = data

const nombre = "Ruben Marchisio"
const titulo = "Técnico universitario en programacion - UTN"
const descripcion1 = "Bienvenido a mi portafolio, Soy un desarrollador web"
const descripcion2 = "Apasionado por crear soluciones digitales innovadoras y funcionales."
const telefono = "Mi Teléfono personal: 265246586"
const ubicacion = "Malargüe, Mendoza, Argentina"
const redesSociales = [
  { nombre: "LinkedIn", url: "", icono: "" },
  { nombre: "GitHub", url: "", icono: "" },
  { nombre: "Instagram", url: "", icono: "" },
]

// 📸 Ruta de tu imagen 
import fotoPerfil from '../assets/foto-perfil.jpeg'
</script>

<template>
  <section class="datos-personal hero" aria-labelledby="heading-yo">
    <div class="info">
      <div class="foto-wrap">
        <img :src="fotoPerfil" alt="Foto de Ruben Marchisio" class="foto" />
      </div>

      <!-- Nombre y título -->
      <h1 id="heading-yo" class="nombre">{{ nombre }}</h1>
      <h2 class="titulo">{{ titulo }}</h2>

      <!-- Descripciones -->
      <p class="descripcion">{{ descripcion1 }}</p>
      <p class="descripcion">{{ descripcion2 }}</p>

      <!-- Contacto -->
      <ul class="meta" aria-label="Datos de contacto">
        <li class="meta-item">{{ telefono }}</li>
        <li class="meta-item">{{ ubicacion }}</li>
      </ul>

      <!-- Redes sociales -->
      <nav class="redes-sociales" aria-label="Redes sociales">
        <a
          v-for="(red, index) in redesSociales"
          :key="index"
          :href="red.url || '#'"
          target="_blank"
          rel="noopener noreferrer"
          class="btn-red"
        >
          {{ red.nombre }}
        </a>
      </nav>
    </div>
  </section>
</template>

<style scoped>


/* Contenedor principal */
.datos-personal.hero {
  background: linear-gradient(180deg, rgba(18,26,42,0.88), rgba(15,28,46,0.68));
  padding: 40px 22px;
  border: 1px solid var(--border, rgba(148,163,184,0.2));
  border-radius: var(--radius, 16px);
  box-shadow: 0 0 12px rgba(0,229,255,0.25), 0 0 30px rgba(176,38,255,0.12);
}

.info {
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

/* === Imagen de perfil === */
.foto-wrap {
  display: flex;
  justify-content: center;
  margin-bottom: 16px;
}
.foto {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid var(--border, rgba(148,163,184,0.2));
  box-shadow: 0 0 20px rgba(0,229,255,0.3), 0 0 40px rgba(176,38,255,0.2);
  transition: transform .3s ease, box-shadow .3s ease;
}
.foto:hover {
  transform: scale(1.03);
  box-shadow: 0 0 25px rgba(0,229,255,0.4), 0 0 50px rgba(176,38,255,0.25);
}

/* === Tipografía === */
.nombre {
  font-size: 2.4rem;
  font-weight: 800;
  margin: 0 0 8px;
  color: var(--heading, #f8fafc);
  text-shadow: 0 0 10px rgba(0,229,255,0.25);
}

.titulo {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--accent, #00ffc6);
  margin-bottom: 16px;
}

.descripcion {
  max-width: 700px;
  margin: 0 auto 12px;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-muted, #94a3b8);
}

/* === Contacto (chips) === */
.meta {
  margin: 12px 0 0;
  padding: 0;
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
}

.meta-item {
  color: var(--text, #e2e8f0);
  border: 1px solid var(--border, rgba(148,163,184,0.2));
  border-radius: 999px;
  padding: 6px 12px;
  background: rgba(0,229,255,0.06);
}

/* === Redes sociales === */
.redes-sociales {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
}

.btn-red {
  display: inline-block;
  padding: 10px 16px;
  border-radius: 10px;
  border: 1px solid var(--border, rgba(148,163,184,0.2));
  background: rgba(18,26,42,0.6);
  color: var(--text, #e2e8f0);
  font-weight: 600;
  text-decoration: none;
  transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
  box-shadow: 0 0 12px rgba(0,229,255,0.18);
}
.btn-red:hover {
  border-color: var(--border-hover, rgba(148,163,184,0.35));
  transform: translateY(-1px);
  box-shadow: 0 0 12px rgba(0,229,255,0.25), 0 0 24px rgba(176,38,255,0.2);
}

/* === Responsive === */
@media (max-width: 640px) {
  .foto { width: 130px; height: 130px; }
  .nombre { font-size: 2rem; }
  .titulo { font-size: 1rem; }
  .descripcion { font-size: 0.96rem; }
}
</style>
