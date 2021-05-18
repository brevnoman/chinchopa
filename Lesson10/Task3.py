class Controller:
    channel_list = ["BBC", "Discovery", "TV1000", "2x2", "QTV"]

    def __init__(self, channel):
        self.channel = channel

    def first_channel(self):  # при нажатии "first"
        self.channel = self.channel_list[0]

    def last_channel(self):  # najat' na "last"
        self.channel = self.channel_list[-1]

    def turn_channel(self, choose):  # число в len(channel_list)
        try:
            if int(choose) in range(1, len(self.channel_list)+1):
                self.channel = self.channel_list[int(choose) - 1]
            else:
                i = []
                print(i[2])
        except IndexError:
            print(f"your choose is out of range from 1 to {len(self.channel_list)}")

    def next_channel(self):  # channel+=1   pri >
        if self.channel != self.channel_list[-1]:
            for i in self.channel_list:
                if self.channel == i:
                    self.channel = self.channel_list[self.channel_list.index(self.channel)]
                    break
        elif self.channel == self.channel_list[-1]:
            self.channel = self.channel_list[0]

    def previous_channel(self):  # pri <
        if self.channel != self.channel_list[0]:
            for i in self.channel_list:
                if self.channel == i:
                    self.channel = self.channel_list[self.channel_list.index(self.channel)]
        elif self.channel == self.channel_list[0]:
            self.channel = self.channel_list[-1]

    def current_channel(self):  # pri !
        print(self.channel, self.channel_list.index(self.channel)+1, "in list")

    @staticmethod
    def is_exist(i):  # pri ?
        if i.isdecimal():
            if int(i) in range(1, len(Controller.channel_list)+1):
                print(f"yes you can choose this channel, this is {Controller.channel_list[int(i) - 1]}")
        elif i.isalpha():
            if i in Controller.channel_list:
                print(f"yes you can choose this channel it's num is {Controller.channel_list.index(i.channel)}")

        else:
            print("there is no channel like this")


def main():
    controller = Controller(Controller.channel_list[0])
    print(f"Use nums from 1 to {len(Controller.channel_list)} to choose channel\nPrint 'first' to choose first channel\nPrint 'last' to choose last channel\n> for nex channel\n< for previous channel\n ! to know current channel\nand ? to know is channel exist")
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
