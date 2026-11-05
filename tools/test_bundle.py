#!/usr/bin/env python3
"""Dependency-free structural tests for the v7 policy bundle."""
from pathlib import Path
import subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parents[1]


def require(path, headings):
    text = (ROOT / path).read_text(encoding="utf-8")
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
    require('templates/PLAN.md', ['Work packages', 'Dependencies and risks', 'Resource envelope', 'Next actions'])
    require('templates/STATE.md', ['User-facing summary', 'Verified facts', 'Inferences and assumptions', 'Blockers and risks', 'Pending user input'])
    require('templates/HANDOFF.md', ['Intended result', 'Scope and authority', 'Write scope', 'Acceptance / evaluation conditions', 'Completion report'])
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([sys.executable, str(ROOT/'tools/lint_policy.py'), str(ROOT/'LAW.md'), '--out', td, '--max-words', '7000'], check=True)
        comm = (Path(td)/'AGENTS.md').read_text(encoding='utf-8')
        manager = (Path(td)/'agents/manager.md').read_text(encoding='utf-8')
        worker = (Path(td)/'agents/worker.md').read_text(encoding='utf-8')
        assert comm.startswith('### You are the Communicator')
        assert manager.startswith('### You are the Manager')
        assert worker.startswith('### You are the Worker')
        assert 'Role-tag semantics' not in comm + manager + worker
        for phrase in ('## 7. Research, discovery', '## 9. Shared memory', '## 10. Execution, quality', '## 11. Learning and policy'):
            assert phrase not in comm, f'Communicator leaked project-only section: {phrase}'
        assert 'published communication status' in comm
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
        assert 'USER_MODEL' in manager or 'user model' in manager.lower()
        assert 'multi-outcome' in manager
        assert 'Asynchronous execution and durable completion' in manager and worker
    print('PASS: v9 bundle structural tests')

if __name__ == '__main__':
    main()
