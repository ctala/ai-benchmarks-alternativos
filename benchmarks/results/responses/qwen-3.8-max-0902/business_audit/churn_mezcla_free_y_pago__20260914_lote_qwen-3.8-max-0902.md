# Qwen 3.8 Max 0902 — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 8.03 | quality: 10.0
- latency_total: 147.801s | tokens_per_second: 38.3
- input_tokens: 227 | output_tokens: 5668

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

Respira. El 31% **no significa necesariamente que tu negocio esté perdiendo el 31% de sus clientes de pago**. Lo que pasó es que el panel está midiendo una población distinta a la que tú tenías en la cabeza.

## 1) Diagnóstico rápido: ¿qué está midiendo realmente ese 31%?

Tu panel está calculando:

\[
\text{Churn reportado} = \frac{62}{200} = 31\%
\]

Eso es correcto **si la población medida son todos los usuarios**, gratuitos y de pago.

Pero tu negocio probablemente no debería evaluar riesgo igualando usuarios gratuitos con usuarios pagos.

### Desglose correcto

| Segmento | Usuarios inicio | Bajas | Churn |
|---|---:|---:|---:|
| Total | 200 | 62 | 31.0% |
| Plan gratuito | 178 | 60 | 33.7% |
| Plan pago | 22 | 2 | 9.1% |

Entonces:

- **Churn total reportado:** 31%
- **Churn de usuarios gratuitos:** 33.7%
- **Churn de usuarios pagos:** 9.1%

El 31% viene casi completamente explicado por bajas del plan gratuito.

---

# ¿Qué tan grave es?

## Respuesta corta

**No es tan grave como parece si tu métrica crítica son clientes pagos, pero sí merece investigación.**

El 31% es alarmante como titular, pero no es la métrica correcta para evaluar salud de ingresos si tienes un plan gratuito.

La métrica que más importa inicialmente es:

\[
\text{Paid churn} = \frac{2}{22} = 9.1\%
\]

Eso está por encima del 5% que pensabas, pero con una base de solo 22 clientes pagos, la muestra es muy pequeña.

Con 22 clientes pagos:

- 1 baja = 4.5% de churn
- 2 bajas = 9.1% de churn
- 3 bajas = 13.6% de churn

Entonces, un solo cliente adicional puede mover mucho la métrica. No puedes entrar en pánico por un mes con 2 bajas pagas, pero tampoco ignorarlo.

---

# Interpretación correcta

## El 31% probablemente no es una catástrofe de ingresos

Si tu modelo depende de usuarios pagos, el número relevante no es el churn total, sino el churn de pago o el churn de ingresos.

El 31% te dice:

> “El 31% de todas las cuentas registradas al inicio del mes se dieron de baja.”

Pero no te dice:

> “El 31% de mis clientes pagos se fue.”

Ni tampoco:

> “El 31% de mis ingresos se perdió.”

Esas son métricas distintas.

---

## El problema real puede ser de definición

Probablemente antes estabas mirando una métrica parecida a:

\[
\text{Churn de clientes pagos}
\]

y ahora el panel está mostrando:

\[
\text{Churn de todos los usuarios}
\]

Eso genera exactamente este tipo de susto.

---

## Pero el churn gratuito sí importa

Las 60 bajas gratuitas pueden ser graves si:

1. Esos usuarios eran leads calificados.
2. Eran usuarios activos.
3. Estaban cerca de convertir a pago.
4. Vienen de una campaña de adquisición reciente.
5. Hay un problema de onboarding.
6. Hay un cambio reciente en producto, precio o comunicación.
7. Hay un error técnico o de registro.

Si los 60 usuarios gratuitos nunca activaron, nunca usaron el producto o eran cuentas de baja calidad, entonces puede ser menos grave.

Pero si eran usuarios activos o con potencial de conversión, tienes un problema de funnel.

---

# Plan de acción

## Fase 1: Hoy mismo, detén el pánico y valida la métrica

### 1. Separa el churn en tres métricas

Tu dashboard debería mostrar, como mínimo:

| Métrica | Fórmula |
|---|---|
| Churn total | Bajas totales / usuarios totales inicio |
| Churn gratuito | Bajas gratuitas / usuarios gratuitos inicio |
| Churn pago | Bajas pagas / usuarios pagos inicio |
| Churn de ingresos | MRR perdido / MRR inicio |

No vuelvas a tomar decisiones con un único churn mezclado.

---

### 2. Verifica si las 62 bajas son bajas reales

Exporta la tabla y revisa:

- `user_id`
- plan al inicio del mes
- plan al final del mes
- fecha de alta
- fecha de baja
- motivo de baja
- último inicio de sesión
- último evento de actividad
- fuente de adquisición
- estado de pago
- si era trial, free o pago
- si la cuenta era duplicada, de prueba o bot

Preguntas clave:

