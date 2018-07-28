import sys


def main():
    digit_string = sys.argv[1]
    sum = 0

    for digit in digit_string:
        sum += int(digit)

    print(sum)


if __name__ == '__main__':
    main()