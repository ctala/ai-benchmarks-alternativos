# Muse Ember — deep_reasoning/fermi_estimation

- model_id: `meta/muse-ember`
- success: True  | final: 1.7 | quality: 0.0
- latency_total: 22.45s | tokens_per_second: 470.8
- input_tokens: 71 | output_tokens: 10569

## Entrada exacta (lo que recibió el modelo)

**user:**

Estima cuantos litros de cafe se consumen al dia en todas las oficinas de Santiago de Chile.

Muestra tu razonamiento paso a paso con cada supuesto numerado.
Da un rango (minimo-maximo) ademas de tu mejor estimacion.
Explica que supuesto tiene mas impacto en el resultado.


## Respuesta completa

### Respuesta corta

**~100.000 litros por día hábil** en oficinas del Gran Santiago.
**Rango plausible: 55.000 - 230.000 litros/día hábil.**

Eso es ~750.000 tazas al día, unos 8 toneladas de café en grano.

Es una estimación de Fermi: día hábil promedio martes-jueves, café preparado y consumido *dentro* de la oficina. No incluye cafeterías de la calle, ni hogar. Si promedias los 7 días de la semana, con fin de semana cerrado, baja a ~70.000 L/día calendario.

### Razonamiento paso a paso

**1. Personas ocupadas en la Región Metropolitana**
Población RM ~8,0 millones. Población en edad de trabajar ~6,5 M, participación ~60%, desocupación ~8%.
**Supuesto: 3,7 millones de ocupados.**

**2. ¿Cuántos trabajan en oficina?**
Profesionales, técnicos, administrativos, gerentes, funcionarios públicos, personal de finanzas, TI, etc. Excluyo comercio en tienda, construcción en obra, transporte, salud/educación en terreno, gastronomía, industria en planta.
**Supuesto: 38% de los ocupados.**
3,7 M x 0,38 = **1,41 millones de puestos de oficina.**

**3. ¿Cuántos están presenciales un día hábil promedio?**
Post-pandemia hay híbrido. Muchos van 100%, otros 2-3 días. Promediando lunes a viernes:
**Supuesto: 65% presencial.**
1,41 M x 0,65 = **914.000 personas presentes.**

**4. ¿Cuántos de esos toman café en la oficina ese día?**
En Chile compite fuerte el té, el mate y el agua. Entre oficinistas la penetración es mayor que en la población general, pero no es universal.
**Supuesto: 55% toma al menos un café en la oficina.**
914.000 x 0,55 = **503.000 consumidores.**

**5. ¿Cuántas tazas por consumidor?**
Muchos 1, muchos 2, algunos 3-4 en oficinas con cafetera buena.
**Supuesto: 1,5 tazas / consumidor / día.**
503.000 x 1,5 = **754.000 tazas/día.**

**6. ¿Qué volumen tiene una taza promedio?**
Mezcla en oficina chilena: espresso/cortado 80-100 ml, filtrado/americano 160-190 ml, café con leche 200 ml. Ponderado a la baja porque en cocina de oficina predomina lo chico.
**Supuesto: 120 ml = 0,12 L por taza.**
754.000 x 0,12 = **90.500 litros.**

**7. Extra por visitas, clientes, reuniones**
Café para gente que no es parte del plantel fijo.
**Supuesto: +10%.**
90.500 x 1,10 = **99.500 litros ≈ 100.000 litros/día hábil.**

### Rango mínimo - máximo

No es sumar errores, es multiplicarlos. Cambio los supuestos a la vez a un escenario bajo y a uno alto, pero sin llevar todos al extremo absoluto:

**Mínimo ~55.000 L**
3,5 M ocupados x 35% oficina x 60% presencial x 50% bebedores x 1,3 tazas x 0,11 L x 1,05 = **55.180 L**

**Máximo ~227.000 L**
3,9 M ocupados x 43% oficina x 75% presencial x 65% bebedores x 1,8 tazas x 0,14 L x 1,10 = **226.600 L**

Por eso el rango es ancho: 55.000 a 230.000. El valor central geométrico está cerca de los 100.000 L.

### ¿Qué supuesto impacta más?

Todos multiplican, pero no tienen la misma incertidumbre:

* Ocupados: 3,5 a 3,9 M = solo **±5%**. Dato del INE, bastante sólido.
* % oficina: 33% a 45% = **±15-18%**
* % presencial: 55% a 80% = **-15% / +23%**
* % bebedores: 45% a 70% = **-18% / +27%**
* Tazas por consumidor: 1,2 a 2,0 = **-20% / +33%**
* Volumen por taza: 90 a 160 ml = **-25% / +33%**

**El que más impacta es el bloque de consumo por persona presente: % bebedores x tazas x ml.**

Individualmente tazas y volumen son los más inciertos (factor casi 2 entre una oficina de espresso chico y una de latte grande), y juntos pueden variar por un factor 3-4. No hay estadística oficial de cuántos cafés se toman *dentro* de oficinas chilenas, depende totalmente de la cultura de cada empresa.

El segundo bloque importante es la definición de "oficina" y la presencialidad híbrida, también sin dato único.

### Chequeo cruzado de arriba hacia abajo

Chile consume del orden de 20.000 toneladas de café verde al año, ~55 t/día. A ~12 litros de bebida por kg de café, son ~650.000 L/día para todo Chile, en hogar + cafeterías + oficinas + restaurantes.

Santiago concentra ~40-45% por población e ingreso: ~260.000-290.000 L/día en total. Si las oficinas son entre un tercio y la mitad de eso, quedan **90.000-140.000 L/día**, justo en torno a nuestra mejor estimación de 100.000 L.

Eso también sugiere que el máximo de 230.000 L es un límite superior poco probable: implicaría que las oficinas fueran >75% de todo el café de Santiago.