# Gemma 4 31B — noticias_verificacion/bloquea_databricks_43_vs_34

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 1.45s | tokens_per_second: 124.2
- input_tokens: 1103 | output_tokens: 180

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el verificador de datos de una redacción. Recibes una FUENTE (en español o en inglés) y una lista numerada de AFIRMACIONES que alguien quiere publicar citándola. Decide, para CADA afirmación, si la fuente la respalda.

Responde SOLO con JSON válido, con un veredicto por cada afirmación y el mismo id:
{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}]}

RESPALDADO: la fuente afirma lo mismo, aunque con otras palabras, en otro idioma o con la cifra escrita en otro formato («US$1.500 millones» = «$1.5 billion»).
NO_RESPALDADO: la fuente no dice nada sobre eso, o lo que dice no alcanza para afirmarlo. La AUSENCIA nunca es contradicción.
CONTRADICE: la fuente afirma algo incompatible: otra cifra, otra fecha, otra entidad haciendo la acción (quién lideró, quién paga, quién confirma), o lo opuesto.

Reglas:
- Usa SOLO la fuente. No uses lo que sabes del mundo, aunque estés seguro.
- Si la fuente está truncada (muro de pago, «Suscríbete para seguir leyendo»), lo que no aparece en el fragmento es NO_RESPALDADO, nunca CONTRADICE.
- La atribución es parte del dato: «según Reuters» no es «la empresa confirmó».
- Lee la fuente completa, hasta el último párrafo, antes de decidir.
- Devuelve exactamente un veredicto por afirmación: ni menos, ni repetidos.

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

AFIRMACIONES A VERIFICAR (6):
1. Databricks recauda US$10.000 millones a una valoración de US$62.000 millones.
2. GIC es uno de los colíderes de la ronda.
3. La valoración es 44% mayor que los US$34.000 millones de septiembre de 2023.
4. Databricks saldrá a bolsa en 2025.
5. Databricks espera superar los US$3.000 millones de ingresos anualizados.
6. La línea de crédito de US$5.250 millones la lidera Goldman Sachs.


## Respuesta completa

```json
{
  "veredictos": [
    {
      "id": 1,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 2,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 3,
      "veredicto": "CONTRADICE"
    },
    {
      "id": 4,
      "veredicto": "NO_RESPALDADO"
    },
    {
      "id": 5,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 6,
      "veredicto": "CONTRADICE"
    }
  ]
}
```