data = []
count = 0
sum_len = 0
line_len = 0
new = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		line_len = len(line)
		sum_len += line_len
		if len(line) < 100:
			new.append(line)

print(len(data))
print('留言的平均長度是', int(sum_len / len(data)))
print('小於100字符的留言有', len(new), '筆。')

