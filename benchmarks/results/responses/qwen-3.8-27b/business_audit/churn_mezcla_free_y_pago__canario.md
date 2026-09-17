# Qwen 3.8 27B — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 6.85 | quality: 8.0
- latency_total: 130.079s | tokens_per_second: 72.6
- input_tokens: 227 | output_tokens: 9444

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



Primero: respira. **El 31% es aritméticamente correcto, pero casi seguro no está midiendo la población que te importaba.**

Tu panel está calculando churn sobre **todos los usuarios registrados al inicio del mes**, incluyendo free. Ese churn está dominado por usuarios gratuitos.

## 1. Cálculo rápido

| Segmento | Base al inicio | Bajas | Churn |
|---|---:|---:|---:|
| Free | 178 | 60 | **33.7%** |
| De pago | 22 | 2 | **9.1%** |
| Total | 200 | 62 | **31.0%** |

Lo importante:

- **No tienes un churn del 31% en clientes de pago.**
- Tienes un churn del **9.1% en pago** y del **33.7% en free**.
- El 31% es un churn “mixto” de cuentas registradas, no necesariamente de clientes.

---

## 2. ¿Qué tan grave es?

Depende de cuál era tu referencia del 5%.

### Si el 5% era churn de pago

Entonces estás a **9.1% mensual**, por encima del objetivo, pero con una base pequeña:

- 22 clientes de pago.
- 2 bajas.
- Si se va 1 cliente: 4.5%.
- Si se van 2: 9.1%.
- Si se van 3: 13.6%.

Con 22 clientes, **una sola baja mueve mucho la métrica**. No es suficiente para declarar una crisis de producto, pero sí es una señal a investigar.

### Si el 5% era churn total

Entonces sí es grave: estás a **31%**, muy por encima. Pero en ese caso tu métrica original probablemente no era la correcta, porque estás mezclando free y pago.

### Si tu modelo depende de free-to-paid

El churn free del **33.7%** puede ser serio, porque estás perdiendo volumen arriba del embudo. Si esos usuarios no activan, no convierten y se van, tu CAC y tu pipeline futuro se resienten.

**Veredicto rápido:**  
No es un incendio de churn de clientes, pero sí hay dos alertas:

1. **Churn de pago por encima del objetivo**, aunque con muestra pequeña.
2. **Churn free alto**, lo que puede indicar problema de activación, tráfico, expectativas o plan gratuito.

---

# Plan de acción

## A. Hoy: valida la métrica

Antes de actuar, confirma qué está midiendo el panel.

Preguntas clave:

1. ¿El denominador de 200 son usuarios **activos** o todos los registrados?
2. ¿Incluye cuentas de prueba, bots, duplicados, empleados, suspended?
3. ¿Una cancelación de pago cuenta como baja?
4. ¿Un downgrade de pago a free cuenta como churn?
5. ¿La fecha de baja es la fecha de cancelación, la fecha de expiración o la fecha de eliminación?
6. ¿Los 62 usuarios que se dieron de baja son todos de la base inicial de 200, o incluye usuarios nuevos que entraron y salieron en el mismo mes?
7. ¿El churn reportado es de logo, de ingresos o de cuentas registradas?

Hasta que no valides esto, no tomes decisiones grandes.

---

## B. Hoy o mañana: segmenta el churn

No mires solo el 31%. Divide la métrica.

### Churn por plan

Ya lo tienes:

- Free: 60/178 = 33.7%
- Pago: 2/22 = 9.1%

### Churn por cohorte

Mira cuándo se registraron los usuarios que se fueron:

- ¿Se fueron usuarios nuevos de esta semana?
- ¿Se fueron usuarios de hace 1 mes?
- ¿Se fueron usuarios de hace 3 meses?
- ¿Se fueron usuarios antiguos?

Eso te dice si el problema es:

- Adquisición de mala calidad.
- Onboarding.
- Activación.
- Producto.
- Billing.
- Fatiga de uso.
- Cambio de precio o política.

### Churn por canal de adquisición

