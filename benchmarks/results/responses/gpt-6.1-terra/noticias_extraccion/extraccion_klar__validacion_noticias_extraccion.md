# GPT-6.1 Terra — noticias_extraccion/extraccion_klar

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 14.063s | tokens_per_second: 82.8
- input_tokens: 900 | output_tokens: 1164

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

{"claims":[{"texto":"Según Bloomberg, Klar, un banco digital mexicano, recaudó 190 millones de dólares en una ronda Serie C.","nucleo":true},{"texto":"Según Bloomberg, General Atlantic lideró la ronda Serie C de Klar.","nucleo":true},{"texto":"La ronda Serie C de Klar se cerró a mediados de 2025.","nucleo":true},{"texto":"La ronda Serie C valoró a Klar en más de 800 millones de dólares.","nucleo":true},{"texto":"La financiación de la Serie C de Klar incluye 170 millones de dólares en capital.","nucleo":true},{"texto":"La financiación de la Serie C de Klar incluye 20 millones de dólares en deuda de riesgo.","nucleo":true},{"texto":"Prosus, inversor existente de Klar, participó en la ronda Serie C.","nucleo":true},{"texto":"IFC, inversor existente de Klar, participó en la ronda Serie C.","nucleo":true},{"texto":"Mouro Capital, inversor existente de Klar, participó en la ronda Serie C.","nucleo":true},{"texto":"Quona Capital, inversor existente de Klar, participó en la ronda Serie C.","nucleo":true},{"texto":"Santander Group se incorporó como nuevo inversor de Klar en la ronda Serie C.","nucleo":true},{"texto":"Grupo Televisa se incorporó como nuevo inversor de Klar en la ronda Serie C.","nucleo":true},{"texto":"Grupo Fórmula se incorporó como nuevo inversor de Klar en la ronda Serie C.","nucleo":true},{"texto":"Una gran proporción de los adultos en México no tiene tarjeta de crédito.","nucleo":false},{"texto":"Muchas personas que solicitan una tarjeta de crédito en México son rechazadas por carecer de historial crediticio.","nucleo":false},{"texto":"Stefan Möller fundó Klar en 2019.","nucleo":false},{"texto":"Klar ofrece una cuenta de débito a través de su aplicación.","nucleo":false},{"texto":"Klar ofrece una tarjeta de crédito a través de su aplicación.","nucleo":false},{"texto":"Klar ofrece préstamos personales a través de su aplicación.","nucleo":false},{"texto":"Según Klar, los fondos se destinarán a impulsar su crecimiento en México.","nucleo":false},{"texto":"Según Klar, los fondos se destinarán a desarrollar nuevos productos.","nucleo":false},{"texto":"Según Klar, los fondos se destinarán a llegar a más clientes.","nucleo":false},{"texto":"Klar está expandiéndose hacia servicios para pequeñas empresas.","nucleo":false},{"texto":"Klar está buscando obtener una licencia bancaria.","nucleo":false},{"texto":"La inversión en fintech mexicanas se está recuperando tras dos años de poca actividad.","nucleo":false},{"texto":"Las rondas de mayor tamaño en las fintech mexicanas vuelven a dirigirse a compañías que muestran crecimiento y una vía creíble hacia la rentabilidad.","nucleo":false},{"texto":"Según un informe citado en la cobertura, Klar se acerca a los 300 millones de dólares en ingresos anuales.","nucleo":false},{"texto":"Según un informe citado en la cobertura, Klar está cambiando su enfoque del crecimiento a la rentabilidad.","nucleo":false},{"texto":"México tiene una de las tasas de penetración crediticia más bajas entre las grandes economías de América Latina.","nucleo":false},{"texto":"La competencia por los clientes en el sector del crédito en México se está intensificando.","nucleo":false},{"texto":"Los bancos tradicionales en México han mejorado sus aplicaciones.","nucleo":false},{"texto":"Los comercios minoristas en México ofrecen sus propios créditos.","nucleo":false},{"texto":"Otros bancos digitales en México compiten por los mismos usuarios con tasas promocionales y programas de recompensas.","nucleo":false},{"texto":"Las tasas promocionales y los programas de recompensas de los bancos digitales en México comprimen los márgenes del mercado.","nucleo":false},{"texto":"Klar recaudó 70 millones de dólares en una ronda anterior.","nucleo":false},{"texto":"La ronda anterior de Klar valoró la compañía en 500 millones de dólares.","nucleo":false},{"texto":"General Atlantic lideró la ronda anterior de Klar.","nucleo":false}]}