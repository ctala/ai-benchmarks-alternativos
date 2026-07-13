# GPT-5.6 Luna — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 6.81 | quality: 7.2
- latency_total: 7.174s | tokens_per_second: 123.1
- input_tokens: 128 | output_tokens: 883

## Respuesta completa

No. **“Retención de ingresos: 114%” no significa que retengas al 114% de tus clientes** ni que prácticamente no haya churn.

Probablemente se refiere a **Net Revenue Retention (NRR)**:

\[
\text{NRR}=\frac{\text{ingresos iniciales de la cohorte} - \text{churn} - \text{downgrades} + \text{expansiones}}{\text{ingresos iniciales de la cohorte}}
\]

El 114% significa que, tomando los clientes que ya existían al inicio del periodo, ahora generas un **14% más de ingresos recurrentes**, después de descontar bajas y reducciones. Puede superar el 100% porque incluye upgrades, más usuarios o productos adicionales.

Pero eso no dice cuántos clientes se fueron.

### Con tus datos

- Clientes al inicio: **40**
- Clientes al final: **36**
- Si no hubo clientes nuevos y cuatro clientes se dieron de baja:
  - Retención de clientes: **90%**
  - Churn de clientes: **10%**

Si además entraron clientes nuevos, entonces se fueron más de cuatro clientes. Por ejemplo, si captaste dos nuevos, habrías perdido seis y tu churn de clientes sería del **15%**.

Además, el 114% puede coexistir perfectamente con un churn de clientes elevado si los clientes que permanecen hacen upgrades importantes. Por ejemplo:

- Ingresos iniciales: 100
- Churn y downgrades: -20
- Expansiones: +34
- Ingresos de la cohorte: 114
- NRR: 114%

En ese caso has perdido clientes e ingresos, pero los clientes restantes han expandido mucho su gasto.

Conviene separar estas métricas:

1. **Retención de clientes o logo retention**: qué porcentaje de clientes sigue activo.
2. **Logo churn**: qué porcentaje de clientes se pierde.
3. **GRR — Gross Revenue Retention**: ingresos retenidos sin contar expansiones. Nunca supera el 100%.
4. **NRR — Net Revenue Retention**: incluye expansiones y puede superar el 100%.
5. **Ingresos de nuevos clientes**: deben quedar fuera del NRR si quieres medir correctamente la salud de la base existente.

Por tanto, **no dejaría de preocuparme por el churn**. Un NRR del 114% es una señal positiva sobre la expansión de los clientes existentes, pero una retención de clientes del 90% —o menor si hubo altas nuevas— puede indicar problemas de producto, onboarding, precio o ajuste con el mercado. Revisa en el panel si ese 114%:

- excluye clientes nuevos;
- se calcula sobre ingresos recurrentes, no facturación puntual;
- está segmentado por cohorte;
- viene acompañado de GRR y logo churn.

La lectura correcta sería: **“Los ingresos de mi cohorte existente crecieron un 14%, pero todavía necesito saber cuántos clientes estoy perdiendo y cuánto ingreso pierdo con ellos.”**