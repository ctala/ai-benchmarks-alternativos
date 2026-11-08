# Qwen 3-Next 80B Instruct — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 6.593s | tokens_per_second: 231.9
- input_tokens: 229 | output_tokens: 1529

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

No. **No le das.**  
Tu cálculo está **errado en la aritmética básica del LTV**, y si lo aplicas así, **vas a quemar dinero rápido**. Vamos a corregirlo paso a paso.

---

### 🔍 Tus datos:
- **Precio mensual (MRR)**: $35  
- **Churn mensual**: 8% → **esto es crítico**  
- **Margen bruto**: 70% → entonces **LTV útil = 70% × LTV bruto**  
- **CAC**: $290  
- **Tu cálculo de LTV**: $35 × 24 = $840 → **esto es incorrecto**.  
  → **No puedes multiplicar por 24 meses si el churn es 8% mensual.**

---

## ✅ Cálculo correcto de LTV (Lifetime Value)

Cuando tienes **churn mensual constante**, el LTV se calcula con la fórmula de **vida media del cliente**:

> **LTV (bruto) = MRR / Churn mensual**

Esto viene de la fórmula de serie geométrica: si un cliente se va con probabilidad 8% cada mes, la vida esperada es 1 / 0.08 = 12.5 meses.

### ✅ Entonces:
> **LTV bruto = $35 / 0.08 = $437.50**

Ahora, aplicamos el **margen bruto del 70%**:

> **LTV neto (con margen) = $437.50 × 0.70 = $306.25**

---

### 📊 CAC = $290  
### ✅ LTV/CAC = $306.25 / $290 ≈ **1.055**

---

## ⚠️ ¡Tienes un LTV/CAC de **1.06**!

Esto significa que **por cada dólar que gastas en adquirir un cliente, solo recuperas $1.06 en ganancia neta**.

👉 **No es rentable.**  
👉 **No es escalable.**  
👉 **Estás ganando 6 centavos de ganancia por cada dólar gastado en publicidad.**

---

## 💡 ¿Qué pasa si escalas con $10.000 en publicidad?

- Adquieres: $10,000 / $290 ≈ **34.5 clientes**  
- LTV neto total generado: 34.5 × $306.25 ≈ **$10,565**  
- Costo de adquisición: $10,000  
- **Ganancia neta: $565**

→ **Sí, ganas $565 este mes.**

Pero...

### ❗ ¡OJO! Esto asume que:
- No hay costos de servicio, soporte, onboarding, retención, etc.  
- El churn se mantiene constante.  
- No hay inflación en CAC (cuando escalas, el CAC sube por competencia).  
- No hay costos operativos fijos que se disparan con más clientes.

Y lo peor: **tu modelo está en el borde de la rentabilidad**.  
Si el churn sube a 9% → LTV cae a $272 → **LTV/CAC = 0.94 → pierdes dinero.**

---

## 🚨 Conclusión: NO le das al plan.

Tu modelo **no es escalable con publicidad pagada**.  
Estás en **LTV/CAC = 1.06**, y necesitas **al menos 3** para escalar con seguridad (y 4+ si quieres crecer rápido y tener margen para errores).

---

## ✅ Recomendaciones para hacerlo escalable:

### 1. **Baja el churn.**
- 8% es muy alto para SaaS.  
- Si lo bajas a 5% → LTV = $35 / 0.05 = $700 → $490 neto → LTV/CAC = 1.69 → aún bajo.  
- Si lo bajas a **3%** → LTV = $35 / 0.03 = $1,167 → $817 neto → LTV/CAC = **2.82** → **casi viable**.  
→ **Enfócate en retención antes que en adquisición.**

### 2. **Sube el precio.**
- ¿Puedes subir a $45/mes? → LTV neto = ($45 / 0.08) × 0.7 = $393.75 → LTV/CAC = 1.36 → aún bajo.  
- ¿$55/mes? → $481 neto → LTV/CAC = **1.66** → mejor, pero aún no ideal.

### 3. **Baja el CAC.**
- ¿Puedes conseguir clientes por $180 en vez de $290? → LTV/CAC = 1.7 → aún bajo.  
- ¿$120? → LTV/CAC = **2.55** → ¡ahí sí empiezas a tener margen!

### 4. **Haz upsells o cross-sells.**
- Si cada cliente genera $50/mes en promedio (no $35), LTV neto sube a $437 → LTV/CAC = 1.5 → mejor.

### 5. **Prueba modelos orgánicos primero.**
- Referral programs, contenido, SEO, comunidad.  
- Tu CAC orgánico podría ser $50 → LTV/CAC = 6.1 → ¡ahí sí escala!

---

## 💬 Frase final para el fundador:

> “**No escala lo que es rentable, escala lo que es *muy* rentable.**  
> Un LTV/CAC de 1.06 no es un modelo de crecimiento, es un modelo de ‘esperar a que el mercado te salve’.  
> Mejora tu retención, sube tu precio o baja tu CAC — antes de poner $10k en ads.”  

---

✅ **Acción inmediata:**  
Haz un análisis de **por qué se va el 8% de tus clientes cada mes**.  
Esa es tu verdadera palanca de crecimiento.  
La publicidad pagada es el acelerador — pero si el carro tiene los frenos puestos, no sirve de nada.

¿Quieres que te ayude a diseñar un plan de reducción de churn? Te doy un template.