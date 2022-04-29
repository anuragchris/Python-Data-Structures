def kmp(text: str, pattern: str) -> bool:
    lps = compute_lps(pattern)
    i, j = 0, 0

    while i < len(text) and j < len(pattern):

        if(text[i] == pattern[j]):
            i += 1
            j += 1

        else:
            if j != 0:
                j = lps[j-1]

            else:
                i += 1

    if j == len(pattern):
        return True

    return False


def compute_lps(pattern: str):
    lps = [0]*len(pattern)
    idx = 0

    for i in range(1, len(pattern)):

        if(pattern[i] == pattern[idx]):
            lps[i] = idx+1
            idx += 1
            i += 1

        else:
            if idx != 0:
                idx = lps[idx-1]

            else:
                lps[i] = 0
                i += 1

    return lps


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(kmp(txt, pat))
