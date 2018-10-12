#若一个口袋中放有12个球，其中有3个红的，3个白的和6个黒的。
#从中任取8个共有多少种不同的颜色搭配
#任取八个球，那么就算红白球全都拿上，也只有6个。
#所以黑球起码有2个。黑球在2到6之间
#如果黑球6个都拿走了，那么红球白球也可能一个都没有
#所以红球和白球取的个数范围在0到3之间
for red in range(0,4):
    for white in range(0,4):
        for black in range(2,6):
            if red+white+black == 8:
                print(red,white,black)
                n += 1
print("一共有",n,"种情况")
