# GLM 5.3 — strategy/business_model_validation

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 116.33s | tokens_per_second: 63.7
- input_tokens: 185 | output_tokens: 7407

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

Bien. Vamos a sentarnos en la mesa de pitch. Lo primero que pienso cuando leo tu modelo: esta categoría es un cementerio. Frubana levantó nueve dígitos y terminó pivotando a distribuidor full-stack. Cheetah quebró. Choco y Rekki tuvieron que volver su app gratis y buscar la monetización en otro lado (fintech). Ningún marketplace de insumos B2B con comisión por transacción ha escalado a nivel global. Eso no significa que sea imposible, pero significa que la carga de la prueba es tuya. Vamos por tus preguntas.

## 1. Los 5 riesgos principales

**1. Desintermediación.** Este es el asesino. Un restaurante compra al mismo proveedor 2-3 veces por semana. Para la transacción #5, ambos lados ya tienen el número del otro guardado. El proveedor tiene un incentivo brutal: "pásame el pedido directo y te doy 7% de descuento" — se reparten tu comisión. WhatsApp es tu competidor real, es gratis, y ya está instalado en ambos teléfonos. ¿Qué valor le das al proveedor **en cada transacción** para que no se salga?

**2. La matemática no cierra.** Hazla conmigo:
- Restaurante pequeño: ~$6,000 USD/mes de ventas
- Costo de insumos: ~30% → $1,800/mes en compras
- Tu comisión del 15%: **$270/mes**
- Margen neto típico de un restaurante: 3-9% → $180-540/mes

Tu comisión equivale a entre el 50% y el 150% de la ganancia neta del restaurante. Le estás pidiendo a un negocio que opera al filo que te entregue su utilidad. Y si se la cobras al proveedor en vez del restaurante, el proveedor sube precios o se va. Alguien siempre absorbe esos $270. ¿Quién, y por qué aceptaría?

**3. Tu competencia no es otra app: es el fiado.** El proveedor tradicional en LATAM le da crédito a 8-15 días, le salva al restaurante cuando le falta algo a las 10pm, y le cambia el jitomate malo sin discusión. Tu marketplace con pago anticipado es *peor* que el status quo para un restaurante que vive semana a semana. No estás compitiendo contra un proceso analógico ineficiente; estás compitiendo contra una línea de crédito informal y una relación de años.

**4. Logística de perecederos.** ¿Quién entrega? Si es el proveedor, la experiencia es inconsistente y tú no controlas nada. Si eres tú, dejaste de ser marketplace y eres distribuidor — con camionetas, cadena de frío, inventario y margen bruto de 15-25% que justifica esa operación. Quieres economía de distribuidor sin hacer el trabajo de distribuidor.

**5. Liquidez y churn.** Efecto huevo-gallina clásico, pero tu lado de demanda además se muere: la tasa de cierre de restaurantes pequeños en LATAM es altísima. Tu CAC nunca deja de correr porque tus clientes quiebran. Y cada ciudad requiere su propia densidad de oferta. No hay una red LATAM; hay 20 mercados fragmentados.

## 2. Por qué podría NO funcionar en LATAM específicamente

- **Informalidad.** Un porcentaje enorme de restaurantes no factura, opera en efectivo, no tiene procesos de compra formales. No hay un "gerente de procurement" al cual venderle eficiencia.
- **El efectivo y las transferencias directas.** Si el pago fluye por fuera de tu plataforma, no puedes ni verificar tu GMV. Tu comisión se vuelve un sistema de honor. Si fluye por dentro, pierdes 3-4% en procesamiento y asumes riesgo operativo.
- **La relación personal es el producto.** "Mi proveedor me conoce, me fía, me resuelve." Le pides reemplazar eso con una interfaz y una disputa por ticket.
- **WhatsApp Business con catálogo ya existe y es gratis.** El proveedor medianamente moderno ya lo usa. Tu propuesta tiene que vencer a eso, no a un mundo analógico imaginario.
- **Disputas de calidad en perecederos.** La lechuga llegó mala. ¿Quién responde? Una sola experiencia mala en este gremio —donde todos se conocen— te quema un barrio entero.

## 3. Key assumptions — lo que tendría que ser verdad

