<script setup>
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
</script>

<template>
  <section class="datos-personal">
    <div class="info">
      <!-- Nombre y título -->
      <h1 class="nombre">{{ nombre }}</h1>
      <h2 class="titulo">{{ titulo }}</h2>

      <!-- Descripciones -->
      <p class="descripcion">{{ descripcion1 }}</p>
      <p class="descripcion">{{ descripcion2 }}</p>

      <!-- Contacto -->
      <p class="contacto">{{ telefono }}</p>
      <p class="contacto">{{ ubicacion }}</p>

      <!-- Redes sociales -->
      <div class="redes-sociales">
        <a
          v-for="(red, index) in redesSociales"
          :key="index"
          :href="red.url"
          target="_blank"
          rel="noopener noreferrer"
          class="btn-red"
        >
          {{ red.nombre }}
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* ===== Contenedor principal ===== */
.datos-personal {
  background: linear-gradient(135deg, #f3f4f6, #e5e7eb);
  padding: 60px 20px;
  border-bottom: 1px solid #d1d5db;
}

.info {
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

/* ===== Tipografía ===== */
.nombre {
  font-size: 2.4rem;
  font-weight: 700;
  margin: 0 0 8px;
  color: #111827;
}

.titulo {
  font-size: 1.2rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 20px;
}

.descripcion {
  max-width: 700px;
  margin: 0 auto 12px;
  font-size: 1rem;
  line-height: 1.6;
  color: #4b5563;
}

.contacto {
  font-size: 0.95rem;
  font-weight: 500;
  margin: 6px 0;
  color: #1f2937;
}

/* ===== Redes sociales ===== */
.redes-sociales {
  margin-top: 22px;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
}

.btn-red {
  display: inline-block;
  padding: 10px 16px;
  border-radius: 8px;
  border: 1px solid #d1d5db;
  background-color: #fff;
  color: #111827;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.2s ease;
}

.btn-red:hover {
  background-color: #f3f4f6;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

/* ===== Responsive ===== */
@media (max-width: 640px) {
  .nombre {
    font-size: 1.8rem;
  }
  .titulo {
    font-size: 1rem;
  }
  .descripcion {
    font-size: 0.95rem;
  }
}
</style>
