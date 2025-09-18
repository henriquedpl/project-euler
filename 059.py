def solution059():
    with open("input/059.txt") as f:
        cypher = [int(c) for c in f.read().strip().split(",")]
        for d1 in range(ord("a"), ord("z") + 1):
            for d2 in range(ord("a"), ord("z") + 1):
                for d3 in range(ord("a"), ord("z") + 1):
                    key = [d1, d2, d3]
                    key_index = 0
                    text = []
                    for c in cypher:
                        text.append(chr(c ^ key[key_index]))
                        key_index = (key_index + 1) % 3
                    full_text = "".join(text)
                    if "the" in full_text and "and" in full_text and "one" in full_text:
                        return sum([ord(c) for c in text])
