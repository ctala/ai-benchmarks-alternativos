# Seed 2.0 Code — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 85.477s | tokens_per_second: 72.0
- input_tokens: 302 | output_tokens: 6154

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

### Regla de oro para **fundador solo con capacidad limitada** (antes de ordenar):
> No empieces proyectos que **no entreguen valor de usuario INMEDIATO** o que **no puedas terminar en el trimestre**. Tu prioridad no es "constuir para el futuro" — es mantener el negocio vivo, liberar capacidad y multiplicar el valor de lo que ya tienes.

---

## 1. Análisis de tu CAPACIDAD REAL vs. iniciativas (clave: no mezcles "tiempo completo" con TU tiempo)
Tus números trimestrales (8 semanas):
- Tiempo de build útil: `4h/día * 5d/sem * 8sem = 160h` (asumimos 5 días laborables; si trabajas 6, son 192h — no cambia el resultado)
- Tiempo de soporte: `2h/día` (no delegable aún — todo lo que reduzca esto es GANANCIA de build futuro)

Ahora, evalúa cada iniciativa con TU capacidad, no la de un equipo de 2:
| Iniciativa | Esfuerzo REAL (TU tiempo) | Viabilidad trimestre? | Por qué |
|------------|-----------------------------|------------------------|---------|
| A (Reescribir framework) | 3 meses **TIEMPO COMPLETO** = `12sem * 40h/sem = 480h` → para ti, **6 MESES** de trabajo (porque solo trabajas 4h/día de build) | ❌ IMPOSIBLE | Necesitas 3 VECES tu capacidad trimestral. No lo terminas, y arrancarlo te quita todo el tiempo sin entregar valor a usuarios. |
| B (Arreglar alta: 60% drop paso 2) | 1 semana TU tiempo = `20h` | ✅ 100% | Menos del 15% de tu capacidad, **alto impacto inmediato** (multiplica usuarios activados) |
| C (Panel de métricas) | 3 semanas TU tiempo, PERO DEPENDE DE A | ❌ IMPOSIBLE (por ahora) | La dependencia de A es casi siempre ARTIFICIAL (lo arreglamos después) |
| D (10 videos) | 2 semanas TU tiempo = `40h` | ✅ 100% | Impacto medio, pero **reduce tu tiempo de soporte futuro** (ganas build time) |

---

## 2. Ordenamiento TRIMESTRAL (8 semanas, ajustado a riesgos y ciclos de feedback)
### Objetivo del trimestre:
> 1) Arreglar el cuello de botella más grande de tu negocio (drop en alta) → multiplicar usuarios activados
> 2) Reducir tu carga de soporte → liberar tiempo de build para el futuro
> 3) Validar proyectos futuros sin perder el foco

---

#### 📅 SEMANA 1: **Prioridad 1 ABSOLUTA: Iniciativa B (Arreglar flujo de alta)**
##### Por qué:
Es tu cuello de botella de **activación**: si 100 usuarios empiezan el alta, solo 40 terminan hoy. Arreglando el drop de 60% a 30% (objetivo realista), pasas a 70 usuarios activados → **75% MÁS usuarios que pueden pagar, dar feedback o reducir tu soporte**.
##### Acción concreta (no hagas "perfecto"):
No reescribas todo el flujo → haz el **cambio mínimo que reduzca el drop**:
- Quita campos innecesarios en el paso 2
- Habilita auto-llenado con Google/Facebook
- Muestra un progreso claro ("Paso 2 de 3 → faltan 2 campos")
##### Métrica a medir HOY:
Tasa de drop en paso 2 ANTES y DESPUÉS (objetivo: <30%)

---

