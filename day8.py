class Animal:
    noise = "Grunt"
    size = "Large"
    color = "brown"
    hair = "covers body"

    def get_color(self, abc):
        return self.color + " " + abc

    def get_size(self):
        return self.size

    @property
    def make_noise(self):
        return self.noise


dog = Animal()
print(dog.get_color('abc'))
print(dog.make_noise)

email = 'hello@teamcfe.com'
to_list = ['abc@gmail.com']
from_list = ['another@gmail.com', 'hello@teamcfe.com']


def send_email(email_param=email, to_list_param=None, from_list_param=None):
    if from_list_param is None:
        from_list_param = from_list
    if to_list_param is None:
        to_list_param = to_list
    print(email_param)
    print(to_list_param)
    print(from_list_param)
    pass


send_email(email_param='chuong@gmail.com')

