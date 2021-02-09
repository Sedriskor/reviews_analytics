data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)#把留言丟到data裡
        count += 1
        if count % 100000 ==0:#如果是100000的倍數
            print(len(data))

print('檔案讀取完,總共有', len(data), '筆檔案')

#求每一筆留言的平均長度
sum_len = 0
for d in data:# 丟到data裡的每一筆留言
    sum_len = sum_len + len(d)
print('平均留言長度為', int(sum_len/len(data)),'字數')
#記得換行 不然會在FOR的範圍內一直跑

#清單的篩選
#長度的篩選
new = [] # new = 留言長度小於100字的清單
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '留言長度小於100')#這邊是字母總數 非單字
print(new[0])
print(new[1])

#單字的篩選
good_str = [] # good_str = 含good單字的清單
for d in data:
    if 'good' in d:
        good_str.append(d)
print('一共有', len(good_str), '留言提到good')
print(good_str[0])
print(good_str[1])

#list comprehension(清單快寫法)
good_str1 = [d for d in data if 'good' in d]
#output=[運算(d) for 變數(d) in 清單(data) if 篩選條件('good' in d) ]
#從for之後開始跑 再丟到d(同等good_str.append(d))
print('一共有', len(good_str1), '留言提到good')

commit = int(input('要看第幾筆留言： '))
commit = commit - 1

print(good_str1[commit])

bad_str = ['bad' in d for d in data]
#'bad' in d 為布林值
print(bad_str[0])
