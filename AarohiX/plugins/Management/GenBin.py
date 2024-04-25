from pyrogram import Client, filters
import random
from AarohiX import app

VALID_PREFIXES = [4, 5, 6, 3]

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def generate_test_card_number(prefix, length):
    card_number = [random.randint(0, 9) for _ in range(length - len(str(prefix)) - 1)]
    card_number.insert(0, str(prefix))
    card_number = ''.join(map(str, card_number))
    checksum = luhn_checksum(int(card_number) * 10)
    return card_number + str((10 - checksum) % 10)

@app.on_message(filters.command("genbin"))
def generate(client, message):
    prefix = random.choice(VALID_PREFIXES)
    length = 6
    card_number = generate_test_card_number(prefix, length)
    message.reply_text(f"**BIN Successfully Generated**\n{card_number} ✅")
