# Tencent Hy3 — business_audit/teardown_competidor_sin_inventar

- model_id: `tencent/hy3`
- success: True  | final: 3.14 | quality: 2.0
- latency_total: 51.851s | tokens_per_second: 71.0
- input_tokens: 222 | output_tokens: 3683

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

Como analista competitivo, presento este *teardown* separando estrictamente tus observaciones (lo que **SÉ**) de mis proyecciones basadas en benchmarks de la industria (lo que **INFERO**), marcando en todo momento mi nivel de certeza.

---

### 1. Estimación de Facturación (Cuánto factura)

*   **SÉ:** Tienen 2.400 miembros visibles en la portada y un precio público de $39/mes. No se observan planes anuales ni descuentos en la superficie.
*   **INFERO:** Si asumimos que esos 2.400 son suscriptores activos pagando estrictamente el precio estándar mensual, su Ingreso Recurrente Mensual (MRR) bruto es de **$93.600/mes** (lo que equivale a ~$1.12M USD anuales).
*   **CERTEZA: BAJA.** El contador de "miembros" en la portada de estas plataformas suele ser una cifra acumulada o de "vanidad" (incluye miembros que cancelaron, cuentas de prueba gratuitas, o accesos de por vida). Además, al no verse planes anuales, es altamente probable que existan descuentos ocultos que bajen el ARPU (Ingreso Promedio por Usuario) real. La cifra real podría estar entre $60k y $90k/mes.

### 2. Salud del Negocio (Qué tan sano es)

*   **SÉ:** El fundador tiene 60.000 seguidores en su red social. Publican 3 posts por semana en el feed público. Tienen 12 cursos listados (sin saber cuántos están terminados).
*   **INFERO (Tracción Externa):** Si los 2.400 miembros provienen mayoritariamente de esa audiencia de 60.000, la tasa de conversión es del **4%** (2.400 / 60.000). En el ecosistema de comunidades de pago e info-productos, una conversión del 1% al 3% es lo estándar; un 4% indica que el fundador tiene una audiencia muy calificada y un *product-market fit* inicial fuerte.
*   **INFERO (Riesgos Internos):** Los 12 cursos listados son una espada de doble filo. Si están inconclusos (algo muy común para inflar catálogos), generarán frustración y *churn* (cancelaciones). Si están completos, representan una alta barrera de entrada por el volumen de activos creados.
*   **CERTEZA: MEDIA** sobre la tracción externa (el embudo de audiencia a pago es sólido sobre el papel). **BAJA** sobre la salud operativa real (no tenemos visibilidad del *Churn Rate* mensual, el engagement en el feed privado, ni los márgenes de ganancia después de costos de plataforma).

### 3. Estrategia Competitiva (Cómo les compito)

*   **SÉ:** Operan en el nicho de automatización, bajo un modelo de membresía con un precio accesible de entrada ($39/mes).
*   **INFERO:** Para penetrar en su mercado o quitarles cuota, puedes atacar los siguientes flancos basándote en las lagunas de su perfil público:
    *   **Flanco de Calidad de Contenido:** Si los 12 cursos están a medio hacer (algo común en plataformas que inflan catálogos), tu ventaja competitiva inmediata es ofrecer un *Core Curriculum* reducido (ej. 3-4 cursos) 100% terminados, pulidos y aplicables.
    *   **Flanco de Modelo de Precios/Escala:** A $39/mes, es un modelo de volumen (low-touch). Podrías competir con un modelo *Freemium* (comunidad gratuita para captar y educar) o crear un Tier Premium ($99-$199/mes) con revisiones de automatizaciones 1-on-1 o soporte directo que ellos no pueden dar a ese precio base.
    *   **Flanco de Nicho Profundo:** "Automatización" es un término amplio. Infiero que si te especializas en un *stack* concreto (ej. Make + N8N para agencias, o Zapier para e-commerce), evitas la guerra de precios frontal y compites por relevancia.
*   **CERTEZA: MEDIA.** Las estrategias son lógicas basadas en los huecos de información visible, pero requieren validación contra tu propio contexto (tu tamaño de audiencia, tu capital semilla y tu capacidad de producción de contenido).