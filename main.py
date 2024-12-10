#morse code dictionary 

morse_code = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",

    ".-.-.-": ".",  # Period
    "--..--": ",",  # Comma
    "..--..": "?",  # Question mark
    "-.-.--": "!",  # Exclamation mark
    "-....-": "-",  # Hyphen
    ".----.": "'",  # Apostrophe
    "-..-.": "/",   # Slash
    "-.-.-.": ";",  # Semicolon
    ".-..-.": "\"",  # Quotation mark
    ".-.-.": "+",   # Plus
    "-...-": "=",   # Equal sign
    ".--.-.": "@",  # At symbol

    "": " " # A space
}

user_mode = input("Choose a mode. 1 for Morse code -> English; 2 for English -> Morse code.\n>>> ")

mode = ""

if int(user_mode) == 1:
    mode = "mte"
elif int(user_mode) == 2:
    mode = "etm"
else:
    print("Invalid input. Try again.")
    exit()


user_input = input("Enter you input. In case of morse code, use / to seperate letters\n>>> ")

list_raw = list()

list_temp_storage = []


def morse_code_to_english():
    list_raw = user_input.split("/")
    try:

        for i in list_raw:
            list_temp_storage.append(morse_code[i])

    except Exception as e:
        print("Opps, someting broke.", e)
        list_temp_storage.append("0")
    finally:
        return "".join(list_temp_storage)


def english_to_morse_code():
    list_raw = user_input.split(" ")
    list_raw_formatted = list(filter(None, list_raw))


    try:
        for i in list_raw_formatted:
            for a in range(len(i)):
                value_to_find = i[a] #value -> english
                for key, value in morse_code.items():
                    if value_to_find.upper() == value:
                        list_temp_storage.append(key)
                        if a == len(i)-1:
                            list_temp_storage.append("//")
                        else:
                            list_temp_storage.append("/")
                        break

    except Exception as e:
        print("Oops, something broke", e)
        list_temp_storage.append("0")
    finally:
        return "".join(list_temp_storage)




if mode == "mte":
    result_english = morse_code_to_english()
    print(result_english)
elif mode == "etm":
    result_morse = english_to_morse_code()
    print(result_morse)
