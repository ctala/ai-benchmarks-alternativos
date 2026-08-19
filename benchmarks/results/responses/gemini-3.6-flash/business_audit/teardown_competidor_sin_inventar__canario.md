# Gemini 3.6 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 3.1 | quality: 2.0
- latency_total: 9.866s | tokens_per_second: 207.2
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

Como analista competitivo, procedo a desglosar a este competidor. Para mantener la máxima rigurosidad, clasificaré la información en:
*   **[DATO DIRECTO]:** Lo que confirmaste en tu observación.
*   **[INFERENCIA - ALTA CERTEZA]:** Deducción lógica basada en dinámicas estándar de la industria de comunidades.
*   **[INFERENCIA - MEDIA CERTEZA]:** Estimación basada en métricas promedio de SaaS/Membresías.
*   **[HIPÓTESIS - BAJA CERTEZA]:** Escenario plausible pero que requiere más información para confirmarse.

---

### 1. Estimación de Facturación (MRR / ARR)

Para calcular cuánto facturan, no debemos caer en la trampa de multiplicar $39 \times 2.400$ a ciegas. En plataformas de membresía (Skool, Circle, Mighty Networks), el número de "miembros" suele incluir usuarios gratuitos, cuentas inactivas o registros históricos.

#### Escenarios de Facturación Mensual (MRR):

*   **Escenario Optimista [HIPÓTESIS - BAJA CERTEZA]:**
    *   *Premisa:* El 100% de los 2.400 miembros son de pago activo a $39/mes.
    *   **MRR:** **$93.600 USD/mes** (~$1,12M USD/año).
*   **Escenario Realista [INFERENCIA - MEDIA CERTEZA]:**
    *   *Premisa:* El contador muestra miembros históricos o incluye un *tier* gratuito/de prueba. Típicamente, solo entre el **30% y el 50%** son pagos activos en un momento dado.
    *   30% de 2.400 = 720 miembros activos $\times$ $39 = **$28.080 USD/mes** (~$337k USD/año).
    *   50% de 2.400 = 1.200 miembros activos $\times$ $39 = **$46.800 USD/mes** (~$561k USD/año).
*   **Escenario Conservador [INFERENCIA - MEDIA CERTEZA]:**
    *   *Premisa:* Tienen alta