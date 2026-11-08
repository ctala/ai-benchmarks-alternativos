# Mistral Small 4 — agent_capabilities/agent_team_delegation

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 7.712s | tokens_per_second: 174.9
- input_tokens: 982 | output_tokens: 1349
- judge_score: 5.0 | justificación: 

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

Entendido. Voy a descomponer esta tarea compleja en sub-tareas lógicas y asignarlas a los agentes especializados correspondientes. Aquí está el plan de ejecución:

---

### **Plan de Ejecución para la Landing Page de "AutoFlow AI"**

#### **Fase 1: Investigación (Prioridad: High)**
1. **Investigar a la competencia**:
   - Identificar 3 competidores directos de "AutoFlow AI" en el mercado de automatización para startups.
   - Analizar sus:
     - Propuestas de valor (value propositions).
     - Estructura de pricing.
     - Features principales.
     - Estrategias de CTA (llamados a la acción).
   - **Agente asignado**: `researcher`.
   - **Dependencia**: Ninguna. Puede iniciarse inmediatamente.

#### **Fase 2: Creación de Contenido (Prioridad: High)**
2. **Redactar el copy de la landing page**:
   - **Hero Section**: Título, subtítulo, y CTA principal.
   - **Features**: Lista de beneficios clave (mínimo 5 features destacadas).
   - **Pricing**: Planes de precios (ej: Free, Pro, Enterprise).
   - **CTA Final**: Mensaje persuasivo y botón de acción.
   - **Agente asignado**: `writer`.
   - **Dependencia**: El researcher debe proporcionar los datos de la competencia primero.

3. **Generar el código HTML/CSS**:
   - Estructura responsive (mobile-first).
   - Diseño moderno y profesional.
   - Incluir:
     - Hero section con animaciones suaves.
     - Sección de features con iconos.
     - Sección de pricing con tablas comparativas.
     - Footer con enlaces relevantes.
   - **Agente asignado**: `coder`.
   - **Dependencia**: El writer debe terminar el copy primero.

#### **Fase 3: Diseño Visual (Prioridad: Medium)**
4. **Crear assets visuales**:
   - **Imagen hero**: Ilustración o mockup de "AutoFlow AI" en acción.
   - **Imágenes de features**: Iconos o ilustraciones para cada feature destacada.
   - **Estilo**: Paleta de colores profesional (ej: azul corporativo + naranja para CTA).
   - **Agente asignado**: `designer`.
   - **Dependencia**: El writer debe definir los mensajes clave y el coder puede sugerir estructura.

#### **Fase 4: Revisión y Calidad (Prioridad: High)**
5. **Revisar todo el contenido**:
   - Coherencia del copy con la propuesta de valor.
   - Errores gramaticales o de estilo.
   - Calidad del código (HTML/CSS válido y responsive).
   - Diseño visual (alineación, colores, legibilidad).
   - **Agente asignado**: `reviewer`.
   - **Dependencia**: Todas las tareas anteriores deben estar completadas.

---

### **Secuencia de Ejecución**
1. **Fase 1**: El researcher inicia la investigación de la competencia.
2. **Fase 2**: Mientras el researcher trabaja, el writer puede preparar un borrador del copy basado en la propuesta inicial de AutoFlow AI (sin depender de la competencia).
3. **Fase 3**: El coder y el designer pueden empezar a bocetar estructuras y estilos en paralelo, pero el código final y los assets dependerán del copy y la investigación.
4. **Fase 4**: Una vez que todas las piezas estén listas, el reviewer valida todo antes de la publicación.

---

### **Asignación Inicial**
Voy a delegar las tareas iniciales ahora. El researcher y el writer pueden empezar en paralelo, pero el coder y el designer esperaran a que el copy y la investigación estén listos.