# tests = (
#     ("asdfadsf", ['as', 'df', 'ad', 'sf']),
#     ("asdfads", ['as', 'df', 'ad', 's_']),
#     ("", []),
#     ("x", ["x_"]),
# )

def solution(s):
    new = [s[x: x + 2] for x in range(0, len(s)-1, 2)]
    if len(s) % 2 == 1:
        new.append(s[-1]+ '_')
        return new
    elif len(s) == 0:
        return []
    else:
        return new