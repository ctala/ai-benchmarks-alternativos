"""
Suite noticias_seo_discover — Título y metadatos para Google Discover.

PENDIENTE DE IMPLEMENTACIÓN: requiere notas de Eco y licencia CC BY 4.0.

Diseño:
- 15 tests con notas publicadas
- Entrada: texto completo de nota + reglas Google Discover
- Salida: JSON con titulo (≤60), meta_titulo (≤60), meta_descripcion (120-155),
  slug (kebab-case, ≤6 palabras), keyword_principal, alt_imagen, 2 titulos_alternativos
- Tokens por test: ~2.800

Reglas Google Discover (consultadas 10-oct-2026):
https://developers.google.com/search/docs/appearance/google-discover
- Evitar clickbait, detalles exagerados, sensacionalismo
- No ocultar información clave
- Títulos que capturen esencia del contenido

Puntuación:
- Automático 70%: JSON válido, largos, formato slug, keyword en título y meta,
  ninguna cifra inventada, sin patrones clickbait ("no vas a creer", "!!",
  mayúsculas sostenidas)
- Verificador Phi-4 30%: 2 preguntas
  (a) ¿Título promete algo que nota no entrega, o esconde dato clave?
  (b) ¿Nombra protagonista y hecho?

Límite: mide guía pública, NO tráfico real (requeriría Search Console).

FUENTE: /workspace/uploads/benchmark-pack-noticias_e470.md § 4.5
BLOQUEANTE: 15 notas + protagonista anotado (~15 min) + licencia CC BY
"""

TESTS = [
    # Placeholder - requiere notas reales de Eco
]
