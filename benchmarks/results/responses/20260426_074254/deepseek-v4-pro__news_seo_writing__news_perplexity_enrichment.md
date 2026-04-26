# DeepSeek V4 Pro — news_seo_writing/news_perplexity_enrichment

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.55 | quality: 7.86
- latency_total: 69.463s | tokens_per_second: 29.5
- input_tokens: 515 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y ofrece una buena profundidad con insights útiles sobre la arquitectura MoE y el impacto económico de DeepSeek V4. Está bien escrita y organizada, adecuada para un emprendedor, y utiliza un estilo periodístico efectivo.

## Respuesta completa

DeepSeek irrumpe con V4: el modelo abierto que desafía a los gigantes con costos ínfimos

La startup china DeepSeek acaba de liberar la cuarta versión de su modelo de lenguaje, una jugada que trastoca el tablero de la inteligencia artificial. V4 combina el código abierto bajo licencia MIT con un precio de inferencia tan agresivo que fuerza a los grandes proveedores a revisar sus tarifas. El extracto original de su anuncio es tan breve como contundente: “DeepSeek released V4, their latest open-source AI model under MIT license. The model costs $0.30 per million input tokens”. Detrás de esa línea se esconde un salto técnico y estratégico que vale la pena desmenuzar.

## Un MoE de 236 mil millones de parámetros con solo 21 mil millones activos

DeepSeek V4 apuesta por una arquitectura de mezcla de expertos (MoE). El modelo alberga 236 mil millones de parámetros en total, pero solo activa 21 mil millones por token, según los datos del blog oficial de la compañía. Este diseño permite un rendimiento comparable al de modelos mucho más grandes —como GPT-4o o Claude Sonnet— sin que el costo computacional se dispare.

El entrenamiento se realizó sobre 15 billones de tokens (15T), un corpus masivo que abarca texto público y datos curados. La eficiencia del MoE es clave para entender por qué DeepSeek puede ofrecer un modelo de esta envergadura con precios tan bajos. En lugar de lanzar un titán monolítico que obligue a procesar cada parámetro en cada consulta, V4 elige dinámicamente los “expertos” adecuados para cada token, reduciendo la carga sin sacrificar calidad.

## Precios que redefinen la economía de la IA generativa

El titular del lanzamiento se resume en números: 0,30 dólares por cada millón de tokens de entrada. Pero hay una segunda cifra que merece tanta atención como la primera. El almacenamiento en caché de tokens —una función que acelera y abarata las consultas repetitivas— cuesta tan solo 0,03 dólares por millón de tokens, un descuento del 90 % respecto a la tarifa estándar.

Estos precios colocan a V4 muy por debajo de las opciones equivalentes de los grandes laboratorios estadounidenses. Para una startup que procesa millones de tokens al día, el ahorro es inmediato y puede determinar la viabilidad de productos enteros. DeepSeek no solo compite en calidad de respuestas, sino que pelea la batalla del margen, un terreno donde la autofinanciación le da una ventaja insólita.

## Quién está detrás del modelo

DeepSeek opera desde Hangzhou, China, y surgió como una escisión del fondo de cobertura High-Flyer. La empresa tiene alrededor de 300 empleados y, según la información recabada por TechCrunch, no ha recaudado un solo dólar de inversión externa. Todo su capital procede de High-Flyer, lo que le permite tomar decisiones sin la presión de los plazos típicos del venture capital.

Este respaldo financiero explica cómo un equipo relativamente pequeño puede entrenar modelos de vanguardia y competir con organizaciones que manejan presupuestos de miles de millones. Mientras OpenAI, Anthropic o Google deben rendir cuentas ante inversores —y, en algunos casos, ante mercados públicos—, DeepSeek se concentra exclusivamente en la eficiencia técnica y en la apertura de su código.

## La licencia MIT: qué implica realmente

El modelo se distribuye bajo licencia MIT, una de las más permisivas que existen. Cualquier persona o empresa puede usar V4, modificarlo, integrarlo en productos comerciales y redistribuirlo con muy pocas restricciones. La principal obligación es conservar el aviso de copyright en el software distribuido.

Para las startups esto elimina la fricción legal que acompaña a otros modelos abiertos con licencias más restrictivas, como las que prohíben el uso comercial o imponen cláusulas de reciprocidad. V4 se convierte así en un componente que se puede embeber sin miedo en aplicaciones SaaS, chatbots, asistentes internos o herramientas de análisis de documentos.

## Competencia directa con los pesos pesados

DeepSeek posiciona a V4 frente a GPT-4o y Claude Sonnet, dos de los modelos más populares entre desarrolladores. Las evaluaciones internas citadas en su blog muestran un rendimiento equiparable en razonamiento, generación de código y comprensión multilingüe. Aunque los benchmarks siempre deben tomarse con cautela —cada laboratorio elige las métricas que más le favorecen—, las primeras pruebas de la comunidad sugieren que V4 está, como mínimo, en el mismo escalón que las ofertas de OpenAI y Anthropic.

La gran diferencia vuelve a ser el precio. Mientras los modelos propietarios cobran entre 2,50 y 15 dólares por millón de tokens (según el modelo y el tipo de consulta), V4 baja la barrera de entrada a unos pocos centavos. Para empresas que escalan rápido, esta estructura de costos puede ser la diferencia entre quemar capital en infraestructura o reinvertirlo en producto.

## La sombra de las sanciones y las restricciones de chips

El origen chino de DeepSeek plantea interrogantes sobre la cadena de suministro tecnológico. Las sanciones de Estados Unidos han limitado la exportación de GPUs avanzadas a China, pero High-Flyer acumuló un stock significativo de hardware antes de que las restricciones entraran en vigor. Esta previsión, combinada con la eficiencia del diseño MoE, le ha permitido a DeepSeek entrenar V4 sin depender de los chips más recientes.

A pesar de las tensiones geopolíticas, la compañía ha mantenido un perfil técnico y ha evitado polémicas públicas. Su apuesta por el código abierto funciona como una carta de transparencia que reduce la desconfianza de la comunidad internacional. Nadie duda de que un modelo abierto puede ser auditado, bifurcado y ejecutado en servidores fuera de China.

## Qué significa esto para tu startup

Si estás construyendo una aplicación que depende de grandes modelos de lenguaje, V4 cambia tus cálculos de costo unitario. Con 0,30 dólares por millón de tokens, muchas ideas que antes eran inviables financieramente ahora entran en zona verde. Y si tus usuarios tienden a repetir consultas similares, los 0,03 dólares de la caché reducen aún más la factura.

La licencia MIT te permite afinar el modelo con datos propios utilizando técnicas de fine-tuning y luego desplegarlo en tu propia infraestructura, sin royalties ni permisos adicionales.