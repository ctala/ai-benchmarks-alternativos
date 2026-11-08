# Muse Wonder — deep_reasoning/fermi_estimation

- model_id: `meta/muse-wonder`
- success: True  | final: 2.36 | quality: 1.67
- latency_total: 30.693s | tokens_per_second: 112.5
- input_tokens: 71 | output_tokens: 3452

## Entrada exacta (lo que recibió el modelo)

**user:**

Estima cuantos litros de cafe se consumen al dia en todas las oficinas de Santiago de Chile.

Muestra tu razonamiento paso a paso con cada supuesto numerado.
Da un rango (minimo-maximo) ademas de tu mejor estimacion.
Explica que supuesto tiene mas impacto en el resultado.


## Respuesta completa

# Estimación: café consumido en oficinas de Santiago

**Definición que voy a usar:** litros de café bebidos en un día laboral típico, dentro de oficinas físicas del Gran Santiago — empresas, servicios públicos, Pymes, coworks, etc. No cuento el café que un teletrabajador se toma en su casa, ni el de cafeterías fuera de la oficina.

Es un problema tipo Fermi: no hay un registro exacto, por lo que multiplico una cadena de supuestos razonables.

### Cálculo paso a paso

**Supuesto 1: Población del Gran Santiago**
~6,8 millones de personas.
Rango: 6,5 - 7,0 millones. Es el supuesto más sólido.

**Supuesto 2: Personas ocupadas**
Aproximadamente el 46% de la población total está ocupada — el resto son niños, jubilados, estudiantes, desempleados o inactivos.
6,8 M x 0,46 = **~3,1 millones de ocupados**
Rango: 2,9 - 3,3 millones.

**Supuesto 3: Fracción que trabaja en oficina**
No todo ocupado trabaja en oficina: hay comercio en tienda, construcción, industria, transporte, salud en terreno, reparto, etc.
Estimo que un **35%** es trabajo típicamente de oficina: administración pública, banca, seguros, servicios profesionales, TI, educación administrativa, gerencias, back-office, etc.
3,1 M x 0,35 = **~1,09 millones de oficinistas**
Rango: 25% - 45% → 0,73 - 1,49 millones.

**Supuesto 4: Presencialidad en un día dado**
Post-pandemia hay mucho trabajo híbrido. A eso hay que sumar vacaciones, licencias, días en terreno y ausencias. En un martes típico, estimo que está físicamente en la oficina el **70%** de los oficinistas.
1,09 M x 0,70 = **~760.000 personas en oficinas hoy**
Rango: 60% - 85%.

**Supuesto 5: Proporción que toma café en la oficina**
Chile toma bastante café, pero también té, mate y bebidas. No todos toman café *en el trabajo*.
Estimo **65%**.
760.000 x 0,65 = **~495.000 bebedores de café en oficina**
Rango: 50% - 80%.

**Supuesto 6: Tazas por bebedor al día**
Una al llegar / en la mañana y otra después de almuerzo es lo típico. Los más cafeteros llegan a 3-4.
Estimo **2,0 tazas por bebedor**.
495.000 x 2,0 = **~990.000 tazas al día**
Rango: 1,5 - 2,5 tazas.

**Supuesto 7: Tamaño de la taza**
No es un espresso de 60 ml ni siempre un mug grande. Entre café de máquina, instantáneo y tazón, el promedio razonable es **180 ml**.
Rango: 150 - 220 ml.

### Resultado

> 990.000 tazas x 0,18 litros = **~180.000 litros por día laboral**

**Mi mejor estimación: 150.000 a 200.000 litros/día, con valor central de ~180.000 litros.**

Eso equivale, como chequeo de cordura, a ~1 millón de tazas y a unos 9.000 kg de café molido al día — asumiendo ~9 g por taza —, unas 2.250 toneladas al año solo en oficinas santiaguinas. Es plausible frente al consumo total de café de Chile, del orden de decenas de miles de toneladas anuales.

### Rango mínimo - máximo

Multiplicando todos los mínimos y todos los máximos:

**Mínimo extremo:** 2,9 M x 0,25 x 0,60 x 0,50 x 1,5 x 0,15 = **~50.000 litros/día**

**Máximo extremo:** 3,3 M x 0,45 x 0,85 x 0,80 x 2,5 x 0,22 = **~550.000 litros/día**

Ese rango extremo es muy ancho porque supone que *todo* sale mal o bien a la vez, algo improbable. Un rango realista, moviendo los supuestos a valores todavía creíbles pero no extremos, sería **100.000 a 300.000 litros/día**.

### ¿Qué supuesto impacta más?

**El Supuesto 3: qué fracción de los ocupados cuenta como "oficinista".**

Es el más incierto porque la frontera es difusa: ¿cuenta el vendedor que pasa 2 horas en oficina?, ¿el profesor?, ¿el funcionario municipal en atención de público? Su rango solo, de 25% a 45%, mueve el resultado desde ~130.000 hasta ~230.000 litros, manteniendo todo lo demás fijo.

Casi empatado viene el **Supuesto 6, tazas por persona** — pasar de 1,5 a 2,5 tazas mueve el resultado de ~135.000 a ~225.000 litros.

En cambio, la población de Santiago y el tamaño de la taza son relativamente conocidos y apenas mueven el resultado. Si quisieras mejorar esta estimación, lo primero que habría que medir bien no es la taza, sino cuánta gente trabaja realmente en oficinas en Santiago y cuántos días va presencial.