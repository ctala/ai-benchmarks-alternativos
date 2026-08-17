# Nemotron 3 Ultra 550B — agent_long_horizon/implicit_state_construction

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.29 | quality: 8.5
- latency_total: 65.313s | tokens_per_second: 213.8
- input_tokens: 21023 | output_tokens: 10392

## Respuesta completa

### **Campaña “Aurora: Tu Piel, Nivel Experto”**  
**Producto exclusivo:** **Set Aurora** (Cuidado facial premium – 3 pasos: Limpiador enzimático + Sérum Péptidos 5 % + Crema Barrera Ceramidas)  
**Objetivo único:** **Vender 40 sets Aurora en 4 semanas** (≈ 10/sem) con **CAC ≤ $55.000 COP** y **ROAS ≥ 4.5x**.  
**Presupuesto total sugerido:** **$8.000.000 COP** (≈ $2.000.000/sem – 70 % Meta, 20 % Google, 10 % WhatsApp retargeting).

---

## 1. AUDIENCIAS (Configuración técnica exacta)

| Plataforma | Audiencia | Detalle técnico Bogotá |
|------------|-----------|------------------------|
| **Meta (Frío)** | **Lookalike 1 % “Compradores Aurora 90 d”** | Si no hay semilla aún → **Intereses apilados**: “Skincare” + “Ácido hialurónico” + “Dermocosmética” + “Belleza premium” + **Comportamiento**: “Compradores online frecuentes” + **Ubicación**: Bogotá (radio 15 km desde Chapinero) + **Edad**: 25-45 + **Género**: Mujeres + **NSE**: Meta “Alto” (códigos postales 110111, 110221, 111111, 110121, 110131). |
| **Meta (Tibio)** | **Visitantes web 30 d – Vieron Aurora / Página “Rutina Bogotá”** | Evento `ViewContent` product_id=AURORA + `PageView` rutina_bogota. Excluir compradores 180 d. |
| **Meta (Caliente)** | **Iniciaron checkout Aurora 7 d (no compraron)** | Evento `InitiateCheckout` value > $300k. |
| **Google (Search)** | **Palabras exactas / frase** | `[set cuidado facial premium Bogotá]`, `[sérum péptidos 5% Colombia]`, `[rutina antiage noche domicilio Bogotá]`, `[crema ceramidas envío mismo día]`. Negativas: “barato”, “oferta”, “mayoreo”, “Botica Verde”, “Skin Lab”. |
| **Google (Shopping / PMax)** | **Feed solo Aurora** | `custom_label_0 = "premium"`, `custom_label_1 = "bogota_sameday"`. Prioridad de puja alta. |
| **WhatsApp (Retargeting)** | **Lista “Click WhatsApp Aurora 14 d – No compra”** | Exportar de WA Business / ManyChat → subir a Meta como Custom Audience → campaña “Click to WhatsApp” solo para esta lista. |

---

## 2. MENSAJE PRINCIPAL (Concepto rector + 3 ángulos creativos)

**Concepto:** **“La única rutina nocturna con péptidos al 5 % y ceramidas idénticas a la piel, formulada para el clima de Bogotá y en tu puerta hoy.”**  
*Diferenciadores claves incrustados: % real, clima local, velocidad, ciencia vs. “natural” genérico de competidores.*

| Ángulo | Gancho (3 s) | Cuerpo (15-20 s) | CTA final |
|--------|--------------|------------------|-----------|
| **A. Ciencia Abierta** | “¿Tu sérum dice ‘péptidos’ pero no dice cuánto?” | Primer plano etiqueta Aurora: “Péptidos 5 % - Clinicamente probado”. Comparativa visual: frasco Aurora vs. frasco genérico “péptidos” (texto borroso). Voz en off: “Nosotras ponemos el % en la cara”. | “Pide tu diagnóstico gratis y recibe Aurora hoy en [Barrio]”. |
| **B. Noche Bogotana** | Split screen: 22:00 frío Chapinero / 22:00 calor Kennedy. | Misma rutina Aurora: limpieza suave → sérum ligero → crema barrera. Texto: “Una fórmula, todos los microclimas de Bogotá”. UGC real clienta en balcón con taza de té. | “Arma tu rutina Bogotá → WhatsApp”. |
| **C. Unboxing Experto** | Mano abre caja kraft sellada sticker “Empacado por Camila – Hoy”. | Saca: 1) Sobre monodosis “Prueba mañana” 2) Tarjeta QR “Video rutina 30 seg” 3) Set Aurora. Close-up textura sérum (gota lenta) + crema (sin residuo). | “Envío gratis mismo día > $150k. Pide el tuyo”. |

