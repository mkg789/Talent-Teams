def teamSize(talent, talentsCount):
    n = len(talent)
    ans = []
    sublists = []

    for start in range(n):
        for end in range(start + 1, n + 1):
            l = []
            count = 0

            if len(talent[start:end]) >= talentsCount:
                for i in (talent[start:end]):
                    if i not in l:
                        l.append(i)
                        count += 1
                if count == talentsCount:
                    sublists.append(talent[start:end])
                    break
    for i in sublists:
        ans.append((len(i)))
    while len(ans) != len(talent):
        ans.append(-1)

    return ans


talent = [1, 1, 2, 2, 3, 1, 3, 2]
talentsCount = 3
sublists_nested = teamSize(talent, talentsCount)
print(sublists_nested)