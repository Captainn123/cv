report={'water_ml':2000, 'milk_ml':500, 'coffee_g':300, 'money_usd':0}
refill={}
def check_resource(water, milk, coffee):
    if water<refill['water_ml']:
        if milk<refill['milk_ml']:
            if coffee<refill['coffee_g']:
                print("We have sufficient resources")
                # return True
                print(refill)
                play_machine()
            else:
                print("Coffee is not sufficient")
        else:
            print("Milk is not Sufficient")   
    else:
        print("Water is not sufficient")
refill=report.copy()

def a():
    global refill
    refill['water_ml'] -= 100
    refill['milk_ml'] -=50
    refill['coffee_g']-=30
    refill['money_usd'] +=2.50
    check_resource(100,50,30)
def b():
    global refill
    refill['water_ml'] -= 100
    refill['milk_ml'] -=50
    refill['coffee_g']-=30
    refill['money_usd'] +=2.50
    check_resource(100,50,30)
def c():
    global refill
    refill['water_ml'] -= 100
    refill['milk_ml'] -=50
    refill['coffee_g']-=30
    refill['money_usd'] +=2.50
    check_resource(100,50,30)
def play_machine():
    global refill
    value=int(input("What would you like?\n'1 for espresso'\n'2 for latte'\n'3 for cappuccino'\n'4 for Turn Off'\n'5 for Refill'\n"))
    if value==1:
        a()
    elif value==2:
        b()
    elif value==3:
        c()
    elif value==5:
        refill=report.copy()
        play_machine()
    else:
        print("Turn Off")
play_machine()
