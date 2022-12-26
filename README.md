# Line-Bot
homework of theorem of computation
## line bot在做什麼？
他可以幫你從網路上查詢人類圖的相關資訊
1. 閘門代表的意義
2. 能量中心代表的意義
3. 人生角色的意義

## 如何與他互動
一開始是在select的步驟，可以打任意訊息，line bot 會回復如何進到3個查詢狀態
![](https://i.imgur.com/r6WpZ0c.png)

1. 輸入gate進入到查詢閘門意義的模式，line bot 會告知如何使用，若不清楚，可以打help得知進一步資訊，輸入閘門數字則會得到此閘門的查詢結果。

![](https://i.imgur.com/krPr7W0.png)

輸入back會回到select的步驟

![](https://i.imgur.com/twYzyc0.png)

2. 輸入center進入到查詢能量中心意義的模式，line bot 會告知如何使用，若不清楚，可以打help得知進一步資訊(能量中心名稱)，輸入能量中心的名稱則會得到他的查詢結果。

![](https://i.imgur.com/klJHlav.png)

3. 輸入profile進入到查詢人生角色意義的模式，line bot 會告知如何使用，若不清楚，可以打help得知進一步資訊(12種人生角色)，輸入人生角色分類則會得到此角色的查詢意義。

![](https://i.imgur.com/dPgmvSN.png)

要回到select狀態才可以進到其他查詢狀態!!

## FSM picture
![](https://i.imgur.com/ZuY4iE1.png)

## 爬蟲
在獲得查詢資料內容的步驟，我使用了python的BeautifulSoup，來對一個有寫好 人類圖 各種解釋的網站做獲取資訊的動作

![](https://i.imgur.com/XvmfaWW.png)

