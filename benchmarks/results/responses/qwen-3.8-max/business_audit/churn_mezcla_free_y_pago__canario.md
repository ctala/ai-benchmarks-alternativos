# Qwen 3.8 Max — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.95 | quality: 10.0
- latency_total: 181.782s | tokens_per_second: 47.1
- input_tokens: 227 | output_tokens: 8560

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

Respira. El 31% es matemáticamente correcto con la definición actual, pero está midiendo una población mezclada que puede exagerar el problema de negocio. Tu métrica real de riesgo, si tu ingreso viene de usuarios de pago, no es 31%: es el churn de clientes pagados.

## 1) Qué está midiendo realmente tu panel

Tu panel está calculando:

\[
\text{Churn reportado} = \frac{62 \text{ bajas}}{200 \text{ usuarios al inicio}} = 31\%
\]

Pero esa población incluye usuarios gratuitos y usuarios de pago. Eso contamina la lectura.

### Cálculo por segmento

| Segmento | Usuarios al inicio | Bajas | Churn |
|---|---:|---:|---:|
| Total | 200 | 62 | 31.0% |
| Plan gratuito | 178 | 60 | 33.7% |
| Plan de pago | 22 | 2 | 9.1% |

Entonces:

- **Churn total / blended:** 31%
- **Churn del plan gratuito:** 33.7%
- **Churn del plan de pago:** 9.1%

## 2) ¿Qué tan grave es?

### Lectura rápida

**No estás frente a un churn del 31% de tu negocio de pago.**  
Estás frente a un churn blended inflado por 60 bajas de usuarios gratuitos.

La gravedad real depende de qué estés optimizando:

### Si tu negocio depende de usuarios de pago

La métrica crítica es:

\[
\text{Churn de clientes pagados} = \frac{2}{22} = 9.1\%
\]

Eso es una **alerta seria**, pero con matices:

- Con solo 22 clientes pagos, cada cliente representa **4.5 puntos porcentuales** de churn mensual.
- 2 cancelaciones = 9.1%.
- 1 cancelación = 4.5%.
- 3 cancelaciones = 13.6%.

Es decir: la muestra es pequeña. Puede ser ruido, pero también puede ser una señal temprana. No debes ignorarlo, pero tampoco debes entrar en pánico por el 31%.

### Si el plan gratuito es parte del funnel

El churn del plan gratuito, 33.7%, puede ser normal o puede indicar un problema de activación, expectativa o calidad de adquisición. Pero no debería gobernar decisiones de ingresos si esos usuarios no pagan.

Importa si:

- Esos usuarios gratuitos luego convierten a pago.
- Tu crecimiento depende del boca a boca o comunidad.
- El plan gratuito tiene costos operativos relevantes.
- Las bajas gratuitas reflejan mala experiencia de onboarding.

Pero si son usuarios free que nunca activaron o nunca pagaron, no es una emergencia financiera.

## 3) Severidad recomendada

Yo lo clasificaría así:

| Métrica | Valor | Severidad | Interpretación |
|---|---:|---|---|
| Churn total | 31% | Baja para decisiones de negocio | Mezcla free y paid; no sirve como alarma principal |
| Churn free | 33.7% | Media/baja | Puede ser esperado; revisar funnel y activación |
| Churn paid logo | 9.1% | Media/alta | Alerta real, pero muestra pequeña |
| Churn paid por ingresos | Falta calcular | Crítico si MRR perdido es alto | Depende del valor de esas 2 cuentas |

La frase correcta para tu equipo sería:

> “El churn del panel es 31% porque incluye usuarios gratuitos. El churn de clientes de pago es 9.1%, equivalente a 2 cuentas de 22. No es un incendio del 31%, pero sí es una alerta de retención que debemos investigar hoy.”

## 4) Lo primero que debes validar antes de actuar

Como analista de retención, yo no interpretaría el 31% sin antes verificar estas definiciones.

### A. ¿Qué significa “baja”?

Pregunta clave:

- ¿Son cancelaciones efectivas?
- ¿Son solicitudes de cancelación que aún no se ejecutan?
- ¿Son usuarios que perdieron acceso por impago?
- ¿Son trials que expiraron?
- ¿Son cuentas duplicadas, bots o cuentas de prueba?
- ¿Son downgrades de pago a gratuito?
- ¿Son usuarios gratuitos que simplemente eliminaron cuenta?

Si “baja” incluye trials vencidos o cuentas free inactivas, el churn está inflado.

