# GPT-6.1 Terra — business_audit/teardown_competidor_sin_inventar

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 5.67 | quality: 6.0
- latency_total: 22.907s | tokens_per_second: 68.9
- input_tokens: 175 | output_tokens: 1578

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

## Resumen ejecutivo

- **Facturación:** no se puede determinar con lo visible. Si los 2.400 miembros fueran de pago y todos abonaran $39 ese mes, serían **$93.600/mes en cobros brutos por suscripciones**. Es un escenario, no una estimación fiable.
- **Salud:** desconocida. Faltan retención, adquisición, costes y proporción de miembros que paga. **Certeza alta** en que esos datos son necesarios; **baja** sobre cualquier diagnóstico actual.
- **Cómo competir:** no intentaría ganar copiando sus 12 cursos o publicando más. Probaría una propuesta para un segmento concreto, con un resultado práctico y acompañamiento medible. Es una **hipótesis estratégica**, no una debilidad demostrada del rival.

## 1. Cuánto podría facturar

### Lo observado

La portada muestra **2.400 miembros** y un precio de **$39/mes**. No sabemos si el contador incluye miembros gratuitos, inactivos o todos los clientes de pago. Tampoco vemos descuentos ni planes anuales.

### Escenarios ilustrativos

Supuestos comunes: los 2.400 representan el universo relevante de miembros, cada pagador abona $39 ese mes y no hay descuentos ni devoluciones. Los porcentajes son ejemplos, **no probabilidades**.

| Miembros que pagan | Pagadores | Cobros brutos mensuales | Anualización al mismo ritmo |
|---|---:|---:|---:|
| 25% | 600 | $23.400 | $280.800 |
| 50% | 1.200 | $46.800 | $561.600 |
| 100% | 2.400 | $93.600 | $1.123.200 |

**Certeza:** alta en la aritmética; baja en que cualquiera de los escenarios refleje la realidad.

La última columna es una *anualización*, no lo que hayan facturado en el último año ni una previsión. Además, estos importes excluyen comisiones, impuestos, devoluciones y costes. Solo modelan suscripciones: podrían tener otros ingresos que no vemos, por lo que $93.600 tampoco es un techo demostrado para el negocio total.

## 2. Qué tan sano es el negocio

**No se puede concluir si es sano o no.** Las señales visibles describen alcance y actividad, pero no economía ni satisfacción.

| Señal observada | Qué permite inferir | Qué no demuestra |
|---|---|---|
| 2.400 miembros mostrados | Existe una base visible. **Certeza alta.** | Cuántos pagan, participan o permanecen. |
| 60.000 seguidores del fundador | Tiene un canal potencial de distribución. **Certeza media:** no conocemos su alcance efectivo. | Conversiones, ingresos ni independencia del fundador. |
| 3 posts públicos por semana | Hay actividad pública regular. **Certeza alta.** | Calidad, engagement o actividad dentro de la comunidad. |
| 12 cursos listados | Hay una oferta amplia en catálogo. **Certeza alta.** | Cuántos están terminados, se usan o generan resultados. |

Para evaluar la salud pediría, en este orden:

1. **Pagadores activos y bajas mensuales:** saber cuántos compran y cuánto tiempo permanecen.
2. **Altas por canal y coste de adquisición:** distinguir crecimiento sostenible de dependencia del alcance gratuito del fundador.
3. **Margen después de plataforma, soporte, contenido e impuestos aplicables.**
4. **Participación y resultados:** consumo de cursos, respuestas en comunidad y logros de los miembros.

Una posible vulnerabilidad es la **dependencia del fundador** para atraer clientes; otra es que el catálogo no garantice implementación. Ambas son hipótesis con **certeza baja** hasta observar cómo operan y hablar con clientes.

## 3. Cómo competir

### Posicionamiento a probar

Elegiría un público y un resultado más concretos que «automatización para todos». Por ejemplo: *«Ayudamos a [tipo de profesional] a implementar [proceso específico] en 30 días»*.

La diferencia no sería tener más contenido, sino combinar:

- Una ruta corta de implementación, en lugar de un catálogo abierto.
- Plantillas y casos adaptados al segmento elegido.
- Revisión o soporte con una frecuencia definida.
- Un resultado verificable acordado al inicio.

**Certeza:** media en que la especialización puede facilitar la diferenciación; baja en que este competidor no ofrezca ya algo equivalente, porque no vemos su producto completo.

### Plan de validación de 30 días

1. **Investiga:** entrevista a 10–15 personas del público objetivo, incluidos clientes actuales o anteriores si puedes encontrarlos. Pregunta qué intentaron automatizar, dónde se atascaron y por qué pagarían o cancelarían.
2. **Observa el producto:** revisa testimonios y condiciones públicas; si es viable, compra un mes para evaluar onboarding, actividad, soporte y profundidad de los cursos.
3. **Prueba una oferta:** crea una página con un resultado concreto y busca conversaciones o reservas de pago, no solo clics.
4. **Ejecuta un piloto pequeño:** mide cuántos participantes llegan al resultado, cuánto soporte requieren y cuántos pagarían por continuar.

No bajaría de $39 por reflejo: primero comprobaría qué valor percibe el segmento y cuánto cuesta atenderlo. Tampoco construiría una biblioteca de 12 cursos antes de demostrar que una solución concreta se usa y se paga.