# GPT-OSS 120B — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 4.25 | quality: 3.33
- latency_total: 45.703s | tokens_per_second: 43.3
- input_tokens: 262 | output_tokens: 1981

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa

## 📊 Análisis rápido de los números propuestos  

| Variable | Valor | Cálculo | Resultado |
|----------|-------|---------|-----------|
| **Visitas mensuales** | 200 000 | – | 200 000 |
| **Tasa de captura** | 1,5 % | 200 000 × 0,015 | **3 000 suscriptores** |
| **Tasa de compra** | 2 % | 3 000 × 0,02 | **60 compradores** |
| **Precio del curso** | $30 | 60 × 30 | **$1 800** de ingresos mensuales |

**Objetivo:** $6 000/mes  
**Gap:** $6 000 – $1 800 = $4 200 (≈ 233 % más de lo que genera el plan).

---

## 📈 ¿Qué combinación de variables nos daría $6 000?

La fórmula básica es:

\[
\text{Ingresos} = \text{Visitas} \times \text{Tasa captura} \times \text{Tasa compra} \times \text{Precio}
\]

Reemplazando con el objetivo y manteniendo visitas = 200 000 y precio = $30:

\[
6 000 = 200 000 \times \text{TC} \times \text{TCp} \times 30
\]

\[
\text{TC} \times \text{TCp} = \frac{6 000}{200 000 \times 30}=0,001 = 0,10\%
\]

**Interpretación:** La **productividad combinada** (captura × compra) tiene que ser 0,10 % del tráfico. Con la captura que proponen (1,5 %) la compra tendría que ser:

\[
\text{TCp} = \frac{0,001}{0,015}=0,0667 \approx **6,7 %**
\]

> **Necesitarían que el 6,7 % de los suscriptores compren**, no el 2 % que estiman.

---

## 🚩 Señales de alerta

| Tema | Por qué es problemático |
|------|------------------------|
| **Ingresos no recurrentes** | Un curso de $30 es venta única. El objetivo habla de “$6 000/mes recurrentes”. Necesitarían vender **el mismo número de cursos cada mes** sin que el público se agote. |
| **Tasa de compra muy baja** | En muchos nichos de educación online, una tasa de compra del **2 %** es típica *solo* cuando el tráfico está muy segmentado y el funnel está optimizado. Con una captura del 1,5 % (poco cualificado) la expectativa de 2 % de compra es demasiado conservadora; la realidad suele ser < 1 % en la mayoría de los sitios de contenido general. |
| **Churn y CAC no contemplados** | No se calculan costos de adquisición (ads, creación de contenido, herramientas) ni la pérdida de suscriptores en el tiempo. Sin ello, la “rentabilidad” real es imposible de estimar. |
| **Escalabilidad del tráfico** | 200 k visitas mensuales pueden ser estacionales o depender de canales que no son sostenibles a largo plazo (ej. tráfico orgánico de una campaña puntual). |

---

## 📌 Qué habría que cambiar para que el plan sea viable

| Área | Opciones concretas | Impacto esperado |
|------|-------------------|-------------------|
| **Precio** | Subir a $70‑$100 (curso premium) o crear paquetes (curso + coaching). | Un precio de $80 con la misma 60 ventas daría $4 800 → aún falta, pero se reduce la presión sobre la tasa de compra. |
| **Tasa de captura** | Mejorar el lead magnet, usar pruebas A/B, añadir incentivos (descuentos, contenido exclusivo). Objetivo: ≥ 3 % (6 000 suscriptores). | 200 k × 3 % = 6 000 suscriptores. |
| **Tasa de compra** | Upsell de membresía, webinars de venta, email‑marketing de nurture, pruebas de precios. Objetivo: ≥ 5 % de los suscriptores. | 6 000 × 5 % = 300 compradores → a $30 = $9 000. |
| **Modelo recurrente** | Convertir el curso en una suscripción mensual (ej. acceso a comunidad, contenido nuevo cada mes) a $15‑$20. | 300 suscriptores a $20 = $6 000 mensuales *recurrentes*. |
| **Diversificación de ingresos** | Añadir productos complementarios (plantillas, consultorías, afiliados). | 10‑20 % de ingresos extra sin cambiar el funnel principal. |
| **Optimización del CAC** | Medir y reducir costo por visita (SEO, contenido evergreen) para que el margen sea positivo. | Mejora la rentabilidad neta. |

> **Ejemplo de hoja de ruta mínima para alcanzar $6 000/mes recurrentes**  
> 1. **Lead magnet mejorado** → 3 % de captura (6 000 leads).  
> 2. **Email‑nurture + webinar de venta** → 5 % de conversión a suscripción mensual de $20.  
> 3. **Ingresos = 6 000 × 5 % × $20 = $6 000**.  
> 4. **Mantenimiento**: contenido nuevo cada mes + comunidad para reducir churn < 5 % mensual.

---

## ✅ Recomendación final

**No aprobamos el plan tal cual está.**  
Los números actuales (solo $1 800) están a un tercio del objetivo y, además, el modelo propuesto no genera ingresos recurrentes, que es el punto clave del objetivo.

Para seguir adelante deberían:

1. **Redefinir el modelo de negocio** hacia algo recurrente (membresía, suscripción de contenido, coaching continuo).  
2. **Incrementar la captura** (optimizar el formulario, lead magnet) al menos al 3 % o más.  
3. **Mejorar la tasa de compra** mediante nurture y upsells, apuntando a ≥ 5 % de los suscriptores.  
4. **Re‑calcular el pricing** y validar con pruebas A/B.  
5. **Construir una hoja de cálculo de CAC, LTV y churn** antes de comprometer presupuesto.

Una vez que se tengan proyecciones que cumplan o superen el umbral de $6 000/mes bajo esas condiciones, el plan puede volver a la mesa para su aprobación. 

---

### Próximos pasos sugeridos

| Acción | Responsable | Deadline | Métrica de éxito |
|--------|--------------|----------|-------------------|
| Test A/B del lead magnet (e‑book vs. mini‑curso) | Equipo de contenido | 2 sem. | ↑ captura ≥ 2 % vs. 1,5 % |
| Implementar secuencia de email de 5‑7 días + webinar de venta | Marketing/CRM | 4 sem. | Tasa de compra ≥ 4 % de los leads |
| Prototipo de membresía mensual ($20) y encuesta de disposición a pagar | Producto + UX | 6 sem. | 30 % de encuestados dispuestos a pagar |
| Modelo financiero con CAC, LTV y churn | Finance | 6 sem. | LTV/CAC > 3 y churn < 5 % |

Con esos experimentos y datos, podremos volver a evaluar si la meta de $6 000/mes recurrentes es alcanzable. 🚀