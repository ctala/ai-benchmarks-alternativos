# Claude Opus 4.7 — strategy/business_model_validation

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 7.95 | quality: 10.0
- latency_total: 45.096s | tokens_per_second: 45.4
- input_tokens: 293 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación crítica y detallada que un emprendedor podría aplicar directamente.

## Respuesta completa

# VC Escéptico - Modo Brutal Activado

Bien, siéntate. Vamos a hablar en serio porque he visto este pitch 47 veces en los últimos 3 años y 45 de esos founders ya no existen.

---

## 1. Los 5 riesgos que te van a hundir

**a) El problema del huevo y la gallina en marketplaces es brutal, y el tuyo es peor.**
Necesitas proveedores suficientes para que el restaurante entre, y restaurantes suficientes para que el proveedor invierta tiempo en tu app. En LATAM, ambos lados tienen márgenes apretados y CERO paciencia para plataformas vacías. ¿Cómo arrancas? "Nos enfocamos en una zona" — sí, todos dicen eso. Concrétamelo.

**b) Tu comisión del 15% es una fantasía.**
Los proveedores de ingredientes trabajan con márgenes del 8-20%. Pedirles 15% significa que o suben precios (y el restaurante se va con su proveedor de siempre por WhatsApp) o absorben el costo (y no te van a usar). Compárate: Cornershop cobra ~10% a retailers grandes. Rappi para restaurantes 20-30% pero es delivery al consumidor final, otro juego. **Tu número está mal y no lo has cuestionado.**

**c) Desintermediación desde el día 1.**
El restaurante encuentra al proveedor en tu app, hacen 2 pedidos, intercambian WhatsApp, chao plataforma. ¿Qué te hace pegajoso? ¿Logística? ¿Crédito? ¿Datos? Si tu respuesta es "la conveniencia de la app", estás muerto.

**d) Fragmentación de SKUs y falta de estandarización.**
"Tomate" no es "tomate". Hay tomate chonto, riñón, cherry, larga vida, calidad A/B/C, con IVA/sin IVA, por kilo/canasta/arroba. Los precios cambian DIARIAMENTE por clima y estacionalidad. ¿Cómo manejas un catálogo dinámico con 500 proveedores que ni siquiera tienen un sistema? Esto no es un problema de software, es operativo brutal.

**e) Cash flow y crédito.**
Los restaurantes pequeños compran a crédito (7-30 días). Los proveedores pequeños necesitan cash rápido. Si tú no financias esa brecha, no aportas valor real vs. la relación existente. Si la financias, ya no eres marketplace, eres fintech y necesitas 10x el capital.

---

## 2. Por qué LATAM te va a doler específicamente

- **Informalidad brutal.** El 60-70% de estas transacciones son en efectivo, sin factura. Tu app formaliza = fricción fiscal = rechazo.
- **Confianza personal > eficiencia.** El dueño del restaurante compra a "don Pedro" hace 15 años porque don Pedro le fía cuando está mal. Tu algoritmo no fía.
- **Penetración digital de proveedores.** El señor de la plaza de mercado no va a subir su inventario a tu app. Punto.
- **Logística fragmentada.** No hay infraestructura de última milla B2B barata. ¿Quién entrega?
- **Ticket promedio bajo + geografía dispersa.** Unit economics durísimos.
- **Cementerios recientes:** Frubana levantó $80M+ y ha tenido que pivotar múltiples veces. Merqueo, Justo, GrainChain — todos han sufrido. Y tenían más capital que tú.

---

## 3. Qué tiene que ser VERDAD para que funcione (tus key assumptions)

Escribe esto y pégalo en tu pared:

1. Los restaurantes pequeños compran a **≥3 proveedores por semana** (si son 1-2, no hay dolor real de coordinación).
2. Están dispuestos a pagar (directa o indirectamente) **≥5% del ticket** por resolverlo.
3. Los proveedores tienen **capacidad ociosa** y quieren más clientes (no siempre cierto — muchos ya están en máxima capacidad).
4. Puedes lograr **densidad geográfica** (mismo barrio) para que la logística funcione.
5. El precio en tu plataforma es **igual o menor** al que ya pagan (si es mayor, adiós).
6. Puedes construir un **moat** más allá de "juntamos oferta y demanda" (datos, crédito, logística, exclusividad).

Si 2 de estas 6 son falsas, no tienes negocio.

---

## 4. Escenario de fracaso rápido (el más probable, siendo honesto)

**Mes 1-3:** Consigues 20 restaurantes y 15 proveedores en Polanco/Palermo/Chapinero con mucho esfuerzo personal. Todos "aman la idea".

**Mes 4-6:** Los restaurantes hacen 1-2 pedidos, se decepcionan porque falta el producto X, el proveedor no llegó a tiempo, o el precio era 8% más caro. Vuelven a WhatsApp.

**Mes 7-9:** Quemas caja en subsidios y descuentos para mantener GMV. Tus métricas de "usuarios activos" se ven bien pero retención cae a 20%.

**Mes 10-12:** Intentas levantar Serie Seed. Los VCs miran tu retention cohort y tu take rate real (que resulta ser 3%, no 15%). No cierra la ronda. Fin.

**Por qué:** confundiste "es molesto llamar proveedores" con "estoy dispuesto a cambiar mi comportamiento y pagar por resolverlo". Son cosas MUY distintas.

---

## 5. Si tuvieras solo $10K — qué haría yo

**No construyas la app. Repito: NO CONSTRUYA