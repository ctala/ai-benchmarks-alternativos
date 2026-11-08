# GLM 5.3 Flash — strategy/business_model_validation

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 118.145s | tokens_per_second: 68.2
- input_tokens: 185 | output_tokens: 8056

## Entrada exacta (lo que recibió el modelo)

**user:**

Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto.


## Respuesta completa

Voy a hacer de VC escéptico que ya vio morir tres startups de food supply chain. Primero, contexto incómodo: esto ya se intentó. Frubana levantó más de US$200M (SoftBank, DST) para hacer casi exactamente esto en LATAM y aun así pivotó varias veces, hubo despidos y terminó pareciendo más un distribuidor full-stack con crédito que un marketplace. Que haya habido capital en la categoría no valida tu tesis: valida que es difícil.

## 1. Los 5 riesgos principales

1. **Tu comisión es matemáticamente agresiva.** Los restaurantes operan con márgenes de 3-10%. La distribución de alimentos trabaja con márgenes de 5-15%. Tu 15% puede ser igual o mayor que *todo el margen del canal*. La pregunta que te van a hacer: ¿quién absorbe la comisión? Si la paga el proveedor, sube precios y eres más caro que el status quo. Si la paga el restaurante, le quitas un tercio de su utilidad. No hay respuesta fácil.

2. **No eres una app, eres una empresa de logística disfrazada de software.** Ingredientes frescos: perecederos, sin estandarización ("una caja de jitomate" no es una especificación), disputas de calidad, devoluciones. Alguien tiene que mover cajas. Si no lo haces tú, ¿cuál es tu valor? Si lo haces tú, la comisión se evapora en costo de servir.

3. **Cold start brutal.** Marketplace bilateral donde ambos lados son microempresas fragmentadas. Necesitas densidad geográfica (un barrio, no una ciudad) para que un camión salga lleno. Antes de densidad: entregas medio vacías y proveedores que te ignoran.

4. **Desintermediación.** Tu "producto" es la relación. Después de 3 pedidos, el restaurante tiene el teléfono del proveedor y viceversa. Los marketplaces de bienes relacionales sangran GMV por diseño.

5. **Los restaurantes pequeños son el peor cliente posible.** Churn altísimo (30%+ mueren en el primer año), tickets pequeños, pagan tarde, y van a exigir crédito a 30-60-90 días. Si das crédito, eres un fintech disfrazado de marketplace, con todo el riesgo que eso implica.

## 2. Por qué LATAM es más duro

- **El status quo es gratis y funciona.** Tu competencia no es otra app: es WhatsApp + 20 años de confianza + el proveedor que te fía. Un marketplace con 15% y pago inmediato compite contra un canal informal con 0% comisión y financiamiento incluido.
- **Informalidad estructural.** Central de Abasto, Corabastos, Lo Valledor: efectivo, sin factura, sin trazabilidad. Formalizar el flujo le cuesta dinero a alguien y nadie quiere pagar por eso.
- **El dueño lo hace todo.** Es chef, cajero y comprador. "Ahorrar tiempo llamando" compite contra llamar mientras cocina, gratis, con quien le fio el mes pasado.
- **Infraestructura.** Tráfico, dispersión, cadena de frío inexistente. El costo de servir por pedido es mayor que en mercados densos.
- **El precedente.** Frubana necesitó años y capital casi ilimitado. Con una fracción de eso, ¿cuál es tu teoría de por qué tú sí?

## 3. Qué tendría que ser verdad (escríbelas como hipótesis falsables)

1. El tiempo perdido llamando cuesta más que la comisión —**medido en pesos, no en molestia**. O el precio vía plataforma es mejor que el negociado en persona (poco probable: en persona negocian y les fían).
2. Los proveedores ceden 15% sin subir precios por encima de lo que el restaurante paga hoy. Casi imposible salvo que agregues crédito, menos merma o menos devoluciones.
3. El restaurante te da **≥30% de su compra total**, no solo las verduras. Share of wallet bajo = economics de nicho.
4. Retención orgánica en el mes 2-4, sin subsidios. Este es EL número. Los marketplaces mueren en el mes 3, no el día 1.
5. Frecuencia ≥2-3 pedidos/semana y ticket suficiente para diluir logística.
6. No te desintermedian, o llenas el balde más rápido de lo que se vacía.

## 4. El escenario de fracaso rápido

Mes 1-2: onboardeas 10 proveedores y 30 restaurantes a puro forceo. Los primeros 50 pedidos se sienten geniales. Después: tickets de $60-120, cada entrega cuesta más que la comisión; un proveedor sube precios 12% para compensarte; el restaurante compara factura contra su grupo de WhatsApp y vuelve; al mes 3, 60% de tu cohorte no pidió de nuevo; y los 3 mejores proveedores ya tienen relación directa con tus mejores restaurantes — les hiciste el matchmaking gratis. Mes 5: $8K quemados, cero software, cero retención.

La lección que no verás a tiempo: la app es el 10% del negocio. El 90% es logística, crédito y confianza, y tu 15% no cubre ese 90%.

## 5. $10K de validación

Nada de código. Con $10K compras evidencia de comportamiento, no producto:

- **Semanas 1-2 — Precios reales, no opiniones:** consigue las listas de compra actuales de 20 restaurantes y cotiza los mismos 20 ítems en el mercado mayorista. Construye el precio "tú + 15%" y ponlo frente a los dueños. Si tu lista no gana en precio ni en conveniencia, ya sabes.
- **Semanas 2-6 — Piloto concierge en una zona de 2-3 km:** 10-15 restaurantes, 3-5 proveedores, pedidos por WhatsApp, catálogo en Google Sheets, entregas tú mismo (moto o camioneta rentada, ~$500/semana). **Cobra la comisión real. No subsidies: el subsidio miente.**
- **Instrumenta:** ticket promedio, frecuencia semanal, costo de servir (tus horas × costo), % de devoluciones, y sobre todo: % de la compra total del restaurante que capturas y retención semanal de cohorte.
- **Prueba de proveedores:** 5 firman acuerdo Y procesan 20+ pedidos al 15% real. Vigila el *price creep* — lo que dicen en la reunión no es lo que hacen con los precios.
- **Criterios de kill escritos HOY:** menos de 40% de la cohorte hace un 3er pedido → hipótesis de comportamiento muerta. Costo de servir >25% del GMV → logística no da. Proveedores suben >10% → take rate no da. Matar esto en la semana 6 con $4K gastados es ganar.

Lo que le muestras a un inversionista no es un pitch: es una curva de retención y unit economics por pedido real.

Y las preguntas que no me hiciste, y que te haré yo: **¿por qué tú?** ¿Qué sabes de la cadena de suministro de alimentos que no sepa un distribuidor con 20 años en el mercado? ¿Y qué te hace pensar que el dolor real es el tiempo y no el precio, la calidad o el crédito? Si no puedes responder eso con evidencia de campo —no con intuición— tienes una hipótesis, no una tesis.