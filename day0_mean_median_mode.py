from scipy import stats

n = int(input())
x = list(map(int, input().split()))

mean = 0

for i in x:
    mean += i

mean = mean / n

x.sort()

if n % 2 == 0:
    median = (x[n//2] + x[(n//2)-1]) / 2
else:
    median = x[(n-1)//2]

mode = stats.mode(x)[0][0]


print(f"{mean:.1f}\n{median:.1f}\n{mode}")
