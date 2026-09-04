# Qwen 3.8 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 69.881s | tokens_per_second: 65.1
- input_tokens: 227 | output_tokens: 4552

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

Tranquilo: **no estás perdiendo el 31% de tu negocio**. Lo que pasó es que tu panel está midiendo una población mezclada: usuarios gratuitos + usuarios de pago. Eso infla muchísimo el churn y te está generando pánico innecesario.

Vamos a separarlo.

---

## 1. El 31% no es tu churn real de negocio

Tu cálculo actual:

```text
62 bajas / 200 usuarios al inicio = 31%
```

Ese número es correcto **como churn total de usuarios**, pero no sirve para entender la salud del negocio si la mayoría de usuarios son gratuitos.

Tu base es esta:

| Segmento | Usuarios inicio | Bajas | Churn |
|---|---:|---:|---:|
| Gratuito | 178 | 60 | 33.7% |
| Pago | 22 | 2 | 9.1% |
| Total | 200 | 62 | 31.0% |

Es decir:

- **Churn gratuito:** 60 / 178 = **33.7%**
- **Churn de pago:** 2 / 22 = **9.1%**
- **Churn total reportado:** 62 / 200 = **31%**

El 31% está dominado por usuarios gratuitos.

De hecho, **60 de las 62 bajas son del plan gratuito**, o sea:

```text
60 / 62 = 96.8% de las bajas son gratuitas
```

Eso cambia completamente la interpretación.

---

## 2. ¿Qué tan grave es realmente?

### Churn total del 31%: no alarmante si incluye gratuitos

Si tu plataforma tiene un plan gratuito grande, un churn alto de usuarios gratuitos puede ser normal, dependiendo del modelo.

Muchos usuarios gratuitos:

- prueban la herramienta,
- no activan,
- no usan,
- abandonan,
- crean cuenta y desaparecen.

Eso no es necesariamente churn de negocio. Es churn de interés o de activación.

### Churn de pago del 9.1%: sí merece atención

Este es el número importante.

```text
2 de 22 clientes de pago se fueron = 9.1% mensual
```

¿Es grave? Depende de dos cosas:

1. **Cuánto MRR representaban esos 2 clientes.**
2. **Si fueron bajas pequeñas o bajas grandes.**

Con una base de 22 clientes, perder 2 puede ser ruido estadístico, pero también puede ser una señal fuerte.

Regla rápida:

- Si los 2 churnados eran clientes pequeños, puede ser una mala racha.
- Si eran clientes medianos o grandes, es alerta roja.
- Si eran clientes muy grandes, puede ser un problema serio de retención o producto.

Necesitas calcular **churn de ingresos**, no solo churn de logos.

---

## 3. La métrica que debes mirar ahora mismo

No mires:

```text
Churn total = 31%
```

Mira:

```text
Churn de clientes de pago = bajas de pago / clientes de pago al inicio
```

Tu número real de negocio hoy es:

```text
2 / 22 = 9.1%
```

Pero todavía falta algo más importante:

```text
Churn de ingresos = MRR perdido / MRR al inicio
```

Por ejemplo, si el MRR total era $10,000 y los 2 clientes que se fueron representaban $1,500, tu churn de ingresos sería 15%. Si representaban $100, sería 1%.

El número de clientes no te dice todo. El dinero sí.

---

## 4. Tu panel está midiendo mal la pregunta

Tu panel está respondiendo:

> ¿Qué porcentaje de usuarios se dieron de baja este mes?

Pero tú necesitas saber:

> ¿Qué porcentaje de clientes que pagan se dieron de baja este mes?

Y además:

> ¿Cuánto MRR perdimos con esas bajas?

Y:

> ¿Cuánto MRR ganamos con nuevos clientes?

Por eso necesitas tres métricas separadas:

### A. Churn de usuarios gratuitos

```text
Bajas gratuitas / usuarios gratuitos al inicio
```

Sirve para salud de activación, onboarding y engagement.

No sirve para evaluar ingresos.

### B. Churn de clientes de pago

```text
Bajas de pago / clientes de pago al inicio
```

Sirve para evaluar retención comercial.

### C. Churn de ingresos

```text
MRR perdido / MRR al inicio
```

Es la métrica más importante para el negocio.

---

## 5. Plan inmediato: qué hacer hoy

### Paso 1: Recalcula el churn por segmento

Haz esta tabla en tu panel:

| Métrica | Fórmula | Tu caso |
|---|---:|---:|
| Churn total | 62 / 200 | 31.0% |
| Churn gratuito | 60 / 178 | 33.7% |
| Churn de pago | 2 / 22 | 9.1% |
| Churn de ingresos | MRR perdido / MRR inicio | Falta calcular |

Si no puedes calcular MRR perdido todavía, hazlo hoy mismo.

Necesitas saber:

