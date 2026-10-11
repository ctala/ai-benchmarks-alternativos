# GPT-6 Luna — business_audit/teardown_competidor_sin_inventar

- model_id: `openai/gpt-6-luna`
- success: True  | final: 4.85 | quality: 4.0
- latency_total: 15.466s | tokens_per_second: 113.1
- input_tokens: 175 | output_tokens: 1749

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

# Teardown competitivo

## Lo que sabemos — certeza alta

- Ofrecen una comunidad de pago sobre automatización en una plataforma de membresía.
- La portada muestra **2.400 miembros**.
- El precio visible es **$39/mes**; no sabemos si hay otros planes o descuentos.
- Publican **3 posts por semana** en el feed público.
- El fundador tiene **60.000 seguidores** en una red social.
- Hay **12 cursos listados**, pero no sabemos cuánto contenido está terminado ni cuánto se consume.

## Cuánto podrían facturar

La cifra depende de qué signifique “2.400 miembros”: personas registradas, miembros actuales o suscriptores de pago. No se puede deducir cuál es el caso solo con la página pública.

**Si los 2.400 fueran todos suscriptores activos a $39/mes:**

- **MRR bruto:** $93.600
- **Run rate anual bruto:** $1.123.200

Eso es un techo aritmético bajo esos supuestos, no una estimación confirmada de ingresos. No descuenta descuentos, impuestos, devoluciones, comisiones de plataforma ni bajas.

| Proporción de los 2.400 que paga $39/mes | Suscriptores estimados | MRR bruto | Run rate anual bruto |
|---:|---:|---:|---:|
| 10% | 240 | $9.360 | $112.320 |
| 25% | 600 | $23.400 | $280.800 |
| 50% | 1.200 | $46.800 | $561.600 |
| 100% | 2.400 | $93.600 | $1.123.200 |

**Inferencia — certeza baja:** el rango real podría estar muy por debajo del escenario del 100% si el contador incluye usuarios gratuitos, antiguos o no activos. Tampoco sabemos cuántos pagan anual o con descuento; en ese caso, multiplicar el contador por $39 sobreestimaría los ingresos.

## ¿Qué tan sano parece el negocio?

**Veredicto provisional: tiene señales de distribución y actividad, pero no hay datos suficientes para evaluar su salud económica. Certeza baja.**

**Señales favorables:**
- Los 60.000 seguidores podrían ser una fuente de adquisición de bajo coste, si la audiencia es relevante y convierte.
- Tres publicaciones semanales sugieren una cadencia de actividad visible.
- Los 12 cursos listados apuntan a una oferta con varios activos educativos, aunque no prueban que estén completos o que aporten valor.

**Lo que no sabemos —y que determina la salud real:**
- Miembros de pago activos y evolución mensual.
- Cancelaciones, retención y antigüedad media de los miembros.
- Conversión desde seguidores a clientes y coste de adquisición.
- Uso de la comunidad y de los cursos, satisfacción y reembolsos.
- Ingresos netos, costes operativos y dependencia del fundador.

Un negocio de membresía puede mostrar muchos miembros y aun así tener alta rotación; también puede tener menos miembros y ser rentable si retiene bien y opera con pocos costes. Las señales públicas no permiten distinguir esos casos.

## Cómo competir

No intentaría ganarles copiando sus 12 cursos, publicando más o rebajando automáticamente el precio. **La oportunidad más defendible es competir por un resultado concreto y un segmento mejor definido.**

1. **Elige una cuña específica.** Por ejemplo, un tipo de profesional, empresa o flujo de trabajo de automatización que la oferta generalista no atienda bien. Valídalo antes de construir el producto.
2. **Vende implementación, no solo contenido.** Plantillas listas para usar, sesiones de trabajo, revisión de automatizaciones y soporte para llevarlas a producción pueden diferenciarte más que añadir cursos.
3. **Promete un resultado verificable.** En lugar de “aprende automatización”, concreta qué podrá automatizar el cliente y en qué plazo razonable. No prometas resultados que no controles.
4. **Diseña la retención desde el inicio.** Onboarding guiado, hitos de progreso, casos compartidos y ayuda para desbloquear proyectos dan motivos para seguir pagando.
5. **Compite por confianza y encaje, no solo por precio.** A $39/mes, el precio de referencia ya es visible. Un producto más especializado podría justificar otro precio; uno más barato solo tiene sentido si el modelo y el coste de servirlo funcionan.
6. **Usa un canal propio.** Lista de correo, buscadores, socios o contenido especializado reducen la dependencia de una sola red social o de la audiencia del fundador.

### Qué medir antes de escalar

Durante una prueba pequeña, mide conversión a pago, activación —si el nuevo miembro consigue un primer resultado—, cancelaciones tempranas y uso del soporte. Si la gente se registra pero no implementa nada, más cursos probablemente no resolverán el problema.

**Conclusión:** el competidor parece tener una oferta pública activa y una posible ventaja de distribución. No hay base para afirmar cuánto factura ni que el negocio sea sano. La cifra de **$93.600/mes** solo aplica si los 2.400 miembros son todos clientes activos que pagan el precio mensual completo.