# Claude Sonnet 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 16.436s | tokens_per_second: 116.3
- input_tokens: 264 | output_tokens: 1911

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

# Respira: el 31% no es tu número de riesgo, pero tampoco te quedes tranquilo todavía

## Qué población mide cada cifra

El 31% mezcla dos poblaciones muy distintas:

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 (89%) | 60 | **33,7%** |
| De pago | 22 (11%) | 2 | **9,1%** |
| Total | 200 | 62 | 31% |

El 97% de las bajas son usuarios gratuitos. El número del panel describe sobre todo a los free, no a tu negocio de ingresos.

## Qué no sabemos todavía

1. **De dónde sale tu 5%.** ¿Era churn de usuarios de pago, churn de ingresos, un promedio histórico, o una expectativa? Si era sobre pagos, hay que comparar 9,1% contra 5%, no 31% contra 5%.
2. **Cuánto pesa la muestra de pago.** Con 22 usuarios, cada baja mueve el churn ~4,5 puntos. Dos bajas dan 9,1%, pero el intervalo de confianza va aproximadamente de **3% a 28%**. Con estos datos no puedes distinguir 5% de 9%, ni afirmar que empeoró ni que está bien.
3. **Qué significa "baja" en el plan gratuito.** ¿Cancelación activa, borrado de cuenta, o inactividad automática? Si hubo una limpieza de cuentas inactivas, un cambio de política o bots/spam, el 33,7% puede ser un evento puntual y no un deterioro.

## Plan

**Hoy**
1. Redefine el reporte: separa churn de pago y churn gratuito. El churn global deja de ser tu métrica principal.
2. Confirma de dónde viene el 5% y qué población cubría.
3. Revisa la definición de "baja" para free y si algo cambió este mes (limpieza, pricing, onboarding, emails, bug en login).

**Esta semana**
4. Compara con los 3 a 6 meses anteriores por segmento. ¿El churn free de ~34% es normal o es un pico?
5. Mira a los 2 usuarios de pago que se fueron: antigüedad, uso previo, motivo de cancelación, ingreso perdido. Con n=2, el análisis cualitativo vale más que el estadístico.
6. Revisa la cohorte gratuita que se fue: ¿eran usuarios activos o cuentas dormidas? Si eran dormidas, el impacto real es casi nulo.

**Para adelante**
7. Mide el churn de pago con ventana móvil de 3 meses para suavizar el ruido de una base tan pequeña.
8. Si los free son tu fuente de conversión, vigila también la conversión free→pago y el churn de usuarios free *activos*. Ahí sí puede haber un problema.

## Veredicto provisional

- **Gravedad del 31%:** baja por sí sola, porque está dominada por usuarios gratuitos.
- **Posible problema real:** el churn de pago (9,1% vs. 5% esperado) podría ser ruido, pero con 22 clientes cada uno importa mucho.
- **Riesgo estructural:** una base de solo 22 usuarios de pago es frágil. Esa es probablemente la conversación de fondo.

Si me dices qué medía el 5% y qué incluye "baja" en el plan gratuito, te afino el diagnóstico.