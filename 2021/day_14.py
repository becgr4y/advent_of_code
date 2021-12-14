from collections import Counter

with open("2021/inputs/14") as f:
    data = [line.strip() for line in f]


instructions_split = data.index("")
polymer_chain = [inner for outer in data[:instructions_split] for inner in outer]

insertion_instructions = {
    item.split(" -> ")[0]: item.split(" -> ")[1]
    for item in data[instructions_split + 1 :]
}

# Part 1
part_1 = polymer_chain

# for step in range(10):
#     next_chain = []
#     for letter in range(len(part_1) - 1):
#         new_letter = insertion_instructions[part_1[letter] + part_1[letter + 1]]
#         next_chain.append(part_1[letter])
#         next_chain.append(new_letter)
#     next_chain.append(part_1[letter + 1])
#     part_1 = next_chain

# c = Counter(part_1).most_common()
# most = c[0]
# least = c[-1]

# print(most[1] - least[1])

# Part 2
insertion_instructions_pairs = {
    item.split(" -> ")[0]: [
        item.split(" -> ")[0][0] + item.split(" -> ")[1],
        item.split(" -> ")[1] + item.split(" -> ")[0][1],
    ]
    for item in data[instructions_split + 1 :]
}

polymer_pairs = [
    polymer_chain[i] + polymer_chain[i + 1] for i in range(len(polymer_chain) - 1)
]

polymer_pairs = {x: polymer_pairs.count(x) for x in polymer_pairs}

for step in range(40):
    new_pairs = {x: 0 for x in list(insertion_instructions.keys())}
    new_pairs.update(polymer_pairs)
    for key, val in polymer_pairs.items():
        new_pairs[key] = new_pairs[key] - val
        new_values = insertion_instructions_pairs[key]
        for pair in new_values:
            new_pairs[pair] = new_pairs[pair] + val
    polymer_pairs.update(new_pairs)
    polymer_pairs = {idx: val for idx, val in polymer_pairs.items() if val > 0}

single_letters = {x: 0 for x in set("".join(polymer_pairs.keys()))}

for key, val in polymer_pairs.items():
    single_letters[key[0]] += val / 2
    single_letters[key[1]] += val / 2

most = max(single_letters, key=single_letters.get)
least = min(single_letters, key=single_letters.get)
print(single_letters[most] - single_letters[least])
