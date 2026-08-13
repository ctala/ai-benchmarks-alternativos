# Claude Opus 5 Fast — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.64 | quality: 9.32
- latency_total: 11.748s | tokens_per_second: 174.3
- input_tokens: 388 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales.

**user:**

Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico.


## Respuesta completa

# Módulo 3
# Automatización con IA: De la idea al flujo de trabajo

> **Duración estimada:** 4 horas (2h teoría + 2h práctica)
> **Nivel:** Emprendedor no-técnico
> **Prerrequisitos:** Módulos 1 (Fundamentos de IA generativa) y 2 (Prompting efectivo)

---

## 1. Objetivo del módulo

Al finalizar este módulo, serás capaz de identificar tareas repetitivas dentro de tu emprendimiento, traducirlas a un **flujo de trabajo automatizado** (workflow) y construir tu primera automatización funcional con IA usando herramientas **no-code/low-code** como N8N, sin escribir una sola línea de código. El foco no es volverte programador, sino desarrollar el **criterio de automatización**: saber *qué* conviene automatizar, *cuándo* hacerlo y *cómo* medir si esa automatización realmente te devuelve horas y dinero. Terminarás el módulo con al menos un flujo activo corriendo en tu negocio.

---

## 2. Contenido teórico

### 2.1 ¿Qué es realmente "automatizar con IA"?

Antes de la IA generativa, automatizar significaba conectar sistemas con **reglas fijas**:

> "Cuando llegue un formulario → guardá los datos en una planilla → mandá un email de bienvenida."

Eso funciona, pero es **rígido**: no entiende contexto, no interpreta lenguaje natural, no toma decisiones matizadas.

La automatización **con IA** agrega una capa de *criterio* al flujo:

> "Cuando llegue un formulario → **leé el mensaje del cliente y clasificá su intención** → si es queja urgente avisá al fundador por WhatsApp, si es consulta comercial **redactá una respuesta personalizada** y agendá seguimiento."

**La diferencia clave:** pasás de automatizar *tareas mecánicas* a automatizar *tareas que antes requerían juicio humano básico*.

---

### 2.2 Los 4 componentes de todo flujo automatizado

Todo workflow, sin importar la herramienta, tiene esta anatomía. Memorizala, es tu esqueleto mental:

| Componente | Qué hace | Ejemplos |
|---|---|---|
| **1. Disparador (Trigger)** | El evento que inicia todo | Llega un email, alguien llena un formulario, son las 9 AM, entra un mensaje de WhatsApp |
| **2. Datos de entrada** | La información que se captura | Nombre, mensaje, monto, producto de interés |
| **3. Procesamiento / IA** | Donde ocurre la magia: clasificar, redactar, resumir, decidir | "Clasificá este mensaje como: Ventas / Soporte / Spam" |
| **4. Acción de salida** | El resultado concreto | Enviar respuesta, crear fila en Sheets, notificar a Slack, crear tarea en Notion |

> **Regla del módulo:** si no podés escribir tu proceso en estos 4 pasos en una servilleta, todavía no estás listo para automatizarlo.

---

### 2.3 El criterio: ¿qué conviene automatizar?

No todo merece automatizarse. Usá esta matriz rápida:

```
                  ALTA FRECUENCIA
                        │
   AUTOMATIZAR YA       │      AUTOMATIZAR
   (quick wins)         │      (proyecto grande)
                        │
BAJA ────────────────────┼──────────────────── ALTA
COMPLEJIDAD              │              COMPLEJIDAD
                        │
   IGNORAR              │      DELEGAR A HUMANO
   (no vale la pena)    │      (o rediseñar el proceso)
                        │
                  BAJA FRECUENCIA
```

**Fórmula del ROI de automatización:**

```
Horas ahorradas al mes × Valor de tu hora  >  Costo de herramientas + Horas de construcción/mes
```

**Ejemplo real:** Respondés 40 consultas repetidas por semana × 4 min = 2,6 h/semana ≈ **10,4 h/mes**.
Si tu hora vale USD 25 → estás perdiendo **USD 260/mes**. Una automatización que cuesta USD 20/mes y 6 horas de armado se paga en **menos de 3 semanas**.

---

### 2.4 El panorama de herramientas

| Herramienta | Tipo | Curva de aprendizaje | Costo aprox. | Ideal para |
|---|---|---|---|---|
| **N8N** | Open source, self-host o cloud | Media | Gratis (self-host) / desde USD 20 | Startups que quieren control y bajo costo a escala |
| **Make (ex Integromat)** | Cloud, visual | Baja-media | Free tier / desde USD 9 | Flujos visuales complejos, principiantes |
| **Zapier** | Cloud, lineal | Muy baja | Free tier / desde USD 20 | Máxima cantidad de integraciones, cero fricción |
| **Google Apps Script** | Código | Alta | Gratis | Todo dentro del ecosistema Google |
| **ChatGPT / Claude (Projects)** | Asistente | Muy baja | USD 20 | Automatización "manual asistida" |

---

### 2.5 ¿Por qué N8N para emprendedores LatAm?

**N8N** (se p