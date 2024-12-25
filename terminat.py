#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = round(3.14159)
b = round(3.14159,3)
print(a)
print(b)


# In[2]:


a = sum([1,2,3,4])
b = sum([1,2,3,4])
c = sum([1,2,3,4],5)
print(a)
print(b)
print(c)


# In[3]:


def hello():     print('OK')      
hello() 
hello() 


# In[7]:


import requests  

# 下載匯率的 CSV 檔案
url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'   
rate = requests.get(url)

# 設定編碼格式
rate.encoding = 'utf-8'      

# 取得文本內容並拆分成行
rt = rate.text              
rts = rt.split('\n')       

# 處理每一行
for i in rts:               
    try:                             
        a = i.split(',')   # 將行內容用逗號拆分成列表
        if len(a) > 12:    # 確保索引 12 存在，避免索引錯誤
            print(a[0] + ': ' + a[12])        
    except Exception as e:  # 捕捉錯誤並打印錯誤訊息
        print(f"Error processing line: {i}, Error: {e}")


# In[8]:


def bubble_sort(arr):
    n = len(arr)
    # 外層迴圈：每次確認最後一個元素是否正確排列
    for i in range(n):
        swapped = False  # 用於檢查本輪是否發生交換
        # 內層迴圈：逐一比較相鄰元素
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 如果前面的元素比後面的大，交換它們
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果內層迴圈沒有交換，代表陣列已經排序完成
        if not swapped:
            break
    return arr

# 測試範例
numbers = [64, 34, 25, 12, 22, 11, 90]
print("未排序陣列:", numbers)
sorted_numbers = bubble_sort(numbers)
print("排序後陣列:", sorted_numbers)


# In[ ]:




