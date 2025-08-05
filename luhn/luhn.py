def is_luhn(number) -> bool:
    """Validate a numeric string using the Luhn Algorithm"""
    
    # Sanitize non digit input
    if not number.isdigit():
        return False

    # Reverse the number and convert each character into integer
    digit = [
            int(num) for num in number[::-1]
            ]

    # Double every second digit (odd indices in the reversed number)
    double = [(num * 2 if idx % 2 == 1 else num) for idx, num in enumerate(digit)]

    # Substract by 9 for any doubled > 9
    result = [(num - 9 if num > 9 else num) for num in double]

    # Return True fof the summary proceed is a multiple of 10
    return sum(result) % 10 == 0

def main():
    """CLI entry point for the luhn-validator script."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: luhn-validator <number>")
        sys.exit(1)

    number = sys.argv[1]
    if is_luhn(number):
        print(f"{number} is a VALID number!")
    else:
        print(f"{number} is an INVALID number.")
