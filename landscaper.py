
## Defining Game state
money = 0
tools = ["teeth", "Rusty Scissors", "Push Mower", "Fancy Mower", "Starving Students"]
winning_amount = 1000
current_tool = "teeth"


def mow():
    global money
    if current_tool =="teeth":
        money += 1
        print(money)                            # testing:

    elif current_tool=="Rusty Scissors":
        money += 5
        print(money)
        
    elif current_tool=="Push Mower":
        money += 50
        print(money)
        
    elif current_tool=="Fancy Mower":
        money += 100
        print(money)
        
    elif current_tool=="Starving Students":
       money += 250
       print(money)
        

def start_mowing():
    user_question = input("Do you want to Mow or buy. Enter 1 for Mow and 2 for Buy tools")
    if int(user_question)==1:
        return "mow"
    elif int(user_question)==2:
        return "buy"
    else:
        return "wrong input"

def upgrade_tools():
    global money
    global current_tool
    buying_new_tool = int(input("What tool do you want to buy, 1. Rusty Scissors, 2. Push Mower, 3. Fancy Mower, 4. Starving Students : "))

    
    if buying_new_tool == 1 and money >= 5:
        current_tool = "Rusty Scissors"

    elif buying_new_tool == 2 and money >= 25:
        current_tool = "Push Mower"
        #print("push mower is bought") #testing

    elif buying_new_tool == 3 and money >= 250:
        current_tool = "Fancy Mower"
        #print("Fancy Mower is bought") #testing

    elif buying_new_tool == 4 and money >= 500:
        current_tool = "Starving Students"
        print("Starving is bought") #testing
        



def user_choice(choice):
    if choice=="mow":
        mow()
    elif choice == "buy":
        upgrade_tools()


# start_mowing()
while money<1000:
    mowing_value=start_mowing()
    user_choice(mowing_value)
print("You won: 1000 dollars")