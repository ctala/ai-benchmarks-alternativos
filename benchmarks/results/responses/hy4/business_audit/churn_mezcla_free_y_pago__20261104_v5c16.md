# Tencent Hy4 — business_audit/churn_mezcla_free_y_pago

- model_id: `tencent/hy4`
- success: True  | final: 7.17 | quality: 8.0
- latency_total: 45.176s | tokens_per_second: 82.9
- input_tokens: 200 | output_tokens: 3743

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

Respira. **No perdiste 31% de tus clientes de pago.** Lo que cambió (o estuvo mal desde el principio) es el denominador. Antes de interpretar cualquier churn, verifico qué población entró en la cuenta — y aquí entraron todos, incluidos los gratuitos.

## 1. Verificación de población

El panel está midiendo:

> *"De todas las cuentas que existían al inicio de mes, ¿qué % se dio de baja?"* → 62 / 200 = **31%**

No está midiendo churn de clientes ni churn de ingresos. Tu 5% casi con certeza era **churn de pago** (o de revenue, o de una cohorte distinta). Estás comparando dos poblaciones diferentes: 200 cuentas mixtas contra 22 cuentas de pago. Esa comparación es inválida, no una degradación del negocio.

## 2. Los números correctos

| Segmento | Base inicio | Bajas | Tasa real | Aporte al 31% |
|---|---:|---:|---:|---:|
| Gratuito | 178 | 60 | **33,7%** | 30,0 pp |
| De pago | 22 | 2 | **9,1%** | 1,0 pp |
| **Agregado (lo que ves)** | **200** | **62** | **31,0%** | **31,0 pp** |

**El 96,8% del churn reportado (60 de 62) viene del plan gratuito.** El segmento de pago aporta solo 1 punto porcentual al número que te asustó.

## 3. Qué tan grave es, por dimensión

| Dimensión | Gravedad | Por qué |
|---|---|---|
| **Gobierno de la métrica** | 🔴 Alta | Un KPI mal etiquetado casi dispara una decisión de crisis. Esto es lo más urgente. |
| **Ingresos / MRR** | 🟡 Bajo–modesto, *pendiente de validar* | 2 de 22 = 9,1% de logo churn, por encima de tu 5%, pero con n=22 **una sola cuenta mueve la tasa 4,5 pp**. Es ruido estadístico tanto como señal: ni pánico ni ignorarlo. Falta el ARPU de esas 2 cuentas para saber el revenue churn real. |
| **Crecimiento / embudo** | 🟠 Potencialmente alta | 60/178 en free es la señal de fondo. Si nunca activaron, es un problema de **activación**, no de retención. Si eran activos, es valor percibido. Si son bots/limpieza, es suciedad de datos. |

## 4. Plan (ordenado, con tiempos)

**Paso 0 — Hoy, 10 min.** Congela cualquier comunicación de crisis, cambio de pricing o reunión de "emergencia de churn" basada en el 31%.

**Paso 1 — Hoy: redefinir antes de interpretar.** Pide a datos la definición exacta del panel y reconstruye tres métricas separadas:
- `logo_churn_pago` = 2/22 = 9,1% ← **tu KPI**
- `revenue_churn` = MRR perdido / MRR inicio ← requiere ARPU de las 2 bajas
- `abandono_free` = 60/178 = 33,7% ← **renómbralo**; que deje de llamarse "churn" en el dashboard ejecutivo

El 31% puede sobrevivir, pero solo como métrica operativa de "rotación de cuentas", nunca como KPI de negocio. Confirma también contra qué población se calculaba ese 5% histórico.

**Paso 2 — 24–48 h: audita los 60.** Segmenta por ¿activaron alguna vez?, antigüedad, última acción, canal, y sobre todo **¿baja voluntaria o limpieza programada / duplicados / cuentas de test?** Según el resultado: arregla onboarding, revisa cambios recientes en límites del plan free, o corrige la ingesta para que esos registros no entren al denominador.

**Paso 3 — 24–48 h: audita los 2, con pinzas.** Motivo de cancelación, tickets, tenure, ARPU, ¿eran cuentas de <30 días? Mira la serie de 3–6 meses en vez de reaccionar a un mes con n=22. Si son 2 cuentas nuevas, vuelve a ser encaje/activación, no fuga de base instalada.

**Paso 4 — Esta semana: arregla el panel.** Segmentación obligatoria por plan, **denominador impreso en cada tarjeta** ("2 de 22 cuentas de pago"), aviso de `n pequeño` cuando n<50, y control de versiones de la definición de métrica.

**Paso 5 — Mensaje al equipo/board:**
> "El 31% es rotación de todas las cuentas; el 97% corresponde al plan gratuito. El churn de pago es 9,1% (2 de 22), sensible a una sola cuenta, y estamos validando ARPU y motivo. No hay pérdida masiva de ingresos: hay un error de etiquetado del dashboard y una señal de activación en free que vamos a investigar."

## 5. Lo que NO voy a asumir (y te pido)

No tengo el ARPU de las 2 bajas, el motivo de cancelación, si los 60 free llegaron a activar, ni si hubo una limpieza de cuentas este mes. **No los invento**: son exactamente las cuatro cosas que determinan si esto es un incidente de ingresos, un problema de onboarding o solo ruido de medición. Tráelos y cerramos el diagnóstico.

Veredicto en una línea: **tu problema hoy es de definición de métrica, no de retención; el hallazgo de valor está en los 60 del plan gratuito.**