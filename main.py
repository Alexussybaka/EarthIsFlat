def earth(x):
    if abs(x) <= 6371:
        return (6371**2 + x**2)**(1/2)
    else:
        return 0

def calculate_delta_y(position):
    return earth(position) - earth(0)

def format_answer(answer):
    suffix = "km"
    multiplier = 1

    if answer < 1:
        suffix = "m"
        multiplier = 1000
    if answer < 0.1:
        suffix = "cm"
        multiplier = 100000

    return f"{round(answer * multiplier, 2)} {suffix}"

def main():
    print("EARTH IS NOT FLAT\n")
    print("Use this console app to calculate how much things are below your ground level.")
    while True:
        print("You stay on a top of the Earth, select the position you want to check:")
        position = input(" : ")

        if not position.isdigit():
            break

        print(f"\nThe position which is {format_answer(abs(int(position)))} afar is {format_answer(abs(calculate_delta_y(int(position))))} below you!\n")
    print("Thank you for using EARTH IS NOT FLAT")

if __name__ == '__main__':
    main()