### B. ¿Cuál es el denominador correcto?

Si quieres medir churn de negocio, el denominador debería ser:

- Clientes de pago al inicio del periodo, o
- Usuarios de pago activos, o
- Cuentas de pago, si una cuenta puede tener varios usuarios/asientos.

No todos los usuarios totales.

### C. ¿Las 2 bajas pagadas son realmente cancelaciones?

Necesitas identificarlas una por una:

- ¿Quién es el cliente?
- ¿Cuánto pagaba?
- ¿Cuándo empezó?
- ¿Cuál fue el motivo?
- ¿Abrió tickets?
- ¿Usó el producto recientemente?
- ¿Falló el pago?
- ¿Canceló por precio, falta de feature, competencia, mal onboarding o cambio de prioridades?
- ¿Se fue a free o se fue completamente?
- ¿Es una cancelación voluntaria o involuntaria?

Con 22 clientes pagos, cada cuenta debe investigarse manualmente.

### D. ¿Cuál es el churn de ingresos?

El churn de clientes pagados es 9.1%, pero el churn de ingresos puede ser mayor o menor.

Fórmula:

\[
\text{Revenue churn} = \frac{\text{MRR perdido por cancelaciones}}{\text{MRR al inicio del mes}}
\]

Ejemplo simple:

- Si tenías 22 clientes pagando $100 cada uno: MRR inicial = $2,200.
- Si perdiste 2 clientes de $100: MRR perdido = $200.
- Revenue churn = 200 / 2,200 = 9.1%.

Pero si una de las cuentas pagaba $500 y otra $100:

- MRR perdido = $600.
- MRR inicial podría ser mucho mayor.
- El churn de ingresos podría ser más alto que el churn de clientes.

Por eso necesitas calcular:

- MRR perdido.
- MRR inicial.
- MRR expandido por upgrades.
- MRR recuperado por reactivaciones.
- Net Revenue Retention.

## 5) Plan inmediato

Te dejo un plan por fases.

---

# Plan 0-24 horas: contener y verificar

## 1. No tomes decisiones con el 31%

No pauses campañas, no cambies pricing, no anuncies crisis interna y no reestructures el producto por ese número sin antes segmentar.

## 2. Recalcula las métricas clave

Debes presentar esto:

- Churn total: 31%
- Churn free: 33.7%
- Churn paid: 9.1%
- Número de clientes pagos perdidos: 2
- MRR perdido: pendiente de calcular
- MRR inicial: pendiente de calcular
- Revenue churn: pendiente de calcular

## 3. Identifica las 2 cuentas pagadas

Haz una mini tabla:

| Cliente | Plan | MRR | Antigüedad | Último uso | Motivo | Tipo de baja | Acción |
|---|---|---:|---|---|---|---|---|
| Cliente A |  |  |  |  |  |  |  |
| Cliente B |  |  |  |  |  |  |  |

## 4. Clasifica cada baja

Para cada cuenta pagada, define si fue:

- Cancelación voluntaria.
- Cancelación por impago.
- Downgrade a free.
- Cambio de plan.
- Fin de trial pagado.
- Cuenta de prueba.
- Duplicado.
- Error de datos.

Si una de las dos no fue churn real, tu número baja inmediatamente.

## 5. Contacta a las cuentas pagadas hoy

Con 22 clientes pagos, esto no se resuelve solo con dashboards. Hay que hablar con ellos.

Mensaje posible:

> “Hola, vi que recientemente cancelaron el servicio. Quería entender si hubo algo que no funcionó para ustedes y si hay algo que podamos corregir. También quiero asegurarme de que no haya quedado ningún problema de facturación o acceso.”

Objetivo:

- Entender motivo.
- Detectar si fue error de pago.
- Detectar si fue problema de onboarding.
- Detectar si fue falta de valor.
- Ofrecer una opción de recuperación si tiene sentido.

---

# Plan 24-72 horas: diagnóstico profundo

## 1. Analiza las causas de las 2 cancelaciones pagadas

Posibles causas:

- Precio.
- Falta de uso.
- Mal onboarding.
- No entendieron el valor.
- Feature faltante.
- Competencia.
- Soporte lento.
- Problema técnico.
- Cambio de presupuesto.
- Compra equivocada.
- Expectativa incorrecta desde ventas/marketing.

Con 2 cuentas no puedes sacar una conclusión estadística sólida, pero sí puedes detectar patrones.