- ¿Las 62 bajas fueron cancelaciones voluntarias?
- ¿Alguna fue por impago?
- ¿Alguna fue por cambio de plan, no por baja real?
- ¿Se dieron de baja usuarios que en realidad nunca activaron?
- ¿Hubo una limpieza masiva de cuentas inactivas?
- ¿Hubo un cambio en la definición de “baja” en el sistema?
- ¿El panel empezó a incluir usuarios gratuitos que antes no incluía?

---

### 3. Confirma si el panel cambió de definición

Pregunta a producto, datos o ingeniería:

> “¿El churn de este mes cambió de definición? ¿Antes medía solo usuarios pagos y ahora mide todos los usuarios?”

Si la respuesta es sí, el problema principal puede ser de reporting, no de negocio.

---

## Fase 2: Próximas 24-48 horas, investiga las 60 bajas gratuitas

No mires solo el número. Tienes que entender quiénes eran esos usuarios.

### Segmenta las 60 bajas gratuitas por:

1. **Fecha de registro**
   - ¿Son usuarios nuevos o antiguos?
   - ¿Se registraron este mes o vienen de meses anteriores?

2. **Activación**
   - ¿Entraron alguna vez?
   - ¿Completaron onboarding?
   - ¿Usaron la función principal?
   - ¿Invitaron a alguien?
   - ¿Crearon contenido/proyecto/registro?

3. **Fuente de adquisición**
   - ¿Vienen de una campaña específica?
   - ¿Vienen de una alianza?
   - ¿Vienen de tráfico orgánico?
   - ¿Hay una fuente con mala calidad?

4. **Comportamiento previo**
   - ¿Estuvieron activos en los últimos 7 días?
   - ¿Recibieron emails?
   - ¿Hicieron clic en algo?
   - ¿Llegaron a algún momento de valor?

5. **Motivo de baja**
   - Si hay encuesta de cancelación, revísala.
   - Si no hay motivo, implementa una pregunta simple al cancelar.

---

### Hipótesis posibles para el churn gratuito

| Hipótesis | Señal |
|---|---|
| Usuarios nunca activaron | Bajas con cero actividad |
| Campaña de baja calidad | Muchas bajas desde una misma fuente |
| Onboarding confuso | Usuarios se registran pero no completan primer paso |
| Trial/free plan mal comunicado | Usuarios esperaban algo que no era |
| Cambio reciente en producto | Bajas concentradas después de un release |
| Error técnico | Usuarios que intentaron usar una función y falló |
| Limpieza de cuentas inactivas | Bajas antiguas procesadas este mes |
| Usuarios falsos/bots | Cuentas sin comportamiento real |

---

## Fase 3: Investiga las 2 bajas pagas con lupa

Con 22 clientes pagos, 2 bajas son importantes, pero no conclusivas.

Para cada cliente pago que canceló, revisa:

- ¿Quién era?
- ¿Cuánto pagaba?
- ¿Cuánto MRR representaba?
- ¿Cuánto tiempo llevaba como cliente?
- ¿Usaba el producto?
- ¿Tuvo tickets de soporte?
- ¿Reportó errores?
- ¿Canceló voluntariamente o fue por impago?
- ¿Habló con alguien antes de cancelar?
- ¿Hay posibilidad de recuperarlo?

Si puedes, contacta personalmente a esos 2 clientes.

Mensaje simple:

> “Hola, vi que cancelaste tu suscripción. Estoy revisando qué podemos mejorar. ¿Te importaría decirme cuál fue el motivo principal? No es una llamada de venta, solo quiero entender qué falló.”

Con 22 clientes pagos, cada baja debe ser casi una entrevista.

---

# Métricas que debes calcular ya

## 1. Churn de clientes pagos

\[
\frac{2}{22} = 9.1\%
\]

## 2. Churn de usuarios gratuitos

\[
\frac{60}{178} = 33.7\%
\]

## 3. Churn total

\[
\frac{62}{200} = 31.0\%
\]

## 4. Churn de ingresos

Necesitas MRR.

Fórmula:

\[
\text{Revenue churn} = \frac{\text{MRR perdido por cancelaciones}}{\text{MRR al inicio del mes}}
\]

Ejemplo:

Si esos 2 clientes pagos representaban 200 de 2,000 de MRR:

\[
\frac{200}{2000} = 10\%
\]

Si representaban 50 de 2,000:

\[
\frac{50}{2000} = 2.5\%
\]

Por eso no basta con contar clientes. Necesitas contar ingresos.

---

# ¿Deberías preocuparte por el 5% anterior?

Depende.

Si antes decías “estoy en 5%” pero ese 5% era solo churn pago, entonces no estás comparando lo mismo.

Ahora tienes:

- 31% total
- 9.1% pago
- 33.7% gratuito

Si tu objetivo era 5% de churn pago, entonces sí estás por encima. Pero con 22 clientes, la variabilidad es alta.

