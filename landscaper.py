
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
        
    # elif tools=="Push Mower":
    #     money += 50
        
    # elif tools=="Fancy Mower":
    #     money += 100
        
    # elif tools=="Starving Students":
    #     money += 250
        

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
    list_of_tools=["Rusty Scissors", "Push Mower", "Fancy Mower", "Starving Students"]
    # if list_of_tools[0]:
    #     money-=5
    
    if buying_new_tool == 1 and money >= 5:
        current_tool = "Rusty Scissors"

    elif buying_new_tool == 2 and money >= 25:
        current_tool = "Push Mower"
        #print("push mower is bought") #testing
        
    # if buying_new_tool == "Rusty Scissors":
    #     money -= 5
    # elif buying_new_tool == "Push Mower":
    #     money -= 50
    # elif buying_new_tool == "Fancy Mower":
    #     money -= 100
    # elif buying_new_tool == "Starving Students":
    #     money -= 250
    # else:
    #     "invalid Input"


def user_choice(choice):
    if choice=="mow":
        mow()
    elif choice == "buy":
        upgrade_tools()


# start_mowing()
while money<1000:
    mowing_value=start_mowing()
    user_choice(mowing_value)
   ## upgrade_tools()