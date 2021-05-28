while True:
    height = int(input("Altura: "))
    if height > 1 and height < 9:
        break

print()

for i in range(1, height + 1): 

    print(" " * (height - i) + "#" * i, end="")
    print("  ", end="")
    print("#" * i)
