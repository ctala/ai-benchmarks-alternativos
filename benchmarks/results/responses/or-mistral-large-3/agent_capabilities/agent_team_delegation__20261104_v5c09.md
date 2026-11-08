# Mistral Large 3 675B — agent_capabilities/agent_team_delegation

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.54 | quality: 9.8
- latency_total: 16.03s | tokens_per_second: 95.1
- input_tokens: 970 | output_tokens: 1524
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado que un emprendedor podría implementar directamente.

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

Voy a coordinar la creación de la landing page para **AutoFlow AI** descomponiendo la tarea en sub-tareas claras, asignando prioridades y respetando las dependencias entre los agentes. Aquí está el plan de ejecución:

---

### **Plan de Ejecución**
**Objetivo**: Crear una landing page completa para el lanzamiento de *AutoFlow AI*, incluyendo investigación, copy, código, assets visuales y revisión.

#### **Fase 1: Investigación (Prioridad: Urgent)**
- **Agente**: `researcher`
- **Tarea**: Investigar a **3 competidores directos** de *AutoFlow AI* (herramientas de automatización para startups).
  - Analizar:
    - Estructura de sus landing pages (secciones, copy, CTA).
    - Features destacadas y cómo las presentan.
    - Modelos de pricing (si son públicos).
    - Imágenes o assets visuales que utilizan.
  - Entregar un informe con:
    - URLs de los competidores analizados.
    - Resumen de hallazgos (qué funciona y qué no).
    - Recomendaciones para diferenciar *AutoFlow AI*.

---

#### **Fase 2: Redacción del Copy (Prioridad: High)**
- **Dependencia**: Resultados de la investigación (Fase 1).
- **Agente**: `writer`
- **Tarea**: Escribir el copy para las siguientes secciones de la landing page:
  1. **Hero Section**:
     - Headline principal (valor único de *AutoFlow AI*).
     - Subheadline (breve explicación del producto).
     - CTA principal (ej: "Empieza gratis", "Solicita una demo").
  2. **Features**:
     - 3-4 features clave con títulos, descripciones y beneficios.
  3. **Pricing**:
     - Descripción de los planes (ej: Básico, Pro, Enterprise).
     - Precios y límites (si aplica).
  4. **CTA final**:
     - Texto persuasivo para convertir visitantes.
  - **Contexto adicional**:
    - Tono: Profesional pero cercano (enfocado en startups).
    - Palabras clave para SEO: "automatización para startups", "herramienta de productividad", "flujo de trabajo automatizado".

---

#### **Fase 3: Creación de Assets Visuales (Prioridad: High)**
- **Dependencia**: Copy de la hero section y features (Fase 2).
- **Agente**: `designer`
- **Tarea**: Crear los siguientes assets:
  1. **Imagen Hero**:
     - Diseño atractivo que refleje el valor de *AutoFlow AI* (ej: ilustración de flujos de trabajo automatizados, robots, startups).
     - Incluir el headline y CTA del copy (opcional: mockup del producto).
  2. **Imágenes para Features**:
     - Iconos o ilustraciones para cada feature (ej: íconos de automatización, integraciones, ahorro de tiempo).
     - Estilo coherente con la imagen hero.
  3. **Otros assets** (si aplica):
     - Testimonios ficticios (o reales si los hay).
     - Gráficos de pricing.

---

#### **Fase 4: Desarrollo del Código (Prioridad: High)**
- **Dependencias**:
  - Copy de la landing (Fase 2).
  - Assets visuales (Fase 3).
- **Agente**: `coder`
- **Tarea**: Generar el código **HTML/CSS** de la landing page, incluyendo:
  1. Estructura responsive (mobile-first).
  2. Secciones:
     - Hero (con imagen y CTA).
     - Features (con imágenes/íconos).
     - Pricing (tabla o tarjetas).
     - CTA final.
  3. Estilo:
     - Paleta de colores: Usar los colores de la marca de *AutoFlow AI* (si no hay, proponer una).
     - Tipografía: Legible y moderna (ej: Inter, Roboto).
  4. Funcionalidad básica:
     - Botones de CTA funcionales (pueden ser enlaces a "#").
     - Formulario de contacto simple (opcional).
  5. Entregar:
     - Archivo `index.html`.
     - Archivo `styles.css`.
     - Carpeta `/assets` con imágenes optimizadas.

---

#### **Fase 5: Revisión Final (Prioridad: Urgent)**
- **Dependencias**:
  - Copy (Fase 2).
  - Assets visuales (Fase 3).
  - Código (Fase 4).
- **Agente**: `reviewer`
- **Tarea**: Revisar todo el material antes de publicar:
  1. **Copy**:
     - Ortografía y gramática.
     - Coherencia del mensaje (¿el valor de *AutoFlow AI* está claro?).
     - Llamados a la acción efectivos.
  2. **Diseño**:
     - Calidad de las imágenes (resolución, estilo coherente).
     - Legibilidad del texto en los assets.
  3. **Código**:
     - Validación HTML/CSS (sin errores).
     - Responsividad (probar en mobile y desktop).
     - Velocidad de carga (imágenes optimizadas).
  4. **Experiencia de usuario**:
     - Flujo lógico de la landing (¿el usuario sabe qué hacer en cada sección?).
     - Pruebas de usabilidad básicas (ej: clics en botones).
  - **Entregar**:
    - Informe con correcciones necesarias (si las hay).
    - Aprobación final para publicar.

---

#### **Fase 6: Ajustes y Entrega (Prioridad: Urgent)**
- **Dependencia**: Resultados de la revisión (Fase 5).
- **Acciones**:
  - Si hay correcciones, asignar tareas específicas a los agentes correspondientes (`writer`, `designer` o `coder`).
  - Una vez aprobado, empaquetar todo el material (código + assets) y entregarlo al equipo de lanzamiento.

---

### **Ejecución**
Voy a comenzar delegando las tareas según el plan. Empezaré con la **Fase 1 (Investigación)**.