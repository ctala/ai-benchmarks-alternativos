# Qwen 3.8 Max 0902 — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 147.262s | tokens_per_second: 41.7
- input_tokens: 227 | output_tokens: 6140

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

Respira: **el 31% es real como “churn total de usuarios”, pero no significa que estés perdiendo el 31% de tu negocio de pago**. El número está siendo arrastrado por el plan gratuito.

## 1) Qué está midiendo realmente tu panel

Tu panel está calculando:

\[
\text{Churn total} = \frac{62}{200} = 31\%
\]

Pero la población está mezclada:

| Segmento | Usuarios inicio | Bajas | Churn |
|---|---:|---:|---:|
| Plan gratuito | 178 | 60 | **33.7%** |
| Plan de pago | 22 | 2 | **9.1%** |
| Total | 200 | 62 | **31.0%** |

Traducción: **96.8% de las bajas fueron gratuitas**. El blended churn de 31% está dominado por el plan gratuito.

Si tu referencia de “5%” venía del churn de clientes de pago, entonces no estabas comparando la misma población.

---

## 2) ¿Qué tan grave es?

### Lectura rápida

- **Churn total reportado: 31%** → alarmante si se interpreta como churn de negocio, pero probablemente engañoso porque incluye gratuitos.
- **Churn gratuito: 33.7%** → puede ser grave o normal dependiendo de qué rol cumple el free plan en tu funnel.
- **Churn pagado: 9.1%** → este es el número que probablemente te importa si tu negocio depende de ingresos recurrentes.

### El churn pagado sí merece atención

Pasaste de una expectativa de ~5% a **9.1% mensual**. Eso es casi el doble. Pero hay una advertencia importante:

Tu base de pago es pequeña: **22 usuarios**.

Con 22 usuarios de pago:

- 1 baja = 4.5% de churn
- 2 bajas = 9.1%
- 3 bajas = 13.6%

Es decir, **una sola cuenta puede mover mucho la métrica**. No puedes concluir todavía que tu churn pagado estructural subió a 9%, pero sí debes investigarlo ya.

Si esas 2 bajas son de alto valor económico o estratégicas, la gravedad sube. Si eran cuentas pequeñas, de prueba, duplicadas o no relevantes, la gravedad baja.

---

## 3) Diagnóstico inmediato

### A. Verifica si el 31% es un problema de definición

Pregúntate:

1. **¿El panel incluye usuarios gratuitos?**  
   Sí. Y eso está inflando el churn.

2. **¿Las 62 bajas son cancelaciones reales?**  
   Podrían ser:
   - usuarios gratuitos que nunca activaron,
   - pruebas,
   - cuentas inactivas eliminadas,
   - expiración de trial,
   - duplicados,
   - bots,
   - limpieza de base de datos.

3. **¿Estás midiendo usuarios o cuentas?**  
   Si los 22 “usuarios de pago” son asientos dentro de una misma cuenta, quizás cancelaron 2 asientos pero no se perdió la cuenta completa. Eso cambiaría la lectura.

4. **¿El denominador está bien?**  
   ¿Los 200 usuarios de inicio de mes eran realmente activos? ¿O incluía cuentas suspendidas, free churned antiguos o cuentas de prueba?

5. **¿Hubo un evento puntual este mes?**  
   Por ejemplo: una purga masiva de gratuitos, cambio de pricing, caída de pagos, cambio en producto, campaña que trajo usuarios de baja calidad, etc.

---

## 4) Plan de acción inmediato

### Hoy / próximas 24 horas

#### 1. Congela la interpretación del 31%

No tomes decisiones estratégicas con ese número sin segmentar.

Comunica internamente algo como:

> “El churn total de 31% incluye plan gratuito. El churn de usuarios de pago fue 9.1% este mes. Estamos validando si las bajas gratuitas corresponden a churn real o a limpieza/expiración de cuentas free. El foco de negocio debe estar en churn pagado y MRR churn.”

#### 2. Separa las métricas

Crea al menos estas tres vistas:

