# Seed 2.0 Code — task_management/project_breakdown

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 4.13 | quality: 4.4
- latency_total: 382.76s | tokens_per_second: 59.6
- input_tokens: 97 | output_tokens: 22824
- judge_score: 1 | justificación: La respuesta proporciona un diseño HTML en lugar de un desglose de proyecto en fases, tareas, dependencias, responsables y un timeline, lo cual no cumple con la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Here's a complete, functional project plan for the inventory management SaaS landing page, following your requirements:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plan de Proyecto: Landing Page SaaS de Inventario</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 py-8">
        <!-- Header -->
        <header class="bg-gradient-to-r from-indigo-600 to-purple-600 rounded-2xl p-8 mb-8 text-white shadow-xl">
            <div class="flex items-center justify-between flex-wrap gap-4">
                <div>
                    <h1 class="text-3xl font-bold mb-2">🚀 Plan de Proyecto: Landing Page SaaS</h1>
                    <p class="text-indigo-100 text-lg">StockMaster Pro - Sistema de Gestión de Inventario</p>
                </div>
                <div class="flex gap-3">
                    <span class="bg-white/20 px-4 py-2 rounded-full text-sm font-medium">⏱️ 4 Semanas</span>
                    <span class="bg-white/20 px-4 py-2 rounded-full text-sm font-medium">👥 4 Personas</span>
                </div>
            </div>
        </header>

        <!-- Team Section -->
        <section class="mb-8">
            <h2 class="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                <span>👥</span> Equipo del Proyecto
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div class="bg-white rounded-xl p-5 shadow-md border-l-4 border-pink-500">
                    <div class="text-3xl mb-2">🎨</div>
                    <h3 class="font-bold text-gray-800">Diseñador</h3>
                    <p class="text-gray-500 text-sm">UI/UX & Prototipado</p>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-md border-l-4 border-blue-500">
                    <div class="text-3xl mb-2">💻</div>
                    <h3 class="font-bold text-gray-800">Dev 1</h3>
                    <p class="text-gray-500 text-sm">Frontend & Componentes</p>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-md border-l-4 border-green-500">
                    <div class="text-3xl mb-2">⚙️</div>
                    <h3 class="font-bold text-gray-800">Dev 2</h3>
                    <p class="text-gray-500 text-sm">Integraciones & Deploy</p>
                </div>
                <div class="bg-white rounded-xl p-5 shadow-md border-l-4 border-yellow-500">
                    <div class="text-3xl mb-2">✍️</div>
                    <h3 class="font-bold text-gray-800">Copywriter</h3>
                    <p class="text-gray-500 text-sm">Contenido & Estrategia</p>
                </div>
            </div>
        </section>

        <!-- Tabs Navigation -->
        <div class="bg-white rounded-xl shadow-md mb-8 overflow-hidden">
            <div class="flex border-b overflow-x-auto">
                <button onclick="showTab('phases')" id="tab-phases" class="tab-btn px-6 py-4 font-semibold text-indigo-600 border-b-2 border-indigo-600 bg-indigo-50 whitespace-nowrap">
                    📋 Fases & Tareas
                </button>
                <button onclick="showTab('timeline')" id="tab-timeline" class="tab-btn px-6 py-4 font-semibold text-gray-500 hover:text-gray-700 whitespace-nowrap">
                    📊 Timeline Visual
                </button>
                <button onclick="showTab('dependencies')" id="tab-dependencies" class="tab-btn px-6 py-4 font-semibold text-gray-500 hover:text-gray-700 whitespace-nowrap">
                    🔗 Dependencias
                </button>
                <button onclick="showTab('summary')" id="tab-summary" class="tab-btn px-6 py-4 font-semibold text-gray-500 hover:text-gray-700 whitespace-nowrap">
                    📈 Resumen
                </button>
            </div>

            <!-- Tab Content -->
            <div class="p-6">
                <!-- Phases Tab -->
                <div id="content-phases" class="tab-content">
                    <div class="space-y-6">
                        <!-- Phase 1 -->
                        <div class="border rounded-xl overflow-hidden">
                            <button onclick="togglePhase('phase1')" class="w-full bg-gradient-to-r from-blue-500 to-blue-600 text-white p-5 flex justify-between items-center hover:from-blue-600 hover:to-blue-700 transition">
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 w-10 h-10 rounded-full flex items-center justify-center font-bold">1</span>
                                    <div class="text-left">
                                        <h3 class="font-bold text-lg">Semana 1: Planificación & Diseño</h3>
                                        <p class="text-blue-100 text-sm">Definición de estrategia, wireframes y diseño visual</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 px-3 py-1 rounded-full text-sm">5 días</span>
                                    <svg id="icon-phase1" class="w-5 h-5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                    </svg>
                                </div>
                            </button>
                            <div id="phase1" class="phase-content">
                                <div class="p-5 bg-gray-50 space-y-4">
                                    <!-- Task 1.1 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs font-semibold px-2 py-1 rounded">Día 1</span>
                                                    <span class="text-yellow-500">🟡</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Kickoff & Definición de Estrategia</h4>
                                                <p class="text-gray-600 text-sm mt-1">Reunión inicial para alinear objetivos, público objetivo, propuesta de valor y KPIs.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Ninguna
                                                </div>
                                            </div>
                                            <div class="ml-4">
                                                <div class="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
                                                    <div class="w-full h-full bg-blue-500"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 1.2 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs font-semibold px-2 py-1 rounded">Día 1-2</span>
                                                    <span class="text-yellow-500">🟡</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Research & Benchmark</h4>
                                                <p class="text-gray-600 text-sm mt-1">Análisis de competidores, tendencias de diseño para SaaS y mejores prácticas de landing pages.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Kickoff completado
                                                </div>
                                            </div>
                                            <div class="ml-4">
                                                <div class="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
                                                    <div class="w-full h-full bg-blue-500"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 1.3 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs font-semibold px-2 py-1 rounded">Día 2</span>
                                                    <span class="text-yellow-500">🟡</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Definición de Arquitectura de Contenido</h4>
                                                <p class="text-gray-600 text-sm mt-1">Definir secciones de la landing page: Hero, Features, Pricing, Testimonios, FAQ, CTA.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Research completado
                                                </div>
                                            </div>
                                            <div class="ml-4">
                                                <div class="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
                                                    <div class="w-full h-full bg-blue-500"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 1.4 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs font-semibold px-2 py-1 rounded">Día 2-3</span>
                                                    <span class="text-pink-500">🟣</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Wireframes de Baja Fidelidad</h4>
                                                <p class="text-gray-600 text-sm mt-1">Creación de wireframes para todas las secciones, definiendo layout y jerarquía visual.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Arquitectura de contenido aprobada
                                                </div>
                                            </div>
                                            <div class="ml-4">
                                                <div class="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
                                                    <div class="w-full h-full bg-blue-500"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 1.5 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs font-semibold px-2 py-1 rounded">Día 3-5</span>
                                                    <span class="text-yellow-500">🟡</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Redacción de Contenidos (Primera Versión)</h4>
                                                <p class="text-gray-600 text-sm mt-1">Copy para todas las secciones: headlines, body copy, features, CTA buttons, testimonios.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Wireframes aprobados, Arquitectura definida
                                                </div>
                                            </div>
                                            <div class="ml-4">
                                                <div class="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
                                                    <div class="w-full h-full bg-blue-500"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 1.6 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs font-semibold px-2 py-1 rounded">Día 4-5</span>
                                                    <span class="text-pink-500">🟣</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Diseño Visual de Alta Fidelidad</h4>
                                                <p class="text-gray-600 text-sm mt-1">Diseño completo con branding, colores, tipografía, iconografía, imágenes y espaciados.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Wireframes aprobados, Guía de estilo (si existe)
                                                </div>
                                            </div>
                                            <div class="ml-4">
                                                <div class="w-16 h-2 bg-gray-200 rounded-full overflow-hidden">
                                                    <div class="w-full h-full bg-blue-500"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Phase 2 -->
                        <div class="border rounded-xl overflow-hidden">
                            <button onclick="togglePhase('phase2')" class="w-full bg-gradient-to-r from-emerald-500 to-teal-600 text-white p-5 flex justify-between items-center hover:from-emerald-600 hover:to-teal-700 transition">
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 w-10 h-10 rounded-full flex items-center justify-center font-bold">2</span>
                                    <div class="text-left">
                                        <h3 class="font-bold text-lg">Semana 2: Desarrollo Frontend</h3>
                                        <p class="text-emerald-100 text-sm">Implementación de componentes, responsive y animaciones</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 px-3 py-1 rounded-full text-sm">5 días</span>
                                    <svg id="icon-phase2" class="w-5 h-5 transition-transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                    </svg>
                                </div>
                            </button>
                            <div id="phase2" class="phase-content hidden">
                                <div class="p-5 bg-gray-50 space-y-4">
                                    <!-- Task 2.1 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-emerald-100 text-emerald-700 text-xs font-semibold px-2 py-1 rounded">Día 6</span>
                                                    <span class="text-blue-500">🔵</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Setup del Proyecto & Sistema de Diseño</h4>
                                                <p class="text-gray-600 text-sm mt-1">Inicializar repo, configurar Tailwind, definir tokens de diseño (colores, fuentes, spacing, componentes base).</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Diseño visual aprobado
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 2.2 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-emerald-100 text-emerald-700 text-xs font-semibold px-2 py-1 rounded">Día 6-7</span>
                                                    <span class="text-blue-500">🔵</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Componentes Base: Navbar + Hero + Footer</h4>
                                                <p class="text-gray-600 text-sm mt-1">Implementación de las secciones fundamentales de la página. Navegación sticky, hero con CTA principal.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Setup completado, Diseño visual listo
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 2.3 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-emerald-100 text-emerald-700 text-xs font-semibold px-2 py-1 rounded">Día 7-8</span>
                                                    <span class="text-green-500">🟢</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Sección Features + Pricing</h4>
                                                <p class="text-gray-600 text-sm mt-1">Cards de características, grid de pricing con toggle mensual/anual, destacado del plan recomendado.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Setup completado
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 2.4 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-emerald-100 text-emerald-700 text-xs font-semibold px-2 py-1 rounded">Día 8-9</span>
                                                    <span class="text-blue-500">🔵</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Testimonios + Sección FAQ</h4>
                                                <p class="text-gray-600 text-sm mt-1">Carrusel/slider de testimonios con avatares, accordion para FAQ con animaciones suaves.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Componentes base listos
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 2.5 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-emerald-100 text-emerald-700 text-xs font-semibold px-2 py-1 rounded">Día 9-10</span>
                                                    <span class="text-green-500">🟢</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Formulario de Contacto + CTA Final</h4>
                                                <p class="text-gray-600 text-sm mt-1">Formulario de lead capture con validación, sección CTA final, sección de logos de clientes.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Componentes base listos
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 2.6 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-emerald-100 text-emerald-700 text-xs font-semibold px-2 py-1 rounded">Día 10</span>
                                                    <span class="text-yellow-500">🟡</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Revisión y Ajuste de Contenidos</h4>
                                                <p class="text-gray-600 text-sm mt-1">El copywriter revisa todo el contenido implementado, sugiere ajustes de longitud y optimizaciones.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Contenido primer versión, secciones implementadas
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Phase 3 -->
                        <div class="border rounded-xl overflow-hidden">
                            <button onclick="togglePhase('phase3')" class="w-full bg-gradient-to-r from-purple-500 to-pink-600 text-white p-5 flex justify-between items-center hover:from-purple-600 hover:to-pink-700 transition">
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 w-10 h-10 rounded-full flex items-center justify-center font-bold">3</span>
                                    <div class="text-left">
                                        <h3 class="font-bold text-lg">Semana 3: Integraciones & Animaciones</h3>
                                        <p class="text-purple-100 text-sm">Formularios, analytics, animaciones y optimizaciones</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 px-3 py-1 rounded-full text-sm">5 días</span>
                                    <svg id="icon-phase3" class="w-5 h-5 transition-transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                    </svg>
                                </div>
                            </button>
                            <div id="phase3" class="phase-content hidden">
                                <div class="p-5 bg-gray-50 space-y-4">
                                    <!-- Task 3.1 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-purple-100 text-purple-700 text-xs font-semibold px-2 py-1 rounded">Día 11</span>
                                                    <span class="text-green-500">🟢</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Conexión de Formularios (Email Service)</h4>
                                                <p class="text-gray-600 text-sm mt-1">Integrar formularios con Mailchimp/ConvertKit, email de bienvenida automático, webhook si es necesario.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Formulario HTML implementado
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 3.2 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-purple-100 text-purple-700 text-xs font-semibold px-2 py-1 rounded">Día 11-12</span>
                                                    <span class="text-green-500">🟢</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Setup de Analytics & Tracking</h4>
                                                <p class="text-gray-600 text-sm mt-1">Google Analytics 4, Google Tag Manager, eventos de conversión (clicks en CTA, envíos de formulario, scroll).</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Setup inicial del proyecto
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 3.3 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-purple-100 text-purple-700 text-xs font-semibold px-2 py-1 rounded">Día 12-13</span>
                                                    <span class="text-blue-500">🔵</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Animaciones & Micro-interacciones</h4>
                                                <p class="text-gray-600 text-sm mt-1">Scroll reveal animations, hover states en botones y cards, transiciones suaves, parallax ligero.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Todas las secciones implementadas
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 3.4 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-purple-100 text-purple-700 text-xs font-semibold px-2 py-1 rounded">Día 13-14</span>
                                                    <span class="text-blue-500">🔵</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Responsive Design & Mobile Optimization</h4>
                                                <p class="text-gray-600 text-sm mt-1">Ajustes fino para mobile, tablet y desktop. Menu hamburguesa, touch-friendly, optimización de espaciados.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Secciones principales implementadas
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 3.5 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-purple-100 text-purple-700 text-xs font-semibold px-2 py-1 rounded">Día 14-15</span>
                                                    <span class="text-pink-500">🟣</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Optimización de Imágenes & Performance</h4>
                                                <p class="text-gray-600 text-sm mt-1">WebP/AVIF, lazy loading, responsive images, minificación de assets, Lighthouse audit inicial.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Diseño visual completo
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 3.6 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-purple-100 text-purple-700 text-xs font-semibold px-2 py-1 rounded">Día 15</span>
                                                    <span class="text-yellow-500">🟡</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">SEO On-Page Básico</h4>
                                                <p class="text-gray-600 text-sm mt-1">Meta tags, Open Graph, Twitter Cards, schema.org, alt text en imágenes, estructura de encabezados.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Contenidos finalizados
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Phase 4 -->
                        <div class="border rounded-xl overflow-hidden">
                            <button onclick="togglePhase('phase4')" class="w-full bg-gradient-to-r from-amber-500 to-orange-600 text-white p-5 flex justify-between items-center hover:from-amber-600 hover:to-orange-700 transition">
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 w-10 h-10 rounded-full flex items-center justify-center font-bold">4</span>
                                    <div class="text-left">
                                        <h3 class="font-bold text-lg">Semana 4: Testing, Deploy & Lanzamiento</h3>
                                        <p class="text-amber-100 text-sm">QA, UAT, deploy, preparativos de lanzamiento</p>
                                    </div>
                                </div>
                                <div class="flex items-center gap-4">
                                    <span class="bg-white/20 px-3 py-1 rounded-full text-sm">5 días</span>
                                    <svg id="icon-phase4" class="w-5 h-5 transition-transform rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                                    </svg>
                                </div>
                            </button>
                            <div id="phase4" class="phase-content hidden">
                                <div class="p-5 bg-gray-50 space-y-4">
                                    <!-- Task 4.1 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-amber-100 text-amber-700 text-xs font-semibold px-2 py-1 rounded">Día 16</span>
                                                    <span class="text-gray-600">⚫</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Cross-Browser Testing & QA</h4>
                                                <p class="text-gray-600 text-sm mt-1">Pruebas en Chrome, Firefox, Safari, Edge. Dispositivos reales o BrowserStack. Bug tracking.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Desarrollo frontend completo
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 4.2 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-amber-100 text-amber-700 text-xs font-semibold px-2 py-1 rounded">Día 16-17</span>
                                                    <span class="text-gray-600">⚫</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Bug Fixes & Iteraciones</h4>
                                                <p class="text-gray-600 text-sm mt-1">Corrección de bugs encontrados durante testing, ajustes de último minuto, mejoras de UI.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Testing inicial completado
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 4.3 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-amber-100 text-amber-700 text-xs font-semibold px-2 py-1 rounded">Día 17-18</span>
                                                    <span class="text-gray-600">⚫</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">UAT (User Acceptance Testing) & Feedback Stakeholders</h4>
                                                <p class="text-gray-600 text-sm mt-1">Presentación a stakeholders, recolección de feedback, aprobación final para lanzamiento.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Bug fixes completados
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 4.4 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-amber-100 text-amber-700 text-xs font-semibold px-2 py-1 rounded">Día 18</span>
                                                    <span class="text-green-500">🟢</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Setup de Producción & Deploy</h4>
                                                <p class="text-gray-600 text-sm mt-1">Configuración de dominio, SSL, CDN, deploy en Vercel/Netlify, build de producción, verificación post-deploy.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> UAT aprobado
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 4.5 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-amber-100 text-amber-700 text-xs font-semibold px-2 py-1 rounded">Día 19</span>
                                                    <span class="text-yellow-500">🟡</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Preparativos de Lanzamiento</h4>
                                                <p class="text-gray-600 text-sm mt-1">Preparar email de anuncio, banners para redes sociales, copy para lanzamiento, guía de lanzamiento.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Deploy completado
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Task 4.6 -->
                                    <div class="bg-white rounded-lg p-4 shadow-sm border border-gray-100">
                                        <div class="flex items-start justify-between">
                                            <div class="flex-1">
                                                <div class="flex items-center gap-2 mb-2">
                                                    <span class="bg-green-100 text-green-700 text-xs font-semibold px-2 py-1 rounded">Día 20 🚀</span>
                                                    <span class="text-gray-600">⚫</span>
                                                </div>
                                                <h4 class="font-semibold text-gray-800">Día del Lanzamiento</h4>
                                                <p class="text-gray-600 text-sm mt-1">Monitoreo en tiempo real, smoke tests post-lanzamiento, verificación de analytics, monitoreo de formularios.</p>
                                                <div class="mt-3 flex flex-wrap gap-2">
                                                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">💻 Dev 1</span>
                                                    <span class="bg-green-100 text-green-700 text-xs px-2 py-1 rounded">⚙️ Dev 2</span>
                                                    <span class="bg-pink-100 text-pink-700 text-xs px-2 py-1 rounded">🎨 Diseñador</span>
                                                    <span class="bg-yellow-100 text-yellow-700 text-xs px-2 py-1 rounded">✍️ Copywriter</span>
                                                </div>
                                                <div class="mt-2 text-xs text-gray-500">
                                                    <strong>Dependencias:</strong> Todos los checks completados
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Timeline Tab -->
                <div id="content-timeline" class="tab-content hidden">
                    <div class="mb-6">
                        <h3 class="text-lg font-bold text-gray-800 mb-4">📊 Cronograma de 4 Semanas</h3>
                        
                        <!-- Legend -->
                        <div class="flex flex-wrap gap-4 mb-6 p-4 bg-gray-50 rounded-lg">
                            <div class="flex items-center gap-2">
                                <div class="w-4 h-4 bg-blue-500 rounded"></div>
                                <span class="text-sm text-gray-600">Semana 1</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <div class="w-4 h-4 bg-emerald-500 rounded"></div>
                                <span class="text-sm text-gray-600">Semana 2</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <div class="w-4 h-4 bg-purple-500 rounded"></div>
                                <span class="text-sm text-gray-600">Semana 3</span>
                            </div>
                            <div class="flex items-center gap-2">
                                <div class="w-4 h-4 bg-amber-500 rounded"></div>
                                <span class="text-sm text-gray-600">Semana 4</span>
                            </div>
                        </div>

                        <!-- Gantt Chart -->
                        <div class="overflow-x-auto">
                            <table class="w-full min-w-[800px]">
                                <thead>
                                    <tr class="border-b">
                                        <th class="text-left p-3 font-semibold text-gray-700 w-64">Tarea</th>
                                        <th class="text-center p-3 font-semibold text-gray-700" colspan="5">Semana 1</th>
                                        <th class="text-center p-3 font-semibold text-gray-700" colspan="5">Semana 2</th>
                                        <th class="text-center p-3 font-semibold text-gray-700" colspan="5">Semana 3</th>
                                        <th class="text-center p-3 font-semibold text-gray-700" colspan="5">Semana 4</th>
                                    </tr>
                                    <tr class="border-b bg-gray-50">
                                        <th class="text-left p-2 text-xs text-gray-500"></th>
                                        <th class="p-2 text-xs text-gray-500">1</th>
                                        <th class="p-2 text-xs text-gray-500">2</th>
                                        <th class="p-2 text-xs text-gray-500">3</th>
                                        <th class="p-2 text-xs text-gray-500">4</th>
                                        <th class="p-2 text-xs text-gray-500">5</th>
                                        <th class="p-2 text-xs text-gray-500">6</th>
                                        <th class="p-2 text-xs text-gray-500">7</th>
                                        <th class="p-2 text-xs text-gray-500">8</th>
                                        <th class="p-2 text-xs text-gray-500">9</th>
                                        <th class="p-2 text-xs text-gray-500">10</th>
                                        <th class="p-2 text-xs text-gray-500">11</th>
                                        <th class="p-2 text-xs text-gray-500">12</th>
                                        <th class="p-2 text-xs text-gray-500">13</th>
                                        <th class="p-2 text-xs text-gray-500">14</th>
                                        <th class="p-2 text-xs text-gray-500">15</th>
                                        <th class="p-2 text-xs text-gray-500">16</th>
                                        <th class="p-2 text-xs text-gray-500">17</th>
                                        <th class="p-2 text-xs text-gray-500">18</th>
                                        <th class="p-2 text-xs text-gray-500">19</th>
                                        <th class="p-2 text-xs text-gray-500">20</th>
                                    </tr>
                                </thead>
                                <tbody class="text-sm">
                                    <!-- Designer Tasks -->
                                    <tr class="border-b hover:bg-gray-50">
                                        <td class="p-3 font-medium">🎨 Wireframes</td>
                                        <td colspan="2" class="bg-blue-200 rounded m-1 h-8"></td>
                                        <td colspan="18"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50">
                                        <td class="p-3 font-medium">🎨 Diseño Visual</td>
                                        <td colspan="2"></td>
                                        <td colspan="3" class="bg-blue-300 rounded m-1 h-8"></td>
                                        <td colspan="15"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50">
                                        <td class="p-3 font-medium">🎨 Optimización Imágenes</td>
                                        <td colspan="13"></td>
                                        <td colspan="2" class="bg-purple-300 rounded m-1 h-8"></td>
                                        <td colspan="5"></td>
                                    </tr>
                                    
                                    <!-- Dev 1 Tasks -->
                                    <tr class="border-b hover:bg-gray-50 bg-blue-50/30">
                                        <td class="p-3 font-medium">💻 Setup Proyecto</td>
                                        <td colspan="5"></td>
                                        <td class="bg-emerald-300 rounded m-1 h-8"></td>
                                        <td colspan="14"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-blue-50/30">
                                        <td class="p-3 font-medium">💻 Navbar + Hero + Footer</td>
                                        <td colspan="5"></td>
                                        <td colspan="2" class="bg-emerald-300 rounded m-1 h-8"></td>
                                        <td colspan="13"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-blue-50/30">
                                        <td class="p-3 font-medium">💻 Testimonios + FAQ</td>
                                        <td colspan="7"></td>
                                        <td colspan="2" class="bg-emerald-300 rounded m-1 h-8"></td>
                                        <td colspan="11"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-blue-50/30">
                                        <td class="p-3 font-medium">💻 Animaciones</td>
                                        <td colspan="11"></td>
                                        <td colspan="2" class="bg-purple-300 rounded m-1 h-8"></td>
                                        <td colspan="7"></td>
                                    </tr>
                                    
                                    <!-- Dev 2 Tasks -->
                                    <tr class="border-b hover:bg-gray-50 bg-green-50/30">
                                        <td class="p-3 font-medium">⚙️ Features + Pricing</td>
                                        <td colspan="6"></td>
                                        <td colspan="2" class="bg-emerald-300 rounded m-1 h-8"></td>
                                        <td colspan="12"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-green-50/30">
                                        <td class="p-3 font-medium">⚙️ Formulario + CTA</td>
                                        <td colspan="8"></td>
                                        <td colspan="2" class="bg-emerald-300 rounded m-1 h-8"></td>
                                        <td colspan="10"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-green-50/30">
                                        <td class="p-3 font-medium">⚙️ Integraciones</td>
                                        <td colspan="10"></td>
                                        <td colspan="2" class="bg-purple-300 rounded m-1 h-8"></td>
                                        <td colspan="8"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-green-50/30">
                                        <td class="p-3 font-medium">⚙️ Deploy</td>
                                        <td colspan="17"></td>
                                        <td class="bg-amber-400 rounded m-1 h-8"></td>
                                        <td colspan="3"></td>
                                    </tr>
                                    
                                    <!-- Copywriter Tasks -->
                                    <tr class="border-b hover:bg-gray-50 bg-yellow-50/30">
                                        <td class="p-3 font-medium">✍️ Contenidos v1</td>
                                        <td colspan="2"></td>
                                        <td colspan="3" class="bg-blue-300 rounded m-1 h-8"></td>
                                        <td colspan="15"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-yellow-50/30">
                                        <td class="p-3 font-medium">✍️ Revisión Contenidos</td>
                                        <td colspan="9"></td>
                                        <td class="bg-emerald-300 rounded m-1 h-8"></td>
                                        <td colspan="10"></td>
                                    </tr>
                                    <tr class="border-b hover:bg-gray-50 bg-yellow-50/30">
                                        <td class="p-3 font-medium">✍️ SEO + Lanzamiento</td>
                                        <td colspan="14"></td>
                                        <td class="bg-purple-300 rounded m-1 h-8"></td>
                                        <td colspan="3"></td>
                                        <td class="bg-amber-400 rounded m-1 h-8"></td>
                                        <td colspan="2"></td>
                                    </tr>
                                    
                                    <!-- Launch Day -->
                                    <tr class="border-b-2 border-amber-400 bg-amber-50">
                                        <td class="p-3 font-bold text-amber-700">🚀 LANZAMIENTO</td>
                                        <td colspan="19"></td>
                                        <td class="bg-gradient-to-r from-amber-400 to-red-500 rounded m-1 h-8 animate-pulse"></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <!-- Workload Distribution -->
                    <div class="mt-8">
                        <h3 class="text-lg font-bold text-gray-800 mb-4">📈 Distribución de Carga por Rol</h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                            <div class="bg-white p-5 rounded-xl shadow-md">
                                <div class="flex items-center gap-3 mb-4">
                                    <span class="text-3xl">🎨</span>
                                    <div>
                                        <h4 class="font-bold">Diseñador</h4>
                                        <p class="text-sm text-gray-500">8 tareas principales</p>
                                    </div>
                                </div>
                                <div class="space-y-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 1</span>
                                        <span class="font-semibold text-blue-600">Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-blue-500 h-2 rounded-full" style="width: 90%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 2</span>
                                        <span class="font-semibold text-emerald-600">Baja</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-emerald-500 h-2 rounded-full" style="width: 30%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 3-4</span>
                                        <span class="font-semibold text-purple-600">Media</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-purple-500 h-2 rounded-full" style="width: 60%"></div>
                                    </div>
                                </div>
                            </div>

                            <div class="bg-white p-5 rounded-xl shadow-md">
                                <div class="flex items-center gap-3 mb-4">
                                    <span class="text-3xl">💻</span>
                                    <div>
                                        <h4 class="font-bold">Dev 1</h4>
                                        <p class="text-sm text-gray-500">Frontend</p>
                                    </div>
                                </div>
                                <div class="space-y-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 1</span>
                                        <span class="font-semibold text-blue-600">Baja</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-blue-500 h-2 rounded-full" style="width: 20%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 2-3</span>
                                        <span class="font-semibold text-emerald-600">Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-emerald-500 h-2 rounded-full" style="width: 95%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 4</span>
                                        <span class="font-semibold text-amber-600">Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-amber-500 h-2 rounded-full" style="width: 85%"></div>
                                    </div>
                                </div>
                            </div>

                            <div class="bg-white p-5 rounded-xl shadow-md">
                                <div class="flex items-center gap-3 mb-4">
                                    <span class="text-3xl">⚙️</span>
                                    <div>
                                        <h4 class="font-bold">Dev 2</h4>
                                        <p class="text-sm text-gray-500">Integraciones/Deploy</p>
                                    </div>
                                </div>
                                <div class="space-y-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 1-2</span>
                                        <span class="font-semibold text-blue-600">Media-Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-blue-500 h-2 rounded-full" style="width: 75%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 3</span>
                                        <span class="font-semibold text-purple-600">Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-purple-500 h-2 rounded-full" style="width: 90%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 4</span>
                                        <span class="font-semibold text-amber-600">Muy Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-amber-500 h-2 rounded-full" style="width: 100%"></div>
                                    </div>
                                </div>
                            </div>

                            <div class="bg-white p-5 rounded-xl shadow-md">
                                <div class="flex items-center gap-3 mb-4">
                                    <span class="text-3xl">✍️</span>
                                    <div>
                                        <h4 class="font-bold">Copywriter</h4>
                                        <p class="text-sm text-gray-500">Contenido</p>
                                    </div>
                                </div>
                                <div class="space-y-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 1</span>
                                        <span class="font-semibold text-blue-600">Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-blue-500 h-2 rounded-full" style="width: 85%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 2-3</span>
                                        <span class="font-semibold text-emerald-600">Media</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-emerald-500 h-2 rounded-full" style="width: 55%"></div>
                                    </div>
                                </div>
                                <div class="space-y-2 mt-2">
                                    <div class="flex justify-between text-sm">
                                        <span class="text-gray-600">Semana 4</span>
                                        <span class="font-semibold text-amber-600">Alta</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-amber-500 h-2 rounded-full" style="width: 80%"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Dependencies Tab -->
                <div id="content-dependencies" class="tab-content hidden">
                    <h3 class="text-lg font-bold text-gray-800 mb-4">🔗 Mapa de Dependencias</h3>
                    
                    <div class="bg-amber-50 border-l-4 border-amber-400 p-4 rounded-r-lg mb-6">
                        <div class="flex items-start gap-3">
                            <span class="text-2xl">⚠️</span>
                            <div>
                                <h4 class="font-bold text-amber-800">Riesgos Críticos</h4>
                                <p class="text-amber-700 text-sm">Estas dependencias pueden retrasar el proyecto si no se gestionan bien.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Critical Path -->
                    <div class="mb-8">
                        <h4 class="font-bold text-gray-800 mb-4 flex items-center gap-2">
                            <span class="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm">CRITICAL PATH</span>
                        </h4>
                        <div class="flex flex-col md:flex-row items-center gap-2 md:gap-4 overflow-x-auto pb-4">
                            <div class="bg-white border-2 border-red-300 p-4 rounded-xl shadow-md min-w-[180px]">
                                <div class="text-red-500 text-sm font-semibold mb-1">Paso 1</div>
                                <div class="font-bold">Kickoff</div>
                                <div class="text-sm text-gray-500">Día 1</div>
                            </div>
                            <div class="text-red-400 text-2xl">→</div>
                            <div class="bg-white border-2 border-red-300 p-4 rounded-xl shadow-md min-w-[180px]">
                                <div class="text-red-500 text-sm font-semibold mb-1">Paso 2</div>
                                <div class="font-bold">Wireframes</div>
                                <div class="text-sm text-gray-500">Día 2-3</div>
                            </div>
                            <div class="text-red-400 text-2xl">→</div>
                            <div class="bg-white border-2 border-red-300 p-4 rounded-xl shadow-md min-w-[180px]">
                                <div class="text-red-500 text-sm font-semibold mb-1">Paso 3</div>
                                <div class="font-bold">Diseño Visual</div>
                                <div class="text-sm text-gray-500">Día 4-5</div>
                            </div>
                            <div class="text-red-400 text-2xl">→</div>
                            <div class="bg-white border-2 border-red-300 p-4 rounded-xl shadow-md min-w-[180px]">
                                <div class="text-red-500 text-sm font-semibold mb-1">Paso 4</div>
                                <div class="font-bold">Desarrollo</div>
                                <div class="text-sm text-gray-500">Día 6-12</div>
                            </div>
                            <div class="text-red-400 text-2xl">→</div>
                            <div class="bg-white border-2 border-red-300 p-4 rounded-xl shadow-md min-w-[180px]">
                                <div class="text-red-500 text-sm font-semibold mb-1">Paso 5</div>
                                <div class="font-bold">Deploy</div>
                                <div class="text-sm text-gray-500">Día 18</div>
                            </div>
                            <div class="text-red-400 text-2xl">→</div>
                            <div class="bg-gradient-to-br from-amber-400 to-orange-500 text-white p-4 rounded-xl shadow-md min-w-[180px]">
                                <div class="text-amber-100 text-sm font-semibold mb-1">🚀</div>
                                <div class="font-bold">Lanzamiento</div>
                                <div class="text-sm text-amber-100">Día 20</div>
                            </div>
                        </div>
                    </div>

                    <!-- Detailed Dependencies -->
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                        <div class="bg-white rounded-xl shadow-md p-5">
                            <h4 class="font-bold text-gray-800 mb-4 flex items-center gap-2">
                                <span class="text-xl">📋</span> Tareas con Dependencias Fuertes
                            </h4>
                            <div class="space-y-4">
                                <div class="border-l-4 border-blue-500 pl-4 py-2">
                                    <div class="font-semibold">Diseño Visual</div>
                                    <div class="text-sm text-gray-500 mt-1">
                                        <span class="text-gray-400">Depende de:</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">Wireframes aprobados</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">Arquitectura definida</span>
                                    </div>
                                </div>
                                <div class="border-l-4 border-emerald-500 pl-4 py-2">
                                    <div class="font-semibold">Desarrollo Frontend</div>
                                    <div class="text-sm text-gray-500 mt-1">
                                        <span class="text-gray-400">Depende de:</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">Diseño visual aprobado</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">Contenidos v1</span>
                                    </div>
                                </div>
                                <div class="border-l-4 border-purple-500 pl-4 py-2">
                                    <div class="font-semibold">Animaciones</div>
                                    <div class="text-sm text-gray-500 mt-1">
                                        <span class="text-gray-400">Depende de:</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">Componentes HTML creados</span>
                                    </div>
                                </div>
                                <div class="border-l-4 border-amber-500 pl-4 py-2">
                                    <div class="font-semibold">Integraciones</div>
                                    <div class="text-sm text-gray-500 mt-1">
                                        <span class="text-gray-400">Depende de:</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">Formularios HTML listos</span>
                                    </div>
                                </div>
                                <div class="border-l-4 border-red-500 pl-4 py-2">
                                    <div class="font-semibold">Deploy a Producción</div>
                                    <div class="text-sm text-gray-500 mt-1">
                                        <span class="text-gray-400">Depende de:</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">QA completado</span>
                                        <span class="inline-block bg-gray-100 px-2 py-1 rounded text-xs ml-1">UAT aprobado</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="bg-white rounded-xl shadow-md p-5">
                            <h4 class="font-bold text-gray-800 mb-4 flex items-center gap-2">
                                <span class="text-xl">🔄</span> Tareas en Paralelo
                            </h4>
                            <div class="space-y-4">
                                <div class="bg-blue-50 rounded-lg p-4">
                                    <div class="font-semibold text-blue-800 mb-2">Semana 1: Diseño + Contenido</div>
                                    <ul class="text-sm text-blue-700 space-y-1">
                                        <li>• Diseñador: Wireframes → Diseño Visual</li>
                                        <li>• Copywriter: Research → Contenidos v1</li>
                                        <li class="font-medium mt-2">Ambos trabajan simultáneamente después del kickoff</li>
                                    </ul>
                                </div>
                                <div class="bg-emerald-50 rounded-lg p-4">
                                    <div class="font-semibold text-emerald-800 mb-2">Semana 2: Dev 1 + Dev 2</div>
                                    <ul class="text-sm text-emerald-700 space-y-1">
                                        <li>• Dev 1: Navbar + Hero + Footer + Testimonios + FAQ</li>
                                        <li>• Dev 2: Features + Pricing + Formulario + CTA</li>
                                        <li class="font-medium mt-2">División clara por secciones, mínimo bloqueo</li>
                                    </ul>
                                </div>
                                <div class="bg-purple-50 rounded-lg p-4">
                                    <div class="font-semibold text-purple-800 mb-2">Semana 3: Múltiples Flujos</div>
                                    <ul class="text-sm text-purple-700 space-y-1">
                                        <li>• Dev 1: Animaciones + Responsive</li>
                                        <li>• Dev 2: Integraciones + Analytics</li>
                                        <li>• Diseñador: Optimización imágenes</li>
                                        <li>• Copywriter: SEO + revisión contenidos</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Slack Channels -->
                    <div class="mt-8 bg-gray-800 rounded-xl p-5 text-white">
                        <h4 class="font-bold mb-4 flex items-center gap-2">
                            <span class="text-xl">💬</span> Canales de Comunicación Sugeridos
                        </h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div class="bg-gray-700 rounded-lg p-3">
                                <div class="font-medium">#lp-landing-inventario</div>
                                <div class="text-gray-400 text-sm">General del proyecto</div>
                            </div>
                            <div class="bg-gray-700 rounded-lg p-3">
                                <div class="font-medium">#lp-diseno-ux</div>
                                <div class="text-gray-400 text-sm">Diseñador + devs</div>
                            </div>
                            <div class="bg-gray-700 rounded-lg p-3">
                                <div class="font-medium">#lp-bugs</div>
                                <div class="text-gray-400 text-sm">Bug tracking QA</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Summary Tab -->
                <div id="content-summary" class="tab-content hidden">
                    <h3 class="text-lg font-bold text-gray-800 mb-4">📈 Resumen del Proyecto</h3>

                    <!-- Quick Stats -->
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
                        <div class="bg-gradient-to-br from-blue-500 to-blue-600 text-white p-5 rounded-xl">
                            <div class="text-3xl font-bold">20</div>
                            <div class="text-blue-100">Días hábiles</div>
                        </div>
                        <div class="bg-gradient-to-br from-emerald-500 to-teal-600 text-white p-5 rounded-xl">
                            <div class="text-3xl font-bold">4</div>
                            <div class="text-emerald-100">Semanas</div>
                        </div>
                        <div class="bg-gradient-to-br from-purple-500 to-pink-600 text-white p-5 rounded-xl">
                            <div class="text-3xl font-bold">22+</div>
                            <div class="text-purple-100">Tareas</div>
                        </div>
                        <div class="bg-gradient-to-br from-amber-500 to-orange-600 text-white p-5 rounded-xl">
                            <div class="text-3xl font-bold">4</div>
                            <div class="text-amber-100">Equipo</div>
                        </div>
                    </div>

                    <!-- Milestones -->
                    <div class="mb-8">
                        <h4 class="font-bold text-gray-800 mb-4">🎯 Hitos Principales</h4>
                        <div class="relative">
                            <div class="absolute left-4 top-0 bottom-0 w-0.5 bg-gray-200"></div>
                            <div class="space-y-6">
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold text-sm z-10">1</div>
                                    <div class="bg-white p-4 rounded-xl shadow-md border border-gray-100 flex-1">
                                        <div class="flex justify-between items-start">
                                            <div>
                                                <h5 class="font-bold text-gray-800">Diseño Aprobado</h5>
                                                <p class="text-gray-600 text-sm">Wireframes + diseño visual + contenidos v1</p>
                                            </div>
                                            <span class="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded-full">Fin Semana 1</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-8 h-8 bg-emerald-500 rounded-full flex items-center justify-center text-white font-bold text-sm z-10">2</div>
                                    <div class="bg-white p-4 rounded-xl shadow-md border border-gray-100 flex-1">
                                        <div class="flex justify-between items-start">
                                            <div>
                                                <h5 class="font-bold text-gray-800">Frontend Completo</h5>
                                                <p class="text-gray-600 text-sm">Todas las secciones implementadas, responsive básico</p>
                                            </div>
                                            <span class="bg-emerald-100 text-emerald-700 text-xs px-2 py-1 rounded-full">Fin Semana 2</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center text-white font-bold text-sm z-10">3</div>
                                    <div class="bg-white p-4 rounded-xl shadow-md border border-gray-100 flex-1">
                                        <div class="flex justify-between items-start">
                                            <div>
                                                <h5 class="font-bold text-gray-800">Staging Listo</h5>
                                                <p class="text-gray-600 text-sm">Integraciones, animaciones, analytics, performance optimizada</p>
                                            </div>
                                            <span class="bg-purple-100 text-purple-700 text-xs px-2 py-1 rounded-full">Fin Semana 3</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex items-start gap-4 relative">
                                    <div class="w-8 h-8 bg-amber-500 rounded-full flex items-center justify-center text-white font-bold text-sm z-10">4</div>
                                    <div class="bg-gradient-to-r from-amber-50 to-orange-50 p-4 rounded-xl shadow-md border-2 border-amber-300 flex-1">
                                        <div class="flex justify-between items-start">
                                            <div>
                                                <h5 class="font-bold text-amber-800">🚀 LANZAMIENTO</h5>
                                                <p class="text-amber-700 text-sm">Deploy producción, monitoreo, anuncios</p>
                                            </div>
                                            <span class="bg-amber-200 text-amber-800 text-xs px-2 py-1 rounded-full font-bold">Día 20</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Checklists -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white rounded-xl shadow-md p-5">
                            <h4 class="font-bold text-gray-800 mb-4">✅ Pre-Launch Checklist</h4>
                            <div class="space-y-3">
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">Todo el contenido revisado y aprobado</span>
                                </label>
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">Links probados (sin 404)</span>
                                </label>
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">Formularios funcionando y guardando leads</span>
                                </label>
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">Responsive en mobile/tablet/desktop</span>
                                </label>
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">Cross-browser probado</span>
                                </label>
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">Analytics tracking eventos</span>
                                </label>
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">Meta tags y Open Graph listos</span>
                                </label>
                                <label class="flex items-start gap-3 cursor-pointer">
                                    <input type="checkbox" class="mt-1 w-4 h-4 rounded text-indigo-600">
                                    <span class="text-sm text-gray-700">SSL y dominio configurados</span>
                                </label>
                            </div>
                        </div>

                        <div class="bg-white rounded-xl shadow-md p-5">
                            <h4 class="font-bold text-gray-800 mb-4">⚠️ Riesgos y Mitigaciones</h4>
                            <div class="space-y-4">
                                <div class="border border-red-200 rounded-lg p-3 bg-red-50">
                                    <div class="font-medium text-red-800 text-sm mb-1">🔴 Riesgo Alto: Aprobaciones demoradas</div>
                                    <p class="text-red-700 text-xs"><strong>Mitigación:</strong> Definir plazos máximos de 24h para aprobaciones. Tener una persona designada para decidir.</p>
                                </div>
                                <div class="border border-amber-200 rounded-lg p-3 bg-amber-50">
                                    <div class="font-medium text-amber-800 text-sm mb-1">🟡 Riesgo Medio: Bugs inesperados en QA</div>
                                    <p class="text-amber-700 text-xs"><strong>Mitigación:</strong> Reservar día 17 completo para bug fixes. Tener buffer de 1 día antes de deploy.</p>
                                </div>
                                <div class="border border-amber-200 rounded-lg p-3 bg-amber-50">
                                    <div class="font-medium text-amber-800 text-sm mb-1">🟡 Riesgo Medio: Integraciones con problemas</div>
                                    <p class="text-amber-700 text-xs"><strong>Mitigación:</strong> Probar integraciones temprano (día 11). Tener alternativas simples (formulario con mailto de respaldo).</p>
                                </div>
                                <div class="border border-blue-200 rounded-lg p-3 bg-blue-50">
                                    <div class="font-medium text-blue-800 text-sm mb-1">🔵 Riesgo Bajo: Performance baja</div>
                                    <p class="text-blue-700 text-xs"><strong>Mitigación:</strong> Optimizar imágenes desde semana 1. Usar lazy loading. CDN para producción.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Meeting Rhythm -->
                    <div class="mt-8 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-xl p-6 text-white">
                        <h4 class="font-bold text-lg mb-4">📅 Ritmo de Reuniones</h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
                                <div class="font-medium mb-1">🔄 Daily Standup</div>
                                <div class="text-indigo-200 text-sm">15 min todos los días</div>
                                <div class="text-indigo-300 text-xs mt-2">¿Qué hiciste? ¿Qué bloqueos? ¿Qué harás?</div>
                            </div>
                            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
                                <div class="font-medium mb-1">👁️ Weekly Demo</div>
                                <div class="text-indigo-200 text-sm">Viernes al final del día</div>
                                <div class="text-indigo-300 text-xs mt-2">Demo de progreso, feedback de stakeholders</div>
                            </div>
                            <div class="bg-white/10 rounded-lg p-4 backdrop-blur">
                                <div class="font-medium mb-1">🚀 Launch Prep</div>
                                <div class="text-indigo-200 text-sm">Semana 4: 2 reuniones</div>
                                <div class="text-indigo-300 text-xs mt-2">Checklist pre-launch, plan post-launch</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <footer class="text-center text-gray-500 text-sm py-4">
            <p>📋 Plan de Proyecto para Landing Page SaaS de Gestión de Inventario</p>
            <p class="mt-1">Timeline: 4 semanas | Equipo: 4 personas</p>
        </footer>
    </div>

    <script>
        // Tab switching
        function showTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(el => {
                el.classList.add('hidden');
            });
            
            document.querySelectorAll('.tab-btn').forEach(el => {
                el.classList.remove('text-indigo-600', 'border-b-2', 'border-indigo-600', 'bg-indigo-50');
                el.classList.add('text-gray-500');
            });
            
            document.getElementById('content-' + tabName).classList.remove('hidden');
            
            const activeTab = document.getElementById('tab-' + tabName);
            activeTab.classList.add('text-indigo-600', 'border-b-2', 'border-indigo-600', 'bg-indigo-50');
            activeTab.classList.remove('text-gray-500');
        }

        // Phase toggle
        function togglePhase(phaseId) {
            const content = document.getElementById(phaseId);
            const icon = document.getElementById('icon-' + phaseId);
            
            if (content.classList.contains('hidden')) {
                content.classList.remove('hidden');
                icon.classList.add('rotate-180');
            } else {
                content.classList.add('hidden');
                icon.classList.remove('rotate-180');
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            showTab('phases');
        });
    </script>
