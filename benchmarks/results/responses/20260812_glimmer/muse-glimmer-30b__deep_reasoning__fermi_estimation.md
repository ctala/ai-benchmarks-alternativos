# Muse Glimmer 30B — deep_reasoning/fermi_estimation

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 2.91 | quality: 1.67
- latency_total: 20.252s | tokens_per_second: 137.6
- input_tokens: 119 | output_tokens: 2786
- judge_score: 4.4 | justificación: 

## Respuesta completa

Una estimación de orden de magnitud se puede armar con 5 supuestos encadenados. Todo es para un día laboral típico, de lunes a viernes. Si lo quieres promediar a calendario hay que multiplicar por 250/365 ≈ 0.69.

**1. Ocupados en la Región Metropolitana de Santiago**
RM Santiago tiene ~7,1 millones de habitantes. Ocupados INE 2024 ≈ 3,6 a 3,8 millones.
Mejor: 3,7 millones. Rango 3,6 - 3,8 M.

**2. Fracción que trabaja en entorno de oficina**
No todo ocupado está en oficina. Se excluye construcción, industria, comercio de piso, transporte, etc.
Rango 35% a 55%. Mejor 45%.
Trabajadores de oficina = 3,7 M x 0,45 = 1,67 M
Rango: 1,26 M a 2,09 M

**3. Fracción de esos trabajadores que toma café en la oficina**
En Chile el café es mayoritario pero no universal.
Rango 60% a 80%. Mejor 70%.
Bebedores = 1,67 M x 0,70 = 1,17 M
Rango: 0,78 M a 1,63 M

**4. Tazas por bebedor por día laboral**
En oficina hay café de filtro, máquina y espresso. Promedio mixto.
Rango 1,2 a 2,5 tazas/día. Mejor 1,8 tazas/día.
Tazas/día = 1,17 M x 1,8 = 2,10 M tazas
Rango: 0,91 M a 4,18 M tazas

**5. Volumen por taza**
Filtros de oficina ~200 ml, espresso ~60 ml. Promedio ponderado.
Rango 120 ml a 200 ml. Mejor 150 ml = 0,15 L.
Litros/día laboral = tazas x volumen

Mejor estimación:
2,10 M tazas x 0,15 L = **~315.000 litros/día laboral**, ~315 m³.

Rango:
Mínimo: 1,26 M oficina x 0,60 bebedores x 1,2 tazas x 0,12 L = **~109.000 litros/día**
Máximo: 2,09 M oficina x 0,80 bebedores x 2,5 tazas x 0,20 L = **~836.000 litros/día**

En promedio calendario, incluyendo fines de semana y vacaciones:
Mejor ~315.000 x 250/365 ≈ 216.000 L/día
Rango ~75.000 a 573.000 L/día calendario.

El supuesto con más impacto es la combinación del **número de trabajadores de oficina** y las **tazas por persona al día**. El número de ocupados en oficina fija la base poblacional y varía ±30% con el rango 35-55%. Las tazas/día varía ±40% con el rango 1,2-2,5. Juntos dominan la incertidumbre, mucho más que el volumen por taza o el % de bebedores, que son relativamente estables.

Es una estimación de orden de magnitud: entre ~100 mil y ~850 mil litros de café líquido preparado se sirven en un día laboral típico en las oficinas de Santiago, con un punto central alrededor de 300-350 mil litros.