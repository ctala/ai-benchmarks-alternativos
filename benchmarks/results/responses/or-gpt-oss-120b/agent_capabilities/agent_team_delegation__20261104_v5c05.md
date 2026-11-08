# GPT-OSS 120B — agent_capabilities/agent_team_delegation

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 18.302s | tokens_per_second: 45.3
- input_tokens: 683 | output_tokens: 830
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, proporcionando un plan detallado que un emprendedor podría usar directamente.

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

**Plan de ejecución**

1. **Investigación (researcher) – Prioridad alta**  
   - Objetivo: Analizar 3 competidores directos de herramientas de automatización para startups (por ejemplo, Zapier, Integromat/Make, y Tray.io).  
   - Necesitamos:  
     * Descripción breve del producto/servicio.  
     * Principales funcionalidades destacadas.  
     * Modelo de precios y estructura de planes.  
     * Mensajes de marketing (hero copy, CTA) que utilizan.  
   - Salida esperada: Un informe estructurado (máx. 1‑2 páginas) con los puntos anteriores y un breve “insight” de oportunidades para **AutoFlow AI**.

2. **Redacción del copy (writer) – Prioridad alta**  
   - Dependencia: Necesita el informe de investigación.  
   - Tareas:  
     * Crear el texto del **hero** (título, subtítulo, CTA).  
     * Definir 4‑5 **features** clave con descripciones breves.  
     * Proponer una sección de **pricing** (plan gratuito, pro, enterprise).  
     * Redactar un **CTA** final y micro‑copy (testimonios, FAQ).  
   - Salida esperada: Documento de copy en formato markdown.

3. **Diseño visual (designer) – Prioridad media**  
   - Dependencia: Necesita el copy (para alinear tono y estilo) y los insights de la competencia.  
   - Tareas:  
     * Crear la **imagen hero** (ilustración o mockup que muestre AutoFlow AI en acción).  
     * Crear **iconos/ilustraciones** para cada feature.  
     * Proveer assets en formatos web‑ready (SVG/PNG, 2 x).  
   - Salida esperada: URLs o archivos base64 de los assets.

4. **Desarrollo (coder) – Prioridad media**  
   - Dependencia: Necesita el copy final y los assets de diseño.  
   - Tareas:  
     * Generar HTML5 semántico y CSS (preferiblemente con Tailwind o CSS Grid).  
     * Incluir placeholders para imágenes entregadas por el designer.  
     * Asegurar responsividad (mobile‑first).  
   - Salida esperada: Archivo `index.html` y `styles.css` (o un solo HTML con CSS embebido).

5. **Revisión (reviewer) – Prioridad alta**  
   - Dependencia: Necesita el código final, el copy y los assets.  
   - Tareas:  
     * Verificar consistencia del mensaje, ortografía y gramática.  
     * Chequear que el HTML/CSS sea válido y accesible (WCAG 2.1 AA).  
     * Confirmar que los assets se cargan correctamente y están optimizados.  
   - Salida esperada: Informe de revisión con observaciones y aprobaciones.

6. **Publicación (opcional)**  
   - Si todo está aprobado, podemos ejecutar el skill `publish_blog_post` o simplemente entregar los archivos al equipo de DevOps.

---

### Delegación de tareas

#### 1️⃣ Investigación
