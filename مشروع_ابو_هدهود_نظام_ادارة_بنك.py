import os
class client:
    def __init__(self,account,pin,name,phone,balance):
        self.account=account
        self.pin=pin
        self.name=name
        self.phone=phone
        self.balance=balance
    
clients=[]

def clear_screen():
        os.system('cls')

def add():
    clear_screen()
    print('='*80)
    print(f' add screen   '.center(80,'='))
    print('='*80)
    account=input('enter account number>>')
    pin=input('enter pin code>>')
    name=input('enter client name >>')
    phone=input('enter phone number >>')
    balance=input('enter client alance >>')
    client1=client(account,pin,name,phone,balance)
    clients.append(client1)
    input('added successfuly \n press enter to continue ...')

def show():
    clear_screen()
    if len(clients)==0:
        input('not found any clients press enter to continue...')
    elif len(clients)>0:
        print('='*80)
        print(f' show screen ({len(clients)}) clients exsists '.center(80,'='))
        print('='*80)
        print('-'*120)
        print('|','account '.ljust(15),'|','pin code'.ljust(15),'|','name'.ljust(40),'|','phone'.ljust(15),'|','balance'.ljust(15),'|')
        print('-'*120)
        for i in range(0,len(clients)):
            print('|',clients[i].account.ljust(15),'|',clients[i].pin.ljust(15),'|',clients[i].name.ljust(40),'|',end='')
            print(clients[i].phone.ljust(15)," |",clients[i].balance.ljust(15),'|')
            print()
        print('-'*120)
        input('press enter to continue ...')

def delete():
    clear_screen()
    print('='*80)
    print(f' delete screen   '.center(80,'='))
    print('='*80)
    account=input('enter the account number to delete >> ')
    check=True
    for i in range(0,len(clients)):
            if account==clients[i].account:
                check=False
                print('-'*120)
                print(f'account number :{clients[i].account}\n pin code :{clients[i].pin}\nName : {clients[i].name}')
                print(f'phone : {clients[i].phone} \nbalance : {clients[i].balance}')
                print('-'*120)
                clients.pop(i)
                print('this client was deleted successfully ')
                input('press enter to continue ...')
    if check:
        input('this client not found \npress enter to continue ...')

def update():
    clear_screen()
    print('='*80)
    print(f' update screen   '.center(80,'='))
    print('='*80)
    account=input('enter the account number to update >> ')
    check=True
    for i in range(0,len(clients)):
            if account==clients[i].account:
                check=False
                print('-'*120)
                print(f'account number :{clients[i].account}\n pin code :{clients[i].pin}\nName : {clients[i].name}')
                print(f'phone : {clients[i].phone} \nbalance : {clients[i].balance}')
                print('-'*120)
                clients.pop(i)
                account=input('enter new account number>>')
                pin=input('enter new pin code>>')
                name=input('enter new client name >>')
                phone=input('enter new phone number >>')
                balance=input('enter new client alance >>')
                client1=client(account,pin,name,phone,balance)
                clients.insert(i,client1)
                input('updated successfuly \n press enter to continue ...')
    if check:
        input('this client not found \npress enter to continue ...')

def find():
    clear_screen()
    print('='*80)
    print(f' find screen   '.center(80,'='))
    print('='*80)
    account=input('enter the account number to find  >> ')
    check=True
    for i in range(0,len(clients)):
            if account==clients[i].account:
                check=False
                print('-'*120)
                print(f'account number :{clients[i].account}\n pin code :{clients[i].pin}\nName : {clients[i].name}')
                print(f'phone : {clients[i].phone} \nbalance : {clients[i].balance}')
                print('-'*120)
                input(' press enter to continue ...')
    if check:
        input('this client not found \npress enter to continue ...')


def main():
    while True:
        clear_screen()
        print()
        print('='*80)
        print(f'  main menue... '.center(80,'='))
        print('='*80)
        print(' '*5,"[1]show clients ")
        print(' '*5,"[2]add  client ")
        print(' '*5,"[3]delete  client ")
        print(' '*5,"[4]update client ")
        print(' '*5,"[5]find client ")
        print(' '*5,"[6]exsit ")
        print('='*80)
        choice=int(input('enter your choice >>'))
        if choice==1:
            show()
        elif choice==2:
            add()
        elif choice==3:
            delete()
        elif choice==4:
            update()
        elif choice==5:
            find()
        elif choice==6:
            input('exsit...\npress enter to continue..')
            break
        else:
            input('warnning choice please try again\npress enter to continue ')
main()