# Qwen 3.8 Omni Flash — strategy/business_model_validation

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 254.636s | tokens_per_second: 45.4
- input_tokens: 221 | output_tokens: 11553

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

Voy directo, sin anestesia: **tu idea huele a “solución digital para un problema que quizá no es el dolor principal”**. Los restaurantes pequeños no pierden solo tiempo llamando; pierden dinero por precio volátil, mala calidad, faltantes, crédito, devoluciones, logística y desconfianza. Si tu propuesta solo ahorra unos minutos pero cobra 15% sobre insumos, probablemente pierdes.

Además, **15% de comisión en marketplace de ingredientes es agresivo**. En alimentos, los márgenes son delgados. Si el proveedor gana 10–20%, tú quieres llevarte la mitad o más de su margen. Si el restaurante paga 15% extra, estás aumentando su costo de comida, que ya es uno de sus mayores gastos. Eso no es un marketplace; es un impuesto sobre una transacción que ya existe.

Ahora, las preguntas brutales.

---

## 1. Los 5 riesgos principales de tu modelo

### Riesgo 1: Tu comisión de 15% puede ser económicamente absurda

Pregunta que te haría un VC:

> ¿Por qué un restaurante pagaría 15% más, o por qué un proveedor aceptaría reducir su margen 15%, si ya tienen una forma de trabajar?

Ejemplo rápido:

- Un restaurante compra $3,000 al mes en ingredientes.
- Tu comisión del 15% son $450 al mes.
- Si no le ahorras al menos $450 en precio, tiempo, merma, crédito o logística, estás destruyendo valor.
- Si el proveedor normalmente tiene margen de 12–18%, tu comisión se come casi todo su beneficio.
- Si subes precio al restaurante 15%, muchos dicen: “mejor llamo a mi proveedor de siempre”.

Riesgo: **no estás creando eficiencia, estás creando fricción monetaria**.

Para que funcione, tendrías que demostrar una de estas tres cosas:

1. Consigues precios 10–20% mejores por aggregación de demanda.
2. Ahorras costos ocultos: entregas, crédito, devoluciones, admin, pérdidas.
3. Das acceso a proveedores que hoy no son accesibles.

Si ninguna es verdadera, tu comisión no se sostiene.

---

### Riesgo 2: Fuga de transacciones: te usan para conocerse y luego trabajan por fuera

Este es el asesino clásico de marketplaces B2B.

Pregunta:

> ¿Qué impide que restaurante y proveedor se conozcan en tu app y después pidan por WhatsApp, efectivo y sin ti?

Escenario típico:

- Semana 1: restaurante pide por tu plataforma.
- Semana 2: proveedor llama directamente: “para la próxima te dejo mejor precio sin comisión”.
- Restaurante acepta.
- Tú quedas como catálogo gratuito.

En LATAM esto es peor porque ya existe infraestructura informal de evasión: WhatsApp, efectivo, transferencias, facturas parciales, “te hago precio aparte”.

Necesitas una razón fuerte para que se queden on-platform:

- crédito,
- garantía de calidad,
- logística,
- consolidación de pedidos,
- facturación,
- seguros,
- devoluciones,
- historial de precios,
- financiamiento,
- cumplimiento fiscal.

Si solo ofreces “conexión”, te filtran.

---

### Riesgo 3: El incumbente no es “llamadas telefónicas”; es una relación comercial completa

Pregunta:

> ¿Estás comparándote contra el teléfono o contra el distribuidor que ya entrega, fía, devuelve producto malo y mantiene relación personal?

El proveedor tradicional no solo toma pedidos. Hace varias cosas:

- entrega en horario conveniente,
- acepta devoluciones por calidad,
- da crédito de 7, 15 o 30 días,
- negocia precio según volumen,
- avisa faltantes,
- surte urgencias,
- conoce al dueño por nombre,
- resuelve problemas sin ticket de soporte.

Si tu app solo digitaliza el pedido, pero no replica esos servicios, eres peor que el incumbente.

Pregunta incómoda:

> ¿Tu solución quita fricción o solo cambia el canal?

Muchas startups creen que “app = modernidad”. Pero si la app no mejora precio, confiabilidad, crédito o servicio, es un PDF bonito.

