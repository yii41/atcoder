n, t, a =  map(int, input().split())
if abs(n - t - a) < abs(t - a):
    print("Yes")
else:
    print("No")
