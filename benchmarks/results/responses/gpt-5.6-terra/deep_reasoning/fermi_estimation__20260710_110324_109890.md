# GPT-5.6 Terra — deep_reasoning/fermi_estimation

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.76 | quality: 7.54
- latency_total: 10.475s | tokens_per_second: 102.0
- input_tokens: 68 | output_tokens: 1068
- judge_score: 4.4 | justificación: 

## Respuesta completa

**Estimación Fermi: litros de café consumidos por día en oficinas de Santiago de Chile**

Interpretaré “en todas las oficinas” como el café consumido **durante una jornada laboral presencial** por personas que trabajan en oficinas en Santiago, ya sea preparado en la oficina o comprado cerca y llevado al trabajo. No incluye café consumido en el hogar, restaurantes fuera de horario laboral ni trabajadores principalmente manuales/industriales.

## Supuestos

1. **Personas que trabajan presencialmente en oficinas en Santiago**
   - Mínimo: **1,0 millón**
   - Mejor estimación: **1,4 millones**
   - Máximo: **1,8 millones**

   Esto incluye servicios profesionales, finanzas, administración pública, tecnología, comercio administrativo, call centers, etc., descontando parcialmente trabajo remoto e híbrido.

2. **Porcentaje de trabajadores de oficina que toma café durante el día laboral**
   - Mínimo: **55%**
   - Mejor estimación: **68%**
   - Máximo: **80%**

3. **Tazas promedio por persona que sí toma café**
   - Mínimo: **1,2 tazas/día**
   - Mejor estimación: **1,8 tazas/día**
   - Máximo: **2,6 tazas/día**

4. **Volumen promedio por taza**
   - Mínimo: **180 ml** (café pequeño o de máquina)
   - Mejor estimación: **220 ml**
   - Máximo: **250 ml** (tazón o café con leche más grande)

---

## Cálculo

La fórmula es:

\[
\text{Litros/día} =
\text{trabajadores en oficina}
\times \% \text{ que toma café}
\times \text{tazas por persona}
\times \text{litros por taza}
\]

### Escenario mínimo

\[
1{,}0\,M \times 55\% \times 1{,}2 \times 0{,}18
\]

\[
= 118.800 \text{ litros/día}
\]

**≈ 120 mil litros diarios**

---

### Mejor estimación

\[
1{,}4\,M \times 68\% \times 1{,}8 \times 0{,}22
\]

\[
= 377.300 \text{ litros/día}
\]

**≈ 380 mil litros diarios**

---

### Escenario máximo

\[
1{,}8\,M \times 80\% \times 2{,}6 \times 0{,}25
\]

\[
= 936.000 \text{ litros/día}
\]

**≈ 940 mil litros diarios**

---

## Resultado

| Escenario | Consumo estimado |
|---|---:|
| Mínimo | **~120.000 litros/día** |
| Mejor estimación | **~380.000 litros/día** |
| Máximo | **~940.000 litros/día** |

Por lo tanto, una respuesta razonable es:

> **En las oficinas de Santiago podrían consumirse del orden de 120 mil a 940 mil litros de café por día laboral, con una mejor estimación cercana a 380 mil litros diarios.**

Equivale aproximadamente a **1,7 millones de tazas diarias** en el escenario central.

## Supuesto con mayor impacto

El supuesto de mayor impacto es el **número de personas que efectivamente trabaja presencialmente en oficinas**.

Esto se debe a que multiplica todo el resultado: una variación de, por ejemplo, 300.000 personas presenciales cambia el cálculo en decenas de miles de litros diarios. Además, es difícil de estimar por factores como:

- teletrabajo e híbrido;
- definición de “oficina”;
- límites geográficos de Santiago;
- inclusión o no de trabajadores de atención, comercio y sector público.

El segundo supuesto más importante es la **cantidad de tazas por consumidor**, porque pasar de cerca de una taza a dos tazas por día casi duplica el consumo total.