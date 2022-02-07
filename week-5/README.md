Request 2
1. 建立一個新的資料庫，取名為 website
2. 在資料庫中，建立會員資料表，取名為 member，須符合欄位設定
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request2.PNG)

Request 3
1. 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request3_1.PNG)

2. 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request3_2.PNG)

3. 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request3_3.PNG)

4. 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request3_4.PNG)

5. 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request3_5.PNG)

6. 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request3_6.PNG)

7. 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request3_7.PNG)

Request 4
1.  取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request4_1.PNG)

2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request4_2.PNG)

3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request4_3.PNG)

Request 5
1. 在資料庫中，建立新資料表，取名字為 message
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request5.PNG)

2. 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request5_1.PNG)

3. 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
![image](https://github.com/CW-Yang/wehelp-assignments/blob/master/week-5/capture/request5_2.PNG)
