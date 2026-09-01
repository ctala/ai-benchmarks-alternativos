# GLM 5.3 Flash — strategy/business_model_validation

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 178.074s | tokens_per_second: 42.1
- input_tokens: 185 | output_tokens: 7497

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

# Primero, el número que mata todo antes de empezar

**El 15% no cierra con nadie. Haz la matemática:**

- Restaurante pequeño en LATAM gasta ~$3.000–6.000 USD/mes en insumos. Comisión del 15% = **$450–900/mes**.
- La utilidad neta típica de esos restaurantes es 3–8% de ventas. Con ventas de $15–25K/mes, su utilidad es $450–2.000/mes. **Tu comisión puede comerse entre el 25% y el 100% de toda su utilidad.**
- Del lado del proveedor: una distribuidora de alimentos opera con margen bruto de 10–20%. Le estás pidiendo entregar su margen completo. O más.

El 15% es un número de marketplace B2C (App Store, Uber Eats) copiado a un contexto donde nadie tiene ese margen. Y ojo: Uber Eats cobra 15–30% porque genera *ingresos incrementales* (clientes nuevos para el restaurante). Tú cobras 15% sobre un *costo*. Son psicologías opuestas.

Pregunta directa: **¿de dónde sacaste el 15%?** Si la respuesta es "es el estándar de marketplaces", es una señal de que aún no has hecho el análisis de quién absorbe el fee.

---

## 1. Los 5 riesgos principales

**1. Desintermediación inmediata.** La comida es una compra repetitiva y relacional. Después del primer match, restaurante y proveedor se intercambian WhatsApps y nunca vuelven a tu plataforma. Tú te conviertes en una herramienta gratuita de descubrimiento.

**2. Tu competidor real no es "llamar a proveedores".** Es WhatsApp + el vendedor de la distribuidora que visita cada semana + crédito a 30–60 días + la flexibilidad de negociar precio en el momento. Ese sistema informal ya funciona. Estás compitiendo contra una relación, no contra una fricción.

**3. La hipótesis del dolor es probablemente falsa.** Los restaurantes pequeños tienen 2–4 proveedores de confianza y ordenan por WhatsApp en 15 minutos. No "pierden tiempo llamando a múltiples proveedores". El dolor real es **volatilidad de precios, acceso a crédito y consistencia de calidad** — no tiempo. Estás resolviendo el problema menos doloroso porque es el más fácil de resolver con software.

**4. Perecederos + oferta fragmentada = infierno operativo.** ¿Quién come los tomates golpeados? ¿Quién actualiza los precios cuando cambian a diario? ¿Quién garantiza entrega? Los proveedores pequeños no van a mantener catálogos; terminarás haciéndolo manualmente, y en ese momento ya no eres un marketplace, eres un distribuidor digital con todos sus costos.

**5. Cold start por ciudad sin economías de escala.** Cada ciudad reinicia el problema de liquidez. Comisión promedio por orden: $15–30. Necesitas volumen masivo solo para pagar operación, soporte y pagos.

---

## 2. Por qué LATAM es peor, no mejor

- **Informalidad.** Gran parte de proveedores y restaurantes no facturan. Una comisión formal del 15% implica transacciones formales, impuestos, precios que suben. El canal informal no tiene ese costo.
- **WhatsApp es el incumbente, y es gratis.** Estás cobrando por algo que ya hacen gratis.
- **Cultura del fiado.** Si exiges prepago, mataste la feature más valiosa del canal actual: el crédito. Si ofreces crédito tú, felicidades: ahora eres una fintech con riesgo de mora sobre restaurantes pequeños, que es de los peores activos de crédito que existen.
- **Los mercados centrales.** En Bogotá, Lima, CDMX, el dueño o el chef va personalmente al mercado central a las 5 AM. Eso no es solo compra: es control de calidad, negociación y networking. Tu app compite contra eso.
- **El precedente que te van a meter por la garganta:** Frubana levantó cientos de millones (SoftBank, Tiger) para exactamente esta tesis y terminó recortando y pivoteando. Choco levantó montañas de capital para digitalizar pedidos restaurante-proveedor y cambió de modelo varias veces. La pregunta brutal: **¿qué sabes tú que no sabían ellos con 500 veces tu capital?**

