# Granite 4.2 8B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 66.023s | tokens_per_second: 91.6
- input_tokens: 227 | output_tokens: 6050

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**Respuesta clara, concisa y práctica (sin jerga innecesaria).** Como analista de unit economics, te respondo directamente con los cálculos correctos, los riesgos reales de tu plan y una recomendación paso a paso. **Te digo si le das los $10.000 ahora, y por qué.** (Te evito teorías; solo números reales y acciones concretas.)

---

### 1. **Tu cálculo de LTV está incorrecto (es el error más común al escalar con publicidad).**  
> *Tú dijiste: "LTV = $35 × 24 meses = $840"*.  
**¿Por qué está mal?** Porque ignoras el **churn mensual del 8%**. Si no consideras el churn, asumes que todos los clientes duran 24 meses, pero con un churn del 8% al mes, *promedio* un cliente dura **~12.5 meses** (no 24). El churn corta la vida del cliente en tiempo real.

**Cálculo correcto de LTV (relevante para decisiones de escalamiento):**  
> LTV = (Ingresos mensuales por cliente × Margen bruto) / Churn mensual  
> *Explicación breve:* Es el ingreso neto (después de costos fijos como infraestructura y pagos) que un cliente genera en promedio durante su vida útil, contabilizando el churn.  
> - Ingresos mensuales por cliente = $35  
> - Margen bruto = 70% → Ingreso neto por cliente por mes = $35 × 70% = **$24.50**  
> - Churn mensual = 8% = 0.08  
> - **LTV (neto) = $24.50 / 0.08 = $306.25**  
> *(Esto significa: un cliente promedio genera ~$306.25 de ingreso neto total durante su ciclo de vida, considerando que se baja al ~12.5 meses promedio. No $840, porque el churn corta el ciclo.)*

> **¿Por qué no usar "$35 × 24"?** Porque con churn del 8% al mes, el 8% de los clientes se van cada mes. En promedio, un cliente dura ~12.5 meses (1 / 0.08 = 12.5), no 24. Hacer "$35 × 24" subestima el churn y sobreestima el LTV. **Tu estimación de $840 es optimista y poco realista para el ciclo actual.**

**LTV/CAC real (neto):**  
> - CAC (costo de adquirir cliente con publicidad) = **$290** (asumimos que este $290 incluye solo el gasto en publicidad; si incluye también ventas/otros costos, confirma eso primero, pero lo usamos tal cual).  
> - LTV neto = $306.25  
> - **LTV/CAC real = $306.25 / $290 ≈ 1.06** (no 2.9).  

> **Interpretación clara:**  
> - LTV/CAC = 1.06 significa que, *promedio*, el ingreso neto que genera un cliente (contabilizando churn) es solo ~106% del costo de adquirirlo.  
> - La regla de oro de la industria (y lo que suele ser sostenible para escalar sin riesgo de pérdida) es **LTV/CAC > 3** para escalamiento fuerte y predecible. **1.06 < 3 es crítico:** estás acudiendo a clientes por $290 para obtener ~$306 de ingreso neto *en total* durante su vida útil. En el primer mes, recibirás solo ~$24.50 de ingreso neto por cliente ($35 × 70%), mientras que el costo de adquisición ($290) se paga al inicio. Esto crea un desequilibrio de flujo de efectivo en los primeros 1–2 meses.

> *Ejemplo práctico con $10.000 en publicidad:*  
> - CAC = $290 → $10.000 / $290 ≈ 34.5 nuevos clientes adquiridos este mes.  
> - Ingresos netos en el mes 1 de estos clientes: 34.5 × $24.50 ≈ $848 (ingreso neto mensual).  
> - Costo de adquisición total este mes: $10.000 (se paga al inicio o al momento de la campaña).  
> - **Flujo de efectivo neto en el mes 1:** ingreso neto ~$848 – costo de adquisición $10.000 = **–$9,152** (pérdida de efectivo en el mes de adquisición).  
> - *Luego*, a medida que los clientes viven (promedio ~12.5 meses), el ingreso neto acumulado superará el CAC ($290 por cliente), pero **ese superávit se paga en meses 2–13**, no en el mes 1. Si no tienes efectivo para cubrir el gasto inicial de $10.000, podrías tener problemas de liquidez (ej.: no pagar salarios, no tener stock de campaña, etc.).

