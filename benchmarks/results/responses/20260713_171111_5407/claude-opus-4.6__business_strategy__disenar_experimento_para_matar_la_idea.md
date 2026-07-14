# Claude Opus 4.6 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 6.56 | quality: 8.0
- latency_total: 50.58s | tokens_per_second: 38.6
- input_tokens: 230 | output_tokens: 1953
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una estrategia detallada y práctica para probar la hipótesis, con claridad y utilidad directa para un emprendedor.

## Respuesta completa

# Experimento para MATAR tu hipótesis

## El problema con tu hipótesis actual

Antes de diseñar el test, necesito descomponer tu hipótesis porque tiene **3 supuestos escondidos** que pueden fallar independientemente:

1. **Las agencias pequeñas sienten dolor real** con los reportes manuales
2. **Ese dolor vale $200/mes** para ellas (no $50, no $0)
3. **No tienen ya una solución** que consideren "suficientemente buena"

Si cualquiera de los tres es falso, tu idea muere. El experimento ataca los tres en orden.

---

## El experimento: "Venta en frío de algo que no existe"

### Qué haces exactamente

**Días 1-2: Preparación (4 horas)**

Creas una landing page simple en Carrd ($19/año) con:
- Headline que describe el dolor específico
- 3 bullets de lo que haría la herramienta
- Precio visible: **$200/mes**
- Botón de CTA que diga **"Quiero acceso anticipado — $99 el primer mes"**
- El botón lleva a un formulario de Tally (gratis) que pide: email, nombre de agencia, cuántos clientes tienen, y **número de tarjeta** → NO. Pide que agenden una llamada de 15 min en Calendly (gratis)

> **¿Por qué una llamada y no solo el email?** Porque dar un email no cuesta nada. Agendar 15 minutos de su tiempo con un desconocido es una señal real de dolor. Y en esa llamada vas a intentar **pre-vender**, que es la señal definitiva.

**Días 2-5: Contacto directo (2-3 horas/día)**

Contactas **40 agencias de marketing pequeñas** (2-10 empleados) por estos canales:

- **20 por LinkedIn** → buscas "marketing agency owner/founder", filtras por tamaño, mensajes personalizados (no automatizados, no spam)
- **10 por email frío** → encuentras agencias en Google Maps/Clutch, sacas emails con Hunter.io (gratis hasta 25 búsquedas)
- **10 en comunidades** → grupos de Facebook de agencias, subreddits como r/marketing, Slack groups de agencias

El mensaje es siempre una variación de esto:

> *"Hola [nombre]. Estoy construyendo una herramienta que genera automáticamente los reportes mensuales para los clientes de agencias como la tuya — conecta tus fuentes de datos, elige plantilla, y el reporte se envía solo. Cuesta $200/mes. ¿Es algo que te resolvería un problema real? Si te interesa, tengo 10 spots de acceso anticipado a mitad de precio."*

**Días 5-8: Las llamadas**

Con cada persona que agende, haces una llamada de 15 minutos donde:

1. **Primero escuchas** (5 min): "Cuéntame cómo haces los reportes hoy"
2. **Detectas el dolor** (3 min): "¿Cuántas horas te toma? ¿Qué has intentado para resolverlo?"
3. **Presentas la oferta** (3 min): descripción simple de lo que harías
4. **Intentas cerrar** (4 min): "Estoy ofreciendo acceso anticipado a $99 el primer mes, $200 después. ¿Te anoto?"

Si dicen que sí, les pides un **pago por adelantado de $99 por PayPal o Stripe** para reservar su lugar. Les dices que si no entregas en 60 días, devuelves el dinero.

---

### Cuánto cuesta

| Concepto | Costo |
|---|---|
| Carrd (landing) | $0 (trial) o $19 |
| Calendly | $0 |
| Tally (formulario) | $0 |
| Hunter.io | $0 (plan gratis) |
| LinkedIn (cuenta normal) | $0 |
| Tu tiempo (~15 horas) | $0 en dinero |
| **TOTAL** | **$0 — $19** |

### Cuánto tarda

**8 días calendario. Máximo 10.**

---

## Los números que MATAN la hipótesis

Aquí es donde la mayoría de founders se engañan. Defino los umbrales **antes** de empezar para que no puedas mover los postes de la portería después.

### Embudo esperado si la hipótesis es VERDADERA:

```
40 contactados
 → 12 responden (30% — generoso para frío)
  → 6 agendan llamada (50% de los que responden)
   → 3 pagan $99 (50% de los que llaman)
```

### Criterio de muerte — ABANDONA si:

| Señal | Umbral de muerte | Por qué mata la idea |
|---|---|---|
| **Tasa de respuesta** | Menos de 4 de 40 responden | El dolor no es lo suficientemente fuerte como para que paren a leer tu mensaje. Supuesto 1 muerto. |
| **Objeción dominante** | Más de la mitad dice "ya uso Google Sheets / Data Studio / AgencyAnalytics y me funciona" | Supuesto 3 muerto. Ya tienen solución "suficientemente buena". |
| **Reacción al precio** | Más de la mitad dice "interesante pero $200 es mucho" o pide descuento agresivo | Supuesto 2 muerto. El dolor existe pero no vale $200. |
| **Pre-ventas** | **0 personas pagan los $99** | Los tres supuestos probablemente muertos. La gente que dice "qué buena idea" pero no saca la tarjeta te está siendo amable, no honesta. |

### Criterio de "sigue adelante":

**3 o más personas te pagan $99 por adelantado.**

No "me interesa". No "avísame cuando esté listo". No "suena genial". **Dinero en tu cuenta.** Esa es la única señal que no miente.

---

## Lo que este experimento NO te dice

Siendo honesto con las limitaciones:

- **No te dice si puedes escalar** más allá de las primeras 10 ventas
- **No te dice si la retención será buena** (pueden pagar un mes y cancelar)
- **No te dice si puedes construirlo técnicamente** en un costo razonable

Pero esos son problemas del **siguiente** experimento. Ahora mismo la pregunta es binaria: **¿alguien saca la tarjeta por esto? Sí o no.**

---

## La trampa que vas a querer hacerte

Después de 8 días, si los resultados son malos, tu cerebro va a decir:

- *"Es que no contacté a las agencias correctas"*
- *"Es que mi mensaje no era bueno"*
- *"Es que la landing no explicaba bien el producto"*

Tal vez. Pero si **40 personas** del target exacto no se emocionan lo suficiente como para darte $99 por algo que supuestamente les ahorra horas cada mes... el problema no es tu copy. **El problema es que el dolor no es tan fuerte como crees.**

---

**8 días y $19 para saber si debes invertir 2 meses de tu vida. Empieza mañana.**