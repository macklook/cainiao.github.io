# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
解题思路：
1.利用range创建4个数，但是range(开始位置，结束位置-1)，所以要设置为range(1,5),创建了第一位数as i
2.利用range创建4个数，但是range(开始位置，结束位置-1)，所以要设置为range(1,5),创建了第二位数as j
3.利用range创建4个数，但是range(开始位置，结束位置-1)，所以要设置为range(1,5),创建了第三位数as k
4.不能重复表明 （i不等于j）并且（i不等于k）并且（j不等于k）
5.打印i和j和k
"""
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i, j, k)