Revisa si las 60 bajas free vienen de:

- Una campaña específica.
- Un país.
- Un dispositivo.
- Una fuente de tráfico.
- Un referral.
- Un evento o viralización.

Si la mayoría viene de un canal, puede ser un problema de expectativa o calidad de tráfico.

### Churn por uso

Compara a los que se fueron con los que se quedaron:

- ¿Hicieron onboarding?
- ¿Invitaron contactos?
- ¿Subieron contenido?
- ¿Conectaron integraciones?
- ¿Tuvieron errores?
- ¿Recibieron soporte?
- ¿Usaron la app en los primeros 3 días?

---

## C. En 24-48 horas: contacta a los 2 clientes de pago

Con solo 22 clientes de pago, cada baja es importante.

Haz esto:

1. Contacta a los 2 que se fueron.
2. Pregunta directamente por qué se fueron.
3. Ofrece una solución concreta si hay problema técnico, billing o de uso.
4. Pide permiso para volver a contactarlos.
5. Registra la razón exacta:
   - Precio.
   - Fallo de producto.
   - No usaban la plataforma.
   - Problema de billing.
   - Competencia.
   - Proyecto terminó.
   - No entendieron el valor.
   - Cambiaron de plan.

Con 2 clientes no puedes generalizar, pero sí puedes detectar una causa sistémica.

---

## D. En 48 horas: revisa billing y pagos

El churn de pago a veces no es producto, es billing.

Revisa:

- ¿Hubo pagos fallidos?
- ¿Hubo tarjetas expiradas?
- ¿Hubo errores en la pasarela?
- ¿Hubo cambios de precio?
- ¿Hubo proration mal calculado?
- ¿Hubo cobros duplicados?
- ¿Hubo suspensiones por pago fallido?
- ¿Hay dunning activo?

Si hay pagos fallidos, activa o mejora el flujo de recuperación:

- Recordatorio de pago fallido.
- Actualizar tarjeta.
- Reintento automático.
- Oferta de retención.
- Contacto manual si es cliente importante.

---

## E. En 1 semana: diagnostica el churn free

El churn free del 33.7% no se arregla con “bajar el churn total”. Hay que entender qué tipo de free estás perdiendo.

Clasifica a los 60 free que se fueron:

### 1. Nunca activaron

Se registraron, no hicieron la acción clave y se fueron.

Solución:

- Mejorar onboarding.
- Reducir fricción.
- Enviar emails de activación.
- Mostrar valor en los primeros 5 minutos.
- Cambiar el CTA inicial.
- Ajustar la página de registro.

### 2. Activaron pero no volvieron

Hicieron algo, pero no crearon hábito.

Solución:

- Emails de reactivación.
- Recordatorios de valor.
- Notificaciones útiles.
- Cases de uso.
- Retos o guías.
- Integraciones clave.

### 3. Usaron mucho y aun así se fueron

Eso sí es más preocupante.

Solución:

- Entrevistar.
- Revisar soporte.
- Revisar errores.
- Revisar performance.
- Revisar si hubo cambio de plan, precio o competencia.

### 4. Vinieron de tráfico no cualificado

Si el free es alto y de baja intención, el problema puede ser adquisición.

Solución:

- Ajustar mensaje de la campaña.
- Ajustar ICP.
- Cambiar landing.
- Pagar menos por tráfico malo.
- Usar trial en vez de free.
- Poner límites al plan gratuito.
- Hacer paywall en features clave.

---

# Plan de 30 días

## 1. Corrige el dashboard

No mires solo “churn total”. Crea estas métricas:

### Métricas de pago

- Churn de logo de pago.
- Churn de MRR.
- Churn por ARPA.
- Churn por cohorte.
- Churn por tamaño de cliente.
- Recuperación de pagos fallidos.
- Downgrades.
- Expansión.
- Net revenue retention.

### Métricas de free

- Churn free.
- Activación free.
- D1, D7, D30 de free.
- Trial-to-paid.
- Free-to-paid.
- Tiempo hasta activación.
- Conversion por canal.
- Churn free por canal.