**Formatos requeridos (entrega lunes semana 1):**  
- 3 Reels verticales (9:16) con subtítulos quemados.  
- 3 Carruseles estáticos (ingrediente estrella, FAQ “¿Para qué piel?”, Comparativa vs. competidor sin nombre).  
- 1 Video horizontal 16:9 (YouTube Shorts / Google Video partners) versión 30 s ángulo A.  
- 5 Imágenes estáticas 1:1 + 4:5 para Shopping / Display / WhatsApp catálogo.

---

## 3. PLAN SEMANAL (Ejecución día a día)

| Semana | Foco | Acciones clave (Quién / Qué / Cuándo) | Presupuesto (COP) | Métrica semanal “Semáforo” |
|--------|------|----------------------------------------|-------------------|----------------------------|
| **1 – Lanzamiento & Aprendizaje** | Tráfico frío + Pixel | **Lun**: Subir catálogo Aurora + UTM `campaign=aurora_launch`. <br>**Mar**: Activar **Meta CBO** 3 ad sets (Frío Lookalike/Intereses, Tibio Web 30d, Caliente Checkout 7d) – 3 creativos cada uno. <br>**Mié**: Activar **Google Search + Shopping** solo Aurora. <br>**Jue**: Revisar CTR > 1.2 % / CPC < $1.200 → apagar peores. <br>**Vie**: Subir mejor Reels orgánico a **Spark Ads** (tibio). <br>**Sáb**: WhatsApp broadcast “Lista Aurora” (clientas Luna/Sol) – sample gratis si piden hoy. | $2.000.000 | 🟢 CTR ≥ 1.2 % <br>🟢 CPC ≤ $1.200 <br>🟢 5 pedidos |
| **2 – Optimización & UGC** | Conversión + Prueba social | **Lun**: Recoger 2 UGC clientas semana 1 (trueque sample Aurora) → editar “Test real 14 días”. <br>**Mar**: Crear **Ad Set “UGC Testimonial”** en Meta (tibio + caliente). <br>**Mié**: Añadir **extensiones de precio y promoción** en Google (“Envío mismo día Chapinero/Usaquén”). <br>**Jue**: A/B landing: **Versión A** diagnóstico 3 preguntas → **Versión B** ficha técnica + “Pide por WhatsApp”. <br>**Vie**: Retargeting WA “Click no compra” – mensaje personalizado “¿Dudas sobre péptidos? Te explico 1 min”. | $2.000.000 | 🟢 CAC ≤ $55k <br>🟢 ROAS ≥ 3.5x <br>🟢 10 pedidos acumulados |
| **3 – Escala Controlada** | Rentabilidad | **Lun**: Duplicar presupuesto **solo** en ad sets Meta con ROAS ≥ 4x (regla automática). <br>**Mar**: Añadir **audiencia “Competidores”** en Meta: “Seguidores Botica Verde / Skin Lab” + excluir compradores. <br>**Mié**: Lanzar **oferta “Combo Aurora + Sample Luna”** (solo 20 sets) – urgencia real. <br>**Jue**: Revisar **Search Terms Report** Google → negar irrelevantes, subir puja exactas rentables. <br>**Vie**: Live 15 min IG “Pregúntale a la formuladora” → guardar en Destacado + clip a Reels. | $2.000.000 | 🟢 ROAS ≥ 4.5x <br>🟢 25 pedidos acumulados <br>🟢 % recurrentes Aurora ≥ 20 % |
| **4 – Cierre & Sistema** | Automatizar lo que funciona | **Lun**: Pausar todo lo < 3x ROAS. <br>**Mar**: Crear **Reglas automáticas Meta**: “Si ROAS 7d < 3 → apagar”, “Si CPA < $50k → +20 % presupuesto”. <br>**Mié**: Documentar **“Playbook Aurora”** (creativos ganadores, audiencias, copies, landing) en Notion. <br>**Jue**: Encuesta NPS compradoras Aurora (WA 1 pregunta). <br>**Vie**: Informe final + decisión: **Evergreen ON / OFF / Iterar**. | $2.000.000 | 🟢 40 pedidos totales <br>🟢 CAC final ≤ $55k <br>🟢 NPS ≥ 65 |