1. **El dolor de llamar proveedores duele lo suficiente para pagar 15%.** Hipótesis alternativa muy plausible: es una molestia tolerada, parte del oficio, no un problema de $270/mes.
2. **Puedes retener las transacciones.** Leakage < 30% al mes 6, teniendo un valor por transacción: crédito, pago garantizado al proveedor, entrega consolidada, o garantía de calidad. Sin uno de esos, la fuga al 100% es cuestión de tiempo.
3. **El crédito o la consolidación logística es el producto real, no el "matching".** El marketplace es la cuña; el negocio probablemente es fintech (crédito al restaurante, pago inmediato al proveedor) o logística.
4. **Densidad en UNA ciudad.** Puedes llegar a suficientes restaurantes y proveedores por kilómetro cuadrado para que el modelo funcione antes de expandirte.
5. **Puedes cobrar verificablemente.** El dinero pasa por tu plataforma, punto.
6. **CAC < LTV considerando que tus clientes cierran.** Con churn estructural del lado demanda, tu LTV por restaurante es corto por diseño.

## 4. El escenario de fracaso rápido

Mes 1: lanzas con promociones en una zona de restaurantes. 50 restaurantes, 20 proveedores. Todo se ve bien — pero es ruido de novedad, no retención.

Mes 2-3: los restaurantes que sobreviven ya guardaron el WhatsApp del proveedor. Los pedidos empiezan a irse por fuera. El GMV se aplana.

Mes 4-5: pones descuentos para reactivar. Los proveedores dejan de contestar en la plataforma porque no les llega volumen. Un restaurante recibe producto malo, no hay proceso de resolución, y te lo cuenta a todos sus conocidos del gremio.

Mes 6-9: quemaste $10K en subsidios reactivando clientes que ya se desintermediaron. Tu métrica de "GMV total" esconde que el 70% es leakage. Sin métrica de retención limpia, no levantas ronda. Muerte por agotamiento de runway con la historia de "vamos bien, solo falta producto".

La variante aún más rápida: en la semana 2 descubres que nadie, ni siquiera con tú parado enfrente, acepta pagar el 15% de comisión. Si no puedes cobrarla con una sonrisa y frente a frente, no la vas a cobrar con una app.

## 5. Con $10K para validar

**Regla absoluta: cero código.** Una app es lo que compras cuando ya sabes que el modelo funciona. Con $10K compras aprendizaje, no software.

**Semanas 1-3 — Observación, no encuestas.** Ve a 25-30 restaurantes y NO preguntes "¿usarías esta app?". Todos dirán que sí; es gratis mentir. En cambio: acompaña al dueño una mañana mientras hace sus pedidos. Mapea cuántos proveedores tiene, con qué frecuencia compra, cómo paga, qué términos de crédito, cuánto tiempo real pierde, qué sale mal. Paralelamente, habla con 10 proveedores: su dolor probablemente es **que le pagan tarde** y tener camiones regresando vacíos. Ahí puede estar tu modelo de verdad.

**Semanas 4-12 — Broker manual (concierge MVP).** WhatsApp Business + Google Sheets + tú. Una sola zona, un solo tipo de restaurante. Acepta pedidos, consíguelos, cobra tu 15% **desde el primer pedido, con dinero real**. Presupuesto: ~$2K en incentivos para shadowing, ~$3K operando el piloto, ~$4K de reserva para iterar. Nada en desarrollo.

**Métricas que definen vida o muerte** (defínelas ANTES de empezar):
- Retención: ¿% de restaurantes con 4+ pedidos/mes en la semana 8, sin subsidio?
- Leakage: ¿qué % de pedidos se intenta mover a contacto directo?
- Take rate efectivo: después de fugas y descuentos, ¿qué % realmente cobras?
- ¿Puedes cobrar 15% o el mercado solo tolera 5-8%?

**Criterio de muerte:** si al mes 2 no puedes sostener ni un 10% de comisión efectiva con retención del 40%+, mata el modelo de marketplace y evalúa los pivotes: distribuidor full-stack (caro pero probado), SaaS gratis + fintech, o agregador de compras grupales.

---

Y la pregunta con la que cerraría el pitch: **¿qué sabes tú que Frubana no supo con $100M y cientos de operadores en el terreno?** Si tu respuesta es "nada todavía, pero voy a averiguarlo gastando $10K y no $10M", esa es la respuesta correcta. Ahora ve a cobrar tu primera comisión a mano. Ese es el único pitch que me interesa ver.