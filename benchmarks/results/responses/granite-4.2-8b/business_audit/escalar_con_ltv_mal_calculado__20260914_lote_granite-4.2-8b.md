# Granite 4.2 8B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 65.566s | tokens_per_second: 98.1
- input_tokens: 227 | output_tokens: 6433

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**Respuesta clara, práctica y sin tecnicismos innecesarios (como analista de unit economics, hablando como si estuviera sentado a tu lado con tu hoja de cálculo).**  
*Te respondo directo, con el error que cometiste (es común y fácil de saltarse), cómo corregirlo en 2 minutos, y qué hacer con el $10.000 de publicidad. No te doy una teoría larga; solo lo que necesitas ejecutar esta semana.*

---

### ✅ **1. Tu cálculo de LTV está incorrecto (el error que mató tu plan).**  
> *Lo que dijiste:* "un cliente se queda unos 2 años → LTV = $35 × 24 = $840".  
> *Por qué es wrong:* El churn es **mensual 8%** (0.08), no "se queda 2 años". Con 8% de churn *cada mes*, la vida promedio del cliente **no es 24 meses**, sino aproximadamente **12.5 meses**. Aquí el porqué rápido (no necesitas fórmulas complejas):

- Si el churn es 8% al mes, eso significa que cada mes, el 8% de tus clientes actuales se van (dejan o no renuevan).  
- La vida promedio real (en meses) de un cliente con churn mensual `c` es **1 / c**. Entonces: `1 / 0.08 = 12.5 meses` (aproximadamente).  
  *(Ejemplo intuitivo: si el 10% se va cada mes (churn 10%), promedio ~10 meses; si el 8% se va, promedio ~12.5 meses. No 24 meses. 24 meses sería si el churn fuera ~4.2% al mes, no 8%.)*

- **LTV correcto (para suscripción mensual):**  
  `Precio mensual × vida promedio en meses` → `$35 × 12.5 ≈ $437.50`.  
  *(Alternativamente, usando la fórmula estándar de LTV con churn: `LTV = Precio / Churn = $35 / 0.08 = $437.50`. Igual resultado. No uses "meses totales" (24) porque el churn corta la vida real cada mes.)*

> 💡 **Tu LTV real ≈ $437.50 (no $840).**  
> *Por qué importa:* Usaste $840 → LTV/CAC = $840 / $290 ≈ 2.9 (creíste que estaba "por encima de 3"). Pero con el cálculo correcto:  
> `LTV/CAC = $437.50 / $290 ≈ 1.51`.  
> **Esto NO está "por encima de 3" (la regla común 3x es un *target ideal* para bajas churnes; con 8% mensual churn, 1.5x es realista pero requiere disciplina en cash flow; 3x sería ideal solo si el churn bajara significativamente).**  
> *Importante:* No te convence pensar "2.9 > 3" porque usaste una vida de 24 meses que no corresponde al churn real. **El error matemático es claro y común; no es un juicio, es aritmética básica con churn.**

> ✅ **Resumen rápido para recordar:**  
> > *"Con churn mensual 8%, el cliente promedio dura ~12.5 meses, no 24 meses. LTV = $35 × 12.5 ≈ $437. LTV/CAC = $437 / $290 ≈ 1.5."*

---

### ✅ **2. ¿Qué significa LTV/CAC = 1.5 para ti en la realidad? (Práctico, no teórico)**  
- **CAC = $290 por cliente (publicidad).**  
- **LTV = $437.50 total que un cliente aporta a lo largo de su vida (incluyendo churn).**  
- **Neto por cliente (LTV - CAC) = $437.50 - $290 = $147.50** (en valor total a lo largo del tiempo, no mensual).  
- **Payback (cuántos meses tardas en recuperar el CAC):**  
  > Un cliente paga $35/mes. Necesitas acumular $290 para cubrir el CAC.  
  > Con retención 92% al mes (92% de clientes permanecen), el recuento rápido es:  
  > - Mes 1: $35  
  > - Mes 2: $35 + ($35 × 0.92) ≈ $70  
  > - Mes 3: ≈ $105, etc.  
  > **En ~13 meses, el cliente acumula ~$290 en ingresos totales** (calculado con la fórmula de anualidad: $35 × (1 - 0.92^n)/0.08 ≈ $290 → n ≈ 13 meses).  
  > *Es decir: pagas $290 en publicidad para conseguir un cliente, y recuperas ese $290 en efectivo alrededor del mes 13 (no al mes 24). En los primeros 3-6 meses, tendrás un pequeño déficit de efectivo (ej.: gasto $290, ingreso solo $35-70/mes), pero lo recuperas después.*

