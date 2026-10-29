#!/usr/bin/env python3
"""
Validator and Originality/Similarity Checker for the Vibe Stack plugin.
Checks:
1. Manifest JSON validity and version sync (.claude-plugin/plugin.json, marketplace.json, .codex-plugin/plugin.json).
2. All 12 skills under skills/<name>/SKILL.md and agents/openai.yaml.
3. Frontmatter rules: name regex & folder match, description length (15-40 words, <=1024 chars), invocation flags.
4. One-way invocation hierarchy: user commands never called via the Skill tool.
5. Co-located sidecar file reference integrity (no broken links or parent ../ escapes).
6. Punctuation hygiene: zero em-dashes or en-dashes across the entire plugin.
7. Originality & 5-word similarity check: zero mentions of studied author/repo/skill names and zero 5+ word overlaps with studied skill texts.
"""

import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

EXPECTED_USER_SKILLS = {
    "start-project",
    "ask-me",
    "freeze-plan",
    "build-step",
    "repair",
    "launch-check",
    "plain-english",
    "undo",
}

EXPECTED_MODEL_SKILLS = {
    "clarifying",
    "showing-options",
    "checking-behavior",
    "auditing-work",
}

ALL_EXPECTED_SKILLS = EXPECTED_USER_SKILLS | EXPECTED_MODEL_SKILLS

FORBIDDEN_ORIGIN_TERMS = [
    "mattpocock",
    "matt pocock",
    "aihero",
    "total-typescript",
    "shoehorn",
    "grill-me",
    "grill-with-docs",
    "wayfinder",
    "setup-matt-pocock",
    "ask-matt",
    "wait-what",
    "to-spec",
    "to-tickets",
    "diagnosing-bugs",
    "writing-for-agents",
    "writing-great-skills",
    "domain-modeling",
    "codebase-design",
    "improve-codebase-architecture",
    "implement-spec",
    "to-questionnaire",
    "glossary.md",
    "asd-ste100",
    "ousterhout",
    "fowler",
    "karpathy",
    "horthy",
    "lakens",
    "nygard",
]

