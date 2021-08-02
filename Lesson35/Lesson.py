# def date_time(time: str) -> str:
#     new_time = " ".join(time.split(".")).split(" ")
#     result = ""
#     month = ["January",
#              "February",
#              "March",
#              "April",
#              "May",
#              "June",
#              "July",
#              "August",
#              "September",
#              "October",
#              "November",
#              "December"]
#     counter = 0
#     for i in new_time:
#         if counter == 0:
#             result += str(int(i)) + " "
#             counter += 1
#         elif counter == 1:
#             try:
#                 result += month[int(i)-1] + " "
#                 counter += 1
#             except IndexError:
#                 print("no such month")
#         elif counter == 2:
#             result += str(int(i)) + " year "
#             counter += 1
#         elif counter == 3:
#             if str(int(i[:2])) != "1":
#                 result += str(int(i[:2])) + " hours "
#             else:
#                 result += str(int(i[:2])) + " hour "
#             if str(int(i[3:])) != "1":
#                 result += str(int(i[3:])) + " minutes"
#             else:
#                 result += str(int(i[3:])) + " minute"
#     return result
#
# print(date_time("01.01.2000 00:00"))  #"1 January 2000 year 0 hours 0 minutes"

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code:str):
    result = ""
    code_list = code.split(" ")
    flag = True
    for i in code_list:
        if flag:
            if i in MORSE.keys():
                result += MORSE[i].upper()
            else:
                result += i
            flag = False
        else:
            if i in MORSE:
                result += MORSE[i]
            else:
                if result[-1] != " ":
                    result += " "
    return result

print(morse_decoder("... --- -- .   - . -..- -"))