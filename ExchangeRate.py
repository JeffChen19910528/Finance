# 安裝台灣銀行即時匯率查詢模組
import twder

n_derall = twder.now_all()   # 擷取目前所有幣別報價
n_der = twder.now('JPY')   # 擷取目前指定幣別(日幣)報價

print(n_derall)   # 輸出觀察「所有幣別報價」擷取結果
print(n_der)    # 輸出觀察「指定幣別報價」擷取結果
print(f"美金(USD)即時匯率報價：{n_derall['USD']}")   # 從所有報價中提取特定幣別報價資料

# =========格式化輸出資料============ #

n_title = ["資料擷取時間：",  "現金買入：",  "現金賣出：",  "即期買入：", "即期賣出："]    # 設定標題的list供格式化輸出對應之用

for n in range(len(n_der)):
    r1 = n_title[n]+str(n_der[n])
    print(r1)

for n in range(len(n_derall['USD'])):
    r2 = n_title[n]+str(n_derall['USD'][n])
    print(r2)