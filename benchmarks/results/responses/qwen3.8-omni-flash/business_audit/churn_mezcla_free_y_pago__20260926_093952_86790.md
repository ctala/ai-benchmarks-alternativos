# Qwen 3.8 Omni Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 69.585s | tokens_per_second: 49.0
- input_tokens: 227 | output_tokens: 3410

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

Tranquilo/a: **el 31% no es necesariamente tu churn real de negocio**. Lo que estás viendo es una métrica agregada mal segmentada. Con los datos que tienes, el problema parece más matizado:

| Segmento | Base inicio mes | Bajas | Churn mensual |
|---|---:|---:|---:|
| Total | 200 | 62 | 31,0% |
| Gratuito | 178 | 60 | 33,7% |
| Pago | 22 | 2 | **9,1%** |

## ¿Qué tan grave es?

Depende de cuál sea tu población relevante.

### 1. Si tu negocio vive de los usuarios de pago
Tu churn pagado es **9,1% mensual**, no 31%.  
Eso sigue siendo alto, pero no es lo mismo que “perder un tercio de la plataforma”.

Anualizado, un 9,1% mensual implicaría retener aproximadamente:

\[
(1 - 0,091)^{12} \approx 0,32
\]

Es decir, **retendría alrededor del 32% de la base pagada tras un año**, o lo que es lo mismo, perderías cerca del 68% anual. Eso es preocupante si tu modelo es SaaS/subscription, pero es accionable.

Además, con solo **22 usuarios de pago**, 2 bajas pesan mucho. Estadísticamente es una muestra pequeña: un mes puedes tener 0 churn pagado y otro 18%. No tomes decisiones estructurales solo por un mes.

### 2. Si tu negocio monetiza vía conversión desde gratuito
El churn gratuito de 33,7% puede ser normal o incluso bueno, dependiendo de tu funnel. En muchos productos freemium, una parte grande de usuarios gratuitos nunca activa valor real y se va. Lo importante ahí no es tanto que se vayan, sino:

- cuántos convierten a pago,
- cuánto tarda la conversión,
- qué porcentaje de gratuitos son realmente activos,
- si los que se van tenían intención de pago o eran curiosos/spam/inactivos.

### 3. El error principal del panel
Está mezclando dos poblaciones distintas:

- usuarios gratuitos, que probablemente tienen churn alto por naturaleza;
- usuarios de pago, que son los que afectan a ingresos.

Por eso el churn total sale inflado. Un churn global de 31% casi seguro no debería usarse como métrica ejecutiva principal.

---

# Plan inmediato

## Paso 1: Recalcular la métrica correctamente

No uses “churn total” como KPI principal. Usa como mínimo:

### Churn de usuarios de pago
\[
\frac{\text{usuarios de pago dados de baja}}{\text{usuarios de pago al inicio del mes}}
\]

En tu caso:

\[
\frac{2}{22} = 9,1\%
\]

### Churn de usuarios gratuitos
\[
\frac{60}{178} = 33,7\%
\]

### Churn de MRR, si aplica
Si cada usuario de pago paga el mismo precio, el churn de ingresos también sería 9,1%.  
Pero si tienen planes distintos, necesitas calcular:

\[
\frac{\text{MRR perdido por bajas}}{\text{MRR al inicio del mes}}
\]

Esto es más importante que el churn de usuarios, porque dos bajas pueden representar 2% del MRR o 40% del MRR según el plan.

---

## Paso 2: Verificar la definición de “baja”

Antes de alarmarte, revisa exactamente qué está contando el panel como churn.

Preguntas clave:

1. ¿Una “baja” significa cancelar el plan?
2. ¿Incluye downgrade de pago a gratuito?
3. ¿Incluye impago/fallo de tarjeta?
4. ¿Incluye usuarios inactivos durante X días?
5. ¿Incluye cuentas creadas pero nunca activadas?
6. ¿Incluye pruebas gratuitas?
7. ¿Está usando usuarios únicos o cuentas?
8. ¿Está mirando cohort del mes o snapshot de inicio de mes?
9. ¿Excluye reactivaciones dentro del mismo mes?
10. ¿Está midiendo churn bruto o churn neto?

Esto importa muchísimo. Por ejemplo:

- Si 60 gratuitos se dieron de baja porque eran registros fríos, no es crisis.
- Si 2 usuarios de pago cancelaron por bug, soporte o falta de valor, sí es señal fuerte.
- Si uno de los pagos era tu cliente más grande, el impacto real puede ser mayor que el 9,1%.

---

## Paso 3: Separar urgencia comercial de urgencia estadística

Con 22 usuarios de pago, 2 bajas son pocas unidades absolutas. Pero pueden ser graves si:

- son clientes antiguos;
- pagan caro;
- representan una cuenta estratégica;
- cancelaron por un problema evitable;
- hay patrón común entre ambos.

Haz una revisión manual inmediata de esas 2 cuentas pagas:

- ¿Cuánto tiempo llevaban activas?
- ¿Qué plan tenían?
- ¿Cuándo empezó su uso a bajar?
- ¿Tuvieron tickets, bugs, cobros fallidos, cambios de equipo?
- ¿Cancelaron voluntariamente o por impago?
- ¿Dijeron motivo al cancelar?
- ¿Podrían ser recuperadas?

Para un negocio pequeño, hablar personalmente con esos 2 clientes vale más que cualquier dashboard.

---

## Paso 4: No optimices el churn gratuito todavía