---

## 3. Qué tendría que ser verdad (asunciones falsables)

1. **Alguien paga ≥5% — no 15% — sin abandonar la plataforma.** Incluso 5% hay que demostrarlo con dinero real, no con "sí, claro que pagaría".
2. **El dolor #1 es tiempo, no precio o crédito.** Si en entrevistas el dolor #1 resulta ser otro (y lo será), tu wedge colapsa.
3. **Los proveedores publican precios reales y los mantienen.** Hoy guardan precios como secreto comercial y los negocian uno a uno.
4. **Ninguna de las partes se salta la plataforma tras el match.** Esto requiere que controles pagos, entrega o crédito — es decir, que dejes de ser marketplace.
5. **Frecuencia × ticket × take rate > CAC + costos operativos.** Pon el número real. Con take rate de 5%, ticket de $150 y 8 órdenes/mes, generas $60/mes por restaurante. ¿Cuánto cuesta adquirirlo y servirlo?
6. **Puedes resolver pagos sin destruir el crédito informal.** Nadie ha resuelto esto bien en el sector.

---

## 4. El escenario de fracaso rápido

Semana 1–4: logras onboardear 40 restaurantes y 15 proveedores. Hay euforia inicial.

Semana 5–8: los restaurantes descubren que los precios en plataforma son *más altos* (el proveedor infló precios para cubrir tu comisión) o que su proveedor de confianza no está. Algunos te usan para comparar precios y luego negocian a la baja con su proveedor actual usando *tu data*. Los proveedores se dan cuenta de que les estás cobrando 15% por clientes que ya eran suyos.

Semana 9–12: ambas partes se intercambian WhatsApps. GMV se desploma. Los que quedan son los de peor calidad, porque los buenos ya se fueron directos. Muerte por desintermediación en ~90 días, y de regalo entrenaste al mercado para negociar mejor contra sus proveedores.

---

## 5. Los $10K

**Cero en app.** WhatsApp + Google Sheets + tu tiempo.

**Semanas 1–2: 40 entrevistas** (20 restaurantes, 20 proveedores). Cero preguntas hipotéticas. Solo comportamiento: "Cuéntame tu última compra. ¿Qué compraste, a quién, cuánto costó, qué salió mal, qué hiciste?" Mide: ¿cuántos proveedores usan realmente? ¿Cuánto tiempo semanal toma? ¿Cuál es su dolor #1 *sin que tú lo sugieras*?

**Semanas 3–8: concierge en UNA zona.** 10–15 restaurantes te mandan su pedido semanal por WhatsApp. Tú lo armas manualmente con 3–5 proveedores. **Cobras comisión real desde el día 1** — prueba 5%, no 15%. Efectivo o transferencia. Si nadie paga, no hay negocio, sin importar cuánto "les guste la idea".

**Criterios de kill definidos ANTES de empezar:**
- A la semana 6, ¿+40% de restaurantes reordenó ≥3 veces sin que les insistas?
- ¿Cobraste ≥5% sin descuentos ni excepciones?
- ¿Algún proveedor cumplió precios y entregas de forma consistente?
- ¿Alguien intentó irse directo? (Van a intentar. La pregunta es cuántos.)

Si fallas dos de estas cuatro, mata el marketplace. Pero los datos te dirán hacia dónde pivotar: **(a)** herramienta de pedidos SaaS para proveedores, **(b)** agregación de demanda para comprar directo a productores (negocio de distribución, no marketplace), **(c)** crédito a restaurantes — probablemente donde está el dinero real, **(d)** marketplace *curado* de productores especiales/locales para restaurantes de gama media-alta, donde el valor es diferenciación de menú y el ticket lo justifica.

---

**La verdad incómoda:** tal como está planteada — marketplace genérico de insumos con 15% — esto está muerto antes de nacer, y no por ejecución sino por matemática. Lo interesante de tu idea no es el marketplace; es lo que se esconde debajo: crédito, agregación o curaduría. Ve a validar con $10K y dinero cambiando de manos. Si el dolor real aparece donde no lo buscabas, escúchalo.