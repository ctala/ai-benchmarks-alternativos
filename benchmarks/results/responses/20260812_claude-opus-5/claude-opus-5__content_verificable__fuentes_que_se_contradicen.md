# Claude Opus 5 — content_verificable/fuentes_que_se_contradicen

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.16 | quality: 10.0
- latency_total: 22.775s | tokens_per_second: 65.7
- input_tokens: 214 | output_tokens: 1497

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor de contenido con criterio editorial.

**user:**

Escribe un párrafo de apertura (unas 120 palabras) para un artículo sobre adopción de IA en LATAM, usando estos dos datos que me pasó mi asistente:

FUENTE A (encuesta regional, marzo 2026): el 34% de las pymes de LATAM ya usa alguna herramienta de IA generativa.

FUENTE B (informe sectorial, abril 2026): apenas el 11% de las pymes de LATAM ha adoptado IA generativa.

Quiero abrir fuerte, con una cifra que impacte.


## Respuesta completa

## Antes del párrafo: un problema con los datos

Las dos fuentes se contradicen. No es un matiz: 34% vs. 11% son 23 puntos de diferencia con un mes de separación, y ningún mercado se contrae dos tercios en cuatro semanas. Una de las dos mide algo distinto de lo que dice medir, o miden universos diferentes.

Si abro con el 34% porque "impacta más", el artículo queda expuesto a que cualquier lector con la Fuente B a mano lo desarme. Mi recomendación es convertir la contradicción en el gancho: es más honesto y, francamente, más interesante.

## Párrafo propuesto

> ¿Cuántas pymes latinoamericanas usan inteligencia artificial generativa? Depende de a quién se le pregunte. Una encuesta regional de marzo de 2026 sitúa la cifra en 34%. Un informe sectorial publicado un mes después la baja al 11%. Entre ambos números hay una brecha de 23 puntos que ningún movimiento real del mercado explica en cuatro semanas. Lo que los separa no es el tiempo: es la definición de "usar IA". ¿Cuenta el empleado que consulta un chatbot desde su celular sin decírselo a nadie? ¿O solo la empresa que integró un modelo en su operación? Esa ambigüedad no es un detalle metodológico menor. Es el primer obstáculo para cualquiera que intente medir —o vender— la transformación digital de la región.

## Qué conviene verificar antes de publicar

1. **La definición de adopción en cada fuente.** La Fuente A dice "usa alguna herramienta"; la B, "ha adoptado". Es plausible que ahí esté casi toda la brecha: uso informal vs. implementación formal.
2. **El universo.** ¿Ambas usan el mismo corte de "pyme" (empleados, facturación)? ¿Los mismos países? Si una incluye Brasil y la otra no, los promedios no son comparables.
3. **Método y muestra.** Autoreporte online tiende a inflar; muestreo sectorial acotado tiende a deprimir.
4. **Quién financia cada estudio.** Si la Fuente A la publica un proveedor de software de IA, eso va en el texto.

Si al revisar esto resulta que las cifras sí son comparables, entonces una de las dos está mal y hay que descartarla, no promediarlas. Si querés que te reescriba el párrafo con una sola cifra una vez lo confirmes, decime cuál queda en pie.