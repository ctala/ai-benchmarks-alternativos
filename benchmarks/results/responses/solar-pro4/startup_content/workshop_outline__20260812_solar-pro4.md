# Solar Pro 4 — startup_content/workshop_outline

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.54 | quality: 9.56
- latency_total: 71.96s | tokens_per_second: 28.5
- input_tokens: 252 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el taller.

## Respuesta completa

Aquí tienes el outline completo, diseñado para que salga volando desde el minuto 1. **Tono: directo, "manos a la obra", sin teoría de relleno.** Todo está pensado para funcionar en un espacio con proyector, mesa central y 20-30 emprendedores early-stage que no saben programar.

---

## 🕒 1. AGENDA DETALLADA (180 min)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00–0:10 | Bienvenida + energía inicial | 10 min |
| 0:10–0:40 | Bloque 1: IA sin código, qué puede (y qué NO debe) hacer tu asistente | 30 min |
| 0:40–1:10 | Bloque 2: Arquitectura simple + casos de uso reales | 30 min |
| 1:10–1:35 | **Ejercicio principal** (construcción guiada paso a paso) | 25 min |
| 1:35–1:55 | Prueba, ajustes y "lo que rompe en la práctica" | 20 min |
| 1:55–2:15 | Lanzamiento suave, métricas básicas y seguridad/ética | 20 min |
| 2:15–2:45 | Pitching relámpago + feedback cruzado | 30 min |
| 2:45–3:00 | Cierre, recursos, commits y networking | 15 min |

*(Total: 180 min. Los descansos se absorven en transiciones; si el grupo necesita estirar, robar 5 min de los bloques 4 y 6 sin romper el flujo.)*

---

## 📦 2. MATERIALES NECESARIOS (preparar antes)

**Para el facilitador:**
- Presentación en projector (ver conteo de slides abajo)
- Cuenta gratuita/configurada en una plataforma no-code de IA (ej: Botpress, Voiceflow, Dify, o similar). Tener un template base pre-cargado.
- 2-3 "prompts de sistema" de ejemplo en papel/digital para repartir.
- Listas de verificación impresas o en QR (ver recursos).
- Altavoz pequeño si el espacio es grande.
- Pizarra o flipchart + post-its para mapeo rápido.

**Para cada participante:**
- Laptop o tablet con conexión a internet (obligatorio para el ejercicio).
- Cuenta de correo activa (para registrarse en la plataforma elegida).
- Notas o hoja en blanco + bolígrafo.
- Acceso a la startup/idea que están validando (nombre, problema que resuelven, tono de comunicación, 3 preguntas frecuentes).

**Logística previa:**
- Enviar 48h antes: link de registro en plataforma, requisitos de navegador, y un mini-prework (5 min: escribir en 1 línea el problema que resuelve su startup y 3 preguntas que les responde su cliente hoy).
- Confirmar que el WiFi soporte 25-30 dispositivos simultáneos. Tener un router backup o hotspot si es posible.

---

## 🧱 3. BLOQUES DETALLADOS

### Bloque 1: IA sin código, qué puede (y qué NO debe) hacer tu asistente
- **Duración:** 30 min
- **Objetivo:** Quitar miedo técnico, alinear expectativas y mostrar valor real para early-stage.
- **Dinámica:** 
  - Charla rápida (10 min) con ejemplos latinos (ej: asistente que agenda reuniones, filtra leads, responde FAQ, resume comentarios de usuarios).
  - "Mito vs Realidad" en pizarra: 3 mitos comunes (IA reemplaza todo, necesito ingeniero, cuesta caro) vs lo que hoy se hace con no-code.
  - Pregunta rápida al grupo: "¿Qué tarea repetitiva de tu startup te quitaría una noche?" (levantar manos / post-its).
- **Key takeaway:** Hoy puedes armar un asistente útil sin escribir código. Empieza con un problema estrecho, no con "tubería de IA".