No puedes concluir que tu churn pago estructural es 9% por un solo mes con 2 bajas. Necesitas ver tendencia.

---

# Cómo comunicar esto internamente

No digas:

> “Perdimos el 31% de nuestros clientes.”

Di:

> “El panel está mostrando un churn del 31% porque incluye usuarios gratuitos y pagos. De las 62 bajas, 60 fueron gratuitas y 2 pagas. El churn de usuarios pagos fue 9.1%, pero la base paga es pequeña. Estamos investigando si las bajas gratuitas corresponden a usuarios no activados, a una campaña específica o a un cambio reciente. El impacto en ingresos depende del MRR perdido, que estamos calculando.”

Eso baja el pánico y pone la conversación en el lugar correcto.

---

# Plan concreto

## Hoy

1. **No tomes decisiones drásticas con el 31%.**
2. Exporta la tabla cruda.
3. Valida que 62 bajas sean reales.
4. Separa churn gratuito, pago y total.
5. Calcula churn pago: 9.1%.
6. Calcula MRR perdido por las 2 bajas pagas.
7. Revisa si el panel cambió de definición.
8. Comunica el hallazgo correctamente.

## Próximos 2-3 días

1. Analiza las 60 bajas gratuitas por cohorte, fuente y actividad.
2. Identifica si eran usuarios activos o inactivos.
3. Revisa si hubo errores, cambios de producto o campañas nuevas.
4. Contacta a los 2 clientes pagos que cancelaron.
5. Revisa si alguna baja paga fue por problema de pago y no por decisión real.
6. Implementa o mejora la encuesta de cancelación.

## Próxima semana

1. Crea un dashboard separado:
   - Churn total
   - Churn free
   - Churn paid
   - MRR churn
   - Net Revenue Retention
2. Define cuál es tu métrica principal.
3. Si tu negocio depende de ingresos, tu métrica principal debe ser:
   - Paid churn
   - MRR churn
   - Net Revenue Retention
4. Deja el churn total como métrica secundaria.
5. Crea alertas semanales, no solo mensuales.
6. Implementa flujo de recuperación:
   - Email para usuarios gratuitos que cancelan
   - Oferta o pausa para usuarios pagos
   - Recuperación por fallo de pago
   - Encuesta de salida
   - Winback a los 7, 14 y 30 días

---

# Qué métrica deberías usar como principal

Depende de tu modelo.

## Si tu negocio es suscripción paga

Métrica principal:

\[
\text{MRR churn}
\]

y

\[
\text{Paid logo churn}
\]

Métricas secundarias:

- Free churn
- Activación
- Trial-to-paid
- Retención por cohorte

## Si tu modelo es freemium y el free es importante

Métricas principales:

- Activación de usuarios gratuitos
- Retención de usuarios gratuitos activos
- Conversión free-to-paid
- Paid churn
- MRR churn

En ese caso, el churn gratuito no puede ignorarse, pero debe interpretarse distinto.

---

# Señales de que sí es grave

Preocúpate más si ves alguno de estos:

- Las 2 bajas pagas representan una parte grande del MRR.
- Los clientes pagos cancelaron por el mismo motivo.
- Los clientes pagos estaban activos y aun así se fueron.
- Hay un aumento de tickets de soporte o quejas.
- Las 60 bajas gratuitas eran usuarios activos.
- Las bajas gratuitas vienen de una campaña reciente con buena intención de compra.
- Hay caída en activación.
- Hay caída en conversión free-to-paid.
- El churn pago se mantiene cerca de 9% durante varios meses.

# Señales de que puede ser menos grave

- Las 60 bajas gratuitas eran usuarios que nunca activaron.
- Eran cuentas antiguas inactivas.
- Hubo una limpieza de base de datos.
- El panel cambió de definición.
- Las 2 bajas pagas son de bajo MRR.
- Los clientes pagos restantes siguen activos.
- No hay patrón repetido en los motivos de cancelación.
- La conversión y el uso de pago se mantienen estables.

---

# Mi lectura final

El 31% es engañoso porque mezcla poblaciones distintas.

La lectura correcta es:

> “El churn total subió a 31%, pero está impulsado por 60 bajas de usuarios gratuitos. El churn de usuarios pagos fue 9.1%, con solo 2 bajas sobre 22 clientes. No es una emergencia automática de ingresos, pero sí requiere análisis inmediato porque el churn pago está por encima del objetivo y el churn gratuito puede indicar un problema de adquisición, activación o expectativa.”

Tu prioridad ahora no es entrar en pánico, sino separar la señal del ruido.

Haz esto primero:

1. Divide churn free vs paid.
2. Calcula MRR perdido.
3. Investiga si las 60 bajas gratuitas eran usuarios reales/activos.
4. Contacta a los 2 clientes pagos perdidos.
5. Corrige el dashboard para que no vuelva a mezclar poblaciones sin aclararlo.