import re
import sys

outer_bag_pattern = re.compile(r'([a-z ]+?) bags contain (.*)')
inner_bag_pattern = re.compile(r'([1-9]*[0-9]) ([a-z ]+?) bags?[,.]')

required_inner_bags = {}
possible_outer_bags = {}

for line in sys.stdin:
    outer_bag_match = outer_bag_pattern.fullmatch(line.strip())
    outer_bag = outer_bag_match.group(1)

    required_inner_bags_for_outer_bag = required_inner_bags.setdefault(outer_bag, {})

    for inner_bag_match in inner_bag_pattern.finditer(outer_bag_match.group(2)):
        inner_bag_count = inner_bag_match.group(1)
        inner_bag = inner_bag_match.group(2)

        required_inner_bags_for_outer_bag[inner_bag] = int(inner_bag_count)

        possible_outer_bags_for_inner_bag = possible_outer_bags.setdefault(inner_bag, {})
        possible_outer_bags_for_inner_bag[outer_bag] = int(inner_bag_count)

def possible_outer_bags_for(inner_bag):
    bags = set()
    for outer_bag in possible_outer_bags.get(inner_bag, {}).keys():
        bags.add(outer_bag)
        bags |= possible_outer_bags_for(outer_bag)
    return bags

print(len(possible_outer_bags_for('shiny gold')))

def required_inner_bags_for(outer_bag):
    bags = 0
    for inner_bag, inner_bag_count in required_inner_bags.get(outer_bag, {}).items():
        bags += inner_bag_count
        bags += inner_bag_count * required_inner_bags_for(inner_bag)
    return bags

print(required_inner_bags_for('shiny gold'))
