<script setup>
// Tus estudios y cursos, se pueden editar o ampliar cuando quieras
const educacion = [
  {
    titulo: "Curso de Python",
    institucion: "Plataforma Online",
    año: "2020",
    descripcion: "Introducción a la programación con Python. Estructuras, funciones y lógica básica."
  },
  {
    titulo: "Curso de Git y Control de Versiones",
    institucion: "Udemy",
    año: "2022",
    descripcion: "Uso de Git y GitHub para proyectos colaborativos. Ramas, merges y manejo de repositorios."
  },
  {
    titulo: "Desarrollo de Aplicaciones Web",
    institucion: "APX School",
    año: "2024",
    descripcion: "Curso enfocado en tecnologías web: HTML, CSS, JavaScript y bases de datos."
  },
  {
    titulo: "Técnico Universitario en Programación",
    institucion: "UTN",
    año: "2025 (En curso)",
    descripcion: "Carrera universitaria centrada en desarrollo de software, algoritmos y bases de datos."
  }
]
</script>

<template>
  <section class="educacion-section">

    <div class="timeline">
      <div
        v-for="(item, index) in educacion"
        :key="index"
        class="timeline-item"
        :class="{ last: index === educacion.length - 1 }"
      >
        <div class="line"></div>
        <div class="dot"></div>

        <div class="content">
          <span class="año">{{ item.año }}</span>
          <h3 class="titulo-item">{{ item.titulo }}</h3>
          <p class="institucion">{{ item.institucion }}</p>
          <p class="descripcion">{{ item.descripcion }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.educacion-section {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 20px;
  color: var(--text, #e2e8f0);
}

/* ===== Título general ===== */
.titulo {
  text-align: center;
  font-size: 2rem;
  color: var(--heading, #f8fafc);
  text-shadow: 0 0 8px rgba(176, 38, 255, 0.3);
  margin-bottom: 40px;
}

/* ===== Timeline ===== */
.timeline {
  position: relative;
  margin: 0;
  padding: 0;
}

.timeline-item {
  position: relative;
  padding-left: 40px;
  margin-bottom: 40px;
}

.timeline-item.last {
  margin-bottom: 0;
}

/* Línea vertical */
.line {
  position: absolute;
  left: 15px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: var(--border, rgba(148,163,184,0.3));
}

/* Punto brillante */
.dot {
  position: absolute;
  left: 6px;
  top: 5px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--primary, #00e5ff);
  box-shadow: 0 0 12px rgba(0,229,255,0.6), 0 0 24px rgba(176,38,255,0.4);
}

/* Contenido */
.content {
  background: rgba(18,26,42,0.6);
  padding: 16px 20px;
  border-radius: 12px;
  border: 1px solid var(--border, rgba(148,163,184,0.2));
  box-shadow: 0 0 12px rgba(0,229,255,0.1);
  transition: transform .2s ease, box-shadow .2s ease;
}

.content:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 18px rgba(0,229,255,0.25), 0 0 36px rgba(176,38,255,0.15);
}

/* Texto */
.año {
  display: inline-block;
  font-weight: 700;
  color: var(--accent, #00ffc6);
  margin-bottom: 6px;
}
.titulo-item {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0;
}
.institucion {
  color: var(--text-muted, #94a3b8);
  margin: 4px 0;
}
.descripcion {
  font-size: 0.95rem;
  line-height: 1.5;
  color: var(--text, #cbd5e1);
}

/* ===== Responsive ===== */
@media (max-width: 640px) {
  .timeline-item {
    padding-left: 30px;
  }
  .dot {
    width: 14px;
    height: 14px;
    left: 4px;
  }
}
</style>
