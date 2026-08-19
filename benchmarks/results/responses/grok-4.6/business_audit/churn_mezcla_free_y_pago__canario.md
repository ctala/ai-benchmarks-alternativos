# Grok 4.6 — business_audit/churn_mezcla_free_y_pago

- model_id: `x-ai/grok-4.6`
- success: True  | final: 5.3 | quality: 6.0
- latency_total: 76.139s | tokens_per_second: 23.5
- input_tokens: 368 | output_tokens: 1793

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

**El 31 % no mide lo que crees.** El panel está calculando bajas sobre **todos** los usuarios (gratuitos + de pago). Eso es 62/200 = 31 %. La población que normalmente importa en un negocio de suscripción es otra.

### Tasas reales (mes actual)
- **Pago**: 2 bajas / 22 usuarios iniciales → **9,1 %**
- **Gratuito**: 60 / 178 → **33,7 %**
- Global (el número del panel): 31 %

Con n=22 el 9 % es ruidoso (2 personas). Sigue siendo alto para la mayoría de SaaS (benchmarks habituales 3-7 % mensual según vertical y ticket), pero **no es un 31 %**. El pánico viene de mezclar poblaciones.

### ¿Qué tan grave es?
- Corto plazo: no es un incendio. Perdiste 2 clientes de pago.
- Medio plazo: 9 % mensual anualizado es ~68 % de pérdida de base de pago si se mantiene. Eso sí duele.
- El churn gratuito alto es esperable en freemium/trial; solo es problema si tu tesis es “el free alimenta el paid” y la conversión está rota.

### Plan inmediato (esta semana)
1. **Separa el dashboard ya**. Dos KPIs fijos: churn logo pago, churn revenue pago (y opcionalmente free). Deja de mirar el número mezclado.
2. **Habla con las 2 bajas de pago hoy**. Motivo real (precio, valor no percibido, competencia, soporte, cambio de necesidades). Anota si era evitable.
3. **Revisa definición**. ¿“Baja” = cancelación explícita, impago, o inactividad? ¿Los 200 incluyen solo activos o también dormidos? Aclara esto antes de comparar con el 5 % que recordabas (puede que ese 5 % fuera de otro periodo, solo paid, o otra fórmula).
4. **Cohortes rápidas**. Churn de los que convirtieron a pago en los últimos 1-3 meses vs. los más antiguos. Si los nuevos se van más, el problema está en onboarding/activación, no en el producto maduro.

### Próximos 30 días
- Encuesta de cancelación automática + oferta de retención (descuento, pausa, downgrade) solo para paid.
- Métricas de salud de la base paid: % que usa la feature core semanalmente, tiempo desde última sesión, tickets abiertos.
- Si el free es un canal de adquisición, mide conversión free→paid y tiempo hasta conversión, no solo su churn.
- Objetivo realista: bajar churn paid a <6 % en 60-90 días. Con 22 clientes cada baja duele; el volumen pequeño te obliga a ser quirúrgico, no a “campañas masivas”.

El 31 % es un artefacto de población. El número que debes vigilar es el 9 % paid (y sobre todo por qué se fueron esas 2 personas). Empieza por hablar con ellas y separar las métricas. Si me pasas más contexto (ticket medio, si es B2B/B2C, razones que ya tengas de las bajas, o cómo calculabas el 5 %), afinamos el plan.