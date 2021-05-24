from validate_email import validate_email
class DavayPoNovoy(Exception):
    def __init__(self, msg):
        self.msg = msg

    @classmethod
    def incorrect_email(cls):
        return cls("Ne katit takoe")


class Email:

    def __init__(self, email):
        self.email = self.validate(email)

    @classmethod
    def validate(cls, email):
        if not validate_email(email):
            raise DavayPoNovoy.incorrect_email()
        else:
            return email

    def __str__(self):
        return f"vashe milo {self.email}"


gmail = Email("Hm_Khm_Eeem_Nu_Ladno_Poka@gmail.com")
print(str(gmail))
print(str(Email("sosochka-devochka@buket.tebe")))
