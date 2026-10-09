import sys
sys.path.insert(0, '/Users/yanping.ma/skill-forge/scripts')
from trigger_score import score

probes = {'probes': [
    {'id': 1, 'expect': 'S', 'prompt': 'a'},
    {'id': 2, 'expect': 'S', 'prompt': 'b'},
    {'id': 3, 'expect': 'NO_SKILL', 'prompt': 'c'},
    {'id': 4, 'expect': 'NO_SKILL', 'prompt': 'd'},
]}
res = [
    {'id': 1, 'choice': 'S'},
    {'id': 2, 'choice': 'OTHER'},
    {'id': 3, 'choice': 'NO_SKILL'},
    {'id': 4, 'choice': 'S'},
]
s = score(probes, res)
assert (s['tp'], s['fn'], s['fp'], s['tn']) == (1, 1, 1, 1), s
print('scorer 单测 PASS, F1 =', s['f1'])