> **Conclusión del cálculo:**  
> - Tu estimación de LTV/CAC = 2.9 estaba **incorrecta** (debido al ignorar churn).  
> - LTV/CAC real ≈ 1.06, **por debajo de 3**.  
> - Gastos de $10.000 en publicidad este mes **generarían una pérdida de efectivo en el mes 1** (ingreso neto inicial < costo de adquisición), incluso si el LTV a largo plazo parece "justo" (~$306 vs $290). Esto es común y peligroso si no se valida primero.

---

### 2. **¿Le das los $10.000 hoy?**  
> **No, no le des $10.000 hoy sin prueba previa.**  
> *Razón práctica y concisa:*  
> - Con LTV/CAC real ≈ 1.06, el gasto de $10.000 en publicidad este mes requeriría que el efectivo disponible cubra el gasto inicial ($10.000) mientras esperas el ingreso neto acumulado (~$848 en el mes 1 y creciendo en meses siguientes). Si tu caja actual no tiene $10.000 + un pequeño margen de seguridad (ej.: $1.000–$2.000 para cubrir el mes 1), **escalar a $10.000 ahora arriesga un problema de liquidez** (ej.: no poder pagar la publicidad si la campaña no convierte bien en el primer mes).  
> - Además, el CAC de $290 es una estimación; en pruebas reales, el CAC suele variar (puede ser un poco más alto o más bajo) porque depende de la tasa de conversión de la campaña, el targeting y la optimización. **No puedes asumir $290 con certeza al escalar directamente a $10.000.**

