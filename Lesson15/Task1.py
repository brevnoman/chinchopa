class DavayPoNovoy(Exception):
    def __init__(self, msg):
        self.msg = msg

    @classmethod
    def incorrect_email(cls):
        return cls("Ne katit takoe")


class Email:
    attributes = ["@", "gmail.com"]

    def __init__(self, email):
        self.email = self.validate(email)

    @classmethod
    def validate(cls, email):
        for i in cls.attributes:
            if i not in email:
                raise DavayPoNovoy.incorrect_email()
        return email

    def __str__(self):
        return f"vashe milo {self.email}"


gmail = Email("Hm_Khm_Eeem_Nu_Ladno_Poka@gmail.com")
print(str(gmail))
print(str(Email("sosochka-devochka@buket.tebe")))