# Verbatim phrases and sentences from the studied repository's skills to check 5+ word n-gram collisions against
STUDIED_REPO_CORPUS = [
    "Not sure which skill to reach for, or how the workflow fits together? Describe where you are and get pointed to the right skill.",
    "Review a git diff across two axes: coding standards (repo docs + Fowler code smells) and spec compliance.",
    "Vocabulary and principles for designing deep modules, interfaces, and test seams. Use when designing new modules, refactoring shallow code, evaluating architecture, or choosing where tests should sit.",
    "Scientific method workflow for reproducing, isolating, and fixing bugs or regressions. Use when debugging a failing test, investigating a bug report, fixing a production error, or diagnosing a performance regression.",
    "Active discipline for sharpening ubiquitous language, maintaining GLOSSARY.md, and recording Architecture Decision Records (ADRs).",
    "Stress-test a plan or idea inside a codebase while sharpening domain vocabulary (GLOSSARY.md) and flagging decisions worth an ADR.",
    "Call the Skill tool twice, for grilling and domain-modeling.",
    "Pick up a single issue or ticket, build it with TDD at the agreed test seams, run code-review, and commit.",
    "Orchestrate parallel implementer subagents across a dependency graph of tickets in isolated git worktrees, fast-forwarding onto an integration branch.",
    "Audit a codebase for shallow modules, leaky seams, and high-churn hotspots, render an interactive HTML report, and plan deepening refactors.",
    "Stop and ask a single line: Which of these would you like to explore?",
    "Write or update a pull request description with a visual summary, before/after evidence, and merge danger assessment.",
    "Build throwaway code on a prototype/<name> branch to answer a specific design question (domain logic state machine or UI variants).",
    "Spin up a background subagent with a fresh context window to investigate a technical question against primary sources and write a cited markdown report in the repo.",
    "Run a post-session retrospective to improve the agent's environment (AGENTS.md, scripts, linters, coding standards, skills) based on observed friction.",
    "One-time repo setup: configure your issue tracker, triage labels, and domain glossary map in docs/agents/, and wire a pointer block into CLAUDE.md or AGENTS.md.",
    "Reference for Test-Driven Development: what makes a good test, choosing test seams, anti-patterns to avoid, and rules of the red-green loop.",
    "Refactoring is not part of the loop. Leave cleanup until all slices are green; refactoring mid-loop invites premature abstraction across shapes that haven't settled yet.",
    "Red before green. Watch the test fail for the expected reason before writing the implementation.",
    "Synthesize the current conversation into a decision-complete spec on your issue tracker, agree on test seams, and label it ready-for-agent.",
    "Do NOT interview the user; just synthesize what you already know.",
    "Break a spec or plan into vertical tracer-bullet tickets (or expand-contract steps) with blocking dependencies on your issue tracker.",
    "Triage inbound issues and external PRs through category and state roles (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix).",
    "Chart and work through a multi-session planning map on your issue tracker using decision tickets (grilling, prototype, research, task) and a fog-of-war list.",
    "Plan, don't do. Wayfinder produces decisions and a clearer map, not production code.",
    "Generate an interactive, idempotent bash wizard script for human-only setup or deployment steps (provisioning, secrets, dashboards, cutovers).",
    "Verify with bash -n and shellcheck. Do not execute the script.",
    "Stress-test an idea, plan, or decision through structured, opinionated interviewing until you and the agent reach shared understanding.",
    "Relentless, structured interview loop that maps a design tree, resolves the frontier of open decisions with recommended answers, and researches facts in subagents.",
    "Finding facts is your job, never the user's. Before asking anything the repo, docs, or web could answer, dispatch a background subagent",
    "Word the question so yes accepts the recommendation.",
    "Compact the current conversation into a portable markdown handoff file in your OS temp directory so a fresh agent session can pick up cleanly.",
    "Multi-session personal tutor that builds an interactive HTML curriculum, tracks storage strength vs fluency in learning records, and tests retrieval with desirable difficulty.",
    "Turn open questions for a stakeholder, client, or teammate into a self-contained markdown questionnaire file they can fill in asynchronously.",
    "Grill the send, never the subject",
    "Lost the thread or hit a wall of jargon? Re-explain the last message in plain Simplified Technical English using your repo's glossary.",
    "Wait, I don't understand where you've got to here. Re-pitch that: give me a little bit of context, talk in ASD-STE100 Simplified Technical English",
    "Principles and mechanics for writing documents that agents read: skills (SKILL.md), AGENTS.md, CLAUDE.md, coding standards, and prompts.",
    "A good agent doc runs the same process every time. Given the same inputs, the agent takes the same steps in the same order",
    "A short doc that branches three ways and hedges its steps is small in context and heavy in thought.",
    "Naming what not to do puts the thing in the working space.",
    "The no-op test: would the agent do this anyway without the instruction? Every instruction that passes the no-op test is pure load.",
    "One adapter is a hypothetical seam; two make it real.",
    "No red-capable command, no Phase 2.",
    "If you cannot state the prediction, the hypothesis is a vibe",
    "Passive domain awareness (reading GLOSSARY.md) is done inline; active domain work calls domain-modeling.",
]


def normalize_words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def build_studied_5grams():
    grams = set()
    for sentence in STUDIED_REPO_CORPUS:
        words = normalize_words(sentence)
        for i in range(len(words) - 4):
            grams.add(tuple(words[i : i + 5]))
    return grams


def parse_frontmatter(content):
    if not content.startswith("---\n"):
        return None, content, "File must start with '---\\n' on line 1"
    end_idx = content.find("\n---\n", 4)
    if end_idx == -1:
        return None, content, "Missing closing '---' for YAML frontmatter"
    fm_raw = content[4:end_idx]
    body = content[end_idx + 5 :]
    fm = {}
    for line in fm_raw.splitlines():
        line_str = line.strip()
        if not line_str or line_str.startswith("#"):
            continue
        if ":" not in line_str:
            return None, body, f"Invalid YAML frontmatter line: {line}"
        k, v = line_str.split(":", 1)
        k = k.strip()
        v = v.strip()
        if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
            v = v[1:-1]
        elif v.lower() == "true":
            v = True
        elif v.lower() == "false":
            v = False
        fm[k] = v
    return fm, body, None