#### 📅 SEMANAS 2-3: **Prioridad 2: Iniciativa D (Grabar 10 videos)**
##### Por qué:
Ahora que tienes **más usuarios activados**, los videos:
1. **Reducen tu tiempo de soporte** (si grabas tutoriales de las 10 preguntas MÁS FRECUENTES de soporte) → objetivo: bajar de 2h/día a 1.5h/día de soporte (ganas 2.5h/sem de build)
2. Generan tráfico orgánico a largo plazo (sin gastar en publicidad)
##### Acción concreta (no hagas producción de cine):
Usa **Loom** (sin editar, 1 toma), graba desde tu pantalla, y prioriza:
- 3 videos de onboarding (pasos que los usuarios se traban)
- 5 videos de preguntas frecuentes de soporte
- 2 videos de valor agregado (ej: "Cómo sacar el máximo provecho de tu cuenta")

---

#### 📅 SEMANAS 4-8 (5 semanas restantes): **Iterar + Optimizar + Validar Futuro**
No llenes el tiempo con proyectos grandes — usa este espacio para **maximizar el valor de lo que ya lanzaste** y **liberar capacidad futura**:
##### 📅 SEMANA 4: Iterar Iniciativa B (1 semana)
- Medir la tasa de drop post-lanzamiento. Si bajó de 60% a 45%, haz otro cambio mínimo (ej: agregar un tooltip en el paso 2) y medir de nuevo.
##### 📅 SEMANAS 5-6: Optimizar Soporte (2 semanas)
- Automatiza respuestas de soporte con herramientas **low-code/sin código** (no necesitas programar):
  - Usa un formulario de soporte pre-llenado (Typeform) para que los usuarios digan su problema antes de escribirte
  - Usa un chatbot simple (ManyChat o Tidio) que muestre los videos de D como primera respuesta a preguntas comunes
- Objetivo: Bajar el tiempo de soporte a **1h/día** (ganas 5h/sem de build — MUY valioso para el futuro)
##### 📅 SEMANAS 7-8: Validar Iniciativa C (SIN A) + Preparar Próximo Trimestre (2 semanas)
- **Rompe la dependencia artificial de A**: El panel de métricas NO necesita un framework nuevo. Haz un **MVP mínimo** con tu framework actual:
  - Conecta tu base de datos a **Metabase** (herramienta low-code gratuita)
  - Crea un dashboard con las 3 métricas que tus clientes PEDEN (ej: número de visitas, ingresos, conversiones)
  - Comparte el dashboard privado con tus 10 clientes TOP
  - Esfuerzo: 2 semanas (en lugar de 3) → sin tocar el framework
- **Valida si A es realmente necesario**: Antes de pensar en reescribir, pregunta: ¿Es el framework el que me limita, o es mi código desorganizado? Prueba optimizaciones sin reescribir (ej: cachear consultas de BD, usar un CDN) → esfuerzo: 0.5 semanas, te ahorra 6 meses de trabajo.

---

## 3. ¿Qué pasa con A y C?
- **A (Reescribir framework)**: **NO lo toques este trimestre**. Es el "proyecto de vanidad" más común de fundadores solo: no entrega valor a usuarios HOY, te quita todo el tiempo de build, y al final no tienes nada que mostrar (ni más usuarios, ni más ingresos). Solo lo consideres cuando:
  - Tu negocio tenga ingresos recurrentes suficientes para delegar soporte
  - El framework actual esté IMPIDIENDO que lances funcionalidades que tus clientes PAGUEN
- **C (Panel de métricas)**: Lo convertimos en un MVP sin A en las semanas 7-8. Si los clientes lo usan (tasa de uso >50%), lo iteras en el próximo trimestre sin necesidad de reescribir.

---

## 4. Métricas para medir el ÉXITO DEL TRIMESTRE
(No te midas por "lo que construiste" — te midas por **lo que generó valor**):
1. Tasa de drop en paso 2 de alta: <30%
2. Tiempo de soporte diario: <1.5h (ideal: 1h)
3. Número de usuarios activados: +75% (gracias a B)
4. (Si lanzas MVP de C) Tasa de uso del panel por clientes top: >50%

---

### Clave final para fundador solo:
> Tu capacidad es finita. No busques "construir el futuro" — busca **multiplicar el valor de lo que ya tienes** y **liberar tiempo para construir lo que importe después**. Este trimestre te va a dar más usuarios, menos soporte y más capacidad para el próximo — y eso es mucho más valioso que un framework reescrito a medias.