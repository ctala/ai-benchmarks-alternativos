---
titulo: Tutoriales del benchmark — empezá por acá
audiencia: Emprendedor latinoamericano que quiere decidir qué modelo de IA usar con datos propios, no con marketing del proveedor
---

# Tutoriales

Bienvenido. Este folder es la rampa de entrada al repo si sos emprendedor o solopreneur y querés **dejar de adivinar qué modelo poner en producción**.

No vas a encontrar acá teoría de transformers ni explicaciones académicas. Son 5 tutoriales hands-on, en español, pensados para que en una tarde puedas:

1. Replicar el benchmark con tus propias keys.
2. Agregar el modelo que a vos te interesa probar.
3. Diseñar tests que reflejen TU caso de uso (no el de papers de Stanford).
4. Auto-evaluar con un juez local gratis (Phi-4 corriendo en tu compu).
5. Decidir qué modelo poner en N8N / OpenClaw / tu producto, con criterios reales.

## Mapa de los tutoriales

| # | Tutorial | Dificultad | Tiempo | Costo aprox |
|---|----------|------------|--------|-------------|
| 1 | [Replicá el benchmark en 30 minutos](01-quick-start.md) | Principiante | 30 min | <$1 USD |
| 2 | [Agregá tu propio modelo al benchmark](02-agregar-tu-modelo.md) | Principiante | 20-40 min | <$0.50 USD |
| 3 | [Diseñá un test custom para TU caso de uso](03-disenar-test-custom.md) | Intermedio | 45-60 min | <$1 USD |
| 4 | [Setup del LLM-as-Judge local con Phi-4](04-configurar-phi4-judge.md) | Intermedio | 30 min + descarga | $0 (local) |
| 5 | [Cómo decidir qué modelo poner en producción](05-elegir-modelo-para-tu-caso.md) | Intermedio | 30 min lectura + 1-2h validación | <$2 USD |

## Orden recomendado

Si nunca corriste el repo: **1 → 2 → 4 → 3 → 5**.

- 1 te da la confianza de que todo funciona en tu máquina.
- 2 te enseña cómo el benchmark se extiende (vas a hacer esto seguido).
- 4 instala el juez local — vas a querer tenerlo antes de tests grandes para no quemar API.
- 3 te lleva al "modo emprendedor": tests que reflejan tu negocio.
- 5 cierra con el framework de decisión real para producción.

Si solo querés decidir un modelo y no replicar nada, leé directo el **5** y usá la calculadora en <https://benchmarks.cristiantala.com/>.

## Pre-requisito común

Una vez antes de empezar cualquier tutorial:

```bash
cd /ruta/a/ai-benchmarks-alternativos
cp .env.example .env
# Abrí .env y pegá al menos OPENROUTER_API_KEY=sk-or-...
# Crear key gratis (depositás $5-10): https://openrouter.ai/keys
```

Con $5 USD en OpenRouter te alcanza para correr los 5 tutoriales completos varias veces. Con $20 USD entrás en territorio profesional.

## Si te trabás

- Errores de Python / dependencias → revisá tutorial 1, sección "Si falla X, hacé Y".
- Costos inesperados → tutorial 5, sección "Anti-patterns".
- Querés saber qué hace internamente el runner → leé `CLAUDE.md` en la raíz, está explicado para agentes pero también para humanos.

## Filosofía del repo

Cristian (autor) es emprendedor chileno usando OpenClaw + N8N en producción. El repo nació porque los benchmarks públicos miden "razonamiento académico" y él necesitaba saber **qué modelo le genera mejores newsletters de startups en español**. Eso es lo que vas a aprender a medir vos también.

Buena suerte. Si encontrás bugs en los tutoriales, abrí un issue en GitHub.
