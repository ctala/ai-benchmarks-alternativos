#!/bin/bash
# Pasos finales tras completar mediciones de Claude 5.5

set -e  # Exit on error

cd /workspace

echo "========================================="
echo "PASOS FINALES - v4.16.0"
echo "========================================="
echo ""

# Verificar presupuesto final
echo "1. Verificando gasto final..."
python3 benchmarks/check_presupuesto.py
echo ""

# Regenerar artefactos
echo "2. Regenerando artefactos..."
python3 benchmarks/regenerate_all.py --skip-og-image 2>&1 | tail -20
echo "   ✓ Artefactos regenerados"
echo ""

# Correr QA
echo "3. Corriendo QA..."
python3 benchmarks/qa.py 2>&1 | tail -30
echo ""

echo "========================================="
echo "LISTO PARA COMMITS FINALES"
echo "========================================="
