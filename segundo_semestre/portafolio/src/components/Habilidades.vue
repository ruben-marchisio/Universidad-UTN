<script setup>
// Cada grupo tiene un título y una lista de tecnologías con nivel
const habilidades = [
  {
    categoria: "Lenguajes de Programación",
    items: [
      { nombre: "JavaScript", nivel: "Avanzado", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" },
      { nombre: "Python", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" },
      { nombre: "HTML / CSS", nivel: "Avanzado", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" },
      { nombre: "Java", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" },
      { nombre: "SQL", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" }
    ]
  },
  {
    categoria: "Frameworks y Librerías",
    items: [
      { nombre: "Vue.js", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg" },
      { nombre: "Node.js", nivel: "Avanzado", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" },
      { nombre: "Bootstrap", nivel: "Avanzado", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg" },
      { nombre: "Django", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" }
    ]
  },
  {
    categoria: "Herramientas y Software",
    items: [
      { nombre: "Git / GitHub", nivel: "Avanzado", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" },
      { nombre: "Docker", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" },
      { nombre: "VS Code", nivel: "Avanzado", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" },
      { nombre: "Figma", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" }
    ]
  },
  {
    categoria: "Bases de Datos",
    items: [
      { nombre: "MongoDB", nivel: "Avanzado", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" },
      { nombre: "MySQL", nivel: "Intermedio", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" }
    ]
  }
]
</script>

<template>
  <section class="skills-section">
    <h2 class="title">Habilidades</h2>
    <h3 class="subtitle">Principales lenguajes, frameworks y herramientas que utilizo.</h3>

    <div
      v-for="(grupo, i) in habilidades"
      :key="i"
      class="grupo"
    >
      <h3 class="cat">{{ grupo.categoria }}</h3>

      <div class="grid">
        <div v-for="(item, j) in grupo.items" :key="j" class="skill-card">
          <img :src="item.icon" :alt="item.nombre" class="icon" />
          <div class="info">
            <h4>{{ item.nombre }}</h4>
            <p>{{ item.nivel }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.skills-section {
  max-width: 1000px;
  margin: 0 auto;
  padding: 50px 20px;
  color: #e2e8f0;
  text-align: center;
}

.title {
  font-size: 2rem;
  margin-bottom: 10px;
  text-shadow: 0 0 8px rgba(176, 38, 255, 0.3);
}

.subtitle {
  color: #94a3b8;
  margin-bottom: 36px;
}

.cat {
  text-align: left;
  color: #00ffc6;
  font-size: 1.2rem;
  margin: 30px 0 16px;
  text-shadow: 0 0 6px rgba(0,229,255,0.25);
}

.grid {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  justify-content: center;
}

.skill-card {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(18,26,42,.65);
  border: 1px solid rgba(148,163,184,.2);
  border-radius: 12px;
  padding: 8px 14px;
  min-width: 190px;
  transition: all .2s ease;
}

.skill-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 16px rgba(0,229,255,.25);
  border-color: rgba(0,229,255,.4);
}

.icon {
  width: 30px;
  height: 30px;
  object-fit: contain;
}

.info {
  text-align: left;
}
.info h4 {
  margin: 0;
  font-size: 1rem;
  color: #f8fafc;
}
.info p {
  margin: 0;
  font-size: 0.85rem;
  color: #94a3b8;
}

/* Responsive */
@media (max-width: 640px) {
  .skill-card {
    min-width: 150px;
    padding: 8px 10px;
  }
  .icon {
    width: 26px;
    height: 26px;
  }
}
</style>