---

### Riesgo 4: Los proveedores locales no son estables ni escalables digitalmente

Pregunta:

> ¿Tus proveedores pueden mantener inventario, precios, calidad, tiempos de respuesta y facturación de forma consistente?

“Proveedor local” suena noble, pero operacionalmente puede ser una pesadilla:

- no tiene stock confiable,
- cambia precios diario,
- no emite factura,
- no usa sistema,
- entrega tarde,
- manda producto de calidad irregular,
- no puede cumplir pedidos grandes,
- depende del clima, temporada o humor del productor.

Si eres marketplace, cada mala experiencia la paga tu marca.

Pregunta letal:

> ¿Vas a ser un intermediario pasivo o vas a controlar calidad, inventario y entrega?

Si eres pasivo, te vuelves responsable de problemas que no controlas.  
Si eres activo, te conviertes en distribuidor, con costo fijo, inventario, logística y riesgo.

Y eso ya no es un marketplace liviano.

---

### Riesgo 5: Unit economics probables: pedidos chicos, comisión baja, costo alto

Pregunta:

> ¿Cuál es tu contribución margen por pedido después de comisiones, pagos, soporte, entregas, reembolsos y adquisición de cliente?

Ejemplo conservador:

- Pedido promedio: $150.
- Comisión 15%: $22.5.
- Pasarela de pago 3%: $4.5.
- Soporte/admin: $3.
- Gestión de calidad/reclamos: $3.
- Logística o incentivo de entrega: $8.
- Margen contribución: ~$4.

Con eso no construyes nada.

Si el restaurante pide 4 veces al mes, generas $16/mes de margen contribución.  
Si tu CAC es $200, tardas más de un año en recuperar, asumiendo cero churn.  
Pero los restaurantes pequeños tienen churn alto. Muchos cierran, cambian de proveedor o reducen compras.

Pregunta dura:

> ¿Tu modelo necesita que el cliente viva 12 meses para ser rentable? Si sí, estás muerto en un mercado con alta mortalidad de restaurantes.

---

## 2. Por qué podría NO funcionar en LATAM específicamente

LATAM no es Silicon Valley con otros nombres. Tiene fricciones estructurales que pueden matar este modelo.

### A. Informalidad y efectivo

Muchos proveedores pequeños no facturan. Muchos restaurantes prefieren pagar en efectivo o transferencia informal.

Problema para ti:

- no puedes cobrar comisión fácilmente,
- no tienes trazabilidad,
- no puedes medir GMV real,
- no puedes construir historial crediticio,
- no puedes escalar confianza.

Si tu marketplace depende de transacciones visibles, la informalidad te rompe.

---

### B. El crédito es parte del producto

En muchos mercados latinos, el pequeño restaurante no paga contado. Vive con “fiado”, crédito de proveedor, pagos semanales o quincenales.

Si tú no das crédito, estás compitiendo contra alguien que sí lo da.

Pero si das crédito, ya no eres marketplace. Eres fintech + distribuidor + riesgo financiero.

Pregunta:

> ¿Vas a financiar cuentas por cobrar de restaurantes pequeños con alta tasa de mortalidad?

Eso puede ser negocio, pero requiere capital, scoring, cobranza y tolerancia a pérdida. No es lo mismo que “una app”.

---

### C. Relaciones personales y desconfianza digital

El pequeño restaurante muchas veces no compra “eficientemente”; compra con confianza.

Conoce al proveedor. Sabe quién lo llama. Sabe quién le manda buen tomate. Sabe quién le espera si le falta dinero.

Una app fría no reemplaza eso fácilmente.

Pregunta:

> ¿Por qué un dueño de restaurante confiaría miles de dólares al mes en una plataforma nueva para comprar insumos críticos?

La respuesta no puede ser “porque es digital”. Tiene que ser: precio, garantía, crédito, ahorro real o acceso exclusivo.

---

### D. Logística cara y caótica

Entregar en LATAM puede ser caro por:

- tráfico,
- inseguridad,
- direcciones imprecisas,
- falta de códigos postales confiables,
- porteros/guardias,
- horarios restringidos,
- combustible,
- refrigeración,
- robos,
- costos de última milla.

