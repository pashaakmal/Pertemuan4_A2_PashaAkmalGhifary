N = input()
N = N.split()

if N[0] == "[]" and N[1] == "()":
    print("Pemain A menang")
elif N[0] == "[]" and N[1] == "8<":
    print("Pemain B menang")
elif N[0] == "()" and N[1] == "[]":
    print("Pemain B menang")
elif N[0] == "()" and N[1] == "8<":
    print("Pemain A menang")
elif N[0] == "8<" and N[1] == "[]":
    print("Pemain A menang")
elif N[0] == "8<" and N[1] == "()":
    print("Pemain B menang")
else:
    print("Draw")