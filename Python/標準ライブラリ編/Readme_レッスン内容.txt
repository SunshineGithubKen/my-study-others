ファイル操作：
ファイルの読み書きとオープン方法
ファイルの存在チェックと例外処理
ファイルへの追記と読み込み方法
pprintモジュールを使ったデータの表示方法

標準ライブラリの利用：
標準ライブラリのimportと利用方法
乱数生成や特殊な計算に関連するモジュール（random, math）の使用
日時を操作するためのモジュール（datetime, calendar）の活用

コレクションモジュールの利用：
集計やデータの表示に関連するモジュール（collections, pprint）の使用
defaultdictを使ったデフォルト値の設定
Counterを使った要素の集計

コピーと参照：
浅いコピーと深いコピーの違いとcopyモジュールの活用
参照や代入時のオブジェクトの挙動と注意点

＃Dotinstallより

File Operations:
Reading and Writing Files and File Opening:
To read or write files in Python, you need to open the file first using the open() function.
The open() function takes the file path and the mode (e.g., 'r' for read, 'w' for write) as arguments.
After processing the file, you should close it using the close() method to free up system resources.

Checking File Existence and Exception Handling:
Before opening a file, it's a good practice to check if the file exists to avoid errors.
Python provides exception handling with try, except, and finally blocks to handle errors gracefully.

Appending to and Reading from Files:
To append data to an existing file, open it in the 'a' mode (append).
To read data from a file, open it in the 'r' mode (read) and use methods like read() or readlines().

Displaying Data with pprint Module:
The pprint module provides a pprint() function to pretty-print data structures in a more readable format.

Using the Standard Library:
Importing and Using the Standard Library:
The standard library in Python contains built-in modules that provide various functionalities.
You can import modules using the import statement and use their functions and classes.

Using Modules for Random Number Generation and Special Calculations:
The random module is used for generating random numbers or selecting random elements from sequences.
The math module provides various mathematical functions for special calculations.

Manipulating Dates and Times with Date and Time Modules:
The datetime module allows you to work with dates, times, and time intervals.
The calendar module provides various calendar-related functionalities.

Using Collection Modules:
Using Modules for Aggregation and Data Display:
The collections and pprint modules offer functionalities for data aggregation and pretty-printing.

Setting Default Values with defaultdict:
The defaultdict class from the collections module is used to provide default values for dictionary keys.

Aggregating Elements with Counter:
The Counter class from the collections module is used to count elements in a sequence.

Copying and Referencing:
Difference Between Shallow Copy and Deep Copy and Using the copy Module:
Shallow copy creates a new object that references the original data. Deep copy creates a new object with its own copy of the data.
The copy module provides functions for making shallow and deep copies of objects.

Object Behavior during Referencing and Assignment:
When assigning or referencing objects, it's important to understand how Python handles mutable and immutable objects.