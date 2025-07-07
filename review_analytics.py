# review(留言)-analytics(分析)
# calc = calculate 計算
# avg = 平均長度
# calc avg length of reviews
data = []
count = 0
length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(data)
		length = length + len(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取玩了，總共有', len(data), '筆留言')
print("平均每筆留言有", length/len(data), "字")
