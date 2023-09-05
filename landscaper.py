
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

    # elif current_tool=="Rusty Scissors":
    #     money += 5
    #     print(money)
        
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
    

def user_choice(choice):
    if choice=="mow":
        mow()


# start_mowing()
while money<1000:
    mowing_value=start_mowing()
    user_choice(mowing_value)