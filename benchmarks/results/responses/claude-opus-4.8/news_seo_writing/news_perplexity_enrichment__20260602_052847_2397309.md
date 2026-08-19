# Claude Opus 4.8 — news_seo_writing/news_perplexity_enrichment

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 6.22 | quality: 7.89
- latency_total: 32.291s | tokens_per_second: 63.4
- input_tokens: 795 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y ofrece una buena profundidad al integrar detalles técnicos y económicos. Está bien estructurada y escrita, con un estilo periodístico adecuado para SEO.

## Respuesta completa

## DeepSeek lanza V4: un modelo de IA de codigo abierto que presiona los precios del mercado

La empresa china DeepSeek presento V4, la version mas reciente de su modelo de inteligencia artificial de codigo abierto, distribuido bajo licencia MIT. El anuncio reaviva la competencia en un sector donde el costo de operacion se ha convertido en un factor tan determinante como el rendimiento tecnico, y donde los modelos abiertos ganan terreno frente a las alternativas cerradas.

El dato que mas llama la atencion es el precio: V4 cuesta 0,30 dolares por cada millon de tokens de entrada. Para los equipos que construyen productos sobre modelos de lenguaje, esa cifra representa una variable directa en sus margenes operativos.

## Que ofrece V4 a nivel tecnico

DeepSeek V4 se apoya en una arquitectura de tipo Mixture of Experts (MoE), un enfoque que activa solo una fraccion de los parametros del modelo en cada operacion. En numeros concretos, V4 cuenta con 236.000 millones de parametros totales (236B), pero solo 21.000 millones (21B) se activan por inferencia.

Este diseno permite mantener un alto nivel de capacidad sin incurrir en el costo computacional de activar el modelo completo en cada consulta. Es precisamente esa eficiencia la que explica que la empresa pueda ofrecer precios tan agresivos sin comprometer la viabilidad del servicio.

El modelo fue entrenado con 15 billones de tokens (15T), un volumen de datos que lo coloca en el rango de los grandes modelos de frontera. Segun la documentacion publicada por la compania, V4 compite de forma directa con GPT-4o de OpenAI y Claude Sonnet de Anthropic, dos de las referencias actuales en el segmento de modelos comerciales de alto rendimiento.

## El factor cache: un descuento del 90%

Mas alla del precio base de entrada, DeepSeek introduce un elemento que puede resultar decisivo para ciertos casos de uso: el cache de tokens cuesta 0,03 dolares por millon, lo que equivale a un descuento del 90% frente al precio estandar de entrada.

El cache de tokens es relevante para aplicaciones que reutilizan contexto de forma repetida, como asistentes conversacionales con instrucciones de sistema extensas, herramientas de analisis documental o flujos de trabajo que procesan los mismos prompts una y otra vez. En esos escenarios, la posibilidad de pagar una fraccion del costo por contenido ya procesado puede traducirse en un ahorro sustancial a escala.

Para una startup que opera con volumenes altos de consultas, la diferencia entre 0,30 y 0,03 dolares por millon de tokens no es un detalle menor: es la diferencia entre un modelo de negocio sostenible y uno que sangra dinero en infraestructura.

## Una empresa autofinanciada y poco convencional

El perfil corporativo de DeepSeek aporta contexto al lanzamiento. La empresa tiene su sede en Hangzhou, China, y nacio como un spin-off de High-Flyer, un fondo de cobertura (hedge fund) cuantitativo. Esa raiz financiera explica en parte la estrategia: DeepSeek no ha recaudado capital externo, sino que se financia integramente con recursos de High-Flyer.

Con una plantilla de aproximadamente 300 empleados, la compania mantiene una estructura relativamente compacta para el nivel de ambicion tecnica que demuestra. El hecho de operar sin presion de inversionistas externos le otorga margen para tomar decisiones que otras empresas dificilmente adoptarian, como publicar modelos competitivos bajo licencia MIT y fijar precios que tensionan al resto del mercado.

La licencia MIT es un punto que merece atencion. Se trata de una de las licencias de codigo abierto mas permisivas que existen: permite usar, modificar y comercializar el modelo con restricciones minimas. Para los desarrolladores, esto significa que pueden integrar V4 en productos comerciales sin las limitaciones que imponen algunas licencias mas restrictivas asociadas a otros modelos abiertos.

## El contexto competitivo

El lanzamiento de V4 se inserta en una dinamica de mercado donde la presion sobre los precios se ha vuelto constante. Cuando un modelo de codigo abierto ofrece rendimiento comparable al de GPT-4o y Claude Sonnet a un costo significativamente menor, el efecto se extiende mas alla de DeepSeek: obliga a los demas actores a justificar sus tarifas o a ajustarlas.

La combinacion de codigo abierto, licencia permisiva y precios bajos configura una propuesta que apunta especificamente a desarrolladores y empresas sensibles al costo. No es casualidad que una compania autofinanciada, sin la necesidad de generar retornos inmediatos para inversionistas, sea quien empuje esta estrategia.

## Que significa esto para tu startup

Si tu producto depende de modelos de lenguaje, el lanzamiento de DeepSeek V4 introduce variables concretas que conviene evaluar:

- **Costos de inferencia.** A 0,30 dolares por millon de tokens de entrada, y especialmente con el cache a 0,03 dolares, V4 puede reducir de forma significativa tu gasto operativo frente a alternativas cerradas. Si procesas grandes volumenes o reutilizas contexto repetidamente, vale la pena correr los numeros con tus propios datos de uso.

- **Flexibilidad por la licencia MIT.** La posibilidad de modificar y comercializar el modelo sin restricciones relevantes abre opciones para quienes quieren personalizar, autohospedar o construir sob