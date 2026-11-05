#!/usr/bin/env python3
"""Lint role-tagged LAW.md and render review previews using the documented tag rules.

This is a standalone reference implementation, not the user's production renderer.
"""
from pathlib import Path
import argparse, re, sys

ROLES = {'communicator', 'manager', 'worker'}
HEADING = re.compile(r'^(#{1,6})\s+(.*)$')
TAG = re.compile(r'\s+@([a-zA-Z][a-zA-Z0-9_-]*)')
REF = re.compile(r'\bSection\s+(\d+(?:\.\d+)*)\b', re.I)

class Node:
    def __init__(self, level, title, roles, explicit, line):
        self.level, self.title, self.roles, self.explicit, self.line = level, title, roles, explicit, line
        self.own=[]; self.children=[]

def parse(path):
    roots=[]; stack=[]; fence=None; errors=[]
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line=raw.rstrip()
        fm=re.match(r'^\s*(```+|~~~+)', line)
        if fm:
            marker=fm.group(1)[0]
            if fence is None: fence=marker
            elif fence==marker: fence=None
            if stack: stack[-1].own.append(line)
            continue
        m=HEADING.match(line) if fence is None else None
        if m:
            level=len(m.group(1)); rawtitle=m.group(2)
            tags=TAG.findall(rawtitle)
            if len(tags) != len(set(tags)): errors.append(f'line {n}: duplicate role tag')
            title=TAG.sub('', rawtitle).rstrip()
            bad=[t for t in tags if t not in ROLES]
            for t in bad: errors.append(f'line {n}: unknown role tag @{t}')
            explicit=bool(tags)
            if explicit:
                roles=set(t for t in tags if t in ROLES)
            else:
                roles=set(stack[-1].roles) if stack else set()
            node=Node(level,title,roles,explicit,n)
            while stack and stack[-1].level>=level: stack.pop()
            if stack: stack[-1].children.append(node)
            else: roots.append(node)
            stack.append(node)
        elif stack:
            stack[-1].own.append(line)
    return roots, errors

def walk(nodes):
    for n in nodes:
        yield n
        yield from walk(n.children)

def render_nodes(nodes, role):
    out=[]
    for n in nodes:
        child=render_nodes(n.children, role)
        own='\n'.join(n.own).strip('\n')
        own_visible = role in n.roles and bool(own.strip())
        if own_visible or child:
            if role in n.roles:
                out.append('#'*n.level+' '+n.title)
                if own.strip(): out.append(own)
            if child: out.append(child)
    return '\n\n'.join(x for x in out if x).strip()+'\n'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('law', type=Path)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--max-words', type=int, default=6000, help='warning threshold per rendered role view')
    args=ap.parse_args()
    nodes, errors=parse(args.law)
    allnodes=list(walk(nodes))
    for role in sorted(ROLES):
        contracts=[n for n in allnodes if n.title==f'You are the {role.title()}' and role in n.roles]
        if len(contracts)!=1: errors.append(f'{role}: expected exactly one role identity contract, found {len(contracts)}')
        view=render_nodes(nodes,role)
        if not view.startswith(f'### You are the {role.title()}'):
            errors.append(f'{role}: rendered view does not begin with its role identity')
        if 'Role-tag semantics' in view or 'This file defines durable operating principles' in view:
            errors.append(f'{role}: source/compiler-only preamble leaked into rendered view')
        if re.search(r'^#{1,6}\s*$',view,re.M): errors.append(f'{role}: empty heading in rendered view')
        present=set(re.findall(r'^##\s+(\d+)(?:\.|\s)',view,re.M))
        for sub in re.findall(r'^###\s+(\d+)\.\d+\b',view,re.M):
            if sub not in present: errors.append(f'{role}: subsection {sub} appears without its parent section')
        for ref in REF.findall(view):
            top=ref.split('.')[0]
            if top not in present: errors.append(f'{role}: dangling cross-reference to Section {ref}')
        wc=len(re.findall(r'\b\w+\b',view))
        if wc>args.max_words: print(f'WARN {role}: {wc} words exceeds warning threshold {args.max_words}')
        dest=args.out/('AGENTS.md' if role=='communicator' else f'agents/{role}.md')
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(view, encoding="utf-8")
        print(f'{role}: {wc} words -> {dest}')
    if errors:
        print('\n'.join('ERROR '+e for e in errors),file=sys.stderr)
        return 1
    print('PASS: role tags, role contracts, headings, and rendered cross-references')
    return 0
if __name__=='__main__': raise SystemExit(main())
