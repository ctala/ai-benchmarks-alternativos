"""
Tests de generacion de imagenes con MiniMax Image-01.
Enfocado en feature images para WordPress optimizadas para Google Discover y SEO.

Estos tests NO usan el runner normal - tienen su propio script.
Correr con: python benchmarks/tests/image_generation.py
"""

# Prompts para feature images de WordPress
IMAGE_PROMPTS = [
    {
        "name": "blog_startup_hero",
        "description": "Feature image para articulo sobre startups y IA",
        "prompt": "Professional tech blog hero image: A diverse group of young Latin American entrepreneurs collaborating around a holographic AI interface in a modern coworking space. Warm lighting, vibrant colors, clean composition. 16:9 aspect ratio, high resolution, editorial style photography. No text overlays.",
        "use_case": "ecosistemastartup.com blog post",
        "seo_notes": "Imagen llamativa para Google Discover, sin texto para que el titulo del post sea legible",
    },
    {
        "name": "ai_tools_comparison",
        "description": "Feature image para comparativa de herramientas IA",
        "prompt": "Clean modern infographic-style illustration showing multiple AI robot assistants of different colors and sizes standing on podiums, numbered 1-2-3. Minimalist flat design, tech blue and white color palette, professional look. 16:9 aspect ratio, suitable for blog featured image.",
        "use_case": "Articulo comparativo de modelos IA",
        "seo_notes": "Visualmente comunica 'comparacion' y 'ranking' sin texto",
    },
    {
        "name": "workshop_emprendimiento",
        "description": "Feature image para workshop de emprendimiento",
        "prompt": "Dynamic photo of a hands-on workshop session: people actively working on laptops with colorful sticky notes on a glass wall, energetic atmosphere, natural light from large windows. Latin American setting, professional but creative environment. 16:9 aspect ratio, editorial style.",
        "use_case": "Promocion de workshop en redes sociales y blog",
        "seo_notes": "Transmite energia y accion, ideal para engagement en redes",
    },
    {
        "name": "curso_online_emprendedores",
        "description": "Feature image para curso online",
        "prompt": "Modern e-learning concept illustration: A glowing laptop screen showing a graduation cap icon, surrounded by floating icons of charts, lightbulbs, rockets, and gears. Gradient purple-to-blue background. Clean, professional, aspirational. 16:9 aspect ratio.",
        "use_case": "Landing page de curso para emprendedores",
        "seo_notes": "Comunica educacion + emprendimiento + tecnologia",
    },
    {
        "name": "newsletter_tech",
        "description": "Feature image para newsletter semanal",
        "prompt": "Stylized digital newspaper front page floating in a futuristic void with holographic tech news headlines and glowing data streams. Cool blue and cyan tones, high-tech aesthetic. Clean composition, no readable text. 16:9 aspect ratio.",
        "use_case": "Header de newsletter semanal",
        "seo_notes": "Reutilizable, transmite noticias + tecnologia",
    },
]


def run_image_tests():
    """Genera imagenes usando la API de MiniMax."""
    import json
    import os
    import sys
    import time
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).parent.parent.parent))

    try:
        from benchmarks.config import MINIMAX_API_KEY
    except ImportError:
        print("ERROR: Configura MINIMAX_API_KEY en benchmarks/config.py")
        return

    if not MINIMAX_API_KEY:
        print("ERROR: MINIMAX_API_KEY esta vacio")
        return

    import httpx

    results_dir = Path("benchmarks/results/images")
    results_dir.mkdir(parents=True, exist_ok=True)

    results = []

    for test in IMAGE_PROMPTS:
        print(f"\nGenerando: {test['name']}...", end=" ", flush=True)
        start = time.time()

        try:
            response = httpx.post(
                "https://api.minimax.io/v1/image_generation",
                headers={
                    "Authorization": f"Bearer {MINIMAX_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "image-01",
                    "prompt": test["prompt"],
                    "aspect_ratio": "16:9",
                    "response_format": "url",
                    "n": 1,
                },
                timeout=120,
            )
            elapsed = time.time() - start

            if response.status_code == 200:
                data = response.json()
                image_url = None
                if "data" in data and "image_urls" in data["data"]:
                    image_url = data["data"]["image_urls"][0]
                elif "data" in data and isinstance(data["data"], list):
                    image_url = data["data"][0].get("url", "")

                print(f"OK ({elapsed:.1f}s)")
                if image_url:
                    print(f"  URL: {image_url[:100]}...")

                results.append({
                    "name": test["name"],
                    "success": True,
                    "time": round(elapsed, 1),
                    "url": image_url,
                    "prompt": test["prompt"][:100],
                    "use_case": test["use_case"],
                })
            else:
                print(f"ERROR {response.status_code} ({elapsed:.1f}s)")
                print(f"  {response.text[:200]}")
                results.append({
                    "name": test["name"],
                    "success": False,
                    "time": round(elapsed, 1),
                    "error": response.text[:200],
                })

        except Exception as e:
            elapsed = time.time() - start
            print(f"ERROR ({elapsed:.1f}s): {str(e)[:100]}")
            results.append({
                "name": test["name"],
                "success": False,
                "time": round(elapsed, 1),
                "error": str(e)[:200],
            })

    # Guardar resultados
    results_file = results_dir / "image_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 60}")
    print(f"Resultados guardados en {results_file}")
    ok = sum(1 for r in results if r["success"])
    print(f"Exitosos: {ok}/{len(results)}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    run_image_tests()
