# 景文高中員生消費合作社 資料庫工具      JWSH CO-OP Tools

## 功能 Functions

### coop_search.py

1.  姓名查詢 Real Name Lookup
2.  儲值餘額查詢 Credit Lookup
3.  累積消費額查詢 Total Spending Lookup

### coop_crawler.py

此為資料庫爬蟲，但受限於學校伺服器速度，效能極低

This is a database crawler,but the performance is limited due to school rubbish internet connection.

1.  輸入學號，爬出姓名
2.  提供迴圈功能，可爬出指定數量的資料
3.  此程式會「忽略所有查詢錯誤」，也就是說，如果輸入錯誤的學號，程式不會主動報錯

# 

1.  Submit Student ID, show students' real name.
2.  Loop function that you can set an amount of results you want.
3.  Will ignore every search error (such as Wrong ID...).

## 需求 Requirement

*   Python 3
*   Beautiful Soup 4
*   Internet Connection (lol)

## 聲明 Announcement

此程式僅供研究之用，禁止從事任何不法行為，本人不負任何法律責任

This program "is only for study".  I don't assume any legal liability.

## 授權 Licence

[![CC BY-NC 4.0](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)
CC Attribution-NonCommercial 4.0 International

Your Fork and Pull Request are welcomed!