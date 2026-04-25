# Claude Opus 4.6 — strategy/business_model_validation

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.24 | quality: 9.54
- latency_total: 53.197s | tokens_per_second: 38.5
- input_tokens: 215 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

# 🔴 Due Diligence Brutal: Marketplace de Ingredientes Locales

Voy a destrozar tu idea. No porque sea mala, sino porque si sobrevive a esto, tal vez valga la pena.

---

## 1. Los 5 Riesgos que te Matan

### Riesgo #1: Desintermediación (el clásico "te saltan")
Tu peor pesadilla tiene nombre: **después de la primera transacción, el restaurante y el proveedor intercambian WhatsApp y nunca más te necesitan.** Tu plataforma es un directorio glorificado. ¿Por qué pagarían 15% eternamente por una conexión que ya hicieron?

> **La pregunta incómoda:** ¿Qué haces tú que un grupo de WhatsApp no hace gratis?

### Riesgo #2: Unit Economics Destructivos
Un restaurante pequeño gasta entre **$500-$2,000 USD/mes** en ingredientes. Tu 15% = **$75-$300/mes por restaurante.** Ahora dime:
- ¿Cuánto te cuesta adquirir ese restaurante? (visitas, demos, onboarding)
- ¿Cuánto te cuesta adquirir y retener a los proveedores?
- ¿Cuánto cuesta la operación, el soporte, las disputas?

**Con tickets tan bajos, necesitas MILES de restaurantes activos para que cierre la matemática.** Y cada uno requiere hand-holding.

### Riesgo #3: Problema de Gallina y Huevo (Cold Start)
- Sin proveedores → los restaurantes no ven valor
- Sin restaurantes → los proveedores no se registran
- Necesitas masa crítica en **la misma zona geográfica** (porque los ingredientes son locales)

**Esto no es como Uber que lanzas en toda una ciudad.** Necesitas densidad hiperlocal. Barrio por barrio.

### Riesgo #4: La Comisión del 15% es Insostenible
Los márgenes de un restaurante pequeño son **5-15%.** Le estás pidiendo que pague 15% extra sobre sus ingredientes. Haz la cuenta:

```
Antes:  Compra $1,000 en ingredientes directamente
Ahora:  Compra $1,000 + $150 de comisión = $1,150

Eso es un 15% de incremento en su costo principal.
Para un negocio que ya opera al límite.
```

**¿Por qué no simplemente cobras al proveedor?** Porque el proveedor también tiene márgenes delgados y te va a mandar al diablo. **Alguien tiene que absorber ese 15% y nadie quiere.**

### Riesgo #5: Complejidad Operativa Oculta
Ingredientes perecederos significan:
- Disputas por calidad ("los tomates llegaron podridos")
- Logística de frío
- Ventanas de entrega estrictas (el chef necesita todo a las 6 AM)
- Estacionalidad de precios
- Devoluciones de producto perecedero (¿quién absorbe la pérdida?)

**No estás construyendo un marketplace digital. Estás construyendo una empresa de logística de perecederos disfrazada de app.** Eso es 10x más difícil y más caro.

---

## 2. Por qué LATAM Específicamente te Destruye

### 💀 La cultura del "de confianza"
En LATAM, las relaciones comerciales son **personales.** El dueño del restaurante le compra a Don José porque lo conoce hace 15 años, le fía cuando está corto, le aparta lo mejor, y le manda un extra de cilantro gratis. **Tu app no puede replicar 15 años de confianza.** Y no están buscando optimizar esa relación, la valoran tal como es.

### 💀 Informalidad masiva
- El 60-80% de estos proveedores **no tienen RFC/RUT/NIT formal**
- No emiten facturas
- Cobran en efectivo
- No tienen catálogo digital ni precios fijos (el precio cambia cada mañana según la central de abastos)

**Tu plataforma necesita formalidad. Tu mercado opera en informalidad. Ese gap no se cierra con UX bonito.**

### 💀 Baja digitalización real
Sí, todos tienen smartphone. No, eso no significa que quieran gestionar sus compras en una app. El dueño de la taquería tiene 55 años, se levanta a las 4 AM, y su "sistema" es una libreta. **La fricción de adopción es BRUTAL.**

### 💀 Sensibilidad extrema al precio
En mercados donde la gente regatea por 50 centavos, **cualquier sobrecosto se siente.** No importa cuánto tiempo "ahorras" — si tu plataforma hace que los ingredientes cuesten más, perdiste.

### 💀 Infraestructura de pagos
- Muchas transacciones son en efectivo
- Transferencias bancarias manuales (SPEI, PSE, etc.) sin confirmación automática
- Penetración de pagos digitales en comercio B2B pequeño: bajísima
- **¿Cómo cobras tu 15% si la transacción ocurre en billetes en la puerta trasera del restaurante?**

### 💀 Competencia invisible
No compites contra otra app. **Compites contra el mercado de abastos a 15 minutos**, contra el cuñado que tiene una camioneta y hace entregas, contra el grupo de WhatsApp del barrio donde 30 restaurantes compran juntos para tener volumen.

---

## 3. Key Assumptions — Qué Tiene que ser Verdad

Para que esto funcione, **TODAS** estas cosas tienen que ser ciertas simultáneamente:

| # | Assumption | Nivel de riesgo |
|---|-----------|----------------|
| A1 | Los restaurantes pequeños realmente **sufren** buscando proveedores (no solo es "incómodo", es un **dolor que cuesta dinero**) | 🔴 Alto |
| A2 | Están **dispuestos a pagar** por resolver ese dolor (no solo quieren, pueden) | 🔴 Alto |
| A3 | Los proveedores locales pueden y quieren **digitalizarse** (catálogo, precios, disponibilidad actualizada) | 🔴 Alto |
| A4 | Puedes generar **suficiente valor recurrente** para que no te salten después de la primera conexión | 🔴 Crítico |
| A5 | 15% de comisión es un precio que **ambos lados** aceptan sin destruir sus márgenes | 🟡 Medio-Alto |
| A6 | Puedes alcanzar **densidad local** suficiente para que el marketplace tenga variedad | 🔴 Alto |
| A7 | La calidad y confiabilidad de los proveedores en la plataforma es **consistente** | 🟡 Medio |
| A8 | Puedes resolver la **logística** sin que te coma los márgenes | 🔴 Alto |

**Mi diagnóstico: Tienes al menos 5 assumptions de alto riesgo que no has validado. Eso es una receta para quemar dinero.**

La pregunta que te hago como VC:

> *"¿Cuál de estas assumptions ya validaste con datos reales, no con conversaciones donde la gente te dijo 'sí, suena interesante'?"*

Porque **"suena interesante" no es validación. Solo la gente que saca la cartera está validando.**

---

## 4. El Escenario Donde Fracasas Rápido

### 📉 El Spiral of Death del Marketplace

```
MES 1-2: Lanzas en una ciudad.