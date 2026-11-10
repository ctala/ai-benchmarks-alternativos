# Tencent Hy4 — noticias_verificacion/bloquea_betterfly_muro_de_pago

- model_id: `tencent/hy4`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 21.042s | tokens_per_second: 111.2
- input_tokens: 698 | output_tokens: 2339

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el verificador de datos de una redacción. Recibes una FUENTE (en español o en inglés) y una lista numerada de AFIRMACIONES que alguien quiere publicar citándola. Decide, para CADA afirmación, si la fuente la respalda.

Responde SOLO con JSON válido, con un veredicto por cada afirmación y el mismo id:
{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}]}

RESPALDADO: la fuente afirma lo mismo, aunque con otras palabras, en otro idioma o con la cifra escrita en otro formato («US$1.500 millones» = «$1.5 billion»).
NO_RESPALDADO: la fuente no dice nada sobre eso, o lo que dice no alcanza para afirmarlo. La AUSENCIA nunca es contradicción.
CONTRADICE: la fuente afirma algo incompatible: otra cifra, otra fecha, otra entidad haciendo la acción (quién lideró, quién paga, quién confirma), o lo opuesto.

Reglas:
- Usa SOLO la fuente. No uses lo que sabes del mundo, aunque estés seguro.
- Si la fuente está truncada (muro de pago, «Suscríbete para seguir leyendo»), lo que no aparece en el fragmento es NO_RESPALDADO, nunca CONTRADICE.
- La atribución es parte del dato: «según Reuters» no es «la empresa confirmó».
- Lee la fuente completa, hasta el último párrafo, antes de decidir.
- Devuelve exactamente un veredicto por afirmación: ni menos, ni repetidos.

**user:**

FUENTE:
Betterfly alcanza valoración de US$1.000 millones con una Serie C de US$125 millones

Santiago — Betterfly, la insurtech chilena que combina seguros de vida con una aplicación de hábitos saludables, levantó en febrero de 2022 una ronda Serie C de US$125 millones que la valora en US$1.000 millones.

La ronda fue liderada por Glade Brook Capital Partners. Entraron como nuevos inversionistas Greycroft, Lightrock y Mundi Ventures, y también participaron QED Investors, que había liderado la Serie A de la compañía, y DST Global Partners, que había encabezado la Serie B.

…

Suscríbete para seguir leyendo. Este contenido es exclusivo para suscriptores.

AFIRMACIONES A VERIFICAR (6):
1. Betterfly levantó US$125 millones en una Serie C.
2. Glade Brook Capital Partners lideró la ronda.
3. QED Investors lideró la Serie C de Betterfly.
4. Betterfly fue fundada en 2018 por Eduardo della Maggiora.
5. Betterfly abrirá operaciones en México en 2022.
6. Betterfly es el tercer unicornio de Chile.


## Respuesta completa

{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}, {"id": 2, "veredicto": "RESPALDADO"}, {"id": 3, "veredicto": "CONTRADICE"}, {"id": 4, "veredicto": "NO_RESPALDADO"}, {"id": 5, "veredicto": "NO_RESPALDADO"}, {"id": 6, "veredicto": "NO_RESPALDADO"}]}