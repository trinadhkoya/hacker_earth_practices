T = int(input())
while T!=0:
    N = int(input())
    S = input()[:N]
    output = []
    for i in S:
        if ord(i) <= 69:
            output.append(67)
        elif ord(i) >= 70 and ord(i) <= 72:
            output.append(71)
        elif ord(i) >= 73 and ord(i) <= 76:
            output.append(73)
        elif ord(i) >= 77 and ord(i) <= 81:
            output.append(79)
        elif ord(i) >= 82 and ord(i) <= 86:
            output.append(83)
        elif ord(i) >= 87 and ord(i) < 94:
            output.append(89)
        elif ord(i) >= 94 and ord(i) <= 99:
            output.append(97)
        elif ord(i) >= 100 and ord(i) <= 102:
            output.append(101)
        elif ord(i) >= 103 and ord(i) <= 105:
            output.append(103)
        elif ord(i) >= 106 and ord(i) <= 108:
            output.append(107)
        elif ord(i) >= 109 and ord(i) <= 111:
            output.append(109)
        elif ord(i) >= 112:
            output.append(113)
         
    print("".join(chr(i) for i in output))
    T-=1