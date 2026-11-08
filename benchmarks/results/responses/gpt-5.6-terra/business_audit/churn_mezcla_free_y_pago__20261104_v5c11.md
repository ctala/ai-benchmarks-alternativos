# GPT-5.6 Terra — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 28.465s | tokens_per_second: 81.0
- input_tokens: 165 | output_tokens: 2305

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

Respira: el **31% no describe el churn de tu negocio de pago**, sino la baja de toda la base, mayoritariamente gratuita.

### Qué está midiendo realmente el panel

| Población | Bajas | Usuarios al inicio | Churn mensual |
|---|---:|---:|---:|
| Todos los usuarios | 62 | 200 | **31.0%** |
| Usuarios gratuitos | 60 | 178 | **33.7%** |
| Usuarios de pago | 2 | 22 | **9.1%** |

Cálculos:

- Churn total: 62 / 200 = **31%**
- Churn free: 60 / 178 = **33.7%**
- Churn de pago: 2 / 22 = **9.1%**

Por tanto:

- El panel **no está equivocado** matemáticamente.
- Pero está mezclando dos poblaciones con comportamientos y valor económico muy distintos.
- Si tu preocupación es ingresos, el número relevante es, por ahora, **2 clientes de pago perdidos de 22: 9,1% mensual de customer/logo churn**.

## ¿Qué tan grave es?

No es una catástrofe del 31% de clientes pagadores. Pero **9,1% mensual de churn de pago merece atención**, especialmente si se sostiene varios meses.

Como referencia, si se mantuviera un churn de 9,1% todos los meses y no hubiera nuevas ventas ni expansiones, retendrías aproximadamente:

\[
(1 - 0{,}091)^{12} \approx 32\%
\]

de esa base tras un año. Es decir, sería alrededor de **68% de churn anual compuesto**.

Ahora bien, hay una advertencia importante: tienes una muestra muy pequeña.

- Con solo 22 clientes de pago, **una sola baja cambia la tasa en 4,5 puntos porcentuales**.
- Dos bajas pueden ser una señal de problema o simple variación mensual.
- No concluyas una tendencia con un único mes; mira al menos 3–6 meses y por cohortes.

Tu situación no es “31% de churn de pago”; es: **base de pago pequeña, con 2 bajas este mes, que hay que investigar inmediatamente.**

---

# Plan de acción

## Hoy: corrige la lectura y verifica los datos

### 1. Separa las métricas en el dashboard

No uses “churn de usuarios” como métrica principal sin segmentación. Crea al menos estas cuatro:

1. **Churn de clientes de pago (logo/customer churn)**  
   \[
   \frac{\text{clientes de pago que cancelaron}}{\text{clientes de pago al inicio del mes}}
   \]
   Resultado actual: **2 / 22 = 9,1%**

2. **Churn de MRR**  
   \[
   \frac{\text{MRR perdido por cancelaciones}}{\text{MRR al inicio del mes}}
   \]
   Esto es más importante que contar clientes si tus planes tienen precios diferentes.

3. **Net Revenue Retention (NRR)**  
   Considera cancelaciones, downgrades, upgrades y expansión de clientes existentes.

4. **Retención/abandono de usuarios free**  
   No lo presentes como churn financiero. Para free, normalmente importan más:
   - activación;
   - uso recurrente;
   - conversión a pago;
   - tiempo hasta abandono;
   - calidad de adquisición.

### 2. Confirma las definiciones

Antes de actuar, valida que las 2 bajas pagas sean realmente churn:

- ¿Eran clientes de pago activos al inicio del mes?
- ¿Cancelaron y perdieron acceso este mes, o solo cancelaron la renovación futura?
- ¿Alguno hizo downgrade a free? Eso puede ser churn de pago, pero no necesariamente pérdida total de usuario.
- ¿Hubo pagos fallidos involuntarios?
- ¿Hubo reactivaciones durante el mes?
- ¿El denominador debe ser 22 o hay clientes que empezaron a pagar durante el mes? Para churn mensual estándar, normalmente usa los clientes activos de pago al inicio.

---

## Próximas 48 horas: investiga las 2 bajas pagas

Con solo dos casos, puedes hacer investigación cualitativa profunda. Revisa para cada uno:

