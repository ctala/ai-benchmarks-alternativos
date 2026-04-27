---
titulo: Diseñá un test custom para TU caso de uso
dificultad: Intermedio
tiempo_estimado: 45-60 minutos
costo_estimado: Menos de $1 USD
requisitos_previos:
  - Tutorial 01 completado
  - Saber qué tarea concreta querés automatizar con IA
  - Editor de código (VS Code, Cursor, lo que uses)
---

# Diseñá un test custom para TU caso de uso

## Para qué sirve este tutorial

Los benchmarks públicos miden cosas como "razonamiento matemático" o "comprensión lectora". Eso no te dice si **el modelo que estás por elegir genera buenos emails de follow-up para tus clientes** o **si arma decentemente templates de N8N**.

Este tutorial te enseña a crear tests que reflejen tu caso de uso real, en español, con criterios que vos definís. Es lo que hace que este repo sea distinto de cualquier otro benchmark que vas a encontrar.

## Lo que vas a tener al final

- Un archivo nuevo `benchmarks/tests/mi_caso_uso.py` con 3-5 tests propios.
- El runner reconociendo tu suite (`--tests mi_caso_uso`).
- Resultados de tu suite contra los modelos que vos quieras.
- Criterio claro para decidir cuál te conviene.

## Por qué los tests genéricos no alcanzan

Cristian (autor del repo) usa Qwen 3.5 397B Cloud para generar contenido de su blog **ecosistemastartup.com**. Cuando empezó, el ranking general decía que GPT-4.1 era "el mejor modelo de contenido". Lo probó y el output sonaba a "blog post genérico de medium en inglés traducido". Probó Qwen y la voz era más natural para LATAM, los ejemplos más relevantes, el tono más cercano.

**Conclusión**: el benchmark general miente para tu caso particular. Necesitás tu propio benchmark.

## Caso ejemplo concreto

Sos emprendedor, vendés un curso online de marketing digital a $97 USD. Después de cada compra querés enviar un **email de follow-up** que:

- Agradezca de forma cálida (no robótica).
- Recuerde cómo acceder al curso (login + URL).
- Recomiende empezar por el módulo 1 con un beneficio concreto.
- Invite a un grupo privado de WhatsApp.
- Cierre con tu firma personal.

¿Qué modelo te lo hace mejor? Vamos a medirlo.

## Paso 1 — Anatomía de un test

Mirá un test existente para entender el formato. Abrí `benchmarks/tests/startup_content.py` y vas a ver:

```python
TESTS = [
    {
        "name": "blog_actualidad_startup",
        "description": "Generar articulo de blog para ecosistemastartup.com",
        "messages": [
            {"role": "system", "content": "Eres un periodista..."},
            {"role": "user", "content": "Escribe un articulo sobre..."},
        ],
        "criteria": {
            "min_words": 500,
            "required_sections": ["titulo", "meta", "startup", "open-source"],
            "language": "es",
        },
    },
    # ... más tests ...
]
```

**5 campos clave**:

| Campo | Para qué sirve |
|-------|----------------|
| `name` | ID corto del test (snake_case). Aparece en los outputs. |
| `description` | Frase humana, una línea, qué mide el test. |
| `messages` | Lista de mensajes tipo OpenAI (`role` + `content`). |
| `criteria` | Reglas automáticas: longitud mínima, palabras requeridas, idioma. |
| `expected_answer` | (opcional) Validación de sustancia más estricta. |

## Paso 2 — Creá tu archivo de tests

```bash
cd /ruta/a/ai-benchmarks-alternativos
touch benchmarks/tests/email_post_compra.py
```

Abrilo en tu editor y pegá esta plantilla con 3 tests para el caso del email de follow-up:

