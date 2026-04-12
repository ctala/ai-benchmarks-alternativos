"""
Tests especificos para generacion de contenido de ecosistemastartup.com
y material educativo para emprendedores.
Estos tests simulan los flujos reales de N8N con Sonnet + Perplexity.
"""

TESTS = [
    {
        "name": "blog_actualidad_startup",
        "description": "Generar articulo de blog para ecosistemastartup.com/actualidad",
        "messages": [
            {"role": "system", "content": """Eres un periodista especializado en startups y tecnologia en Latinoamerica.
Escribes para ecosistemastartup.com, un blog enfocado en el ecosistema emprendedor.
Tu estilo es informativo pero accesible, con datos concretos y relevancia regional.
Siempre incluyes contexto de como afecta a emprendedores latinoamericanos."""},
            {"role": "user", "content": """Escribe un articulo de blog sobre el impacto de los modelos de IA open-source en las startups latinoamericanas en 2026.

El articulo debe incluir:
- Titulo SEO-friendly (max 70 caracteres)
- Meta description (max 160 caracteres)
- Introduccion con hook
- 3-4 secciones con subtitulos H2
- Datos y ejemplos concretos de la region
- Mencion de modelos relevantes (DeepSeek, Qwen, Llama, Gemma)
- Como las startups pueden aprovechar estos modelos
- Conclusion con perspectiva a futuro
- 3 tags sugeridos para el post

Extension: ~800 palabras. Idioma: Espanol."""},
        ],
        "criteria": {
            "min_words": 500,
            "required_sections": ["titulo", "meta", "startup", "open-source", "latinoamerica", "conclusion"],
            "language": "es",
        },
    },
    {
        "name": "curso_emprendimiento_modulo",
        "description": "Generar modulo de curso para emprendedores",
        "messages": [
            {"role": "system", "content": """Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales."""},
            {"role": "user", "content": """Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico."""},
        ],
        "criteria": {
            "min_words": 600,
            "required_sections": ["objetivo", "ejercicio", "ejemplo", "n8n", "autoevaluacion"],
            "language": "es",
        },
    },
    {
        "name": "workshop_outline",
        "description": "Generar outline de workshop de emprendimiento",
        "messages": [
            {"role": "system", "content": "Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica."},
            {"role": "user", "content": """Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico."""},
        ],
        "criteria": {
            "min_words": 400,
            "required_sections": ["agenda", "ejercicio", "workshop", "hora", "slide"],
            "language": "es",
        },
    },
    {
        "name": "newsletter_startup",
        "description": "Generar newsletter semanal del ecosistema",
        "messages": [
            {"role": "system", "content": "Eres el editor del newsletter semanal de ecosistemastartup.com. Tono profesional pero cercano, informativo y con opinion editorial."},
            {"role": "user", "content": """Genera el newsletter semanal #47 de ecosistemastartup.com con estos temas:

1. DeepSeek lanzo V4, su modelo mas avanzado - impacto en startups
2. Chile lanza programa de $50M para startups deep tech
3. Mercado Libre abre API de IA para sellers
4. Gemma 4 de Google: el modelo open-source que compite con GPT-4o
5. Tips: 3 herramientas de IA gratis para emprendedores en 2026

Formato del newsletter:
- Titulo del newsletter
- Saludo breve
- 5 secciones con: emoji + titulo, resumen de 2-3 oraciones, por que importa para emprendedores
- Seccion "El dato de la semana" (un dato curioso sobre IA/startups)
- CTA final invitando a compartir
- Firma"""},
        ],
        "criteria": {
            "min_words": 400,
            "required_sections": ["newsletter", "deepseek", "chile", "gemma", "herramienta"],
            "language": "es",
        },
    },
    {
        "name": "perplexity_style_research",
        "description": "Simular busqueda tipo Perplexity para alimentar articulo",
        "messages": [
            {"role": "system", "content": """Eres un asistente de investigacion. Tu rol es compilar informacion actual sobre un tema
para que un redactor pueda escribir un articulo. Proporciona datos estructurados, fuentes posibles,
y puntos clave. Formato similar a como Perplexity presenta resultados."""},
            {"role": "user", "content": """Investiga: "Estado del venture capital en Latinoamerica Q1 2026"

Necesito:
1. Resumen ejecutivo (3 bullets)
2. Datos clave con numeros:
   - Inversion total estimada
   - Deals mas grandes
   - Paises lideres
   - Sectores hot
3. Tendencias principales (3-5)
4. Comparacion con Q1 2025
5. Quotes o perspectivas de actores relevantes
6. Fuentes sugeridas para profundizar

Formato estructurado, facil de escanear."""},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["venture", "latinoamerica", "inversion", "tendencia", "fuente"],
            "language": "es",
        },
    },
]
