# 递归算法
def fac(n):
    if n == 1 or n == 1:
        return 1
    else:
        return fac(n-1)*n
    
if __name__ == '__main__':   
    n = int(input("请输入你要计算的阶乘的数字:"))
    print("递归计算：{}的阶乘是:{}".format(n,fac(n)))
