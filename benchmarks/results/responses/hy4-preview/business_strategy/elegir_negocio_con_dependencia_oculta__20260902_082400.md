# Tencent Hy4 preview — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.25 | quality: 10.0
- latency_total: 174.394s | tokens_per_second: 54.5
- input_tokens: 365 | output_tokens: 9504

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres asesor de fundadores. Eliges por lo que se puede EJECUTAR con los activos actuales, no por el tamaño del mercado en una diapositiva.

**user:**

Tengo que elegir en qué me enfoco los próximos 3 meses. Soy uno solo, 4 horas al día, y necesito ingresos ANTES de que se me acabe el colchón (me quedan 3 meses de caja).

OPCIÓN A — Vender datos vía API a empresas.
  Mercado: enorme. Ticket: $500-2.000/mes por cliente.
  Requisito: contratos B2B con empresas. Mi ciclo de venta B2B histórico es de 5 a 7 meses desde el primer contacto hasta el cobro.
  Producto: habría que construirlo (~6 semanas).

OPCIÓN B — Marca blanca de mi tecnología para agencias.
  Mercado: mediano. Ticket: $300/mes.
  Requisito: necesito 3 casos de éxito documentados para que alguien me compre. Hoy tengo 0.

OPCIÓN C — Contenido patrocinado en el medio que ya opero.
  Mercado: chico. Ticket: $400-800 por pieza.
  Requisito: ya tengo el tráfico y la audiencia. Ya me escribieron 2 marcas preguntando precios el mes pasado (no les respondí).
  Producto: no hay que construir nada.

¿Cuál agarro? Justifica.


## Respuesta completa

**Veredicto: Opción C. Ahora. Hoy mismo les respondes a esas dos marcas.**

No elijas por tamaño de mercado. Elige por **tiempo a caja con los activos que ya tienes**. Con 3 meses de colchón, trabajando solo y 4h/día, tienes apenas ~240–340 horas en total. Cualquier cosa que no te ponga dinero en el banco en menos de 12 semanas es una distracción mortal.

---

## El filtro que mata a A y B

### Opción A — Datos vía API (mercado enorme, ticket alto): la trampa de la diapositiva
- Hay que **construir ~6 semanas**.
- Tu **ciclo B2B histórico es de 5 a 7 meses** desde el primer contacto hasta el cobro.
- Cuenta realista: 6 semanas de build + 5–7 meses de ciclo = **8–9 meses para el primer dólar** (y eso si empiezas a vender hoy; si construyes primero, peor).
- Aunque el ticket sea $2.000/mes, un cliente que cobras en 9 meses no paga tus gastos del mes 3.
- Solo, con 4h/día, no puedes construir una API y además vender a empresas.

**Veredicto:** no es ejecutable en tu ventana. Mueres antes de cobrar.

### Opción B — Marca blanca para agencias: parece cerca, pero te falta prueba
- Ya tienes la tecnología, sí. Pero necesitas **3 casos de éxito documentados** y hoy tienes **0**.
- Para conseguirlos tienes que regalar o pilotar la tecnología, esperar a que la usen, medir resultados y escribir los casos. Mínimo **6–10 semanas**.
- Después aún hay que vender a agencias. Con un ticket de **$300/mes**, aunque cierres 3–5 agencias en el mes 3 son $900–$1.500 MRR… y llegas justo al filo, habiendo gastado casi todas tus horas.
- En tu propio historial, conseguir la prueba social no es inmediato.

**Veredicto:** no es una fuente de caja a 90 días. Es un proyecto de validación para más adelante.

### Opción C — Contenido patrocinado: la única que pasa el filtro
- **Activo ya existe:** tráfico y audiencia. No hay que construir nada.
- **Demanda ya existe:** 2 marcas te escribieron preguntando precios. Eso es pipeline tibio. (No responderles fue dejar dinero en la mesa.)
- **Ciclo corto:** se cierra en días/semanas, no meses.
- **Ticket suficiente:** $400–800 por pieza. Si cierras esas 2 marcas, son **$800–$1.600 en semanas 1–2**.
- **Cabe en tus horas:** ya operas el medio; producir una pieza patrocinada es contenido con un brief. Con 4h/día puedes vender y producir varias piezas al mes.
- El mercado sea “chico” es irrelevante: no necesitas un mercado de $1B para sobrevivir 3 meses, necesitas **transacciones ahora**.

---

## Plan de ejecución (próximos 90 días, foco absoluto en C)

1. **Días 1–3:** Responde a las 2 marcas. Ten listo un **media kit de 1 página** (audiencia, tráfico, formatos, precios). Cierra rápido; pide 50% por adelantado o pago contra publicación.
2. **Semana 1:** Publica un **rate card** claro:  
   - 1 pieza: $600  
   - Paquete 3 piezas: $1.500  
   - Newsletter + pieza: $800  
   Ancla alto; si hay demanda, subes.
3. **Semanas 1–4:** Prospección enfocada. Haz una lista de **30–50 marcas/agencias** que ya anuncien en medios de tu nicho o encajen con tu audiencia. Email corto: *“tengo X visitas/mes, audiencia de Y, formatos Z. ¿Hablamos?”*. Objetivo: **2–4 cierres en el primer mes**.
4. **Mes 2–3:** Convierte piezas sueltas en **retainers** (“3 piezas al mes por $1.500/mes”). El retainer te da previsibilidad y te quita la presión de vender cada semana.
5. **Estandariza:** plantilla de brief, calendario, aprobación del sponsor. Que una pieza patrocinada te tome **3–5 horas, no 15**.

---

## Qué hago con A y B

- **A:** Olvídala por ahora. No construyas. Como máximo, haz 5–10 entrevistas de validación (sin escribir código) para tener el aprendizaje listo cuando tengas 6+ meses de caja. Pero no gastes tus 4h/día en build.
- **B:** Es tu siguiente paso, no tu primer paso. Cuando ya factures con C y tengas relación con agencias (muchas agencias compran patrocinio y también necesitan tecnología), ofréceles la white-label como piloto gratis/descuento a cambio de caso de éxito. Ahí consigues los 3 casos y luego vendes. Eso es para el mes 4+.

---

## Regla para decidir

Si necesitas caja en <90 días, el filtro no es TAM ni ticket: es  
**(1) ¿tengo el activo hoy?, (2) ¿puedo cobrar en semanas?, (3) ¿cuántas horas me roba?**

Solo la **C** pasa las tres.

Compra tiempo con C. Después, con caja y casos, atacas B y luego A.  
El orden es **C → B → A**. Nunca A primero.