# 6.6 superによる親への支援要請
import chapter6_2


class EmailPerson(chapter6_2.Person):
    def __init__(self, name, email):
        # super()を使って、親クラスの定義を取り出す。
        super().__init__(name)
        self.email = email


email_person = EmailPerson('Bob', 'Bob@Bob.com')
print(email_person.name)
print(email_person.email)
