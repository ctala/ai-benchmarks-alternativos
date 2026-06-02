# Qwen 3.6 Max — strategy/business_model_validation

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.36 | quality: 10.0
- latency_total: 118.224s | tokens_per_second: 30.7
- input_tokens: 179 | output_tokens: 3629
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, abordando los riesgos y desafíos específicos del modelo de negocio en un contexto de mercado B2B y LATAM.

## Respuesta completa

Aquí no hay espacio para validación emocional. Si quieres dinero de verdad, prepárate para que te destrocen la tesis antes de que quemes el primer dólar. Aquí van las preguntas y respuestas que un VC serio te haría en una sala de due diligence:

### 1. Los 5 riesgos principales de este modelo
1. **Desintermediación estructural (leakage):** En cuanto un restaurante y un proveedor se conocen, ¿qué los obliga a seguir pagándote el 15%? Los marketplaces de servicios B2B mueren por esto. Si no hay lock-in tecnológico, contractual o de valor agregado, te conviertes en un directorio gratuito en 2 ciclos de compra.
2. **Comisión del 15% vs márgenes reales:** Los restaurantes pequeños operan con márgenes netos del 3-8%. Los proveedores de ingredientes suelen tener márgenes del 5-12%. Cobrar 15% sobre el ticket es económicamente inviable para ambas partes a menos que subsidies precios o absorbas costos logísticos. Nadie pagará esa prima por "ahorrar llamadas".
3. **Liquidez y chicken-and-egg:** Un marketplace B2B de perecedores requiere densidad geográfica extrema. Si no tienes suficientes proveedores en un radio de 3-5 km, los restaurantes no obtienen frescura ni precios competitivos. Si no tienes restaurantes, los proveedores no suben inventario. La fricción de arranque es brutal.
4. **Logística de perecederos y control de calidad:** No es SaaS. Es cadena de frío, ventanas de entrega estrechas, mermas, devoluciones y reclamos por calidad. ¿Quién asume el costo cuando el tomate llega golpeado o el pescado no pasa inspección? Si lo asumes tú, quemas margen. Si lo delegas, pierdes confianza.
5. **Adopción digital real vs declarada:** En encuestas todos dicen "quiero digitalizarme". En la práctica, el dueño del restaurante está en cocina, con las manos ocupadas, y prefiere un WhatsApp o una llamada de 30 segundos a navegar una app, comparar precios, subir facturas y gestionar pagos. La fricción operativa mata más startups que la falta de demanda.

---

### 2. ¿Por qué podría NO funcionar en LATAM específicamente?
- **Informalidad y economía de efectivo:** Gran parte de los proveedores locales no facturan, operan en cash, y evaden IVA/ISR. Tu plataforma los obliga a formalizar, pagar comisiones y dejar rastro fiscal. Muchos preferirán no entrar.
- **Compras basadas en relación, no en precio/app:** En LATAM, el proveedor le fía, le ajusta el peso, le regala el cilantro, le espera el pago hasta el viernes. Esa confianza no se digitaliza con un marketplace. La lealtad es personal, no transaccional.
- **Infraestructura logística fragmentada:** Tráfico impredecible, falta de cadena de frío accesible, direcciones mal georreferenciadas, y costos de última milla que se comen el margen. Lo que en EE.UU. se resuelve con routing algorithms, aquí se resuelve con motoqueros y paciencia.
- **Alta mortalidad de restaurantes pequeños:** >60% cierran antes de los 2 años. Tu LTV se desploma si tu cliente base rota constantemente. CAC recurrente + churn alto = unidad económica rota.
- **Fragmentación regulatoria y pagos:** Cada país (y a veces cada estado) tiene reglas fiscales distintas para plataformas, retenciones, facturación electrónica y alimentos. Integrar pagos B2B con términos de crédito (30-60 días) es complejo y caro. Si obligas a pago inmediato, pierdes a los restaurantes. Si das crédito, asumes riesgo de cartera.

---

