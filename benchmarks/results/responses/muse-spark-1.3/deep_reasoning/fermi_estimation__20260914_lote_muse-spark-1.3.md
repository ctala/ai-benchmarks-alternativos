# Muse Spark 1.3 — deep_reasoning/fermi_estimation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 2.68 | quality: 1.67
- latency_total: 21.979s | tokens_per_second: 147.2
- input_tokens: 70 | output_tokens: 3236

## Entrada exacta (lo que recibió el modelo)

**user:**

Estima cuantos litros de cafe se consumen al dia en todas las oficinas de Santiago de Chile.

Muestra tu razonamiento paso a paso con cada supuesto numerado.
Da un rango (minimo-maximo) ademas de tu mejor estimacion.
Explica que supuesto tiene mas impacto en el resultado.


## Respuesta completa

Esta es una estimación tipo Fermi para un día laboral normal (lunes a viernes), no un promedio de fin de semana. Solo cuenta el café consumido *en* la oficina.

La fórmula es:

**Litros/día = Población x % empleados x % oficinistas x % presencial x % que toma café x tazas por persona x litros por taza**

### Supuestos numerados

**1. Población del Gran Santiago: 6,5 millones**
Santiago RM tiene ~7-8 millones, Gran Santiago urbano ~6-6,5. Uso 6,5.
Rango: 6,0 - 7,0 millones

**2. Fracción con empleo: 38,5% de la población**
No todos trabajan: niños, estudiantes, jubilados, desempleados. ~70% tiene +15 años, ~60% participa laboralmente, ~92% está empleado. 0,70 x 0,60 x 0,92 = 0,386.
6,5M x 0,385 = ~2,5 millones de trabajadores.
Rango: 35% - 41%

**3. Fracción que trabaja en oficina: 35%**
Descontamos comercio, construcción, transporte, salud, educación en sala, fábricas, delivery, etc. Chile es servicios, pero no todos están en escritorio.
2,5M x 0,35 = ~876.000 oficinistas.
Rango: 25% - 45%. Este es el supuesto más difuso: ¿qué cuenta como "oficina"?

**4. Fracción presencial en un día dado: 70%**
Descontamos teletrabajo, vacaciones, licencias, feriados, trabajo en terreno y reuniones fuera.
876.000 x 0,70 = ~613.000 personas físicamente en una oficina hoy.
Rango: 60% - 80%

**5. Fracción que toma café en la oficina: 55%**
Chile es país de té, no de café. El consumo per cápita de café es muy bajo (~0,8 kg/año vs 5-6 kg en Brasil/Colombia). En oficina sube por la máquina gratis y presión social, pero muchos toman té.
613.000 x 0,55 = ~337.000 consumidores de café.
Rango: 40% - 70%

**6. Tazas promedio por consumidor por jornada: 2,0**
Rutina típica: una al llegar + una post-almuerzo. Algunos 1, algunos 3-4.
337.000 x 2,0 = ~674.000 tazas al día.
Rango: 1,5 - 2,5 tazas

**7. Volumen por taza de oficina: 0,15 litros**
En oficina no es el mug de 300ml, es el vasito plástico/dispensador o taza chica de máquina: 120-200 ml. Uso 150 ml.
674.000 x 0,15 = **~101.000 litros**
Rango: 0,12 - 0,20 litros

### Resultado

**Mejor estimación: ~100.000 litros al día**

Eso es ~674.000 tazas al día, o ~0,11 litros por cada oficinista (tome o no tome). Para visualizarlo: como llenar al 4% una piscina olímpica cada día laboral.

**Rango mínimo-máximo: 23.000 - 360.000 litros al día**

* Mínimo: 6,0M x 0,35 x 0,25 x 0,60 x 0,40 x 1,5 x 0,12 = ~22.700 L
* Máximo: 7,0M x 0,41 x 0,45 x 0,80 x 0,70 x 2,5 x 0,20 = ~361.600 L

Redondeando: **25.000 a 350.000 litros/día.**

### ¿Qué supuesto tiene más impacto?

El **Supuesto 3: % que trabaja en oficina.**

¿Por qué?
1. Tiene el mayor rango de incertidumbre: 25% a 45% es un factor de 1,8x (casi duplica el resultado por sí solo). Es más incierto que población o presencialidad.
2. Es un problema de definición: ¿contamos call centers, bancos, sector público, coworks, recepcionistas? ¿Contamos a alguien híbrido que va 2 días? Cambiar la definición mueve cientos de miles de personas.
3. Está multiplicado por todo lo demás. Un error de 10 puntos aquí (ej. 35% vs 45%) cambia el resultado en ~29.000 litros, mucho más que equivocarse en 20 ml por taza.

El segundo más importante es el **Supuesto 5 (% que toma café)**, justamente por la particularidad chilena: si Santiago fuera Bogotá o São Paulo, ese 55% sería 75-80% y la estimación se dispararía.