Si tus pedidos son pequeños, la logística se come la comisión.

Pregunta:

> ¿Tu logística es tan densa que baja el costo por entrega, o estás subsidiando envíos para parecer moderno?

---

### E. Proveedores locales con capacidad limitada

Un productor local puede tener 200 kg de algo esta semana y cero la próxima.

Restaurantes necesitan consistencia. Si fallas dos veces, te botan.

Pregunta:

> ¿Puedes garantizar disponibilidad real o solo muestras catálogo ilusorio?

---

### F. Impuestos, facturación y cumplimiento

Dependiendo del país, puedes chocar con:

- IVA,
- retenciones,
- facturación electrónica,
- regulaciones sanitarias,
- responsabilidad por alimentos,
- transporte refrigerado,
- permisos municipales,
- trabajo informal.

Marketplace “ligero” puede volverse pesado rápido.

Pregunta:

> ¿Quién asume responsabilidad si un producto causa intoxicación, llega podrido o no cumple normativa sanitaria?

---

### G. Alta competencia de soluciones “feas” pero efectivas

Tus competidores no son solo apps. Son:

- WhatsApp,
- llamadas,
- distribuidores de ruta,
- mayoristas,
- mercados centrales,
- grupos de compradores,
- apps de delivery adaptadas,
- plataformas B2B existentes,
- contactos familiares.

Pregunta:

> ¿Por qué tu solución gana contra un ecosistema que ya funciona suficientemente bien para el usuario?

“Suficientemente bien” es el enemigo de toda startup.

---

## 3. Qué tendría que ser verdad para que funcione: key assumptions

Necesitas que todas estas afirmaciones sean verdaderas. Si una falla, el modelo se cae.

### Supuesto 1: El dolor es suficientemente grande y monetizable

Debe ser verdad que los restaurantes no solo “pierden tiempo”, sino que pierden dinero significativo por:

- sobreprecio,
- merma,
- urgencias,
- falta de comparación,
- admin,
- devoluciones,
- crédito ineficiente,
- proveedores poco confiables.

Cómo lo falsas:

- Entrevista a 30 dueños/chefs.
- Pide datos de sus últimas 20 compras.
- Mide horas perdidas, sobrecostos, reclamos, pedidos urgentes.
- Si el ahorro potencial es menor a tu comisión, mataste la tesis.

Métrica mínima:

- El restaurante debe ahorrar o ganar al menos 1.5x a 2x el valor de tu comisión.
- Ejemplo: si cobras $300/mes, debes generar $450–$600/mes de valor comprobable.

---

### Supuesto 2: Puedes ofrecer mejor costo total landed, no solo “app”

Costo total no es precio de lista. Incluye:

- precio,
- envío,
- fallas,
- devoluciones,
- producto dañado,
- tiempo administrativo,
- crédito,
- penalizaciones por falta,
- riesgo.

Debe ser verdad:

> Tu plataforma ofrece menor costo total que el proveedor actual, incluso con 15% de comisión.

Cómo lo falsas:

- Compara 20 pedidos reales contra compras históricas.
- Mide precio final, entregas, reclamos, tiempo, faltantes.
- Si pierdes en costo total, no tienes negocio.

---

### Supuesto 3: Los proveedores aceptan la comisión sin destruir su margen

Debe ser verdad:

> El proveedor tiene margen suficiente, capacidad excedente y motivación para pagar 15% por nuevos clientes o pedidos agregados.

Pero ojo: si el 15% se lo traslada al restaurante, vuelve el problema anterior.

Cómo lo falsas:

- Entrevista 20 proveedores.
- Pide margen bruto real, costos de venta, capacidad, política de precios.
- Haz pilotajes con comisión visible.
- Si solo aceptan “los primeros 3 meses”, no es comportamiento sostenible.

---

### Supuesto 4: Puedes evitar la fuga de transacciones

Debe ser verdad:

> Hay una razón estructural para que compren por ti aunque se conozcan.

Posibles razones válidas:

- crédito,
- garantía,
- consolidación de compras,
- precio negociado por volumen,
- logística incluida,
- facturación,
- devolución simplificada,
- seguro de calidad,
- programa de lealtad,
- financiamiento,
- datos de precios.

