# Qwen 3.6 35B base (OpenRouter FP8) — deep_reasoning/fermi_estimation

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 6.54 | quality: 7.36
- latency_total: 23.183s | tokens_per_second: 152.4
- input_tokens: 76 | output_tokens: 3532
- judge_score: 4.4 | justificación: 

## Respuesta completa

Aquí tienes una estimación estructurada tipo "Fermi", con todos los supuestos explícitos, cálculo paso a paso, rango, mejor estimación y análisis de sensibilidad.

---

### 📌 Marco de cálculo
Calculamos el consumo **por día laboral** (lunes a viernes), ya que el consumo en oficinas está vinculado a la actividad laboral. Se asume que los fines de semana el consumo en oficinas es despreciable.

---

### 🔢 Supuestos numerados

1. **Número total de trabajadores de oficina en Santiago**  
   `1,2 millones` | Rango: `1,0M – 1,4M`  
   *Base:* Población ocupada en Región Metropolitana ~2,8M (INE). Aproximadamente el 40-50% labora en actividades de servicios, administración pública, finanzas, tecnología y corporaciones, con entorno predominantemente de oficina.

2. **Proporción de trabajadores que consume café**  
   `85%` | Rango: `75% – 90%`  
   *Base:* Chile tiene una de las tasas más altas de consumo per cápita de café en Latinoamérica. En entornos corporativos y administrativos, la penetración supera ampliamente el 80%.

3. **Volumen por taza estándar de café en oficina**  
   `250 ml` | Rango: `200 ml – 300 ml`  
   *Base:* Taza de máquina de filtro o granos corporativa (tamaño "mug" o "taza de trabajo"). No se incluye café de barra o preparación artesanal de mayor volumen.

4. **Tazas diarias por bebedor de café**  
   `3 tazas/día` | Rango: `1 – 4 tazas/día`  
   *Base:* Patrón típico: 1 en desayuno, 1 a media mañana, 1 post-almuerzo. Varía según intensidad laboral, disponibilidad de máquina, cultura de empresa y teletrabajo híbrido.

---

### 🧮 Cálculo paso a paso

| Paso | Operación | Valor |
|------|-----------|-------|
| 1 | Trabajadores de oficina | 1.200.000 |
| 2 | Bebedores de café (1.200.000 × 85%) | 1.020.000 |
| 3 | Consumo diario por bebedor (3 tazas × 0,25 L) | 0,75 L/día |
| 4 | **Consumo total diario** (1.020.000 × 0,75 L) | **765.000 L/día laboral** |

**Rango mínimo:**  
1.000.000 × 75% = 750.000 bebedores × (1 taza × 0,20 L) = **150.000 L/día**

**Rango máximo:**  
1.400.000 × 90% = 1.260.000 bebedores × (4 tazas × 0,30 L) = **1.512.000 L/día**

---

### 📊 Resultado final
- **Mejor estimación:** `~750.000 – 800.000 litros por día laboral`
- **Rango plausible:** `150.000 – 1.500.000 litros por día laboral`

*(Nota: si se quisiera extrapolar a días calendario, se multiplicaría por ~5/7 ≈ 0,71, dando ~530.000 L/día calendario como mejor estimación).*

---

### 🔍 Supuesto con mayor impacto

El que más influye en el resultado es el **número de tazas diarias por bebedor (Supuesto 4)**.

**Por qué:**
- Tiene la mayor variabilidad relativa: su rango abarca un factor de **4x** (de 1 a 4 tazas), mientras que el número de trabajadores varía ~1,4x y la proporción de bebedores ~1,2x.
- Es altamente sensible a factores conductuales y estructurales no cuantificables con precisión: intensidad laboral, disponibilidad de café de calidad, políticas de empresa, cultura de pausas, y la adopción de trabajo híbrido (que puede reducir o redistribuir el consumo).
- Un cambio de ±1 taza por persona desplaza el resultado en ±250.000 L/día, lo que representa ~33% del mejor estimado.

---

### 📝 Notas metodológicas
- Esta estimación no incluye consumo en domicilios, cafeterías comerciales, hospitales, universidades ni tiendas.
- No ajusta por días festivos, vacaciones o teletrabajo permanente, que reducirían el consumo promedio real.
- Los rangos reflejan incertidumbre razonable, no error de cálculo. Para precisión operativa se requerirían datos de proveedores corporativos, facturación de granos o encuestas sectoriales.

¿Te gustaría que ajuste el modelo para incluir un subsector específico (ej. banca, gobierno, startups) o que lo exprese en kg de café verde/tostado equivalente?