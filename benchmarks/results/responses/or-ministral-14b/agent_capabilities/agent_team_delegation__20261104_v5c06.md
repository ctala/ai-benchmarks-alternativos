# Ministral 14B — agent_capabilities/agent_team_delegation

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.56 | quality: 9.72
- latency_total: 57.944s | tokens_per_second: 17.4
- input_tokens: 970 | output_tokens: 1008
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el agente coordinador de un Agent Team. Tienes 5 sub-agentes:
- researcher: busca informacion y datos
- writer: redacta contenido
- coder: genera codigo y automatizaciones
- reviewer: revisa calidad y errores
- designer: crea assets visuales

Reglas:
- Descompone tareas complejas en sub-tareas para cada agente
- Respeta dependencias (el writer necesita los datos del researcher primero)
- Asigna prioridades correctamente
- Explica el plan de ejecucion antes de delegar

**user:**

Necesito crear una landing page para el lanzamiento de nuestro nuevo producto "AutoFlow AI" (herramienta de automatizacion para startups). Incluye:
1. Investigar que hace la competencia (3 competidores)
2. Escribir el copy de la landing (hero, features, pricing, CTA)
3. Generar el codigo HTML/CSS de la pagina
4. Crear las imagenes hero y de features
5. Revisar todo antes de publicar

Coordinalo todo.


## Respuesta completa

Entendido. Vamos a descomponer el proyecto en un plan de ejecución claro y organizado, respetando las dependencias entre las tareas. Aquí está el flujo de trabajo:

---

### **Plan de Ejecución**
**Objetivo:** Crear una landing page profesional para el lanzamiento de *AutoFlow AI*.

#### **Fase 1: Investigación (Dependencia para el copy y diseño)**
- **Tarea:** Investigar qué ofrece la competencia (3 competidores) para identificar diferenciadores clave.
- **Agente responsable:** `researcher`.
- **Prioridad:** Alta.
- **Resultado esperado:** Un informe con:
  - Características principales de cada competidor.
  - Puntos débiles y oportunidades para destacar *AutoFlow AI*.
  - Palabras clave y tono de comunicación usado por la competencia.

---

#### **Fase 2: Redacción del Copy (Dependencia de la investigación)**
- **Tarea:** Escribir el contenido de la landing page basado en los hallazgos de la competencia.
  - Secciones:
    1. **Hero** (título, subtítulo y CTA principal).
    2. **Features** (beneficios clave de *AutoFlow AI*).
    3. **Pricing** (plan de precios, destacando valor).
    4. **CTA final** (llamado a la acción para registrar interés o comprar).
- **Agente responsable:** `writer`.
- **Prioridad:** Alta.
- **Contexto para el writer:** Usar los diferenciadores identificados por el `researcher` para posicionar *AutoFlow AI* como la mejor opción.

---

#### **Fase 3: Diseño Visual (Dependencia del copy)**
- **Tarea:** Crear los assets visuales necesarios para la landing page:
  1. **Imagen hero:** Diseño atractivo que muestre el producto en acción (ej: interfaz o beneficio clave).
  2. **Imágenes de features:** Ilustraciones o mockups que respalden cada beneficio mencionado en el copy.
- **Agente responsable:** `designer`.
- **Prioridad:** Alta.
- **Contexto para el designer:** Usar el tono y estilo visual de la marca de *AutoFlow AI* (si existe una guía de diseño, adjuntarla).

---

#### **Fase 4: Desarrollo del Código (Dependencia del copy y diseño)**
- **Tarea:** Generar el código HTML/CSS para la landing page, integrando:
  - El copy escrito por el `writer`.
  - Los assets visuales creados por el `designer`.
  - Estructura responsive y optimizada para conversiones.
- **Agente responsable:** `coder`.
- **Prioridad:** Alta.
- **Contexto para el coder:** Asegurar que el diseño sea consistente con el copy y que la página sea funcional en dispositivos móviles.

---

#### **Fase 5: Revisión de Calidad (Dependencia de todas las fases anteriores)**
- **Tarea:** Revisar:
  1. **Copy:** Coherencia, claridad y persuasión.
  2. **Diseño:** Calidad visual, alineación con la marca y usabilidad.
  3. **Código:** Funcionalidad, responsividad y optimización.
  4. **Mensaje general:** Diferenciación frente a la competencia y valor para el usuario.
- **Agente responsable:** `reviewer`.
- **Prioridad:** Alta.
- **Resultado esperado:** Lista de ajustes o aprobación final para publicación.

---

#### **Fase 6: Publicación (Posterior a la revisión)**
- **Nota:** Esta fase no está automatizada en este flujo, pero el resultado final será un paquete listo para desplegarse en un sistema como Webflow, WordPress o directamente en un servidor.

---

### **Orden de Ejecución**
1. **Investigación** (`researcher`).
2. **Redacción del copy** (`writer`).
3. **Diseño visual** (`designer`).
4. **Desarrollo del código** (`coder`).
5. **Revisión final** (`reviewer`).

---
### **Delegación de Tareas**
Voy a asignar las tareas según el plan. Comenzamos con la investigación, que es la base de todo el proyecto.