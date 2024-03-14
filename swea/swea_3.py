t = int(input())

for i in range(1,t+1):
    text = input()
    result = ""
    for char in text[::-1]:
        if char == "p":
            char = "q"
        elif char == "q":
            char = "p"
        elif char == "b":
            char = "d"
        elif char == "d":
            char = "b"
        result += char

    print(f'#{i} {result}')
