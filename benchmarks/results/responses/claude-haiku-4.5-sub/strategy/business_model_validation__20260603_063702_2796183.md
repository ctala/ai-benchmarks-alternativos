# Claude Haiku 4.5 (suscripción) — strategy/business_model_validation

- model_id: `claude-haiku-4-5`
- success: True  | final: 7.77 | quality: 9.9
- latency_total: 38.359s | tokens_per_second: 87.1
- input_tokens: 10 | output_tokens: 3340
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Pitch Review: Marketplace Restaurantes ↔ Proveedores Locales

No le voy a dar validación barata. Aquí está el análisis crudo.

---

## **LOS 5 RIESGOS QUE MATAN ESTE MODELO**

### 1. **El problema que describes ya está "resuelto" (mal, pero resuelto)**
Los restaurantes pequeños usan:
- Proveedores establecidos con relaciones personales de 5-10 años
- Crédito informal (pagan a fin de mes sin contrato)
- Negociación verbal de precios
- Un proveedor que les entrega TODO (aunque sea caro)

Tu marketplace les pide:
- Cambiar flujos operativos
- Aprender una app nueva
- Volver a negociar con desconocidos cada semana

**El costo de switching es altísimo**. No compites con Didi Delivery. Compites con "mi compadre el distribuidor que me conoce hace 8 años."

### 2. **El unit economics está roto a escala pequeña**
Un restaurante pequeño en LATAM:
- Gasta ~$2-5K/mes en ingredientes
- Tu 15% = $300-750/mes de comisión POR restaurante
- Necesitas 50-80 restaurantes ACTIVOS para pagar a 1 persona full-time ($600-800/mes)
- En una ciudad pequeña/mediana, hay máximo 100-150 restaurantes

**¿Cómo escala esto?** Si conquistaste una ciudad (70 restaurantes), ganaste $15-20K/mes pero el costo de adquisición fue probably $30K+. Y no puedes copiar el modelo a otra ciudad sin duplicar ops.

### 3. **Los proveedores no tienen incentivos claros**
¿Por qué un distribuidor de verduras con ruta establecida usaría tu plataforma?

- Pierde información de clientes (antes les vendía directo, ahora vende a través tuyo)
- Pierde control de precios (competencia transparente con otros proveedores)
- Tu comisión es SOBRE su margen, no sobre tu costo (a ellos les importa si ganan menos)
- Si yo soy proveedor, prefiero crecer mi fuerza de ventas directa

**Especialmente en LATAM**, donde los proveedores son PyMEs también y no tienen la sofisticación para ver "volume growth" de corto plazo.

### 4. **Pricing opacity es tu fortaleza y tu debilidad**
Hoy un restaurante paga caro porque no sabe el precio real. Tu app lo transparenta.

- Resultado: los restaurantes negocian MEJOR (baja comisión)
- Los proveedores se dan cuenta de que estaban cobrando 40% arriba de mercado → quieren vender directo
- Tu margen se erosiona o los restaurantes te abandonan de todas formas

### 5. **Logística + pagos = complejidad legal + operativa que NO ves**
- ¿Quién es responsable si llega comida en mal estado? (el proveedor directo dice: "tu plataforma", el cliente dice: "ustedes")
- ¿Cómo manejas insolvencia de restaurantes? (15% de comisión asume que la transacción se cierra; en LATAM muchos restaurantes cierran sin pagar deudas)
- Impuestos: ¿eres intermediario o realizador de la operación? (LATAM es unclear, cambia por país)
- Pagos: ¿TÚ pagas al proveedor o el restaurante lo hace? (si tú lo haces, es flujo de caja de $50K+ mensual sin garantía de cobro)

---

## **POR QUÉ PODRÍA NO FUNCIONAR EN LATAM ESPECÍFICAMENTE**

### **El contexto es diferente de USA/Europa:**

1. **Confianza < Digital**
   - Los restaurantes generalmente NO usan apps para B2B crítico. Llaman por teléfono.
   - Adoption de B2B SaaS en LATAM es 3-5 años atrás respecto a USA.
   - Un restaurante que factura $30K/mes no va a poner supply chain en una app desconocida.

2. **Proveedores desorganizados + sin estandarización**
   - En Chile hay ~500 distribuidoras de alimentos. Ninguna sabe su propio precio list actualizado.
   - Muchas NO tienen API, integración, ni quieren tecn.
   - Para que TÚ muestres "Proveedor A: $2.50/kg, Proveedor B: $2.80/kg", ELLOS tienen que estar en tu sistema. ¿Quién les paga eso?

3. **Márgenes del proveedor son FINOS**
   - Un distribuidor gana 12-18% de margen bruto
   - Tu 15% de comisión es casi LA MITAD DE SU GANANCIA
   - Simplemente no van a usarlo

4. **Restaurantes pequeños = finanzas informales**
   - Muchos pagan en efectivo al proveedor
   - No usan POS integrado
   - Defaultearán pagos o usarán mal la plataforma
   - **El riesgo crediticio es TUYO si manejas pagos.**

5. **Competencia local brutal**
   - En cada ciudad hay ya 2-3 distribuidoras grandes que conocen a todos
   - En Chile: Asplosa, Makro, Wong tienen relación directa con restaurantes
   - ¿Cómo compites contra eso sin escala nacional?

---

## **¿QUÉ TENDRÍA QUE SER VERDAD PARA QUE FUNCIONE?**

Para que esto NO sea un fracaso, TODAS estas cosas tienen que pasar:

