with open("2019.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")
    slot_sub = {}
    slot = []
    sub = []
    for line in lines:
        words = line.split()
        first_word = words[0]
        third_word = words[2]
        slot.append(first_word)
        sub.append({first_word: third_word})
    sub_slot = {}
    for s in sub:
        key = list(s.keys())[0]
        value = list(s.values())[0]
        if key not in sub_slot:
            sub_slot[key] = [value]
        else:
            sub_slot[key].append(value)

    print(sub_slot)