### Bloque 2: Arquitectura simple + casos de uso reales
- **Duración:** 30 min
- **Objetivo:** Dar un mapa mental claro: inputs → lógica → outputs → integración ligera.
- **Dinámica:**
  - Demo en vivo (10 min) de un flujo básico: el usuario escribe → el asistente clasifica → responde con plantilla + contexto → guarda resumen en hoja/CRM simple.
  - Ejercicio de 5 min en parejas: elegir 1 caso de uso y dibujar 3 pasos en un post-it (entrada, decisión, salida).
  - Discusión abierta (5 min): límites, cuándo NO usar IA (decisiones legales, críticas, datos sensibles).
- **Key takeaway:** Un buen asistente de startup hace 1 cosa bien, tiene contexto claro y sabe cuándo derivar a un humano.

### Bloque 3: EJERCICIO PRINCIPAL (construcción guiada)
- **Duración:** 25 min
- **Objetivo:** Que cada persona/s pareja tenga un asistente funcional (aunque sea básico) al salir del bloque.
- **Dinámica:** 
  - Seguimiento paso a paso con pantalla compartida (ver detalle del ejercicio abajo).
  - Cada participante construye su propio flujo; el facilitador va validando, respondiendo dudas y mostrando "trucos" de prompt.
  - Se anima a trabajar en parejas si alguien llega sin laptop o con conexión inestable.
- **Key takeaway:** Salir con un prototipo vivo que pueden mostrar hoy a un usuario real.

### Bloque 4: Prueba, ajustes y "lo que rompe en la práctica"
- **Duración:** 20 min
- **Objetivo:** Validar el prototipo rápido y aprender a depurarlo sin perder la noche.
- **Dinámica:**
  - Prueba entre pares (8 min): 3 intents distintos (pregunta válida, pregunta confusa, intento de "romper" el asistente).
  - Ajuste de prompts/contexto (7 min) usando una checklist simple.
  - Charla rápida (5 min): alucinaciones, formato de respuesta, límites de contexto, costos básicos, qué monitorear.
- **Key takeaway:** La primera versión nunca es perfecta; lo importante es medir, iterar y cerrar bucles de feedback.

### Bloque 5: Lanzamiento suave, métricas básicas y seguridad/ética
- **Duración:** 20 min
- **Objetivo:** Dar criterios para ponerlo en manos de usuarios sin exponer la startup.
- **Dinámica:**
  - Charla + diálogo (12 min): dónde lo publicas primero (WhatsApp, landing simple, embed, grupo cerrado), qué métricas son útiles hoy (tasa de respuesta útil, % de derivación a humano, tiempo ahorrado), y reglas de seguridad (no guardar datos sensibles sin necesidad, aviso de que es IA, política de uso).
  - Preguntas rápidas del grupo (8 min).
- **Key takeaway:** Lanza con límites claros, mide uso real, y protege datos y reputación desde el día 1.

### Bloque 6: Pitching relámpago + feedback cruzado
- **Duración:** 30 min
- **Objetivo:** Visibilizar lo construido, generar feedback útil y crear accountability.
- **Dinámica:**
  - Formatos de 2 min por pareja/grupo: (1) problema, (2) qué hace el asistente, (3) una métrica que quieren mejorar.
  - Feedback estructurado con post-its o formulario rápido: "1 cosa que sí", "1 sugerencia", "1 pregunta".
  - Facilitador sintetiza patrones en pizarra (5 min).
- **Key takeaway:** Recibir 2-3 ideas concretas para la próxima iteración y compromisos de prueba con usuarios reales.

### Cierre
- **Duración:** 15 min
- **Objetivo:** Cerrar con energía, recursos claros y próximos pasos.
- **Dinámica:** 
  - Recapitulación de 3 puntos clave (3 min).
  - Compromiso público rápido: "Esta semana, le muestro el asistente a ___ y mido ___" (5 min).
  - Entrega de recursos (digitales/QR) y espacio de networking informal (