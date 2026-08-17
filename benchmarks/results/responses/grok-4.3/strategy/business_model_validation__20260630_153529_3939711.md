# Grok 4.3 — strategy/business_model_validation

- model_id: `x-ai/grok-4.3`
- success: True  | final: 8.18 | quality: 9.42
- latency_total: 18.079s | tokens_per_second: 89.2
- input_tokens: 289 | output_tokens: 1613

## Respuesta completa

**Aquí va la versión sin filtro:**

### 1. Los 5 riesgos principales del modelo

- **Riesgo de liquidez bilateral extremo**: Este no es un marketplace de productos digitales. Es un marketplace de bienes perecederos con restricciones logísticas. Si no logras densidad geográfica brutal en un radio muy pequeño (máximo 8-12 km), el modelo se muere. La mayoría de marketplaces de alimentos fallan aquí.
- **Comisión del 15% es suicida en el segmento que estás atacando**: Restaurantes pequeños en LATAM suelen tener márgenes netos de 8-15%. Un proveedor local que ya opera con márgenes ajustados no va a absorber 15%. O lo absorbe el restaurante (y se queja), o lo absorbe el proveedor (y desaparece). ¿Quién paga realmente esa comisión en la práctica?
- **Logística de último kilómetro de productos frescos es brutalmente cara y frágil**: No estás vendiendo libros ni ropa. Estás moviendo carne, pescado, hierbas y lácteos con control de temperatura, devoluciones y alta tasa de reclamos. El costo real de servir una orden pequeña suele comerse la comisión.
- **Relaciones personales > precio en este segmento**: Muchos chefs y dueños de restaurantes pequeños mantienen relaciones con 2-3 proveedores porque les fián, les dan mejor calidad en persona, o les resuelven cuando hay quiebre de stock. Un marketplace no resuelve el "fiado" ni la confianza personal.
- **Baja retención estructural**: El switching cost es muy bajo. Un restaurante puede usar tu plataforma un mes cuando le conviene y volver a llamar directamente cuando el proveedor le ofrece mejor precio por fuera. Esto genera un modelo de "punta de lanza" en vez de retención.

### 2. Por qué probablemente no funciona en LATAM (específicamente)

- La informalidad es altísima. Muchos proveedores pequeños no quieren facturar, no quieren dejar rastro de ventas, y operan en efectivo. Obligarlos a pasar por una plataforma formal reduce drásticamente la oferta.
- La fragmentación es tan alta que el costo de adquisición por proveedor es caro y la calidad es inconsistente. Un proveedor puede ser excelente un día y pésimo al siguiente. Tú heredas ese problema de calidad.
- El poder de negociación está del lado de los restaurantes medianos/grandes, no de los pequeños. Los proveedores decentes prefieren venderle a quien les compra volumen.
- La infraestructura de entrega (especialmente en ciudades como CDMX, Bogotá, Lima o São Paulo) hace que los tiempos y costos sean impredecibles. Una helada o un taco de tráfico te rompe la promesa de frescura.

### 3. Qué tendría que ser verdad para que funcione

- Que los restaurantes pequeños estén dispuestos a pagar (directa o indirectamente) 12-15% más por el mismo producto solo por la conveniencia de no hacer llamadas. Esto es la hipótesis más peligrosa.
- Que exista suficiente oferta de proveedores que ya tengan excedente de capacidad y estén dispuestos a vender a precios más bajos que los mayoristas tradicionales (para compensar la comisión).
- Que puedas alcanzar densidad mínima viable (mínimo 25-30 restaurantes activos + suficientes proveedores) en un radio geográfico pequeño sin quemar más de $40-50k.
- Que el ticket promedio por orden sea lo suficientemente alto como para que el 15% justifique los costos operativos y logísticos.
- Que los dueños de restaurantes pequeños (que suelen ser los que toman decisiones) usen realmente una app en vez de WhatsApp.

### 4. Escenario de fracaso rápido

Lanzas en una ciudad, logras meter 40-50 restaurantes en los primeros 3 meses con subsidios o descuentos, pero solo 8-12 proveedores serios se activan consistentemente. Los restaurantes hacen 1-2 órdenes y luego desaparecen porque la oferta es limitada, los precios no son mejores, o la calidad es inconsistente. 

En 5-6 meses tienes un marketplace con baja actividad, CAC alto, y los proveedores que entraron se van porque no reciben suficiente volumen. Quedas con un producto que nadie usa consistentemente y te quedas sin runway.

Este es el final más común de este tipo de marketplaces.

### 5. Con $10K para validar

No construyas nada.

Toma $3,000-4,000 y contrata a 2-3 personas (o hazlo tú) para hacer un experimento manual de concierge en un barrio específico durante 6-8 semanas. 

El experimento real es:
- Consigue 15-20 restaurantes pequeños y 8-10 proveedores.
- Haz el matching manualmente (WhatsApp + coordinación de entregas).
- Cobra la comisión del 15% real en cada transacción.
- Mide cuántos restaurantes repiten más de 3 veces cuando ya no hay subsidio y cuando el precio no es mejor que su proveedor actual.

Si después de 6 semanas no logras que al menos 8-10 restaurantes hagan pedidos recurrentes pagando comisión completa (sin descuentos), el modelo no funciona. El resto es cope.

Todo lo demás (app bonita, onboarding, catálogo) es irrelevante hasta que pruebes que alguien está dispuesto a pagar consistentemente ese 15%.