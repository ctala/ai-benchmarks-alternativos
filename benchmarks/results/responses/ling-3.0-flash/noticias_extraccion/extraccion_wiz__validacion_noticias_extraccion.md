# Ling 3.0 Flash — noticias_extraccion/extraccion_wiz

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.2 | quality: 8.4
- latency_total: 20.608s | tokens_per_second: 120.8
- input_tokens: 1078 | output_tokens: 2489

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
      "texto": "Wiz es una empresa de ciberseguridad con sede en Nueva York.",
      "nucleo": true
    },
    {
      "texto": "La compra es la más grande en la historia de Google en sus 26 años de existencia.",
      "nucleo": true
    },
    {
      "texto": "Es el mayor acuerdo íntegramente en efectivo que Google ha firmado jamás.",
      "nucleo": true
    },
    {
      "texto": "Según informes, Google ofreció aproximadamente 23.000 millones de dólares por Wiz el año anterior.",
      "nucleo": true
    },
    {
      "texto": "Wiz rechazó la oferta anterior de Google de aproximadamente 23.000 millones de dólares.",
      "nucleo": true
    },
    {
      "texto": "Wiz declaró en ese momento que perseguiría la salida a bolsa (IPO) que tenía planificada en lugar de aceptar la oferta.",
      "nucleo": true
    },
    {
      "texto": "Wiz desarrolla software que escanea la infraestructura que las empresas ejecutan en nubes públicas y detecta errores de configuración, credenciales expuestas y cargas de trabajo vulnerables.",
      "nucleo": true
    },
    {
      "texto": "Según ambas empresas, los productos de Wiz seguirán funcionando en los principales proveedores de nube, incluidos Amazon Web Services, Microsoft Azure y Oracle Cloud, y no solo en la plataforma de Google.",
      "nucleo": true
    },
    {
      "texto": "La adquisición aún necesita aprobación regulatoria.",
      "nucleo": true
    },
    {
      "texto": "Las empresas indicaron que esperan que la operación se cierre en 2026.",
      "nucleo": true
    },
    {
      "texto": "Analistas esperan que las autoridades antitrust de Estados Unidos y Europa examinen de cerca la operación, dada la posición de Google en otros mercados y la creciente concentración entre los grandes proveedores de ciberseguridad en la nube.",
      "nucleo": true
    },
    {
      "texto": "Wiz fue fundada en 2020 por Assaf Rappaport, Ami Luttwak, Yinon Costica y Roy Reznik.",
      "nucleo": true
    },
    {
      "texto": "Los fundadores habían construido previamente una empresa de seguridad que vendieron a Microsoft.",
      "nucleo": true
    },
    {
      "texto": "Los fundadores dirigen la empresa desde Nueva York y Tel Aviv.",
      "nucleo": true
    },
    {
      "texto": "Según Reuters, Google acordó pagar a Wiz una tarifa de terminación de 3.200 millones de dólares si la adquisición no se concreta.",
      "nucleo": true
    }
  ]
}
```