# Claude Haiku 4.5 — strategy/business_model_validation

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 19.633s | tokens_per_second: 104.3
- input_tokens: 215 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación exhaustiva y perspicaz de los riesgos y desafíos específicos del modelo de negocio en LATAM.

## Respuesta completa

# Análisis VC Escéptico - Tu Marketplace de Restaurantes

## 1. Los 5 Riesgos Principales

**Riesgo #1: Problema que no duele lo suficiente**
- Los restaurantes pequeños ya tienen proveedores. Sí, es ineficiente, pero funciona.
- El costo de cambiar (aprender sistema, probar nuevos proveedores, riesgo de falla) > el tiempo ahorrado.
- "Perder tiempo llamando" no es un problema existencial. Es molesto, no es urgente.

**Riesgo #2: Márgenes de transacción insostenibles**
- 15% es muy agresivo para un marketplace B2B sin network effect establecido.
- Los restaurantes van a presionar: "¿Por qué pago 15% si puedo llamar directo?"
- Los proveedores dirán: "Prefiero vender directo y evitar la comisión."
- Te quedas en el medio siendo innecesario.

**Riesgo #3: Calidad y confiabilidad = muerte**
- Un restaurante necesita ingredientes mañana. Si falla una entrega, cierra su cocina.
- Esto no es como un marketplace de ropa. Una falla = pérdida de clientes del restaurante.
- Necesitas SLA garantizados. Eso requiere capital, operaciones, seguros. No es software.

**Riesgo #4: Proveedores locales no están digitalizados**
- Muchos proveedores en LATAM operan con sistemas legacy o papel.
- ¿Quién integra su inventario? ¿Quién maneja logística? ¿Quién garantiza calidad?
- Si tienes que hacer todo eso, no es un marketplace, es una operación logística.

**Riesgo #5: Dependencia de volumen en mercado fragmentado**
- Cada ciudad/región tiene dinámicas diferentes.
- Necesitas escala local para ser rentable. Pero cada mercado es distinto.
- Terminas con 50 ciudades con 5 restaurantes cada una = inviable.

---

## 2. Por Qué NO Funciona en LATAM Específicamente

**La realidad brutal:**

- **Relaciones > Plataformas**: Los restaurantes tienen relaciones personales con proveedores. "Mi compadre me vende a buen precio." Eso no se disrumpe con UI bonita.

- **Informalidad del 60%**: Muchos proveedores no tienen facturación formal, no pueden estar en plataforma regulada. ¿Cómo cobras comisión si la transacción es informal?

- **Poder de compra fragmentado**: Un restaurante pequeño compra 50kg de tomates. Un proveedor quiere vender 500kg. No hay match. La agregación requiere capital para warehouse.

- **Logística es el cuello de botella**: No es información. Es que alguien tiene que ir a buscar tomates a las 5am. Eso cuesta dinero real. ¿Quién lo paga?

- **Márgenes ya comprimidos**: Los restaurantes pequeños operan con márgenes del 5-10%. No pueden absorber 15% extra en costos. Punto.

- **Confianza en efectivo**: Muchas transacciones en LATAM son en efectivo. Tu plataforma de pagos digitales es una fricción, no una ventaja.

---

## 3. Key Assumptions Que Necesitan Ser Verdad

Si esto funciona, DEBE ser verdad que:

1. **Restaurantes ahorran >20% en costo de ingredientes** (no solo tiempo)
   - De lo contrario, ¿por qué cambiar?
   - ¿Cómo lo haces si proveedores no bajan precio por volumen?

2. **Puedes agregar demanda de 50+ restaurantes en la MISMA zona geográfica**
   - Sin esto, no tienes poder de compra para negociar con proveedores.
   - ¿Cuántos restaurantes hay en un radio de 5km? ¿Cuántos puedes convertir?

3. **Los proveedores están dispuestos a vender a menor precio por volumen garantizado**
   - Pero si garantizas volumen, eres distribuidor, no marketplace.
   - ¿Quién absorbe el riesgo si no se vende?

4. **La logística es resolvible sin capital operacional masivo**
   - ¿Repartes tú? ¿Los proveedores? ¿Los restaurantes?
   - Si los proveedores reparten, ¿por qué te necesitan?

5. **Hay suficientes proveedores competidores en cada zona**
   - Si hay 3 proveedores de tomates en la ciudad, tu marketplace es un catálogo.
   - Necesitas verdadera competencia para crear valor.

---

## 4. Escenario de Fracaso Rápido (Y Por Qué)

**El fracaso más probable ocurre en 6-8 meses:**

**Mes 1-2:** Lanzas en una ciudad. Reclutadores consiguen 30 restaurantes. Se ven emocionados en demos.

**Mes 3:** Descubres que solo 8 hacen compras reales. Los otros "lo van a usar después."

**Mes 4:** Los 8 restaurantes que compran descubren que:
- El proveedor de tomates no tiene variedad que necesitan
- Las entregas llegan 2-3 horas tarde
- El precio no es mejor que lo que pagan directo
- Tienen que pedir por app en vez de llamar (más fricción, no menos)

**Mes 5:** Contactas proveedores. Te dicen:
- "¿15% de comisión? Prefiero vender directo."
- "¿Quién garantiza que se vende? No puedo comprometer inventario."
- "Mis clientes me llaman directo. No necesito plataforma."

**Mes 6:** Burn rate: $15K/mes. Runway: 8 meses. Crecimiento: 0% MoM.

**Mes 7:** Intentas pivotar a "agregador" (tú compras, tú vendes). Necesitas $200K capital. No tienes.

**Mueres.**

---

## 5. Si Solo Tienes $10K, Qué Haría Yo

**No construyo la app. Aún.**

### Semana 1-2: Validación brutal ($500)
- Entrevisto 30 restaurantes pequeños (no demos, preguntas duras)
- Pregunta clave: **"¿Cuánto dinero ahorrarías si tuvieras mejor acceso a proveedores?"**
- Si dicen <5%, STOP. No hay problema.
- Si dicen >15%, continúa.

### Semana 3-4: Validación de supply ($500)
- Contacto 20 proveedores de ingredientes
- Pregunta: **"¿Venderías a través de una plataforma si pierdes el 15% de margen?"**
- Si dicen no, STOP. No hay negocio.
- Si 5+ dicen sí, continúa.

### Semana 5-6: MVP manual ($2K)
- NO construyo software.
- Hago un Airtable/Google Sheets que simula marketplace.
- Manualmente agrego 10 restaurantes + 5 proveedores en UNA zona.
- Manualmente proceso 20 transacciones.

**Objetivo:** Validar que el match existe sin código.

### Semana 7-8: Operación manual ($3K)
- Intento hacer 50 transacciones en 2 semanas.
- Yo mismo soy la "plataforma."
- Mido:
  - % de repetición (¿vuelven a comprar?)
  - Satisfacción (NPS)
  - Margen real (¿15% es viable?)
  - Churn (¿