| Métrica | Fórmula | Para qué sirve |
|---|---|---|
| Churn de usuarios gratuitos | bajas free / usuarios free inicio | Entender salud del funnel/free plan |
| Churn de usuarios de pago | bajas paid / usuarios paid inicio | Entender retención de clientes |
| Churn de ingresos / MRR churn | MRR perdido / MRR inicio | Entender impacto real en negocio |

Si tu negocio cobra, tu métrica principal no debería ser “churn total de usuarios”, sino **churn de ingresos** o **net revenue retention**.

---

### Próximos 2–3 días

#### 3. Haz una autopsia de las 2 bajas de pago

Con tan poca base, cada baja pagada debe investigarse individualmente.

Para cada una, revisa:

- Nombre / cuenta / plan / MRR.
- Fecha de cancelación.
- Motivo declarado.
- ¿Fue voluntaria o involuntaria?
- ¿Hubo fallo de tarjeta/pago?
- ¿Tenían tickets de soporte?
- ¿Bajó su uso antes de cancelar?
- ¿Canceló toda la cuenta o solo un usuario/asiento?
- ¿Era una cuenta de prueba, duplicada o interna?
- ¿El cliente podría recuperarse con downgrade, pausa, descuento o cambio de plan?

Acción inmediata:

- Contacta personalmente a esos 2 clientes.
- Si fue fallo de pago, activa recuperación de pago/dunning.
- Si fue problema de producto, registra el bug o fricción.
- Si fue precio/valor, evalúa si necesitas mejor comunicación de valor, downgrade o save offer.

#### 4. Revisa las 60 bajas gratuitas

No todas las bajas gratuitas son igualmente graves.

Clasifícalas:

| Tipo de baja gratuita | Interpretación |
|---|---|
| Usuarios que nunca activaron | Problema de onboarding/adquisición |
| Usuarios que probaron y no vieron valor | Problema de activación |
| Usuarios inactivos eliminados | Puede ser limpieza, no churn real |
| Trial expirado | Debe medirse como conversión/expiración, no necesariamente churn |
- Usuarios que venían de campañas de baja calidad | Problema de targeting |
| Usuarios que no pueden pagar | Posible oportunidad de plan más barato/free |

Para diagnosticar, segmenta por:

- fecha de registro,
- fuente de adquisición,
- si completaron onboarding,
- si usaron la función principal,
- días activos,
- última actividad,
- plan al que intentaban acceder,
- país/dispositivo/canal.

Si descubres que las 60 bajas gratuitas fueron una limpieza masiva o cuentas inactivas, el 31% pierde gravedad inmediatamente.

---

## 5) Cómo saber si el churn pagado realmente empeoró

Tu expectativa era 5%. Con 22 clientes de pago, el cálculo es inestable.

Escenarios:

| Bajas pagadas | Churn pagado |
|---:|---:|
| 0 | 0% |
| 1 | 4.5% |
| 2 | 9.1% |
| 3 | 13.6% |

Es decir, estás a **una sola baja** de parecer “normal” o “preocupante”.

Por eso, con bases pequeñas, no mires solo el churn mensual aislado. Usa:

- churn pagado móvil de 3 meses,
- número absoluto de bajas pagadas,
- MRR perdido,
- MRR recuperado,
- net revenue retention,
- retención por cohorte.

Ejemplo:

> “Este mes perdimos 2 clientes de pago sobre 22. Son 9.1%, pero por el tamaño de la base la métrica es volátil. Vamos a evaluarlo sobre ventana de 3 meses y por MRR perdido.”

---

## 6) Qué métricas deberías usar de ahora en adelante

### Si tu objetivo es ingresos

Usa:

#### Churn de MRR

\[
\text{MRR churn} = \frac{\text{MRR perdido por cancelaciones}}{\text{MRR al inicio del mes}}
\]

Ejemplo: si tus 2 clientes cancelados representaban el 20% del MRR, el problema es mucho más grave que si representaban el 2%.

#### Net Revenue Retention

\[
NRR = \frac{\text{MRR inicial} - \text{MRR perdido} - \text{downgrades} + \text{expansión}}{\text{MRR inicial}}
\]