- MRR total al inicio del mes.
- MRR de cada cliente que se dio de baja.
- MRR de nuevos clientes del mes.
- MRR de expansiones o upgrades.

Con eso calculas:

```text
Net Revenue Retention = (MRR inicio + expansiones - contracciones - churn) / MRR inicio
```

Esa es la métrica que realmente importa si tienes ingresos recurrentes.

---

### Paso 2: Identifica a los 2 clientes de pago que se fueron

Para cada uno, responde:

1. ¿Cuánto pagaban al mes?
2. ¿Cuánto tiempo fueron clientes?
3. ¿Por qué se fueron?
4. ¿Fueron downgrade o baja total?
5. ¿Tuvieron contacto con soporte o ventas antes de irse?
6. ¿Usaban el producto activamente?
7. ¿Fueron churn por precio, falta de uso, competencia, bug, falta de feature o desinterés?

Si puedes, llámalos o escríbeles para una mini entrevista. No para venderles, sino para entender.

Pregunta simple:

> “Vimos que dejaste el plan de pago. ¿Qué fue lo que más influyó en tu decisión?”

Con solo 2 clientes, cada entrevista vale muchísimo.

---

### Paso 3: Revisa si los 60 gratuitos son realmente usuarios activos

No todos los usuarios gratuitos que se dan de baja son iguales.

Divide los 178 usuarios gratuitos en:

| Tipo de gratuito | Descripción |
|---|---|
| Inactivos | Nunca usaron o no usaron hace semanas |
| Activos | Usan el producto con frecuencia |
| En riesgo | Usaban y bajaron su actividad |
| Trial recientes | Acaban de llegar |
| Cuentas basura | Emails temporales, spam, cuentas sin uso |

Si la mayoría de los 60 gratuitos eran inactivos, el churn gratuito es menos grave.

Si muchos gratuitos activos se fueron, ahí sí hay una señal de problema de producto o onboarding.

---

### Paso 4: No tomes decisiones por pánico

Tu instinto puede ser:

- hacer descuentos agresivos,
- enviar emails masivos,
- cambiar el pricing,
- crear features nuevas,
- contactar a todos los usuarios.

Antes de eso, necesitas segmentar.

No es lo mismo:

- 60 usuarios gratuitos inactivos que se van,
que
- 2 clientes de pago importantes que se van.

---

## 6. Plan para esta semana

### Día 1: Corregir la métrica

Configura el dashboard con estas métricas:

```text
Churn total de usuarios
Churn de usuarios gratuitos
Churn de clientes de pago
Churn de ingresos
MRR perdido
MRR ganado
Net Revenue Retention
```

Elimina del título principal la palabra “churn” si no especifica segmento.

Ejemplo:

Mal:

```text
Churn: 31%
```

Mejor:

```text
Churn de clientes de pago: 9.1%
Churn de usuarios gratuitos: 33.7%
Churn de ingresos: pendiente
```

---

### Día 2: Analizar los 2 clientes churnados

Crea una ficha para cada uno:

| Cliente | MRR | Antigüedad | Último uso | Motivo | Recuperable |
|---|---:|---:|---:|---|---|
| Cliente A | ? | ? | ? | ? | Sí/No/Posible |
| Cliente B | ? | ? | ? | ? | Sí/No/Posible |

Si fueron clientes pequeños y por falta de uso, puede ser normal.

Si fueron clientes grandes y por problema de producto, es urgente.

---

### Día 3: Analizar los 60 gratuitos

Pregunta:

- ¿Se dieron de baja ellos o los borraste tú?
- ¿Cuántos habían iniciado sesión el mes anterior?
- ¿Cuántos completaron onboarding?
- ¿Cuántos llegaron de una campaña específica?
- ¿Cuántos eran trials que no convirtieron?
- ¿Hay un patrón de fecha, fuente o comportamiento?

Esto te dirá si el churn gratuito es ruido o señal.

---

### Día 4: Revisar cohortes

No mires solo el mes actual. Mira por cohorte.

Ejemplo:

| Cohorte | Usuarios inicio | Bajas | Churn pago | Churn free |
|---|---:|---:|---:|---:|
| Enero | ? | ? | ? | ? |
| Febrero | ? | ? | ? | ? |
| Marzo | ? | ? | ? | ? |

Con 22 clientes de pago, una sola baja mueve mucho el porcentaje.

Si en los últimos 3 meses tienes:

```text
Mes 1: 1/20 = 5%
Mes 2: 0/21 = 0%
Mes 3: 2/22 = 9.1%
```

Puede ser variabilidad normal.

Pero si viene subiendo:

```text
Mes 1: 2%
Mes 2: 5%
Mes 3: 9%
```

Ahí sí hay tendencia.

---

### Día 5: Definir usuarios de pago en riesgo

