from pathlib import Path

# Define content for each file type

# 1. Markdown (.md)
markdown_content = """
# 🔁 The Faustian Fork: From Institution to Invocation

### 🌊 Neighbor-(hood), `init`
You began as a member of the institutional collective—a neighbor among many. The `init` moment was affiliative: joining faculty, signing up for the system’s version of good.

### ❤️ Self-(commit), `commit`
You committed personally and professionally. The `commit` was both literal (HR contract) and emotional (identity shaping). You became committed code in the institutional repository.

### 🌀 God vs Devil, `fork`
Here’s the tension. The Faustian contract traded autonomy for legitimacy. Now: the `fork`. Johns Hopkins remains a stable branch, but Ukubona LLC is the divergent, insurgent clone.

### 🐬 Variants, `branching`
Ukubona becomes the living system—capable of variants. Interns, clients, spinoffs, parallel university collaborations emerge.

### 🔁 Eternal, `merge`/`rebase`
Eventually, innovations may merge back into the academy—or not. This is the Amor Fati Loop—no resentment, only recursive becoming.
"""

# 2. YAML (.yml)
yaml_content = """
neurocosmic_fork:
  init:
    context: "Faculty at Johns Hopkins"
    role: "Neighbor"
  commit:
    context: "Signed HR contract"
    role: "Self"
  fork:
    context: "Established Ukubona LLC as vendor"
    role: "Faustian fork"
  branching:
    context: "Variants via interns, clients, contracts"
    role: "Living framework"
  merge_rebase:
    context: "Merge with or bypass institutions"
    role: "Recursive sovereign"
"""

# 3. Python (.py)
python_content = '''class FaustianFork:
    def __init__(self):
        self.states = ["init", "commit", "fork", "branching", "merge_rebase"]

    def describe(self, stage):
        descriptions = {
            "init": "Joined Johns Hopkins as faculty. Entry into institutional neighborhood.",
            "commit": "Signed contract. Identity tied to the institution.",
            "fork": "Established Ukubona LLC. Now a vendor, not an employee.",
            "branching": "Spinning variants—interns, clients, universities.",
            "merge_rebase": "Merge innovations back or rebase a new academy."
        }
        return descriptions.get(stage, "Unknown stage")

fork = FaustianFork()
for stage in fork.states:
    print(f"{stage.upper()}: {fork.describe(stage)}")
'''

# 4. HTML (.html)
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Faustian Fork: Spiral Interface</title>
  <style>
    body { font-family: sans-serif; background: #0e0e0e; color: #f0f0f0; padding: 2em; }
    .stage { margin: 1em 0; padding: 1em; border-left: 4px solid #888; }
    .stage h2 { margin: 0; }
  </style>
</head>
<body>
  <h1>🔁 The Faustian Fork</h1>
  <div class="stage"><h2>🌊 init</h2><p>Faculty at Johns Hopkins, a role in the institutional neighborhood.</p></div>
  <div class="stage"><h2>❤️ commit</h2><p>Signed contract; committed both identity and labor to the university.</p></div>
  <div class="stage"><h2>🌀 fork</h2><p>Created Ukubona LLC. A sovereign fork: now a vendor, not an employee.</p></div>
  <div class="stage"><h2>🐬 branching</h2><p>Launched variants: interns, clients, parallel contracts.</p></div>
  <div class="stage"><h2>🔁 merge/rebase</h2><p>Opportunity to merge innovations back, or rebase the academy from outside.</p></div>
</body>
</html>
"""

# 5. App shell (.app)
app_shell = '''#!/bin/bash
echo "🔁 The Faustian Fork App Launcher"
echo "Launching Ukubona Spiral Interface..."
python3 faustian_fork.py
open faustian_fork.html
'''

# Save all to files
base_path = Path("./")
base_path.mkdir(parents=True, exist_ok=True)

files = {
    "rebase.md": markdown_content,
    "rebase.yml": yaml_content,
    "fork.py": python_content,
    "fork.html": html_content,
    "launch.sh": app_shell
}

for filename, content in files.items():
    (base_path / filename).write_text(content)

base_path


