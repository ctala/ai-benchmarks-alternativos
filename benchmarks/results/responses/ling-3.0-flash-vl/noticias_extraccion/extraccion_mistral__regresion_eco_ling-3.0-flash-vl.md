# Ling 3.0 Flash VL — noticias_extraccion/extraccion_mistral

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.09 | quality: 9.55
- latency_total: 6.913s | tokens_per_second: 269.1
- input_tokens: 1043 | output_tokens: 1860

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el extractor de afirmaciones de una redacción que publica noticias de startups, inversión y tecnología en español. Recibes una FUENTE (en español o en inglés). Tu trabajo es sacar TODAS las afirmaciones verificables que la fuente hace sobre la noticia, para que un verificador las contraste una por una antes de publicar.

Responde SOLO con JSON válido:
{"claims": [{"texto": "<una afirmación, en español, autocontenida>", "nucleo": true}]}

QUÉ ES UNA AFIRMACIÓN VERIFICABLE (sí se extrae):
- cifras, montos, porcentajes, valoraciones, cantidades;
- fechas de HECHOS relatados (cuándo se cerró, cotizó o aprobó algo);
- entidades y quién hizo qué: quién lideró, quién participó, quién compró, quién aprobó;
- atribuciones: si la fuente dice «según la empresa» o «según Reuters», la afirmación conserva la atribución («Según la empresa, …»).

QUÉ NO SE EXTRAE:
- conocimiento de dominio (cómo funciona una Serie B, qué es un marketplace), opiniones y adjetivos sin dato;
- la fecha de publicación de la propia nota;
- nada que la fuente no diga: no conviertas monedas, no sumes, no restes, no calcules.

nucleo=true → el hecho de la noticia misma: qué pasó, quién, cuánto, cuándo, con quién.
nucleo=false → contexto: rondas anteriores, historia de la empresa, tamaño de mercado, comparaciones, planes y declaraciones accesorias.

Cada afirmación debe nombrar a la entidad de la que habla (nada de «la empresa» sin nombre). Una afirmación por dato. Lee la fuente COMPLETA, hasta el último párrafo: los datos del final cuentan igual que los del principio.

**user:**

FUENTE:
Mistral AI raises €385 million, its second round in seven months

Paris — Mistral AI, the French startup that builds large language models, has raised €385 million in a round led by Andreessen Horowitz and Lightspeed Venture Partners. Reuters put the amount at about $414.41 million. The round values the company at about $2 billion, according to Bloomberg.

Salesforce, the French public investment bank Bpifrance and the shipping group CMA CGM also invested, along with individual backers including former Google chief executive Eric Schmidt and the investor Elad Gil.

Building foundation models is among the most expensive activities in software. Training a competitive model requires thousands of specialized chips for weeks or months, and the cost of that compute has to be paid before a single customer signs up. For that reason, most labs raise capital at a pace that would be unusual for any other kind of startup, and investors accept losses for years in exchange for a position in what they see as a platform shift.

Mistral has taken a different route from some of its American rivals by releasing several of its models with open weights, which lets developers download and run them on their own infrastructure. The company argues that this builds trust with enterprises that do not want to send sensitive data to a third party, and that it creates a community that improves and tests the models for free.

The company was founded in Paris in 2023 by Arthur Mensch, a former researcher at Google DeepMind, and Timothée Lacroix and Guillaume Lample, who previously worked at Meta.

European governments have treated the startup as a strategic asset. Policymakers in France have argued that the continent needs its own model developers rather than depending entirely on companies in the United States, and that argument has shaped the debate over how the European Union regulates artificial intelligence.

Customers evaluating models now look beyond raw benchmark results. Price per token, latency, the ability to run a model inside their own data centers and the terms under which their data is processed all weigh on the decision. That opens room for smaller developers whose models are not the most capable on every test but are cheaper to run, easier to customize or better suited to regulated industries such as banking, health care and the public sector, where control over data is often a legal requirement rather than a preference.

This is Mistral's second funding round in seven months. Its earlier seed round, of €105 million and led by Lightspeed, was described at the time as the largest seed round in European history. That round valued the young company at €240 million.



## Respuesta completa

```json
{
  "claims": [
    {
      "texto": "Mistral AI recaudó 385 millones de euros en una ronda liderada por Andreessen Horowitz y Lightspeed Venture Partners.",
      "nucleo": true
    },
    {
      "texto": "Según Reuters, el monto de la ronda asciende a aproximadamente 414,41 millones de dólares.",
      "nucleo": true
    },
    {
      "texto": "Según Bloomberg, la ronda valora a Mistral AI en aproximadamente 2.000 millones de dólares.",
      "nucleo": true
    },
    {
      "texto": "Salesforce, el banco público de inversión francés Bpifrance y el grupo naviero CMA CGM también invirtieron en la ronda de Mistral AI.",
      "nucleo": true
    },
    {
      "texto": "Eric Schmidt, exdirector ejecutivo de Google, y el inversor Elad Gil participaron como inversores individuales en la ronda de Mistral AI.",
      "nucleo": true
    },
    {
      "texto": "Mistral AI fue fundada en París en 2023 por Arthur Mensch, exinvestigador de Google DeepMind, y Timothée Lacroix y Guillaume Lample, quienes trabajaron previamente en Meta.",
      "nucleo": true
    },
    {
      "texto": "Mistral AI ha liberado varios de sus modelos con pesos abiertos.",
      "nucleo": false
    },
    {
      "texto": "Es la segunda ronda de financiación de Mistral AI en siete meses.",
      "nucleo": true
    },
    {
      "texto": "La ronda semilla anterior de Mistral AI fue de 105 millones de euros y fue liderada por Lightspeed Venture Partners.",
      "nucleo": false
    },
    {
      "texto": "La ronda semilla anterior fue descrita en su momento como la mayor ronda semilla de la historia europea.",
      "nucleo": false
    },
    {
      "texto": "Esa ronda semilla valoró a Mistral AI en 240 millones de euros.",
      "nucleo": false
    }
  ]
}
```