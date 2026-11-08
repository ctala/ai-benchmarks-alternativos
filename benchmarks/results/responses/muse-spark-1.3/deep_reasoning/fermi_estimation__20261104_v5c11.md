# Muse Spark 1.3 — deep_reasoning/fermi_estimation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 2.67 | quality: 1.67
- latency_total: 29.162s | tokens_per_second: 118.7
- input_tokens: 71 | output_tokens: 3461

## Entrada exacta (lo que recibió el modelo)

**user:**

Estima cuantos litros de cafe se consumen al dia en todas las oficinas de Santiago de Chile.

Muestra tu razonamiento paso a paso con cada supuesto numerado.
Da un rango (minimo-maximo) ademas de tu mejor estimacion.
Explica que supuesto tiene mas impacto en el resultado.


## Respuesta completa

**Respuesta corta: ~210.000 litros en un día laboral típico.**

Eso es ~1,4 millones de tazas. Suficiente para llenar unas 5 piscinas de 25 metros cada día.

Esto es solo días hábiles lunes a viernes, no promedio de fin de semana. Es café preparado, no kilos de café en grano.

### Mis supuestos numerados

**1. Población de referencia: Gran Santiago = 6,8 millones**
No la comuna de Santiago (200 mil), sino la ciudad completa + RM urbana.
Rango: 6,2 - 7,5 millones.

**2. Número de personas que trabajan en oficina en Santiago = 1,2 millones**
RM tiene ~3,4 millones de ocupados. Santiago concentra servicios, bancos, Estado, call centers, etc.
Supongo que 35% son oficinistas: administrativos, profesionales, ejecutivos, sector público, que toman café en el lugar de trabajo.
1,2M = 3,4M x 0,35
Rango: 0,8M - 1,6M. Rango bajo si excluyes comercio, salud, educación, construcción, informal. Rango alto si incluyes híbridos y coworks.

Este es el supuesto más difícil de definir: ¿qué es "oficina"?

**3. % de oficinistas que toma café en la oficina habitualmente = 60%**
Chile es un país más teinero que cafetero, el mayor consumidor de té de Latam. No todos toman café, y muchos toman té o ninguno.
Rango: 40% - 80%.

Mejor estimación: 1.200.000 x 0,60 = 720.000 bebedores de café de oficina.

**4. Tazas promedio por bebedor por día laboral = 2,0**
La clásica: una al llegar y una después de almuerzo. Algunos 1, algunos 4-5.
Rango: 1,2 - 3,0 tazas/día.

Mejor estimación: 720.000 x 2,0 = 1.440.000 tazas al día.

**5. Volumen promedio por taza de oficina = 150 ml = 0,15 litros**
En Chile oficina es típicamente café instantáneo en tazón chico o vaso, no mug gigante de 300 ml de EE.UU. ni espresso de 60 ml.
Rango: 0,12 - 0,20 litros.

**6. Solo cuenta día laboral.**
El sábado/domingo el consumo en oficinas cae a casi cero. Si quieres promedio de 7 días, divide por ~1,4.

### Cálculo mejor estimación

> 1.200.000 oficinistas x 0,60 bebedores x 2,0 tazas x 0,15 L
> = **216.000 litros / día**
> Redondeo a **~200.000 - 220.000 L/día**

### Rango mínimo-máximo

**Mínimo:** 800.000 x 0,40 x 1,2 x 0,12 = **~46.000 L/día**
Poca gente en oficina, muchos toman té, 1 café chico.

**Máximo:** 1.600.000 x 0,80 x 3,0 x 0,20 = **~768.000 L/día**
Todos en oficina, cultura muy cafetera, 3 tazas grandes.

> **Rango: 50.000 - 770.000 litros/día, mejor estimación ~210.000**

Estamos seguros del orden de magnitud: decenas de miles a menos de un millón. No son 2.000 litros ni 20 millones.

Chequeo de cordura: 1,44M tazas x ~7g de café instantáneo por taza = ~10 toneladas de café al día en oficinas de Santiago. En 250 días hábiles = 2.500 toneladas/año. Chile importa ~20.000-25.000 toneladas/año, así que oficinas de Santiago serían ~10-12% del total nacional. Suena plausible.

### ¿Qué supuesto tiene más impacto?

**El 2: cuántos oficinistas hay.**

Porque la fórmula es multiplicativa:

Resultado = Oficinistas x %Bebedores x Tazas x Volumen

Un error de 10% en cualquiera pega 10% al resultado, pero el 2 es el que tiene más incertidumbre absoluta y conceptual.

Si me equivoco en 400.000 oficinistas, el resultado se mueve en ~70.000-100.000 litros de un golpe. En cambio, si la taza es de 150 ml o 180 ml, solo se mueve ~40.000 litros.

El segundo más importante es el **4: tazas por persona**, porque varía de 1 a 3 (factor 3x). Y en Chile el **3: % que toma café vs té** también es muy incierto por la cultura del té.

En resumen: si quieres afinar la estimación, no midas los ml de la taza. Cuenta mejor cuánta gente trabaja realmente en oficinas en Santiago.