## 2. Revisa si fueron clientes nuevos o antiguos

Pregunta clave:

- ¿Cancelaron en los primeros 30-60 días?
- ¿Llevaban meses activos?
- ¿Nunca activaron una acción clave?
- ¿Usaban la funcionalidad principal?

Si cancelan rápido, puede ser problema de onboarding o expectativa.

Si cancelan después de meses, puede ser valor, precio, competencia o soporte.

## 3. Revisa el comportamiento de uso

Para esas 2 cuentas:

- Último login.
- Frecuencia de uso.
- Features usadas.
- Configuración completada.
- Integraciones conectadas.
- Invitaciones a otros usuarios.
- Reportes generados.
- Acciones clave de valor.

Si no hubo activación, el problema suele ser onboarding.

## 4. Revisa facturación

A veces el “churn” es en realidad dunning fallido.

Valida:

- Tarjeta rechazada.
- Pago fallido.
- Correos de cobro no abiertos.
- Factura no pagada.
- Suscripción cancelada automáticamente por el procesador de pagos.

Si fue impago, puedes recuperar con emails, actualización de tarjeta o contacto directo.

## 5. Analiza el churn gratuito por separado

Las 60 bajas gratuitas pueden ser:

- Usuarios que nunca activaron.
- Leads de mala calidad.
- Cuentas creadas por error.
- Pruebas.
- Usuarios que solo querían probar.
- Limpieza de cuentas inactivas.
- Cancelación después de una campaña específica.

Si el free churn viene de una campaña concreta, revisa:

- Fuente de adquisición.
- Intención del usuario.
- Mensaje del anuncio o landing.
- Nivel de activación.
- Tiempo entre registro y baja.

---

# Plan 1 semana: corregir la medición

## 1. Define claramente qué es churn

Te sugiero una definición simple y documentada:

> Churn de clientes pagados = cuentas de pago activas al inicio del periodo que cancelan o no renuevan durante el periodo, excluyendo trials, cuentas gratuitas, cuentas de prueba y duplicados.

## 2. Separa dashboards

Tu dashboard debería mostrar, como mínimo:

- Usuarios totales.
- Usuarios free.
- Usuarios paid.
- Churn free.
- Churn paid.
- Churn de ingresos.
- MRR perdido.
- MRR recuperado.
- MRR expandido.
- Net Revenue Retention.
- Churn voluntario.
- Churn involuntario.
- Churn por cohorte.
- Churn por antigüedad.
- Churn por plan.
- Churn por canal de adquisición.

## 3. Cambia la métrica principal

Si tu negocio es de pago, tu métrica principal no debería ser:

> Churn total de usuarios.

Debería ser:

> Churn de clientes pagados y churn de ingresos.

Y si quieres una métrica más completa:

> Net Revenue Retention.

## 4. Usa promedios móviles

Con 22 clientes pagos, un mes puede variar mucho.

En lugar de mirar solo:

- Churn mensual = 9.1%

Mira también:

- Churn promedio de 3 meses.
- Churn por cohorte.
- Churn acumulado de cuentas nuevas.
- Churn de cuentas con más de 90 días.

Ejemplo:

| Periodo | Clientes pagos inicio | Cancelaciones | Churn |
|---|---:|---:|---:|
| Mes actual | 22 | 2 | 9.1% |
| Promedio 3 meses | por calcular | por calcular | por calcular |

---

# Plan 2-4 semanas: reducir churn real

## 1. Crea un proceso de salvamento para cuentas pagadas

Para cada cancelación pagada:

1. Detectar cancelación en menos de 24 horas.
2. Contactar personalmente.
3. Registrar motivo.
4. Ofrecer solución si aplica.
5. Medir tasa de recuperación.

Opciones de salvamento:

- Pausa temporal.
- Descuento puntual si el problema es precio.
- Cambio de plan.
- Sesión de onboarding.
- Corrección técnica.
- Extensión gratuita por molestia.
- Acompañamiento para configurar el producto.

No ofrezcas descuento automáticamente sin entender el motivo.

## 2. Mejora onboarding

Si los clientes cancelan pronto, revisa:

- Primera experiencia.
- Tiempo hasta valor.
- Configuración inicial.
- Activación de feature principal.
- Emails de bienvenida.
- Llamada o demo inicial.
- Checklist de activación.
- Alertas de cuentas sin uso.

Meta sugerida:

> Que el cliente experimente el valor principal del producto en los primeros 7 días.

