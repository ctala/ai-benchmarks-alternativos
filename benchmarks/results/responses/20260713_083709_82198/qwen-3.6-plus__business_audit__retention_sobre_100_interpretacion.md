# Qwen 3.6 Plus — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 5.86 | quality: 6.0
- latency_total: 51.072s | tokens_per_second: 53.5
- input_tokens: 143 | output_tokens: 2732

## Respuesta completa

No, no es correcto. Estás confundiendo dos métricas distintas que miden cosas diferentes y que, en tu caso, están contando historias opuestas.

### 🔍 Qué significa realmente ese 114%
Esa cifra es **Net Revenue Retention (NRR)** o Retención Neta de Ingresos. Se calcula sobre **dinero**, no sobre clientes:
`NRR = (MRR inicial - MRR perdido por bajas - MRR perdido por rebajas + MRR ganado por subidas/expansiones) / MRR inicial`

Un 114% indica que, con la misma cohorte de clientes del mes pasado, hoy generas un 14% más de ingresos recurrentes. Lo has logrado porque las subidas de plan han compensado con creces las pérdidas. **Es una excelente señal de capacidad de expansión y pricing power**, pero no dice nada sobre cuántas cuentas se han quedado.

### 📉 Qué dicen tus números de clientes
Si pasaste de 40 a 36 clientes de pago (y no asumimos que hayas captado nuevos en el camino), tu **Logo Retention** es del 90% y tu **Logo Churn** del 10%. La retención de clientes nunca puede superar el 100% por definición matemática: no puedes retener más cuentas de las que empezaste.

### ⚠️ Por qué es peligroso dejar de preocuparte por el churn
Un NRR >100% con churn de clientes alto es una situación estructuralmente frágil:

1. **Techo de expansión:** Los 36 clientes restantes no pueden subir de plan indefinidamente. Cuando su consumo o necesidad se estabilice, las expansiones se secarán y tu NRR caerá en picado si el churn de logos se mantiene.
2. **Efecto compuesto:** Un 10% de churn mensual equivale a retener solo ~28% de tu base en 12 meses `(0.9^12 ≈ 0.28)`. Estás perdiendo el 72% de tus clientes al año.
3. **Economía unitaria:** Adquirir un nuevo cliente cuesta entre 5 y 25 veces más que retener uno existente. Si compensas bajas constantes con captación, tu CAC payback se alarga y tu LTV/CAC se degrada.
4. **Sesgo de supervivencia:** Estás midiendo el éxito en una base que se está reduciendo. Un SaaS maduro y escalable necesita **ambos** motores: Logo Retention >95% mensual + NRR >100%.

### ✅ Qué deberías hacer ahora
- **Separa los KPIs:** Sigue midiendo NRR, pero añade obligatoriamente `Gross Logo Retention` y `Gross Logo Churn` a tu panel.
- **Audita las 4 bajas:** ¿Eran planes bajos o altos? ¿Fue por onboarding, soporte, ajuste de precio, o falta de uso? El churn cualitativo explica por qué tu NRR aguanta y tu base no.
- **No pares la retención:** Invierte en customer success, revisa triggers de renovación, mide el tiempo hasta la primera acción de valor y reduce la fricción en la re-contractación.
- **Objetivo realista:** Un NRR del 114% es un motor potente, pero si pierdes clientes constantemente, estás acelerando con el freno de mano puesto. Apunta a <3% de logo churn mensual mientras mantienes NRR >100%.

Si quieres, puedo ayudarte a calcular tu churn mensual por logos, segmentar las bajas por cohorte/plan y montar un dashboard que te muestre ambas métricas en paralelo para que dejes de tomar decisiones con una sola mitad del espejo.