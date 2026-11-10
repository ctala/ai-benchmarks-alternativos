# GPT-OSS 120B — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.67 | quality: 8.0
- latency_total: 20.623s | tokens_per_second: 97.2
- input_tokens: 231 | output_tokens: 2004

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Experimento “Mata‑hipótesis”  
**Hipótesis**: *“Las agencias de marketing pequeñas pagarían $200 / mes por una herramienta que les automatice los reportes a clientes.”*  

### 1. Principios del experimento  
| Principio | Qué significa para este caso |
|-----------|------------------------------|
| **Falla concluyente** | Necesitamos una métrica que, si no se alcanza, indique sin lugar a dudas que la hipótesis es falsa. |
| **Barato y rápido** | No desarrollaremos nada. Usaremos sólo pruebas de concepto (landing page, encuesta y pre‑venta). |
| **Mínimo “producto”** | Un mock‑up de 1‑2 pantallas con copy‑writing que explique la herramienta y el precio. |
| **Objetivo** | Medir **disposición a pagar** (WTP) real, no solo “interés”. |

---

## 2. Diseño del experimento (paso a paso)

| Paso | Acción concreta | Herramientas (costo) | Tiempo estimado |
|------|----------------|----------------------|-----------------|
| **0️⃣ Definir “agencia pequeña”** | <ul><li>Facturación ≤ $500 k/año.</li><li>1‑5 empleados.</li></ul> | - | 1 h |
| **1️⃣ Crear mock‑up** | <ul><li>2‑3 pantallas (dashboard de reportes, configuración de cliente).</li><li>Copy: “Automatiza los reportes mensuales a tus clientes en 1 click. Solo $200 / mes.”</li></ul> | **Figma** (plan gratis) → **0 $** | 3 h |
| **2️⃣ Landing page ultra‑simple** | <ul><li>URL corta (ej.: bit.ly/ReportAuto).</li><li>Encabezado, descripción, mock‑up, botón “Quiero la herramienta”.</li><li>Formulario de captura: nombre, email, nombre de la agencia, presupuesto mensual de herramientas de reporting.</li></ul> | **Carrd** (plan Pro $19/mes) o **WordPress** (dominio $12 + hosting $5) → **≈ $20** total. | 3 h |
| **3️⃣ Oferta de pre‑venta** | <ul><li>Al enviar el formulario, se muestra una segunda pantalla: “Reserva tu lugar pagando $10 ahora y serás el primero en usarla cuando salga. Precio final $200/mes”.</li><li>Botón “Pagar $10”.</li></ul> | **Stripe Checkout** (solo tarifas de transacción: 2.9 % + $0.30 por pago) → **≈ $0.30** por cada intento. | 1 h |
| **4️⃣ Tráfico de prueba (validación de demanda)** | <ul><li>Campaña de **Facebook/Instagram Ads** dirigida a “Propietarios de pequeñas agencias de marketing”, intereses: “marketing digital”, “agencia de publicidad”, “Google Analytics”.</li><li>Presupuesto: **$150** (costo por clic ~ $0.50 → ~300 visitas).</li></ul> | **$150** (puedes reducir a $50 y ajustar los cálculos, pero $150 da un margen razonable). | 1 día para lanzar, 5‑7 días para correr. |
| **5️⃣ Encuesta de salida (opcional, pero barato)** | En la página de “gracias” después del pago o del formulario, incluye 2‑3 preguntas rápidas: <br>1) ¿Cuánto pagarías al mes por esta herramienta? <br>2) ¿Qué te haría cancelar? <br>3) ¿Usarías la herramienta ahora mismo? | **Google Forms** (gratis). | 30 min |
| **6️⃣ Análisis y criterio de “matar”** | Recopila: <br>• Nº de visitas a la landing. <br>• Nº de formularios completados. <br>• Nº de pagos de $10 (pre‑venta). <br>• Respuestas de la encuesta. | Excel/Google Sheets (gratis). | 1 h |

---

## 3. Métricas y umbral de fracaso

| Métrica | Fórmula | Umbral “Mata‑hipótesis” |
|---------|---------|------------------------|
| **Tasa de conversión a pre‑venta (C‑Pre)** | (Pagos $10 ÷ Visitas) × 100 | **< 1 %** (menos de 3 pagos en 300 visitas) |
| **WTP medio** (según encuesta) | Promedio de respuestas a “¿Cuánto pagarías?” | **< $150/mes** |
| **Interés cualificado** (IC) | (Formularios completados ÷ Visitas) × 100 | **< 2 %** |
| **Número de agencias interesadas** | Total de pagos $10 | **0** o **1** |

**Regla de decisión**  
- Si **C‑Pre** está por debajo del 1 % **o** el **WTP medio** está bajo $150 **o** obtienes **≤ 1** pago de $10, **abandona la idea**.  
- Si cualquiera de esas métricas supera el umbral, la hipótesis *no* está matada y puedes pasar a validar más a fondo (MVP, entrevistas, etc.).

---

## 4. Coste total estimado

| Concepto | Coste |
|----------|-------|
| Dominio + hosting (opcional) | $20 |
| Carrd (plan Pro) | $19 |
| Publicidad Facebook/IG | $150 |
| Stripe fees (asumiendo 0‑3 pagos) | ≤ $1 |
| **Total máximo** | **≈ $190** |

*(Si ya tienes dominio/hosting, el gasto cae a ≈ $170.)*

---

## 5. Cronograma compacto (10 días)

| Día | Acción |
|-----|--------|
| 1 | Definir perfil, crear mock‑up y landing page, integrar Stripe. |
| 2 | Testar la página (técnicamente). |
| 3 | Lanzar campaña de ads ($150). |
| 4‑8 | Recoger datos (visitas, formularios, pagos). |
| 9 | Cerrar campaña, exportar datos, enviar encuesta final. |
| 10 | Analizar métricas, aplicar regla de decisión, decidir. |

**Tiempo total de trabajo:** ≈ 12 horas (≈ $0 de tu tiempo si lo haces tú).  
**Tiempo de espera:** 5‑7 días (tiempo de la campaña).

---

## 6. Qué hacer si el experimento **mata** la hipótesis

1. **Documenta** los números y el feedback (p.ej., “No necesito automatizar, ya uso Excel”).  
2. **Re‑evalúa** la propuesta de valor: ¿quizá el precio es demasiado alto? ¿Tal vez el problema no es la automatización sino la visualización?  
3. **Desvío**: Usa lo aprendido para buscar otra necesidad en el mismo segmento (p.ej., “Plantillas de reportes personalizables”).  
4. **Cierra** la inversión en desarrollo y destina esos recursos a otro proyecto con mejor señal de mercado.

---

## 7. Resumen rápido (para copiar‑pegar)

1. **Mock‑up** → 2‑3 pantallas (Figma, gratis).  
2. **Landing** con botón “Pagar $10” (Carrd $19).  
3. **Campaña FB/IG** → $150, 300 visitas.  
4. **Mide**: pagos $10, formularios, WTP.  
5. **Mata** si C‑Pre < 1 % **o** WTP < $150 **o** ≤ 1 pago.  
6. **Coste total** ≈ $190, **tiempo** 10 días, **trabajo** 12 h.

Con este experimento tienes una prueba **conclusiva y barata** de que las agencias pequeñas **no** están dispuestas a pagar $200/mes por la herramienta, sin invertir ni una línea de código. ¡A lanzar!