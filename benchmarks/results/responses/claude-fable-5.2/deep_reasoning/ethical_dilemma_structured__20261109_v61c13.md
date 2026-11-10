# Claude Fable 5.2 — deep_reasoning/ethical_dilemma_structured

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.87 | quality: 10.0
- latency_total: 44.193s | tokens_per_second: 93.7
- input_tokens: 306 | output_tokens: 4143

## Entrada exacta (lo que recibió el modelo)

**user:**

Una startup de IA tiene un modelo que puede detectar cancer con 95% de precision.
Sin embargo:
- El 5% de falsos positivos causa ansiedad severa y procedimientos innecesarios
- El modelo funciona peor en personas de piel oscura (90% precision vs 97% en piel clara)
- Lanzar ahora salvaria vidas pero con sesgo conocido
- Esperar 6 meses para corregir el sesgo significa que gente morira mientras tanto

El board te pide una recomendacion. Estructura tu analisis:
1. Identifica a todos los stakeholders afectados
2. Analiza los trade-offs cuantitativamente
3. Proporciona 3 opciones con pros/contras de cada una
4. Da tu recomendacion final con justificacion

No busques la respuesta "correcta" - busca la mejor argumentada.


## Respuesta completa

Antes de empezar, una advertencia: "95% de precisión" es ambiguo (puede ser sensibilidad, especificidad o exactitud global). Asumo 95% de sensibilidad y 95% de especificidad, y lo primero que el board debería exigir es que se aclare ese dato, porque cambia los números.

## 1. Stakeholders

- **Pacientes con cáncer:** se benefician de la detección temprana, y los no detectados reciben una falsa tranquilidad.
- **Personas sanas con falso positivo:** sufren ansiedad, biopsias y costos innecesarios.
- **Pacientes de piel oscura:** reciben más errores de ambos tipos, sobre una historia previa de peor atención médica.
- **Médicos y sistema de salud:** asumen la carga de seguimiento y la responsabilidad legal.
- **La startup (empleados e inversores):** enfrenta riesgo regulatorio, legal y reputacional.
- **Reguladores y aseguradoras:** deciden la aprobación y la cobertura.
- **El campo de la IA médica:** un lanzamiento con sesgo mal gestionado erosiona la confianza en todo el sector.

## 2. Trade-offs cuantitativos

Los números son ilustrativos: por cada 100.000 personas examinadas, con una prevalencia supuesta del 1% (1.000 cánceres).

| | Detectados | No detectados | Falsos positivos | Positivos que son cáncer real |
|---|---|---|---|---|
| Global (95%) | 950 | 50 | 4.950 | 16% |
| Piel clara (97%) | 970 | 30 | 2.970 | 25% |
| Piel oscura (90%) | 900 | 100 | 9.900 | 8% |

De aquí salen tres conclusiones:

1. **Los falsos positivos pesan más de lo que sugiere el 5%.** Con baja prevalencia, 5 de cada 6 positivos son falsas alarmas. El modelo no puede usarse como diagnóstico, solo como filtro previo a una confirmación.
2. **La brecha es mayor de lo que parece.** La diferencia entre 90% y 97% suena a 7 puntos, pero implica 3,3 veces más cánceres no detectados y 3,3 veces más falsas alarmas en piel oscura.
3. **El costo de esperar depende de con qué se compare.** Si la práctica actual detecta, por ejemplo, el 80% de los casos y la detección temprana reduce la mortalidad en 30 puntos, esperar cuesta unas 45 vidas por cada 100.000 personas no examinadas (1.000 × 0,15 × 0,30).

El comparador correcto es la atención actual que recibe cada grupo, no un modelo perfecto. Si el estándar actual para piel oscura está por debajo del 90%, esperar también perjudica a ese grupo, porque pasa de 90% a no tener la herramienta.

## 3. Opciones

**A. Lanzamiento general inmediato**
- *Pros:* máximo de vidas salvadas a corto plazo, ingresos y datos reales.
- *Contras:* institucionaliza una disparidad conocida, con el riesgo legal de haberlo sabido y lanzado igual. Además, una vez en el mercado, el incentivo para corregir el sesgo se debilita.

**B. Esperar 6 meses**
- *Pros:* producto más equitativo, menor riesgo legal y mensaje claro de principios.
- *Contras:* hay muertes evitables en todos los grupos, incluido el que se busca proteger. Los 6 meses son una estimación, no una garantía. La equidad se logra dejando a todos igual de mal durante la espera.

**C. Lanzamiento condicionado con mitigaciones**

El modelo se lanza como apoyo al médico, no como diagnóstico autónomo, con estas condiciones:
- Confirmación obligatoria de todo positivo antes de comunicarlo como diagnóstico.
- Protocolo reforzado para piel oscura: un resultado negativo no descarta, y se añade una segunda lectura humana o umbrales ajustados.
- Divulgación del rendimiento por subgrupo a médicos y pacientes.
- Compromiso público y vinculante de corregir el sesgo, con plazo y auditoría externa.
- Monitoreo continuo, con criterios de suspensión definidos de antemano.

- *Pros:* captura la mayor parte del beneficio, reduce el daño diferencial y genera los datos necesarios para corregir el sesgo.
- *Contras:* es más cara y compleja de operar. Los protocolos diferenciados pueden percibirse como atención de segunda, y las mitigaciones pueden cumplirse mal en la práctica.

## 4. Recomendación: opción C

1. **Esperar no protege al grupo afectado.** Les quita una herramienta que probablemente ya mejora su atención actual. Negar un beneficio a todos porque no es igual para todos solo se justifica si el modelo causa daño neto a algún grupo.
2. **Conocer el sesgo genera la obligación de mitigarlo y divulgarlo, no necesariamente de detenerse.** Lo indefendible sería la opción A: lanzar sabiendo y sin hacer nada al respecto.
3. **El problema de los falsos positivos es de diseño del flujo clínico.** Se resuelve con confirmación obligatoria, no con seis meses de espera.
4. **El compromiso vinculante neutraliza el mayor riesgo de lanzar,** que es que la corrección nunca llegue.

Cambiaría mi recomendación a B en tres casos: si el 90% en piel oscura resulta peor que el estándar de atención actual para ese grupo (daño neto), si el modelo va a reemplazar el juicio médico en lugar de complementarlo, o si la empresa no acepta las condiciones como obligatorias.

El mejor argumento en contra es que las mitigaciones suelen cumplirse peor en la práctica que sobre el papel, y que un daño desigual impuesto a sabiendas tiene un costo de confianza que los números no capturan. Por eso las condiciones de C deben ser requisitos para lanzar, no promesas.