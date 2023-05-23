import numpy as np
#numpyとは。行列の計算やベクトル演算を高速に処理するためのライブラリ
x = np.array([1,2])
print(x)
print(x.shape)#配列の要素数

#二次元配列
y = np.array([[1,2],[3,4]])
print(y)
print(y.shape)#配列の要素数
#配列の計算
x1 = x+1#すべての要素に+1する。
print(x1)
#配列同士の計算
x2 = x + x1
print(x2)
x3 = x + y
print(x3)#ブロードキャスト
#次元を確認
print("xの次元数は、",x.ndim,"yの次元数は、",y.ndim)
    #len(x.shape)
#n次元配列の全ての要素数
print(y.size)
#dtypeオブジェクト(numpyのデータ型)
print(x.dtype)
x4 = np.array([3.14,1.414,1.732])
print(x4.dtype)
#x=np.array([1,2,3],dtype = 'float32')#など、データ型の指定ができる。
