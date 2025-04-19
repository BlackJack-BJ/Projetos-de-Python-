print("\033[1;36m")
print(f"{'Добро пожаловать от Lazy calc 2.0':-^70}\n")
while True:
    try:
        exp = input("\033[1;34m❯ EXPRESSION: ")
        ans = eval(exp)
        print(f"\033[1;33m❯ ANS: {ans}\n")

    except (ValueError, SyntaxError):
        print("\033[1;31mInvalyd Syntax!")

    except KeyboardInterrupt:
        print("\033[1;35m", end = "")
        print(f"{'Давай!':-^70}")
        break
