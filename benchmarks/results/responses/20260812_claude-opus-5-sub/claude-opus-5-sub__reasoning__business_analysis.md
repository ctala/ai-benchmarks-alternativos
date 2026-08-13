# Claude Opus 5 (suscripción) — reasoning/business_analysis

- model_id: `claude-opus-5`
- success: True  | final: 7.62 | quality: 9.76
- latency_total: 151.651s | tokens_per_second: 70.0
- input_tokens: 2 | output_tokens: 10608
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y acciones concretas basadas en los datos.

## Entrada exacta (lo que recibió el modelo)

**user:**

Analiza estos datos de mi SaaS:

Enero: 1,200 usuarios, $18,000 MRR, 45 churns, CAC $85, LTV $420
Febrero: 1,350 usuarios, $20,250 MRR, 52 churns, CAC $92, LTV $415
Marzo: 1,480 usuarios, $22,200 MRR, 68 churns, CAC $78, LTV $408

Necesito:
1. Calcula las metricas clave (churn rate, growth rate, LTV/CAC ratio, net revenue retention)
2. Identifica tendencias preocupantes
3. Sugiere 3 acciones concretas basadas en los datos
4. Proyecta abril si las tendencias continuan


## Respuesta completa

## 1. Métricas calculadas

| Métrica | Enero | Febrero | Marzo | Dirección |
|---|---|---|---|---|
| ARPU | $15.00 | $15.00 | $15.00 | Plano |
| Churn mensual (logo)¹ | 3.75% | 4.33% | 5.04% | ⬆ malo |
| Churn anualizado | 36.6% | 41.2% | 46.2% | ⬆ malo |
| Altas brutas | — | 202 | 198 | Plano |
| Altas netas | — | 150 | 130 | ⬇ |
| Crecimiento MRR | — | 12.5% | 9.6% | ⬇ |
| NRR (inferido)² | — | 95.7% | 95.0% | ⬇ |
| LTV/CAC reportado | 4.94 | 4.51 | 5.23 | Estable |
| **LTV/CAC recalculado³** | **4.71** | **3.76** | **3.81** | ⬇ |
| CAC payback (meses) | 5.7 | 6.1 | 5.2 | OK |
| Quick ratio⁴ | — | 3.88 | 2.91 | ⬇ |
| Gasto en adquisición | — | $18,584 | $15,444 | ⬇ 17% |

¹ Base inicio de período. Enero asume base de diciembre ≈ 1,200 (falta el dato real).
² No tengo expansión/contracción separadas. Como el ARPU es exactamente $15.00 los tres meses, la expansión es ≈ $0, así que NRR = GRR = (MRR inicial − MRR churneado) / MRR inicial.
³ LTV = ARPU / churn real del mes, base ingresos (sin margen bruto).
⁴ (MRR nuevo) / (MRR churneado).

---

## 2. Tendencias preocupantes

**A. Tu LTV está calculado con un churn que ya no existe.** Este es el hallazgo más importante. $408 de LTV con $15 de ARPU implica una vida de 27.2 meses, o sea 3.68% de churn mensual — el churn de **enero**. El de marzo es 5.04%, que implica 19.8 meses y un LTV real de ~$298 (~$238 si aplicas 80% de margen bruto).

El churn subió 34% en dos meses y tu LTV solo bajó 2.9%. Está anclado a un supuesto viejo. Consecuencia práctica: crees que tienes un ratio de 5.2x y en realidad tienes 3.8x sobre ingresos, o ~3.0x sobre margen. Si estabas por pisar el acelerador en adquisición con ese 5.2x, estarías escalando sobre un número que no existe.

**B. El crecimiento se desacelera por churn, no por adquisición.** Las altas brutas están planas (202 → 198). Lo que cambió es la fuga: 52 → 68 (+31%). Estás llenando el balde al mismo ritmo y el agujero creció. Por eso las altas netas caen 150 → 130 y el MRR pasa de 12.5% a 9.6%.

**C. NRR de 95% = no tienes motor de expansión.** El ARPU es exactamente $15.00 los tres meses. Eso apunta a plan único sin tiers ni asientos: no existe mecanismo para que un cliente te pague más con el tiempo. Sin logos nuevos, tu base se encoge 5% mensual. Referencia: SaaS SMB sano está en 100-110%.