### 3. ¿Qué tendría que ser verdad para que funcione? (Key Assumptions)
1. **El tiempo ahorrado vale >15% del costo de insumos** para el restaurante, y están dispuestos a pagar esa prima de forma recurrente.
2. **Los proveedores aceptan ceder 15% de margen** sin intentar vender directo después del primer match, porque tu plataforma les trae volumen neto nuevo, no solo canibaliza sus clientes actuales.
3. **La frecuencia de compra es alta (≥3x/semana) y el ticket promedio es suficiente** para que CAC < LTV en <6 meses, con churn <5% mensual.
4. **Puedes estandarizar calidad, entrega y pagos** sin convertirte en una empresa logística pesada que quema capital por orden.
5. **La barrera digital es irrelevante o la eliminas por diseño** (ej. pedido por WhatsApp, facturación automática, crédito integrado), no obligando a descargar una app y aprender un flujo nuevo.

Si una de estas falla, el modelo colapsa. No es "ajustar sobre la marcha". Es structural.

---

### 4. Escenario donde fracasas rápido y por qué
**Día 0-30:** Lanzas en una zona. Onboardeas 40 restaurantes y 15 proveedores con visitas puerta a puerta. Subsidias primeras órdenes. Funciona.
**Día 31-60:** Los restaurantes notan que los precios + 15% son mayores que su proveedor habitual. Empiezan a usar la app solo para descubrir proveedores nuevos, luego los contactan directo por WhatsApp. Los proveedores, felices, aceptan el bypass para recuperar su margen.
**Día 61-90:** Tu plataforma se convierte en un catálogo gratuito. Las transacciones recurrentes caen >70%. Tu equipo de soporte gestiona reclamos por calidad y entregas tardías. Quemas cash en retención y descuentos. Churn mensual >15%. LTV/CAC < 0.8.
**Por qué fracasa:** No construiste un moat. Vendiste conveniencia en un mercado donde el precio, la confianza y el crédito dominan. La comisión del 15% aceleró el leakage. Sin lock-in operativo o financiero, el marketplace se drena en 3 meses.

---

### 5. Si solo tuvieras $10K para validar, ¿qué harías?
Cero código. Cero app. Cero branding bonito. Validación quirúrgica o muerte rápida.

**Setup ($10K):**
- $0 en desarrollo. Usas WhatsApp Business + Google Sheets + Notion + enlaces de pago (MercadoPago/Stripe) + un courier local por pedido.
- $2K en proscripción directa: visitas a 15 restaurantes y 8 proveedores en un radio de 2 km. Pagas café, tiempo, y ofreces pilotaje gratuito las primeras 2 semanas.
- $3K en subsidio logístico/control de calidad: pagas entregas puntuales, empaques básicos, y un inspector freelance que valide calidad en las primeras 50 órdenes.
- $2K en herramientas y legal básico: contrato de comisión, facturación electrónica, cuenta bancaria separada, seguro de responsabilidad mínimo.
- $3K colchón operativo para imprevistos y pruebas de pricing.

**Mecánica de validación (4-6 semanas):**
1. Actúas como concierge: el restaurante te manda lista por WhatsApp, tú cotizas con proveedores, consolidas, coordinas entrega, cobras, pagas al proveedor menos 15%, y entregas factura.
2. Mides sin piedad:
   - % de órdenes repetidas después de la semana 2 y 4
   - % de intentos de bypass (te piden contacto directo o pagan fuera)
   - Willingness to pay: ¿aceptan el +15% sin subsidio en la semana 3?
   - Tiempo real ahorrado vs declarado (cronometra el proceso actual vs tu flujo)
   - Margen neto por orden después de logística, soporte y mermas

**Criterios de KILL (no pivot, KILL):**
- <30% de repeat rate en semana 4
- >20% de bypass detectado
- Los restaurantes exigen bajar comisión a <8% para seguir
- Margen operativo por orden <5% después de costos reales
- Churn de proveedores >25% en 30 días

Si pasas los umbrales, iteras pricing, automatizas flujos con no-code, y levantas pre-seed con datos duros, no con hipótesis de pitch deck. Si no los pasas, matas el proyecto antes de quemar $50K en una app que nadie va a usar.

---

**Última realidad:** Los marketplaces B2B de alimentos no se ganan con "conectar". Se ganan con crédito, logística confiable, estandarización de calidad y lock-in financiero. Si tu única propuesta es "ahorrar llamadas", estás construyendo un directorio con comisión de lujo. Valida con números o no levantes capital. El mercado no perdena romanticismo operativo.