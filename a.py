print("3 tane sayı gir")
s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1 > s2 and s1 > s3:
    print(str(s1) + " en büyük")
else:
    if s2 > s1 and s2 > s3:
        print(str(s2) + " en büyük")
    else:
        print(str(s3) + " en büyük")
