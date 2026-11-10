# Qwen 3-Next 80B Instruct — noticias_extraccion/extraccion_klar

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.21 | quality: 9.86
- latency_total: 3.492s | tokens_per_second: 173.3
- input_tokens: 991 | output_tokens: 605

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



## Respuesta completa

{
  "claims": [
    {
      "texto": "Klar, la banca digital mexicana, ha recaudado 190 millones de dólares en una ronda Serie C liderada por General Atlantic.",
      "nucleo": true
    },
    {
      "texto": "La ronda Serie C de Klar se cerró a mediados de 2025.",
      "nucleo": true
    },
    {
      "texto": "La ronda Serie C de Klar valora a la empresa en más de 800 millones de dólares.",
      "nucleo": true
    },
    {
      "texto": "La financiación de la ronda Serie C de Klar combina 170 millones de dólares en capital propio con 20 millones de dólares en deuda de capital de riesgo.",
      "nucleo": true
    },
    {
      "texto": "Los inversionistas existentes Prosus, IFC, Mouro Capital y Quona Capital participaron en la ronda Serie C de Klar.",
      "nucleo": true
    },
    {
      "texto": "Nuevos inversionistas, incluyendo Santander Group, Grupo Televisa y Grupo Fórmula, participaron en la ronda Serie C de Klar.",
      "nucleo": true
    },
    {
      "texto": "Klar fue fundada en 2019 por Stefan Möller.",
      "nucleo": true
    },
    {
      "texto": "Klar ofrece una cuenta de débito, una tarjeta de crédito y préstamos personales a través de su aplicación.",
      "nucleo": true
    },
    {
      "texto": "Según la empresa, el dinero de la ronda Serie C se destinará al crecimiento en México, nuevos productos y alcanzar a más clientes.",
      "nucleo": false
    },
    {
      "texto": "Klar está expandiéndose hacia servicios para pequeñas empresas.",
      "nucleo": false
    },
    {
      "texto": "Klar está buscando una licencia bancaria que le permita aceptar depósitos bajo las mismas reglas que un banco tradicional.",
      "nucleo": false
    },
    {
      "texto": "Según un informe citado en la cobertura, Klar se acerca a 300 millones de dólares en ingresos anuales.",
      "nucleo": false
    },
    {
      "texto": "General Atlantic lideró una ronda anterior de Klar en la que la empresa recaudó 70 millones de dólares a una valoración de 500 millones de dólares.",
      "nucleo": false
    }
  ]
}