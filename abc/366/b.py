def make_s_list(n, s):
    s.reverse()
    s_list = []
    for i in range(n):
        s_list.append(list(s[i]))
    return s_list

def t(n, s, j):
    t = []
    s_list = make_s_list(n, s)
    for i in range(n):
        if j >= len(s_list[i]):
            t.append("*")
        else:
            t.append(s_list[i][j])
    t_join = "".join(t)
    return t_join

def vertical_writing(n, s):
    result = []
    for j in range(4):
        result.append(t(n, s, j))
    return result

n = int(input())
s = [input() for _ in range(n)]
print(vertical_writing(n, s))