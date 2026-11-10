# Gemini 3.8 Flash — noticias_extraccion/extraccion_wiz

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.5 | quality: 9.85
- latency_total: 13.683s | tokens_per_second: 157.1
- input_tokens: 963 | output_tokens: 2149

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
Google agrees to buy Wiz for $32 billion in its largest deal ever

Google has agreed to acquire Wiz, the New York-based cloud security company, for $32 billion in cash. The purchase is the largest in Google's 26-year history and the biggest all-cash deal the company has ever signed.

Wiz builds software that scans the infrastructure companies run on public clouds and flags misconfigurations, exposed credentials and vulnerable workloads. Its pitch is that security teams no longer need to install agents on every server: the platform connects to the cloud account and builds a map of everything that is running.

The price is well above the roughly $23 billion that Google reportedly offered for Wiz the previous year. Wiz turned down that offer and said at the time that it would pursue the initial public offering it had been planning instead.

Cloud security has become one of the most contested categories in enterprise software. As companies moved workloads to several clouds at once, the number of permissions, keys and connections to watch grew faster than the teams in charge of watching them. Large buyers increasingly prefer a single platform over a patchwork of tools, which favors the vendors that can cover the most ground and explains the premiums being paid for leaders in the category.

Once the deal closes, Wiz will join Google Cloud. Both companies said Wiz's products will keep working across the major cloud providers, including Amazon Web Services, Microsoft Azure and Oracle Cloud, and not only on Google's own platform. That commitment matters to customers, many of whom use Wiz precisely because it is not tied to any single provider.

The acquisition still needs regulatory approval, and the companies said they expect it to close in 2026. Analysts expect antitrust authorities in the United States and Europe to look closely at the deal, given Google's position in other markets and the growing concentration among large cloud security vendors.

Wiz was founded in 2020 by Assaf Rappaport, Ami Luttwak, Yinon Costica and Roy Reznik, who had previously built a security company that they sold to Microsoft. The founders lead the company from New York and Tel Aviv.

For customers, large acquisitions in security bring a familiar worry. Products that were neutral can drift toward the acquirer's own platform over time, prices can change once the buyer integrates its sales teams, and roadmaps can slow down while two organizations merge. Buyers typically negotiate longer contracts and price protections when they suspect that a vendor is about to change hands, and procurement teams watch closely for signs that support quality is slipping during the integration.

The deal also carries protection for Wiz if regulators get in the way. According to Reuters, Google agreed to pay Wiz a termination fee of $3.2 billion if the acquisition falls through.



## Respuesta completa

```json
{
  "claims": [
    {
      "texto": "Google acordó adquirir Wiz por 32.000 millones de dólares en efectivo.",
      "nucleo": true
    },
    {
      "texto": "Wiz es una empresa de seguridad en la nube con sede en Nueva York.",
      "nucleo": false
    },
    {
      "texto": "La compra de Wiz es la adquisición más grande en los 26 años de historia de Google.",
      "nucleo": true
    },
    {
      "texto": "La adquisición de Wiz es el mayor acuerdo totalmente en efectivo que Google ha firmado en su historia.",
      "nucleo": true
    },
    {
      "texto": "Wiz desarrolla software que escanea la infraestructura de empresas en nubes públicas y detecta configuraciones erróneas, credenciales expuestas y cargas de trabajo vulnerables.",
      "nucleo": false
    },
    {
      "texto": "La plataforma de Wiz se conecta a cuentas en la nube y crea un mapa de ejecución sin requerir la instalación de agentes en cada servidor.",
      "nucleo": false
    },
    {
      "texto": "Google ofreció aproximadamente 23.000 millones de dólares por Wiz el año anterior.",
      "nucleo": false
    },
    {
      "texto": "Wiz rechazó la oferta previa de compra de Google de aproximadamente 23.000 millones de dólares.",
      "nucleo": false
    },
    {
      "texto": "Wiz declaró en su momento que buscaría llevar a cabo una oferta pública inicial (OPI) en lugar de venderse a Google.",
      "nucleo": false
    },
    {
      "texto": "Una vez cerrada la transacción, Wiz se integrará en Google Cloud.",
      "nucleo": true
    },
    {
      "texto": "Google y Wiz afirmaron que los productos de Wiz seguirán funcionando en los principales proveedores de nube, incluidos Amazon Web Services, Microsoft Azure y Oracle Cloud, y no solo en la plataforma de Google.",
      "nucleo": true
    },
    {
      "texto": "La adquisición de Wiz por parte de Google aún requiere aprobación regulatoria.",
      "nucleo": true
    },
    {
      "texto": "Google y Wiz señalaron que esperan cerrar la adquisición en 2026.",
      "nucleo": true
    },
    {
      "texto": "Wiz fue fundada en 2020 por Assaf Rappaport, Ami Luttwak, Yinon Costica y Roy Reznik.",
      "nucleo": false
    },
    {
      "texto": "Los fundadores de Wiz crearon previamente una empresa de seguridad que vendieron a Microsoft.",
      "nucleo": false
    },
    {
      "texto": "Los fundadores de Wiz dirigen la empresa desde Nueva York y Tel Aviv.",
      "nucleo": false
    },
    {
      "texto": "Según Reuters, Google acordó pagar a Wiz una tarifa de rescisión de 3.200 millones de dólares si la adquisición se frustra.",
      "nucleo": true
    }
  ]
}
```