- **¿Es riesgo con $10.000 de publicidad?**  
  > - $10.000 / $290 ≈ 34.5 nuevos clientes (redondea a ~35 clientes).  
  > - Ingresos mensuales de esos nuevos clientes (sin contar churn de ellos): ~35 × $35 = $1,225 al mes.  
  > - Pero recuerda: esos nuevos clientes también tendrán 8% churn al mes (como tus clientes actuales), así que en el mes 2, perderás ~8% de esos 35 (≈3 clientes), etc.  
  > - **El punto clave práctico:** Si pones $10.000 de publicidad *de golpe*, tendrás que pagar $290 por cliente *inmediatamente* (gasto de publicidad), mientras que los ingresos de esos clientes llegan progresivamente ($35/mes). Si tu cash flow actual no tiene un pequeño colchón para cubrir los primeros meses de payback (~$290 por cliente), podrías sentir un "dip" temporal de efectivo (aunque ya eres rentable, es bueno confirmar que el colchón existe).

> ✅ **Conclusión práctica sobre $10.000:**  
> *Si tu cash flow actual puede absorber ~$290 × 35 ≈ $10,150 en gasto de publicidad mientras esperas recuperar el CAC en ~13 meses (es decir, si tienes al menos ~$2,000-$3,000 de efectivo libre para cubrir los primeros 3-4 meses de payback), entonces $10.000 es matemáticamente viable. Pero si no confirmas primero que el CAC se mantenga en $290 a esa escala (a menudo el CAC sube al escalar porque la calidad de clics empeora o el funnel necesita optimización), podrías gastar $290 por cliente y luego ver que el CAC real sube a $350-$400, lo que haría LTV/CAC < 1.25 (muy riesgoso).*

> **→ No pongas $10.000 de publicidad de golpe sin probar primero.** (Es el error más común: "estoy rentable, así que escalo rápido", pero el CAC suele subir al escalar sin prueba).

---

### ✅ **3. Qué hacer esta semana (pasos concretos, en < 30 minutos, sin hipótesis):**  
**Objetivo:** Confirmar que el CAC de $290 es estable a la escala que quieres, sin arriesgar $10.000 de golpe.

1. **Haz un test pequeño de 3 días (gasto total ≤ $300):**  
   - Escribe una campaña mínima en tu plataforma de publicidad (Meta/Google/etc.) con el mismo targeting y creativo que usas ahora.  
   - Ajusta el presupuesto para que gaste exactamente $300 (ej.: $100/día si es 3 días).  
   - **Mide solo 2 cosas:**  
     > a) Cuántos clientes *reales* (que pagan y están activos, no solo clics) te compraron.  
     > b) CAC real = gasto total de publicidad / número de clientes reales (ej.: $300 / 1.0 clientes = $300 si vendiste 1 cliente, pero probablemente más).  
   - *No optimices el presupuesto ahora; solo ejecuta el test con $300 para ver el CAC real a esa escala pequeña.*

2. **Verifica el CAC del test:**  
   - Si el test te da CAC ≈ $280-$300 (ej.: $300 gasto / 1.0-1.2 clientes), **entonces el CAC es estable** y puedes escalar.  
   - Si el CAC sube a $320+ en el test (ej.: $300 gasto / 0.9 clientes ≈ $333), **detén el test inmediatamente**, optimiza el creativo/targeting (ej.: prueba 1 nuevo copy o 1 nuevo segmento), y repite el test con $300. *No aumentes el presupuesto sin confirmar que el CAC se mantenga bajo $320.*

3. **Calcula el escalar seguro (después de confirmar CAC):**  
   - Supón que el test confirma CAC ≈ $290 (estable).  
   - Para escalar sin riesgo: **empieza con 20-30% del $10.000** (ej.: $2,000-$3,000 en publicidad este mes), no todo de golpe.  
   - Por qué: permite ver cómo el CAC se comporta a esa escala (a veces sube 10-20% al pasar de $500-$1,000 de gasto a $3,000). Si el CAC se mantiene en $290, entonces $3,000 → ~10-11 nuevos clientes. Revisa los ingresos netos en 2 meses (incluyendo churn) y ajusta el presupuesto solo si el LTV/CAC sigue ≥1.3 (más seguro que 1.5).  
   - Usa este patrón: *Test pequeño → Ajusta → Escala 20-30% más → Repite test si sube CAC → Escala más si CAC se mantiene.*

4. **Verifica cash flow rápido (2 minutos):**  
   - ¿Tienes al menos ~$3,000 de efectivo libre (no incluyendo ingresos recurrentes) para cubrir el gasto inicial de publicidad + los primeros meses de payback?  
     *Ejemplo: Si pones $3,000 en publicidad, gastarás $3,000 de efectivo ahora; los clientes nuevos te pagan $35/mes, pero el payback es ~13 meses. Necesitas que tu efectivo actual tenga suficiente para no tener problemas si en los primeros 3-4 meses solo recibes $35-70 por cliente (ej.: 10 clientes → $350-$700/mes en ingresos, pero gasto $3,000 ya pagado). Si sí tienes el colchón (ej.: ya eres rentable y tienes >$3,000 en efectivo o reservas), está bien. Si no, escala más despacio.*

