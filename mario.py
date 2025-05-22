blocks_number = input("Please enter the number of blocks (1-8): ")

while not blocks_number.isdigit() or not (1 <= int(blocks_number) <= 8):
    blocks_number = input("Invalid input! Please enter a number between 1 and 8: ")

blocks_number = int(blocks_number)

for i in range(blocks_number):
    print(" " * (blocks_number - i - 1) + "#" * (i + 1))
