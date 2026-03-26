---
description: Sync experiment data to Hugging Face dataset repo and push
---

Sync the audio understanding test data from this repo to the Hugging Face dataset at `/home/daniel/repos/hugging-face/datasets/public/Audio-Understanding-Test-Set`, structured as a proper HF dataset, then push.

## Step 1: Read current state

1. Read `test-prompts/prompt-index.json` to get all prompts and their statuses
2. Read `experiment.json` for metadata
3. Check what already exists in the HF dataset repo

## Step 2: Structure as a Hugging Face dataset

Create/update the following structure in `/home/daniel/repos/hugging-face/datasets/public/Audio-Understanding-Test-Set/`:

```
Audio-Understanding-Test-Set/
├── README.md                    # HF dataset card (YAML frontmatter + description)
├── metadata.json                # experiment metadata
├── data/
│   ├── prompts.jsonl            # one JSON object per prompt (id, name, category, description, author, status)
│   ├── results.jsonl            # one JSON object per completed run (id, name, prompt, model, output_text)
│   └── audio/                   # audio samples (copy FLAC files)
│       ├── full-sample.flac     # symlink or copy of the main recording
│       └── short-sample.flac    # symlink or copy of the short sample
```

### README.md (Dataset Card)

Use standard HF dataset card format with YAML frontmatter:
```yaml
---
license: mit
task_categories:
  - audio-classification
  - automatic-speech-recognition
language:
  - en
tags:
  - audio-understanding
  - voice-analysis
  - multimodal
  - evaluation
  - gemini
size_categories:
  - n<1K
---
```

Then a description section explaining the dataset, its purpose, the prompt categories, and how to use it.

### prompts.jsonl

One line per prompt from `prompt-index.json`. Each line is a JSON object with fields: `id`, `name`, `category`, `description`, `author`, `status`.

### results.jsonl

One line per completed prompt (where `run_status == "complete"`). Each line is a JSON object with:
- `id`, `name`, `category`, `prompt` (the description text)
- `model`: "gemini-3.1-flash-lite-preview"
- `output`: the full text content of the output .md file (read from `outputs/<name>.md`, strip the H1 header line)

### Audio files

Copy the FLAC files from `2026-03-26/` into `data/audio/`. Use git LFS for the audio files (configure `.gitattributes`).

## Step 3: Git add, commit, and push

```bash
cd /home/daniel/repos/hugging-face/datasets/public/Audio-Understanding-Test-Set
git add -A
git commit -m "Sync audio understanding test data (<N> prompts, <M> results)"
git push
```

Report the total prompts synced and results included when done.
