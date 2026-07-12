# Claude Opus 4.8 (suscripción) — business_audit/roadmap_restriccion_capacidad

- model_id: `claude-opus-4-8`
- success: True  | final: 5.03 | quality: 5.74
- latency_total: 63.645s | tokens_per_second: 50.4
- input_tokens: 4 | output_tokens: 3206

## Respuesta completa

## Primero la matemática, porque ahí se acaba la discusión

- 4h/día × 5 días = **20h/semana**
- 8 semanas = **160h teóricas**
- Descuento realista (imprevistos, soporte que se desborda, un día malo por semana): **~120-130h reales de construcción en el trimestre**

Ahora traduzco tus estimaciones. Cuando dices "3 meses a tiempo completo" o "1 semana", estás pensando en semanas de 40h ideales. En tu capacidad real cada "semana ideal" son **2 semanas de calendario**.

| | Tu estimación | Horas ideales | Semanas reales tuyas | ¿Cabe en 8 semanas? |
|---|---|---|---|---|
| A) Rewrite | 3 meses FT | ~480h | **~24 semanas** | No. Es 3x tu trimestre completo |
| B) Alta rota | 1 semana | ~40h | **~2 semanas** | Sí |
| C) Panel | 3 semanas | ~120h | **~6 semanas** | Solo si matas A. Y depende de A |
| D) 10 videos | 2 semanas | ~80h | **~4 semanas** | Sí |

A no es una iniciativa del trimestre. A es **dos trimestres de tu vida**, y eso asumiendo que no se pasa (los rewrites se pasan 2x, siempre). Si arrancas A, tu trimestre entero es A a medias, sin nada en producción y con el 60% de fuga intacto.

Y C está encadenada a A, así que C también está muerta por dependencia.

## El veredicto

**B es lo único que no está en discusión.** Estás perdiendo 6 de cada 10 personas en el paso 2. Todo lo demás —contenido, panel, velocidad— es echar agua en un balde agujereado. Si arreglas la fuga a la mitad (60% → 30%), con el mismo tráfico tienes **~1.75x más gente activada**. Nada más en tu lista se acerca a ese multiplicador por 2 semanas de trabajo.

**D va después de B**, no antes. Traer tráfico a un funnel que pierde el 60% es pagar por ese desperdicio.

**A la congelas.** "Velocidad y todo lo futuro" no es un problema, es una sensación. Te propongo el reemplazo abajo.

**C la desacoplas.** Casi seguro no depende de A de verdad; depende de que *tú decidiste* hacerla después de A.

## Tu trimestre

**Semanas 1-2 — B (arreglar el alta)**
- Días 1-3: **no toques código todavía.** Instrumenta el paso 2 y habla con 5-8 personas que se cayeron. El 60% tiene una causa concreta y probablemente no es la que crees.
- Días 4-10: arreglar. Envío incremental.

**Semana 3 — Medir B + segundo pase**
Ver el número moverse. Si sigue en 55%, atacaste el síntoma equivocado: vuelve a la data. Este es el ciclo que más plata te va a dar en todo el trimestre.

Bonus: parte de tus 2h/día de soporte probablemente **es gente atascada en ese paso 2**. Etiqueta tus tickets por categoría durante estas 3 semanas. Si B te libera 30 min/día de soporte, acabas de recuperar 20h de capacidad para el resto del trimestre. Esa es la única forma de comprar tiempo que tienes.

**Semanas 4-7 — D (contenido)**
Ahora sí: 10 videos apuntando a un funnel que retiene. Graba en tandas (2 días de grabación, no 10 sesiones). Y ojo: si en la semana 3 la data te dice que B necesita otro pase, **B gana**. Bajas a 6 videos y no pasa nada.

**Semana 8 — Buffer y decisión**
No planifiques trabajo nuevo aquí. Se va a llenar sola. Lo que sobre, lo usas para escribir el caso de A con datos reales.

## Las dos preguntas que te tienes que contestar antes de tocar A y C

**Sobre A:** escribe los 3 dolores concretos que te hacen querer el rewrite. No "es lento", sino "el endpoint X tarda 4s", "agregar una feature me toma 3 semanas cuando debería tomar 1". Después mira cada uno y pregúntate si se arregla *en el stack actual* en días. En mi experiencia, 2 de los 3 sí. Un rewrite de 6 meses en un founder solo a 4h/día es la forma más común de matar un negocio que funcionaba. Reevalúalo en 2 trimestres, con dolores medidos, no con intuición.

**Sobre C:** ¿qué métrica quieren ver tus clientes realmente? Si son 3 números, mándales un **email semanal automatizado con esos 3 números**. Eso son 2 días, no 6 semanas. Si nadie abre el email, acabas de ahorrarte un panel entero. Si lo abren todos y te piden más, ya tienes el caso para construirlo — y con la especificación regalada.

---

**Resumen:** B → medir → D. A y C fuera del trimestre, y C reemplazada por su versión de 2 días. Es lo único que cabe en 120h reales, y da la casualidad de que también es lo que más impacto tiene.