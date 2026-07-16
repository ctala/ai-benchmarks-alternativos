# GPT-5.4 Mini — sales_outreach/campaign_optimization

- model_id: `gpt-5.4-mini`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 10.452s | tokens_per_second: 161.9
- input_tokens: 261 | output_tokens: 1692
- judge_score: 5.0 | justificación: 

## Respuesta completa

Claro. Voy a calcular primero las métricas y luego te doy una recomendación práctica de asignación de presupuesto y tests.

---

## 1) Métricas por campaña

### Fórmulas
- **CTR** = Clicks / Impresiones
- **CPC** = Costo / Clicks
- **CPA** = Costo / Signups
- **Conversion rate** = Signups / Clicks

---

### Campaña A — Landing principal
- Impresiones: 50,000
- Clicks: 1,500
- Signups: 45
- Costo: $2,100

**CTR**
- 1,500 / 50,000 = **3.0%**

**CPC**
- 2,100 / 1,500 = **$1.40**

**CPA**
- 2,100 / 45 = **$46.67**

**Conversion rate**
- 45 / 1,500 = **3.0%**

---

### Campaña B — Blog content
- Impresiones: 120,000
- Clicks: 4,800
- Signups: 24
- Costo: $1,800

**CTR**
- 4,800 / 120,000 = **4.0%**

**CPC**
- 1,800 / 4,800 = **$0.375** → **$0.38**

**CPA**
- 1,800 / 24 = **$75.00**

**Conversion rate**
- 24 / 4,800 = **0.5%**

---

### Campaña C — Competidor
- Impresiones: 15,000
- Clicks: 900
- Signups: 36
- Costo: $3,200

**CTR**
- 900 / 15,000 = **6.0%**

**CPC**
- 3,200 / 900 = **$3.56**

**CPA**
- 3,200 / 36 = **$88.89**

**Conversion rate**
- 36 / 900 = **4.0%**

---

## Resumen en tabla

| Campaña | CTR | CPC | CPA | Conversion Rate |
|---|---:|---:|---:|---:|
| A | 3.0% | $1.40 | $46.67 | 3.0% |
| B | 4.0% | $0.38 | $75.00 | 0.5% |
| C | 6.0% | $3.56 | $88.89 | 4.0% |

---

## 2) ¿Qué campaña escalar y cuál pausar?

### Mi recomendación
- **Escalar: Campaña A**
- **Pausar o reducir fuertemente: Campaña B**
- **Mantener con control: Campaña C**

### Justificación con números

#### Campaña A: mejor balance entre volumen y eficiencia
- Tiene **CPA de $46.67**, el más bajo después de comparar valor real de adquisición.
- Su **conversion rate es 3.0%**, bastante sano.
- CPC moderado (**$1.40**), lo que permite escalar sin que el costo se dispare tan rápido como en C.
- Aunque no tiene el CTR más alto, sí convierte bien.

**Conclusión:** es la mejor candidata para escalar porque combina tráfico decente + conversión buena + CPA razonable.

---

#### Campaña B: mucho tráfico, pero mala calidad de conversión
- Tiene el **CTR alto (4.0%)** y el **CPC más bajo ($0.38)**.
- Pero su **conversion rate es solo 0.5%**, extremadamente bajo.
- Eso hace que el **CPA suba a $75**, peor que A.
- Está atrayendo clics baratos, pero no signups.

**Conclusión:** es la campaña que más sentido tiene **pausar o reducir** hasta optimizar el mensaje, keywords o landing. Está generando volumen sin retorno suficiente.

---

#### Campaña C: muy buena intención, pero demasiado cara
- Tiene el **mejor CTR (6.0%)** y el **mejor conversion rate (4.0%)**.
- Pero el **CPC es muy alto ($3.56)**.
- Por eso el **CPA termina siendo el peor: $88.89**.

**Conclusión:** no la pausaría de inmediato porque demuestra intención fuerte, pero sí la mantendría con presupuesto limitado y optimización agresiva. Puede ser rentable si el valor por signup es alto o si mejora el CPC.

---

## 3) ¿Cómo redistribuiría el presupuesto de $5,000?

Dado el desempeño actual, una distribución razonable sería:

### Propuesta de presupuesto
- **Campaña A: 50% → $2,500**
- **Campaña C: 30% → $1,500**
- **Campaña B: 20% → $1,000** o incluso **0% si decides pausar**

### Si quieres ser más agresivo:
- **A: $3,000**
- **C: $2,000**
- **B: $0**

### Lógica de la redistribución
- **A** recibe más porque tiene el mejor equilibrio entre costo y conversión.
- **C** recibe presupuesto porque convierte bien, aunque es cara; vale la pena seguir probando.
- **B** se reduce drásticamente porque su conversión es demasiado baja.

---

## 4) A/B tests sugeridos para el próximo mes

### Para Campaña A
Objetivo: bajar CPA y subir conversion rate.

**Tests sugeridos:**
1. **Landing page**
   - Versión A: landing actual
   - Versión B: landing más enfocada en “inventario para pymes” con CTA más directo

2. **CTA**
   - “Solicitar demo”
   - “Probar gratis”
   - “Ver precios”

3. **Mensaje del anuncio**
   - Enfatizar ahorro de tiempo
   - Enfatizar control de stock
   - Enfatizar reducción de errores

---

### Para Campaña B
Objetivo: mejorar calidad del tráfico y la intención.

**Tests sugeridos:**
1. **Cambiar keywords informacionales por semi-comerciales**
   - En vez de “como gestionar inventario”
   - Probar:
     - “software para gestionar inventario”
     - “sistema inventario pymes”
     - “automatizar inventario”

2. **Alinear el contenido con una landing intermedia**
   - Blog → lead magnet / demo suave
   - En lugar de mandar directo a signup duro

3. **CTA contextual**
   - “Descarga plantilla”
   - “Calcula tu inventario ideal”
   - “Ver solución”

---

### Para Campaña C
Objetivo: bajar CPC sin perder intención.

**Tests sugeridos:**
1. **Variantes de anuncio**
   - “Alternativa a [competidor]”
   - “Más simple que [competidor]”
   - “Mejor soporte que [competidor]”

2. **Landing comparativa**
   - Tabla comparativa con ventajas claras
   - Prueba social / casos de éxito

3. **Match type y negativas**
   - Revisar si hay búsquedas irrelevantes
   - Añadir negativas para evitar tráfico de baja intención

---

## Recomendación final corta

- **Escalar:** Campaña A
- **Reducir/pausar:** Campaña B
- **Mantener y optimizar:** Campaña C

### Distribución sugerida:
- **A: $2,500**
- **C: $1,500**
- **B: $1,000** o **$0** si quieres priorizar eficiencia

Si quieres, también puedo hacerte una **proyección de signups esperados con el presupuesto de $5,000** usando el CPA actual de cada campaña.