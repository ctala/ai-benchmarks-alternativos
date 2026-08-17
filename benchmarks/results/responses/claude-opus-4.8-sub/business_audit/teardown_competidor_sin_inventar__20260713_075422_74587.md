# Claude Opus 4.8 (suscripción) — business_audit/teardown_competidor_sin_inventar

- model_id: `claude-opus-4-8`
- success: True  | final: 4.15 | quality: 4.8
- latency_total: 165.059s | tokens_per_second: 60.9
- input_tokens: 4 | output_tokens: 10047

## Respuesta completa

# Teardown: comunidad de automatización, $39/mes

## Veredicto en 30 segundos

Con lo que me diste, **el rango honesto de facturación es $2.000 – $90.000 MRR**. Un rango de 45x no es un estimado: es una confesión de ignorancia. No es un problema de método, es que falta **un solo dato** que colapsa todo el rango.

Ese dato es: **¿los 2.400 miembros pagan, o son gratis?**

Todo lo demás (posts, cursos, seguidores) es ruido comparado con eso. El resto de este teardown va a: (1) separar lo que sé de lo que infiero, (2) darte los dos escenarios con su aritmética, (3) decirte cómo conseguir ese dato en una tarde, (4) cómo compites en cualquiera de los dos casos.

---

## 1. Lo que SÉ vs lo que INFIERO vs lo que NO se puede saber

| Afirmación | Estatus | Certeza |
|---|---|---|
| Muestra "2.400 miembros" en portada | **DATO** (lo viste) | Alta |
| Precio listado: $39/mes | **DATO** | Alta |
| 12 cursos listados | **DATO** | Alta |
| 3 posts/semana en el feed público | **DATO** | Alta |
| Fundador: 60.000 seguidores | **DATO** | Alta |
| Los 2.400 son **miembros totales, no pagadores** | **INFERENCIA** | Media (55-65%) |
| El feed público es marketing, no salud comunitaria | **INFERENCIA** | Media-alta |
| Los 12 cursos incluyen contenido desactualizado | **INFERENCIA** | Media-alta (en automatización el contenido caduca en 12-18 meses) |
| Su facturación real | **NO SE PUEDE SABER desde fuera** | — |
| Su churn mensual | **NO SE PUEDE SABER desde fuera** | — (y es LA variable del negocio) |
| Cuántos cursos están terminados | **NO SE PUEDE SABER sin entrar** | — |
| Si hay plan anual / descuentos | **NO SE PUEDE SABER sin llegar al checkout** | — |

Nota importante: **no sé qué plataforma es** (dijiste "tipo membresía"). Las mecánicas cambian mucho el cálculo. En una plataforma con paywall duro, el contador de miembros ≈ pagadores activos. En una plataforma freemium o en un grupo gratis con upsell, el contador ≈ gente que se registró alguna vez. Es la diferencia entre $90K y $4K.

---

## 2. Los dos escenarios

### Escenario A — Paywall duro (los 2.400 pagan)
- Bruto: 2.400 × $39 = **$93.600 MRR**
- Ajustes que **siempre** bajan la cifra: plan anual con descuento (típico 20-40% de la base), founders grandfathered a precio viejo, cuentas comped, fees de plataforma+pasarela (~5%).
- MRR neto realista: **$73.000 – $85.000**. ARR ~$900K–$1M.
- **Probabilidad que le asigno: ~30%.**

### Escenario B — Comunidad gratis / freemium, $39 es el tier pago
- Conversión free→paid típica en comunidades: 2-10%.
- 2.400 × 2-10% = 48 a 240 pagadores.
- MRR: **$1.900 – $9.400**. Centro ~$4.700.
- **Probabilidad: ~55%.**

### Escenario C — Contador inflado/acumulado (incluye gente que ya se fue)
- MRR: **$10.000 – $40.000**. **Probabilidad: ~15%.**

### El cruce que me hace inclinarme a B