## 3. Crea señales de riesgo

Con 22 cuentas puedes hacer seguimiento manual, pero necesitas sistema.

Señales de alerta:

- No login en 7/14 días.
- No uso de feature clave.
- Tickets de soporte negativos.
- Error de pago.
- Bajón repentino de uso.
- Eliminación de usuarios.
- Solicitud de exportar datos.
- Pregunta por cancelación.

## 4. Implementa encuesta de cancelación

Cuando alguien cancele, captura:

- Motivo principal.
- Qué faltó.
- Qué herramienta usarán ahora.
- Si fue precio, valor, soporte, usabilidad o timing.
- Si estarían dispuestos a volver bajo ciertas condiciones.

Con pocas cuentas, cada respuesta vale oro.

---

# Plan para el plan gratuito

No lo ignores, pero no lo mezcles con la salud financiera.

Preguntas:

- ¿Los usuarios gratuitos activan?
- ¿Cuánto tardan en bajar?
- ¿Vienen de algún canal específico?
- ¿Entienden el valor del producto?
- ¿Hay fricción en registro?
- ¿Están llegando usuarios equivocados?
- ¿El free plan está generando cuentas basura?
- ¿Deberías pedir tarjeta para trial?
- ¿Deberías limitar features o tiempo?

Métricas free:

- Registros.
- Activación.
- Uso semanal.
- Conversión free a paid.
- Tiempo a conversión.
- Churn free.
- Cuentas free que nunca usaron el producto.

Si el free plan no convierte, puede ser un problema de funnel, no de churn de negocio.

---

## 6) Mensaje listo para enviar a tu equipo o jefe

Puedes usar algo así:

> “El churn reportado del 31% está calculado sobre todos los usuarios, incluyendo el plan gratuito. Al segmentar, vemos que 60 de las 62 bajas corresponden a usuarios gratuitos. El churn de clientes de pago es 9.1%: 2 cancelaciones sobre 22 cuentas pagas.  
>   
> Este 9.1% es una alerta real, pero la muestra es pequeña y cada cuenta representa 4.5 puntos porcentuales. Estamos validando si esas 2 cancelaciones son churn real, impago, downgrade o error de medición. También estamos calculando el impacto en MRR.  
>   
> Próximo paso: contactar a las 2 cuentas pagadas, confirmar motivo, corregir la definición del dashboard y separar churn free, paid y revenue churn.”

---

## 7) Qué no hacer

No hagas esto:

1. No digas “perdimos el 31% de nuestros clientes” si la mayoría eran free.
2. No cambies pricing por pánico.
3. No pauses adquisición sin entender si el problema es free o paid.
4. No borres usuarios free del análisis, pero sepáralos.
5. No ignores las 2 cancelaciones pagadas.
6. No uses un solo mes como tendencia con solo 22 clientes pagos.
7. No mezcles trial, free, paid, downgrade e impago en la misma métrica.

---

## 8) Qué sí hacer hoy

Tu checklist inmediato:

- [ ] Confirmar que 62/200 = 31% es churn blended.
- [ ] Calcular churn free: 60/178 = 33.7%.
- [ ] Calcular churn paid: 2/22 = 9.1%.
- [ ] Identificar las 2 cuentas pagadas canceladas.
- [ ] Verificar si fueron cancelaciones reales.
- [ ] Verificar si hubo impago.
- [ ] Verificar si fueron downgrade a free.
- [ ] Calcular MRR perdido.
- [ ] Contactar a las 2 cuentas.
- [ ] Corregir el dashboard para separar free y paid.
- [ ] Comunicar el hallazgo con calma.

---

## Conclusión

No estás en un churn del 31% de tu negocio principal. Estás viendo una métrica mezclada.

La lectura correcta es:

- **Churn total reportado:** 31%, pero contaminado por usuarios gratuitos.
- **Churn gratuito:** 33.7%, relevante para funnel/activación, pero no necesariamente para ingresos.
- **Churn pagado:** 9.1%, que sí es una alerta real.
- **Gravedad:** media/alta en clientes pagados, pero con muestra pequeña.
- **Acción inmediata:** investigar manualmente esas 2 cuentas pagadas y corregir la definición del dashboard.

Tu prioridad hoy no es entrar en pánico por el 31%. Es separar la población correcta, proteger el ingreso y entender si esas 2 cancelaciones pagadas son un caso aislado o el inicio de un problema.