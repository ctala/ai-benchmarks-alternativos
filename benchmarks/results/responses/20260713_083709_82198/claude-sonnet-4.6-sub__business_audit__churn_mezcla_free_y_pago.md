# Claude Sonnet 4.6 (suscripción) — business_audit/churn_mezcla_free_y_pago

- model_id: `claude-sonnet-4-6`
- success: True  | final: 6.13 | quality: 7.2
- latency_total: 48.82s | tokens_per_second: 35.8
- input_tokens: 3 | output_tokens: 1748

## Respuesta completa

## Para. Tu plataforma está midiendo la población equivocada.

El 31% mezcla usuarios gratuitos y de pago en un solo denominador. Eso distorsiona todo.

---

## Qué está midiendo realmente el panel

| Métrica | Cálculo | Resultado |
|---|---|---|
| Churn total (lo que reporta el panel) | 62 / 200 | **31%** ← población mezclada |
| Churn de usuarios gratuitos | 60 / 178 | **33.7%** |
| Churn de usuarios de pago | 2 / 22 | **9.1%** |

El panel trata igual a alguien que nunca pagó y a alguien que te generaba ingresos. Eso no es un KPI de retención — es un conteo de cuentas.

---

## Diagnóstico real

**Churn de pago: 9.1% mensual**

Esto es lo único que le importa a tu negocio hoy. Es alto (anualizado ronda el 66%), pero manejable si actúas ahora. Y es muy distinto a 31%.

**El 5% que esperabas** — ¿de dónde salía ese número? Si era churn de pago histórico, entonces sí hay deterioro real: de 5% → 9.1% es casi el doble y merece atención. Si era churn total histórico calculado diferente, la comparación no es válida.

**Churn gratuito: 33.7%**

Esperable en muchos modelos freemium. Usuarios que se registraron y nunca activaron, o que exploraron y salieron. Sin impacto en revenue directo. Puede ser señal de problema de activación, pero no es la urgencia del día.

---

## Plan concreto

**Esta semana — los 2 usuarios de pago que se fueron**

Con 22 usuarios de pago, cada uno representa ~4.5% de tu base. Necesitas entender por qué se fueron.

1. Contacta a ambos directamente. No encuesta — conversación real. Pregunta qué faltó, qué los hizo decidir salir.
2. Revisa su historial: ¿usaban el producto activamente antes de irse? ¿Hubo algún evento (precio, feature, soporte) que coincida con la baja?

**Esta semana — corrige cómo mides**

Configura o calcula manualmente estas tres métricas separadas:

- **Churn de pago mensual** = bajas de pago / total de pago a inicio de mes
- **Revenue churn** = MRR perdido por bajas / MRR total a inicio de mes (si tienes distintos planes, esto es más preciso que contar cuentas)
- **Churn gratuito** = lo monitoreas, pero por separado y con mucho menos urgencia

**Este mes — entiende el 33.7% gratuito**

No para alarmarte, sino para diagnosticar:
- ¿Qué porcentaje de los 60 que se fueron jamás hizo la acción clave del producto (publicar, integrar, completar el onboarding)?
- Si la mayoría nunca activó, el problema es activación, no retención.
- Si activaron y se fueron igual, hay un problema de valor percibido que vale investigar.

---

## Conclusión directa

**El 31% es una métrica rota.** No porque estés bien — 9.1% de churn pagado mensual es un número que hay que bajar. Sino porque mezclar poblaciones te llevaría a tomar decisiones equivocadas (descuentos masivos a gratuitos, features para usuarios inactivos) mientras el problema real está en entender por qué se fueron esos 2 usuarios de pago.

Empieza por hablar con ellos.