Cómo lo falsas:

- Después del primer pedido, mide cuántos segundos pedidos ocurren on-platform.
- Si a los 30 días más del 30–40% se va fuera, tu marketplace es un directorio.

Métrica clave:

- Retención on-platform >70% al segundo mes.
- Fuga <20% después de 60 días.

---

### Supuesto 5: Los restaurantes recompran con frecuencia suficiente

Debe ser verdad:

> Compran al menos 2–4 veces al mes y mantienen gasto estable.

Si compran una vez al mes o sporádicamente, no hay LTV.

Cómo lo falsas:

- Piloto de 4–6 semanas.
- Mide frecuencia real, no intención.

Métricas mínimas:

- Al menos 40–50% de pilotos hacen segunda compra en 14–21 días.
- Al menos 25–30% hacen tercera compra en 30–45 días.
- GMV mensual por restaurante activo >$1,500–$3,000, dependiendo de tu comisión y costos.

---

### Supuesto 6: Tu margen contribución es positivo por pedido

Debe ser verdad:

> Después de comisión, pagos, soporte, logística, reembolsos y costos variables, ganas dinero en cada pedido.

Fórmula mínima:

```text
Margen contribución =
Comisión recibida
- fee pasarela
- costo soporte
- costo logística/incentivo
- reembolsos/merma
- costos de calidad
- costos de cobranza
```

Si es negativo, escalar es acelerar la quiebra.

Meta inicial:

- Margen contribución >30–40% de la comisión bruta.
- Idealmente >50% una vez maduro.

---

### Supuesto 7: Puedes adquirir restaurantes con CAC razonable

Debe ser verdad:

> Tu CAC se recupera en menos de 3–6 meses con margen contribución.

En B2B local, la venta puede ser cara: visita física, confianza, demostración, soporte.

Ejemplo:

- Comisión mensual por restaurante: $300.
- Margen contribución mensual: $150.
- CAC máximo para payback 4 meses: $600.
- Si tu CAC es $1,200, necesitas retenerlo 8+ meses.
- Con churn alto de restaurantes, eso es riesgoso.

Pregunta:

> ¿Puedes bajar CAC con referidos, densidad geográfica o canal de proveedores, o cada cliente te cuesta una venta cara?

---

### Supuesto 8: Puedes resolver calidad y disputas sin volverte inviable

Debe ser verdad:

> Tienes un mecanismo claro para productos malos, faltantes, retrasos y devoluciones.

Si no, los usuarios te culpan a ti.

Opciones:

- garantía plataforma,
- inspección,
- SLA proveedor,
- reembolso inmediato,
- blacklisting,
- seguros,
- estándares mínimos.

Pero cada opción cuesta dinero u operación.

---

### Supuesto 9: El modelo es defendible

Debe ser verdad:

> No basta con conectar. Tienes algo que otros no pueden copiar fácil.

Posibles moats:

- datos de demanda agregada,
- poder de negociación por volumen,
- red densa de proveedores exclusivos,
- sistema de crédito basado en compras,
- logística propia eficiente,
- marca de confianza,
- contratos con chefs/compradores,
- integración con POS/inventario,
- comunidad o gremio.

Si tu moat es “somos una app”, no tienes moat.

---

### Supuesto 10: LATAM permite operar esto sin morir en cumplimiento

Debe ser verdad:

> Puedes facturar, cobrar, cumplir normas sanitarias y operar legalmente sin costo prohibitivo.

Si no, tu crecimiento se frena o te expones a multas.

---

## 4. Escenario donde fracasas rápido y por qué

Te pinto el funeral típico.

### Mes 1: entusiasmo falso

Lanzas en una ciudad. Consigues 30 restaurantes y 10 proveedores mediante descuentos, favores y ventas personales.

GMV inicial: $30,000.  
Comisión 15%: $4,500.  
Todos felices en el dashboard.

Pero no sabes si es real porque diste incentivos.

---

### Mes 2: primera señal de alerta

Los restaurantes empiezan a pedir menos.

Descubres que:

