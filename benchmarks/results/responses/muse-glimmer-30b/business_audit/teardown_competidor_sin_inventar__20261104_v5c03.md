# Muse Glimmer 30B — business_audit/teardown_competidor_sin_inventar

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 6.02 | quality: 6.0
- latency_total: 14.165s | tokens_per_second: 134.6
- input_tokens: 192 | output_tokens: 1906

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

Teardown con lo que realmente puedes ver. Separado en **Hecho observado** vs **Inferencias** con nivel de certeza.

### 1. Lo que sabes con certeza ALTA

* Comunidad de pago sobre automatización en plataforma tipo membresía.
* Muestra '2.400 miembros' en portada.
* Precio visible $39/mes. No hay evidencia visible de plan anual ni descuentos.
* Publican 3 posts/semana en feed público.
* Fundador tiene 60.000 seguidores en una red social.
* Tienen 12 cursos listados, estado de finalización no visible.

Eso es todo. El resto es inferencia.

### 2. Estimación de facturación

**Hecho:** 2.400 miembros mostrados x $39/mes.

**Inferencias necesarias:**
* ¿2.400 = miembros pagando activos hoy? Certeza BAJA. En membresías ese número suele ser vanity: incluye inactivos, free trial, invitados, o total histórico.
* ¿Precio $39 es el que realmente paga la mayoría? Certeza MEDIA-BAJA. No se ve plan anual, descuento por pago adelantado, o planes de nivel.

Escenarios de MRR con supuestos explícitos:

* **Optimista - Certeza BAJA:** 2.400 son pagando activos. 2.400 x $39 = **$93.600 MRR ≈ $1.12M ARR**
* **Realista - Certeza MEDIA:** 60-80% activos pagando. 1.440-1.920 x $39 = **$56.160 - $74.880 MRR ≈ $674k - $898k ARR**
* **Conservador - Certeza MEDIA:** 30-50% activos pagando. 720-1.200 x $39 = **$28.080 - $46.800 MRR ≈ $337k - $562k ARR**

Sin datos de churn, refund o % de miembros gratuitos, no se puede afirmar facturación real.

### 3. Salud del negocio - señales visibles y ciegas

**Señales positivas inferidas, Certeza MEDIA:**
* Tracción inicial: 2.400 miembros mostrados y fundador con 60k seguidores sugiere capacidad de adquisición orgánica.
* Cadencia de contenido: 3 posts/semana indica motor de contenido activo, necesario para retención en comunidad.

**Señales de riesgo inferidas, Certeza MEDIA-ALTA:**
* Dependencia de persona: 60k seguidores del fundador = canal de adquisición centralizado. Vulnerable a algoritmo y reputación.
* Oferta poco diferenciada: 12 cursos listados sin visibilidad de finalización. Certeza BAJA de calidad/terminación. Puede ser catálogo inflado.
* Precio único visible $39/mes sin anual. Certeza MEDIA de que no están optimizando LTV con anual ni reduciendo churn con compromiso.
* No hay métricas de salud públicas: no se ve tasa de participación, testimonios recientes, casos de uso, o churn. Certeza ALTA de que no puedes validar retención.

**Lo que no se puede evaluar y es crítico:**
Churn mensual, CAC, LTV, % de miembros activos vs inactivos, ratio de conversión seguidores -> pago, costo de plataforma, equipo, margen.

### 4. Cómo les compites

No compitas en precio $39/mes contra un número de miembros. Compite en los huecos que se ven desde fuera.

**1. Ataque a la retención y prueba social**
Ellos muestran cantidad, no calidad. Tú muestra calidad:
* Métricas vivas: miembros activos hoy, posts de miembros/día, proyectos completados.
* Caso de estudio por nicho de automatización en lugar de cursos genéricos.

**2. Modelo de precio y compromiso**
Si no tienen anual visible, es oportunidad.
* Oferta anual con descuento real + garantía de permanencia.
* Tier de entrada más bajo $19-29 para capturar seguidores del fundador que no pagan $39.

**3. Desintermedia al fundador**
Su adquisición parece dependiente de 60k seguidores. Tú construye:
* SEO de contenido sobre automatización específico por herramienta/uso.
* Partnerships con creadores pequeños en automatización.
* Canal de referido con incentivo económico.

**4. Productización del catálogo**
12 cursos sin estado visible = riesgo de percepción de "work in progress".
* Tú lanza con 3-4 cursos terminados y certificados, con roadmap público.
* Formato híbrido: comunidad + implementación guiada en vivo, no solo cursos grabados.

**5. Señales de salud que puedes comunicar desde día 1**
Ellos no muestran. Tú sí:
* Tasa de finalización de cursos, tiempo medio a primer win, NPS.
* Dashboard público de actividad de la comunidad.

### Qué necesitas verificar para afinar el teardown

* ¿Los 2.400 miembros son pagando activos o total de registro?
* % de conversión de seguidores del fundador a miembros.
* Churn a 3/6/12 meses y % de uso semanal.
* Cuántos de los 12 cursos están realmente completos y con estudiantes activos.
* Si existe plan anual y tasa de adopción.

Con eso puedes pasar de estimación a diagnóstico real de salud financiera.

¿Quieres que haga un modelo de escenario con churn asumido para estimar LTV y punto de equilibrio contra ellos?