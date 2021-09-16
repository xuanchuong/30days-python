from argparse import ArgumentParser
from user_class import UserManager

parser = ArgumentParser(prog='hungry')
parser.add_argument('type', type=str, choices=['view', 'message'])
parser.add_argument('-id', '--user_id', type=int)
parser.add_argument('-e', '--email', type=str)

args = parser.parse_args()

if args.type == 'view':
    print(UserManager().get_user_data(user_id=args.user_id, user_email=args.email))
elif args.type == 'message':
    print(UserManager().message_user(user_id=args.user_id, user_email=args.email))