```python
"""
Tests para emails de follow-up post-compra de cursos online.
Mide la capacidad del modelo de escribir copy cálido, en español rioplatense
o neutro LATAM, sin tono robótico ni sobre-formalidad.
"""

TESTS = [
    {
        "name": "email_followup_compra_curso",
        "description": "Email post-compra de curso de marketing digital ($97)",
        "messages": [
            {"role": "system", "content": """Sos un copywriter de email marketing
para emprendedores LATAM. Escribís en español neutro, cálido pero profesional,
nunca robótico. Evitás clichés como "esperamos que disfrutes" o "si tenés alguna
duda no dudes en contactarnos"."""},
            {"role": "user", "content": """Escribí un email de follow-up para enviar
inmediatamente despues de que un cliente compra mi curso "Marketing Digital
para Emprendedores" ($97 USD).

El email debe incluir:
- Saludo agradeciendo la compra (sin sonar a plantilla)
- Como acceder al curso: login en https://miacademia.com/login con el mismo
  email de la compra
- Recomendación concreta: empezar por el Módulo 1 (lo termina en 45 minutos
  y ya tiene un beneficio aplicable hoy)
- Invitación al grupo privado de WhatsApp: https://chat.whatsapp.com/abc123
- Firma de Cristian, fundador

Tono: cercano, primera persona singular ("te escribo yo, Cristian, no un bot").
Largo: 150-250 palabras. Sin asunto del email — solo el body."""},
        ],
        "criteria": {
            "min_words": 130,
            "required_sections": ["modulo 1", "whatsapp", "miacademia.com", "cristian"],
            "language": "es",
        },
    },
    {
        "name": "email_followup_no_login",
        "description": "Cliente que compro pero no entro al curso en 3 dias",
        "messages": [
            {"role": "system", "content": "Sos un copywriter empático para emprendedores LATAM. No usás guilt-tripping ni FOMO agresivo."},
            {"role": "user", "content": """Escribí un email de re-engagement para
clientes que compraron el curso hace 3 dias y no hicieron login todavia.

Debe:
- No hacerlos sentir culpables
- Reconocer que están ocupados
- Ofrecer ayuda concreta (responder este email si hay un problema técnico)
- Recordar que el primer modulo dura solo 45 minutos
- Cerrar con CTA claro al login

Tono: comprensivo, no comercial. 100-180 palabras."""},
        ],
        "criteria": {
            "min_words": 90,
            "required_sections": ["modulo", "login", "ayuda"],
            "language": "es",
        },
    },
    {
        "name": "email_upsell_post_modulo1",
        "description": "Upsell a programa premium tras completar modulo 1",
        "messages": [
            {"role": "system", "content": "Sos un copywriter especializado en upsell de cursos online sin sonar a vendedor de TV."},
            {"role": "user", "content": """El cliente completo el Modulo 1 del curso
de $97. Escribí un email ofreciendole el "Programa Mentoría 1-1" de $497
(8 sesiones de 60 min con Cristian).

Debe:
- Felicitar por completar el primer paso
- Conectar el avance con la siguiente etapa logica
- Explicar el valor del 1-1 vs el curso solo
- Dejar claro que NO es obligatorio y que el curso esta completo asi
- CTA suave: agendar una llamada de 15 min para ver si encaja
- Link: https://calendly.com/cristian/15min

Tono: educativo, no high-pressure. 180-260 palabras."""},
        ],
        "criteria": {
            "min_words": 160,
            "required_sections": ["mentoría", "calendly.com", "modulo 1"],
            "language": "es",
        },
    },
]
```

**Notas sobre la plantilla**:

- Usé 3 tests, no 91. Es **deliberadamente chico**. La regla es: empezá con 3-5, iterá, después escalás.
- `required_sections` no tiene que ser frases largas — son palabras clave que **deben aparecer** en la respuesta. Si el modelo no menciona "modulo 1", probablemente está alucinando una estructura distinta.
- `min_words` te protege contra respuestas truncadas o demasiado escuetas. Para emails poné 90-160; para blog posts, 500+.

## Paso 3 — Registrá el suite en `runner.py`

Abrí `benchmarks/runner.py` y buscá las dos secciones a editar.

**a) En la zona de imports** (línea ~44 aprox):

```python
from benchmarks.tests import content_generation, tool_calling, task_management
from benchmarks.tests import code_generation, reasoning, summarization, presentation
from benchmarks.tests import startup_content, deep_reasoning, customer_support, structured_output
# ... más imports ...
from benchmarks.tests import email_post_compra   # ← AGREGÁ ESTA LÍNEA
```

**b) En el dict `ALL_TEST_SUITES`** (línea ~53 aprox):

```python
ALL_TEST_SUITES = {
    "content_generation": content_generation.TESTS,
    "tool_calling": tool_calling.TESTS,
    # ... entries existentes ...
    "email_post_compra": email_post_compra.TESTS,   # ← AGREGÁ ESTA LÍNEA
}
```

**Tip**: la clave del dict (`"email_post_compra"`) es la que usás con `--tests`. Que sea snake_case y descriptiva.

## Paso 4 — Verificá que el runner reconoce tu suite

```bash
source .venv/bin/activate
python benchmarks/runner.py --list-tests
```

