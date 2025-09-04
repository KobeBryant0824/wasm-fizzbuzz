def fizzbuzz(n: int) -> str:
    out = ""
    if n % 3 == 0: out += "Fizz"
    if n % 5 == 0: out += "Buzz"
    return out or str(n)

if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
