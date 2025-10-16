<script setup>
import { onMounted, onBeforeUnmount, ref } from "vue";

// Enlaces de navegación (ids de sección)
const navegacion = [
  { nombre: "Sobre mí", enlace: "#sobre-mi" },
  { nombre: "Educación", enlace: "#educacion" },
  { nombre: "Experiencia", enlace: "#experiencia" },
  { nombre: "Proyectos", enlace: "#proyectos" },
  { nombre: "Habilidades", enlace: "#habilidades" },
  { nombre: "Intereses", enlace: "#intereses" },
];

const isOpen = ref(false);
const activeHash = ref(navegacion[0].enlace);

// Scroll suave al hacer click
function goTo(hash) {
  const el = document.querySelector(hash);
  if (!el) return;
  el.scrollIntoView({ behavior: "smooth", block: "start" });
  activeHash.value = hash;
  isOpen.value = false;
}

// Observa secciones y marca activa en la barra
let observer;
onMounted(() => {
  const opts = { root: null, rootMargin: "0px 0px -60% 0px", threshold: 0 };
  observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      const id = "#" + entry.target.id;
      if (entry.isIntersecting) activeHash.value = id;
    });
  }, opts);

  navegacion.forEach((item) => {
    const el = document.querySelector(item.enlace);
    if (el) observer.observe(el);
  });

  // Habilitá scroll-behavior si no lo tenés en CSS global
  const html = document.documentElement;
  if (!getComputedStyle(html).scrollBehavior || getComputedStyle(html).scrollBehavior === "auto") {
    html.style.scrollBehavior = "smooth";
  }
});

onBeforeUnmount(() => {
  if (observer) observer.disconnect();
});
</script>

<template>
  <nav class="navbar" role="navigation" aria-label="Principal">
    <div class="navbar-container">
      <button
        class="menu-toggle"
        :aria-expanded="isOpen ? 'true' : 'false'"
        aria-controls="menu"
        @click="isOpen = !isOpen"
      >
        <span class="sr-only">Abrir/cerrar menú</span>
        ☰
      </button>

      <ul
        id="menu"
        class="navbar-menu"
        :class="{ open: isOpen }"
        role="menubar"
      >
        <li
          v-for="(item, i) in navegacion"
          :key="i"
          class="navbar-item"
          role="none"
        >
          <a
            role="menuitem"
            :href="item.enlace"
            :class="['link', { active: activeHash === item.enlace }]"
            @click.prevent="goTo(item.enlace)"
          >
            {{ item.nombre }}
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
/* ===== Base / contenedor ===== */
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
  backdrop-filter: blur(10px);
  background: linear-gradient(180deg, rgba(11,15,26,0.85), rgba(11,15,26,0.55));
  border-bottom: 1px solid var(--border, rgba(148,163,184,0.2));
}

/* Layout */
.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ===== Botón hamburguesa ===== */
.menu-toggle {
  display: none;
  margin-right: 12px;
  font-size: 1.2rem;
  border: 1px solid var(--border, rgba(148,163,184,0.2));
  background: rgba(18,26,42,0.6);
  color: var(--text, #e2e8f0);
  border-radius: 10px;
  padding: 6px 10px;
  box-shadow: 0 0 12px rgba(0,229,255,0.18);
}
.menu-toggle:hover {
  border-color: var(--border-hover, rgba(148,163,184,0.35));
}

/* ===== Menú ===== */
.navbar-menu {
  list-style: none;
  display: flex;
  gap: 14px;
  margin: 0;
  padding: 0;
}
.navbar-item {
  display: inline-flex;
}

/* Links */
.link {
  color: var(--text, #e2e8f0);
  text-decoration: none;
  padding: 8px 12px;
  border: 1px solid transparent;
  border-radius: 12px;
  transition: border-color .2s ease, box-shadow .2s ease, transform .2s ease, background-color .2s ease;
}
.link:hover {
  border-color: var(--border-hover, rgba(148,163,184,0.35));
  box-shadow: 0 0 10px rgba(0,229,255,0.25);
  transform: translateY(-1px);
}
.link.active {
  background: rgba(0,229,255,0.08);
  border-color: rgba(0,229,255,0.35);
  box-shadow: 0 0 12px rgba(0,229,255,0.25), 0 0 24px rgba(176,38,255,0.18);
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .navbar-container {
    justify-content: space-between;
  }
  .menu-toggle {
    display: inline-block;
  }
  .navbar-menu {
    position: absolute;
    left: 0; right: 0; top: 54px;
    background: linear-gradient(180deg, rgba(11,15,26,0.95), rgba(11,15,26,0.85));
    border-bottom: 1px solid var(--border, rgba(148,163,184,0.2));
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 10px 0;
    display: none;
  }
  .navbar-menu.open {
    display: flex;
  }
  .link { width: calc(100% - 32px); text-align: center; }
}

/* ===== Utilidad a11y ===== */
.sr-only {
  position: absolute !important;
  height: 1px; width: 1px;
  overflow: hidden; clip: rect(1px, 1px, 1px, 1px);
  white-space: nowrap; border: 0; padding: 0; margin: -1px;
}
</style>
