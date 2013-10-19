def main():
    #global ciphertext
    myMessage = ' Message-govnessage'
    myKey = 5

    ciphertext = encryptMessage(myKey, myMessage)
    print (ciphertext + '|')

def encryptMessage(key, message):
    #global ciphertext
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
            

    return ''.join(ciphertext)

if __name__ == "__main__":
    main()
