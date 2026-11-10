# Qwen 3-Next 80B Instruct — noticias_extraccion/extraccion_databricks

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.25 | quality: 8.54
- latency_total: 4.23s | tokens_per_second: 170.0
- input_tokens: 1045 | output_tokens: 719

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
Databricks raises $10 billion at a $62 billion valuation

San Francisco — Databricks, the data and artificial intelligence company, said it is raising $10 billion in a Series J round at a $62 billion valuation, one of the largest venture rounds ever recorded. The company described the financing as non-dilutive and said $8.6 billion had been completed so far.

The round is led by Thrive Capital, a new investor in the company. Andreessen Horowitz, DST Global, GIC, Insight Partners and WCM Investment Management are co-leads, and Ontario Teachers' Pension Plan is also taking part. New investors include ICONIQ Growth, MGX, Sands Capital and Wellington Management.

Data platforms have become the plumbing behind most corporate AI projects. Before a company can train or fine-tune a model, or even ask a chatbot questions about its own documents, it needs its data in one place, cleaned and governed so that only the right people and systems can reach it. Vendors that already store and process that data are well positioned to sell the AI tools that sit on top of it, which is why the category has attracted so much capital.

The new valuation is 44% higher than the $43 billion the company was valued at in September 2023.

Databricks said it plans to use the money to invest in new AI products, make acquisitions and significantly expand its international go-to-market operations. Part of the proceeds will provide liquidity for current and former employees, and to pay related taxes.

That last item says as much about the market as about the company. Late-stage startups are staying private for longer, and many employees hold stock that they cannot sell until there is an initial public offering. Large rounds that include a secondary component let those employees turn part of their equity into cash without the company having to go public.

Databricks has not said when it might list its shares. Executives have repeatedly said the company could go public when market conditions are right, but that it does not need to.

Competition in the category is intense. Cloud providers offer their own data warehouses and AI tools, often bundled with other services, and rival independent vendors compete on price and ease of use. Customers increasingly ask for open formats that let them move data between platforms without being locked in, which pushes vendors to compete on performance, governance and the quality of the tools built on top of the data rather than on the storage itself.

The company also gave an update on its finances. Databricks said it expects to cross a $3 billion revenue run-rate and to be free cash flow positive for the first time in the fourth quarter of its fiscal year, which ends January 31, 2025. Separately, it closed a $5.25 billion credit facility led by JPMorgan Chase.



## Respuesta completa

{
  "claims": [
    {
      "texto": "Databricks está recaudando $10 mil millones en una ronda Serie J a una valoración de $62 mil millones.",
      "nucleo": true
    },
    {
      "texto": "Databricks describió la financiación como no dilutiva.",
      "nucleo": true
    },
    {
      "texto": "Databricks dijo que $8,6 mil millones de la ronda ya se han completado.",
      "nucleo": true
    },
    {
      "texto": "Thrive Capital lidera la ronda de financiación de Databricks.",
      "nucleo": true
    },
    {
      "texto": "Andreessen Horowitz, DST Global, GIC, Insight Partners y WCM Investment Management son co-líderes de la ronda de financiación de Databricks.",
      "nucleo": true
    },
    {
      "texto": "Ontario Teachers' Pension Plan participa en la ronda de financiación de Databricks.",
      "nucleo": true
    },
    {
      "texto": "ICONIQ Growth, MGX, Sands Capital y Wellington Management son nuevos inversores en la ronda de financiación de Databricks.",
      "nucleo": true
    },
    {
      "texto": "La valoración de Databricks es un 44% más alta que los $43 mil millones que tenía en septiembre de 2023.",
      "nucleo": true
    },
    {
      "texto": "Databricks planea usar el dinero recaudado para invertir en nuevos productos de IA, realizar adquisiciones y expandir significativamente sus operaciones internacionales de comercialización.",
      "nucleo": true
    },
    {
      "texto": "Parte de los fondos recaudados por Databricks se destinará a proporcionar liquidez a empleados actuales y anteriores y para pagar impuestos relacionados.",
      "nucleo": true
    },
    {
      "texto": "Databricks no ha anunciado cuándo podría listar sus acciones.",
      "nucleo": true
    },
    {
      "texto": "Los ejecutivos de Databricks han dicho repetidamente que la empresa podría salir a bolsa cuando las condiciones del mercado lo permitan, pero que no necesita hacerlo.",
      "nucleo": true
    },
    {
      "texto": "Databricks espera superar un ritmo anual de ingresos de $3 mil millones en el cuarto trimestre de su año fiscal, que termina el 31 de enero de 2025.",
      "nucleo": true
    },
    {
      "texto": "Databricks espera ser positivo en flujo de efectivo libre por primera vez en el cuarto trimestre de su año fiscal, que termina el 31 de enero de 2025.",
      "nucleo": true
    },
    {
      "texto": "Databricks cerró una línea de crédito de $5,25 mil millones liderada por JPMorgan Chase.",
      "nucleo": true
    }
  ]
}