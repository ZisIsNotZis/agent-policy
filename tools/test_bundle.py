#!/usr/bin/env python3
"""Dependency-free structural tests for the v10 policy bundle."""
from pathlib import Path
import subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parents[1]


def require(path, headings):
    text = (ROOT / path).read_text()
    missing = [h for h in headings if h.lower() not in text.lower()]
    if missing:
        raise SystemExit(f'{path}: missing {missing}')


def main():
    require('templates/GOAL.md', ['Intended outcome', 'Deliverables', 'Constraints and preferences', 'Acceptance conditions', 'Scope mode', 'Shared theme'])
    require('templates/INTENT.md', ['expressed intent', 'Current interpreted Goal', 'Context and scope'])
    require('templates/DECISION_PACKET.md', ['Decision needed', 'Recommended default', 'Reuse', 'Work continuing meanwhile'])
    require('templates/USER_MODEL.md', ['derived', 'inferred', 'Confidence', 'Contradictions'])
    require('agent-policy-skills/user-model-and-questions/SKILL.md', ['Decision packet', 'Explicit current user instructions'])
    require('agent-policy-skills/portfolio-management/SKILL.md', ['Multi-outcome scope', 'Sibling boundaries'])
    for slug in ('portfolio-management', 'user-model-and-questions'):
        skill = (ROOT/'agent-policy-skills'/slug/'SKILL.md').read_text()
        assert skill.startswith('---\nname: '+slug+'\ndescription: '), f'{slug}: missing YAML frontmatter'
    require('templates/PLAN.md', ['Work packages', 'Dependencies and risks', 'Actual operating constraints', 'Next actions'])
    require('templates/STATE.md', ['User-facing summary', 'Verified facts', 'Inferences and assumptions', 'Blockers and risks', 'Pending user input'])
    require('templates/HANDOFF.md', ['Intended result', 'Scope and authority', 'Write scope', 'Acceptance / evaluation conditions', 'Completion report'])
    require('templates/STAGING.md', ['Situation', 'Expected behavior', 'Responsible layer', 'Owner', 'Next action', 'Verification', 'Due point'])
    require('agent-policy-skills/root-cause-and-learning/SKILL.md', ['Reconstruct before correcting', 'Verify learning', 'Process and consume every entry'])
    require('evals/role-and-runtime-scenarios.md', ['A5 — Operation may exceed 60 seconds', 'A6 — Runtime cannot preserve responsiveness or async execution', 'A7 — Runtime imposes a short execution timeout', 'L3 — Processed staging entry remains in queue', 'T1 — Worker sends raw technical diagnostics to Manager'])
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([sys.executable, str(ROOT/'tools/lint_policy.py'), str(ROOT/'LAW.md'), '--out', td, '--max-words', '8000'], check=True)
        comm = (Path(td)/'AGENTS.md').read_text()
        manager = (Path(td)/'agents/manager.md').read_text()
        worker = (Path(td)/'agents/worker.md').read_text()
        assert comm.startswith('### You are the Communicator')
        assert manager.startswith('### You are the Manager')
        assert worker.startswith('### You are the Worker')
        assert 'Role-tag semantics' not in comm + manager + worker
        for phrase in ('## 7. Research, discovery', '## 9. Shared memory', '## 10. Execution, quality', '## 11. Learning and policy'):
            assert phrase not in comm, f'Communicator leaked project-only section: {phrase}'
        assert 'published communication status' in comm
        assert 'user-return/poll driven' in comm
        assert 'do not generate periodic' in comm.lower()
        assert 'Governing precedence' in comm
        assert 'premature' in manager.lower()
        assert 'recursive' in manager.lower()
        assert 'recursive' in worker.lower()
        assert 'root Manager' in comm
        assert 'user communicates only with you' in comm
        assert 'same-CWD Manager' not in comm
        assert 'explicitly selected root' in comm
        assert 'do not search parent directories' in comm
        assert 'startup' in comm
        assert 'upward' not in comm.lower() or 'parent-directory' in comm.lower()
        assert 'write scope' in worker
        assert 'independent verification' in manager
        assert 'principal' in manager and 'escalation path' in manager
        release = Path(td)/'release'
        subprocess.run([sys.executable, str(ROOT/'tools/render.py'), '--out', str(release)], check=True, stdout=subprocess.DEVNULL)
        manager_def = (release/'agents/manager.md').read_text()
        assert manager_def.startswith('---\nname: manager\n')
        assert 'subagentOnlyExtensions: npm:pi-subagents' in manager_def
        assert 'allowNestedSubagents: true' in manager_def
        assert 'timeoutMs:' not in manager_def
        worker_def = (release/'agents/worker.md').read_text()
        assert worker_def.startswith('---\nname: worker\n')
        assert 'timeoutMs:' not in worker_def
        assert 'USER_MODEL' in manager or 'user model' in manager.lower()
        assert 'multi-outcome' in manager
        assert 'Asynchronous execution and durable completion' in manager and worker
        assert 'MUST execute asynchronously' in manager and worker
        assert '60 seconds' in manager and worker
        assert 'PANIC immediately' in manager and worker
        assert 'Do not inspect or reason through raw implementation diagnostics' in manager
        assert 'seven calendar days' in manager
        assert 'PANIC' in comm and 'do not suppress' in comm
        assert 'translates its findings' in worker
        assert 'root-cause-and-learning' in manager and worker
    print('PASS: v12 bundle structural tests')

if __name__ == '__main__':
    main()
