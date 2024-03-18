data = [] # original from TXT
count = 0
with open ('reviews.txt', 'r') as file: # 開啟某個檔案並讀取內容，使用with open ('file_name.type', 'r') as ___
	for line in file: # 透過.append函式將line內容 for loop填寫至data清單中
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

# filter function: 1. 有條件 2. 參考資料可定義的
# 篩選條件 word < 100
word = []
for word in data: # 將原始data清單更新至word清單中，以免破壞原有
	if len(word) < 100:
		print(word)