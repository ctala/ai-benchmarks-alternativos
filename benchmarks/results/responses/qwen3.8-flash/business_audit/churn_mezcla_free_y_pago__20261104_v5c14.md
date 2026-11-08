# Qwen 3.8 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 65.173s | tokens_per_second: 102.3
- input_tokens: 227 | output_tokens: 6666

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

Respira: **el 31% casi seguro no es “churn de negocio”**. Tu panel está mezclando **usuarios gratuitos** con **clientes de pago**. Eso cambia completamente la lectura.

## 1) Qué está midiendo realmente ese 31%

### Churn total de usuarios
```text
62 bajas / 200 usuarios = 31%
```
Esto incluye **178 gratuitos + 22 de pago**.

### Churn de usuarios gratuitos
```text
60 bajas / 178 gratuitos = 33.7%
```
Esto puede ser normal si el plan gratuito tiene mucha entrada/salida, o puede ser una señal de activación/engagement, pero **no suele ser churn de ingresos**.

### Churn de clientes de pago
```text
2 bajas / 22 clientes de pago = 9.1%
```
Esta es la métrica que probablemente te importaba si esperabas un 5%.

---

## 2) ¿Qué tan grave es?

Depende de qué significaba tu “5% esperado”.

### Escenario A: tu 5% esperado era churn de clientes de pago
Entonces sí hay una alerta.

```text
Esperado: 5%
Actual: 9.1%
```

Estás casi al doble de churn de logos de pago. Pero con una base de solo **22 clientes**, la métrica es volátil: una sola baja mueve el número mucho.

- 2 bajas sobre 22 = **9.1%**
- 1 baja sobre 22 = **4.5%**
- 3 bajas sobre 22 = **13.6%**

Así que no es una crisis catastrófica, pero sí una **señal de retención que merece investigación inmediata**.

### Escenario B: tu 5% esperado era churn total de usuarios
Entonces el problema principal es de **definición de métrica**, no necesariamente de negocio.

El panel te está mostrando churn de todos los usuarios, incluyendo gratuitos. Si antes medías solo pago y ahora medías total, el salto de 5% a 31% puede ser simplemente un cambio de población.

### Escenario C: tu negocio depende de ingresos recurrentes
La gravedad real no es 9.1% de logos, sino:

```text
Churn de ingresos = MRR perdido por churn / MRR al inicio del mes
```

Si los 2 clientes de pago que se fueron eran pequeños, el churn de ingresos puede estar lejos del 9.1%.  
Si eran cuentas importantes, el problema puede ser mayor.

**Sin MRR no se puede decir si hay emergencia real.**

---

## 3) Semáforo rápido

| Situación | Nivel |
|---|---|
| El 31% incluye gratuitos | Métrica poco útil como churn principal |
| Churn de pago: 9.1% | Amarillo/rojo si esperabas 5% |
| Base de solo 22 clientes de pago | Volátil, una baja cambia mucho |
| Si las 2 bajas son cuentas de bajo MRR | Menos grave |
| Si las 2 bajas son cuentas clave o con alto MRR | Grave |
| Si hubo fallas de pago / cobros fallidos | Operativo, se puede recuperar |
| Si los gratuitos se van pero nunca activaron | No necesariamente malo |
| Si los gratuitos son leads y no convierten | Sí afecta crecimiento |

---

## 4) Lo que deberías hacer ahora mismo

### Paso 1: Separa las métricas en el panel

No midas “churn” como un solo número. Crea estas métricas:

1. **Paid logo churn**  
   ```text
   Clientes de pago perdidos / Clientes de pago al inicio del mes
   ```

2. **Gross revenue churn**  
   ```text
   MRR perdido por bajas / MRR al inicio del mes
   ```

3. **Net revenue retention / churn**  
   ```text
   (MRR inicial - MRR perdido + expansiones - contracciones) / MRR inicial
   ```

4. **Free user churn**  
   ```text
   Usuarios gratuitos que se dieron de baja / Usuarios gratuitos al inicio
   ```

5. **Free-to-paid conversion**  
   ```text
   Nuevos clientes de pago / Usuarios gratuitos activos
   ```

El número que debe preocuparte principalmente es **churn de pago**, no churn total.

---

### Paso 2: Investiga las 2 bajas de pago

Para cada uno de los 2 clientes que se fueron, responde:

- ¿Cuánto MRR tenía?
- ¿Desde cuándo era cliente?
- ¿Fue baja voluntaria o falló un cobro?
- ¿Usaba el producto?
- ¿Tuvo tickets de soporte?
- ¿Se quejó de precio, funcionalidades, soporte o cambio de producto?
- ¿Fue reemplazado por un competidor?
- ¿Era cliente nuevo o antiguo?
- ¿Se fue por una razón estructural o aislada?

Esto es lo más importante. No actives todo un plan de retención sin saber por qué se fueron.

---

### Paso 3: Contacta a los 2 clientes de pago que se fueron

No para venderles. Para entender.

Mensaje simple:

```text
Hola [nombre], vi que cancelaste tu cuenta. No quiero insistir en nada, solo me ayuda mucho entender qué te llevó a irte: ¿precio, falta de funcionalidades, uso, soporte, cambio de prioridad o algo más? Si hubo algún problema de cobro o configuración, puedo revisarlo directamente.
```

