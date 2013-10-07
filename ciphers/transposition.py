def main():
    #global ciphertext
    myMessage = 'This is my message to you-ou-ou.'
    myKey = 8

    cip = encryptMessage(myKey, myMessage)
    print (ciphertext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
            

    return ''.join(ciphertext)

#if __name__ == "__main__":
#    main()
