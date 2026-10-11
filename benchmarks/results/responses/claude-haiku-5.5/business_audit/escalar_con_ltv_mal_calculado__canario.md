# Claude Haiku 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 12.892s | tokens_per_second: 193.0
- input_tokens: 297 | output_tokens: 2488

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

**No le des todavía.** Con tus números, cada cliente nuevo apenas recupera lo que cuesta, y el problema está en la aritmética.

**1. Tu LTV usa un plazo que tus datos no respaldan.** Con 8% de churn mensual, la vida media de un cliente es 1/0,08 = **12,5 meses**, no 24. A los 24 meses sobrevive solo el 0,92²⁴ ≈ 13% de la cohorte.

**2. Tu LTV ignora el margen.** Es ingreso, no ganancia.

Recalculado:

- LTV con ingreso: 35 × 12,5 = $437
- LTV bruto (× 70%): **$306**
- CAC: $290
- **LTV/CAC = 306 / 290 ≈ 1,06**

No es 2,9. Estás en 1:1, y la regla de 3:1 no se cumple.

**3. El payback es mucho más largo de lo que sugiere el número simple.** Ganancia bruta mensual por cliente: 35 × 0,70 = $24,5. Sin churn, recuperar $290 tomaría unos 12 meses. Pero como la mitad de los clientes se van antes de que eso ocurra, la cohorte completa tarda unos **35 meses** en pagar su CAC.

**4. Con $10.000 en este momento:**

- Compras ~34 clientes.
- Ganancia bruta esperada de toda su vida: 34 × $306 ≈ $10.400.
- Resultado: unos +$400 nominales en 3 años, sin descontar el dinero. Estás financiando el crecimiento con caja durante casi toda la vida de esos clientes.

**Qué tendría que ser cierto para escalar (LTV/CAC ≥ 3):**

- Bajar el CAC a ~$102, o
- Bajar el churn a ~2,8% mensual (con $290 de CAC), o
- Subir el precio a unos $100+ con el mismo churn y CAC (aproximado, depende de cómo afecte el precio al churn).

Ejemplo de sensibilidad al churn con precio $35, margen 70% y CAC $290:

| Churn mensual | LTV bruto | LTV/CAC |
|---|---|---|
| 8% | $306 | 1,06 |
| 4% | $612 | 2,1 |
| 2% | $1.225 | 4,2 |

**Qué haría yo en tu lugar:**

1. **Prueba con $1.000–1.500**, no con $10.000. Eso te da unos 4–5 clientes por semana si el CAC es realista, suficientes para medir algo sin quemar caja.
2. **Investiga el churn antes que el CAC.** 8% mensual es alto para una suscripción de $35. Mira las razones de cancelación, el primer mes de uso y si hay un momento en el que el cliente deja de recibir valor. Es lo más barato de mejorar.
3. **Prueba planes anuales con descuento.** Un cliente anual con 20–30% de descuento cambia completamente la ecuación y reduce el churn efectivo.
4. **Verifica tu CAC.** ¿Incluye herramientas, creativos, tiempo de ventas? Si lo calculas solo con gasto en anuncios dividido entre clientes, puede estar subestimado, o sobreestimado si atribuyes mal.
5. **Escala solo cuando LTV/CAC (con margen) sea ≥ 3 en una muestra de al menos 2–3 cohortes.**

Si me pasas tu churn por cohorte, de dónde salen los clientes (canal) y cuánto gastaste en anuncios los últimos meses, puedo ayudarte a calcular el CAC real y ver si hay un canal que sí cumpla.