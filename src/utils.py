def splitarg(s):
    words = list()
    tmpw = ""
    in_quota = False
    for w in s.split():
        if '"' not in w and not in_quota:
            words.append(w)
        elif '"' in w and w[w.index('"')-1] == "\\":
            words.append(w)
        else:
            if '"' in w and w[w.index('"')-1] == "\\":
                tmpw += " " + w
            elif w[-1] == '"':
                tmpw += " " + w[:-1]
                words.append(tmpw)
                tmpw = ""
                in_quota = False
            elif in_quota:
                tmpw += " " + w
            elif w[0] == '"':
                tmpw = ""
                tmpw += w[1:]
                in_quota = True
    return words
