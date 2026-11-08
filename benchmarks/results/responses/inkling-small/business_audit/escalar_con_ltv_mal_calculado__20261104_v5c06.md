# Inkling Small — business_audit/escalar_con_ltv_mal_calculado

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 18.627s | tokens_per_second: 201.2
- input_tokens: 193 | output_tokens: 3747

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

**No. No apruebo. No metas los $10.000.**

El plan muere en la aritmética, como casi todos. Recalculé con tu propio papel. Aquí está el daño:

---

### 1. El error de vida útil (el más grave)
Dijiste: *“se queda unos 2 años”*.  
Con **8% de churn mensual**, la retención es 92%. La vida media no es 24 meses; es:

**Vida media = 1 / Churn = 1 / 0.08 = 12.5 meses**

En 24 meses solo sobreviviría el 15% de tu cohorte (0.92²⁴ ≈ 0.15). Estás duplicando la vida.

### 2. El error de margen (el segundo más grave)
Dijiste: *LTV = $35 × 24 = $840*.  
Ese es **ingreso bruto**, no valor que te quede para pagar CAC.

Tu margen bruto es **70%**, así que tu contribución mensual real por cliente es:

**$35 × 0.70 = $24.50 / mes**

El LTV debe calcularse sobre **contribución**, no sobre precio de lista.

---

### 3. La recalculación real (tu unit economics)

| Concepto | Tu cálculo | Realidad |
|---|---|---|
| Vida media | 24 meses | **12.5 meses** |
| Contribución mensual | $35 | **$24.50** |
| **LTV** | $840 | **$306.25** |
| **CAC** | $290 | $290 |
| **LTV / CAC** | ~2.9 (y dices “por encima de 3”) | **1.06** |
| **Payback** (CAC / contribución) | — | **11.8 meses** |

**LTV/CAC = 1.06.** Eso no es “casi 3”. Es **casi 1**. Eso significa que por cada dólar que gastas en ads, recuperas $1.06 en valor bruto a lo largo de toda la vida del cliente, y eso sin considerar el valor temporal del dinero ni los riesgos.

---

### 4. Qué pasa si metes los $10.000

- Clientes nuevos: **$10.000 / $290 ≈ 34 clientes**.
- Valor que traen esos 34: **34 × $306.25 ≈ $10.412**.
- **Neto de la operación:** **+$412** en ~12 meses de recuperación lenta.
- **Flujo de caja hoy:** **-$10.000** hoy por una recuperación de ~$833/mes al inicio (que se va erosionando por el 8% de churn).

Con 8% de churn mensual, tu cohorte pierde la mitad antes de los 9 meses. Estás quemando efectivo por un retorno casi nulo y un payback de casi 12 meses. Eso no es escala; es un **agujero de liquidez** disfrazado.

---

### 5. Por qué “soy rentable” no importa aquí

Ser rentable con **adquisición orgánica o referencias** (CAC implícito bajo o cero) no significa que soportes **CAC pagado de $290**. El plan de publicidad pagada es un **cambio de modelo de adquisición**, no un acelerador del que ya funciona. Si tu negocio es rentable a $290 de CAC, la matemática debería gritar **LTV/CAC > 3** y **payback < 6 meses**. Aquí grita lo contrario.

---

### 6. Condiciones para aprobar ese $10.000 (o cualquier escala)

No apruebo hasta que no veas **uno o más** de estos cambios:

1. **Baja el churn.** A 8% mensual necesitas **~3% mensual** para que la vida sea ~33 meses y el LTV suba a ~$800 (con margen).
2. **Sube el LTV** (precio, upsells, expansión) sin subir proporcionalmente el churn.
3. **Baja el CAC** drásticamente (mejor landing, mejor funnel, mejor audiencia). Con $306 de LTV, tu CAC objetivo para LTV/CAC = 3 es **~$100**.
4. **Payback < 6 meses.** Ahora es 11.8. Eso es inaceptable para escalar con deuda o caja.

**Regla de oro:** Si tu LTV/CAC está cerca de 1 y tu payback es igual a tu vida media, **no estás comprando clientes; estás prestándoles dinero con tasa negativa**.

---

### Veredicto final

**No metas los $10.000 en publicidad pagada hoy.**

Tu LTV real es **~$306**, no $840. Tu ratio es **~1.06x**, no 3x. Con $10.000 te compras 34 clientes que te devuelven casi lo mismo, en más de un año, mientras tu caja se desangra.

Primero **arregla el churn** o **baja el CAC a la mitad/tercio**, o sube la contribución mensual. Cuando tu LTV esté por encima de **$870** (o tu CAC por debajo de **$100**) y el payback esté en 3-6 meses, **entonces** escala con fuerza.

**La aritmética no miente: en este momento, cada dólar en ads es casi un dólar perdido en tiempo y riesgo.**