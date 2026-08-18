# Gemini 3.7 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 3.16 | quality: 2.0
- latency_total: 16.038s | tokens_per_second: 127.4
- input_tokens: 177 | output_tokens: 2044

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

Aquí tienes el teardown analítico de tu competidor, separando con rigor los datos duros de las deducciones y proyecciones.

---

### 1. Datos Verificados vs. Inferencias

| Tipo | Elemento | Nivel de Certeza |
| :--- | :--- | :--- |
| **Hecho** | Precio facial: $39 USD/mes. | 100% |
| **Hecho** | Número visible en landing: 2.400 miembros. | 100% (el dato visual existe) |
| **Hecho** | Audiencia del fundador: 60.000 seguidores en una red social. | 100% |
| **Hecho** | Actividad pública: 3 posts/semana. | 100% |
| **Hecho** | Catálogo: 12 cursos listados. | 100% |
| **Inferencia** | Los 2.400 miembros **no** son todos suscriptores de pago activos. | **Certeza: Alta**. En la mayoría de plataformas (Skool, Circle, Whop), los contadores muestran usuarios acumulados históricos, cuentas gratuitas o miembros inactivos/churned a menos que se aclare explícitamente. |
| **Inferencia** | El principal canal de adquisición es la marca personal del fundador. | **Certeza: Alta**. Ratio típico en comunidades de creadores (60k seguidores $\rightarrow$ embudo directo a membresía). |
| **Inferencia** | Tasa de churn mensual estimada entre el 8% y el 15%. | **Certeza: Media**. Común en membresías B2C/prosumer de bajo ticket ($39) enfocadas en contenido. |

---

### 2. Estimación de Facturación (MRR / ARR)

Dado que no sabemos si los 2.400 son activos y pagando, se modelan 3 escenarios:

#### Escenario A: Techo Teórico / Vanilla (Certeza: BAJA)
*Asume que los 2.400 pagan la tarifa completa actualmente.*
* **MRR:** $93.600 USD/mes
* **ARR:** ~$1.12M USD/año
* *Nota analítica:* Muy improbable. Requeriría una tasa de conversión del 4% directo de toda su base de seguidores (60k) y churn cero.

#### Escenario B: Base Activa Realista (Certeza: MEDIA)
*Asume que los 2.400 son miembros históricos/mixtos, y la base activa real es del 25% al 40% (600 - 960 miembros de pago).*
* **MRR:** **$23.400 – $37.440 USD/mes**
* **ARR:** **$280.000 – $450.000 USD/año**
* *Nota analítica:* Cuadra con una conversión del 1% al 1.6% de su audiencia total de 60k.

#### Escenario C: Fase de Retención Crítica (Certeza: MEDIA-BAJA)
*Comunidad con alto churn donde solo el 10-15% sigue activo (240 - 360 miembros).*
* **MRR:** **$9.360 – $14.040 USD/mes**
* **ARR:** **$112.000 – $168.000 USD/año**

---

### 3. Diagnóstico de Salud del Negocio

* **Motor de Adquisición (Fuerte | Certeza: Alta):** Con 60k seguidores y posting regular (3 posts/semana), su CAC (coste de adquisición) orgánico es cercano a cero. Tienen tracción inicial garantizada.
* **Riesgo de Churn por Contenido (Alto | Certeza: Media):** Cobrar $39/mes por "12 cursos" suele provocar el efecto *Netflix*: los usuarios entran, consumen el curso que necesitan en 30 días y cancelan. Si no tienen soporte en vivo, bolsa de trabajo o herramientas propietarias, sufren retención a