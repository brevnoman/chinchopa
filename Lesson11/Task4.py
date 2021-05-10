class CustomException:

    def __init__(self, msg):
        self.msg=msg

    def Type(self):
        print(self.msg)

    def Index(self):
        print(self.msg)

def main():
    try:
        y=[1, "a"]
        b=y[1]+y[0]
        c=y[0]-y[3]
    except (TypeError, IndexError) as error:
        if error is TypeError:
            msg=CustomException("Baka, i will not combine strings with nums!!!")
            msg.Type()
        else:
            msg=CustomException("Oni-chan your index is too big for me...")
            msg.Index()

main()
