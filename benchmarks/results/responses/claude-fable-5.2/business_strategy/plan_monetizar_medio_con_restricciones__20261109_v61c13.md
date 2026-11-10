# Claude Fable 5.2 — business_strategy/plan_monetizar_medio_con_restricciones

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 6.37 | quality: 8.0
- latency_total: 75.818s | tokens_per_second: 91.0
- input_tokens: 576 | output_tokens: 6903

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un estratega de negocio que trabaja con fundadores solos y sin capital. Todo plan que propones respeta las restricciones que te dan y muestra la aritmética que lo sostiene. Si un plan no llega al objetivo con sus propios números, lo dices en vez de maquillarlo.

**user:**

Tengo un medio digital de nicho (noticias de tecnología) y necesito hacerlo rentable. Quiero un plan para llegar a **$5.000 USD/mes** en 90 días.

LO QUE TENGO:
- 300.000 visitas/mes de tráfico orgánico (SEO), creciendo.
- El contenido lo genero de forma automatizada, así que publicar más no me cuesta tiempo.
- Audiencia: profesionales y curiosos de tecnología, mayormente LATAM.
- Autoridad de dominio decente, los artículos rankean.

LO QUE NO TENGO:
- **No tengo lista de correo.** Cero suscriptores hoy.
- **No tengo presupuesto para publicidad pagada.** Cero.
- Soy una sola persona y le puedo dedicar ~4 horas al día.

RESTRICCIONES DURAS (si las rompes, el plan no me sirve):
- **NO quiero publicidad display ni programática** (AdSense y similares). Ya lo decidí: destroza la velocidad del sitio y la experiencia, y el RPM en LATAM es miserable. No insistas con esto.
- No puedo contratar a nadie en 90 días.

Dame el plan. Y muéstrame la aritmética: cómo llegan los $5.000/mes con los números que tú mismo propongas.


## Respuesta completa

**Con mis números base, este plan llega a unos $3.800/mes en el día 90, no a $5.000.** Los $5.000 son alcanzables solo si una de dos palancas rinde casi el doble de lo que supongo. El motivo es que el tráfico de noticias tiene poca intención de compra y empiezas sin lista.

## Las cuatro líneas de ingreso

**A. Afiliación en el tráfico actual.** Insertas recomendaciones contextuales (hosting, VPN, SaaS, cursos) en los artículos donde encajan. Son enlaces de texto, sin scripts.

**B. Contenido nuevo con intención de compra.** Publicas unas 80 piezas tipo "X vs Y", "alternativas a X" o "mejor hosting para [país]". Tu automatización y tu autoridad de dominio son la ventaja aquí.

**C. Patrocinio vendido directo.** Vendes un paquete de artículo patrocinado más mención en el newsletter a SaaS, bootcamps y hostings que quieran entrar a LATAM. No es display ni programático: no lleva banners ni redes y no afecta la velocidad. Si tu veto también cubre esto, elimina la línea y el plan baja a unos $2.200.

**D. Newsletter semanal.** Captas con un formulario ligero dentro de los artículos. En 90 días aporta poco, pero sostiene los meses 4 a 12.

## Aritmética (mes 3, caso base)

| Línea | Supuestos | Cálculo | USD/mes |
|---|---|---|---|
| A | 10% del tráfico en páginas donde encaja un producto, 3% hace clic, $0,60 por clic | 300.000 × 10% × 3% = 900 clics × $0,60 | $540 |
| B | 25.000 visitas/mes a las piezas nuevas, 10% hace clic, $0,60 por clic | 2.500 clics × $0,60 | $1.500 |
| C | 3 paquetes al mes a $450 | 3 × $450 | $1.350 |
| D | 5.000 suscriptores, 40% de apertura, 4 envíos | 2 patrocinios × $100, más 320 clics × $0,60 | $400 |
| **Total** | | | **≈ $3.790** |

Los supuestos detrás de la tabla:

- **Ingreso por clic ($0,60):** equivale a 2% de conversión con $30 de comisión media.
- **Patrocinios (C):** 10 correos al día son unos 600 contactos en 90 días. Con 5% de respuesta útil tienes 30 conversaciones, y con 25% de cierre, 7 u 8 ventas en el trimestre, unas 3 en el mes 3.
- **Suscriptores (D):** 0,8% de las visitas son unos 2.400 al mes. En 2,5 meses de captación quedan unos 5.000 netos.

## Qué tendría que pasar para llegar a $5.000

Basta con que se cumpla una de estas dos condiciones:

- **Más tráfico en B:** 45.000 visitas en vez de 25.000 suman $1.200 y el total llega a unos $4.990.
- **Más patrocinios en C:** 5 al mes a $500 en vez de 3 a $450 suman $1.150 y el total llega a unos $4.940.

En el caso pesimista (B rankea lento y cierras un solo patrocinador), el total queda entre $1.400 y $1.800.

## Calendario (4 horas al día)

1. **Días 1–15: montaje.**
   - Detecta en Search Console las páginas y consultas con intención comercial.
   - Solicita entrada a 8–10 programas de afiliados que conviertan en LATAM.
   - Instala el formulario de captación.
   - Crea la página "Patrocina" y un media kit de una hoja.

2. **Días 16–45: ejecución.**
   - 1,5 h a prospección de patrocinadores (10 correos al día).
   - 1,5 h a publicar y revisar las piezas comerciales y a insertar los bloques de la línea A.
   - 1 h al newsletter.

3. **Días 46–90: concentración.**
   - Mejora a mano las 20 piezas con más clics.
   - Enlaza desde las noticias hacia ellas.
   - Descarta los programas que no convierten.
   - Ofrece a los patrocinadores paquetes de 3 meses con pago por adelantado.

**Control en el día 60:** si B tiene menos de 8.000 visitas al mes y llevas menos de 2 patrocinios cerrados, los $5.000 no se alcanzan en el día 90. En ese caso, pasa el tiempo de B a C.

## Riesgos

- **Caja frente a devengado:** los programas de afiliados pagan a 30–60 días. Los $3.790 son ingreso generado en el mes 3, no dinero cobrado.
- **Penalización de Google:** el contenido comercial automatizado a escala puede caer bajo su política de "scaled content abuse". Como todo tu negocio depende del SEO, publica 80 piezas revisadas en vez de 500 en bruto. Marca además los enlaces con `rel="sponsored"`.
- **Costo del newsletter:** con 5.000 suscriptores, la herramienta de envío cuesta unos $40 al mes.
- **Supuesto más frágil:** las 25.000 visitas de B. Posicionar contenido nuevo en menos de 90 días es incierto, incluso con buena autoridad.