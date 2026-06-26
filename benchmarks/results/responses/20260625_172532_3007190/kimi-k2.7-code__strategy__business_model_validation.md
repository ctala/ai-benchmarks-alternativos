# Kimi K2.7 Code — strategy/business_model_validation

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.17 | quality: 9.16
- latency_total: 101.088s | tokens_per_second: 30.6
- input_tokens: 201 | output_tokens: 3089
- judge_score: 4.4 | justificación: 

## Respuesta completa

Voy a ser directo. Tu idea no es mala, pero suena como el pitch #847 que escucho cada año. Todo el mundo quiere ser el “Faire de restaurantes” o el “Mercado Libre de la comida”. La gran mayoría fracasa antes del año 2. Aquí te va el cuestionario que te haría en la sala, sin filtro.

---

## 1. Los 5 riesgos principales del modelo

**A. Take rate del 15%: es económicamente absurdo para este segmento.**
Un restaurante pequeño trabaja con márgenes de EBITDA del 5–12% y costo de alimentos del 25–35%. Si tu les cobras 15% sobre ingredientes, no les estás vendiendo conveniencia, les estás comiendo la utilidad. Los proveedores locales tampoco tienen margen: muchos operan al 10–20% bruto. Un 15% les quita casi toda la ganancia. Ese número solo funciona si logras **volumen masivo + eficiencia logística + financiamiento**, no con entregas locales chicas.

**B. El problema de la gallina y el huevo es brutal.**
Necesitas suficientes restaurantes para que los proveedores se molesten en subir inventario, y suficientes proveedores para que los restaurantes encuentren todo lo que necesitan. Mientras tanto, nadie tiene liquidez. Si un restaurante entra y no encuentra tomate fresco, cebolla y pollo el mismo día, no vuelve. Si un proveedor entra y no vende rápido, abandona.

**C. WhatsApp ya es el marketplace ganador.**
En LATAM, el 80% de estos pedidos ya se hacen por WhatsApp: confianza personal, precio negociable, crédito de 7–15 días, entrega flexible, relación directa. Tu “solución digital” compite contra una herramienta gratis, universal y con relaciones humanas incrustadas. No es un bug, es el producto real.

**D. Logística de última milla de productos perecederos.**
Ingredientes frescos no son paquetes de Amazon. Necesitas cadena de frío, entregas a primera hora, control de calidad, peso exacto, devoluciones por merma. Si un restaurante recibe verdura en mal estado una vez, pierdes la cuenta para siempre. Y tú eres responsable, no el proveedor.

**E. Morosidad y flujo de caja.**
Los restaurantes pequeños no pagan de contado. Exigen crédito de 15–30 días. Los proveedores locales no pueden esperar. Si tú actúas como intermediario, te comes el riesgo crediticio. ¿Tienes capital para financiar eso? ¿Un seguro contra impagos? ¿Cobranza? Si no, tu plataforma colapsa en el primer mes.

---

## 2. ¿Por qué podría NO funcionar específicamente en LATAM?

- **Economía informal y evasión fiscal.** Muchos proveedores no quieren facturar ni dejar rastro digital. Una plataforma los expone al fisco. Te dirán que sí, pero te pedirán “facturar a otro lado” o “cobrar afuera”.
- **Cultura del crédito y la confianza personal.** El dueño del restaurante compra al proveedor porque lo conoce, le fiado y le resuelve. Una app no reemplaza eso fácilmente.
- **Baja bancarización y preferencia por efectivo.** Pagar con tarjeta/digital tiene costos, fricción y desconfianza. El proveedor quiere efectivo o transferencia directa. Tú metido en medio generas fricción y costo.
- **Ciudades caóticas y costo logístico.** El tráfico, la inseguridad, las calles sin nombre y la falta de densidad comercial hacen que la entrega de última milla sea cara e inconsistente. No hay DoorDash barato aquí.
- **Alta mortalidad de restaurantes pequeños.** El churn natural del cliente es enorme. Cerraron 30% de los restaurantes independientes en muchas ciudades post-pandemia. Tu CAC se va a la basura cada vez que cierra uno.
- **Competencia no digital barata.** Mercados mayoristas, central de abastos, camiones de la Central, proveedores que pasan a dejar catálogo. Son rápidos, baratos y no cobran comisión.

---

## 3. ¿Qué tendría que ser verdad para que funcione? (Key assumptions)

Para creerte, necesito que demuestres que:

