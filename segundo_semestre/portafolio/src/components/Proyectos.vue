<script setup>
const proyectos = [
  {
    titulo: "Gestor de Kiosko — KiokoG (2025)",
    descripcion:
      "Aplicación web progresiva (PWA) Offline-First para gestión de kioscos. Desarrollada con Vue, IndexedDB y MongoDB. Sincronización automática y escaneo de códigos.",
    imagen: "https://cdn-icons-png.flaticon.com/512/9414/9414101.png",
    linkProyecto: "https://www.kiokog.com",
    linkCodigo: "https://github.com/ruben-marchisio"
  },
  {
    titulo: "Portafolio Personal (2025)",
    descripcion:
      "Sitio web construido con Vue + Vite, diseño moderno y responsive. Presenta educación, experiencia y proyectos destacados.",
    imagen: "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    linkProyecto: "https://github.com/ruben-marchisio",
    linkCodigo: "https://github.com/ruben-marchisio"
  },
  {
    titulo: "Asistente de Voz para Carga Masiva (2024)",
    descripcion:
      "Módulo del sistema KiokoG que permite registrar productos mediante comandos de voz. Implementado con JavaScript y reconocimiento de voz nativo.",
    imagen: "https://cdn-icons-png.flaticon.com/512/4712/4712026.png",
    linkProyecto: "https://github.com/ruben-marchisio",
    linkCodigo: "https://github.com/ruben-marchisio"
  },
  {
    titulo: "API de Productos Comunitarios (2024)",
    descripcion:
      "Backend colaborativo que centraliza información de productos escaneados. Construido con Node.js y MongoDB Atlas.",
    imagen: "https://cdn-icons-png.flaticon.com/512/6062/6062646.png",
    linkProyecto: "https://github.com/ruben-marchisio",
    linkCodigo: "https://github.com/ruben-marchisio"
  }
]
</script>

<template>
  <section class="proyectos-wrap">
    <h2 class="title">Proyectos</h2>
    <h3 class="subtitle">Algunos proyectos son ficticios y se utilizan con fines demostrativos.</h3>

    <div class="grid">
      <article v-for="(p, i) in proyectos" :key="i" class="card">
        <div class="img-wrap">
          <img :src="p.imagen" :alt="p.titulo" />
        </div>
        <div class="info">
          <h3>{{ p.titulo }}</h3>
          <p>{{ p.descripcion }}</p>

          <div class="btns">
            <a :href="p.linkProyecto" target="_blank" class="btn btn-primary">Ver Proyecto</a>
            <a :href="p.linkCodigo" target="_blank" class="btn btn-code">Ver Código</a>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.proyectos-wrap {
  max-width: 1100px;
  margin: 0 auto;
  padding: 50px 20px;
  color: #e2e8f0;
  text-align: center;
}
.subtitle {
  font-size: 1rem;
  font-weight: 500;
  color: #94a3b8;
  margin-top: -10px;
  margin-bottom: 26px;
  text-shadow: 0 0 6px rgba(176, 38, 255, 0.15);
}

.title {
  font-size: 2rem;
  margin-bottom: 30px;
  text-shadow: 0 0 8px rgba(176, 38, 255, 0.3);
}

.grid {
  display: grid;
  gap: 24px;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
}

.card {
  background: rgba(18, 26, 42, 0.6);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 0 18px rgba(0, 229, 255, 0.08);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 24px rgba(0, 229, 255, 0.2), 0 0 40px rgba(176, 38, 255, 0.15);
}

.img-wrap {
  background: linear-gradient(90deg, #b026ff, #00e5ff);
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.img-wrap img {
  width: 90px;
  height: 90px;
  object-fit: contain;
  filter: drop-shadow(0 0 6px rgba(0, 0, 0, 0.4));
}

.info {
  padding: 16px;
  text-align: left;
}

.info h3 {
  font-size: 1.1rem;
  color: #00ffc6;
  margin-bottom: 8px;
}

.info p {
  font-size: 0.95rem;
  line-height: 1.5;
  color: #cbd5e1;
  margin-bottom: 16px;
}

.btns {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn {
  flex: 1;
  text-align: center;
  padding: 8px 10px;
  border-radius: 10px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.btn-primary {
  background: linear-gradient(90deg, #00e5ff, #b026ff);
  color: #0b0f1a;
  border: none;
}

.btn-primary:hover {
  filter: brightness(1.1);
}

.btn-code {
  background: transparent;
  border: 1px solid rgba(148, 163, 184, 0.3);
  color: #e2e8f0;
}

.btn-code:hover {
  background: rgba(0, 229, 255, 0.1);
}
</style>
