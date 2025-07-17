# review(留言)-analytics(分析)
# calc = calculate 計算
# avg = 平均長度
# calc avg length of reviews
# 讀取
data = []
count = 0
length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length = length + len(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取玩了，總共有', len(data), '筆留言')
print("平均每筆留言有", length/len(data), "字")
# 篩選
good = []
for g in data:
	if 'good' in g:
		good.append(g)
print("一共有", len(good), "筆留言有提到good")
# 新增單字進到字典裡
wc = {}
for d in data:
	words = d.split(
		)
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
# 列出出現次數超過100萬的單字
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
# 查詢功能
while True:
	word = input('請問你想要查什麼字')
	if word == 'q':
		break
	if word in wc:
		print(w, '出現過的次數為:', wc[w])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用本查詢功能')



# print(data[0])
# List comprehention 清單快寫法(自取): 變數 = [{運算}for {變數} in {清單} {篩選條件}]
# good = [d for d in data if 'good' in d ]
# print("一共有", len(good), "筆留言有提到good")