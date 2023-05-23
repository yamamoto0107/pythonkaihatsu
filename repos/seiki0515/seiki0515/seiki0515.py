# -*- coding: utf-8 -*-
str = input("文字列を入力してください\n")

print("文字列は、",str,"です")
print("０番目の文字は、",str[0],"です")
print("文字列を逆順にすると、",str[::-1],"です")
print("文字列の長さは、",len(str),"です")

#大小文字変換(メソッド)
print("大文字:",str.upper())
print("小文字:",str.lower())

#フォーマット
print("{0}は{1}{2}です。".format("今日","よい","天気"))
print("{key1}は{key2}{key3}です。".format(key1="今日",key2="よい",key3="天気"))
print("{:,}円".format(1000))
