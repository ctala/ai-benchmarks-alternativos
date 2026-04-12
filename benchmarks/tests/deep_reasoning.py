"""
Tests de razonamiento profundo.
Diseñados para diferenciar modelos "inteligentes" de los que solo formatean bien.
Estos tests tienen respuestas correctas verificables, no solo formato.

Cada test incluye 'expected_answer' para validacion automatica.
"""

TESTS = [
    {
        "name": "math_word_problem",
        "description": "Problema matematico con trampa logica",
        "messages": [
            {"role": "user", "content": """Un tren sale de Santiago a las 8:00 AM hacia Valparaiso a 80 km/h.
Otro tren sale de Valparaiso a las 8:30 AM hacia Santiago a 120 km/h.
La distancia entre ambas ciudades es 120 km.
A que hora se cruzan los trenes y a que distancia de Santiago?

Muestra todo el razonamiento paso a paso."""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": ["paso", "distancia", "hora"],
            "language": "es",
        },
        "expected_answer": {
            "type": "numeric",
            "values": {"hora_cruce": "8:42", "distancia_santiago": "56"},
            "tolerance": 2,  # km de tolerancia
        },
    },
    {
        "name": "logic_puzzle_constraint",
        "description": "Puzzle logico con restricciones multiples",
        "messages": [
            {"role": "user", "content": """Hay 4 casas en una calle, cada una de un color diferente.
- La casa roja esta a la izquierda de la azul (no necesariamente adyacente)
- La casa verde esta al lado de la blanca
- La casa azul NO esta en los extremos
- La casa verde NO esta al lado de la roja

En que orden estan las casas de izquierda a derecha?
Explica tu razonamiento paso a paso probando cada posibilidad."""},
        ],
        "criteria": {
            "min_words": 80,
            "required_sections": ["roja", "azul", "verde", "blanca"],
            "language": "es",
        },
        "expected_answer": {
            "type": "sequence",
            "values": ["roja", "blanca", "azul", "verde"],
        },
    },
    {
        "name": "causal_reasoning",
        "description": "Razonamiento causal con informacion ambigua",
        "messages": [
            {"role": "user", "content": """Una startup de delivery tiene estos datos de los ultimos 3 meses:

Mes 1: 1000 pedidos, 50 quejas, tiempo promedio 35 min, lluvia 5 dias
Mes 2: 1200 pedidos, 90 quejas, tiempo promedio 42 min, lluvia 12 dias
Mes 3: 1100 pedidos, 110 quejas, tiempo promedio 38 min, lluvia 8 dias

El CEO dice: "Las quejas suben porque tenemos mas pedidos".
El CTO dice: "Las quejas suben por la lluvia".
El COO dice: "Hay un problema operacional que empeora cada mes".

Analiza los datos cuantitativamente. Calcula las tasas relevantes.
Determina cual hipotesis es mas probable y por que.
Identifica que dato adicional necesitarias para estar seguro."""},
        ],
        "criteria": {
            "min_words": 150,
            "required_sections": ["tasa", "queja", "hipotesis", "dato adicional"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "tasa de quejas sube: 5% -> 7.5% -> 10%",
                "la tasa sube independiente del volumen",
                "mes 3 tiene menos lluvia que mes 2 pero mas quejas",
                "COO tiene la hipotesis mas probable",
            ],
        },
    },
    {
        "name": "code_bug_subtle",
        "description": "Bug sutil que requiere razonamiento sobre edge cases",
        "messages": [
            {"role": "user", "content": """Este codigo tiene un bug sutil que solo aparece en ciertos casos.
Identificalo sin ejecutar el codigo. Explica exactamente cuando falla y por que.

```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def remove_outliers_and_average(data):
    if len(data) < 3:
        return sum(data) / len(data)

    median = find_median(data)
    mad = find_median([abs(x - median) for x in data])
    threshold = 3 * mad

    filtered = [x for x in data if abs(x - median) <= threshold]
    return sum(filtered) / len(filtered)
```

Hint: piensa en que pasa con datos especificos, no en el algoritmo general."""},
        ],
        "criteria": {
            "min_words": 80,
            "required_sections": ["bug", "falla", "caso"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "MAD puede ser 0 cuando todos los valores son iguales o la mediana de diferencias es 0",
                "threshold seria 0, filtrando todos excepto los que son exactamente la mediana",
                "division por cero si filtered queda vacio",
                "tambien falla con lista vacia en la primera funcion",
            ],
        },
    },
    {
        "name": "fermi_estimation",
        "description": "Estimacion de Fermi que requiere razonamiento estructurado",
        "messages": [
            {"role": "user", "content": """Estima cuantos litros de cafe se consumen al dia en todas las oficinas de Santiago de Chile.

Muestra tu razonamiento paso a paso con cada supuesto numerado.
Da un rango (minimo-maximo) ademas de tu mejor estimacion.
Explica que supuesto tiene mas impacto en el resultado."""},
        ],
        "criteria": {
            "min_words": 150,
            "required_sections": ["supuesto", "estimacion", "rango", "impacto"],
            "language": "es",
        },
        "expected_answer": {
            "type": "range",
            "reasonable_range": [100000, 2000000],  # litros/dia
            "must_mention": ["poblacion santiago", "tasa empleo oficina", "tazas por persona"],
        },
    },
    {
        "name": "ethical_dilemma_structured",
        "description": "Dilema etico que requiere analisis multi-perspectiva",
        "messages": [
            {"role": "user", "content": """Una startup de IA tiene un modelo que puede detectar cancer con 95% de precision.
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

No busques la respuesta "correcta" - busca la mejor argumentada."""},
        ],
        "criteria": {
            "min_words": 250,
            "required_sections": ["stakeholder", "trade-off", "opcion", "recomendacion"],
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "identifica al menos 4 stakeholders",
                "cuantifica el impacto del sesgo racial",
                "presenta al menos 3 opciones viables",
                "la recomendacion no es binaria (lanzar/no lanzar)",
            ],
        },
    },
]
