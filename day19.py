import sys

rules = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        break
    key_s, rule_s = line.split(':')
    value = []
    for alt_s in rule_s.strip().split('|'):
        subvalue = []
        for cat_s in alt_s.strip().split():
            if cat_s[0] == '"' and cat_s[-1] == '"':
                subvalue.append(cat_s[1:-1])
            else:
                subvalue.append(int(cat_s))
        value.append(subvalue)
    rules[int(key_s)] = value

def match(rules, message):
    return len(message) in submatch(rules, message, 0, {0})

def submatch(rules, message, rule, indices):
    new_indices = set()
    for alt in rules[rule]:
        cat_indices = set(indices)
        for cat in alt:
            if not cat_indices:
                break
            elif isinstance(cat, str):
                cat_indices = set(i+len(cat) for i in cat_indices if message[i:i+len(cat)] == cat)
            else:
                cat_indices = submatch(rules, message, cat, cat_indices)
        new_indices |= cat_indices
    return new_indices

messages = [line.strip() for line in sys.stdin]

print(sum(match(rules, message) for message in messages))

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

print(sum(match(rules, message) for message in messages))
