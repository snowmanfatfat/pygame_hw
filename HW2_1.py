def remove_outliers():
    data = []
    # 當要刪除的資料數量>輸入資料時要重新輸入
    while True:
        n = int(input('Enter the number of smallest and largest values to remove: '))
        q = ""
        while True:
            i = input('Enter a value (q or Q to quit): ')
            # 如果遇到q、Q就跳出迴圈不再輸入資料
            if i.lower() == "q":
                break
            # 如果輸入非q、Q的文字會跳錯誤，要重新輸入
            try:
                # 把輸入的資料存起來
                data.append(int(i))
            except:
                print("Data must be a number, please re-enter")

        print(f'The original data: {data}')
        
        if len(data) >= n:
            # 先把輸入資料排序再挑出前n小跟前n大形成outliers_list，並刪除重複值
            data.sort()
            data_outliers = sorted(list(set(data[:n] + data[-n:])))
            # 將原本輸入資料和outliers_list相比，如果不一樣就挑出來形成處理好的list
            # data[-n:] 取序列的最後 n 個元素。data[:-n]取序列除了最後 n 個元素的其他所有元素。
            data_prep = [i for i in data if i not in data_outliers]
            print(f'The data with the outliers removed: {data_prep}')
            print(f'The outliers: {data_outliers}')
            break
        else:
            print("Error: the number of removed value must smaller than number of entered data, please re-enter")
    
remove_outliers()