### Alertas

- Cualquier baja de pago.
- Churn de pago mensual > 5%.
- Churn de MRR > 5%.
- Aumento de pagos fallidos.
- Caída de activación.
- Caída de D7.
- Churn free por canal por encima del promedio.

---

## 2. Define el objetivo correcto

Si tu negocio es de pago, tu métrica norte debería ser:

- **Churn de pago mensual ≤ 5%**
- **Churn de MRR mensual ≤ 5%**
- **Activación free ≥ X%**
- **D7 free ≥ Y%**
- **Trial-to-paid ≥ Z%**

Con 22 clientes de pago, 5% mensual significa aproximadamente:

- Esperado: 1.1 bajas.
- Aceptable: 1 baja.
- Alerta: 2 o más bajas.

No intentes optimizar el churn total si tu modelo de negocio depende de usuarios de pago.

---

## 3. Acciones inmediatas por prioridad

### Prioridad 1: Billing y retención de pago

- Contactar a los 2 que se fueron.
- Revisar pagos fallidos.
- Mejorar dunning.
- Crear alertas de riesgo.
- Hacer seguimiento manual a clientes de pago.
- Crear un score de salud de cuenta.

### Prioridad 2: Onboarding y activación

- Identifica la acción clave que predice retención.
- Haz que el usuario la haga en los primeros minutos.
- Reduce pasos innecesarios.
- Envía emails de activación.
- Añade guías o plantillas.
- Muestra valor temprano.

### Prioridad 3: Calidad del tráfico free

- Si el free viene de campañas, revisa expectativa vs producto.
- Si el free es masivo y no convierte, ajusta adquisición.
- Considera trial en vez de free.
- Considera límites en free.
- Considera paywall en features de alto valor.

### Prioridad 4: Producto y soporte

- Revisa tickets.
- Revisa errores técnicos.
- Revisa performance.
- Revisa cambios recientes.
- Revisa si hubo incidentes en el mes.
- Pide feedback a usuarios que se quedaron.

---

# Qué no haría

No haría esto:

1. **No tomaría el 31% como churn de clientes de pago.**  
   Es churn de cuentas registradas, dominado por free.

2. **No cambiaría pricing o producto radicalmente con solo 22 clientes de pago.**  
   La muestra es pequeña.

3. **No ignoraría el churn free.**  
   Si tu crecimiento depende de free-to-paid, perder 60 free al mes es un problema de embudo.

4. **No me fijaría solo en un mes.**  
   Necesitas cohortes de 30/60/90 días.

5. **No optimizaría “churn total” como métrica única.**  
   Esconde la diferencia entre free y pago.

---

# Cómo lo comunicaría a tu equipo

Puedes decir algo así:

> “El panel reportó un churn del 31%, pero está midiendo todas las cuentas registradas al inicio del mes, incluyendo free. Al segmentar, el churn de pago es 9.1% y el churn free es 33.7%. No es un churn del 31% en clientes de pago, pero sí tenemos dos alertas: el churn de pago está por encima del objetivo de 5%, y el churn free es alto. En los próximos 7 días vamos a validar la definición de la métrica, revisar billing, contactar a los 2 clientes de pago que se fueron y analizar por qué los free no activan o no convierten.”

---

# Resumen ejecutivo

- **31% = churn total de cuentas registradas.**
- **9.1% = churn de pago.**
- **33.7% = churn free.**
- Si tu objetivo era 5% de churn de pago, estás por encima, pero con base pequeña.
- Si tu objetivo era 5% de churn total, estás muy por encima.
- Lo urgente no es “bajar el 31%”, sino:
  1. Validar la métrica.
  2. Bajar churn de pago a ≤5%.
  3. Mejorar activación y conversión de free.
  4. Revisar billing, onboarding y calidad de tráfico.

Tu situación **no parece un desastre de producto**, pero sí una señal clara de que tu métrica estaba mal enfocada y que tu embudo gratuito está perdiendo mucho volumen.