- algunos solo compraron para probar,
- otros compararon precio y volvieron con su proveedor,
- varios pidieron una sola categoría, no canasta completa,
- los proveedores subieron precio offline para compensar tu comisión,
- hubo dos entregas malas y ya no confían.

Retención: 20%.  
Fuga a canal directo: 35%.

---

### Mes 3: unit economics negativos

AOV: $120.  
Comisión: $18.  
Pagos: $4.  
Soporte: $4.  
Logística/incentivo: $7.  
Reembolsos: $3.  
Margen contribución: $0 o negativo.

Estás pagando por que usen la plataforma.

---

### Mes 4: el proveedor te traiciona

Tu mejor proveedor te dice:

> “Ya tengo 15 restaurantes tuyos. Para la próxima les doy 10% descuento directo y trabajamos sin comisión.”

No tienes contrato fuerte, no tienes exclusividad, no tienes crédito, no tienes logística.

Te conviertes en marketing gratuito.

---

### Mes 5: churn de restaurantes se dispara

Los restaurantes pequeños cierran, cambian de menú, reducen compras o encuentran precio mejor.

Tu base activa cae de 30 a 12.

CAC fue alto, LTV no existe.

---

### Mes 6: quema de caja

Necesitas más proveedores, más soporte, más logística, más cobro.

Tu equipo crece, pero el GMV no.

Inversores preguntan:

- ¿retención?
- ¿fuga?
- ¿margen contribución?
- ¿por qué no te cortan?
- ¿cuál es el moat?

No tienes respuestas.

Muerte rápida.

---

### Por qué fracasaste

No fracasaste por “falta de app”.

Fracasaste por una o varias de estas razones:

1. El dolor no era suficiente.
2. La comisión no estaba justificada.
3. No ofreciste crédito, logística ni garantía.
4. Los proveedores te绕过.
5. Los pedidos eran muy chicos.
6. La calidad fue inconsistente.
7. El CAC fue alto y el churn también.
8. Confundiste digitalización con creación de valor.

---

## 5. Si solo tuvieras $10,000 para validar, qué haría yo

No haría app. No haría branding. No contrataría desarrollador. No gastaría en oficina. No haría “plataforma scalable”.

Haría un **MVP concierge brutalmente manual** en una zona pequeña.

Objetivo: demostrar que restaurantes pagan, recompran y no se fugan, y que proveedores cumplen.

---

### Paso 1: Elige un nicho ridículamente específico

No “restaurantes en general”.

Elige algo como:

- 20 taquerías en un barrio,
- 15 comedores populares en una zona,
- 10 restaurantes de menú del día,
- 12 cafeterías que compran lácteos/huevos/pan,
- 15 restaurantes que compran verduras y frutas básicas.

Criterios:

- alta densidad geográfica,
- frecuencia de compra,
- productos relativamente estándar,
- bajo riesgo sanitario inicial,
- proveedores locales accesibles,
- tickets no demasiado pequeños.

Evita al inicio:

- mariscos delicados,
- cárnicos con cadena de frío compleja,
- productos ultra perecederos,
- proveedores muy informales sin factura,
- restaurantes gourmet con necesidades raras.

Empieza con aburrido: papa, cebolla, tomate, huevo, arroz, aceite, lácteos básicos, pan, verduras comunes.

---

### Paso 2: Haz 30 entrevistas reales, no de validación barata

No preguntes: “¿usarías una app?”

Eso es basura. Todos dicen que sí para no herirte.

Pregunta hechos:

- ¿Cuánto gastaste la semana pasada en cada categoría?
- ¿A quién le compraste?
- ¿Cómo hiciste el pedido?
- ¿Cuánto tardaste?
- ¿Qué salió mal?
- ¿Hubo devoluciones?
- ¿Te dieron crédito?
- ¿Pagaste efectivo o transferencia?
- ¿Recibiste factura?
- ¿Cambiarías de proveedor por 5% menos? ¿por 10%? ¿por entrega más confiable?
- ¿Cuánto perdiste por producto malo o faltante el último mes?

Meta:

- 20 restaurantes.
- 10 proveedores.

Kill test:

Si menos del 30% de restaurantes confirma un dolor cuantificable y dispuesto a cambiar, para.

