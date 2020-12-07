def naive_search(string: str, substring: str, case_insensitive: bool = False) -> list:
    occurrences: list = []
    if case_insensitive:
        string = string.lower()
        substring = substring.lower()
    for i in range(len(string) - len(substring) + 1):
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                break
        else:
            occurrences.append(i)
    return occurrences


if __name__ == '__main__':
    text: str = 'AABAACAADAABAAABAA'
    query: str = 'AABA'
    
    print(naive_search(text, query))
    
    import re
    
    print([match.span()[0] for match in list(re.finditer(query, text))])