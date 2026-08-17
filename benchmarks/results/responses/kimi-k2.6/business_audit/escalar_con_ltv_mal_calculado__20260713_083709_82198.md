# Kimi K2.6 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.08 | quality: 8.4
- latency_total: 128.324s | tokens_per_second: 31.8
- input_tokens: 231 | output_tokens: 4086

## Respuesta completa

 **No le doy.** Y deberías agradecerme.

Tu plan no muere por ambición, muere en la aritmética. Tienes tres errores que convierten esos $10.000 en un auto para quemar efectivo. Te los corrijo:

---

### Error 1: El churn del 8% mata tu supuesto de "2 años"
Un churn mensual del 8% no da una vida útil de 24 meses. Da una vida útil promedio de:

**Vida útil = 1 / Churn = 1 / 0,08 = 12,5 meses.**

Si tus clientes realmente se quedan 2 años, tu churn mensual debería ser de ~4,2%, no 8%. Estás usando un supuesto deseado (24 meses) que contradice tu dato real (8%). En finanzas de suscripción, **gana el churn sobre los deseos**.

### Error 2: Tu LTV real no es $840
Con churn del 8%, el cálculo correcto es:

* **LTV de ingresos** = $35 / 0,08 = **$437,50**
* **LTV de margen bruto** = ($35 × 0,70) / 0,08 = **$306,25**

Tu ratio LTV/CAC real:

* Por ingresos: $437 / $290 = **1,5x**
* Por margen: $306 / $290 = **1,06x**

Ni siquiera estás cerca del 3x sano. Estás en zona de quiebre unitario.

### Error 3: El payback period es letal
Con un margen de $24,50 por cliente ($35 × 70%), necesitas:

**$290 / $24,50 = 11,8 meses** para recuperar cada adquisición.

Pero con un churn del 8% mensual, la probabilidad de que un cliente llegue vivo al mes 12 es solo:

**(0,92)^12 = 36,8%**

**Traducción:** Más del **63% de tus clientes pagados se irán antes de que recuperes lo que invertiste en traerlos**. Estás apostando a una moneda cargada en tu contra.

---

### ¿Qué pasa si metes los $10.000?

* Adquieres ~**34 clientes**.
* Toda esa cohorte, a lo largo de toda su vida, genera ~**$10.400** de margen bruto.
* Invertiste **$10.000**.

Tu retorno neto de la inversión es de unos **$400** (un 4%). Y tu capital estará congelado casi un año. Eso no es escalar; es financiar el crecimiento de Facebook y Google a cambio de migajas.

Peor aún: si al escalar con tráfico frío tu churn empeora (lo habitual), esos números se invertirán y empezarás a perder plata por cada cliente que entra.

---

### ¿Por qué sientes que eres rentable hoy?

Probablemente porque tus clientes actuales vienen de canales orgánicos, referidos o con CAC muy bajo. Eso es rentable. **Pero la publicidad pagada con estos números es una unidad económica distinta y enferma.** Si escalar significa inyectarle cáncer al negocio, no es escalar.

---

### Mi recomendación antes de tocar esos $10.000

1. **Baja ese churn a <4% mensual** (ideal <2%). Con 8% estás fugando clientes más rápido de lo que puedes traerlos sanamente.
2. **Optimiza el CAC.** Debe bajar a <$150 para respirar, o mejor aún, <$100.
3. **Sube el ticket.** $35 con 8% de churn es un modelo agotador. ¿Puedes hacer pricing anual con descuento? ¿Upsells?
4. **Si quieres probar, usa $1.000, no $10.000.** Mide cohortes semanales reales: CAC, churn a los 30-60-90 días y payback period. No inviertas a ciegas en una unidad que no cierra.

**Conclusión:** Con un 8% de churn y un CAC de $290 sobre $35/mes, **escalar con publicidad pagada es suicidio de cash**. Arregla la unidad económica primero. Después hablamos de los $10.000.