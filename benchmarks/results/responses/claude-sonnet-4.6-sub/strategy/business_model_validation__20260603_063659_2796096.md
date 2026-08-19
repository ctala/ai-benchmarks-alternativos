# Claude Sonnet 4.6 (suscripción) — strategy/business_model_validation

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.06 | quality: 9.92
- latency_total: 93.318s | tokens_per_second: 44.5
- input_tokens: 3 | output_tokens: 4152
- judge_score: 5.0 | justificación: 

## Respuesta completa

# VC Escéptico activado. Sin filtros.

---

## 1. LOS 5 RIESGOS QUE ME HARÍAN PASAR

### 🔴 Riesgo #1: Desintermediación inevitable
Tu modelo de negocio **enseña a los clientes a evitarte**. Conecto a un restaurante con un proveedor de tomates → hacen el primer pedido por tu plataforma → la próxima semana se llaman directo. ¿Por qué pagarían 15% por siempre para algo que ya saben hacer? Los marketplaces B2B sobreviven cuando el **producto es la plataforma** (Uber: el chofer no puede ser tu amigo y llevarte gratis). Aquí el producto es la *relación*, y tú no puedes ser parte de ella permanentemente.

**La pregunta que no puedes responder fácilmente:** ¿Cuál es tu mecanismo de retención después del primer pedido?

### 🔴 Riesgo #2: El 15% no cabe en los márgenes
Los restaurantes pequeños operan con **3-8% de margen neto**. Sus proveedores de insumos frescos operan con **10-20% de margen bruto**. ¿De dónde sale tu 15%? Alguien tiene que absorberlo:

- Si lo paga el proveedor → sube precios al restaurante → el restaurante se va
- Si lo paga el restaurante → es literalmente más que su margen neto → imposible
- Si "lo absorbe el mercado" → no has hablado con suficientes restaurantes reales

El marketplace de comida es brutalmente diferente a software: **los márgenes no tienen espacio para un intermediario del 15%.**

### 🔴 Riesgo #3: Problema de pollo y huevo sin solución obvia
Proveedores no entran sin volumen. Restaurantes no entran sin proveedores. Clásico, sí. Pero lo específico de tu caso: **los proveedores locales son negocios familiares hiperfragmentados**. Para tener catálogo útil necesitas 50+ proveedores activos. Para convencer a esos 50 proveedores necesitas mostrarles demanda. Para conseguir demanda necesitas catálogo. Tienes que resolver los dos lados simultáneamente con $10K y sin track record.

### 🔴 Riesgo #4: Eres un negocio de logística disfrazado de tech
Ingredientes frescos = cadena de frío, entrega el mismo día, disputas de calidad ("los tomates llegaron malos"), trazabilidad sanitaria. En el momento en que hay un problema de calidad, **¿quién responde?** Si dices "el proveedor", los restaurantes no confían. Si dices "yo", acabas de convertirte en una empresa de logística de alimentos con el costo operacional que implica. La escusa de "somos solo la plataforma" no funciona cuando tu chef perdió el servicio del mediodía por una entrega fallida.

### 🔴 Riesgo #5: La hipótesis es de confort, no validada
"Los restaurantes pierden tiempo llamando a múltiples proveedores." ¿Tienes datos de esto? ¿O es lo que **tú creerías** si fueras restaurante? El dueño de un restaurante pequeño tiene 15 problemas antes del proveedor: flujo de caja, rotación de personal, reclamos de clientes, Servicio de Impuestos Internos. **¿El tiempo en llamadas es realmente el dolor #1?** Porque si no lo es, toda tu propuesta de valor colapsa.

---

## 2. POR QUÉ LATAM ES ESPECIALMENTE DIFÍCIL

### La informalidad es feature, no bug
Una fracción enorme de transacciones restaurante-proveedor son **en efectivo, sin boleta, sin IVA**. Tu plataforma hace esas transacciones visibles al fisco. Estás pidiendo a dos partes que voluntariamente aumenten su carga tributaria a cambio de conveniencia digital. En Chile es mejor, pero en México, Colombia, Perú: **la resistencia es estructural, no conductual.**

### Don Manuel no es un problema, es el producto
El proveedor con quien lleva 15 años el dueño del restaurante le **fía cuando no tiene caja**, le guarda el mejor corte, le avisa cuando hay oferta de última hora, entrega el domingo aunque no quiera. Eso no es un pain point. Es capital social acumulado durante años. Tu app no replica eso. Al contrario, **propones reemplazar confianza personal con una interfaz digital**, en una cultura donde el trato interpersonal es fundacional al negocio.

### El crédito informal es invisible en tu modelo
Los proveedores locales dan crédito a 30-60 días basado en relación personal. Tu plataforma, para funcionar bien, necesita pagos digitales inmediatos o near-realtime. Si no manejas el crédito, excluyes una parte central de cómo funciona el ecosistema. Si sí lo manejas, acabas de convertirte en una fintech con riesgo crediticio, KYC, cobranza... con $10K de capital.

