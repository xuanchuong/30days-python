import datetime


class MessageUser:
    user_details = []
    messages = []
    base_message = """Hi {name}
    Thank you for the purchase on {date}.
    We hope you are excited about using it. Just as a
    reminder the purchase total was ${total}.
    Have a great one!
    
    Team CFE  
    """

    def add_user(self, name, amount):
        name = name[0].upper() + name[1:].lower()
        new_amount = '%.2f' % amount
        detail = {
            'name': name,
            'amount': new_amount
        }
        today = datetime.date.today()
        date_text = '{today.day}/{today.month}/{today.year}'.format(today=today)
        detail['date'] = date_text
        self.user_details.append(detail)

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.user_details:
                name = detail['name']
                date = detail['date']
                amount = detail['amount']
                message = self.base_message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(message)
            return self.messages
        else:
            return []

    def get_users(self):
        return self.user_details
