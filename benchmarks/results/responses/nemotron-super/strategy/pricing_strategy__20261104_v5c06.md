# Nemotron 3 Super — strategy/pricing_strategy

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 6.91 | quality: 7.5
- latency_total: 132.018s | tokens_per_second: 55.5
- input_tokens: 208 | output_tokens: 7329

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

Aquí tienes el análisis completo para tu decisión de subir el precio de **$60 → $89/mes** (+48,3 %).

---

## 1. LTV / CAC: actual vs. después del aumento

Tu LTV actual se calcula como ingresos (sin descontar costos de servicio):

| Métrica | Valor actual | Fórmula |
|---------|-------------|---------|
| ARPU | $60 / mes | Dado |
| Churn mensual | 7 % | Dado |
| Vida promedio del cliente | ~14,3 meses | 1 / 0,07 |
| **LTV (ingresos)** | **$840** | $60 × 14,3 |
| **CAC** | **$120** | Dado |
| **LTV / CAC** | **7,0** | $840 / $120 |

**Benchmark saludable:** > 3,0. Tú estás en **7,0**, lo cual es excelente.

### Si subes a $89 y el churn se mantiene en 7 %
- Vida promedio: 14,3 meses
- LTV nuevo: $89 × 14,3 = **$1.271**
- **LTV / CAC: 10,6**

Incluso si el churn empeora, el ratio se mantiene muy por encima del umbral de seguridad.

---

## 2. Impacto estimado en el churn (benchmarks SaaS)

Un aumento de precio del **~48 %** es significativo. Según benchmarks de Price Intelligently / ProfitWell y estudios de SaaS Capital:

- Un aumento de precio > 30 % suele generar un **churn adicional de 1 a 5 puntos porcentuales mensuales** en los primeros 6-12 meses.
- Como tu precio destino ($89) sigue dentro del rango competitivo ($29 – $149) y tu costo por usuario es bajo ($8), el valor percibido puede amortiguar la fuga.

**Supuestos de churn mensual usados en los escenarios:**

| Escenario | Churn mensual | Interpretación |
|-----------|--------------|----------------|
| **Optimista** | 8 % | +1 pp (aumento relativo ~14 %). Buena comunicación y valor agregado. |
| **Realista** | 9,5 % | +2,5 pp (aumento relativo ~36 %). Impacto moderado, algunos clientes sensibles al precio se van. |
| **Pesimista** | 12 % | +5 pp (aumento relativo ~71 %). Resistencia fuerte, competidores directos más baratos captan clientes. |

---

## 3. Modelo de 3 escenarios (cohorte actual de 200 clientes, 12 meses)

Modelo sin nuevos clientes (solo para medir el impacto sobre tu base actual).  
Contribución bruta mensual por cliente: **$89 – $8 = $81** (vs. $52 actual).

| Escenario | Churn mensual | LTV ($89) | LTV / CAC | Ingresos acumulados 12 meses | Contribución bruta acumulada 12 meses | Diferencia vs. estado actual | Clientes restantes al mes 12 |
|-----------|--------------|-----------|-----------|------------------------------|---------------------------------------|------------------------------|------------------------------|
| **Estado actual** | 7 % | $840 | 7,0 | $99.800 | $86.500 | — | ~84 clientes |
| **Optimista** | 8 % | $1.113 | 9,3 | $138.700 | $126.200 | **+$39.700 (+46 %)** | ~75 clientes |
| **Realista** | 9,5 % | $937 | 7,8 | $130.800 | $119.100 | **+$32.600 (+38 %)** | ~61 clientes |
| **Pesimista** | 12 % | $742 | 6,2 | $116.400 | $105.900 | **+$19.400 (+22 %)** | ~44 clientes |

### Puntos clave del modelo
- **Incluso en el escenario pesimista**, subir el precio genera **más contribución bruta** que mantener los $60, porque el margen por cliente sube de $52 a $81 (+56 %).
- **Punto de equilibrio de clientes:** para igualar tu contribución mensual actual ($10.400), con el nuevo precio necesitas solo **128 clientes** (200 × $52 ÷ $81). Es decir, **podrías perder hasta 72 clientes (36 % de tu base)** y seguir generando el mismo efectivo mensual.
- **Payback de CAC:** con el nuevo precio y margen de $81, recuperas los $120 de CAC en **~1,5 meses** de contribución (vs. ~2,3 meses actuales).

---

## 4. Recomendación con números concretos

**Sí, sube el precio a $89/mes**, pero hazlo de forma segmentada y con aviso previo.

### Por qué (números):
- En el escenario **realista**, aumentas la contribución bruta de tu base actual en **+$32.600 en 12 meses** (+38 %).
- Tu **LTV/CAC se mantiene entre 6,2 y 9,3**, muy por encima del mínimo saludable de 3.
- El **punto de equilibrio es muy indulgente**: puedes permitirte perder hasta el 36 % de los clientes actuales y no perder dinero mensualmente.
- $89 está dentro del rango de mercado ($29–$149), no te posiciona como el más caro.

### Condición para ejecutar:
Debes acompañar el aumento con **mejora de valor percibido** (nuevas funcionalidades, mejor soporte, integraciones, etc.) para justificar el +48 % y mantener el churn más cerca del escenario optimista (8 %) que del pesimista (12 %).

---

## 5. Estrategia de implementación recomendada

No subas el precio a todos los 200 clientes el mismo día sin aviso. Usa una estrategia híbrida:

### A. Nuevos clientes (inmediato)
- **Precio: $89/mes desde hoy.** No hay razón para dar descuento a quien llega nuevo.

### B. Clientes actuales (transición de 60 a 90 días)
1. **Aviso con 60 días de antelación** por email y dentro de la app. Explica el "por qué" (nuevas features, mejor estabilidad, soporte).
2. **Opción A (recomendada): Plan anual con descuento.**
   - $890/año (equivalente a $74,17/mes, 2 meses gratis).
   - Objetivo: asegurar flujo de caja, reducir churn y bloquear al cliente por 12 meses.
3. **Opción B: Grandfathering temporal.**
   - Mantener $60/mes durante 6 meses, luego pasar a $89. Da tiempo de adaptación.
4. **Opción C: Descuento de lealtad.**
   - $79/mes si se comprometen a renovar por 12 meses (menos agresivo que el anual, pero fideliza).

### C. Segmentación (opcional pero poderosa)
- **Clientes de alto uso / enterprise:** subir a $89 sin descuento (menos sensibles al precio).
- **Clientes pequeños o inactivos:** ofrecer el plan anual o el grandfathering temporal para retenerlos.

### D. Comunicación sugerida
> "Hemos mejorado [X, Y, Z] en la plataforma. Para seguir invirtiendo en estas mejoras, ajustamos nuestro precio a $89/mes a partir del [fecha]. Como cliente actual, puedes mantener tu plan actual por 6 meses más o cambiar hoy al plan anual a $890 y ahorrar el equivalente a 2 meses."

---

## Resumen de acción inmediata

| Acción | Plazo | Impacto esperado |
|--------|-------|------------------|
| Nuevo precio $89 para leads nuevos | Inmediato | Mejora LTV/CAC de nuevos clientes a >9 |
| Email de aviso a 200 clientes actuales | Semana 1 | Reduce sorpresa y churn por enojo |
| Lanzar plan anual $890/año | Semana 2 | Bloquea flujo de caja y reduce churn |
| Migración de clientes actuales a $89 | Día 60-90 | Contribución mensual por cliente sube de $52 a $81 |

Si logras mantener el churn en **≤ 9,5 %**, esta es una de las decisiones de crecimiento más rentables que puedes tomar este año.