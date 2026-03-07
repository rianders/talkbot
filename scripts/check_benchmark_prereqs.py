#!/usr/bin/env python3
"""Preflight checks for benchmark readiness (no benchmark execution)."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def _placeholder_key(value: str) -> bool:
    v = (value or "").strip()
    if not v:
        return True
    lowered = v.lower()
    return ("your_" in lowered) or ("placeholder" in lowered) or ("changeme" in lowered)


def _check_uv_cache() -> list[str]:
    issues: list[str] = []
    uv_cache_dir = os.getenv("UV_CACHE_DIR", "").strip()
    if not uv_cache_dir:
        issues.append("UV_CACHE_DIR is not set (recommend: UV_CACHE_DIR=.uv-cache)")
        return issues
    cache_path = Path(uv_cache_dir)
    if not cache_path.exists():
        issues.append(f"UV_CACHE_DIR points to missing directory: {cache_path}")
    return issues


def _check_openrouter_key(matrix_data: dict) -> list[str]:
    issues: list[str] = []
    uses_openrouter = any(
        (p.get("provider") == "openrouter") for p in matrix_data.get("profiles", [])
    )
    if uses_openrouter:
        key = os.getenv("OPENROUTER_API_KEY", "")
        if _placeholder_key(key):
            issues.append(
                "OPENROUTER_API_KEY missing/placeholder while matrix contains openrouter profiles"
            )
    return issues


def _check_matrix_local_models(matrix_data: dict, repo_root: Path) -> list[str]:
    issues: list[str] = []
    seen: set[str] = set()
    for profile in matrix_data.get("profiles", []):
        if profile.get("provider") != "local":
            continue
        model_path = (profile.get("local_model_path") or "").strip()
        if not model_path or model_path in seen:
            continue
        seen.add(model_path)
        full = repo_root / model_path
        if not full.exists():
            issues.append(f"Missing local model file required by matrix: {model_path}")
    return issues


def _check_voice_manifests(manifests: list[Path], repo_root: Path) -> list[str]:
    issues: list[str] = []
    total = 0
    missing = 0
    for manifest in manifests:
        if not manifest.exists():
            issues.append(f"Missing manifest: {manifest}")
            continue
        payload = json.loads(manifest.read_text(encoding="utf-8"))
        entries = payload.get("entries", []) if isinstance(payload, dict) else payload
        if not isinstance(entries, list):
            issues.append(f"Unexpected manifest format: {manifest}")
            continue
        for entry in entries:
            audio_path = entry.get("audio_path", "")
            if not audio_path:
                continue
            total += 1
            if not (repo_root / audio_path).exists():
                missing += 1
    if total == 0:
        issues.append("No audio entries found in manifests")
    elif missing > 0:
        issues.append(f"Voice dataset incomplete: missing {missing}/{total} referenced audio files")
    return issues


def _check_kittentts_ready() -> list[str]:
    issues: list[str] = []
    try:
        from talkbot.tts import TTSManager

        tts = TTSManager(backend="kittentts")
        if not tts.available_voices:
            issues.append("kittentts initialized but returned zero voices")
    except Exception as exc:  # pragma: no cover - environment dependent
        issues.append(f"kittentts not ready: {exc}")
    return issues


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--matrix",
        default="benchmarks/model_matrix.next_run.json",
        help="Benchmark matrix to validate (default: benchmarks/model_matrix.next_run.json)",
    )
    parser.add_argument(
        "--manifest",
        action="append",
        default=[],
        help="Voice dataset manifest path (repeatable). Defaults to manifest.json + pipeline_manifest.json",
    )
    parser.add_argument(
        "--check-kittentts",
        action="store_true",
        help="Attempt to initialize kittentts and list voices",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    repo_root = Path(__file__).resolve().parent.parent
    os.chdir(repo_root)

    matrix_path = Path(args.matrix)
    if not matrix_path.exists():
        print(f"[FAIL] Matrix not found: {matrix_path}")
        return 2

    matrix_data = json.loads(matrix_path.read_text(encoding="utf-8"))
    manifests = (
        [Path(p) for p in args.manifest]
        if args.manifest
        else [
            Path("benchmarks/voice_dataset/manifest.json"),
            Path("benchmarks/voice_dataset/pipeline_manifest.json"),
        ]
    )

    failures: list[str] = []
    failures.extend(_check_uv_cache())
    failures.extend(_check_openrouter_key(matrix_data))
    failures.extend(_check_matrix_local_models(matrix_data, repo_root))
    failures.extend(_check_voice_manifests(manifests, repo_root))
    if args.check_kittentts:
        failures.extend(_check_kittentts_ready())

    if failures:
        print("Benchmark preflight: FAIL")
        for issue in failures:
            print(f"- {issue}")
        print("\nSuggested next steps:")
        print("- export UV_CACHE_DIR=.uv-cache")
        print("- Populate OPENROUTER_API_KEY in .env (if using openrouter profiles)")
        print("- Download required local GGUF files listed above")
        print("- Restore or regenerate benchmarks/voice_dataset/raw audio files")
        print("- Run with --check-kittentts once network/cache is ready")
        return 1

    print("Benchmark preflight: PASS")
    print("- Required env and files look ready for benchmark execution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