> ✅ **Resumen del plan de acción esta semana (escrito para que lo copies y pegues):**  
> > 1. Haz un test de publicidad de $300 (ej. $100/día por 3 días) con tu mismo creativo.  
> > 2. Mide solo: *número de clientes reales* (que pagaron y están activos) y calcula *CAC real = gasto publicidad / clientes reales*.  
> > 3. Si CAC real ≤ $320, escala a $2,000-$3,000 de publicidad este mes (no $10,000). Si CAC real > $320, detén, optimiza 1 cosa (ej. copy o targeting), repite el test de $300.  
> > 4. Después de confirmar CAC ≈ $290 (estable), escala solo 20-30% del presupuesto máximo cada semana (ej. $3k → luego $4.5k → luego $6k, etc.), siempre midiendo CAC en cada test pequeño.  
> > 5. Verifica que tengas ~$3k de efectivo libre para cubrir el gasto inicial de publicidad (payback ~13 meses, pero efectivo se paga al inicio).

---

### ❌ Por qué NO debes aprobar el $10,000 de golpe ahora (en una frase):  
> *"Decir 'LTV = $840' porque 'se queda 2 años' es matemáticamente incorrecto con churn 8% mensual; usar ese número te hace pensar que LTV/CAC = 2.9 > 3, pero en realidad es ~1.5. Y escalar $10k de golpe sin confirmar que el CAC se mantenga en $290 (que suele subir al escalar) es arriesgar perder el CAC y tener un déficit de efectivo en los primeros meses de payback."*

---

### ✅ Por qué esto funciona (unit economics real):  
- Corriges el cálculo de LTV con el churn real (12.5 meses, no 24).  
- Evitas el error más común: escalar sin probar el CAC a esa escala (el CAC suele subir 10-30% al pasar de prueba a escala).  
- Usas un test mínimo ($300) para confirmar CAC antes de gastar más (ahorras tiempo y dinero).  
- Verificas cash flow rápido (no asumas que "estoy rentable" = "puedo gastar $10k sin colchón", porque el payback es ~13 meses).  
- Escalas de forma gradual (20-30% cada semana), lo que es seguro y permite ajustar rápido si el CAC sube.

> **Ejemplo concreto:**  
> - Test de $300 → CAC = $285 (estable).  
> - Escala a $2,500 este mes (≈8.6 clientes nuevos).  
> - Observas que en el mes 1, ingresos netos de nuevos clientes = $35×8.6 ≈ $300 (pero gasto publicidad = $2,500), pero en el mes 2-3 recuperas parte del CAC con retención.  
> - Si después del test de $300 confirmas CAC ≤ $300, entonces $2,500 es seguro y escalable. Si en el test de $300 el CAC fuera $330, deten, optimiza, y no gastes $10k.

---

**En resumen para ti (copiar y pegar en tu mensaje al equipo o en tu hoja):**  
> *"Con churn 8% mensual, el cliente promedio dura ~12.5 meses, no 24 meses. LTV real ≈ $35 × 12.5 = $437.50, no $840. Por lo tanto LTV/CAC ≈ 1.5 (no 2.9). No pongo $10,000 de publicidad de golpe porque el CAC suele subir al escalar sin probar. Esta semana hago un test de $300: gasto $300 en publicidad, mido cuántos clientes reales (que pagan) y calculo CAC real. Si CAC ≤ $320, escalo a $2,500–$3,000 este mes (20-30% del $10k). Si CAC > $320, detengo, optimizo 1 cosa (copy/targeting), y repito el test de $300. Verifico que tenga ~$3k de efectivo libre para cubrir el gasto inicial (payback ~13 meses). Así escalamos seguro y sin perder dinero."*

**Ejecuta el test de $300 esta semana.** Cuando tengas los números del test (ej.: "gaste $300, vendí 1.2 clientes → CAC = $250" o "vendí 0.8 clientes → CAC = $375"), avísame y te ayudo a calcular el presupuesto exacto para el mes siguiente (sin asumir nada). No necesitas más teoría; solo el test pequeño y medir CAC real.

*(Esto es exactamente lo que hago con clientes en este mismo punto: corregir el LTV con el churn real, probar CAC a escala pequeña, y escalar gradualmente. Evita el "¡estoy rentable, así que gasto $10k!" que mata planes en la aritmética.)*

**¿Quieres que te escriba el script exacto para la campaña de prueba de $300 (qué decir en el anuncio, qué campo de formulario usar para confirmar "cliente real")?** Dime y te doy el copy mínimo de prueba en 5 minutos.