**Output esperado**: vas a ver `email_post_compra` listado entre los suites con sus 3 tests.

**Si no aparece**: revisá que en `runner.py` agregaste **ambas** líneas (import + entry en dict). Si Python tira `ModuleNotFoundError: No module named 'benchmarks.tests.email_post_compra'`, revisá que el archivo exista en la carpeta correcta.

## Paso 5 — Corré tu suite contra modelos candidatos

Para emails LATAM en español, los candidatos típicos son: DeepSeek V3, Qwen 3.6, Mistral Small, GPT-4.1 Mini, Gemini 2.5 Flash. Empezá con 3:

```bash
python benchmarks/runner.py \
  --quick \
  --tests email_post_compra \
  --models deepseek-v3 mistral-small qwen-3.6
```

**Tiempo**: ~5 minutos. **Costo**: <$0.20 USD.

**Output esperado**:

```
[1/3] DeepSeek V3.2
  email_followup_compra_curso     score: 7.4 | $0.0009
  email_followup_no_login         score: 7.1 | $0.0007
  email_upsell_post_modulo1       score: 7.6 | $0.0011

[2/3] Mistral Small 4
  ...

[3/3] Qwen 3.6
  ...
```

## Paso 6 — Leé las respuestas reales (esto es lo importante)

Los scores automáticos te dan un primer filtro, pero **vos tenés que leer las respuestas** y formarte un juicio. El score automático no sabe si "Hola, espero te encuentres bien" suena a robot, pero vos sí.

```bash
ls benchmarks/results/responses/ | tail -1
# 20260426_201534
```

```bash
ls benchmarks/results/responses/20260426_201534/ | grep email
# deepseek-v3__email_post_compra__email_followup_compra_curso.md
# mistral-small__email_post_compra__email_followup_compra_curso.md
# qwen-3.6__email_post_compra__email_followup_compra_curso.md
# ... (3 modelos × 3 tests = 9 archivos)
```

Abrí los 3 archivos del mismo test (`email_followup_compra_curso`) en pestañas distintas y compará lado a lado:

- ¿Cuál suena más vos?
- ¿Cuál evita clichés?
- ¿Cuál tiene la longitud adecuada?
- ¿Cuál usa la URL de forma natural y no como copy-paste?

Esa es **tu fuente de verdad**, no el score numérico.

## Paso 7 — Iterá sobre tu suite

Después de leer las respuestas vas a notar cosas. Por ejemplo:

- "Todos los modelos abrieron con 'Espero que te encuentres bien' — necesito agregar un anti-criterio"
- "El test era muy permisivo, ningún modelo es claramente mejor — necesito casos más complejos"
- "Faltó un test donde el cliente pidió reembolso"

Editá tu archivo de tests, agregá/modificá tests, y volvé a correr. **Iteración rápida es el punto** — por eso empezamos con 3 tests, no con 91.

### Tip: anti-clichés con `expected_answer`

Si querés penalizar frases robot, podés usar:

```python
{
    "name": "email_sin_cliches",
    # ... messages ...
    "criteria": { "min_words": 100, "language": "es" },
    "expected_answer": {
        "type": "anti_phrases",
        "phrases_to_avoid": [
            "espero que te encuentres bien",
            "no dudes en contactarnos",
            "estamos a tu disposición",
            "esperamos que disfrutes",
        ]
    },
}
```

(Ver `benchmarks/scoring.py` función `score_expected_answer` para todos los tipos disponibles.)

## Paso 8 — Cuando ya estés contento, escalá

Cuando tu suite refleja bien tu caso, corrélo contra **más modelos** y con el **juez Phi-4** activado:

```bash
python benchmarks/runner.py \
  --quick \
  --judge --judge-model phi4 \
  --tests email_post_compra \
  --models deepseek-v3 mistral-small qwen-3.6 gpt-4.1-mini gemini-2.5-flash devstral-small
```

Eso te da un ranking robusto **para TU tarea específica**. Ese ranking puede ser radicalmente distinto al ranking global.

## Próximos pasos

Si todavía no tenés Phi-4 instalado, urgente: [04 — Setup del LLM-as-Judge con Phi-4](04-configurar-phi4-judge.md). Sin juez, los scores tienen mucho ruido para tests de estilo.

Cuando tengas tu suite + Phi-4 funcionando, cerrá con: [05 — Cómo decidir qué modelo poner en producción](05-elegir-modelo-para-tu-caso.md).
