n = int(input())
x = list(map(int, input().split()))
weight = list(map(int, input().split()))

wmean = 0
wsum = 0
for i in range(n):
    wmean += x[i] * weight[i]
    wsum += weight[i]

wmean = wmean / wsum

print(f"{wmean:.1f}")