- plan y MRR perdido;
- antigüedad como cliente;
- canal de adquisición;
- caso de uso;
- nivel de uso en los últimos 7, 30 y 60 días;
- si completó la activación inicial;
- tickets de soporte, errores o quejas;
- eventos previos a la cancelación;
- motivo declarado de cancelación;
- si hubo cambio de precio, fallo de pago o problema de producto.

Contacta personalmente a ambos, sin presionar:

> “Vi que cancelaste [producto]. Estamos intentando mejorar y agradecería mucho entender qué no funcionó: ¿precio, falta de una función, dificultad de uso, resultados insuficientes o algo más? No es una venta; cualquier feedback nos ayuda.”

Tu objetivo no es necesariamente recuperarlos de inmediato; es identificar si ambos comparten una causa evitable.

---

## Esta semana: identifica el riesgo en los 20 clientes restantes

Construye una lista de clientes de pago con señales de riesgo:

- caída fuerte de uso vs. semanas anteriores;
- nunca alcanzaron el evento de activación clave;
- baja frecuencia de uso;
- pagos fallidos;
- tickets de soporte sin resolver;
- usuarios que no invitaron equipo, no configuraron integración o no completaron onboarding;
- cuentas con una sola persona activa;
- contratos o renovaciones próximas.

Para los clientes de mayor valor o mayor riesgo:

- envía outreach proactivo;
- ofrece ayuda de onboarding o revisión de uso;
- resuelve bloqueos concretos;
- documenta el “momento de valor” que deberían alcanzar.

No mandes una campaña genérica de “¿sigues ahí?” a todos. Con una base de 22 pagadores, la intervención personalizada probablemente tiene más retorno.

---

## En las próximas 2–4 semanas: construye un sistema de retención

### A. Define tu evento de activación

Identifica qué comportamiento temprano predice que un usuario se queda y paga. Por ejemplo:

- creó su primer proyecto;
- conectó una integración;
- invitó a un colaborador;
- publicó algo;
- obtuvo un resultado medible;
- usó una función clave varias veces en la primera semana.

Luego mide:

- % de nuevos registros que se activan;
- tiempo hasta activación;
- retención de activados vs. no activados;
- conversión free → paid de usuarios activados.

### B. Analiza cohortes, no solo el total mensual

Separa clientes por:

- mes de alta;
- plan;
- canal de adquisición;
- caso de uso;
- tamaño de cuenta;
- país o segmento, si aplica.

Puede ocurrir que las bajas vengan de una cohorte específica: por ejemplo, clientes adquiridos por una promoción, un canal de baja intención o después de un cambio de producto.

### C. Mide churn por motivos

Estandariza motivos de baja:

- precio;
- falta de valor/ROI;
- producto incompleto;
- problema técnico;
- mala experiencia de onboarding;
- cambió la necesidad;
- competidor;
- cierre de negocio;
- pago fallido;
- “solo estaba probando”.

Después prioriza por impacto: no todos los motivos son solucionables ni igual de frecuentes.

---

# Cómo reportarlo internamente

En lugar de decir:

> “Tenemos 31% de churn.”

Di:

> “El churn agregado fue 31%, impulsado por 60 bajas de usuarios gratuitos. El churn de clientes de pago fue 9,1%: 2 bajas sobre una base inicial de 22. Es una señal que debemos investigar, pero la muestra es pequeña. Esta semana validaremos los motivos de esas dos bajas, calcularemos churn de MRR y segmentaremos la retención por cohorte.”

Eso es preciso, evita pánico injustificado y mantiene la urgencia donde corresponde.

## Prioridad real

1. **No optimices el churn combinado de free + paid como si fuera una sola métrica.**
2. **Investiga las 2 bajas de pago hoy.**
3. **Calcula MRR churn y NRR.**
4. **Monitorea 3–6 meses de churn pagado por cohortes.**
5. **Trata el abandono free como problema de activación, calidad de adquisición o conversión, no necesariamente como crisis de ingresos.**

En resumen: el 31% es alarmante solo si estabas interpretándolo como churn de clientes de pago. Tu dato relevante de negocio es **9,1% mensual de churn de pago**, que no debe ignorarse, pero tampoco justifica el pánico sin entender los dos casos y la tendencia histórica.