Si los proveedores no pueden dar precio, disponibilidad y cumplimiento mínimo, para.

---

### Paso 3: Diseña una oferta que no sea “app”

No vendas “marketplace”. Vende una promesa concreta:

Ejemplos:

- “Te consigo estos 8 básicos con precio cerrado semanal y entrega martes/jueves.”
- “Agrupamos tu compra con otros restaurantes para bajarte precio.”
- “Te garantizamos reposición si llega mal.”
- “Te damos crédito a 7 días si cumples historial.”
- “Te facturamos y centralizamos pedidos.”

La comisión de 15% puede ser demasiado visible al inicio. Podrías probar estructura:

- 10–15% al proveedor si trae nuevo cliente/volumen,
- o fee al restaurante por servicio,
- o markup transparente,
- o comisión fija por pedido,
- o suscripción + comisión menor.

Pero debes probar que alguien paga.

---

### Paso 4: Construye un stack no-code/manual

Con $10K no programo app custom.

Usaría:

- WhatsApp Business,
- Google Sheets o Airtable,
- Formulario simple,
- Catálogo PDF o link,
- Mercado Pago/Stripe/transferencia,
- contrato simple,
- Excel de pedidos,
- ruta de entrega manual,
- kurier/courier local por pedido.

No inventes tecnología. Inventa proceso.

---

### Paso 5: Recluta 10 restaurantes piloto, no 100

Quiero 10 obsesionados, no 100 curiosos.

Condiciones del piloto:

- pedido mínimo real,
- pago por adelantado o contra entrega,
- comisión visible,
- compromiso de 4 semanas,
- feedback semanal,
- permiso para medir datos.

Importante: no regales el servicio por 3 meses. Eso no valida disposición a pagar.

Puedes dar descuento primera orden, pero segunda y tercera deben ser a precio completo.

---

### Paso 6: Opera como servicio manual durante 4–6 semanas

Tú o tu cofundador hacen de:

- vendedor,
- comprador,
- coordinador logístico,
- soporte,
- control de calidad,
- cobrador,
- analista.

Cada pedido debe responder:

- ¿quién pidió?
- ¿qué pidió?
- ¿precio normal vs tu precio?
- ¿quién entregó?
- ¿llegó bien?
- ¿hubo reclamo?
- ¿pagó comisión?
- ¿repitió?
- ¿intentó irse fuera de plataforma?

---

### Paso 7: Métricas de vida o muerte

No me interesan downloads, registros, likes ni “interés”.

Me interesan:

#### Demanda

- % de pilotos que hacen segundo pedido en 14 días.
- % que hacen tercer pedido en 30 días.
- frecuencia semanal.
- ticket promedio.
- GMV mensual por restaurante.

#### Oferta

- % de pedidos cumplidos completos.
- % de entregas a tiempo.
- % de productos rechazados.
- tiempo de resolución de reclamos.
- disposición del proveedor a repetir sin subsidio.

#### Economía

- comisión cobrada real.
- costos variables por pedido.
- margen contribución por pedido.
- CAC por restaurante.
- payback estimado.
- fuga off-platform.

#### Retención

- churn mensual.
- % de clientes que recomiendan.
- % que aumentan canasta.

---

### Umbrales que yo usaría para matar o continuar

Con $10K, después de 6 semanas:

#### Matar el proyecto si:

- Menos del 30% de pilotos repite compra en 21 días.
- Más del 40% de transacciones se fuga fuera de plataforma.
- El margen contribución por pedido es negativo.
- Los proveedores no pueden mantener precio/calidad/disponibilidad.
- El ahorro para el restaurante es menor al 50% de tu comisión.
- Necesitas subsidiar cada pedido para que exista tracción.
- El CAC es mayor a 6 meses de margen contribución.

#### Continuar si:

- 5–7 de 10 pilotos repiten al menos 3 veces.
- Fuga on-platform <20–25%.
- Margen contribución positivo por pedido.
- Restaurantes ahorran o perciben valor >1.5x comisión.
- Proveedores aceptan condiciones sin descuento extremo.
- Puedes explicar por qué no te cortan.
- Tienes evidencia de que el modelo puede repetirse en otra zona similar.