Crea una lista de clientes de pago que podrían ser las próximas bajas.

Señales de riesgo:

- No inician sesión en 7/14/30 días.
- Usan menos features que antes.
- Tienen tickets de soporte sin resolver.
- No completaron onboarding.
- Están en plan mensual y no anual.
- Tuvieron downgrade.
- No usan la función principal.
- Su uso mensual cayó más de 30%.
- Su equipo dejó de usarlo.

Con solo 22 clientes de pago, puedes hacer seguimiento manual. Eso es una ventaja.

---

## 7. Plan para el próximo mes

### 1. Medir churn solo sobre clientes de pago

Tu métrica principal debería ser:

```text
Churn mensual de clientes de pago
```

No mezcles gratuitos.

### 2. Medir revenue churn

Tu métrica financiera:

```text
Churn mensual de ingresos
```

### 3. Medir Net Revenue Retention

```text
NRR = (MRR inicio + expansiones - contracciones - churn) / MRR inicio
```

NRR es mejor que churn solo porque incluye expansiones.

### 4. Separar churn de activación

Para usuarios gratuitos:

```text
Free users que nunca activan
Free users activos que se van
Free users que se convierten a pago
```

No midas “churn” como una sola cosa.

### 5. Crear una alerta temprana

Si un cliente de pago:

- baja su uso,
- no entra en 10 días,
- abre un ticket crítico,
- cancela sin hablar con soporte,

debe entrar en una lista de riesgo.

---

## 8. Diagnóstico rápido según tu caso

Con los datos que tienes, mi lectura es:

### Grave: no tanto como parece

El 31% no es el problema real.

El problema potencial es el churn de pago:

```text
9.1% mensual
```

Eso es alto si se sostiene, pero con solo 2 bajas sobre 22 clientes puede ser ruido.

### Prioridad máxima:

Investigar los 2 clientes de pago que se fueron.

### Prioridad media:

Entender por qué se van 60 usuarios gratuitos.

### Prioridad baja:

No obsesionarte con el 31% como si fuera churn comercial.

---

## 9. Cómo debería verse tu panel

Te recomiendo este formato:

```text
Churn de clientes de pago: 9.1%
Churn de ingresos: [pendiente]
MRR perdido: [pendiente]
Clientes de pago al inicio: 22
Clientes de pago al final: 20
Bajas de pago: 2

Churn de usuarios gratuitos: 33.7%
Usuarios gratuitos al inicio: 178
Bajas gratuitas: 60
```

Y debajo, una tabla:

| Segmento | Inicio | Bajas | Final | Churn |
|---|---:|---:|---:|---:|
| Gratuito | 178 | 60 | 118 | 33.7% |
| Pago | 22 | 2 | 20 | 9.1% |
| Total | 200 | 62 | 138 | 31.0% |

Pero ojo: el total de usuarios finales depende de cuántos usuarios nuevos entraron durante el mes.

---

## 10. Un detalle importante que falta

Tu panel dice:

```text
Usuarios totales a inicio de mes: 200
Usuarios que se dieron de baja este mes: 62
```

Pero no dice:

- ¿Cuántos usuarios nuevos entraron?
- ¿Cuántos usuarios había al final?
- ¿Cuántos usuarios gratuitos son activos?
- ¿Cuántos usuarios de pago son anuales vs mensuales?
- ¿Cuánto MRR tenían los 2 clientes que se fueron?

Si entraron muchos usuarios nuevos, el churn sobre usuarios al inicio puede estar subestimando o distorsionando la realidad.

Una fórmula más precisa para usuarios de pago es:

```text
Clientes de pago al final =
Clientes de pago al inicio
- bajas de pago
+ nuevos clientes de pago
```

Y para ingresos:

```text
MRR final =
MRR inicio
+ MRR nuevo
+ MRR expansión
- MRR contracción
- MRR churn
```

Eso es lo que necesitas para saber si realmente estás creciendo o no.

---

## 11. Resumen ejecutivo

No estás en una emergencia del 31%.

Tu situación es:

```text
Churn total: 31% → métrica contaminada por usuarios gratuitos
Churn gratuito: 33.7% → señal de activación/interés
Churn de pago: 9.1% → métrica importante a vigilar
Gravedad real: depende del MRR perdido
```

Tu siguiente acción no es “arreglar el churn”, es **dejar de medirlo mal**.

Empieza hoy con esto:

1. Separar free vs pago.
2. Calcular churn de pago: 9.1%.
3. Calcular churn de ingresos.
4. Entrevistar a los 2 clientes de pago que se fueron.
5. Revisar si los 60 gratuitos eran activos o inactivos.
6. Crear un dashboard con churn de pago, MRR perdido y NRR.

Si me pasas el MRR de los 2 clientes que se fueron y el MRR total del mes, puedo decirte si el problema es leve, moderado o serio.