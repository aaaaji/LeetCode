## 解題解析
- 初始化一個 Directory 為 D
- 用 for 迴圈搭配 enumerate, 同時取 序列 ＆ 值
- 如果 目標值 - 現在數據值 不在 D 裡面，則在 D 存 Key & 值
- 如果 差值 在 D 裡面，則回傳 D 存的 值對應序列 及 現在的序列

## 問題
- 若結果不只一個（有多種可相加為目標數值的組合）
    - 其 顯示結果 會是 **最先** 相加為目標值的答案
    - 第一個序列值為最右（如果數值重複出現），第二個序列值為最左（最先達成目標值）