---

### Distribución sugerida del presupuesto de $10,000

Aproximada, adaptable a país:

| Rubro | Monto | Para qué |
|---|---:|---|
| Investigación de campo | $1,000 | Transporte, entrevistas, pequeños incentivos éticos, café, movilización |
| Herramientas no-code/admin | $500 | WhatsApp Business, Airtable/Sheets, dominio, correo, firma electrónica básica |
| Operación piloto | $2,500 | Courier, gasolina, empaques, pesaje, apoyo operativo |
| Reserva para reembolsos/calidad | $1,500 | Producto malo, faltantes, reclamos |
| Pagos/fees/float | $1,000 | Comisiones pasarela, cambios, retenciones, caja pequeña |
| Ventas presenciales | $1,000 | Material simple, visitas, demostraciones, seguimiento |
| Legal básico/contratos | $500 | Términos, acuerdo proveedor, privacidad, factura |
| Contingencia | $1,500 | Imprevistos reales, no feature creep |
| Total | $10,000 |  |

No gastaría ni $1 en app custom en esta fase.

---

## Lo que yo haría si quisiera aumentar probabilidades de éxito

No empezaría como marketplace puro. Empezaría como **servicio de abastecimiento gestionado**.

Modelo posible:

1. Agrupas demanda de 20 restaurantes en una zona.
2. Negocias precio con 3–5 proveedores.
3. Controlas calidad mínima.
4. Coordinas entregas consolidadas.
5. Cobras fee por servicio o comisión.
6. Eventualmente digitalizas lo que ya funciona manualmente.

Eso es menos sexy, pero más real.

Otra variante:

- No cobres 15% flat.
- Cobra 5–8% + fee fijo por pedido + servicio premium.
- O cobra suscripción al restaurante por acceso a precios negociados.
- O cobra al proveedor por lead calificado, no por transacción.
- O monetiza financiamiento, no comisión.

En B2B de commodities, la comisión pura es frágil.

---

## Preguntas finales que te dejarían sin sueño en un pitch

1. **¿Cuál es tu costo total de adquisición por restaurante y en cuántos meses lo recuperas con margen contribución real?**

2. **¿Qué porcentaje de tus primeros 50 clientes volvió a comprar sin descuento a los 30 días?**

3. **¿Qué porcentaje de transacciones se fugó fuera de plataforma después del segundo pedido?**

4. **¿Por qué un proveedor no te corta en cuanto tenga cinco clientes tuyos?**

5. **¿Qué valor entregas que justifique 15% sobre un insumo donde el margen del restaurante ya es apretado?**

6. **¿Comparaste contra el incumbente en precio, crédito, entrega, calidad y devolución, no solo en “facilidad de pedir”?**

7. **¿Cuál es tu ticket promedio y cuánto margen contribución dejas después de costos variables?**

8. **¿Qué haces cuando llega tomate podrido, falta huevo o el proveedor entrega tarde?**

9. **¿Cómo escalas sin convertirte en una distribuidora con camiones, almacén, crédito y personal fijo?**

10. **¿Por qué esto no es simplemente WhatsApp + hoja de cálculo + un amigo que coordina entregas?**

---

## Veredicto brutal

Hoy, tal como está planteado, yo no invertiría.

No porque la idea sea imposible, sino porque está demasiado cerca de:

> “Vamos a cobrar 15% por conectar dos partes que ya se encuentran por WhatsApp, teléfono y relación personal, sin resolver precio, crédito, logística ni confianza.”

Eso no es un marketplace defensibles. Es un peaje fácil de evadir.

Para que me intereses, necesito ver evidencia de tres cosas:

1. **Restaurantes pagando comisión real y recomprando.**
2. **Proveedores cumpliendo sin subsidio y sin fugarse.**
3. **Unit economics positivas por pedido, no por proyección bonita.**

Si me traes 10 restaurantes que compraron 3+ veces, con fuga menor a 20%, margen contribución positivo y un motivo claro por el que no te cortan, entonces sí podemos hablar.

Si no, estás construyendo una app para resolver un problema que quizá se arregla mejor con un grupo de compras, un servicio logístico, financiamiento o una relación comercial más profunda.