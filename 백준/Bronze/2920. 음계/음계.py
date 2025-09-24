st = "".join(input().split())

if st == "12345678":
    print("ascending")
elif st == "12345678"[::-1]:
    print("descending")
else:
    print("mixed")