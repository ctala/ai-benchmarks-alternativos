# Qwen3-Coder-Next (OpenRouter FP8) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 26.664s | tokens_per_second: 57.4
- input_tokens: 229 | output_tokens: 1531

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

**No le des — y no por poco margen, sino por un error grave en el cálculo del LTV.**  
Tu plan suena atractivo, pero **no es sostenible** tal como está estructurado. Vamos a desglosarlo con unit economics rigurosas.

---

### 🔍 Errores críticos en tu cálculo actual:

#### ❌ 1. **Estás usando duración *promedio* en años (24 meses) sin ajustar por descuento o churn exponencial**
- El churn del 8% mensual implica una **vida útil esperada** de:
  \[
  \text{Vida esperada (en meses)} = \frac{1}{\text{churn}} = \frac{1}{0.08} = 12.5 \text{ meses}
  \]
  **No 24 meses.**  
  📌 *¿Por qué?* Porque cada mes pierdes el 8% de tu base, así que el cliente promedio se va mucho antes de los 2 años.  
  (24 meses sería el caso si el churn fuera ~4.2% mensual — pero no es tu caso).

#### ❌ 2. **No estás considerando el margen bruto en el LTV**
- Tu margen bruto es **70%**, así que el **contributo mensual neto** por cliente es:
  \[
  \text{Contributo mensual} = 35 \times 0.70 = \$24.50
  \]

#### ❌ 3. **No estás descontando flujos futuros (aunque para escala temprana, a veces se omite, pero aquí es crítico por el churn alto)**

---

### ✅ Cálculo correcto del LTV (con churn exponencial y margen bruto)

La fórmula estándar para LTV con churn mensual constante y sin descuento es:

\[
\text{LTV} = \frac{\text{Contributo mensual}}{\text{churn}} = \frac{24.50}{0.08} = \$306.25
\]

> 📌 **Este es el LTV real por cliente adquirido.**

---

### 📊 Comparación con CAC

- **CAC = \$290**
- **LTV = \$306.25**
- **LTV/CAC = 306.25 / 290 ≈ 1.05**

➡️ **Estás barely cubriendo el CAC.**  
➡️ **No hay margen para operación, marketing adicional, errores, o crecimiento sostenible.**

---

### 🚨 ¿Qué pasa si escalas $10k en publicidad este mes?

- Clientes nuevos = $10,000 / \$290 ≈ **34 clientes**
- Contributo mensual inicial = 34 × \$24.50 = **\$833**
- Pero:  
  - Mes 1: pierdes 8% → 2.7 clientes → contributo real ≈ \$782  
  - Mes 2: pierdes 8% de lo que queda → y así sucesivamente.

**El valor total de contributo de esos 34 clientes (LTV real) es solo ~\$306 × 34 = \$10,412.**  
**Invertiste \$10,000 en CAC.**  
➡️ **Margen neto total ≈ +\$412 sobre 24 meses.**

Pero…  
⚠️ Esto **no considera**:
- Costos operativos (soporte, CS, desarrollo, marketing no pagado, etc.)
- Costos de retención (ofertas para evitar churn)
- Posible degradación del LTV si el producto no mejora (churn sube con escala)
- Impuestos, gastos financieros, etc.

**En la práctica, es probable que no generes *ningún* margen operativo real.**

---

### 🛠️ ¿Qué puedes hacer?

#### Opción 1: **Reducir CAC**
- Optimiza adquisición: prueba canales orgánicos, referidos, retargeting barato.
- Mejora tasa de conversión (más landing, más confianza, menos fricción).
- Usa A/B testing para bajar el CAC real.

#### Opción 2: **Subir LTV**
- **Sube el precio** (si el mercado lo permite):  
  +5% → $36.75 → LTV sube a ~\$323  
  +10% → $38.50 → LTV = \$367  
- **Bajar churn** (¡clave!):  
  - Churn 6% → LTV = 24.50 / 0.06 = **\$408**  
  - Churn 5% → LTV = **\$490**  
  → Aquí es donde ganas *verdadero* margen.

#### Opción 3: **Modelo de freemium o trial**
- Atraer con valor gratuito y vender después (reduce CAC efectivo).

#### Opción 4: **LTV con retención activa (opcional, más realista)**
Si inviertes en retención (ej. CS proactivo), puedes *bajar el churn* con un CAC relativo bajo.

Ejemplo:  
- Ganas $1,000 en CS/retención → churn baja del 8% al 6%  
- LTV sube de \$306 a \$408  
- Net gain = (\$408 – \$306) × # clientes = \$102 × 34 = **\$3,468**  
→ Invertiste \$1,000, ganas \$3,468. **Excelente ROI.**

---

### 📌 Veredicto final:

> ❌ **No le des a escalar con CAC = $290 y churn = 8% tal como está.**  
> ✅ **Sí le das si primero:**
> - Bajas el churn a ≤6% **o**
> - Subes el precio ≥10% **o**
> - Bajas el CAC a ≤\$200  
> → y validas que el LTV real supere **3× el CAC** (es decir, LTV > \$870 para CAC = \$290, lo cual requiere **churn ≤2.8%** si no cambias nada más).

---

¿Quieres que diseñemos un plan de acción para reducir el churn o mejorar el LTV? Puedo ayudarte a priorizar acciones con impacto real.