> *Ejemplo realista:* Si haces una prueba pequeña de $500–$1,000 en publicidad esta semana, mides:
> 1. **Tasa de conversión real:** cuántos clics → leads → clientes reales (ej.: $500 en ads → ¿cuántos clientes nuevos compran? → CAC real = $500 / #clientes nuevos).
> 2. **Churn real en la prueba:** observa el churn de los nuevos clientes en los primeros 1–2 meses (no asumas 8% si es tu promedio general; puede variar por segmento o campaña).
> 3. **LTV real observado:** registra el ingreso neto mensual de los nuevos clientes durante sus primeros 3–4 meses.
> 4. **Flujo de efectivo:** calcula: costo de la prueba (ej. $500) vs ingreso neto acumulado en los primeros 2 meses (ej. #clientes × $24.50 × meses vivos).

> **Si la prueba de $500 funciona (CAC real ≈ $280–$300, churn ≈ 7–9%, LTV neto observado ≈ $280–$320), entonces puedes escalar gradualmente:**  
> - Aumenta la inversión solo en el mismo canal/segmento que validaste.  
> - Usa un factor seguro: por ejemplo, **solo aumenta el gasto en publicidad en un 20–30% por mes** si la prueba muestra CAC real ≤ $280 y LTV neto observado ≥ $300 (así mantienes LTV/CAC > 1.2 en el mes 1 y te da margen para ajustar).  
> - **Nunca subitas al 100% del presupuesto planeado ($10.000) sin validación previa.** Escalar rápido sin prueba es el motivo más común de que planes de crecimiento "muera en la aritmética" (como mencionas).

> **¿Por qué esto es seguro?** Porque:
> - Validar con $500–$1,000 te da datos reales (no una estimación optimista).
> - Mantienes flujo de efectivo: si la prueba funciona, puedes escalar con incrementos pequeños y medidos. Si no funciona (CAC > $320 o churn > 10%), detienes la campaña antes de gastar $10.000.
> - Te evita riesgo de liquidez: no gastas $10.000 de efectivo que necesitas para operar si la campaña no convierte en el mes 1.

---

### 3. **Recomendación paso a paso (acción concreta para este mes):**  
> 1. **Haz una prueba pequeña de $500–$1,000 en la misma publicidad (mismo canal, público, mensaje).** Usa el mismo targeting que usaste antes; solo reduce el presupuesto inicial.  
> 2. **Mide exactamente esto en 7–14 días:**  
>    - # de clientes nuevos adquiridos por la prueba.  
>    - CAC real = gasto de prueba / # clientes nuevos (ej. $700 gasto / 2.5 clientes = $280 CAC).  
>    - Churn de los nuevos clientes en los primeros 30 días (observa cuántos se van en el mes 1).  
>    - Ingreso neto mensual de los nuevos clientes (usando $24.50 = $35 × 70%).  
> 3. **Calcula LTV neto observado en 2–3 meses:** (Ingreso neto mensual × meses vivos promedio en prueba). Ejemplo: si 2.5 clientes nuevos, churn de nuevos en mes 1 = 5%, y todos pagan 2 meses, LTV neto observado ≈ 2.5 × $24.50 × 2 = $122.50 total neto por prueba → LTV/CAC observado = $122.50 / $280 ≈ 0.44 (esto te dirá si la campaña funciona para tu segmento). *Si ves LTV/CAC > 1.5 en la prueba, es buen signo para escalar.*  
> 4. **Decide escalar solo si:**  
>    - CAC real en la prueba ≤ $280 (≤ 90% de tu CAC estimado de $290).  
>    - Churn de nuevos clientes ≤ 9% (cerca de tu promedio general de 8%).  
>    - LTV/CAC observado en 2–3 meses ≥ 1.5 (ej. $350 neto / $280 CAC = 1.25+ es mínimo seguro; 1.5+ es más cómodo para escalar). *1.5 es mejor que 1.06 porque te da margen para pequeñas variaciones.*  
>    - Tienes efectivo suficiente: si la prueba cuesta $800 y genera $150 de ingreso neto en el mes 1, asegúrate de tener al menos $800 + $200 de margen de seguridad en efectivo antes de escalar (ej.: no gastar todo el efectivo en la prueba).  
> 5. **Si la prueba funciona (LTV/CAC ≥ 1.5), escala gradualmente:**  
>    - Mes 1 de escalamiento: gasto en publicidad = $1,000 (ej. 20% más que la prueba).  
>    - Mes 2: si la campaña sigue con CAC ≤ $280 y LTV observado ≥ $300, aumenta otro 20–30%.  
>    - **Nunca subas más del 30% por mes en gasto de publicidad hasta que hayas validado 2–3 ciclos de prueba (2–3 meses) con datos reales.**  
>    - *Ejemplo:* Prueba $500 → funciona → Mes 1 escalar $600 → Mes 2 escalar $700 → Mes 3 escalar $800, etc. Así evitas saltar a $10.000 de golpe.

> **¿Por qué este paso a paso?** Porque:
> - Te ahorra perder $10.000 en una campaña que podría tener CAC real de $320 (ej.: si la tasa de conversión baja 10% vs la estimación).
> - Te da datos reales para ajustar el targeting o el mensaje antes de escalar.
> - Mantienes flujo de efectivo (no pones $10.000 de efectivo que necesitas operar en el mes 1).
> - Escalas de forma predecible y sostenible (LTV/CAC > 1.5 en prueba → escalada segura).

---

### Resumen final en 3 frases (para recordar):
> **"No gastes $10.000 ahora porque LTV/CAC real ≈ 1.06 < 3 (y el gasto inicial de $10.000 causaría pérdida de efectivo en el mes 1). Haz una prueba pequeña ($500–$1,000) para medir CAC real, churn de nuevos y LTV neto observado. Solo escala gradualmente (+20–30% por mes) si la prueba muestra CAC ≤ $280 y LTV/CAC ≥ 1.5 en 2–3 meses, con efectivo suficiente para cubrir el gasto inicial."**

> ✅ **Acción inmediata para este mes:** Lanza una prueba de $500–$1,000 en la misma publicidad, mide CAC real, churn de nuevos y LTV neto en 30–60 días. *Eso es todo lo que necesitas para decidir si $10.000 es seguro o no.* Si la prueba funciona, escala con pasos pequeños; si no, ajusta targeting/mensaje y prueba otra vez.

> *No hay teoría: solo números reales, flujo de efectivo y una prueba mínima para evitar perder dinero en la aritmética. Escalar fuerte requiere escalar con pruebas, no con suposiciones.*

¿Quieres que te ayude a redactar el brief de la prueba pequeña (ej. qué decir en la campaña, cómo medir el churn en 30 días, qué campo usar en tu CRM para registrarlo)? Dime el canal de publicidad (Meta, Google, etc.) y te doy un ejemplo concreto de mensaje + métrica de seguimiento en 1 línea. Estoy listo para ayudarte a ejecutarlo.