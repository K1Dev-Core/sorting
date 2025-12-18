def fac(n):
    if n == 0:
        print(f"fac({n}) returns 1")  
        return 1
    else:
        result = n * fac(n - 1)
        print(f"fac({n}) returns {result}")  
        return result


if __name__ == "__main__":
    n = 10
    print(f"{n}!={fac(n)}")

