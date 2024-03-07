def bin_to_dec(binary_no):
    dec = 0
    b = str(binary_no)
    for val in b:
        if int(val) > 1:
            return "Invalid Binary Digit!"
    h_index = len(b) - 1

    for char in b:
        dec += int(char) * (2 ** h_index)
        h_index -= 1

    return dec


def dec_to_bin(dec):
    b = dec
    remainders = []
    while b != 0:
        remainders.append(b % 2)
        b = b // 2
    remainders = remainders[::-1]
    binary = int("".join(map(str, remainders)))

    return binary


def main():
    print("""
    A program that converts Binary to Denary and vice-versa
    Input your base number!
    """)

    number = 0
    base = ""

    while number < 1:
        try:
            number = int(input("Input the number to convert: "))
        except ValueError:
            print("Number cannot be a non-digit!")

        if number < 1:
            print("Input a valid number!")
        else:
            break

    while base != "bin" and base != "dec":
        base = input("To what base? (bin/dec): ").lower()

        if base != "bin" and base != "dec":
            print("Input has to be either of 'bin' or 'dec'!")

    if base == 'bin':
        result = dec_to_bin(number)
    elif base == 'dec':
        result = bin_to_dec(number)

    return f"{number} in {base}: {result}"


if __name__ == "__main__":
    print(main())


