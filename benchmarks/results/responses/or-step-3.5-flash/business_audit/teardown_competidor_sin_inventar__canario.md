# Step 3.5 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 4.76 | quality: 4.0
- latency_total: 30.048s | tokens_per_second: 68.2
- input_tokens: 206 | output_tokens: 2048

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

## **Teardown del Competidor (Análisis Basado en Datos Externos)**

**ADVERTENCIA CRÍTICA:** Todo lo siguiente es **INFERENCIA** basada en datos limitados de superficie. No tengo acceso a sus estados financieros, métricas internas (churn, CAC, LTV), estructura de costos, porcentaje de planes anuales, tasa de conversión de seguidores a clientes, ni desglose de cursos (completos vs. en curso). El nivel de certeza es **BAJO-MEDIO** para proyecciones financieras, **MEDIO** para evaluación de salud basada en proxies.

---

### **1. Estimación de Facturación (Ingresos)**

**Supuestos clave (marcados como inferencias):**
*   **Inferencia 1 (Alta probabilidad):** Los "2.400 miembros" mostrados son **miembros de pago activos**. Es el estándar de marketing en este modelo. *Certeza: 85%.*
*   **Inferencia 2 (Alta probabilidad):** El precio de **$39/mes** es el plan **mensual base**. Es común que exista un plan anual con descuento (ej: $390/año = ~$32.5/mes), pero no se ve. *Certeza: 75%.*
*   **Inferencia 3 (Incertidumbre alta):** **% de miembros en plan anual.** Si el 50% está en anual (descuento del ~17%), el MRR (Ingreso Mensual Recurrente) se reduce. Sin datos, asumiré un **mix 70% mensual / 30% anual** como escenario base para el cálculo.
*   **Inferencia 4 (Incertidumbre alta):** **Tasa de churn (abandono).** No se ve. Para un negocio de membresía en nicho especializado, un churn mensual del 3-5% es común si el valor es alto. Asumiré **4% mensual** para calcular un MRR "estable" (no el máximo teórico).

**Cálculo de MRR (Ingreso Mensual Recurrente) Estimado:**
*   Miembros totales: 2,400
*   Ajuste por mix de planes (asumiendo 70% mensual, 30% anual):
    *   Miembros mensuales: 2,400 * 70% = 1,680
    *   Miembros anuales (en MRR): 2,400 * 30% = 720 (cada uno cuenta como $32.5/mes en MRR)
*   MRR bruto (sin churn): (1,680 * $39) + (720 * $32.5) = $65,520 + $23,400 = **$88,920/mes**
*   **Ajuste por churn (4% mensual):** Un negocio en estado "estable" ya tiene en cuenta el churn en su base de miembros. Los 2,400 ya son los que se quedan. **Por lo tanto, el MRR ESTIMADO es ~$88,900/mes.**
*   **Facturación Anual (ARR):** $88,900 * 12 = **~$1,066,800/año.**

**Rango de Facturación Posible (por sensibilidad a supuestos):**
*   **Escenario Optimista (pocos anuales, churn bajo):** Todos pagan $39/mes. ARR = (2,400 * $39) * 12 = **$1,123,200.**
*   **Escenario Conservador (muchos anuales, churn alto):** Mix 50/50, con ARPU (Ingreso por Usuario) efectivo de ~$35. ARR = (2,400 * $35) * 12 = **$1,008,000.**
*   **Conclusión Facturación:** El rango realista está entre **$1M - $1.15M anuales.** La cifra de ~$1.07M es una estimación central sólida.

---

### **2. Evaluación de la Salud del Negocio (Señales Positivas y de Riesgo)**

**Señales de SALUD / FORTALEZA (Verificables/Inferidas):**
1.  **Validación de Mercado:** 2,400 miembros de pago en un nicho específico (automatización) es un **logro significativo**. Demuestra que hay demanda y que la propuesta de valor es creíble.
2.  **Precio Premium:** $39/mes (~$470/año) es un precio alto para una membresía genérica, pero apropiado para un nicho profesional (automatización = ROI claro para negocios). Sugiere **baja sensibilidad al precio** y clientes con poder adquisitivo (empresarios, freelancers senior).
3.  **Autoridad del Fundador:** 60,000 seguidores en una red social (probablemente LinkedIn/Twitter/X) es un **activo de adquisición enorme**. Si ese público es relevante, su CAC (Costo de Adquisición de Cliente) orgánico debe ser **muy bajo**.
4.  **Consistencia de Contenido:** 3 posts/semana en el feed público es un ritmo sostenido que mantiene engagement y atrae tráfico orgánico.
5.  **Producto "Sticky":** 12 cursos listados (asumo que es el núcleo) crean un **efecto de "biblioteca"**. Un miembro rara vez consume todo, lo que reduce el churn por "consumo completo".

**Señales de RIESGO / PREOCUPACIÓN (Inferidas):**
1.  **Churn Desconocido:** El mayor riesgo. Si el churn es >6% mensual, el negocio está en una **cinta de correr constante de adquisición** y es menos sostenible. Los 2,400 podrían ser el pico, no la base estable.
2.  **Dependencia del Fundador:** El 60%+ del marketing parece basarse en la audiencia personal del fundador. Esto es un **punto único de fallo**. Si el fundador reduce su actividad o cambia de plataforma, el flujo de nuevos clientes se resquebrajaría.
3.  **Falta de Diversificación de Producto:** Solo ven 12 cursos. ¿Hay comunidad activa? ¿Herramientas