</body>
</html>
```

This project plan is a comprehensive, single-page application that covers all aspects of the landing page development for the inventory management SaaS. Here's what's included:

## Key Features:

1. **Project Overview**: Header with project details and team members
2. **Interactive Tabs**:
   - **Phases & Tasks**: Detailed breakdown of work into 4 weekly phases with tasks, dependencies, and responsible team members
   - **Timeline Visual**: Gantt chart showing task schedules and workload distribution
   - **Dependencies**: Critical path analysis and parallel task planning
   - **Summary**: Milestones, checklists, risk mitigation, and meeting rhythms

3. **Phase Breakdown**:
   - **Semana 1 (Planning & Design)**: Kickoff, research, wireframes, content strategy, visual design
   - **Semana 2 (Frontend Development)**: Setup, component implementation, responsive design
   - **Semana 3 (Integrations & Animations)**: Forms, analytics, animations, performance optimization, SEO
   - **Semana 4 (Testing, Deploy & Launch)**: QA, bug fixes, UAT, production deploy, launch preparations

4. **Team & Responsibilities**:
   - 🎨 Designer: UI/UX, wireframes, visual design, images
   - 💻 Dev 1: Frontend development, responsive design, animations
   - ⚙️ Dev 2: Integraciones, deploy, analytics, performance
   - ✍️ Copywriter: Content, SEO, messaging

5. **Visual Elements**:
   - Color-coded phases for clarity
   - Gantt chart with timeline
   - Workload distribution charts
   - Critical path analysis
   - Checklists and risk assessments
   - Responsive design for all screen sizes

This plan is designed to be realistic, with clear dependencies, parallel tasking, and buffer time for testing and iterations. The 4-week timeline is aggressive but achievable given the team size and scope.