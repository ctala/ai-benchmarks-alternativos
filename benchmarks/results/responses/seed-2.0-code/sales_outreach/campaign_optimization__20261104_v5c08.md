# Seed 2.0 Code — sales_outreach/campaign_optimization

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 1.2 | quality: 0.0
- latency_total: 163.395s | tokens_per_second: 62.6
- input_tokens: 332 | output_tokens: 10236

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa

Here's the complete, functional web application for analyzing your Google Ads campaigns:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Análisis Google Ads - Optimización de Campañas</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gray-900 text-white min-h-screen p-6">
    <div class="max-w-7xl mx-auto">
        <h1 class="text-4xl font-bold text-center mb-2 bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
            📊 Análisis de Campañas Google Ads
        </h1>
        <p class="text-gray-400 text-center mb-8">Presupuesto total: $5,000/mes</p>

        <!-- Input Section -->
        <div class="bg-gray-800 rounded-2xl p-6 mb-8 shadow-xl">
            <h2 class="text-xl font-semibold mb-4 flex items-center gap-2">
                <span>📝</span> Datos de las Campañas
            </h2>
            <div class="grid md:grid-cols-3 gap-4" id="campaignsInput">
                <!-- Campaign A -->
                <div class="bg-gray-700/50 rounded-xl p-4 border-2 border-blue-500/30">
                    <h3 class="font-bold text-blue-400 mb-3">Campaña A (Landing Principal)</h3>
                    <div class="space-y-2 text-sm">
                        <div class="flex justify-between">
                            <span class="text-gray-400">Impresiones:</span>
                            <input type="number" value="50000" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="A" data-field="impressions">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Clicks:</span>
                            <input type="number" value="1500" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="A" data-field="clicks">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Signups:</span>
                            <input type="number" value="45" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="A" data-field="conversions">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Costo ($):</span>
                            <input type="number" value="2100" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="A" data-field="cost">
                        </div>
                    </div>
                </div>

                <!-- Campaign B -->
                <div class="bg-gray-700/50 rounded-xl p-4 border-2 border-green-500/30">
                    <h3 class="font-bold text-green-400 mb-3">Campaña B (Blog Content)</h3>
                    <div class="space-y-2 text-sm">
                        <div class="flex justify-between">
                            <span class="text-gray-400">Impresiones:</span>
                            <input type="number" value="120000" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="B" data-field="impressions">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Clicks:</span>
                            <input type="number" value="4800" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="B" data-field="clicks">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Signups:</span>
                            <input type="number" value="24" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="B" data-field="conversions">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Costo ($):</span>
                            <input type="number" value="1800" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="B" data-field="cost">
                        </div>
                    </div>
                </div>

                <!-- Campaign C -->
                <div class="bg-gray-700/50 rounded-xl p-4 border-2 border-purple-500/30">
                    <h3 class="font-bold text-purple-400 mb-3">Campaña C (Competidor)</h3>
                    <div class="space-y-2 text-sm">
                        <div class="flex justify-between">
                            <span class="text-gray-400">Impresiones:</span>
                            <input type="number" value="15000" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="C" data-field="impressions">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Clicks:</span>
                            <input type="number" value="900" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="C" data-field="clicks">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Signups:</span>
                            <input type="number" value="36" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="C" data-field="conversions">
                        </div>
                        <div class="flex justify-between">
                            <span class="text-gray-400">Costo ($):</span>
                            <input type="number" value="3200" class="w-32 bg-gray-600 rounded px-2 py-1 text-right" data-campaign="C" data-field="cost">
                        </div>
                    </div>
                </div>
            </div>
            <div class="mt-4 flex gap-4">
                <button onclick="calculate()" class="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 px-6 py-2 rounded-lg font-semibold transition-all transform hover:scale-105">
                    🔄 Calcular Análisis
                </button>
                <button onclick="resetDefaults()" class="bg-gray-600 hover:bg-gray-500 px-4 py-2 rounded-lg transition-all">
                    ↩️ Valores Originales
                </button>
            </div>
        </div>

        <!-- Results Section -->
        <div id="results" class="space-y-8">
            <!-- Question 1: Metrics -->
            <div class="bg-gray-800 rounded-2xl p-6 shadow-xl">
                <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
                    <span class="bg-blue-500 text-white w-8 h-8 rounded-full flex items-center justify-center text-sm">1</span>
                    Métricas por Campaña (CTR, CPC, CPA, Tasa de Conversión)
                </h2>
                <div class="overflow-x-auto">
                    <table class="w-full text-sm">
                        <thead>
                            <tr class="border-b border-gray-700">
                                <th class="text-left py-3 px-4">Campaña</th>
                                <th class="text-right py-3 px-4">CTR</th>
                                <th class="text-right py-3 px-4">CPC</th>
                                <th class="text-right py-3 px-4">CPA</th>
                                <th class="text-right py-3 px-4">Conv. Rate</th>
                                <th class="text-center py-3 px-4">Status</th>
                            </tr>
                        </thead>
                        <tbody id="metricsTable">
                            <!-- Dynamic content -->
                        </tbody>
                    </table>
                </div>
                
                <!-- Metric Cards -->
                <div class="grid md:grid-cols-3 gap-4 mt-6" id="metricCards">
                    <!-- Dynamic content -->
                </div>
            </div>

            <!-- Question 2: Recommendations -->
            <div class="bg-gray-800 rounded-2xl p-6 shadow-xl">
                <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
                    <span class="bg-green-500 text-white w-8 h-8 rounded-full flex items-center justify-center text-sm">2</span>
                    Recomendaciones: ¿Escalar o Pausar?
                </h2>
                <div id="recommendations" class="space-y-4">
                    <!-- Dynamic content -->
                </div>
            </div>

            <!-- Question 3: Budget Redistribution -->
            <div class="bg-gray-800 rounded-2xl p-6 shadow-xl">
                <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
                    <span class="bg-purple-500 text-white w-8 h-8 rounded-full flex items-center justify-center text-sm">3</span>
                    Redistribución del Presupuesto ($5,000)
                </h2>
                
                <div class="grid md:grid-cols-2 gap-8">
                    <!-- Chart -->
                    <div class="flex flex-col items-center">
                        <h3 class="font-semibold mb-4 text-gray-300">Nueva Distribución</h3>
                        <div class="relative w-64 h-64">
                            <svg viewBox="0 0 100 100" class="w-full h-full transform -rotate-90" id="budgetChart">
                                <!-- Dynamic content -->
                            </svg>
                            <div class="absolute inset-0 flex items-center justify-center">
                                <div class="text-center">
                                    <div class="text-2xl font-bold">$5,000</div>
                                    <div class="text-xs text-gray-400">Presupuesto</div>
                                </div>
                            </div>
                        </div>
                        <div class="flex gap-4 mt-4 text-sm" id="chartLegend">
                            <!-- Dynamic content -->
                        </div>
                    </div>

                    <!-- Budget Table -->
                    <div>
                        <h3 class="font-semibold mb-4 text-gray-300">Comparativa de Presupuesto</h3>
                        <table class="w-full text-sm">
                            <thead>
                                <tr class="border-b border-gray-700">
                                    <th class="text-left py-2">Campaña</th>
                                    <th class="text-right py-2">Actual</th>
                                    <th class="text-right py-2">Recomendado</th>
                                    <th class="text-right py-2">Cambio</th>
                                    <th class="text-right py-2">Signups Est.</th>
                                </tr>
                            </thead>
                            <tbody id="budgetTable">
                                <!-- Dynamic content -->
                            </tbody>
                        </table>
                        
                        <div class="mt-6 bg-gradient-to-r from-green-500/20 to-blue-500/20 rounded-xl p-4 border border-green-500/30">
                            <h4 class="font-semibold text-green-400 mb-2">📈 Resultado Estimado</h4>
                            <div class="grid grid-cols-2 gap-4 text-sm">
                                <div>
                                    <span class="text-gray-400">Signups actuales:</span>
                                    <span class="font-bold text-white ml-2" id="currentSignups">105</span>
                                </div>
                                <div>
                                    <span class="text-gray-400">Signups estimados:</span>
                                    <span class="font-bold text-green-400 ml-2" id="estimatedSignups">+0%</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Question 4: A/B Tests -->
            <div class="bg-gray-800 rounded-2xl p-6 shadow-xl">
                <h2 class="text-2xl font-bold mb-6 flex items-center gap-2">
                    <span class="bg-orange-500 text-white w-8 h-8 rounded-full flex items-center justify-center text-sm">4</span>
                    Tests A/B Sugeridos para el Próximo Mes
                </h2>
                <div class="grid md:grid-cols-2 gap-4" id="abTests">
                    <!-- Dynamic content -->
                </div>
            </div>
        </div>

        <!-- Summary -->
        <div class="mt-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl p-6 shadow-xl">
            <h2 class="text-2xl font-bold mb-4">🎯 Resumen Ejecutivo</h2>
            <div id="summary" class="text-lg leading-relaxed">
                <!-- Dynamic content -->
            </div>
        </div>
    </div>

    <script>
        const campaigns = {
            A: {
                name: "Campaña A",
                fullName: "Campaña A (Landing Principal)",
                color: "#3B82F6",
                keywords: ['"software gestion inventario"', '"inventario pymes"']
            },
            B: {
                name: "Campaña B",
                fullName: "Campaña B (Blog Content)",
                color: "#22C55E",
                keywords: ['"como gestionar inventario"', '"problemas inventario restaurante"']
            },
            C: {
                name: "Campaña C",
                fullName: "Campaña C (Competidor)",
                color: "#A855F7",
                keywords: ['"alternativa a [competidor]"', '"[competidor] vs"']
            }
        };

        function getCampaignData() {
            const data = {};
            ['A', 'B', 'C'].forEach(campaign => {
                data[campaign] = {
                    impressions: parseInt(document.querySelector(`[data-campaign="${campaign}"][data-field="impressions"]`).value) || 0,
                    clicks: parseInt(document.querySelector(`[data-campaign="${campaign}"][data-field="clicks"]`).value) || 0,
                    conversions: parseInt(document.querySelector(`[data-campaign="${campaign}"][data-field="conversions"]`).value) || 0,
                    cost: parseInt(document.querySelector(`[data-campaign="${campaign}"][data-field="cost"]`).value) || 0
                };
            });
            return data;
        }

        function calculateMetrics(data) {
            return {
                ctr: data.clicks > 0 ? ((data.clicks / data.impressions) * 100) : 0,
                cpc: data.clicks > 0 ? (data.cost / data.clicks) : 0,
                cpa: data.conversions > 0 ? (data.cost / data.conversions) : Infinity,
                conversionRate: data.clicks > 0 ? ((data.conversions / data.clicks) * 100) : 0
            };
        }

        function getScore(metrics, data) {
            let score = 0;
            
            if (metrics.cpa <= 50) score += 30;
            else if (metrics.cpa <= 75) score += 20;
            else if (metrics.cpa <= 100) score += 10;
            else score -= 10;

            if (metrics.conversionRate >= 5) score += 25;
            else if (metrics.conversionRate >= 3) score += 20;
            else if (metrics.conversionRate >= 1) score += 10;
            else score -= 5;

            if (metrics.ctr >= 4) score += 15;
            else if (metrics.ctr >= 2) score += 10;
            else if (metrics.ctr >= 1) score += 5;

            if (metrics.cpc <= 0.8) score += 20;
            else if (metrics.cpc <= 1.5) score += 15;
            else if (metrics.cpc <= 3) score += 10;
            else score -= 10;

            if (data.conversions >= 30) score += 10;

            return Math.max(0, score);
        }

        function getBudgetRecommendation(key, metrics, data, totalBudget) {
            const score = getScore(metrics, data);
            
            if (score >= 70) {
                return { action: "ESCALAR", percentage: 0.50, reason: "Excelente rendimiento: CPA bajo y alta tasa de conversión" };
            } else if (score >= 40) {
                return { action: "MANTENER", percentage: 0.30, reason: "Rendimiento aceptable, optimizar gradualmente" };
            } else {
                return { action: "PAUSAR/REDUCIR", percentage: 0.20, reason: "Bajo rendimiento: CPA alto o baja conversión" };
            }
        }

        function formatCurrency(num) {
            if (num === Infinity) return "∞";
            return "$" + num.toFixed(2);
        }

        function calculate() {
            const data = getCampaignData();
            const totalBudget = 5000;
            
            const metrics = {};
            const scores = {};
            const recommendations = {};
            
            let totalScore = 0;
            ['A', 'B', 'C'].forEach(key => {
                metrics[key] = calculateMetrics(data[key]);
                scores[key] = getScore(metrics[key], data[key]);
                totalScore += scores[key];
                recommendations[key] = getBudgetRecommendation(key, metrics[key], data[key], totalBudget);
            });

            const normalizedScores = {};
            ['A', 'B', 'C'].forEach(key => {
                normalizedScores[key] = totalScore > 0 ? scores[key] / totalScore : 0.33;
            });

            const currentTotalConversions = data['A'].conversions + data['B'].conversions + data['C'].conversions;
            
            let estimatedTotalConversions = 0;
            ['A', 'B', 'C'].forEach(key => {
                const newBudget = normalizedScores[key] * totalBudget;
                const conversionsPerDollar = data[key].cost > 0 ? data[key].conversions / data[key].cost : 0;
                estimatedTotalConversions += newBudget * conversionsPerDollar;
            });

            renderMetricsTable(data, metrics, scores);
            renderMetricCards(data, metrics);
            renderRecommendations(data, metrics, scores, recommendations);
            renderBudgetChart(data, metrics, normalizedScores, totalBudget);
            renderBudgetTable(data, metrics, normalizedScores, totalBudget, currentTotalConversions, estimatedTotalConversions);
            renderABTests(data, metrics);
            renderSummary(data, metrics, scores, normalizedScores, currentTotalConversions, estimatedTotalConversions);
        }

        function renderMetricsTable(data, metrics, scores) {
            const tbody = document.getElementById('metricsTable');
            tbody.innerHTML = '';
            
            const sortedKeys = Object.keys(scores).sort((a, b) => scores[b] - scores[a]);
            
            sortedKeys.forEach((key, index) => {
                const m = metrics[key];
                const d = data[key];
                const campaign = campaigns[key];
                
                const statusColors = [
                    { bg: 'bg-green-500/20', text: 'text-green-400', label: '🏆 Mejor' },
                    { bg: 'bg-yellow-500/20', text: 'text-yellow-400', label: '⚡ Regular' },
                    { bg: 'bg-red-500/20', text: 'text-red-400', label: '⚠️ Peor' }
                ];
                
                const status = statusColors[index];
                
                tbody.innerHTML += `
                    <tr class="border-b border-gray-700/50 hover:bg-gray-700/30">
                        <td class="py-3 px-4">
                            <div class="flex items-center gap-2">
                                <div class="w-3 h-3 rounded-full" style="background-color: ${campaign.color}"></div>
                                <span class="font-medium">${campaign.fullName}</span>
                            </div>
                        </td>
                        <td class="text-right py-3 px-4">
                            <span class="${m.ctr >= 3 ? 'text-green-400' : m.ctr >= 1.5 ? 'text-yellow-400' : 'text-red-400'} font-semibold">
                                ${m.ctr.toFixed(2)}%
                            </span>
                        </td>
                        <td class="text-right py-3 px-4">
                            <span class="${m.cpc <= 1 ? 'text-green-400' : m.cpc <= 2 ? 'text-yellow-400' : 'text-red-400'}">
                                ${formatCurrency(m.cpc)}
                            </span>
                        </td>
                        <td class="text-right py-3 px-4">
                            <span class="${m.cpa <= 50 ? 'text-green-400 font-bold' : m.cpa <= 80 ? 'text-yellow-400' : 'text-red-400'}">
                                ${formatCurrency(m.cpa)}
                            </span>
                        </td>
                        <td class="text-right py-3 px-4">
                            <span class="${m.conversionRate >= 4 ? 'text-green-400 font-bold' : m.conversionRate >= 2 ? 'text-yellow-400' : 'text-red-400'}">
                                ${m.conversionRate.toFixed(2)}%
                            </span>
                        </td>
                        <td class="text-center py-3 px-4">
                            <span class="${status.bg} ${status.text} px-3 py-1 rounded-full text-xs font-medium">
                                ${status.label}
                            </span>
                        </td>
                    </tr>
                `;
            });
        }

        function renderMetricCards(data, metrics) {
            const container = document.getElementById('metricCards');
            container.innerHTML = '';
            
            ['A', 'B', 'C'].forEach(key => {
                const campaign = campaigns[key];
                const m = metrics[key];
                const d = data[key];
                
                container.innerHTML += `
                    <div class="bg-gray-700/50 rounded-xl p-5 border-l-4" style="border-color: ${campaign.color}">
                        <h4 class="font-bold mb-4" style="color: ${campaign.color}">${campaign.name}</h4>
                        <div class="grid grid-cols-2 gap-3 text-sm">
                            <div>
                                <div class="text-gray-400 text-xs">CTR</div>
                                <div class="font-semibold ${m.ctr >= 3 ? 'text-green-400' : 'text-gray-200'}">${m.ctr.toFixed(2)}%</div>
                            </div>
                            <div>
                                <div class="text-gray-400 text-xs">CPC</div>
                                <div class="font-semibold">${formatCurrency(m.cpc)}</div>
                            </div>
                            <div>
                                <div class="text-gray-400 text-xs">CPA</div>
                                <div class="font-semibold ${m.cpa <= 50 ? 'text-green-400' : m.cpa >= 100 ? 'text-red-400' : ''}">${formatCurrency(m.cpa)}</div>
                            </div>
                            <div>
                                <div class="text-gray-400 text-xs">Conv. Rate</div>
                                <div class="font-semibold ${m.conversionRate >= 4 ? 'text-green-400' : ''}">${m.conversionRate.toFixed(2)}%</div>
                            </div>
                        </div>
                        <div class="mt-4 pt-4 border-t border-gray-600 text-xs text-gray-400">
                            Keywords: ${campaign.keywords.join(', ')}
                        </div>
                    </div>
                `;
            });
        }

        function renderRecommendations(data, metrics, scores, recommendations) {
            const container = document.getElementById('recommendations');
            container.innerHTML = '';
            
            const sortedKeys = Object.keys(scores).sort((a, b) => scores[b] - scores[a]);
            
            sortedKeys.forEach(key => {
                const campaign = campaigns[key];
                const m = metrics[key];
                const d = data[key];
                const rec = recommendations[key];
                const score = scores[key];
                
                const actionColors = {
                    "ESCALAR": { bg: 'bg-green-500/20', border: 'border-green-500', text: 'text-green-400', icon: '🚀' },
                    "MANTENER": { bg: 'bg-yellow-500/20', border: 'border-yellow-500', text: 'text-yellow-400', icon: '⚡' },
                    "PAUSAR/REDUCIR": { bg: 'bg-red-500/20', border: 'border-red-500', text: 'text-red-400', icon: '🛑' }
                };
                
                const style = actionColors[rec.action];
                
                container.innerHTML += `
                    <div class="${style.bg} border ${style.border} rounded-xl p-5">
                        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                            <div class="flex items-center gap-4">
                                <div class="w-12 h-12 rounded-full ${style.bg} flex items-center justify-center text-2xl" style="border-color: ${campaign.color}; border: 2px solid">
                                    ${style.icon}
                                </div>
                                <div>
                                    <h4 class="font-bold text-lg" style="color: ${campaign.color}">${campaign.fullName}</h4>
                                    <p class="text-gray-400 text-sm">${rec.reason}</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-6">
                                <div class="text-center">
                                    <div class="text-xs text-gray-400">Score</div>
                                    <div class="text-2xl font-bold ${style.text}">${score}/100</div>
                                </div>
                                <div class="text-center">
                                    <div class="text-xs text-gray-400">CPA</div>
                                    <div class="text-xl font-semibold">${formatCurrency(m.cpa)}</div>
                                </div>
                                <div class="text-center">
                                    <div class="text-xs text-gray-400">Conversiones</div>
                                    <div class="text-xl font-semibold">${d.conversions}</div>
                                </div>
                                <div class="px-4 py-2 rounded-lg ${style.bg} border ${style.border}">
                                    <span class="font-bold ${style.text}">${rec.action}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
            });
        }

        function renderBudgetChart(data, metrics, normalizedScores, totalBudget) {
            const chart = document.getElementById('budgetChart');
            const legend = document.getElementById('chartLegend');
            
            let cumulativePercent = 0;
            let paths = '';
            let legendHtml = '';
            
            const sortedKeys = Object.keys(normalizedScores).sort((a, b) => normalizedScores[b] - normalizedScores[a]);
            
            sortedKeys.forEach(key => {
                const percent = normalizedScores[key];
                const campaign = campaigns[key];
                const budget = percent * totalBudget;
                
                const startAngle = cumulativePercent * 360;
                const endAngle = (cumulativePercent + percent) * 360;
                
                const x1 = 50 + 40 * Math.cos((startAngle - 90) * Math.PI / 180);
                const y1 = 50 + 40 * Math.sin((startAngle - 90) * Math.PI / 180);
                const x2 = 50 + 40 * Math.cos((endAngle - 90) * Math.PI / 180);
                const y2 = 50 + 40 * Math.sin((endAngle - 90) * Math.PI / 180);
                
                const largeArc = percent > 0.5 ? 1 : 0;
                
                paths += `<path d="M 50 50 L ${x1} ${y1} A 40 40 0 ${largeArc} 1 ${x2} ${y2} Z" fill="${campaign.color}" stroke="#1f2937" stroke-width="2"/>`;
                
                legendHtml += `
                    <div class="flex items-center gap-2">
                        <div class="w-3 h-3 rounded-full" style="background-color: ${campaign.color}"></div>
                        <span class="text-xs">${campaign.name}: ${(percent * 100).toFixed(0)}% ($${budget.toFixed(0)})</span>
                    </div>
                `;
                
                cumulativePercent += percent;
            });
            
            chart.innerHTML = paths;
            legend.innerHTML = legendHtml;
        }

        function renderBudgetTable(data, metrics, normalizedScores, totalBudget, currentConversions, estimatedConversions) {
            const tbody = document.getElementById('budgetTable');
            tbody.innerHTML = '';
            
            const currentTotalSpent = data['A'].cost + data['B'].cost + data['C'].cost;
            
            Object.keys(normalizedScores).forEach(key => {
                const campaign = campaigns[key];
                const newBudget = normalizedScores[key] * totalBudget;
                const oldBudget = data[key].cost;
                const change = newBudget - oldBudget;
                const changePercent = oldBudget > 0 ? ((change / oldBudget) * 100) : 0;
                
                const conversionsPerDollar = oldBudget > 0 ? data[key].conversions / oldBudget : 0;
                const estimatedConversionsForCampaign = newBudget * conversionsPerDollar;
                
                tbody.innerHTML += `
                    <tr class="border-b border-gray-700/50">
                        <td class="py-3">
                            <div class="flex items-center gap-2">
                                <div class="w-3 h-3 rounded-full" style="background-color: ${campaign.color}"></div>
                                <span>${campaign.name}</span>
                            </div>
                        </td>
                        <td class="text-right py-3 text-gray-400">$${oldBudget.toFixed(0)}</td>
                        <td class="text-right py-3 font-semibold">$${newBudget.toFixed(0)}</td>
                        <td class="text-right py-3">
                            <span class="${change >= 0 ? 'text-green-400' : 'text-red-400'} font-medium">
                                ${change >= 0 ? '+' : ''}$${change.toFixed(0)}
                                <span class="text-xs">(${changePercent >= 0 ? '+' : ''}${changePercent.toFixed(0)}%)</span>
                            </span>
                        </td>
                        <td class="text-right py-3">
                            <span class="text-blue-400">${estimatedConversionsForCampaign.toFixed(0)}</span>
                            <span class="text-xs text-gray-500"> (actual: ${data[key].conversions})</span>
                        </td>
                    </tr>
                `;
            });
            
            document.getElementById('currentSignups').textContent = `${currentConversions}`;
            
            const liftPercent = estimatedConversions > currentConversions 
                ? ((estimatedConversions - currentConversions) / currentConversions * 100) 
                : 0;
            
            document.getElementById('estimatedSignups').textContent = 
                `${estimatedConversions.toFixed(0)} (+${liftPercent.toFixed(0)}%)`;
        }

        function renderABTests(data, metrics) {
            const container = document.getElementById('abTests');
            
            const tests = [
                {
                    campaign: "A",
                    title: "Test de Landing Page",
                    description: "Probar 2 variaciones de landing page: actual vs. versión con más pruebas sociales (casos de éxito, logos de clientes).",
                    hypothesis: "Aumentar la tasa de conversión en un 20-30%",
                    metric: "Tasa de conversión (Signups / Clicks)",
                    priority: "🔴 Alta"
                },
                {
                    campaign: "A",
                    title: "Test de Copys en Anuncios",
                    description: "Actual: 'Software de Gestión de Inventario'. Variaciones: 'Controla tu Inventario en 5 Minutos' vs 'Reduce Perdidas por Inventario Mal Gestionado'.",
                    hypothesis: "Mejorar el CTR y atraer clicks más calificados",
                    metric: "CTR y Tasa de Conversión",
                    priority: "🔴 Alta"
                },
                {
                    campaign: "B",
                    title: "Test de CTA en Blog",
                    description: "Probar diferentes ubicaciones y textos de CTA en los artículos del blog: popup vs. inline vs. final del artículo.",
                    hypothesis: "Aumentar la tasa de conversión de usuarios que llegan por contenido informativo",
                    metric: "Tasa de Conversión",
                    priority: "🟡 Media"
                },
                {
                    campaign: "B",
                    title: "Test de Segmentación de Palabras Clave",
                    description: "Separar las keywords informativas ('como gestionar') de las de problema ('problemas inventario') en grupos de anuncios diferentes.",
                    hypothesis: "Mejorar relevancia del anuncio y reducir CPC",
                    metric: "CTR, CPC, Posición Promedio",
                    priority: "🟡 Media"
                },
                {
                    campaign: "C",
                    title: "Test de Comparativas en Landing Page",
                    description: "Crear una landing page dedicada de comparación vs. competidor con tabla detallada de ventajas, pricing y features.",
                    hypothesis: "Aumentar significativamente la tasa de conversión de esta campaña",
                    metric: "Tasa de Conversión y CPA",
                    priority: "🔴 Alta"
                },
                {
                    campaign: "C",
                    title: "Test de Ofertas Especiales",
                    description: "Probar anuncios con oferta exclusiva para usuarios de competidores: '20% descuento si vienes de [Competidor]'.",
                    hypothesis: "Mejorar CTR y conversiones a pesar del CPC alto",
                    metric: "CTR y Tasa de Conversión",
                    priority: "🟢 Baja"
                }
            ];
            
            container.innerHTML = tests.map(test => {
                const campaign = campaigns[test.campaign];
                return `
                    <div class="bg-gray-700/30 rounded-xl p-5 border-l-4 hover:bg-gray-700/50 transition-all" style="border-color: ${campaign.color}">
                        <div class="flex items-center justify-between mb-3">
                            <span class="text-xs px-2 py-1 rounded-full" style="background-color: ${campaign.color}30; color: ${campaign.color}">
                                ${campaign.name}
                            </span>
                            <span class="text-xs">${test.priority}</span>
                        </div>
                        <h4 class="font-bold mb-2">${test.title}</h4>
                        <p class="text-sm text-gray-400 mb-3">${test.description}</p>
                        <div class="text-xs space-y-1">
                            <div class="flex items-start gap-2">
                                <span class="text-green-400">💡 Hipótesis:</span>
                                <span class="text-gray-300">${test.hypothesis}</span>
                            </div>
                            <div class="flex items-start gap-2">
                                <span class="text-blue-400">📏 KPI:</span>
                                <span class="text-gray-300">${test.metric}</span>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function renderSummary(data, metrics, scores, normalizedScores, currentConversions, estimatedConversions) {
            const container = document.getElementById('summary');
            
            const sortedKeys = Object.keys(scores).sort((a, b) => scores[b] - scores[a]);
            const bestCampaign = sortedKeys[0];
            const worstCampaign = sortedKeys[2];
            
            const liftPercent = estimatedConversions > currentConversions 
                ? ((estimatedConversions - currentConversions) / currentConversions * 100) 
                : 0;
            
            container.innerHTML = `
                <p class="mb-4">
                    Basado en el análisis de tus campañas Google Ads del último mes, 
                    <strong class="text-yellow-400">${campaigns[bestCampaign].name}</strong> es la de mejor rendimiento 
                    con un CPA de <strong>${formatCurrency(metrics[bestCampaign].cpa)}</strong> y una tasa de conversión de 
                    <strong>${metrics[bestCampaign].conversionRate.toFixed(2)}%</strong>.
                </p>
                <p class="mb-4">
                    La recomendación principal es <strong class="text-green-400">escalar ${campaigns[bestCampaign].name}</strong> 
                    ya que tiene el mejor balance entre costo por adquisición y volumen de conversiones. 
                    <strong class="text-yellow-400">${campaigns[sortedKeys[1]].name}</strong> debe mantenerse pero optimizarse, 
                    mientras que <strong class="text-red-400">${campaigns[worstCampaign].name}</strong> requiere cambios significativos 
                    (su CPA de ${formatCurrency(metrics[worstCampaign].cpa)} es el más alto).
                </p>
                <p>
                    Al redistribuir el presupuesto de $5,000 basado en rendimiento, puedes esperar aproximadamente 
                    <strong class="text-green-400">${estimatedConversions.toFixed(0)} signups</strong>, 
                    lo que representa un aumento de ~<strong class="text-green-400">${liftPercent.toFixed(0)}%</strong> 
                    sobre los ${currentConversions} actuales.
                </p>
            `;
        }

        function resetDefaults() {
            const defaults = {
                A: { impressions: 50000, clicks: 1500, conversions: 45, cost: 2100 },
                B: { impressions: 120000, clicks: 4800, conversions: 24, cost: 1800 },
                C: { impressions: 15000, clicks: 900, conversions: 36, cost: 3200 }
            };
            
            ['A', 'B', 'C'].forEach(campaign => {
                document.querySelector(`[data-campaign="${campaign}"][data-field="impressions"]`).value = defaults[campaign].impressions;
                document.querySelector(`[data-campaign="${campaign}"][data-field="clicks"]`).value = defaults[campaign].clicks;
                document.querySelector(`[data-campaign="${campaign}"][data-field="conversions"]`).value = defaults[campaign].conversions;
                document.querySelector(`[data-campaign="${campaign}"][data-field="cost"]`).value = defaults[campaign].cost;
            });
            
            calculate();
        }

        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('change', calculate);
            input.addEventListener('input', calculate);
        });

        calculate();
    </script>
</body>
</html>
```

This is a complete, self-contained web application that provides a comprehensive analysis of your Google Ads campaigns. Here's what it includes:

## Key Features:

### 1. Interactive Metrics Dashboard
- Calculates and displays CTR, CPC, CPA, and Conversion Rate for each campaign
- Color-coded performance indicators (green = good, yellow = average, red = poor)
- Detailed metric cards with campaign-specific information

### 2. Budget Optimization
- Recommends budget redistribution based on campaign performance scores
- Visual pie chart showing new budget allocation
- Comparative table with actual vs. recommended budget, changes, and estimated conversions

### 3. Campaign Recommendations
- Ranks campaigns by performance
- Provides clear recommendations: Escalar (Scale), Mantener (Maintain), or Pausar/Reducir (Pause/Reduce)
- Justifications with numerical data (CPA, conversion rate, score)

### 4. A/B Test Suggestions
- Campaign-specific test ideas to improve performance
- Hypotheses and KPIs for each test
- Priority levels (High/Medium/Low)
- Tests for landing pages, ad copies, CTAs, keyword segmentation, and offers

### 5. Executive Summary
- Summarizes key findings in clear language
- Highlights the best and worst performing campaigns
- Provides estimated impact of budget changes
- Actionable recommendations

### 6. Interactive Features
- Editable input fields to update campaign data
- "Calculate" button to refresh analysis
- "Reset to Defaults" button to restore original values
- Real-time updates when inputs change

## Design Highlights:
- Modern dark theme with gradient accents
- Responsive grid layout that works on all devices
- Clean visual hierarchy with clear section headers
- Smooth transitions and hover effects
- Tailwind CSS for styling (CDN version included)
- SVG pie chart for budget visualization
- Comprehensive tables and cards for data display

All functionality is implemented in a single HTML file, making it easy to run and share. The application provides professional-grade analysis to help you optimize your Google Ads campaigns effectively.