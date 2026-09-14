# Fugu Max — strategy/pricing_strategy

- model_id: `sakana/fugu-max`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 103.404s | tokens_per_second: 103.8
- input_tokens: 252 | output_tokens: 10730

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

## Supuestos

Asumo que:

- El precio es por cliente/cuenta.
- Los $8/mes representan el costo variable por cliente.
- El CAC permanece en $120.
- No hay expansión de ingresos, upsells ni nuevas altas en el modelo de la base actual.
- El churn es churn mensual de clientes, no necesariamente churn de ingresos.

Si realmente son **$8 por usuario** y cada cliente tiene varios usuarios, hay que sustituir $8 por `$8 × usuarios promedio por cliente`.

---

# 1. LTV/CAC actual y con precio de $89

### Situación actual

Tu LTV reportado es:

\[
LTV = 14 \text{ meses} \times \$60 = \$840
\]

\[
LTV/CAC = \$840/\$120 = 7.0x
\]

Esto es un ratio fuerte, aunque está calculado sobre ingresos, no sobre margen bruto.

Con costo variable de $8:

- Margen bruto por cliente: **$60 - $8 = $52/mes**
- Margen bruto porcentual: **86.7%**
- LTV basado en margen: **$52 × 14 = $728**
- LTV/CAC basado en margen: **$728/$120 = 6.07x**
- Payback del CAC: **$120/$52 = 2.3 meses**

### Con precio de $89

El margen por cliente sería:

\[
\$89-\$8=\$81
\]

- Incremento de precio: **48.3%**
- Margen bruto por cliente: **$81/mes**
- Margen bruto porcentual: **91.0%**
- Payback del CAC: **$120/$81 = 1.5 meses**

Si el churn permaneciera igual y conservaras la vida promedio de 14 meses:

\[
LTV = \$89 \times 14 = \$1,246
\]

\[
LTV/CAC = \$1,246/\$120 = 10.38x
\]

Sobre margen:

\[
LTV_{\text{margen}}=\$81 \times 14=\$1,134
\]

\[
LTV/CAC_{\text{margen}}=9.45x
\]

La pregunta crítica es cuánto aumentará el churn.

---

# 2. Impacto estimado en churn

Tu churn actual de **7% mensual** implica una retención anual aproximada de:

\[
0.93^{12}=41.9\%
\]

Es decir, sin nuevas altas, aproximadamente **58% de los clientes actuales se perderían durante un año**. Para SaaS SMB, 7% mensual está en la parte alta del rango habitual.

Una subida de **48.3%** es mucho mayor que un incremento de precio típico de 5%-15%. Por tanto, no asumiría que el churn se mantendrá en 7%.

Como rango operativo:

- **Optimista:** aumento de 0.5 puntos porcentuales.
- **Realista:** aumento de 2 puntos porcentuales.
- **Pesimista:** aumento de 5 puntos porcentuales.

No son benchmarks exactos; el impacto dependerá de la dependencia del producto, valor percibido, facilidad de sustitución y sensibilidad al precio.

---

# 3. Tres escenarios

## Economía unitaria

| Escenario | Churn mensual | Vida promedio | LTV de ingresos | LTV/CAC | LTV sobre margen | LTV/CAC sobre margen |
|---|---:|---:|---:|---:|---:|---:|
| Actual | 7.0% | 14.0 meses | $840 reportado | **7.0x** | $728 | **6.1x** |
| Optimista | 7.5% | 13.3 meses | $1,187 | **9.9x** | $1,080 | **9.0x** |
| Realista | 9.0% | 11.1 meses | $989 | **8.2x** | $900 | **7.5x** |
| Pesimista | 12.0% | 8.3 meses | $742 | **6.2x** | $675 | **5.6x** |

El escenario realista mejora claramente la economía por cliente. El pesimista todavía genera un margen atractivo, pero el LTV/CAC cae frente a tu situación actual.

## Impacto sobre los 200 clientes actuales

Este cálculo supone que no entran clientes nuevos y que todo el grupo empieza a pagar $89.

| Escenario | Clientes después de 12 meses | MRR después de 12 meses | Margen bruto mensual |
|---|---:|---:|---:|
| Sin subir precio, churn 7% | 84 | $5,028 | $4,358 |
| Optimista, churn 7.5% | 79 | $6,986 | $6,359 |
| Realista, churn 9% | 64 | $5,732 | $5,216 |
| Pesimista, churn 12% | 43 | $3,845 | $3,499 |

Al inicio:

- MRR actual: **200 × $60 = $12,000**
- MRR a $89: **200 × $89 = $17,800**
- Incremento inicial de MRR: **$5,800/mes**
- Margen bruto actual: **$10,400/mes**
- Margen bruto a $89: **$16,200/mes**

El precio de $89 sigue siendo mejor que mantener $60 mientras el churn no suba demasiado.

### Punto de equilibrio

Usando tu LTV actual reportado de $840:

