#!/usr/bin/env python3
"""Trigger-regression scorer. Usage:
  python3 trigger_score.py --probes prompts.json --results results.json [--baseline baseline.json] [--out baseline.json]
Writes F1/precision/recall + FP/FN detail; --baseline prints delta against a previous run."""
import argparse, json, sys

def load(p):
    return json.load(open(p))

def score(probes, results):
    by_id = {r['id']: r['choice'] for r in results}
    tp = fn = fp = tn = 0
    detail = []
    for pr in probes['probes']:
        got = by_id.get(pr['id'])
        exp, pos_exp = pr['expect'], pr['expect'] != 'NO_SKILL'
        if got is None:
            verdict, fn = 'MISSING', fn + 1
        elif exp == got:
            verdict = 'OK'
            if pos_exp: tp += 1
            else: tn += 1
        else:
            verdict = 'FP' if not pos_exp else 'FN'
            fp, fn = fp + (0 if pos_exp else 1), fn + (1 if pos_exp else 0)
        detail.append({'id': pr['id'], 'verdict': verdict, 'expect': exp, 'got': got, 'prompt': pr['prompt']})
    prec = tp / (tp + fp) if tp + fp else 1.0
    rec = tp / (tp + fn) if tp + fn else 1.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    return {'skill': probes.get('skill'), 'n': len(probes['probes']), 'tp': tp, 'fn': fn, 'fp': fp, 'tn': tn,
            'precision': round(prec, 3), 'recall': round(rec, 3), 'f1': round(f1, 3),
            'issues': [d for d in detail if d['verdict'] != 'OK']}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--probes', required=True)
    ap.add_argument('--results', required=True, help='{"results":[{"id":1,"choice":"wxarticle"},...]}')
    ap.add_argument('--baseline')
    ap.add_argument('--out')
    a = ap.parse_args()
    s = score(load(a.probes), load(a.results)['results'])
    if a.baseline:
        b = load(a.baseline)
        print(f"baseline: F1={b['f1']} (P={b['precision']} R={b['recall']})  now: F1={s['f1']} (P={s['precision']} R={s['recall']})  delta F1={s['f1']-b['f1']:+.3f}")
    print(f"F1={s['f1']} precision={s['precision']} recall={s['recall']}  (tp={s['tp']} fn={s['fn']} fp={s['fp']} tn={s['tn']})")
    for i in s['issues']:
        print(f"  [{i['verdict']}] #{i['id']} expect={i['expect']} got={i['got']} :: {i['prompt'][:40]}")
    if a.out:
        json.dump(s, open(a.out, 'w'), ensure_ascii=False, indent=2)
        print(f"-> {a.out}")

if __name__ == '__main__':
    main()
