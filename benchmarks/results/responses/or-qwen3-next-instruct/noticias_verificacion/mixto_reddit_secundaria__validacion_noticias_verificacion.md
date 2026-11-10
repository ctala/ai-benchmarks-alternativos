# Qwen 3-Next 80B Instruct — noticias_verificacion/mixto_reddit_secundaria

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.66 | quality: 10.0
- latency_total: 1.291s | tokens_per_second: 121.6
- input_tokens: 1087 | output_tokens: 157

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
Reddit prices IPO at top of range, raising $748 million

San Francisco — Reddit priced its initial public offering at $34 per share in March 2024, the top of the $31 to $34 range it had marketed to investors, raising about $748 million. At that price, the social media company is valued at about $6.4 billion.

Not all of the money goes to the company. About $228 million corresponds to shares sold by existing shareholders who chose to cash out part of their holdings. Excluding those secondary sales, Reddit raised gross proceeds of $519.4 million.

The shares are set to begin trading on the New York Stock Exchange under the ticker RDDT. Morgan Stanley, Goldman Sachs, JPMorgan Chase and Bank of America are the lead underwriters.

Initial public offerings of consumer internet companies had been rare for more than two years. Rising interest rates pushed investors toward profitable companies and away from businesses that promised growth in the future, and many startups that had planned to list in 2022 postponed their plans. Bankers had been watching the Reddit listing as a test of whether that window was reopening.

Reddit's business depends on advertising, which makes it sensitive to the same swings that affect other social platforms. The company has also started to license its archive of public conversations to companies that train artificial intelligence models, a source of revenue that did not exist a few years ago and that investors are still trying to value.

The company took an unusual step for a listing of its size: it set aside part of the offering for some of its most active users and moderators, who could buy shares at the IPO price before trading began. The move reflects how much the platform depends on volunteers who run its communities without pay.

Founded in 2005 by Steve Huffman and Alexis Ohanian, Reddit was acquired by Condé Nast a year later and became independent again in 2011. Huffman is the company's chief executive.

Investors also weighed the company's governance. Like many technology companies that list their shares, Reddit set up a structure that gives some shareholders more voting power than others, which limits the influence of the investors who buy in the offering. Supporters say such structures let management plan for the long term; critics say they weaken accountability. The debate has accompanied almost every large technology listing of the past decade, and index providers have at times excluded companies with unequal voting rights from some benchmarks.

The IPO valuation is well below what private investors paid for the company before the market downturn. In a private fundraising round in 2021, Reddit was valued at $10 billion.

AFIRMACIONES A VERIFICAR (6):
1. Reddit fijó el precio de su OPI en el piso del rango, US$31 por acción.
2. Sin contar la venta de accionistas existentes, Reddit obtuvo US$519,4 millones brutos.
3. Reddit cotizará en la Bolsa de Nueva York bajo el símbolo RDDT.
4. Steve Huffman es el director ejecutivo de Reddit.
5. Reddit reservó parte de la oferta para usuarios activos y moderadores.
6. En 2021, una ronda privada valoró a Reddit en US$10.000 millones.


## Respuesta completa

{
  "veredictos": [
    {
      "id": 1,
      "veredicto": "CONTRADICE"
    },
    {
      "id": 2,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 3,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 4,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 5,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 6,
      "veredicto": "RESPALDADO"
    }
  ]
}