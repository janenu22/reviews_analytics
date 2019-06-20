data = []
count = 0
total_len = 0
line_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		line_len = len(line)
		total_len = total_len + line_len
		if count % 100000 == 0:
			print(len(data))

print(len(data))
print('留言的平均長度是', int(total_len / len(data)))

