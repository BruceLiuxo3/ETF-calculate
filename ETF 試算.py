Python 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def moneysecret ():
    資產 = int(input("初始資產（幾萬）:"))
    利率 = float(input("利率(ex:年化報酬8% 輸入1.08):"))
    每年投入 = int(input("每年固定投入（幾萬）:"))
    幾年 = int(input("投入幾年:"))
    本金=資產

    for i in range(0,幾年):
        if i<=(幾年-1):
            資產 = (資產+每年投入)*利率
            print('第{}年ETF總資產:'.format(i+1),資產)
            淨利潤=資產-(本金+每年投入*幾年)
            i += 1
    print('第{}年總資產:'.format(幾年),資產)
    print('淨利潤:',淨利潤)

moneysecret()
