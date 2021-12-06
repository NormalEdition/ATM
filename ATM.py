import datetime
td = datetime.datetime.now()
time_date = td.strftime("%d-%m-%Y %H:%M:%S")  #To mention time and date in mini statement

def set_pin():
    check_pin = open("##LOCATION OF PIN.TXT FILE##","r")  #To check pin set or not
    ck_pin = check_pin.read()

    if ck_pin == "":
        set_pin = str(input("Enter your new pin number: "))
        strs = list(set_pin)
        for i in strs:
            if i in ["0","1","2","3","4","5","6","7","8","9"]:  #To allow only numerical characers
                character = 0
            else:
                character = 1
                break
                    
        if character == 1 or len(set_pin) > 4 or len(set_pin) < 4:
            print("Use 4 characters(0-9).")
                
        else:    
            c_pin = open("##LOCATION OF PIN.TXT FILE##","w")  #To write pin
            cw_pin = c_pin.write(set_pin)
            c_pin.close()
            print("Pin setup Successful.")

    else:
        print("You already set your PIN. \nIf you forgot your PIN contact our bank")
    

print("<------------Choose your Action-------------->")
initial_action = str(input("Do Transacstion........(1)\nSet PIN................(2)\n"))

if initial_action == "2":
    set_pin()

if initial_action == "1":
    pass
    
for i in range(4):
    remain = 3 - i  #To know remaining chance
    
    read_pin = open("##LOCATION OF PIN.TXT FILE##","r")  #To read pin
    pin = read_pin.read()

    read_balance = open("##LOCATION OF AMOUNT.TXT FILE##","r")  #To read balance
    account_balance = read_balance.read()
    account_balance = int(account_balance)

    read_old_pin = open("##LOCATION OF OLD_PIN.TXT FILE##","r")  #To read old pin
    old_pin = read_old_pin.read()

    if pin == "":
        print("You still not set your pin")  #To stop transaction before setting pin
        break

    else:
        print("<---------------PIN NUMBER--------------->")
        ip_pin = str(input("Enter your pin number: "))

            
#Deposit Function
    def deposit():
        deposit_amt = int(input("Depositing Amount: "))
        new_balance = account_balance + deposit_amt
        new_balance = str(new_balance)
        c_balance = open("##LOCATION OF AMOUNT.TXT FILE##","w")  #To write deposit ammount
        cw_balance = c_balance.write(new_balance)
        c_balance.close()
        print("Depositing of",deposit_amt,"is Successful. \nYour new balance:",new_balance,"\nPlease take your card")
        deposit_amt = str(deposit_amt)  #To write mini statement
        m_balance = open("##LOCATION OF MINI_STATE.TXT FILE##","a")
        ms_balance = m_balance.write(time_date)
        ms_balance = m_balance.write(" Deposit  ")
        ms_balance = m_balance.write(deposit_amt)
        ms_balance = m_balance.write("\n")
        m_balance.close()

        
#Withdraw Function
    def withdraw():
        withdraw_amt = int(input("Withdraw Amount: "))
        valid_amt = withdraw_amt
        initial = 0
        for i in range(2):  #To check if the given ammount is whole or not
            remainder = valid_amt%10
            initial = initial + remainder
            valid_amt = valid_amt//10
        if withdraw_amt < 99 or withdraw_amt > 10000 or initial != 0:
                print("You would have entered either below 100 or above 10,000 \nor the digit entered may not be whole amount or\nInsufficient Balance.")
        else:
            new_balance = account_balance - withdraw_amt
            new_balance = str(new_balance)
            if withdraw_amt < account_balance:
                c_balance = open("##LOCATION OF AMOUNT.TXT FILE##","w")  #To write withdraw ammount
                cw_balance = c_balance.write(new_balance)
                c_balance.close()
                print("Withdraw Successful. \nPlease take your cash:",withdraw_amt,"\nYour new balance:",new_balance,"\nPlease take your card")
                withdraw_amt = str(withdraw_amt)  #To write mini statement
                m_balance = open("##LOCATION OF MINI_STATE.TXT FILE##","a")
                ms_balance = m_balance.write(time_date)
                ms_balance = m_balance.write(" Withdraw ")
                ms_balance = m_balance.write(withdraw_amt)
                ms_balance = m_balance.write("\n")
                m_balance.close()
            else:
                print("Insufficient Balance.")


#Mini Statement
    def mini_state():
        ms = open('##LOCATION OF MINI_STATE.TXT FILE##', 'r')  #To show mini statement
        mini = ms.readlines()  #To read line by line
        mini = mini[-10:]  #To select last lines
        mini.reverse()  #To reverse readed line
        for i in mini:
            print(i)  #To print lines
        ms.close()
        
                
#Change pin Function
    def change_pin():
        new_pin = str(input("Enter your new pin number: "))
        if ip_pin == new_pin:
            print("Your new pin is similar to the old one.\nSo try a diffrent pin.")  #To avoid similar pins
        else:
            strs = list(new_pin)
            for i in strs:
                if i in ["0","1","2","3","4","5","6","7","8","9"]:  #To allow only numerical characers
                    character = 0
                else:
                    character = 1
                    break
                    
            if character == 1 or len(new_pin) > 4 or len(new_pin) < 4:
                print("Use 4 characters(0-9).")
                
            else:
                old_pin = open("##LOCATION OF OLD_PIN.TXT FILE##","w")  #To write old pin
                cw_old_pin = old_pin.write(ip_pin)
                old_pin.close()
            
                c_pin = open("##LOCATION OF PIN.TXT FILE##","w")  #To write new pin
                cw_pin = c_pin.write(new_pin)
                c_pin.close()
                print("Pin change Successful.")
        
#Action decider
    if pin == "ACCOUNT  BLOCKED":
        print("\n**********ACCOUNT  BLOCKED DUE TO MULTIPLE INVAILD PIN********** \nContact our bank for further details.")
        break
        
    elif pin == ip_pin:
        print("<------------Choose your Action-------------->")
        
        action = str(input("Deposit................(1)\nWithdraw...............(2)\nCheck balance..........(3)\nMini Statement.........(4)\nChange pin.............(5)\nCancel Transaction.....(6)\n"))

        if action == '1':
            deposit()
            break
    
        elif action == '2':
            withdraw()
            break

        elif action == '3':
            print("Your Account balance:",account_balance)
            break

        elif action == '4':
            mini_state()
            break
    
        elif action == '5':
            change_pin()
            break

        elif action == '6':
            print("Transaction Canceled")
            break
    
        else :
            print("Invalid input \nChoose from the above list.")
            break
            
    elif ip_pin == old_pin:
        print("You Enter your old pin. Try with new one. \nYou have still",remain,"more chance(s).") #To say that you entered your old pin
            
    elif i != 3:
        print("Incorrect pin number. \nYou have still",remain,"more chance(s).")  #To say your remaining chance
    else:
        print("\n**********ACCOUNT  BLOCKED********** \nContact our bank for further details.")
        
        block_acc = open("##LOCATION OF PIN.TXT FILE##","w")  #To block account permanently
        w_block = block_acc.write("ACCOUNT  BLOCKED")
        block_acc.close()
        break
    
