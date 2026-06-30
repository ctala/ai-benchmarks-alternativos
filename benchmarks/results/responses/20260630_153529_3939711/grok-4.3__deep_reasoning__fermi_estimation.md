# Grok 4.3 — deep_reasoning/fermi_estimation

- model_id: `x-ai/grok-4.3`
- success: True  | final: 4.52 | quality: 3.74
- latency_total: 8.965s | tokens_per_second: 108.2
- input_tokens: 192 | output_tokens: 970

## Respuesta completa

**Estimación paso a paso (supuestos numerados)**

1. Población de Santiago metropolitano: 6,8 millones de habitantes (dato realista a 2023-2024).
2. Tasa de empleo: 48 % de la población total está empleada (considerando niños, jubilados, inactivos y desempleo). → 3,26 millones de trabajadores.
3. Porcentaje que trabaja en oficinas: 28 % (resto son retail, construcción, transporte, industria, comercio, etc.). → 913 000 trabajadores de oficina.
4. Consumo promedio por trabajador de oficina: 1,8 tazas al día (mezcla de quienes toman 0-1 taza y quienes toman 3-4).
5. Tamaño promedio de taza: 150 ml (0,15 L). Muchos usan 120 ml o 180 ml, pero 150 ml es un punto medio razonable.

**Cálculo central**  
913 000 trabajadores × 1,8 tazas × 0,15 L = **246 000 litros/día**.

**Rango (mínimo-máximo)**  
- Escenario bajo: 700 000 trabajadores de oficina × 1,4 tazas × 0,13 L = **128 000 litros**.  
- Escenario alto: 1 100 000 trabajadores de oficina × 2,3 tazas × 0,17 L = **427 000 litros**.  

**Mejor estimación puntual: 220 000 – 280 000 litros/día** (rango más probable).

**Supuesto de mayor impacto**  
El supuesto #3 (porcentaje de trabajadores que realmente están en oficinas) es el que más mueve el resultado. Variar este porcentaje entre 22 % y 35 % cambia el total en ±80 000–100 000 litros, más que cualquier otro supuesto individual.

---

**Respuesta final**  
~250 000 litros/día (rango probable 130 000 – 430 000 L).