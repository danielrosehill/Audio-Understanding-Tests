---
description: Add a new audio understanding test prompt, run it against the model, and save the output
---

The user is providing a new test prompt for the audio understanding experiment. Follow these steps exactly:

## Step 1: Parse the prompt

Extract from the user's input (`$ARGUMENTS`):
- The **prompt text** (the actual question/instruction to send to the model)
- Infer a short **kebab-case name** for it
- Infer the best **category** from existing categories in `test-prompts/prompt-index.json`
- The **author** is "Daniel Rosehill" unless stated otherwise

## Step 2: Add to the index

1. Read `test-prompts/prompt-index.json`
2. Determine the next available `id` (max existing id + 1)
3. Add a new entry:
   ```json
   {
     "id": <next_id>,
     "name": "<kebab-case-name>",
     "category": "<category>",
     "description": "<the prompt text>",
     "author": "Daniel Rosehill",
     "status": "implemented",
     "run_status": "pending",
     "input": "test-prompts/<kebab-case-name>.txt",
     "output": "outputs/<kebab-case-name>.md"
   }
   ```
4. Write the updated JSON back
5. Write the prompt text to `test-prompts/<kebab-case-name>.txt`

## Step 3: Run against the model

Launch a background subagent to run the prompt against the audio sample. The subagent should:

1. Run: `python3 run-prompts.py --only <kebab-case-name>`
2. If that fails (e.g. missing deps), fall back to running the Gemini API directly via the script
3. Wait for completion

## Step 4: Report results

Once the subagent completes:
1. Read the output file at `outputs/<kebab-case-name>.md`
2. Show the user a brief summary: prompt name, category, and a preview of the model's response
3. Confirm the JSON index has been updated with `run_status: "complete"`

User's prompt specification:
$ARGUMENTS
