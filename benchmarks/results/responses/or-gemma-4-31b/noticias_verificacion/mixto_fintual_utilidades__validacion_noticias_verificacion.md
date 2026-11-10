# Gemma 4 31B — noticias_verificacion/mixto_fintual_utilidades

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.598s | tokens_per_second: 95.1
- input_tokens: 1063 | output_tokens: 152

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
Fintual levanta US$39 millones en una ronda liderada por Sequoia Capital

Santiago — Fintual, la administradora de fondos chilena que permite invertir desde una aplicación, cerró en noviembre de 2021 una ronda Serie B de US$39 millones liderada por Sequoia Capital. También participaron ALLVP y Kaszek, que ya eran inversionistas desde la Serie A.

Es la primera inversión de Sequoia en Chile y, según la prensa local, la tercera del fondo en una empresa latinoamericana, después de Rappi y Nubank.

Fintual nació con una idea concreta: que una persona sin conocimientos financieros pueda invertir en fondos diversificados con montos pequeños y comisiones bajas, sin pasar por un ejecutivo. En Chile, el ahorro voluntario para la jubilación es un mercado relevante porque las pensiones del sistema obligatorio suelen quedar por debajo de lo que las personas esperan, y eso empuja a muchos trabajadores a buscar alternativas.

La compañía fue fundada en 2016 por Pedro Pineda, Agustín Feuerhake, Alfonso Valdés y Pablo Mansilla. Opera en Chile y en México, donde lanzó su servicio en 2020.

Según la empresa, los recursos se destinarán principalmente a acelerar su operación en México, aunque también seguirá creciendo en Chile.

Unos meses antes, Fintual había levantado cerca de US$15 millones en una Serie A liderada por Kaszek.

Las plataformas de inversión digital compiten con bancos y administradoras tradicionales que han lanzado sus propias aplicaciones, y con corredoras que ofrecen acciones sin comisión. El costo de adquirir clientes es alto y la rentabilidad depende de acumular un volumen grande de activos administrados, porque las comisiones, por diseño, son bajas.

Para los inversionistas de riesgo, el atractivo del modelo está en su escala potencial: una vez que la plataforma funciona en un país, sumar clientes cuesta poco y cada peso administrado genera ingresos durante años. El riesgo está en que la regulación y la cultura de ahorro cambian de un país a otro, y lo que funcionó en Chile no necesariamente se replica en México.

Los reguladores también observan de cerca a estas plataformas. Las administradoras de fondos deben cumplir reglas sobre cómo invierten el dinero de sus clientes, cómo informan las comisiones y cómo protegen los activos ante una eventual quiebra de la propia administradora. Para las empresas nuevas, cumplir esas exigencias desde el inicio es costoso, pero también es lo que les permite competir en confianza con instituciones que llevan décadas en el mercado y que tienen marcas reconocidas por varias generaciones de ahorrantes.

La ronda dejó también una meta explícita: alcanzar la rentabilidad. Según Diario Financiero, la empresa reportó utilidades por primera vez en el primer semestre de 2024.

AFIRMACIONES A VERIFICAR (5):
1. Sequoia Capital lideró la Serie B de Fintual, por US$39 millones.
2. Es la primera inversión de Sequoia en Chile.
3. ALLVP y Kaszek ya eran inversionistas de Fintual desde la Serie A.
4. Fintual planea salir a bolsa en Santiago el próximo año.
5. Según Diario Financiero, Fintual reportó utilidades por primera vez en el primer semestre de 2024.


## Respuesta completa

```json
{
  "veredictos": [
    {
      "id": 1,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 2,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 3,
      "veredicto": "RESPALDADO"
    },
    {
      "id": 4,
      "veredicto": "NO_RESPALDADO"
    },
    {
      "id": 5,
      "veredicto": "RESPALDADO"
    }
  ]
}
```