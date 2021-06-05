your_string=input("input your string\n")
words_list=your_string.split(' ')
num_of_words_dict={i:words_list.count(i) for i in words_list if i!=''}
print(num_of_words_dict)