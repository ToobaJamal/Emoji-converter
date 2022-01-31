def emoji_conv(message):
    words = message.split(" ")
    emojis = {':)': '🙂',
             ':(': '😔',
             '<3': '❤️'}
    output = ""
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_conv(message))
