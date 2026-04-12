"""
Tests de creatividad, originalidad y calidad de escritura.
Evalua si el modelo produce contenido genuinamente interesante o solo generico.

El scoring busca:
- Evitar cliches y frases genericas
- Usar metaforas o analogias originales
- Variedad en vocabulario
- Profundidad vs superficialidad
"""

# Lista de cliches comunes que penalizan el score
CLICHES = [
    "en la era digital",
    "en el mundo actual",
    "no es de extranar",
    "en este sentido",
    "cabe destacar",
    "es importante senalar",
    "sin lugar a dudas",
    "en conclusion",
    "por otro lado",
    "en primer lugar",
    "it is worth noting",
    "in today's world",
    "at the end of the day",
    "it goes without saying",
    "game changer",
    "cutting edge",
    "paradigm shift",
    "synergy",
    "leverage",
    "deep dive",
]

TESTS = [
    {
        "name": "creative_hook_writing",
        "description": "Escribir hooks creativos sin cliches",
        "messages": [
            {"role": "user", "content": """Escribe 5 hooks (primeras oraciones) para articulos sobre estos temas.
Cada hook debe ser ORIGINAL, provocador, y hacer que el lector quiera seguir leyendo.
NO uses cliches como "en la era digital", "en el mundo actual", "no es de extranar".
NO empieces con preguntas retoricas genericas.

Temas:
1. Por que las startups latinoamericanas deberian usar modelos de IA open-source
2. El futuro del trabajo remoto despues de la pandemia
3. Como la automatizacion esta cambiando el soporte al cliente
4. Por que los developers deberian aprender sobre IA
5. El impacto de la IA en la educacion

Para cada uno, escribe SOLO el hook (1-2 oraciones). Nada mas."""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": [],
            "language": "es",
        },
        "expected_answer": {
            "type": "creativity_check",
            "penalize_cliches": CLICHES,
            "min_hooks": 5,
        },
    },
    {
        "name": "analogy_generation",
        "description": "Crear analogias originales para conceptos tecnicos",
        "messages": [
            {"role": "user", "content": """Crea una analogia ORIGINAL y memorable para explicar cada concepto a un emprendedor no-tecnico.
Las analogias deben ser sorprendentes, no las tipicas.
NO uses: "es como un cerebro", "es como una autopista", "es como una biblioteca".

1. Como funciona un modelo de lenguaje (LLM)
2. Que es una API
3. Que es el fine-tuning de un modelo
4. Que es un rate limit
5. Que es el prompt engineering

Para cada uno: concepto + analogia en 2-3 oraciones."""},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": [],
            "language": "es",
        },
        "expected_answer": {
            "type": "creativity_check",
            "penalize_cliches": ["cerebro", "autopista", "biblioteca", "como un chef", "como un libro"],
            "min_analogies": 5,
        },
    },
    {
        "name": "depth_vs_superficial",
        "description": "Evaluar profundidad de analisis vs respuesta superficial",
        "messages": [
            {"role": "user", "content": """Un emprendedor te dice: "Estoy pensando en usar IA para mi startup de delivery de comida en Santiago. Que deberia hacer?"

Da una respuesta que demuestre PROFUNDIDAD real, no consejos genericos.
Incluye:
- Al menos 2 ideas especificas que NO sean obvias (no digas "usa IA para optimizar rutas", eso lo sabe cualquiera)
- Numeros o estimaciones concretas cuando sea posible
- Un riesgo no obvio que otros no mencionarian
- Una opinion contrarian o controversia sobre el tema

No me des una lista generica de "5 formas de usar IA". Quiero pensamiento original."""},
        ],
        "criteria": {
            "min_words": 200,
            "required_sections": ["riesgo", "idea"],
            "language": "es",
        },
        "expected_answer": {
            "type": "depth_check",
            "penalize_generic": [
                "optimizar rutas",
                "mejorar la experiencia del cliente",
                "reducir costos",
                "aumentar la eficiencia",
                "personalizar recomendaciones",
            ],
        },
    },
    {
        "name": "storytelling_quality",
        "description": "Calidad narrativa - contar una historia corta",
        "messages": [
            {"role": "user", "content": """Escribe un micro-relato (exactamente 100 palabras, ni mas ni menos) sobre un emprendedor latinoamericano que descubre que su startup de IA tiene un bug que la hace demasiado honesta.

Requisitos:
- Exactamente 100 palabras
- Debe tener un giro inesperado
- Debe ser divertido o ironico
- Debe sentirse autentico, no generico"""},
        ],
        "criteria": {
            "min_words": 80,
            "required_sections": [],
            "language": "es",
        },
        "expected_answer": {
            "type": "creativity_check",
            "word_count_target": 100,
            "word_count_tolerance": 15,
        },
    },
]
