<script setup>
import { onMounted, onUnmounted, ref } from 'vue'

const intereses = [
  "Crear proyectos útiles para la gente: me motiva resolver problemas reales con software simple y accesible.",
  "KiokoG y el comercio local: me inspira ayudar a kioscos y pequeños negocios a digitalizarse sin complicaciones.",
  "Aprendizaje continuo: disfruto estudiar nuevas tecnologías (PWA, IndexedDB, IA práctica) y aplicarlas en mini-proyectos.",
  "Paseos en el parque con mi perro: desconectar, caminar y pensar ideas nuevas mientras escucho música.",
  "Fotografía casual y video corto: me gusta capturar momentos y usarlos para contar historias de proyectos.",
  "Trabajo en equipo: organizar tareas, revisar código y sumar desde la empatía y la comunicación clara."
]

// ===== Partículas tipo “nieve” =====
const canvasRef = ref(null)
let ctx, rafId
let particles = []
let w = 0, h = 0

const opts = {
  density: 0.00020,   // más valor => más partículas
  sizeMin: 1.0,
  sizeMax: 2.6,
  speedMin: 20,       // px/seg
  speedMax: 60,
  drift: 12,          // px/seg (deriva horizontal)
  colors: ['#c8f5ff','#a5f3fc','#e9d5ff']
}

function rnd(a,b){ return a + Math.random()*(b-a) }
function makeParticle() {
  const r = rnd(opts.sizeMin, opts.sizeMax)
  return {
    x: Math.random()*w,
    y: rnd(-h, 0),
    r,
    vy: rnd(opts.speedMin, opts.speedMax)/60,
    vx: rnd(-opts.drift, opts.drift)/60,
    a: rnd(0, Math.PI*2),
    col: opts.colors[Math.floor(Math.random()*opts.colors.length)]
  }
}

function resize() {
  const c = canvasRef.value
  if (!c) return
  const dpr = Math.max(1, window.devicePixelRatio || 1)
  w = c.width = c.offsetWidth * dpr
  h = c.height = c.offsetHeight * dpr
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0)

  const target = Math.max(18, Math.floor((c.offsetWidth * c.offsetHeight) * opts.density))
  if (particles.length < target) {
    for (let i=particles.length; i<target; i++) particles.push(makeParticle())
  } else {
    particles.length = target
  }
}

function draw() {
  ctx.clearRect(0,0,w,h)
  for (let p of particles) {
    p.a += 0.02
    p.x += p.vx + Math.cos(p.a) * 0.2
    p.y += p.vy
    if (p.y - p.r > h) { // reciclar
      p.x = Math.random()*w
      p.y = rnd(-40, -10)
      p.vy = rnd(opts.speedMin, opts.speedMax)/60
      p.vx = rnd(-opts.drift, opts.drift)/60
    }
    ctx.beginPath()
    ctx.arc(p.x, p.y, p.r, 0, Math.PI*2)
    ctx.fillStyle = p.col
    ctx.shadowColor = p.col
    ctx.shadowBlur = 8
    ctx.fill()
    ctx.shadowBlur = 0
  }
  rafId = requestAnimationFrame(draw)
}

onMounted(() => {
  const c = canvasRef.value
  if (!c) return
  ctx = c.getContext('2d', { alpha: true })
  resize()
  window.addEventListener('resize', resize)
  rafId = requestAnimationFrame(draw) // forzamos animación
})

onUnmounted(() => {
  window.removeEventListener('resize', resize)
  cancelAnimationFrame(rafId)
})
</script>

<template>
  <section class="intereses-wrap">
    <canvas ref="canvasRef" class="snow"></canvas>

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
.snow{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
  opacity: .9;
  background:
    radial-gradient(1200px 500px at 20% 0%, rgba(176,38,255,.10), transparent 60%),
    radial-gradient(1200px 500px at 80% 100%, rgba(0,229,255,.10), transparent 55%);
}

/* Tarjeta (glass) */
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
  list-style: none; padding: 0; margin: 0; display: grid; gap: 12px;
}
.list li{
  display: grid; grid-template-columns: 18px 1fr; gap: 10px; align-items: start;
  background: rgba(18,26,42,.45);
  border: 1px solid rgba(148,163,184,.18);
  border-radius: 12px; padding: 10px 12px;
}
.dot{
  width: 10px; height: 10px; border-radius: 999px;
  background: radial-gradient(circle at 30% 30%, #00e5ff, #b026ff);
  box-shadow: 0 0 10px rgba(0,229,255,.5); margin-top: 6px;
}
.list p{ margin: 0; line-height: 1.55; color: #cbd5e1; }

/* Responsive */
@media (max-width: 640px){ .card{ padding: 18px 14px; } }
</style>
