# Nemotron 3 Ultra 550B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 78.883s | tokens_per_second: 19.6
- input_tokens: 223 | output_tokens: 1550

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

**No. No le des. Apaga la intención de meter los $10.000 hoy mismo.**

Tu aritmética tiene un error grave que te va a quemar la caja. Vamos a la autopsia:

---

### 1. Tu LTV está inflado un 174%
Usaste: `Precio × Meses estimados = 35 × 24 = $840`.
**Error:** Asumiste que el cliente se queda 24 meses fijos. Con **8% de churn mensual**, la vida media real es:
$$ \text{Vida media (meses)} = \frac{1}{\text{Churn}} = \frac{1}{0.08} = 12,5 \text{ meses} $$
No 24. **12,5**.

El LTV correcto (con margen bruto) es:
$$ \text{LTV} = \frac{\text{Precio} \times \text{Margen Bruto}}{\text{Churn Mensual}} = \frac{35 \times 0,70}{0,08} = \frac{24,5}{0,08} = \mathbf{\$306,25} $$

---

### 2. Tu ratio real LTV/CAC es **1,05**, no 2,9
$$ \frac{306,25}{290} = 1,05 $$
Un ratio **< 3** es zona de peligro. **< 1,5** es "estás pagando por trabajar". Cada cliente nuevo te deja **$16,25 de profit vitalicio** antes de impuestos, overhead, salarios, herramientas, devoluciones, chargebacks...

---

### 3. Payback Period: **11,8 meses**
$$ \frac{\text{CAC}}{\text{Margen mensual por cliente}} = \frac{290}{35 \times 0,70} = \frac{290}{24,5} = 11,8 \text{ meses} $$
Tardas casi **un año** en recuperar el cash de cada cliente. Si metes $10.000 hoy:
- Adquieres ~34 clientes.
- Sales de caja **-$10.000** hoy.
- Recuperas tu dinero **en noviembre del año que viene** (si nadie se da de baja antes).
- Mientras tanto, sigues pagando servidores, sueldos, impuestos, tú.

---

### 4. El churn del 8% mensual es una hemorragia
- **Churn anualizado:** $1 - (0,92)^{12} = \mathbf{63,4\%}$.
- De cada 100 clientes que entran en enero, **63 se van antes de diciembre**.
- Estás echando gasolina a un cubo con agujeros. Escalar publicidad **acelera la quema de caja**, no el crecimiento neto.

---

## ¿Qué hacer antes de meter un solo dólar en ads?

| Palanca | Objetivo mínimo | Por qué |
|---|---|---|
| **Bajar churn** | ≤ 3 %/mes (≈ 30 %/año) | Sube vida media a 33 meses → LTV $808 → LTV/CAC 2,8. |
| **Subir precio** | ≥ $59/mes (o planes anuales con descuento) | Mejora margen y payback sin tocar CAC. |
| **Bajar CAC** | ≤ $100 | Canales orgánicos, referidos, SEO, partnerships, outbound barato. |
| **Recuperar cash upfront** | Plan anual = 10-11 × mensual | Cobras 12 meses por adelantado → payback instantáneo. |

---

### Regla de oro para escalar paid:
> **LTV/CAC ≥ 3**  
> **Payback ≤ 6 meses** (idealmente ≤ 3)  
> **Churn mensual ≤ 3 %** (B2B SaaS sano)

Hoy cumples **cero de tres**.

---

## Plan de acción esta semana
1. **Frena el gasto en ads.** $0 hasta que las métricas cuadren.
2. **Entrevista a los 20 últimos churned.** Descubre *por qué* se van (onboarding, features, precio, soporte). Arregla lo top-3.
3. **Lanza plan anual:** $350/año (≈ $29/mes efectivo, 2 meses gratis). Cash upfront = payback día 1.
4. **Testea canales baratos:** cold email, SEO, programa de referidos (regala 1 mes gratis por referido que pague).
5. **Recalcula dentro de 60 días.** Si churn bajó a 4 % y CAC a $150 → **ahora sí** metes los $10k (o más).

---

**Conclusión:** Tu instinto de crecer está bien; tu hoja de cálculo miente. Arregla la física del negocio antes de pisar el acelerador.