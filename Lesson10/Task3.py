class Controller:
    def __init__(self, channel):
        self.channel = channel

    def first_channel(self):  # при нажатии "first"
        self.channel = channel_list[0]

    def last_channel(self):  # najat' na "last"
        self.channel = channel_list[-1]

    def turn_channel(self, choose):  # число в len(channel_list)
        if int(choose) in range(len(channel_list) + 1):
            self.channel = channel_list[int(choose) - 1]
        else:
            print(f"your choose is out of range from 1 to {len(channel_list)}")
            main()

    def next_channel(self):  # channel+=1   pri >
        if self.channel != channel_list[-1]:
            counter = 0
            for i in channel_list:
                counter += 1
                if self.channel == i:
                    self.channel = channel_list[counter]
                    break
        elif self.channel == channel_list[-1]:
            self.channel = channel_list[0]
        else:
            main()

    def previous_channel(self):  # pri <
        if self.channel != channel_list[0]:
            counter = -2
            for i in channel_list:
                counter += 1
                if self.channel == i:
                    self.channel = channel_list[counter]
        elif self.channel == channel_list[0]:
            self.channel = channel_list[-1]

    def current_channel(self):  # pri !
        print(self.channel, channel_list.index(self.channel)+1, "in list")

    @staticmethod
    def is_exist(i):  # pri ?
        if i.isdecimal():
            if int(i) in range(len(channel_list)+1):
                print(f"yes you can choose this channel, this is {channel_list[int(i) - 1]}")
        elif i.isalpha():
            counter = 0
            for j in channel_list:
                counter += 1
                if i == j:
                    print(f"yes you can choose this channel it's num is {counter}")
        else:
            print("there is no channel like this")


def main():
    global channel_list
    channel_list = ["BBC", "Discovery", "TV1000", "2x2", "QTV"]
    controller = Controller(channel_list[0])
    print(f"Use nums from 1 to {len(channel_list)} to choose channel\nPrint 'first' to choose first channel\nPrint 'last' to choose last channel\n> for nex channel\n< for previous channel\n ! to know current channel\nand ? to know is channel exist")
    while True:
        print(controller.__dict__)
        choose = input("\n")
        if choose == "first":
            controller.first_channel()
        elif choose == "last":
            controller.last_channel()
        elif choose.isdecimal():
            controller.turn_channel(choose)
        elif choose == "<":
            controller.previous_channel()
        elif choose == ">":
            controller.next_channel()
        elif choose == "!":
            controller.current_channel()
        elif choose == "?":
            i = input("write name or num of channel")
            Controller.is_exist(i)
        elif choose == "exit":
            break
        else:
            print("tyr something else")


main()