Si fueron bajas por cobro fallido, hay oportunidad de recuperarlos.

---

### Paso 4: Revisa si el churn es involuntario

Si alguno de los 2 clientes se fue por:

- tarjeta rechazada,
- falta de fondos,
- error de cobro,
- expiración de pago,
- problema de facturación,

eso no es churn de producto. Es churn operativo.

En ese caso, la acción es:

- emails de actualización de pago,
- reintentos de cobro,
- avisos claros,
- período de gracia,
- opción de downgrade o pausa,
- soporte proactivo ante fallos de cobro.

---

### Paso 5: Analiza el churn de gratuitos, pero con la lente correcta

60 de 178 gratuitos se fueron. Eso es **33.7%**.

Pregúntate:

- ¿Eran usuarios que nunca activaron?
- ¿Eran usuarios que probaron y no encontraron valor?
- ¿Eran usuarios de abuso, spam o cuentas temporales?
- ¿Eran leads que podrían convertirse?
- ¿Los gratuitos aportan valor indirecto: comunidad, red, contenido, datos, referrals?
- ¿La salida de gratuitos afecta conversiones a pago?

Si los gratuitos son solo cuentas sin monetizar y no afectan el funnel, no es una emergencia.

Si el plan gratuito es tu motor de adquisición, sí puede ser una alerta de activación.

---

## 5) Plan inmediato por tiempos

### Hoy / próximas 24 horas

1. **No uses el 31% como churn principal.**
2. Recalcula churn de pago: **9.1%**.
3. Pide o exporta el MRR de los 2 clientes de pago que se fueron.
4. Revisa si fueron bajas voluntarias o fallas de cobro.
5. Contacta a los 2 clientes de pago perdidos.
6. Revisa el histórico: ¿antes el 5% era pago o total?

### Próximas 48 horas

1. Calcula:
   - Paid logo churn: 9.1%
   - Revenue churn: requiere MRR
   - Free churn: 33.7%
   - Free-to-paid conversion
2. Segmenta los 62 churns:
   - gratuitos inactivos,
   - gratuitos activos,
   - clientes nuevos,
   - clientes antiguos,
   - cuentas de alto MRR,
   - cuentas de bajo MRR,
   - bajas por cobro,
   - bajas por producto,
   - bajas por precio.
3. Identifica si hay un patrón:
   - mismo plan,
   - mismo canal de adquisición,
   - mismo onboarding,
   - misma funcionalidad,
   - mismo problema de soporte,
   - mismo cambio de precio,
   - mismo tipo de cliente.

### Esta semana

1. Haz 3-5 llamadas/emails a usuarios gratuitos que se fueron para entender si había potencial de conversión.
2. Haz llamadas a clientes de pago activos con riesgo:
   - bajo uso,
   - tickets recientes,
   - renovación cerca,
   - downgrade,
   - login frecuente pero sin acciones clave.
3. Revisa cohortes:
   - clientes adquiridos en los últimos 30/60/90 días,
   - clientes de hace más de 6 meses,
   - clientes gratuitos que llegaron a pago.
4. Ajusta el dashboard:
   - separa free vs paid,
   - muestra MRR,
   - muestra NRR,
   - muestra churn por plan,
   - muestra churn por antigüedad.

### Próximas 2-4 semanas

1. Implementa acciones según la causa:
   - si es onboarding, mejora activación,
   - si es soporte, revisa SLA y tickets,
   - si es precio, evalúa planes o downgrade,
   - si es producto, prioriza el gap más común,
   - si es facturación, implementa dunning y reintentos,
   - si es falta de valor, crea check-ins y success plans.
2. Define alertas tempranas:
   - usuario con 7 días sin login,
   - usuario con 14 días sin acción clave,
   - cliente con ticket crítico abierto,
   - cliente con pago fallido,
   - cliente que baja de plan.
3. Mide si las acciones bajan churn de pago.

---

## 6) Qué decirle a tu equipo o a tus stakeholders

Puedes decir algo así:

```text
El 31% no es churn de clientes de pago. El panel está incluyendo usuarios gratuitos.

Lo relevante es:
- Churn total de usuarios: 31%
- Churn de gratuitos: 33.7%
- Churn de clientes de pago: 9.1%

Si nuestro objetivo era 5% de churn de pago, sí hay una alerta, pero la base es pequeña: 22 clientes. Lo siguiente es calcular churn de ingresos, revisar por qué se fueron los 2 clientes de pago y separar la métrica en el dashboard.
```

---

## 7) Tu decisión final debería ser esta

No te quedes con el 31%.

Mide esto:

```text
Churn de pago relevante = clientes de pago perdidos / clientes de pago al inicio
```

Y luego:

```text
Churn de ingresos relevante = MRR perdido / MRR inicial
```

Con tus datos actuales:

```text
Churn total reportado: 31%
Churn de pago: 9.1%
Churn de gratuitos: 33.7%
```

Si esperabas 5% en pago, **hay problema de retención, pero no necesariamente una catástrofe**.  
Si esperabas 5% total, **tu panel está midiendo otra cosa y necesitas corregir la definición**.

Lo urgente no es entrar en pánico. Lo urgente es:

1. Separar free de paid.  
2. Calcular revenue churn.  
3. Investigar las 2 bajas de pago.  
4. Corregir el dashboard.  
5. Actuar solo sobre la causa real.