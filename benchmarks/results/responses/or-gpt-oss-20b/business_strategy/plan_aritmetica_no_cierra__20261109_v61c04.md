# GPT-OSS 20B — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 4.66 | quality: 3.33
- latency_total: 10.243s | tokens_per_second: 134.2
- input_tokens: 262 | output_tokens: 1375

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa

**Resumen rápido:**  
Con los números que tu socio ha puesto, el plan **no** alcanzará los $6 000 USD/mes.  

| Paso | Métrica actual | Resultado mensual | Comentario |
|------|----------------|-------------------|------------|
| 1. Visitas | 200 000 | – | |
| 2. Conversión a suscriptor | 1,5 % | 3 000 suscriptores | Muy bajo, típico de sitios “básicos” |
| 3. Conversión a compra | 2 % | 60 clientes | 60 × $30 = $1 800 | |
| 4. Ingresos | – | $1 800 | < $6 000 |

Para llegar a $6 000 con el mismo modelo, necesitarías:

* **3,33 × más ingresos** → 3 333 clientes al mes.  
* Con 2 % de compra, eso requiere **166 665 suscriptores**.  
* Con 1,5 % de conversión, necesitas **11 111 111 visitas** al mes.  
  (¡un número totalmente fuera de alcance en 6 meses!)

---

## ¿Por qué falla la multiplicación?

1. **Funnel demasiado estrecho** – cada fase pierde la mayor parte del tráfico.  
2. **Valor del ticket bajo** – $30 no es suficiente para amortizar 200 k visitas.  
3. **Sin escalabilidad definida** – no se plantea cómo crecer visitas, suscriptores o tasas de compra en los 6 meses.  

---

## Alternativas realistas

| Estrategia | Cómo mejora | Impacto estimado |
|------------|-------------|------------------|
| **Aumentar el precio** | Si subes a $60, necesitas la mitad de clientes (30) para $1 800. | Reduce carga de tráfico. |
| **Upsell/Cross‑sell** | Ofrecer un módulo avanzado a $20 o un paquete de 3 cursos a $75. | 1 000 USD de upsell * 0,1% → $100. |
| **Lead magnet de mayor valor** | Más contenido (ebook + webinar) que genere leads con mayor intención de compra. | Eleva la tasa de compra a 4 % → 120 clientes → $3 600. |
| **Segmentación y remarketing** | Enviar emails de carrusel, test de precios, ofertas por tiempo. | +15 % de conversión. |
| **Canales adicionales** | Publicidad pagada (Google, Facebook), SEO + contenido. | Triplica tráfico en 3 meses. |

---

## Plan de acción de 6 meses (ejemplo)

| Mes | Visitas | Suscriptores | Clientes | Ingresos |
|-----|---------|--------------|----------|----------|
| 1 | 200 000 | 3 000 | 60 | $1 800 |
| 2 | 250 000 | 3 750 | 75 | $2 250 |
| 3 | 300 000 | 4 500 | 90 | $2 700 |
| 4 | 400 000 | 6 000 | 120 | $3 600 |
| 5 | 500 000 | 7 500 | 150 | $4 500 |
| 6 | 600 000 | 9 000 | 180 | $5 400 |

*Este escenario asume:*
- **4 % de compra** (doble de la estimación inicial).  
- **$30 por curso**.  
- **Incremento constante de tráfico** (30 % cada mes).

**Resultado:** $5 400/mes – todavía **$1 600** shy.  
Para cerrar la brecha, podrías combinar un **precio de $45** o un **upsell** de $15 que genere $600 extra al mes.

---

## Conclusión

- **No aprobar** el plan tal cual.  
- La lógica de multiplicación funciona solo si cada fase del embudo es alta.  
- Necesitas **re‑definir la estrategia**: mejores tasas de conversión, mayor ticket medio, múltiples ingresos y un plan de crecimiento de tráfico.

En lugar de lanzar el plan tal cual, proponle a tu socio que revisen los puntos anteriores y creen un **roadmap de crecimiento** donde cada variable sea medible y ajustable. Sólo así tendrás una probabilidad realista de alcanzar los $6 000 USD/mes en 6 meses.