El churn gratuito alto puede ser ruido. Primero entiende si esos 60 gratuitos tenían valor potencial.

Clasifícalos:

| Tipo de usuario gratuito | Acción recomendada |
|---|---|
| Registrado sin activar | No contar como churn real; mejorar onboarding o limpieza de base |
| Activo pocos días | Revisar activation funnel |
| Usó producto y luego se fue | Buscar causa de abandono |
| Esperaba feature concreta | Priorizar roadmap |
| Inactivo prolongado | Reenganchar o purgar de métricas |
| Posible lead frío | No alarmarse |

Si tu plataforma tiene muchos registros gratuitos que nunca activan, tu churn total siempre será alto. Eso no significa que el producto esté mal; significa que tu métrica está contaminada.

---

## Paso 5: Construir el tablero correcto

Reemplaza “Churn total 31%” por estos KPIs:

### Para negocio/SaaS
- **Paid user churn**: 9,1%
- **MRR churn**: pendiente de calcular
- **Net Revenue Retention, NRR**: ideal si tienes expansiones/downgrades
- **Gross Revenue Retention, GRR**: más conservador
- **ARPA/ARPU de pagados**
- **Lifetime value estimado**
- **CAC payback**
- **Conversión free → paid**
- **Time to first value**
- **Activation rate**
- **Retention por cohorte**

### Para producto
- Retention D1/D7/D30
- % usuarios que completan acción clave
- % usuarios que regresan tras 7/14/30 días
- Funnel de onboarding
- Uso de features críticas
- Tickets/premios de churn
- NPS o CSAT en usuarios próximos a cancelar

---

## Paso 6: Diagnosticar causas con foco en pagados

Para los 2 usuarios de pago, haz entrevistas o revisión profunda. Busca patrones:

1. **Valor percibido**
   - ¿Entendieron el producto?
   - ¿Lograron un resultado claro?
   - ¿Usaron la feature principal?
   - ¿Hubo cambio interno en su empresa?

2. **Precio/plan**
   - ¿Les pareció caro?
   - ¿Necesitaban otro plan?
   - ¿Hubo subida de precio?
   - ¿Tenían usage bajo vs coste?

3. **Producto**
   - Bugs
   - Lentitud
   - Falta de integración
   - UX confusa
   - Feature ausente

4. **Servicio**
   - Soporte lento
   - Falta de onboarding
   - Comunicación insuficiente
   - Expectativas mal vendidas

5. **Facturación**
   - Cobro duplicado
   - Fallo de tarjeta
   - Confusión con prueba gratuita
   - Cancelación accidental

Con solo 2 casos, no busques significancia estadística. Busca aprendizaje cualitativo.

---

## Paso 7: Acciones de corto plazo

### Esta semana
1. Contactar a los 2 usuarios de pago que cancelaron.
2. Ofrecer llamada de recuperación, sin descuento automático todavía.
3. Revisar si alguna cancelación fue por impago evitable.
4. Calcular MRR perdido y MRR actual.
5. Recalcular churn segmentado y compartir versión correcta al equipo.
6. Identificar si hubo algún release, cambio de pricing, bug o incidencia ese mes.

### Próximas 2 semanas
1. Implementar alerta temprana de riesgo para usuarios de pago:
   - caída de login,
   - menos uso,
   - ticket abierto,
   - fallo de pago,
   - downgrade,
   - inactividad 7/14 días.
2. Crear playbook de retención pagada:
   - email de check-in,
   - llamada de éxito del cliente,
   - encuesta de cancelación,
   - oferta de pausa en vez de baja,
   - alternativa de plan inferior antes de churn total.
3. Medir activation rate de gratuitos.
4. Limpiar definición de “usuario activo”.
5. Separar métricas de negocio y métricas de producto.

### Próximo mes
1. Definir target de paid churn.
2. Establecer cohort retention semanal/mensual.
3. Revisar pricing/paquetes si hay mismatch.
4. Lanzar programa de onboarding asistido para nuevos pagados.
5. Crear dashboard con churn bruto, neto, involuntario y por segmento.

---

## Paso 8: Qué decirle a tu equipo/inversores/jefes

No digas: “tenemos 31% de churn”.

Di algo así:

> El churn agregado de 31% está mezclado entre usuarios gratuitos y de pago. El churn de usuarios de pago fue 9,1% este mes, equivalente a 2 bajas sobre 22 cuentas. El churn de gratuitos fue 33,7%, pero esa población incluye registros posiblemente no activados. La prioridad ahora es validar impacto en MRR, entender causas de las 2 bajas pagadas y separar métricas de negocio y producto.

Eso transmite control, no pánico.

---

# Mi lectura rápida

No estás necesariamente en crisis de 31%.  
Tienes una posible señal de atención en el segmento de pago: **9,1% mensual con base pequeña**.

Lo urgente no es “bajar el churn total”, sino:

1. confirmar si el churn pagado afecta MRR de forma material;
2. entender por qué se fueron esos 2 clientes;
3. evitar que el panel mezcle gratuito y pago;
4. medir retención por cohortes y segmentos.

Si quieres, pásame estos datos y te armo el diagnóstico más preciso:

- precio o MRR de cada usuario de pago;
- fecha de alta de los 22 pagados;
- fecha exacta de las 2 bajas;
- motivo de cancelación, si existe;
- cuántos gratuitos estaban realmente activos;
- si hay conversión free → paid este mes;
- si las bajas incluyen impagos o cancelaciones voluntarias.