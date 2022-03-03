def longest_repetition(c):
    count, m = '', ''
    for x in c:
        if x in count or count == '':
            count += x
        else:
            count = x
        if len(count) > len(m):
            m = count
    return ('',0) if m == '' else (m[0],len(m))