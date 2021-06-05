
def main():
    while True:
        a = input("введите текст\n")
        if len(a) < 2:
            print("try to write longer word")
        else:
            cens(a)
            symb_num(a)
            words_repeat_num(a)
            words_num(a)
            sentence_num(a)
            break
def symb_num(a):
    list_sym=' '.join(','.join(a.split('.')).split(',')).split(' ')
    endlist=[]
    for i in list_sym:
        if i != " ":
            endlist.append(i)
    num_of_sym=len(''.join(endlist))
    print(f"you entered {str(num_of_sym)} characters")

def words_repeat_num(a):
    words_list = ' '.join(','.join(a.split('.')).split(',')).split(' ')
    num_of_words_dict = {i: words_list.count(i) for i in words_list if i != ''}
    max_value=max(num_of_words_dict.values())
    for key, value in num_of_words_dict.items():
        if value == max_value:
            print("most repeated word is", key)
    print("word: repeat times :",num_of_words_dict)

def words_num (a):
    words = ' '.join(','.join(a.split('.')).split(',')).split(' ')
    result=[]
    for i in words:
        if i.isalpha():
            result.append(i)
    print(f"you had write {len(result)} words")

def sentence_num(a):
    sentences=a.split(".")
    result=[]
    for i in sentences:
        if len(i)>2:
            result.append(i)
    print(f"you had write {len(result)} sentences")

def cens(a):
    words = ' '.join(','.join(a.split('.')).split(',')).split(' ')
    for i in words:
        if str(i).lower() == "shag":
            print(f"plz dont write this dirty word '{i}'")







if __name__ == "__main__":
    main()