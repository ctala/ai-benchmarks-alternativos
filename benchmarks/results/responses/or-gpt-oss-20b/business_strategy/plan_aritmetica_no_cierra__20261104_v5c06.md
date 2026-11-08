# GPT-OSS 20B — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 4.6 | quality: 3.33
- latency_total: 17.078s | tokens_per_second: 115.9
- input_tokens: 249 | output_tokens: 1979

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

**Respuesta rápida:**  
> **NO** – con los supuestos que has puesto el plan no alcanzará los $6 000/mes.  
> La multiplicación de los porcentajes te deja con solo **$1 800** al mes.  

---

## 1. ¿Qué está pasando con las métricas?

| Paso | Monto | % de conversión | Resultado |
|------|-------|-----------------|-----------|
| Visitas al sitio | 200 000 | – | 200 000 |
| Suscriptores (1.5 %) | 200 000 × 0.015 | 3 000 | 3 000 |
| Compras (2 %) | 3 000 × 0.02 | 60 | 60 |
| Ingreso (30 USD) | 60 × 30 | – | **$1 800** |

El **tasa de conversión total** (visita → compra) es:

\[
1.5\% \times 2\% = 0.03\% \quad (\text{es decir, 1 de cada 3 333 visitas})
\]

Con 200 000 visitas llegas a:

\[
200\,000 \times 0.0003 = 60 \;\text{ventas}
\]

### Necesitamos 200 ventas para llegar a $6 000
\[
200\,000 \times 0.0003 = 60 \quad \text{vs.} \quad 200\,000 \times 0.006 = 1\,200
\]

Para alcanzar 200 ventas con los mismos porcentajes tendrías que:

* **Incrementar el tráfico** a **600 000 visitas** (3 000 × 0.03 = 90; 600 000 × 0.0003 = 180 – aún corto, pero más cercano).
* **Alzar la tasa de captura de suscriptores** a **5 %** (200 000 × 0.05 = 10 000; 10 000 × 0.02 = 200).
* **Elevar el precio** a **$100** (60 × 100 = $6 000).

---

## 2. ¿Qué puede cambiarse o optimizarse?

| Área | Posible mejora | Impacto esperado |
|------|----------------|------------------|
| **Tráfico** | Aumentar en 50–100 % con campañas pagas, SEO, contenido viral | Más leads, mayor base de suscriptores |
| **Landing / Formulario** | Pruebas A/B de copy, CTA, posición del form, testimonio | 1.5 % → 3–5 % |
| **Nutrición de leads** | Automatización de email, lead magnets, webinars | 2 % → 5–10 % |
| **Oferta** | Incrementar precio o crear upsells/subscriptions | $30 → $50–$100 o + recurring |
| **Retención** | Ofrecer contenido de valor y soporte post‑venta | Reduce churn, maximiza LTV |

> **Tip:** La mayor ganancia suele venir de **ajustar el embudo** (captura + nutrir + vender) antes de escalar tráfico.

---

## 3. Propuesta de ajuste rápido

| Paso | Meta nueva | Comentario |
|------|------------|------------|
| Visitas | 200 000 (mantener) | Se trabaja en la tasa de conversión |
| Suscriptores | 5 % → 10 000 | Se requiere una landing más persuasiva |
| Compras | 5 % → 500 | Se lanza una oferta de valor superior (p.ej. un mini‑curso + acceso a comunidad) |
| Precio | $30 → $50 | Se justifica con contenido de alta calidad + soporte |
| Ingreso | 500 × 50 = $25 000 | Supera el objetivo; permite margen para inversiones |

> **Resultado**: Con una mejora de la tasa de captura al 5 % y la tasa de compra al 5 % (sigue conservador), ya alcanzas **$1 250** con $30 y **$2 500** con $50. Necesitas solo **un 2 % de incremento en la tasa de compra** y **un 1 % de incremento en la captura** para llegar a $6 000 con $30.

---

## 4. Conclusión

- **El plan tal cual no cumple el objetivo.**  
- La multiplicación de los porcentajes es la causa del “muerte” del plan en la fase de conversión.  
- **Recomendación**: No apruebes el plan como está. Pon en marcha un programa de **optimización de funnel** y prueba los supuestos antes de escalar.  
- Si decides seguir adelante, al menos **aumenta la tasa de captura a 5 %** y/o **eleva el precio** a $50 o más.  

¿Te parece una buena ruta a seguir? Podemos diseñar un roadmap de pruebas y métricas para validarlo.