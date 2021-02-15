
import time
import progressbar


def read_file(filename): #file read
    data = []
    count = 0
    print('請等待檔案讀取...')
    bar = progressbar.ProgressBar(max_value=1000000)
    bar.start() #修正全部程式運行完會跑出進度調問題
    with open (filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            data.append(line)
            count += 1
            #time.sleep(0.1)
            bar.update(count)
    bar.finish() #修正全部程式運行完會跑出進度調問題
    print('檔案讀取完,總共有', len(data), '筆檔案')
    return data


def data_anaiytics(data): #data anaiytics
    print('數據分析中，請稍等...')
    start_time = time.time() #time模組的'time()'function

    numbers_and_symbol = '1234567890!@#$%^&*()_+~`-=[]}{|:;/.?><,'    
    word_count = {} 
    for d in data:
        for n_a_s in numbers_and_symbol:
             if n_a_s in d:
                d = d.replace(n_a_s, '') #去掉numbers_and_symbol字串
        words = d.split() #split本身就是跳過空白鍵 如果打入' '會出現空字串
        for word in words:
            if word in word_count:
                word_count[word] += 1 
            else:
                word_count[word] = 1 #新增新的字進去word_count字典       
    # for word in word_count: #列出大於__次的字
    #     if word_count[word] > 1000:
    #         print(word, word_count[word])
    # print(word_count['the'])

    end_time = time.time()
    print('共花了', end_time - start_time, '秒')
    return word_count


def user_search(word_count): #user search word
    while True:
        word = input('請問你想找那個單字?(按 q 離開 ): ')
        if word == 'q':
            break
        if word in word_count: #避免當掉 檢查是否有輸入單字
            print('這個字:', word, '出現', word_count[word] , '次')
        else:
            print('這個字:', word, '沒有出現過')
    

def main():
    data = read_file('reviews.txt') 
    word_count = data_anaiytics(data)
    user_search(word_count)


if __name__ == '__main__':
    main()