Si tienes expansión, upsells o upgrades, puedes perder clientes pero aún así retener ingresos.

### Si tu objetivo es crecimiento de producto

Usa:

- activación,
- retención por cohorte,
- free-to-paid conversion,
- churn gratuito,
- tiempo hasta primer valor,
- uso semanal/mensual.

---

## 7) Plan concreto de 7 días

### Día 1

- [ ] Confirmar si el 31% incluye gratuitos.
- [ ] Calcular churn pagado: 2/22 = 9.1%.
- [ ] Calcular churn gratuito: 60/178 = 33.7%.
- [ ] Verificar si hubo limpieza masiva, purga, cambio de plan o error de tracking.
- [ ] Revisar si las bajas son usuarios, cuentas o asientos.

### Día 2

- [ ] Identificar las 2 cuentas pagadas canceladas.
- [ ] Revisar MRR perdido.
- [ ] Contactar a esas cuentas.
- [ ] Clasificar motivo: precio, producto, soporte, pago, falta de uso, error, competencia.

### Día 3

- [ ] Revisar si alguna de las 2 bajas fue involuntaria por pago fallido.
- [ ] Activar flujo de recuperación de pagos si aplica.
- [ ] Revisar si hay más clientes de pago con riesgo: bajo uso, tickets abiertos, fallo de tarjeta, renovación cercana.

### Días 4–5

- [ ] Analizar las 60 bajas gratuitas por cohorte y fuente.
- [ ] Determinar si son churn real, trial expiration, inactividad o limpieza.
- [ ] Si son usuarios que nunca activaron, investigar onboarding.
- [ ] Si son usuarios que probaron y se fueron, revisar propuesta de valor.

### Día 6–7

- [ ] Crear dashboard separado: free churn, paid churn, MRR churn.
- [ ] Definir alerta: por ejemplo, investigar cualquier baja pagada > X MRR o cualquier mes con >1 baja pagada.
- [ ] Preparar informe ejecutivo con la versión correcta.

---

## 8) Mensaje recomendado para tu equipo o jefatura

Puedes decir:

> “El churn reportado de 31% corresponde a la base total de usuarios, incluyendo el plan gratuito. Las bajas gratuitas explican casi todo ese número: 60 de 62.  
>   
> El churn de usuarios de pago fue 9.1%: 2 bajas sobre 22 clientes. Es un número a investigar porque supera nuestra referencia de 5%, pero la base es pequeña y una sola baja mueve la métrica 4.5 puntos.  
>   
> Vamos a validar si las bajas gratuitas son churn real o expiración/limpieza de cuentas free, y vamos a analizar las 2 bajas pagadas por MRR, motivo y posibilidad de recuperación.  
>   
> De ahora en adelante vamos a separar churn gratuito, churn pagado y churn de ingresos para evitar interpretaciones erróneas.”

---

## 9) Nivel de gravedad: resumen

| Métrica | Valor | Gravedad | Interpretación |
|---|---:|---|---|
| Churn total | 31% | Alta como señal de reporte, pero engañosa | Incluye gratuitos y está dominada por free |
| Churn gratuito | 33.7% | Variable | Puede ser normal si free es funnel; grave si indica mala activación |
| Churn pagado | 9.1% | Preocupante, pero muestra pequeña | Supera tu referencia de 5%; investigar ya |
| Impacto real | Depende del MRR | Crítico si esas 2 cuentas son grandes | Necesitas medir churn de ingresos |

---

## 10) Decisión rápida

Si tuviera que resumirlo en una frase:

> **No estás en pánico por un churn real del 31% de tu negocio; estás viendo un churn total contaminado por el plan gratuito. Tu número crítico es el churn pagado de 9.1%, y debes investigarlo por MRR, motivo y calidad de la base, pero sin sobrerreaccionar porque solo son 2 clientes sobre 22.**

Tu plan inmediato es: **separar free/paid, auditar las bajas, contactar a los 2 clientes de pago, calcular MRR perdido y corregir el dashboard para que el churn principal sea churn de ingresos o churn pagado, no churn total.**