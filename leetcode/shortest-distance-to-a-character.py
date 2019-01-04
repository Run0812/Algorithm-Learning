S = "baab"
C = 'b'

a = [None, None]
l = len(S)
ans = []
# [3,2,1,0,1,0,0,1,2,2,1,0]
for i in range(l):
    if S[i] == C:
        a.append(i)
        a.pop(0)
        if a[0] is None:
            ans[:a[1]] = range(a[1], 0, -1)
        else:
            max = (a[1] - a[0]) // 2
            if (a[1] - a[0] - 1) % 2 == 0:
                ans[a[0] + 1:a[1]] = list(range(1, max + 1)) + list(range(max, 0, -1))
            else:
                ans[a[0] + 1:a[1]] = list(range(1, max)) + list(range(max, 0, -1))
        ans.append(0)
        print(ans)
if a[1] != l-1:
    ans[a[1]+1:] = range(1, l-a[1])
print('ans=', ans)