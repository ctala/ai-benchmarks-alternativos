"""
Tests de Text-to-Speech con MiniMax Speech-02.
Genera audio para contenido de ecosistemastartup.com y cursos.

Correr con: python benchmarks/tests/tts_generation.py
"""

TTS_TESTS = [
    {
        "name": "intro_newsletter",
        "description": "Intro de newsletter en espanol",
        "text": "Bienvenidos al newsletter semanal de Ecosistema Startup. Esta semana traemos las noticias mas importantes del mundo emprendedor y tecnologico en Latinoamerica. Vamos con los highlights.",
        "voice_id": "English_Graceful_Lady",
        "language": "es",
    },
    {
        "name": "resumen_articulo",
        "description": "Resumen de articulo para audio blog",
        "text": "DeepSeek acaba de lanzar la version 4 de su modelo de inteligencia artificial. Lo interesante es que es completamente open source bajo licencia MIT, lo que significa que cualquier startup puede descargarlo y correrlo en sus propios servidores sin pagar un centavo. Esto es un cambio de juego para los emprendedores en Latinoamerica que buscan reducir costos.",
        "voice_id": "English_Persuasive_Man",
        "language": "es",
    },
    {
        "name": "intro_curso",
        "description": "Introduccion de modulo de curso",
        "text": "Hola, bienvenido al modulo 3 de nuestro curso de IA practica para emprendedores. Hoy vamos a aprender como automatizar tareas repetitivas usando herramientas como N8N y agentes de inteligencia artificial. Al final de este modulo vas a poder crear tu primer flujo de automatizacion.",
        "voice_id": "English_Persuasive_Man",
        "language": "es",
    },
    {
        "name": "podcast_snippet_en",
        "description": "Snippet para podcast en ingles",
        "text": "The open source AI revolution is here, and Latin American startups are uniquely positioned to benefit. With models like DeepSeek V4, Qwen 3.6, and Gemma 4 now available for free, the barrier to entry for AI-powered products has never been lower.",
        "voice_id": "English_Insightful_Speaker",
        "language": "en",
    },
]


def run_tts_tests():
    """Genera audio usando la API de MiniMax TTS."""
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

    results_dir = Path("benchmarks/results/audio")
    results_dir.mkdir(parents=True, exist_ok=True)

    results = []

    for test in TTS_TESTS:
        print(f"\nGenerando TTS: {test['name']}...", end=" ", flush=True)
        start = time.time()

        try:
            response = httpx.post(
                "https://api.minimax.io/v1/t2a_v2",
                headers={
                    "Authorization": f"Bearer {MINIMAX_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "speech-02-turbo",
                    "text": test["text"],
                    "voice_setting": {
                        "voice_id": test["voice_id"],
                        "speed": 1.0,
                        "vol": 1.0,
                        "pitch": 0,
                    },
                    "audio_setting": {
                        "sample_rate": 32000,
                        "bitrate": 128000,
                        "format": "mp3",
                    },
                },
                timeout=60,
            )
            elapsed = time.time() - start

            if response.status_code == 200:
                data = response.json()

                # Extraer audio
                audio_data = None
                if "data" in data and "audio" in data["data"]:
                    audio_data = data["data"]["audio"]
                elif "audio" in data:
                    audio_data = data["audio"]

                if audio_data:
                    # Guardar audio
                    import base64
                    audio_bytes = base64.b64decode(audio_data)
                    audio_file = results_dir / f"{test['name']}.mp3"
                    with open(audio_file, "wb") as f:
                        f.write(audio_bytes)
                    print(f"OK ({elapsed:.1f}s, {len(audio_bytes)//1024}KB)")
                    print(f"  Guardado: {audio_file}")
                    results.append({
                        "name": test["name"],
                        "success": True,
                        "time": round(elapsed, 1),
                        "file": str(audio_file),
                        "size_kb": len(audio_bytes) // 1024,
                    })
                else:
                    # Quizas la respuesta tiene URL en vez de base64
                    print(f"OK ({elapsed:.1f}s) - formato respuesta diferente")
                    print(f"  Keys: {list(data.keys())}")
                    results.append({
                        "name": test["name"],
                        "success": True,
                        "time": round(elapsed, 1),
                        "response_keys": list(data.keys()),
                        "raw": json.dumps(data)[:300],
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
    results_file = results_dir / "tts_results.json"
    with open(results_file, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 60}")
    ok = sum(1 for r in results if r["success"])
    print(f"TTS Completado: {ok}/{len(results)} exitosos")
    print(f"Resultados: {results_file}")
    print(f"Audio: {results_dir}/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    run_tts_tests()
