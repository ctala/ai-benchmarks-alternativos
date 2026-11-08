# Claude Opus 5.5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 5.23 | quality: 6.0
- latency_total: 40.841s | tokens_per_second: 90.7
- input_tokens: 288 | output_tokens: 3704

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

# Teardown del competidor

**Advertencia general:** con 6 datos públicos solo se puede dar **rangos**, no cifras. Casi todo lo que sigue es **inferencia**. Marco cada punto así:

- **[DATO]**: lo que viste tú.
- **[INFERENCIA · certeza alta/media/baja]**: lo que deduzco.

---

## 1. Qué sabemos y qué no

| Dato | Lo que sabemos | Lo que NO sabemos |
|---|---|---|
| 2.400 miembros | [DATO] La portada muestra esa cifra | Si son todos de pago, si incluye pruebas gratuitas, accesos regalados, afiliados o equipo |
| $39/mes | [DATO] Precio de lista visible | Plan anual, descuentos de lanzamiento, precios antiguos mantenidos para los primeros miembros |
| 3 posts/semana | [DATO] En el feed público | Actividad dentro de la comunidad, lives, interacción real |
| 60.000 seguidores | [DATO] En una red social | Email, YouTube u otros canales; calidad y nicho de esa audiencia |
| 12 cursos | [DATO] Listados | Cuántos están completos, cuándo se actualizaron por última vez |

**Lo que no sabemos y más pesa:** el **churn** (tasa de bajas). Es lo que define si el negocio está sano, y no se ve desde fuera.

---

## 2. ¿Cuánto factura?

### Techo matemático
2.400 × $39 = **$93.600/mes** (~$1,1M/año).
[INFERENCIA · certeza alta] **Es un techo, no una estimación.** Es casi seguro que la cifra real es menor, porque es raro que el 100% de los miembros mostrados pague el precio completo.

### Escenarios

| Escenario | % que paga | Precio medio efectivo | MRR | Anual aprox. |
|---|---|---|---|---|
| Pesimista | 40% | $30 | ~$29.000 | ~$350K |
| **Base** | 65% | $33 | **~$51.000** | **~$620K** |
| Optimista | 90% | $38 | ~$82.000 | ~$980K |

**Supuestos (todos inferidos, certeza media-baja):**
- El precio medio efectivo baja por planes anuales con descuento, cupones y miembros antiguos con precio menor.
- El "% que paga" refleja que muchos contadores de plataformas incluyen pruebas gratuitas o accesos regalados. **Esto depende de la plataforma concreta; verifícalo.**
- Faltan las comisiones de plataforma y pasarela de pago (típicamente un porcentaje de un dígito, más una cuota fija).

**Mi lectura [INFERENCIA · certeza media]:** probablemente sea un negocio de **$30K–$80K/mes**, con el escenario base como el más razonable. No me jugaría nada a una cifra concreta.

---

## 3. ¿Qué tan sano es?

### Señales positivas
- **Conversión de audiencia notable.** 2.400 miembros sobre 60.000 seguidores es un 4%. [INFERENCIA · certeza media] Es alto para una red social. Caben tres explicaciones:
  - (a) mucha confianza en el fundador;
  - (b) otros canales de captación que no viste (email, YouTube, SEO);
  - (c) el contador incluye miembros que no pagan.
  
  Las tres son plausibles.
- **Estructura de costes probablemente ligera.** [INFERENCIA · certeza media-alta] Una comunidad de contenido suele tener márgenes altos si el equipo es pequeño. Es probable que sea rentable.

### Señales de riesgo
- **Dependencia del fundador.** [INFERENCIA · certeza media-alta] La audiencia está ligada a su persona. Si deja de publicar, la captación probablemente cae.
- **Presión de churn.** [INFERENCIA · certeza baja en la cifra, alta en la lógica] Las comunidades de pago mensual suelen perder un porcentaje relevante de miembros cada mes. Si su churn fuera del 10% mensual, necesitarían unos 240 miembros nuevos al mes **solo para no decrecer**. Eso los obliga a captar sin parar.
- **"Deuda de promesas" en los cursos.** [INFERENCIA · certeza baja] 12 cursos listados sin saber cuántos están terminados puede indicar contenido a medias. En comunidades, eso suele traducirse en frustración y bajas.
- **Ritmo de contenido modesto.** [INFERENCIA · certeza baja] 3 posts semanales en público no dicen mucho del valor interno, pero tampoco sugieren un equipo grande.

**Veredicto [INFERENCIA · certeza media]:** probablemente es un negocio rentable y real, pero frágil. Depende del fundador y de captar constantemente. Su salud real depende del churn, que desconocemos.

---

## 4. Cómo verificar (barato y en pocas semanas)

1. **Pagar un mes ($39).** Es la inteligencia más barata que vas a conseguir. Revisa:
   - si hay plan anual y su precio;
   - el estado real de los 12 cursos;
   - la actividad interna;
   - el onboarding;
   - qué piden y de qué se quejan los miembros.
2. **Hacer capturas semanales del contador de miembros** durante 4–8 semanas. El crecimiento neto te da una pista indirecta del balance entre altas y bajas.
3. **Usar Wayback Machine** para ver cifras y precios históricos. Así sabrás su ritmo de crecimiento y si subieron el precio, lo que implicaría miembros antiguos con precio menor.
4. **Medir el engagement por post** (comentarios frente a miembros). Si 2.400 miembros generan 5 comentarios por post, muchos están inactivos, y los inactivos son futuras bajas.
5. **Revisar si el fundador ha publicado hitos** ("llegamos a $X MRR"). Algunos lo hacen.
6. **Buscar reseñas y menciones** en Reddit, X y foros: quejas recurrentes, motivos de cancelación.

---

## 5. Cómo competirles

[INFERENCIA · recomendaciones estratégicas, no datos]

**No compitas en precio como estrategia principal.** $39 ya es accesible, y bajar a $29 te da poco margen y poca diferenciación.

**Ataca sus probables debilidades:**

1. **Especialización.** Ellos son "automatización" en general. Tú puedes ser "automatización para [agencias / ecommerce / contables / un tool concreto]". Un nicho claro convierte mejor y retiene más.
2. **Resultados, no contenido.** Si sus cursos están incompletos, tu propuesta puede ser:
   - menos cursos, todos terminados;
   - rutas con resultado concreto ("tu primera automatización funcionando en 14 días");
   - plantillas listas para usar.
3. **Atención que su escala no permite.** Con 2.400 miembros y dependencia del fundador, el acceso personal es escaso. Puedes ofrecer:
   - revisiones de casos;
   - sesiones en vivo con grupos pequeños;
   - respuesta garantizada.
   
   Esto justifica incluso un precio **más alto**.
4. **Retención como foco.** Si su debilidad es el churn, la tuya debe ser la fortaleza: onboarding guiado, hitos y comunidad activa.

**Tu cuello de botella real:** ellos tienen 60.000 seguidores y una máquina de captación. Antes de pensar en el producto, pregúntate **cuál es tu canal de distribución**. Sin audiencia propia, el mejor producto no compite.

---

**Siguiente paso recomendado:** paga un mes y empieza las capturas semanales del contador hoy. En 30 días podrás reemplazar la mitad de mis inferencias por datos, y afinar la estimación de facturación de forma considerable.