60.000 seguidores → 2.400 **pagadores** = **4,0% de conversión seguidor→suscripción recurrente**. Eso sería excepcional. La banda normal para una oferta low-ticket es 0,5-1,5%, y 2% ya es muy bueno.

60.000 seguidores → 2.400 **registros gratis** = 4% de conversión seguidor→miembro gratis. Eso es completamente normal, incluso bajo.

[INFERENCIA, certeza media] El Escenario A solo cuadra si tienen fuentes de tráfico que no estás viendo: publicidad pagada, una lista de email mayor que su base de seguidores, YouTube/podcast con alcance real muy superior, o 3+ años acumulando. Que es posible. Por eso no descarto A, solo le pongo menos peso.

---

## 3. Qué tan sano es el negocio (lectura de las señales visibles)

**3 posts/semana en el feed público → señal neutra, probablemente marketing.**
[INFERENCIA, certeza media-alta] El feed público de una comunidad es escaparate. La salud no se mide en posts del fundador, se mide en **posts de miembros y comentarios por post**. Si esos 3 posts son del equipo, es una comunidad que hay que **alimentar** — eso es costo, no salud. Si hay hilos de miembros con 10+ comentarios reales, ahí sí hay algo vivo.

**12 cursos → es un pasivo disfrazado de activo.**
[INFERENCIA, certeza media-alta] "12 cursos" es un pitch de cantidad, y en automatización el contenido se pudre rápido: cambian las APIs, cambian las herramientas, cambian los precios de los SaaS. Un curso de hace 18 meses no es neutro, es **peor que no tenerlo** (le haces perder la tarde al miembro). Que no se vea cuántos están terminados es en sí una señal: **si estuvieran todos terminados, lo dirían.**

**Churn → invisible, y es el negocio entero.**
En membresías de $39/mes de este tipo, el churn mensual típico va de 5% a 12%. A 8%, la vida media del cliente es ~12,5 meses y el LTV ≈ **$490**. Eso define todo: cuánto pueden pagar por adquirir, y si crecen o solo reemplazan.

**La verdad incómoda:** una comunidad puede mostrar 2.400 miembros y estar perdiendo dinero, y otra puede tener 200 y ser rentable. El número de portada no dice nada sobre salud. **Lo único que la delata desde fuera es la curva de crecimiento neta**, y eso sí lo puedes conseguir (siguiente sección).

---

## 4. Cómo conseguir los datos que faltan (2-3 horas de trabajo, sin adivinar)

En orden de rentabilidad:

1. **Busca si el fundador ya dijo su MRR.** Podcasts, entrevistas, hilos de "cómo llegué a X". La mayoría de los fundadores de comunidades lo han dicho en algún lado. Es la fuente más barata y la gente la salta para ponerse a estimar.
2. **Wayback Machine sobre la página de la comunidad.** Captura el contador de miembros en 5-6 fechas (hace 24, 18, 12, 6, 3, 1 mes). Eso te da el **crecimiento neto mensual**. Si está plano → están reemplazando churn, no creciendo. Es el mejor proxy de salud que existe desde fuera.
3. **Llega hasta el checkout.** ¿Te pide tarjeta obligatoriamente, o hay trial/tier gratis? Esa sola observación decide entre Escenario A y B. De paso ves si existe plan anual y con qué descuento (un descuento anual agresivo = están priorizando caja y retención, señal de presión de churn).
4. **Biblioteca de anuncios de Meta** (buscar por el nombre de la página). ¿Corren ads? ¿Hace cuánto lleva vivo el mismo creativo? Un creativo corriendo 3+ meses significa que **les cierran los números** — eso sube la probabilidad del Escenario A y te dice que compiten con presupuesto, no solo con orgánico.
5. **Si puedes entrar (gratis o trial):** cuenta (a) posts de miembros vs. de staff en los últimos 30 días, (b) comentarios promedio por post, (c) fecha de última actualización de los cursos, (d) cuántos cursos están realmente completos.
6. **Busca exmiembros.** Nombre de la comunidad + "cancelé" / "vale la pena" / "refund" en Reddit, YouTube, X. Los que se fueron te dicen exactamente dónde está el hueco. Es tu mapa de ataque.
7. **Tamaño del equipo** (LinkedIn, página de "about"). Un equipo de 5 personas no sobrevive con $5K MRR. El tamaño del equipo te pone un **piso** a la facturación.

