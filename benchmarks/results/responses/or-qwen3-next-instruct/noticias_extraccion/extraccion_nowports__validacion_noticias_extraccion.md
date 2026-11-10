# Qwen 3-Next 80B Instruct — noticias_extraccion/extraccion_nowports

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.34 | quality: 8.55
- latency_total: 2.462s | tokens_per_second: 182.8
- input_tokens: 1130 | output_tokens: 450

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
Nowports se convierte en el primer unicornio logístico de Hispanoamérica

Monterrey — Nowports, la empresa mexicana de logística y agenciamiento de carga, cerró en mayo de 2022 una ronda Serie C de US$150 millones que la valora en US$1.100 millones. La ronda fue liderada por el SoftBank Latin America Fund y contó con la participación de Tencent.

Con esta operación, la compañía regiomontana se convierte en el primer unicornio de tecnología logística de Hispanoamérica.

El agenciamiento de carga es uno de los eslabones menos digitalizados del comercio internacional. Para mover un contenedor de un puerto asiático a una bodega en México intervienen navieras, agentes aduanales, transportistas terrestres, almacenes y bancos, y buena parte de esa coordinación todavía se hace por correo electrónico y hojas de cálculo. Las empresas como Nowports ofrecen una plataforma que centraliza el seguimiento de la carga, los documentos y los pagos, y en algunos casos financian a los importadores mientras la mercancía está en tránsito.

La compañía fue fundada en 2018 por Maximiliano Casal y Alfonso de los Ríos.

El financiamiento de inventario es una parte importante del negocio. Muchos importadores pequeños deben pagar a sus proveedores antes de recibir la mercancía y venderla, y esa brecha de caja limita cuánto pueden comprar. Prestarles contra la carga en tránsito permite a la plataforma cobrar intereses además de las tarifas logísticas.

Según la empresa, los nuevos recursos se usarán para ampliar sus servicios financieros en América Latina y para abrir oficinas en Brasil, México y Chile.

La relocalización de cadenas de suministro hacia América del Norte, conocida como nearshoring, ha puesto a Monterrey en el centro del interés de inversionistas y fabricantes, y las empresas de logística de la ciudad buscan aprovechar ese impulso.

El sector tiene una dificultad estructural: el negocio logístico depende de ciclos de comercio internacional que nadie controla. Cuando las tarifas de los fletes marítimos se dispararon durante la pandemia, las empresas de agenciamiento de carga facturaron más que nunca; cuando las tarifas cayeron, los ingresos se contrajeron con la misma rapidez. Los inversionistas valoran por eso a las compañías que logran ingresos recurrentes por software o por servicios financieros, menos expuestos a los vaivenes del precio del flete y más fáciles de proyectar en el tiempo. Esa es también la razón por la que muchas empresas del rubro intentan venderse como compañías de tecnología y no como agentes de carga tradicionales.

Pocos meses antes, en diciembre de 2021, Nowports había cerrado una Serie B de US$60 millones liderada por Tiger Global.



## Respuesta completa

{
  "claims": [
    {
      "texto": "Nowports cerró en mayo de 2022 una ronda Serie C de US$150 millones.",
      "nucleo": true
    },
    {
      "texto": "Nowports fue valorada en US$1.100 millones tras la ronda Serie C de mayo de 2022.",
      "nucleo": true
    },
    {
      "texto": "La ronda Serie C de mayo de 2022 de Nowports fue liderada por el SoftBank Latin America Fund.",
      "nucleo": true
    },
    {
      "texto": "La ronda Serie C de mayo de 2022 de Nowports contó con la participación de Tencent.",
      "nucleo": true
    },
    {
      "texto": "Nowports se convirtió en el primer unicornio de tecnología logística de Hispanoamérica tras la ronda Serie C de mayo de 2022.",
      "nucleo": true
    },
    {
      "texto": "Nowports fue fundada en 2018 por Maximiliano Casal y Alfonso de los Ríos.",
      "nucleo": true
    },
    {
      "texto": "Según la empresa, los nuevos recursos de la ronda Serie C se usarán para ampliar sus servicios financieros en América Latina.",
      "nucleo": false
    },
    {
      "texto": "Según la empresa, los nuevos recursos de la ronda Serie C se usarán para abrir oficinas en Brasil, México y Chile.",
      "nucleo": false
    },
    {
      "texto": "Nowports había cerrado una Serie B de US$60 millones en diciembre de 2021.",
      "nucleo": true
    },
    {
      "texto": "La Serie B de diciembre de 2021 de Nowports fue liderada por Tiger Global.",
      "nucleo": true
    }
  ]
}