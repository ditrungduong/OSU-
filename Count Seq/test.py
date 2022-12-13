def count_seq():
    seq = "2"
    while True:
        yield seq
        new_seq = ""
        cur = seq[0]
        ct = 1
        for char in seq[1:]:
            if char == cur:
                ct += 1
            else:
                new_seq += str(ct) + cur
                cur = char
                ct = 1
        seq = new_seq + str(ct) + cur
print(count_seq())