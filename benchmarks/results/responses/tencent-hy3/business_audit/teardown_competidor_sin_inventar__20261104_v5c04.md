# Tencent Hy3 — business_audit/teardown_competidor_sin_inventar

- model_id: `tencent/hy3`
- success: True  | final: 3.16 | quality: 2.0
- latency_total: 55.371s | tokens_per_second: 59.8
- input_tokens: 222 | output_tokens: 3313

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

Como analista competitivo, voy a desglosar esto rigurosamente. Para cada punto, etiquetaré claramente lo que es un **[HECHO]** (dato que me proporcionaste) y lo que es una **[INFERENCIA]** (mi deducción lógica basada en el hecho), acompañado de su nivel de certeza (ALTA, MEDIA, BAJA).

---

### 1. Estimación de Facturación (¿Cuánto factura?)

* **[HECHO]** Muestran "2.400 miembros" en la portada.
* **[HECHO]** El precio visible es $39/mes.
* **[INFERENCIA - CERTEZA: MEDIA]** Si asumimos que esos 2.400 son suscriptores activos y pagantes al precio estándar (sin contar planes anuales prepagados que inflarían el MRR real, ni descuentos que lo bajarían), la facturación mensual recurrente (MRR) es de **$93.600/mes** (2.400 x $39). Anualizado, ronda el **$1.12M USD**.
* **[INFERENCIA - CERTEZA: BAJA]** Es muy probable que la cifra real sea menor. Muchas plataformas de membresía muestran el "total de miembros acumulados" (incluyendo a los que cancelaron hace meses pero siguen en la base de datos, o cuentas de fundadores/moderadores). Si solo el 70% son pagantes activos reales, el MRR bajaría a ~$65.5k.

### 2. Salud del Negocio (¿Qué tan sano es?)

* **[HECHO]** El fundador tiene 60.000 seguidores en una red social.
* **[HECHO]** Publican 3 posts por semana en el feed público.
* **[HECHO]** Tienen 12 cursos listados, no se ve cuántos están terminados.
* **[INFERENCIA - CERTEZA: MEDIA]** **Tasa de Conversión:** 2.400 miembros / 60.000 seguidores = **4% de conversión**. En el ecosistema de comunidades de pago, un 1-3% es estándar; un 4% es bastante sano y sugiere que el fundador tiene buena autoridad o un embudo orgánico efectivo.
* **[INFERENCIA - CERTEZA: MEDIA]** **Modelo de Precio:** A $39/mes, es un modelo "low-ticket". Esto es positivo para la retención (el dolor de cancelar $39 es bajo, lo que reduce la fricción de entrada), pero exige un volumen alto de adquisición constante para crecer.
* **[INFERENCIA - CERTEZA: BAJA]** **Riesgo de Contenido:** Si de los 12 cursos listados varios están "en construcción" o incompletos, podría haber una tasa de churn (cancelación) oculta más alta de lo normal por falta de valor entregado. Sin embargo, al publicar 3 posts/semana, mantienen la atención viva (engagement constante), lo que amortigua ese riesgo de abandono.

### 3. Cómo Competirles (Estrategia)

* **[INFERENCIA - CERTEZA: ALTA]** **Diferenciación por Nicho:** Ellos compiten en "automatización" (término amplio). Para ganar, no intentes superar su volumen de 12 cursos. Enfócate en una vertical específica (ej. "Automatización para e-commerce de Shopify" o "Automatización con IA para consultores").
* **[INFERENCIA - CERTEZA: MEDIA]** **Ataque a la "Completitud":** Si sospechas (por el hecho de no verlos terminados) que sus cursos son una vitrina a medias, tu ventaja competitiva es prometer y entregar un "Curso 100% grabado y aplicable desde el día 1", contrastando con el modelo de "acceso a lo que vaya saliendo".
* **[INFERENCIA - CERTEZA: MEDIA]** **Canales de Adquisición:** Su motor parece ser el fundador (60k seguidores). Si tú no tienes esa audiencia, compite en canales donde ellos probablemente no estén dominando: SEO (contenido escrito de alta intención de búsqueda), partnerships B2B, o tráfico pagado a webinars.
* **[INFERENCIA - CERTEZA: BAJA]** **Modelo de Precio:** Si entras a $39 también, serás un "me-too". Podrías probar un precio anual único (ej. $290/año) para capturar el valor total de front-end y darte más capital de trabajo que ellos, asumiendo que ellos viven de MRR puro mensual.

---
**Resumen del Analista:**
El competidor tiene una base sólida (MRR ~$90k inferido, conversión del 4% desde su audiencia). El negocio parece sano y depende fuertemente del carisma/audiencia del fundador. Para competir, evita la guerra de volumen de cursos y ataca con nicho específico, contenido terminado y canales de adquisición alternativos a las redes sociales del fundador.