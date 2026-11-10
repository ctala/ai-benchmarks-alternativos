# Ling 3.0 Flash — noticias_verificacion/mixto_klar_deuda

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 2.387s | tokens_per_second: 156.3
- input_tokens: 1067 | output_tokens: 373

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
Mexican fintech Klar raises $190 million Series C led by General Atlantic

Mexico City — Klar, the Mexican digital bank, has raised $190 million in a Series C round led by General Atlantic, Bloomberg reported. The round, closed in mid-2025, values the company at more than $800 million.

The financing combines $170 million in equity with $20 million in venture debt.

Existing investors Prosus, IFC, Mouro Capital and Quona Capital took part, and the round brought in new backers including Santander Group, Grupo Televisa and Grupo Fórmula.

Digital banks in Mexico target a population that has historically been underserved by traditional lenders. A large share of adults do not have a credit card, and many who apply are rejected because they lack a credit history. The newer players try to solve that with secured cards, small initial credit limits that grow with good payment behavior, and underwriting models that use alternative data. The trade-off is risk: lending to customers without a history requires careful collection practices and enough capital to absorb losses in a downturn.

Klar was founded in 2019 by Stefan Möller. The company offers a debit account, a credit card and personal loans through its app.

According to the company, the money will go toward growth in Mexico, new products and reaching more customers. Klar is also expanding into services for small businesses and is pursuing a banking license, which would allow it to take deposits under the same rules as a traditional bank.

The round comes as investment in Mexican fintech recovers after two quiet years. Larger rounds are again going to companies that can show both growth and a credible path to profitability. One report cited in the coverage said Klar is approaching $300 million in annual revenue as it shifts its focus from growth to profitability.

For investors, the appeal of the segment lies in the size of the gap. Mexico has one of the lowest rates of credit penetration among large Latin American economies, and every customer who builds a good payment record becomes eligible for larger and more profitable products. The risk is that competition for those same customers is intensifying: traditional banks have improved their apps, retailers offer their own credit, and other digital banks with deep-pocketed backers are chasing the same users with promotional rates and rewards programs that compress margins for everyone in the market.

This is not the first time General Atlantic has led a round for the company. In an earlier round, Klar raised $70 million at a $500 million valuation, also led by General Atlantic.

AFIRMACIONES A VERIFICAR (5):
1. General Atlantic lideró la Serie C de US$190 millones de Klar.
2. De los US$190 millones, US$50 millones son deuda.
3. Grupo Televisa entró como inversionista nuevo de Klar.
4. Klar busca una licencia bancaria.
5. En una ronda anterior, Klar levantó US$70 millones a una valoración de US$500 millones.


## Respuesta completa

```json
{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}, {"id": 2, "veredicto": "CONTRADICE"}, {"id": 3, "veredicto": "RESPALDADO"}, {"id": 4, "veredicto": "RESPALDADO"}, {"id": 5, "veredicto": "RESPALDADO"}]}
```