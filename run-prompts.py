#!/usr/bin/env python3
"""Run test prompts against a voice sample using Gemini 3.1 Flash Lite.

Reads from test-prompts/prompt-index.json and updates run_status, input, and output fields.
Only runs prompts that have a .txt file in test-prompts/.
Skips prompts already marked run_status=complete unless --force is passed.
"""

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()

AUDIO_FILE = Path("2026-03-26/26_03_2026_16_08.flac")
PROMPTS_DIR = Path("test-prompts")
OUTPUT_DIR = Path("outputs")
INDEX_PATH = PROMPTS_DIR / "prompt-index.json"


def main():
    parser = argparse.ArgumentParser(description="Run audio understanding test prompts")
    parser.add_argument("--force", action="store_true", help="Re-run prompts even if already complete")
    parser.add_argument("--only", nargs="*", help="Only run these prompt names")
    parser.add_argument("--author", help="Only run prompts by this author")
    parser.add_argument("--category", help="Only run prompts in this category")
    parser.add_argument("--dry-run", action="store_true", help="Show what would run without running")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "your-api-key-here":
        print("Set GEMINI_API_KEY in .env first")
        sys.exit(1)

    with open(INDEX_PATH) as f:
        data = json.load(f)

    prompts = data["prompts"]

    # Determine which prompts to run
    to_run = []
    for p in prompts:
        name = p["name"]
        prompt_file = PROMPTS_DIR / f"{name}.txt"

        if args.only and name not in args.only:
            continue
        if args.author and args.author.lower() not in p["author"].lower():
            continue
        if args.category and args.category.lower() not in p["category"].lower():
            continue
        if not prompt_file.exists():
            continue
        if p.get("run_status") == "complete" and not args.force:
            continue

        to_run.append((p, prompt_file))

    if not to_run:
        print("Nothing to run. All matching prompts with .txt files are already complete.")
        print("Use --force to re-run, or create .txt files for suggested prompts.")
        sys.exit(0)

    print(f"Will run {len(to_run)} prompt(s)")
    if args.dry_run:
        for p, pf in to_run:
            print(f"  [{p['id']:3d}] {p['name']} ({p['category']})")
        sys.exit(0)

    client = genai.Client(api_key=api_key)

    print(f"Uploading {AUDIO_FILE}...")
    uploaded = client.files.upload(file=str(AUDIO_FILE))
    print(f"Uploaded: {uploaded.name}")

    OUTPUT_DIR.mkdir(exist_ok=True)

    for p, prompt_file in to_run:
        name = p["name"]
        prompt_text = prompt_file.read_text().strip()
        out_file = OUTPUT_DIR / f"{name}.md"

        print(f"Running: {name}...")
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite-preview",
                contents=[prompt_text, uploaded],
            )
            out_file.write_text(f"# {name.replace('-', ' ').title()}\n\n{response.text}\n")
            print(f"  -> {out_file}")

            p["run_status"] = "complete"
            p["input"] = str(prompt_file)
            p["output"] = str(out_file)
            p["status"] = "implemented"
        except Exception as e:
            print(f"  FAILED: {e}")
            p["run_status"] = "failed"

    # Write updated JSON
    with open(INDEX_PATH, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")

    complete = sum(1 for p in prompts if p.get("run_status") == "complete")
    print(f"\nDone! {complete}/{len(prompts)} prompts complete. Index updated.")


if __name__ == "__main__":
    main()
