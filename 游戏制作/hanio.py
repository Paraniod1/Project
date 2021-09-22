def hanio(n, x, y, z):
    if n == 1:
        print(x, "-->", z)
    else:
        hanio(n-1, x, z, y)  # 将前n-1个盘子从x移动到y
        print(x, "-->", z)  # 将最地下最后一个盘子从x移动到z
        hanio(n-1, y, x, z)  # 将y上的n-1个盘子移动到z上


if __name__ == "__main__":
    n = int(input("请输入汉诺塔的层数："))
    hanio(n, 'X', 'Y', 'Z')
