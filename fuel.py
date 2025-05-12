def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        num, denom = fraction.split("/")
        x = int(num)
        y = int(denom)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        return round((x / y) * 100)
    except ValueError:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
