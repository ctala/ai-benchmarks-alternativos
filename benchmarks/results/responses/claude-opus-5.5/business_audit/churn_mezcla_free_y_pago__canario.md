# Claude Opus 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 14.947s | tokens_per_second: 89.5
- input_tokens: 264 | output_tokens: 1338

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

# Respira: el 31% no mide lo que te preocupa

El 31% mezcla dos poblaciones con comportamientos muy distintos. Separándolas:

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| **Total (lo que reporta el panel)** | 200 | 62 | **31%** |

El 97% de las bajas (60 de 62) vienen del plan gratuito. El número que afecta a tus ingresos es el **churn de pago: 9,1%**.

## ¿Qué tan grave es?

**El churn de pago (9,1%)** está por encima del 5% que esperabas, pero con matices:
- **Son 2 personas.** Con 22 clientes, cada baja mueve el indicador unos 4,5 puntos. Una sola baja menos y estarías en 4,5%. Un mes no basta para concluir que hay una tendencia.
- **Conviene saber de dónde salía tu 5%.** Si era el churn de pago de meses anteriores, compara la misma métrica, no el total.
- Revisa también el **churn de ingresos (MRR perdido)**: si esos 2 clientes pagaban poco, el impacto es menor que el 9%.

**El churn gratuito (33,7%)** es alto, pero en planes gratuitos suele serlo. Lo importante es qué cuenta tu plataforma como "baja" de un usuario gratuito: ¿borró la cuenta, dejó de entrar 30 días o fue una limpieza automática de cuentas inactivas? Si la definición o algún proceso cambió este mes, eso explicaría el salto.

## Plan

**Esta semana (diagnóstico)**
1. **Corrige el panel.** Configúralo para mostrar churn de pago, churn gratuito y MRR churn por separado. El 31% combinado no sirve para decidir.
2. **Averigua qué es una "baja" gratuita** y si hubo algún cambio este mes (purga de inactivos, cambio de definición, migración).
3. **Habla con los 2 clientes de pago que se fueron.** Con tan pocos casos, la conversación directa vale más que cualquier análisis: precio, producto, competencia o un cierre de negocio.
4. **Mira la tendencia de 3 a 6 meses** del churn de pago, no solo este mes.

**Próximas semanas (si los datos lo justifican)**
5. **Si el churn de pago sigue alto de forma sostenida:** busca señales previas a la baja (caída de uso, tickets de soporte) y crea alertas tempranas para contactar a quien muestre riesgo.
6. **Para el plan gratuito:** más que reducir su churn, mide la **conversión a pago**. Un usuario gratuito que se va sin haber activado el producto no es un problema de retención, sino de onboarding o de captación.
7. **Mide la activación:** ¿los 60 que se fueron llegaron a usar la función principal? Si no, el problema está en los primeros días.

## En resumen

No tienes un churn del 31%. Tienes un churn de pago del 9% basado en 2 bajas, que merece atención pero no pánico, y un churn gratuito alto que depende de cómo se define. Lo primero es separar las métricas en el panel y hablar con esos 2 clientes.