---

## 4. MÉTRICAS DE ÉXITO (Dashboard único – Actualizar Lunes/Viernes)

| KPI | Meta 4 sem | Fuente | Acción si falla |
|-----|------------|--------|-----------------|
| **Sets Aurora vendidos** | **40** | WooCommerce/Shopify (SKU AUR) | Semana 2 < 8 → activar “Combo Aurora+Luna” + micro-influencer trueque. |
| **CAC Blended Aurora** | **≤ $55.000** | (Gasto Meta+Google+WA) / Compradoras nuevas Aurora | > $65k semana 2 → apagar frío, subir % tibio/caliente + UGC. |
| **ROAS Blended** | **≥ 4.5x** | Ingresos Aurora / Gasto total | < 3.5x semana 2 → mejorar landing (test A/B) + subir AOV con cross-sell Sol. |
| **% Pedidos envío mismo día** | **≥ 90 %** | Logística (Mensa/Rappi API) | < 80 % → reducir zona cobertura a 10 km Chapinero. |
| **UGC generados** | **6** (2/sem desde sem 2) | Hashtag #AuroraBogotá + WA | < 3 semana 3 → incentivar “Reto 14 días Aurora” con regalo Sol. |
| **NPS post-compra** | **≥ 65** | Encuesta WA 24 h | < 50 → llamar 5 clientas detectar fricción (textura, olor, empaque). |

---

## 5. CHECKLIST TÉCNICO “CERO ERRORES” (Antes del lunes semana 1)

- [ ] **Pixel / CAPI** disparando `ViewContent` `AddToCart` `InitiateCheckout` `Purchase` **solo con product_id=AURORA**.  
- [ ] **Catálogo Commerce Manager**: 1 item Aurora + 1 combo “Aurora+Luna” (precio bundle).  
- [ ] **UTM obligatorias** en **todos** los enlaces: `utm_source=meta&utm_medium=cpc&utm_campaign=aurora_launch&utm_content={{ad.name}}`.  
- [ ] **Landing / Diagnóstico**: carga < 2.5 s móvil, botón WhatsApp fijo, badge “Envío gratis hoy Bogotá > $150k”.  
- [ ] **WhatsApp Business**: mensaje de bienvenida “👋 Bienvenida a Aurora. ¿Quieres tu diagnóstico 3 preguntas o pides directo?” + etiqueta `aurora_lead`.  
- [ ] **Exclusiones**: Compradores 180 d, empleados, IPs oficina, audiencias “Luna/Sol only” en campañas Aurora.  
- [ ] **Presupuesto diario** configurado en **nivel CBO** (Meta) y **campaña diaria** (Google) – no vitalicio.  

---

### Próximo paso tuyo (hoy)
1. Apruebas **concepto + 3 ángulos** → yo te doy **guiones técnicos** (segundo a segundo) para que grabes el lunes.  
2. Me confirmas **presupuesto exacto semanal** (si ajustas $/sem).  
3. Agendamos **revisión 30 min viernes semana 1** (semáforo).  

¿Arrancamos con los guiones de grabación?