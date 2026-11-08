# Claude Sonnet 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 15.133s | tokens_per_second: 110.0
- input_tokens: 264 | output_tokens: 1665

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

# Respira: el 31% es real, pero mezcla dos poblaciones muy distintas

## Qué dicen los datos

| Segmento | Base inicial | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| Total | 200 | 62 | 31% |

El 89% de tu base es gratuita y aporta el 97% de las bajas, así que el número total casi solo describe al plan gratuito.

## Qué tan grave es

**Lo que probablemente importa (los de pago):**
- 9,1% vs. tu 5% esperado. Con 22 clientes, **5% equivale a ~1 baja; tuviste 2**. La diferencia es un solo cliente.
- Con una muestra tan pequeña, el dato es muy ruidoso. Un intervalo de confianza razonable va de ~1% a ~29%, así que no puedes concluir que haya empeorado ni que esté bien.
- Aun así, perder 2 de 22 puede ser un golpe real de ingresos. Calcula cuánto MRR representan.

**Lo que es ruido o no (los gratuitos):**
- Un 34% mensual de bajas en free es alto, pero es común en freemium, sobre todo si hay muchos registros de prueba o curiosos.
- Su impacto directo en ingresos es nulo, pero sí afecta tu **embudo de conversión** a pago.

**Veredicto:** no es una crisis de ingresos confirmada, pero tampoco hay que ignorarla. Es una alerta amarilla por la señal de los de pago y por la salud del embudo.

## Plan

**Hoy (verificación):**
1. **Confirma qué mide tu "5%".** ¿Era churn de pago? ¿De ingresos? ¿De otro periodo? Si comparabas manzanas con naranjas, buena parte del pánico desaparece.
2. **Revisa qué cuenta como "baja" en free.** ¿Cancelación activa, borrado de cuenta o inactividad automática? Si es inactividad, es otra métrica.
3. **Identifica a los 2 clientes de pago:** antigüedad, plan, MRR, uso previo, motivo de cancelación, si hubo contacto con soporte. Contacta si puedes.

**Esta semana:**
4. **Compara con meses anteriores**, por segmento. ¿El 34% en free y el 9% en pago son nuevos o habituales?
5. **Segmenta el churn free por antigüedad de cohorte.** Si la mayoría eran registros de las últimas 2–4 semanas, es un problema de activación, no de retención.
6. **Mira la conversión free→pago** de esos 60 que se fueron: ¿habían usado funciones clave? Eso te dice cuánto potencial perdiste.

**A partir de ahora:**
7. **Cambia el panel:** reporta churn por segmento (free y pago) y churn de ingresos (MRR), no un único número global.
8. **Usa una ventana más larga para pago** (trimestral o media móvil de 3 meses), porque con 22 clientes un mes aislado engaña.
9. **Define una alerta** en términos absolutos para pago (p. ej., ≥2 bajas en un mes) en vez de solo porcentaje.

## Qué no hacer
- No lances descuentos ni cambios de producto reaccionando a un solo mes con 2 bajas.
- No uses el 31% en reportes a inversores o equipo sin explicar la composición.

Si me dices cuál era tu base del "5%" y el MRR de esos 2 clientes, afino el diagnóstico.