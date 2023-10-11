s1 = input()
s2 = input()
swap = {}
correct = []

for i in range(len(s1)):
	if s1[i] != s2[i]:
		if s1[i] in correct or s2[i] in correct:
			print(-1)
			exit()
		if s2[i] not in swap and s1[i] not in swap:
			swap[s2[i]] = s1[i]
			swap[s1[i]] = s2[i]
		if (s1[i] in swap and swap[s1[i]] != s2[i]) or (s2[i] in swap and swap[s2[i]] != s1[i]):
			print(-1)
			exit()
	else:
		if s2[i] in swap or s1[i] in swap:
			print(-1)
			exit()
		else:
			correct.append(s1[i])
print(round(len(swap) / 2))

for i in set(s1):
	if i in swap and swap[i] != 0:
		print(i, swap[i])
		swap[swap[i]] = 0