### La sensibilidad al precio es extrema
El restaurantero pequeño en LATAM **manejará 30 minutos en colectivo para ahorrar $3 en tomates**. La eficiencia en tiempo no es su prioridad revelada. Su prioridad revelada es el precio. Y tu plataforma, estructuralmente, agrega costo.

### El mercado central ya existe
La Vega, La Merced, Corabastos, Mercado Mayoreo. Ya hay infraestructura física de agregación de proveedores. Los restaurantes ya saben cómo llegar. ¿Por qué tu app es mejor que ir al mercado el martes?

---

## 3. LO QUE TENDRÍA QUE SER VERDAD (Key Assumptions)

Para que este modelo funcione, **las siguientes cosas deben ser simultáneamente ciertas**. Si alguna falla, el modelo colapsa:

| Assumption | Por qué es arriesgada |
|---|---|
| Los restaurantes valoran tiempo > precio | Evidencia anecdótica dice lo contrario |
| Los proveedores tienen margen para ceder 10-15% | En frescos, raramente cierto |
| La retención supera el 60% al mes 3 | Sin lock-in técnico, improbable |
| Los proveedores digitalizarán su inventario | Cambio de comportamiento masivo |
| Las disputas de calidad son manejables sin logística propia | Una sola crisis lo desmiente |
| La informalidad no bloquea adopción masiva | Requiere validación específica por país |
| Puedes crecer más rápido que el tiempo que toman los acuerdos directos | Requiere velocidad de escala que no tienes |

**Si solo 4 de 7 son verdad, el negocio es marginal. Necesitas las 7.**

---

## 4. EL ESCENARIO DE FRACASO RÁPIDO

> **El modo más probable de muerte: 18 meses, lento y doloroso.**

Construyes una app decente en 6 meses ($40-60K si tienes dev). Consigues 80 restaurantes y 30 proveedores en una ciudad. Los primeros 3 meses, GMV crece: $8K → $15K → $22K/mes. Generas $3,300 de revenue mensual al 15%. Tu burn es $12K/mes.

En el mes 4, notas que el 40% de los pares que conectaste empezaron a ordenar directo. Tu GMV se estanca. Los proveedores empiezan a negociar tu comisión ("te doy 5% o me voy"). Bajas a 8% para retenerlos. Revenue cae a $1,760/mes.

Intentas levantar capital. Los VCs te piden $100K GMV mensual estable. No lo tienes. Los ángeles quieren ver unit economics claros. No los tienes porque el churn es opaco (no sabes cuánto volumen se fue offline).

En el mes 15, tienes $0 en caja. Nunca llegaste a ser un negocio de logística (muy caro) ni un software puro (sin stickiness). Estás en el peor de ambos mundos.

**La causa raíz:** Validaste que los restaurantes *querían* la solución, no que estaban dispuestos a *pagar permanentemente* por ella.

---

## 5. CON $10K PARA VALIDAR: LO QUE YO HARÍA

**Regla #1: No construyas nada todavía.**

### Semana 1-2: Validación del dolor real
- Acompaña a **10 dueños de restaurantes** durante su proceso de pedidos. Cronometra. Graba (con permiso). ¿Cuánto tiempo pierden realmente? ¿Es ese tiempo su problema #1 o mencionan otras 5 cosas primero?
- **Presupuesto: $0** (tu tiempo)

### Semana 3-4: Validación de márgenes del proveedor
- Habla con **15 proveedores locales**. Pregunta directamente: "Si te consigo 10 restaurantes nuevos, ¿me darías el 15% de esas ventas?" Escucha la respuesta real, no la educada.
- **Presupuesto: $0**

### Semana 5-8: MVP sin tecnología
- Crea un **grupo de WhatsApp** con 10 restaurantes y 8 proveedores. Tú eres el operador manual. Recibes pedidos, los pasas a proveedores, confirmas entregas. Cobras 5% de comisión (no 15%, eso viene después).
- **Presupuesto: $500 en tiempo tuyo + incentivos para primeros usuarios**

### Semana 9-12: Mide lo que importa
- ¿Cuántos de los pares conectados intentaron hacer su segundo pedido fuera del grupo? (disintermediation rate)
- ¿Cuántos proveedores están dispuestos a subir su comisión a 10%?
- ¿El NPS de restaurantes es >50?
- **Presupuesto: $1,000 en pequeños incentivos/descuentos para retención**

### Si las métricas son buenas: recién ahí tecnología
- **$8,500 restantes** para un MVP mínimo (landing page + formulario de pedido simple, ni siquiera app). Valida que la tecnología no frena la adopción que ya viste en WhatsApp.

---

## La pregunta que deberías poder responder hoy

> **¿Cuántos restaurantes has acompañado realmente durante su proceso de pedidos?**

Si la respuesta es menos de 10, todavía no tienes hipótesis. Tienes una idea.

La diferencia entre un buen pitch y un pitch que paso es exactamente esa: **¿hablaste con el mercado o con tus amigos que te dijeron que era buena idea?**