\[
\$89/churn = \$840
\]

El churn máximo para conservar el mismo LTV sería aproximadamente:

\[
churn = 10.6\%
\]

Sobre margen bruto, el punto de equilibrio es aproximadamente **11.1% mensual**.

Por tanto:

- Por debajo de aproximadamente **9%**, la subida parece claramente atractiva.
- Entre **9% y 10.5%**, sigue siendo razonable, pero requiere vigilancia.
- Por encima de **10.5%-11%**, la mejora de precio empieza a perder buena parte de su beneficio económico.

---

# 4. Recomendación

## Sí subiría el precio, pero no haría una migración inmediata de los 200 clientes

Mi recomendación concreta sería:

1. **Nuevos clientes:** ofrecer $89 inmediatamente.
2. **Clientes actuales:** transición de 6 a 12 meses.
3. **Clientes sensibles al precio:** ofrecer un plan inferior, no necesariamente mantener el mismo producto completo a $60.
4. **No hacer grandfathering indefinido para toda la base.**

El precio de $89 está dentro del rango competitivo que mencionas, por lo que es defendible si el producto entrega suficiente valor y no está posicionado como una herramienta básica.

La razón principal para subir es que el margen aumenta de $52 a $81 por cliente, un incremento de aproximadamente **56% en margen por cliente**, mientras el churn no supere aproximadamente 10%-11%.

Sin embargo, tu churn actual de 7% ya es relativamente alto. Antes de atribuir todo al precio, revisaría:

- Clientes con poco uso.
- Clientes que no activaron funciones clave.
- Segmentos con mayor churn.
- Número de usuarios por cuenta.
- Cancelaciones por falta de valor versus precio.
- Si el CAC de $120 incluye ventas, soporte y marketing realmente.

---

# 5. Estrategia de implementación

## Opción recomendada

### Para nuevos clientes

- Precio estándar: **$89/mes**
- Plan anual: entre **$79 y $80/mes**, cobrado anualmente
- Mantener quizás un plan de entrada de **$49-$59**, pero con menos funcionalidades, usuarios o límites

Evitaría ofrecer $89 con descuentos permanentes. Es mejor presentar claramente:

- Starter: menor precio, menor capacidad
- Standard: $89
- Pro: precio superior, más automatización, usuarios o soporte

## Para los 200 clientes actuales

Propondría:

### Fase 1: comunicación y protección

- Aviso con **60 días de anticipación**
- Explicar mejoras de producto y el motivo del cambio
- Mantener $60 durante un período de gracia de **60-90 días**

### Fase 2: precio transitorio

Una alternativa concreta:

- Meses 1-3: $60
- Meses 4-9: **$79**
- Mes 10 en adelante: **$89**

O, de manera más simple:

- Ofrecer **$79 durante 12 meses** a los clientes actuales que acepten prepago anual
- Después, pasar a $89

Esto reduce el impacto psicológico de pasar directamente de $60 a $89, pero evita congelar para siempre una base con menor precio.

## Grandfathering selectivo

Usaría grandfathering permanente solamente para:

- Clientes estratégicos.
- Clientes con contratos especiales.
- Cuentas grandes que puedan generar referencias.
- Clientes con alta probabilidad de cancelar ante cualquier aumento.

Para el resto, limitaría el precio antiguo a una transición de máximo 3-12 meses. Mantener permanentemente una base a $60 puede generar:

- Complejidad de soporte y facturación.
- Comparaciones entre clientes.
- Menor MRR por cliente.
- Dificultad para subir precios posteriormente.

## Métricas y umbrales de decisión

Mide por cohorte y por segmento:

- Churn mensual de clientes.
- Churn de ingresos.
- MRR perdido por cancelaciones.
- Conversión a anual.
- Uso de funcionalidades clave.
- Cancelaciones por precio versus falta de valor.

Usaría estas reglas:

- **Churn hasta 8.5%-9%:** avanzar hacia $89.
- **Churn entre 9% y 10.5%:** mantener $79 por más tiempo y mejorar el onboarding.
- **Churn superior a 10.5% durante dos meses consecutivos:** detener la migración completa y revisar segmentación o packaging.
- **Churn superior a 12%:** no aplicar $89 universalmente; crear planes diferenciados.

## Conclusión

Subir a $89 parece financieramente conveniente, especialmente porque reduce el payback del CAC de **2.3 a 1.5 meses** y eleva el margen mensual por cliente de **$52 a $81**. No obstante, el aumento de 48.3% es demasiado grande para aplicarlo sin transición.

La estrategia que elegiría sería:

- **$89 para todos los nuevos clientes desde ahora.**
- **60-90 días de aviso para clientes actuales.**
- **$79 durante 6-12 meses como precio transitorio.**
- **$89 posteriormente.**
- **Plan de entrada reducido para clientes muy sensibles al precio.**
- Decisión final basada en mantener el churn por debajo de aproximadamente **9%-10% mensual**.