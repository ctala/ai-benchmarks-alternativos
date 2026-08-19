# Claude Fable 5 (suscripción) — translation/detect_language_issues

- model_id: `claude-fable-5`
- success: True  | final: 5.82 | quality: 7.15
- latency_total: 15.437s | tokens_per_second: 79.6
- input_tokens: 2 | output_tokens: 1229

## Respuesta completa

```json
{
  "problemas": [
    {
      "tipo": "chino",
      "texto": "En特别是在拉丁美洲",
      "correccion": "Especialmente en Latinoamérica"
    },
    {
      "tipo": "gramatical",
      "texto": "los emprendedores estan",
      "correccion": "los emprendedores están (falta tilde)"
    },
    {
      "tipo": "spanglish",
      "texto": "estan leveraging nuevas herramientas",
      "correccion": "están aprovechando nuevas herramientas"
    },
    {
      "tipo": "spanglish",
      "texto": "para scale their businesses",
      "correccion": "para escalar sus negocios"
    },
    {
      "tipo": "spanglish",
      "texto": "permite optimize los procesos",
      "correccion": "permite optimizar los procesos"
    },
    {
      "tipo": "spanglish",
      "texto": "de manera unprecedented",
      "correccion": "de manera sin precedentes / inédita"
    },
    {
      "tipo": "spanglish",
      "texto": "Las companies que adoptan AI",
      "correccion": "Las empresas que adoptan IA"
    },
    {
      "tipo": "spanglish",
      "texto": "tienen un competitive advantage significativo",
      "correccion": "tienen una ventaja competitiva significativa"
    },
    {
      "tipo": "spanglish",
      "texto": "hacer un deep dive en las opciones disponibles",
      "correccion": "analizar a fondo las opciones disponibles"
    },
    {
      "tipo": "spanglish",
      "texto": "encontrar la best fit para tu organización",
      "correccion": "encontrar la opción que mejor se ajuste a tu organización"
    },
    {
      "tipo": "cliche",
      "texto": "La inteligencia artificial ha revolucionado el mundo de las startups",
      "correccion": "Apertura genérica de IA. Reemplazar por un dato concreto o ejemplo específico (ej. cifra de adopción, caso real)"
    },
    {
      "tipo": "cliche",
      "texto": "Es importante hacer un deep dive",
      "correccion": "'Es importante...' es relleno típico de IA. Ir directo: 'Antes de elegir herramienta, compara X, Y y Z'"
    }
  ],
  "score_idioma": 1,
  "veredicto": "inaceptable"
}
```

**Nota:** el texto mezcla 3 idiomas (español, inglés, chino) — síntoma clásico de un modelo barato sin control de idioma de salida. Más allá de las correcciones puntuales, requiere reescritura completa, no edición. Con ~10 anglicismos en 2 párrafos, corregir palabra por palabra dejaría igual un texto genérico sin sustancia (cero cifras, cero ejemplos concretos).