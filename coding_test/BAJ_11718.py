while True:
    try:
        a=str(input())
        # 맞긴 맞았는데 a=input()이렇게 해도 됌.
        print(a)
    except EOFError:
        break

# cf1
# import sys
# print(sys.stdin.read())

# cf2
# print(open(0).read())