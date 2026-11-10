# Tencent Hy4 — noticias_extraccion/extraccion_betterfly

- model_id: `tencent/hy4`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 105.854s | tokens_per_second: 119.6
- input_tokens: 1176 | output_tokens: 12659

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
Betterfly alcanza valoración de US$1.000 millones con una Serie C de US$125 millones

Santiago — Betterfly, la insurtech chilena que combina seguros de vida con una aplicación de hábitos saludables, levantó en febrero de 2022 una ronda Serie C de US$125 millones que la valora en US$1.000 millones.

La ronda fue liderada por Glade Brook Capital Partners. Entraron como nuevos inversionistas Greycroft, Lightrock y Mundi Ventures, y también participaron QED Investors, que había liderado la Serie A de la compañía, y DST Global Partners, que había encabezado la Serie B.

El modelo de Betterfly se vende principalmente a empleadores. Las empresas contratan la plataforma como beneficio para su personal, y cada trabajador acumula una moneda virtual cuando camina, medita o duerme bien. Esa moneda se convierte en cobertura de un seguro de vida que crece con el tiempo o en donaciones a causas sociales. La apuesta es que la prevención reduce el riesgo del asegurado y, con ello, el costo para la aseguradora.

Los seguros fueron durante años una de las industrias menos digitalizadas de la región. La venta depende de corredores, los productos son difíciles de comparar y la penetración de los seguros de vida en América Latina es baja frente a la de los países desarrollados. Las insurtech intentan cambiar eso con distribución digital y productos más simples, aunque la mayoría termina asociándose con aseguradoras tradicionales, que son las que asumen el riesgo.

La compañía fue fundada en 2018 por Eduardo della Maggiora, quien antes había creado otras empresas de tecnología en Chile.

Según la empresa, los fondos permitirán iniciar operaciones en siete nuevos mercados durante 2022, entre ellos México, Colombia y Argentina, y acelerar el desarrollo de su plataforma.

La industria de beneficios corporativos es competitiva. Plataformas de bienestar, gimnasios con convenios y las propias aseguradoras compiten por el mismo presupuesto de recursos humanos, y la retención de clientes depende de que los trabajadores realmente usen la aplicación.

Betterfly se presenta además como una empresa de impacto social, y varios medios la describieron como el primer unicornio social de América Latina, una etiqueta que la propia compañía promueve.

Para las aseguradoras tradicionales, las alianzas con plataformas como esta tienen un atractivo claro: llegan a clientes jóvenes que difícilmente comprarían un seguro de vida por iniciativa propia y obtienen datos sobre sus hábitos. Para la startup, el reto está en que el valor percibido por el trabajador se mantenga en el tiempo, porque la novedad de acumular puntos por caminar se desgasta rápido si la aplicación no ofrece algo más.

Con esta ronda, Betterfly se convierte en el tercer unicornio de Chile, después de Cornershop y NotCo.



## Respuesta completa

{"claims":[{"texto":"Betterfly es una insurtech chilena.","nucleo":false},{"texto":"Betterfly combina seguros de vida con una aplicación de hábitos saludables.","nucleo":false},{"texto":"Betterfly levantó en febrero de 2022 una ronda Serie C de US$125 millones.","nucleo":true},{"texto":"La ronda Serie C que Betterfly levantó en febrero de 2022 valora a Betterfly en US$1.000 millones.","nucleo":true},{"texto":"La ronda Serie C de Betterfly de febrero de 2022 fue liderada por Glade Brook Capital Partners.","nucleo":true},{"texto":"Greycroft entró como nuevo inversionista en la ronda Serie C de Betterfly de febrero de 2022.","nucleo":true},{"texto":"Lightrock entró como nuevo inversionista en la ronda Serie C de Betterfly de febrero de 2022.","nucleo":true},{"texto":"Mundi Ventures entró como nuevo inversionista en la ronda Serie C de Betterfly de febrero de 2022.","nucleo":true},{"texto":"QED Investors participó en la ronda Serie C de Betterfly de febrero de 2022.","nucleo":true},{"texto":"QED Investors había liderado la Serie A de Betterfly.","nucleo":false},{"texto":"DST Global Partners participó en la ronda Serie C de Betterfly de febrero de 2022.","nucleo":true},{"texto":"DST Global Partners había encabezado la Serie B de Betterfly.","nucleo":false},{"texto":"El modelo de Betterfly se vende principalmente a empleadores.","nucleo":false},{"texto":"Los empleadores contratan la plataforma de Betterfly como beneficio para su personal.","nucleo":false},{"texto":"En la plataforma de Betterfly, cada trabajador acumula una moneda virtual cuando camina, medita o duerme bien.","nucleo":false},{"texto":"En la plataforma de Betterfly, la moneda virtual acumulada por cada trabajador se convierte en cobertura de un seguro de vida que crece con el tiempo.","nucleo":false},{"texto":"En la plataforma de Betterfly, la moneda virtual acumulada por cada trabajador se convierte en donaciones a causas sociales.","nucleo":false},{"texto":"Betterfly fue fundada en 2018 por Eduardo della Maggiora.","nucleo":false},{"texto":"Eduardo della Maggiora había creado otras empresas de tecnología en Chile antes de la fundación de Betterfly.","nucleo":false},{"texto":"Según la empresa, los fondos de la ronda Serie C permitirán a Betterfly iniciar operaciones en siete nuevos mercados durante 2022.","nucleo":false},{"texto":"Según la empresa, México figura entre los siete nuevos mercados donde los fondos de la ronda Serie C permitirán a Betterfly iniciar operaciones durante 2022.","nucleo":false},{"texto":"Según la empresa, Colombia figura entre los siete nuevos mercados donde los fondos de la ronda Serie C permitirán a Betterfly iniciar operaciones durante 2022.","nucleo":false},{"texto":"Según la empresa, Argentina figura entre los siete nuevos mercados donde los fondos de la ronda Serie C permitirán a Betterfly iniciar operaciones durante 2022.","nucleo":false},{"texto":"Según la empresa, los fondos de la ronda Serie C permitirán acelerar el desarrollo de la plataforma de Betterfly.","nucleo":false},{"texto":"Betterfly se presenta como una empresa de impacto social.","nucleo":false},{"texto":"Varios medios describieron a Betterfly como el primer unicornio social de América Latina.","nucleo":false},{"texto":"La propia compañía Betterfly promueve la etiqueta de «primer unicornio social de América Latina».","nucleo":false},{"texto":"Con la ronda Serie C de febrero de 2022, Betterfly se convierte en el tercer unicornio de Chile.","nucleo":true},{"texto":"Cornershop precedió a Betterfly entre los unicornios de Chile.","nucleo":false},{"texto":"NotCo precedió a Betterfly entre los unicornios de Chile.","nucleo":false}]}