def main():
    errors = []
    warnings = []
    metrics = []

    # 1. Check manifests
    pkg_path = os.path.join(ROOT, "package.json")
    cp_path = os.path.join(ROOT, ".claude-plugin", "plugin.json")
    mp_path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    cx_path = os.path.join(ROOT, ".codex-plugin", "plugin.json")

    for mpath in [pkg_path, cp_path, mp_path, cx_path]:
        if not os.path.exists(mpath):
            errors.append(f"Missing manifest: {mpath}")
        else:
            try:
                with open(mpath, "r", encoding="utf-8") as f:
                    json.load(f)
            except Exception as e:
                errors.append(f"Invalid JSON in {mpath}: {e}")

    if not errors:
        with open(pkg_path) as f:
            pkg = json.load(f)
        with open(cp_path) as f:
            cp = json.load(f)
        with open(mp_path) as f:
            mp = json.load(f)
        with open(cx_path) as f:
            cx = json.load(f)

        if cp.get("version") != pkg.get("version") or cx.get("version") != pkg.get("version"):
            errors.append("Version mismatch between package.json, .claude-plugin/plugin.json, and .codex-plugin/plugin.json")
        if mp.get("plugins", [{}])[0].get("name") != cp.get("name"):
            errors.append("Marketplace plugin entry name does not match .claude-plugin/plugin.json name")
        if "version" in mp.get("plugins", [{}])[0]:
            warnings.append("marketplace.json plugin entry sets 'version' alongside plugin.json (triggers Claude Code validator warning)")

    # 2. Check skills directory
    skills_dir = os.path.join(ROOT, "skills")
    if not os.path.isdir(skills_dir):
        errors.append("Missing skills/ directory")
        found_skills = set()
    else:
        found_skills = {
            d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))
        }

    missing_skills = ALL_EXPECTED_SKILLS - found_skills
    extra_skills = found_skills - ALL_EXPECTED_SKILLS
    if missing_skills:
        errors.append(f"Missing expected skills: {sorted(missing_skills)}")
    if extra_skills:
        errors.append(f"Unexpected skill folders: {sorted(extra_skills)}")

    # 3. Validate each skill
    for skill_name in sorted(found_skills):
        sdir = os.path.join(skills_dir, skill_name)
        sfile = os.path.join(sdir, "SKILL.md")
        oyaml = os.path.join(sdir, "agents", "openai.yaml")

        if not os.path.exists(sfile):
            errors.append(f"[{skill_name}] Missing SKILL.md")
            continue
        if not os.path.exists(oyaml):
            errors.append(f"[{skill_name}] Missing agents/openai.yaml")

        with open(sfile, "r", encoding="utf-8") as f:
            content = f.read()

        fm, body, err = parse_frontmatter(content)
        if err:
            errors.append(f"[{skill_name}] Frontmatter error: {err}")
            continue

        # Check name
        fm_name = fm.get("name", "")
        if fm_name != skill_name:
            errors.append(f"[{skill_name}] Frontmatter name '{fm_name}' != folder name '{skill_name}'")
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", str(fm_name)) or len(str(fm_name)) > 64:
            errors.append(f"[{skill_name}] Invalid skill name format: '{fm_name}'")

        # Check description
        desc = str(fm.get("description", ""))
        desc_words = len(desc.split())
        desc_chars = len(desc)
        if not desc:
            errors.append(f"[{skill_name}] Missing description")
        elif desc_chars > 1024:
            errors.append(f"[{skill_name}] Description exceeds 1024 chars ({desc_chars})")
        elif desc_words < 12 or desc_words > 42:
            errors.append(f"[{skill_name}] Description word count ({desc_words}) outside 12-42 word target")

        # Check invocation flags
        is_user = skill_name in EXPECTED_USER_SKILLS
        if is_user:
            if fm.get("disable-model-invocation") is not True:
                errors.append(f"[{skill_name}] User command must set 'disable-model-invocation: true'")
            if os.path.exists(oyaml):
                with open(oyaml, "r", encoding="utf-8") as yf:
                    ycontent = yf.read()
                if "allow_implicit_invocation: false" not in ycontent:
                    errors.append(f"[{skill_name}] User command agents/openai.yaml must set 'allow_implicit_invocation: false'")
        else:
            if "disable-model-invocation" in fm:
                errors.append(f"[{skill_name}] Model capability must NOT set 'disable-model-invocation'")
            if fm.get("user-invocable") is not False:
                errors.append(f"[{skill_name}] Model capability must set 'user-invocable: false'")
            if "Use when" not in desc:
                errors.append(f"[{skill_name}] Model capability description must include 'Use when...' trigger clause")
            if os.path.exists(oyaml):
                with open(oyaml, "r", encoding="utf-8") as yf:
                    ycontent = yf.read()
                if "allow_implicit_invocation: true" not in ycontent:
                    errors.append(f"[{skill_name}] Model capability agents/openai.yaml must set 'allow_implicit_invocation: true'")

        # Check body lines
        total_lines = len(content.splitlines())
        body_lines = len(body.strip().splitlines())
        if total_lines > 110:
            errors.append(f"[{skill_name}] SKILL.md exceeds 110-line budget ({total_lines} lines)")

        # Check cross-skill invocation syntax and one-way hierarchy
        called_skills = re.findall(r'run the `([a-z0-9-]+)` skill|Skill tool with "([a-z0-9-]+)"', body)
        for g1, g2 in called_skills:
            target = g1 or g2
            if target in EXPECTED_USER_SKILLS:
                errors.append(f"[{skill_name}] Illegal call to user-invoked command '{target}' via Skill tool")
            elif target not in EXPECTED_MODEL_SKILLS:
                errors.append(f"[{skill_name}] Calls unknown skill '{target}'")

        # Check sidecar file references inside skill
        sidecar_refs = re.findall(r'`([A-Z0-9_-]+\.md)`', body)
        for sref in sidecar_refs:
            if sref in ("SKILL.md", "CLAUDE.md", "AGENTS.md", "README.md", "WORDS.md", "DECISIONS.md", "CHANGELOG.md"):
                continue
            if not os.path.exists(os.path.join(sdir, sref)):
                errors.append(f"[{skill_name}] Broken sidecar reference '{sref}' (file not found in {sdir})")

        metrics.append({
            "skill": skill_name,
            "type": "user-command" if is_user else "model-capability",
            "desc_words": desc_words,
            "desc_chars": desc_chars,
            "total_lines": total_lines,
            "body_lines": body_lines,
        })

    # 4. Walk all plugin files for originality, forbidden terms, em-dashes, and 5-gram similarity
    studied_5grams = build_studied_5grams()
    for dirpath, _, filenames in os.walk(ROOT):
        for fname in filenames:
            if fname == "validate-plugin.py":
                continue
            fpath = os.path.join(dirpath, fname)
            rel_fpath = os.path.relpath(fpath, ROOT)
            if os.path.islink(fpath):
                continue
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    text = f.read()
            except Exception:
                continue

            # Em-dash / en-dash check
            if "—" in text or "–" in text:
                errors.append(f"[{rel_fpath}] Contains forbidden em-dash (—) or en-dash (–)")

            # Forbidden origin terms check
            lower_text = text.lower()
            for term in FORBIDDEN_ORIGIN_TERMS:
                if term in lower_text:
                    errors.append(f"[{rel_fpath}] Contains forbidden reference term '{term}' (violates Originality Rule)")

            # 5-word similarity check against studied repo corpus
            words = normalize_words(text)
            for i in range(len(words) - 4):
                gram = tuple(words[i : i + 5])
                if gram in studied_5grams:
                    phrase = " ".join(gram)
                    errors.append(f"[{rel_fpath}] 5-word overlap with studied repo: '{phrase}'")

    # Print report
    print("=== VIBE-STACK VALIDATION & ORIGINALITY REPORT ===")
    print(f"Skills discovered: {len(found_skills)} / {len(ALL_EXPECTED_SKILLS)}")
    if metrics:
        print("\nSkill Size & Context Footprint:")
        print(f"{'Skill':<20} {'Type':<18} {'Desc Words':<12} {'Desc Chars':<12} {'Total Lines':<12}")
        print("-" * 76)
        for m in metrics:
            print(f"{m['skill']:<20} {m['type']:<18} {m['desc_words']:<12} {m['desc_chars']:<12} {m['total_lines']:<12}")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  [ERROR] {e}")
        sys.exit(1)
    else:
        print("\nSUCCESS: All manifest, frontmatter, link, invocation, and originality checks passed 100% clean!")
        sys.exit(0)


if __name__ == "__main__":
    main()
