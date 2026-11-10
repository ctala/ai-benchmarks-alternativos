# Claude Fable 5.2 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 5.1 | quality: 6.0
- latency_total: 42.126s | tokens_per_second: 83.9
- input_tokens: 288 | output_tokens: 3533

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

# Teardown: comunidad de pago sobre automatización

**En corto:** probablemente facturan entre 35.000 y 95.000 $/mes brutos, con un escenario central cercano a 60.000 $. La salud del negocio no se puede determinar con estos datos. La mejor inversión antes de decidir cómo competir es pagar un mes de membresía (39 $) y mirar dentro.

## 1. Facturación

El único cálculo firme es el techo: 2.400 × 39 $ = **93.600 $/mes** (unos 1,12 M $/año). Solo se cumple si los 2.400 pagan precio completo hoy, y no sé si es así. La cifra podría incluir miembros gratuitos, altas acumuladas, precios antiguos más bajos o pruebas gratis.

| Escenario | Supuesto (mío, no dato) | Ingreso mensual | Ingreso anual |
|---|---|---|---|
| Conservador | 50 % paga, precio efectivo 29 $ | ~34.800 $ | ~418.000 $ |
| Central | 75 % paga, precio efectivo 34 $ | ~61.200 $ | ~734.000 $ |
| Techo | 100 % paga 39 $ | 93.600 $ | ~1,12 M $ |

**Certeza: baja-media.** El rango es fiable como orden de magnitud, pero el punto central es una conjetura. Además, son ingresos brutos, sin comisiones ni otros ingresos que no se ven (afiliados, consultoría, patrocinios).

## 2. Salud del negocio

No hay datos sobre lo que la determina: bajas mensuales, tendencia de crecimiento, coste de adquisición y actividad real dentro. Solo puedo inferir esto:

- **Necesitan muchas altas para no encoger (certeza media).** Con bajas del 5–10 % mensual, que es mi referencia general para membresías mensuales y no un dato suyo, tendrían que captar 120–240 miembros nuevos al mes.
- **La cifra de miembros no cuadra solo con su audiencia (certeza media).** 2.400 sobre 60.000 seguidores es un 4 %, alto para un producto de pago. O tienen otros canales (anuncios, email, afiliados), o la cifra está inflada, o la audiencia es muy afín.
- **Dependen del fundador (certeza media).** Si la captación es su cuenta personal, hay riesgo de persona clave y de saturar la audiencia.
- **Los 12 cursos pueden ser fachada (certeza baja).** Si varios están incompletos, la promesa es amplitud más que resultado, lo que suele traer bajas tras consumir lo útil.
- **Los 3 posts por semana no dicen nada.** Es el feed público y no refleja la actividad interna.

## 3. Cómo reducir la incertidumbre

1. **Entra un mes.** Verás la actividad real, los cursos terminados, el onboarding y las ofertas internas.
2. **Llega hasta el checkout.** Ahí suelen aparecer el plan anual, los cupones o la prueba gratis.
3. **Anota el contador de miembros cada semana** durante 6–8 semanas para ver el crecimiento neto.
4. **Mira el historial de la página en Wayback Machine** para ver precios y cifras anteriores.
5. **Busca sus anuncios en las bibliotecas públicas** (Meta, por ejemplo) para saber si pagan por captar.
6. **Revisa el engagement del fundador.** 60.000 seguidores con poca interacción valen mucho menos.

## 4. Cómo competir

Estas son hipótesis a validar con lo anterior. Tampoco conozco tu audiencia ni tu producto, así que tómalas como opciones:

- **Si su contenido es ancho y poco terminado:** compite con una promesa estrecha y completa, con un resultado concreto para un perfil concreto (por ejemplo, automatización para agencias o para e-commerce) en vez de "automatización" en general.
- **Si dentro hay poca actividad:** diferénciate con implementación, como cohortes, revisiones en vivo y plantillas listas. Eso justifica un precio igual o mayor; no competiría bajando el precio.
- **Si no tienen plan anual:** ofrécelo tú desde el inicio, porque reduce bajas y te da caja.
- **Si dependen de una sola red:** capta donde no están (SEO, YouTube, alianzas con herramientas de automatización, email).
- **Si todo sale sólido** (comunidad activa, cursos completos, crecimiento sostenido): no los ataques de frente. Elige un subnicho que atiendan mal.

Si me cuentas qué tienes tú (audiencia, producto, precio), afino la estrategia.