1. **Los restaurantes REALMENTE pierden 10+ horas/mes llamando proveedores** (no 2 llamadas de rutina)
   - Y esas 10 horas valen >$750/mes (cantidad de ahorro que justifica cambio)
   - ✗ En LATAM, el costo de mano de obra es tan bajo que esto es improbable

2. **Los proveedores ganan VOLUMEN a través tuyo** que compensa perder margen
   - Ej: "a través del marketplace triplicaré mis clientes de restaurantes"
   - ✗ No hay prueba de esto. Típicamente el proveedor pierde información.

3. **Hay un gap de información real** entre restaurante y proveedor
   - Que el restaurante no pueda resolver con 3 llamadas
   - ✗ En LATAM, las relaciones personales CIERRAN esta brecha

4. **La logística es simple** (proveedores ya hacen entregas, no necesitas cuadrar rutas)
   - ✓ Esto es verdad, pero es el 10% del problema
   - ✗ El 90% (pricing, pagos, confianza) sigue siendo duro

5. **Tienes >30% de restaurantes penetration en una ciudad antes de expandir**
   - Y eso se logra sin subsidios o con subsidios que NO escalan

---

## **ESCENARIO DE FRACASO RÁPIDO (6 MESES)**

Así es cómo lo veo caer:

**Mes 1-2:** Lanzan en una ciudad (ej. Santiago). Hacen manual outreach a 50 restaurantes.
- Convencen a 10 (20% conversion) con descuentos/comisión gratis
- Los proveedores entran con desconfianza ("¿qué es esto?")

**Mes 3:** Los primeros 10 restaurantes hacen 2-3 órdenes cada uno, experimentan.
- Resultado: algunos proveedores están más caros que directo
- Restaurantes vuelven a sus proveedores viejos
- Drop: 40% de restaurantes ya no usan la app

**Mes 4:** Intentan pivotar a "descuentos", pero:
- Para subsidiar restaurantes necesitan proveedores en volumen
- Para conseguir proveedores, necesitan restaurantes (chicken-egg)
- Dinero se quema en customer acquisition que no pega

**Mes 5-6:** El equipo se da cuenta:
- Las transacciones que ocurren NO alcanzan para pagar ops
- Los proveedores no quieren vender a margen reducido
- Los restaurantes realmente prefieren sus proveedores viejos
- Pivot forzado o shutdown

---

## **SI TIENES SOLO $10K, AQUÍ ESTÁ LO QUE HARÍA** (No lo que dices)

**NOT:**
- ❌ Armar una app web/mobile ($5-8K)
- ❌ Hacer marketing digital ($3-5K)
- ❌ Registrar empresa, pedir permisos

**SÍ (Validation sprint 4 semanas):**

**Semana 1 - Validar premisa ($0)**
- Entrevista 20 restaurantes (30 min cada uno)
  - Pregunta exacta: "¿Cuánto tiempo a la SEMANA gastas llamando proveedores? ¿Cuánto de eso sería resuelto por una app?"
  - Si responden <2 horas: STOP. No hay problema.
  - Si responden 8+ horas: avanza. Pero probablemente digan <2.

**Semana 2 - Validar oferta proveedor ($200 en coffees)**
- Entrevista 15 distribuidoras / proveedores
  - "¿Usarían una plataforma donde restaurantes los encuentren? ¿A qué comisión?"
  - Si dicen "no, prefiero mis clientes directos": esto es tu respuesta.
  - Si dicen "sí, pero a <5% comisión": los math no cierran.

**Semana 3 - Manual MVP ($500 Zapier + Airtable)**
- Crea form en Airtable (restaurantes = demanda, proveedores = oferta)
- Zapier conecta órdenes manual entre ellos (tú eres el marketplace = una persona)
- 2 restaurantes, 3 proveedores, 5 órdenes reales
- Métricas: ¿se completan las órdenes? ¿los que no vuelven, por qué?

**Semana 4 - Decisión ($0)**
- Si hiciste 20 órdenes y 60%+ se repitieron: hay algo
- Si hiciste 5 órdenes y 80% fue "una sola vez, gracias": no hay producto

---

## **MI VEREDICTO**

Este es un **problema real pero NO es problema TUYO resolver.**

✗ Unit economics roto en LATAM  
✗ Proveedores desincentivados  
✗ Restaurantes con alternativas  
✗ Finanzas informales en target market  

**El modelo SÍ funcionaría si:**
- Fueras un **proveedor grande con 50+ proveedores pequeños** que quieren vender (pero entonces no es marketplace, eres distribuidor)
- O si creyeras que los restaurantes van a adoptar **basándose en una feature que NO existe** (ej. financiamiento = "pequeño crédito a 30 días"; pero eso requiere onboarding crediticio que es carísimo)

**Alternativas que **sí tendrían lógica:**
1. **Sell TO los proveedores grandes** (Wong, Makro, Asplosa): "una app para gestionar sus clientes restaurante" (software, no marketplace)
2. **Solve financing:** "Línea de crédito para restaurantes que compran juntos" (el marketplace es el vehículo de cobranza)
3. **B2B ordering para cadenas pequeñas** (10-20 restaurantes, 1 dueño): Aquí SÍ hay eficiencia porque es 1 toma-decisiones

**Mi recomendación:**
Gasta los $10K validando SI el problema es real antes de construir. Apuesto a que descubres que los restaurantes pequeños en LATAM **no** pierden 8+ horas/mes en esto. Y si NO pierden ese tiempo, no cambian de proveedor.

¿Quieres que profundice en alguno de estos puntos?