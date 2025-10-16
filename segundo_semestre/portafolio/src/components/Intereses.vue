<script setup>
// Editá libremente. Mantengo un tono personal y concreto.
const intereses = [
  "Crear proyectos útiles para la gente: me motiva resolver problemas reales con software simple y accesible.",
  "KiokoG y el comercio local: me inspira ayudar a kioscos y pequeños negocios a digitalizarse sin complicaciones.",
  "Aprendizaje continuo: disfruto estudiar nuevas tecnologías (PWA, IndexedDB, IA práctica) y aplicarlas en mini-proyectos.",
  "Paseos en el parque con mi perro: desconectar, caminar y pensar ideas nuevas mientras escucho música.",
  "Fotografía casual y video corto: me gusta capturar momentos y usarlos para contar historias de proyectos.",
  "Trabajo en equipo: organizar tareas, revisar código y sumar desde la empatía y la comunicación clara."
]
</script>

<template>
  <section class="intereses-wrap">
    <!-- BG animado (2 blobs) -->
    <svg class="blob blob-a" viewBox="0 0 600 600" aria-hidden="true">
      <defs>
        <linearGradient id="gradA" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#b026ff"/>
          <stop offset="100%" stop-color="#00e5ff"/>
        </linearGradient>
      </defs>
      <path
        fill="url(#gradA)"
        d="M300,520C210,520,90,470,70,360C50,250,140,170,230,120C320,70,410,60,470,120C530,180,560,290,510,380C470,450,390,520,300,520Z"
      />
    </svg>

    <svg class="blob blob-b" viewBox="0 0 600 600" aria-hidden="true">
      <defs>
        <linearGradient id="gradB" x1="100%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#00ffc6"/>
          <stop offset="100%" stop-color="#0ea5e9"/>
        </linearGradient>
      </defs>
      <path
        fill="url(#gradB)"
        d="M300,520C220,510,120,470,90,380C60,290,110,190,200,140C290,90,400,90,470,160C540,230,560,350,510,430C470,495,380,530,300,520Z"
      />
    </svg>

    <!-- Contenido -->
    <div class="card">
      <h2 class="title">Intereses</h2>
      <h3 class="subtitle">Un poco de lo que me mueve dentro y fuera del código.</h3>

      <ul class="list">
        <li v-for="(i, idx) in intereses" :key="idx">
          <span class="dot" aria-hidden="true"></span>
          <p>{{ i }}</p>
        </li>
      </ul>
    </div>
  </section>
</template>


<style scoped>
.intereses-wrap{
  position: relative;
  overflow: hidden;
  isolation: isolate;
  min-height: 460px;
  padding: 64px 20px;
  display: grid;
  place-items: center;
  color: #e2e8f0;
}
/* Fondo partículas */

.blob{
  position: absolute;
  width: 60vmax;
  height: 60vmax;
  opacity: .55;
  filter: blur(30px) saturate(120%);
  pointer-events: none;

  /* 🔧 FIXES IMPORTANTES */
  z-index: 1;                 
  transform-box: fill-box;   
  transform-origin: 40% 40%;  
  will-change: transform;    
}

.card { position: relative; z-index: 1; }

/* Movimiento (más visible y un poco más rápido) */
.blob-a{
  left: -19vmax; top: -15vmax;
  animation: floatA 9s ease-in-out infinite;
}
.blob-b{
  right: -14vmax; bottom: -10vmax;
  animation: floatB 12s ease-in-out infinite;
}


@keyframes floatA{
  0%   { transform: translate(0,0) rotate(0deg) scale(1); }
  25%  { transform: translate(6vmax,3vmax) rotate(10deg) scale(1.08); }
  50%  { transform: translate(0,6vmax)   rotate(18deg) scale(1.15); }
  75%  { transform: translate(-4vmax,3vmax) rotate(10deg) scale(1.08); }
  100% { transform: translate(0,0) rotate(0deg) scale(1); }
}

@keyframes floatB{
  0%   { transform: translate(0,0) rotate(0deg) scale(1); }
  25%  { transform: translate(-4vmax,-5vmax) rotate(-8deg) scale(0.95); }
  50%  { transform: translate(-7vmax,0) rotate(-16deg) scale(0.90); }
  75%  { transform: translate(-4vmax,3vmax) rotate(-8deg) scale(0.95); }
  100% { transform: translate(0,0) rotate(0deg) scale(1); }
}



/* Tarjeta de contenido (glass) */
.card{
  width: min(1000px, 92vw);
  background: rgba(10,16,28,.55);
  border: 1px solid rgba(148,163,184,.22);
  border-radius: 18px;
  padding: 26px 20px;
  box-shadow: 0 10px 28px rgba(0,0,0,.35), 0 0 28px rgba(0,229,255,.10);
  backdrop-filter: blur(6px);
}


.title{
  text-align: center;
  font-size: 2rem;
  margin: 0 0 6px;
  text-shadow: 0 0 8px rgba(176,38,255,.25);
}
.subtitle{
  text-align: center;
  color: #94a3b8;
  margin: 0 0 18px;
}

/* Lista */
.list{
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 12px;
}
.list li{
  display: grid;
  grid-template-columns: 18px 1fr;
  gap: 10px;
  align-items: start;
  background: rgba(18,26,42,.45);
  border: 1px solid rgba(148,163,184,.18);
  border-radius: 12px;
  padding: 10px 12px;
}
.dot{
  width: 10px; height: 10px; border-radius: 999px;
  background: radial-gradient(circle at 30% 30%, #00e5ff, #b026ff);
  box-shadow: 0 0 10px rgba(0,229,255,.5);
  margin-top: 6px;
}
.list p{
  margin: 0;
  line-height: 1.55;
  color: #cbd5e1;
}

/* Responsive */
@media (max-width: 640px){
  .card{ padding: 18px 14px; }
}
</style>
