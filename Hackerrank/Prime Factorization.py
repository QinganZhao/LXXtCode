import sys

def find_prime(args):
    for num in args:
        dic, ans, factors = {}, "", []
        try:
            int(num)
        except ValueError:
            print(f"{num} skip invalid request")
            continue
        if int(num) != float(num) or int(num) in [-1, 0, 1]:
            print(f"{num} skip invalid request")
        else:
            n = abs(int(num))
            i = 2
            while i * i <= n:
                while n % i == 0:
                    factors.append(i)
                    n //= i
                i += 1
            if n > 1:
                factors.append(n)
            for factor in factors:
                dic[factor] = dic.get(factor, 0) + 1
            for factor, cnt in dic.items():
                ans += f"({factor} ** {cnt})"
            if int(num) > 0:
                print(f"{num} = {ans}")
            else:
                print(f"{num} = -{ans}")
if __name__ == "__main__":
    find_prime(sys.argv[1:])