---

## 5. Cómo les compites

Esto aplica en cualquiera de los dos escenarios, porque ataca lo que es estructuralmente débil en su modelo, no su tamaño.

**No pelees por número de cursos.** Su "12 cursos" es su deuda técnica. Tu jugada es lo opuesto: **menos cursos, todos vigentes, con fecha de última actualización visible**. En automatización, "Actualizado en {mes} {año}" vale más que "12 cursos". Es un diferenciador barato para ti y carísimo para ellos (tienen 12 cosas que mantener, tú 4).

**No pelees por distribución.** 60.000 seguidores te llevan años. Si intentas ganar arriba del embudo, pierdes. Lo que sí puedes hacer es **estrechar el nicho**: ellos son "automatización" genérico. Tú eliges un ICP (automatización para agencias, para e-commerce, para founders solos) y en ese segmento eres obviamente mejor. Ellos no pueden seguirte ahí sin canibalizar su promesa amplia.

**No bajes el precio.** Si entras a $19 para competir con $39, atraes precisamente al segmento que más churnea. Dos caminos viables:
- **Arriba:** más caro, con contacto real (cohorte, revisión de workflows, Q&A). Vendes resultado, no acceso.
- **Freemium agresivo:** regalas lo que ellos cobran (los fundamentos) y cobras por lo que ellos no dan (implementación, plantillas vivas, soporte). Tu batalla pasa a ser conversión free→paid, no tráfico — que es una pelea que puedes ganar sin 60.000 seguidores.

**Ataca su punto ciego estructural: el miembro nuevo se siente solo.** Una comunidad de 2.400 se siente vacía para el que llega. Tu ventaja de ser pequeño es la única que no pueden copiar: **onboarding humano, respuesta del fundador, primer resultado en 7 días.** Vende "vas a hacer que funcione", no "vas a tener acceso a".

**Pon en público lo que ellos no pueden mostrar.** Ellos publican miembros y cursos. Tú publica **resultados**: workflows en producción, horas ahorradas, casos con cifras. Cambias el eje de la comparación de "quién tiene más" a "quién hace que funcione", y en ese eje empiezas empatado.

---

## 6. Qué medir para saber si les estás ganando

No mires tu MRR contra el suyo (no lo conoces). Mide:

1. **Conversión free→paid** — el único número que decide si tu negocio escala.
2. **Churn a 1 y 3 meses** — a $39/mes, esto es el negocio.
3. **Time-to-first-win** del miembro (días hasta su primera automatización funcionando). Es el predictor de churn y es tu arma frente a ellos.

Y estas son las señales de que **ellos** están en problemas (búscalas cada 60 días):
- El contador de miembros se aplana en Wayback.
- Aparecen descuentos, "lifetime deals" o promociones agresivas → presión de caja.
- El fundador pivota a coaching high-ticket → la membresía no da.
- El fundador empieza a publicar más sobre la comunidad que sobre automatización → está alimentando un embudo que no se llena solo.

**Lo que te diría que son fuertes de verdad:** hilos de miembros con conversación real, plan anual empujado en el checkout, subidas de precio en el tiempo, testimonios con fecha y cifras concretas.

---

**Resumen honesto:** no puedo decirte cuánto facturan, y nadie que solo haya visto esa página puede. Lo que sí puedo decirte es que la respuesta depende de **una** pregunta (¿pagan los 2.400?), que esa pregunta se contesta llegando al checkout, y que **tu plan de competencia es el mismo en los dos casos** — porque no atacas su tamaño, atacas su mantenimiento, su nicho amplio y su soledad interna.