1. **Los restaurantes están dispuestos a pagar más por comprar digitalmente.** No solo decirlo: que paguen repetidamente un premium real sobre su opción actual.
2. **Hay proveedores locales con capacidad real de escalar.** No solo la tía que vende queso en el mercado. Necesitas proveedores que puedan surtir 10–50 restaurantes con calidad y precio estable.
3. **La densidad geográfica es suficiente.** Restaurantes y proveedores concentrados en una zona pequeña para hacer la entrega barata y rápida (menos de 30 min o entregas programadas eficientes).
4. **Puedes operar con un take rate sostenible.** Probablemente no 15%, sino 3–7%, y aún así con volumen. O cobrar SAS al restaurante, o monetizar al proveedor por leads/ads/logística.
5. **Puedes resolver el crédito sin morosidad masiva.** Ya sea con fondeo, scoring o cobranza efectiva.
6. **La calidad y cumplimiento son mejores que WhatsApp.** Si no, no hay retención.
7. **El AOV (ticket promedio) es alto y frecuente.** Menos de 3 pedidos/semana por restaurante y no hay negocio.

---

## 4. Escenario de fracaso rápido: ¿cómo y por qué?

**Los primeros 6–9 meses vas a quemar dinero armando la app “bonita”**, contratas equipo tech, integras pasarelas de pago y logística.

Lanzas con 15% de comisión. Los restaurantes entran por curiosidad o descuento inicial. Hacen 1–2 pedidos. Descubren que:

- Algunos productos no están disponibles.
- El precio con comisión es más caro que su proveedor de confianza.
- La entrega llega tarde o en mal estado.
- No pueden pedir fiado.

Los proveedores se frustran porque:

- La plataforma les quita margen.
- Les exige fotos, precios actualizados y entregas puntuales para los que no están equipados.
- Les pagan tarde o con retenciones.

Al mes 6, la retención de restaurantes es menor al 20%, los proveedores abandonan, tu equipo gasta el 70% del tiempo en soporte manual, y te das cuenta de que vendiste una app a un problema que en realidad es **crédito + logística + relaciones**. Cierras o pivotas a “software para proveedores”, que es otro mercado difícil.

El fracaso no será por falta de demanda, será porque **no lograste que ambos lados paguen suficiente para sostener el modelo**.

---

## 5. Si solo tuvieras $10K para validar, ¿qué haría?

Ni una línea de código. Punto.

**Plan de 45–60 días en un solo barrio o corredor gastronómico:**

- **$0 en app.** Usa WhatsApp Business, Google Sheets, un formulario de Typeform/Notion y un grupo de WhatsApp.
- **$2K en tiempo tuyo + un becario local.** Que salga a la calle. No anuncios. Puerta a puerta en 15–20 restaurantes pequeños reales.
- **$3K en subsidio operativo.** No para bajar precios a lo loco, sino para cubrir entregas y garantizar SLAs mientras validas.
- **$2K en “crédito piloto” de prueba.** Fondea tú mismo 5–10 pedidos a crédito de 7 días para medir morosidad real.
- **$3K en incentivos/control de calidad.** Muestras gratis, seguimiento de entregas, encuestas de satisfacción.

**Métricas que necesitas demostrar antes de levantar un peso más:**

1. **Repeat rate:** >50% de restaurantes hace 3+ pedidos en 30 días.
2. **Retención de proveedores:** >60% sigue activo después de mes 1.
3. **Take rate real:** Los clientes pagan precio con tu margen incluido, o el proveedor acepta el fee sin quebrar.
4. **Morosidad:** <5% en crédito piloto.
5. **Unit económica:** Costo de entrega + operación < margen bruto por pedido.
6. **AOV y frecuencia:** Ticket promedio >$X (define según ciudad) y ≥2 pedidos/semana.

Si no logras eso con un WhatsApp y una hoja de cálculo, **no la app es el problema: el modelo es el problema**.

---

## Preguntas que te haría cerrando el pitch

- ¿Cuántos restaurantes y proveedores ya tienes firmados con LOI o pedidos reales?
- ¿Por qué un restaurante dejaría de usar WhatsApp con su proveedor de toda la vida para pagarte 15% más?
- ¿Tienes capital para financiar crédito a restaurantes? ¿Cuánto?
- ¿Has hecho un pedido real tú mismo con tu propia plataforma?
- ¿Qué pasa si Mercado Libre, Rappi o un mayorista local entra con logística propia y 0% de comisión?

Mi veredicto provisional: **la hipótesis es débil porque confunde “pérdida de tiempo” con “dolor de pagar”.** El tiempo que gastan llamando no necesariamente lo quieren pagar con dinero. Tienes que probar que sí lo harán, y pronto.

Dime qué has validado hasta ahora y te sigo apretando.