**D. El CAC bajó — y esto puede ser bueno o el origen del problema.** Cortaste 17% del gasto ($18,584 → $15,444) y perdiste solo 2% de las altas. Eso sugiere que ese gasto marginal casi no compraba nada, y que hay más por optimizar.

Pero hay una lectura alternativa: cambiaste a un canal más barato que trae peor fit, y eso terminará en más churn. **Ojo con el timing**: el CAC cayó en marzo, así que la cohorte barata todavía no ha tenido tiempo de churnear. El pico de churn de marzo (68) viene de cohortes de diciembre-enero, no de esta. Si hubo cambio de canal, su efecto real en retención lo vas a ver en **mayo-junio**. No canceles la alarma todavía.

---

## 3. Tres acciones

**1. Análisis de cohortes antes que cualquier otra cosa (1 día de SQL).**
Corta los 68 churns de marzo por mes de alta. Hay dos escenarios con soluciones opuestas:

- Se concentran en cohortes recientes (dic-ene) → problema de **calidad de adquisición**. Se arregla en marketing/ICP.
- Se reparten parejo entre todas las cohortes → problema de **producto o competencia**. Se arregla en producto.

Grafica las curvas de retención M1/M2/M3 por cohorte de alta. Si la curva de la cohorte de enero está por debajo de la de octubre en el mismo mes de vida, ya tienes tu respuesta. Esta acción va primera porque **determina cuál de las otras dos importa**.

**2. Reconstruye el LTV y ponlo en el tablero mensual.**
Fórmula: `LTV = ARPU × margen bruto / churn promedio de los últimos 3 meses`. Recalcúlalo cada mes con churn móvil, no con un supuesto fijo. Congela cualquier decisión de escalar spend hasta tener ese número. La diferencia entre 5.2x y 3.0x es la diferencia entre "acelerar" y "no tocar nada".

**3. Abre un camino de expansión para romper el ARPU plano.**
Con NRR en 95% dependes 100% de logos nuevos. Un segundo tier o un add-on por uso cambia la matemática. Para llegar a NRR de 100% con 5% de churn necesitas que la expansión iguale el 5% del MRR cada mes — hoy es $0. Concreto: si el 15% de la base migra de $15 a $29, el ARPU sube a $17.10 y sumas ~$3,100 de MRR sin un solo cliente nuevo. La barra real no es una migración puntual sino un flujo sostenido de upgrades (~5% de la base al mes).

---

## 4. Proyección abril

Extrapolando el churn con la misma aceleración observada (~+16% relativo mensual → 5.85%) y altas brutas planas en ~194:

| | Marzo (real) | Abril (proyectado) |
|---|---|---|
| Usuarios | 1,480 | ~1,587 |
| MRR | $22,200 | ~$23,805 |
| Crecimiento MRR | 9.6% | **7.2%** |
| Churns | 68 | ~87 |
| Altas netas | 130 | ~107 |
| NRR | 95.0% | ~94.2% |

La secuencia de crecimiento queda **12.5% → 9.6% → 7.2%**: pierdes entre 2 y 3 puntos por mes.

**El dato que importa más que abril:** si nada cambia, los churns alcanzan a las altas brutas y el crecimiento llega a cero. Modelando la aceleración del churn de forma agresiva (geométrica) eso pasa en **julio-agosto** a ~1,750 usuarios; de forma conservadora (lineal, +0.7pp mensual) en **septiembre-octubre** a ~1,820. En ambos casos: **Q3 de este año, entre 1,750 y 1,820 usuarios como techo**. Ese es tu horizonte real para arreglar el churn.

---

## Advertencias sobre los datos

Tres puntos son muy poco para separar tendencia de ruido. Los 68 churns de marzo pueden ser una tendencia o un evento puntual (un lote de contratos anuales venciendo, una promoción de diciembre que expiró, un competidor que lanzó). Lo que le da peso a la lectura no es ninguna métrica sola, sino que **cuatro se mueven en la misma dirección a la vez**: churn arriba, crecimiento abajo, quick ratio abajo, NRR abajo.

Para cerrar el análisis me faltan: usuarios de diciembre (para el churn real de enero), margen bruto (todo el LTV está en base ingresos, o sea optimista), separación de expansión vs contracción (el NRR es inferido, no medido), si los churns son solo bajas o incluyen downgrades, y si estos conteos son de fin de mes o promedio.