# Qwen 3.6 Max — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.33 | quality: 10.0
- latency_total: 105.421s | tokens_per_second: 37.9
- input_tokens: 309 | output_tokens: 3991
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes el análisis completo, paso a paso, con métricas, recomendaciones estratégicas y pruebas accionables.

### 1. Métricas clave por campaña
| Campaña | CTR | CPC | Conversion Rate (CVR) | CPA |
|---------|-----|-----|----------------------|-----|
| **A (Landing principal)** | 3.0% | $1.40 | 3.0% | $46.67 |
| **B (Blog content)** | 4.0% | $0.38 | 0.5% | $75.00 |
| **C (Competidor)** | 6.0% | $3.56 | 4.0% | $88.89 |

*Cálculos:*
- `CTR = (Clicks / Impresiones) × 100`
- `CPC = Costo / Clicks`
- `CVR = (Signups / Clicks) × 100`
- `CPA = Costo / Signups`

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación numérica)

✅ **Escalar: Campaña A**  
- **Mejor eficiencia:** CPA más bajo ($46.67) y CVR sólido (3.0%).  
- **Intención comercial clara:** Keywords como `"software gestion inventario"` indican fondo de embudo.  
- **CPC moderado ($1.40)** deja margen para escalar sin disparar el CPA inmediatamente.  
- **ROI implícito:** Cada signup cuesta menos de la mitad que en C y un 38% menos que en B.

⏸️ **Pausar o reorientar: Campaña B**  
- **CVR muy bajo (0.5%)** y **CPA alto ($75)** a pesar del CPC más barato.  
- Las keywords son informacionales (`"como gestionar..."`), por lo que el tráfico no está listo para convertir.  
- Mantenerla con objetivo de signups directos es ineficiente. Solo tendría sentido si se usa para **remarketing, captura de emails o nutrición de leads**, no para conversión fría.

⚠️ **Mantener controlada: Campaña C**  
- **Mayor CTR (6%) y CVR (4%)**, lo que confirma alta intención.  
- Pero el **CPC ($3.56) y CPA ($88.89)** son los peores, probablemente por subastas agresivas contra competidores.  
- No pausar, pero **optimizar antes de escalar**: ajustar pujas, mejorar landing de comparación y filtrar keywords de baja intención.

---

### 3. Redistribución del presupuesto ($5,000/mes)

*Nota: Tu gasto actual reportado suma $7,100, por lo que esta redistribución asume un límite estricto de $5k hacia adelante.*

| Campaña | Presupuesto sugerido | % del total | Rationale |
|---------|---------------------|-------------|-----------|
| **A (Escalar)** | $3,000 | 60% | Maximiza signups eficientes. Con CPA actual, ~64 signups. Monitorear rendimientos decrecientes al escalar. |
| **C (Optimizar)** | $1,500 | 30% | Mantener presencia en intención alta, pero con topes de puja y landing optimizada. ~17 signups esperados. |
| **B (Reorientar)** | $500 | 10% | Solo si se usa para remarketing, lead magnet o prueba de nueva oferta. De lo contrario, $0. |

**Impacto proyectado:**  
- Signups estimados: ~81-88/mes (vs 105 con $7.1k)  
- CPA blended objetivo: ~$56-$62 (vs ~$67.6 actual)  
- Mayor eficiencia y control del CAC. Ajustar semanalmente según curva de rendimientos.

---

### 4. A/B Tests sugeridos para el próximo mes

#### 🔹 Campaña A (Escalar con eficiencia)
| Variable | Test | Hipótesis | Métrica a vigilar |
|----------|------|-----------|-------------------|
| Landing Page | Formulario corto (3 campos) vs largo (5-6) | Menos fricción → +CVR sin perder calidad | CVR, CPA, tasa de activación post-signup |
| Copy de anuncio | Enfoque en beneficio ("Reduce mermas un 30%") vs funcionalidad ("Control de stock en tiempo real") | Mensaje orientado a dolor convierte mejor | CTR, CVR, CPA |
| Estrategia de puja | Max Clicks con límite CPC vs tCPA ($45) | Automatización enfocada en conversión estabiliza CPA al escalar | CPA, volumen de signups |

#### 🔹 Campaña B (Reorientar o pausar)
| Variable | Test | Hipótesis | Métrica a vigilar |
|----------|------|-----------|-------------------|
| Oferta en blog | CTA a demo directa vs lead magnet (checklist/plantilla Excel) | Tráfico informativo convierte mejor con valor intermedio | CVR a lead, costo por lead, tasa de nurturing→signup |
| Audiencia | Tráfico frío vs remarketing (visitantes blog 30d) | Usuarios ya expuestos al contenido convierten mejor | CVR, CPA, frecuencia |

#### 🔹 Campaña C (Bajar CPA sin perder intención)
| Variable | Test | Hipótesis | Métrica a vigilar |
|----------|------|-----------|-------------------|
| Landing Page | Página genérica vs tabla comparativa directa ("Nosotros vs [Competidor]") | Comparación explícita reduce dudas y aumenta CVR | CVR, tiempo en página, CPA |
| Keywords | Broad/Phrase vs Exact + long-tail ("alternativa a [competidor] para restaurantes") | Filtrar intención baja reduce CPC sin perder conversiones | CPC, CVR, CPA, Search Terms |
| Copy de anuncio | Enfoque en migración fácil ("Importa tus datos en 5 min") vs precio ("30% más barato") | Reducir percepción de riesgo mejora conversión en tráfico competidor | CTR, CVR, CPA |

#### 🔄 Tests transversales recomendados
- **Tracking:** Verificar que el evento `signup` se dispare correctamente y excluir conversiones duplicadas o de baja calidad.
- **Dayparting/Dispositivos:** Analizar CVR por hora y dispositivo. Ajustar bids -20%/+20% donde el CPA se dispare.
- **Negative Keywords:** En B y C, añadir términos como `"gratis"`, `"excel"`, `"pdf"`, `"curso"` para filtrar tráfico no comercial.

---

### ✅ Próximos pasos accionables
1. Implementar la redistribución 60/30/10 y pausar pujas agresivas en C.
2. Lanzar 2 A/B tests simultáneos (uno en A, uno en C) con duración mínima de 14 días o 30 conversiones por variante.
3. Configurar alertas de CPA > $55 en A y > $80 en C para ajustes rápidos.
4. Si B se mantiene, cambiar objetivo a `Leads` o `Page Engagement` y conectar con secuencia de email nurturing.

¿Quieres que te arme una plantilla de seguimiento semanal (Google Sheets) con estas métricas y umbrales de alerta, o prefiero profundizar en la estructura de la landing comparativa para la Campaña C?