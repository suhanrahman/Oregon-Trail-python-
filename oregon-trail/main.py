
import random
# this help's me write text slowly
import time
import sys

#colors for the text
class bcolors:
    Green = '\033[92m' #GREEN
    Yellow = '\033[93m' #YELLOW
    Red = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    bold = '\033[1m' #bold
    underline = '\033[4m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan= '\033[36m'


#got this from the DO NOW
welcome_text = """
Welcome to the Oregon Trail! The year is 1850 and Americans are headed out West to populate the frontier. Your goal is to travel by wagon train from New York, NY to Oregon (2000 miles). You start
on March 1st, and your goal is to reach Oregon by December 31st.
The trail is arduous. Each day costs you food and health. You can hunt and rest, but you have to get there before winter!
"""
#this function is what writes txt slow
for i in welcome_text:
 sys.stdout.write(i)
 sys.stdout.flush()
 time.sleep(0.1)


help_text = (bcolors.bold+"""


 gameplay functions:                                                            
 t or travel to travel                                                            
 r or rest to rest                                                                 
 h or hunt to hunt                                                             
 e or eat to eat (don't need)                      
  
  You can also use:                                                           
 s or status for status about your health, travel distance, and other useful stuff  

 ? or help to open up this manue again 

 c or credits for credits

 q or quit to end this game!
 ________________________________


  
"""+ bcolors.RESET)

#this function is what writes txt slow
for i in help_text:
 sys.stdout.write(i)
 sys.stdout.flush()
 time.sleep(0.03)

good_luck_text = "Good luck, and see you in Oregon!"






# global veriables
miles_traveled = 0
food_remaining = 500
health_level = 5
month = 3
day = 1
sicknesses_this_month = 0
player_name = None
Difficulty= None
sick=2
random_events=2
#Constants>>>>>>>>>>>>>>>>>>>>>>>

max_food=500
FOOD_EATEN_PER_DAY = 5
MILES_BETWEEN_NYC_AND_OREGON = 2000
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]
MONTHS_WITH_28_DAYS = [2]

NAME_OF_MONTH = [
    'none', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December'
]


#random event lists

random_obby=[" crossed a river", " climed a big mountent"," crossed a muddy puddle"]


#here we start our functions>>>>>>>

#prints dates
def date_as_string(m, d):
 print ("today is "+ NAME_OF_MONTH[m] + " " + str(d) )

def miles_remaining():
  global miles_traveled,player_name,MILES_BETWEEN_NYC_AND_OREGON
  print (bcolors.cyan +str(player_name)+ " have " + str(MILES_BETWEEN_NYC_AND_OREGON - miles_traveled) + " miles left." + bcolors.RESET)

#return integer of days and monts
def add_days(m):  
 if m in MONTHS_WITH_31_DAYS:
   return 31
 
 elif m in MONTHS_WITH_30_DAYS:
   return 30
 
 elif m in MONTHS_WITH_28_DAYS:
   return 28



#sickness function
def random_sickness_occurs():
 global day, month,sick, health_level,sicknesses_this_month
 days_remainin_in_month = add_days(month) - day
 random_day = random.randint(0,days_remainin_in_month)
 if random_day <= sick:
    sick -=1
    print (player_name + " got sick")
    health_level -= 1
    sicknesses_this_month +=1



#random events function
def random_eventts():
 global day,month,random_events,health_level,food_remaining,player_name
 random_events_in_month=add_days(month) - day
 random_stuff=random.randint(0,random_events_in_month)
 if random_stuff <= random_events:
    random_events -=1
    z=random.randint(0,1)
    y=random.randint(1,10)
    day_took= random.randint (1,10)
    x=random.choice (random_obby)
    print (player_name + str(x)+" in "+str(day_took) + " days")
    day+= day_took
    health_level -= z
    food_remaining -=y *5

    




#makes the mont more robust
def fixed_month():
 global day,month,sick
 if day > add_days(month):
    day -= add_days(month)
    month += 1
    sick = 2




# game events>>>>
#travel function
def travel():
 global day, miles_traveled, food_remaining, player_name,FOOD_EATEN_PER_DAY
 distance_traveled= random.randint(30,60)
 days_traveled= random.randint (3,7)
 print ( player_name+ " have traveled " + str(distance_traveled)+ " miles in " + str(days_traveled)+ " days")
 day += days_traveled
 miles_traveled += distance_traveled
 food_remaining -= days_traveled *FOOD_EATEN_PER_DAY
 fixed_month()
 random_sickness_occurs()
 random_eventts()

#rest function
def rest():
 global day,health_level,food_remaining, player_name,FOOD_EATEN_PER_DAY
 days_rested = random.randint(2,5)
 print (player_name + " have reasted for "+ str(days_rested)+ " days.")
 day += days_rested
 health_level += 1
 food_remaining -= days_rested *FOOD_EATEN_PER_DAY-4
 fixed_month()
 random_sickness_occurs()
 
 
#hunt function
def hunt():
 global day, food_remaining, player_name,FOOD_EATEN_PER_DAY,max_food
 if food_remaining > max_food:
   print ("Your bag is full!")
 else:
 
   days_hinted= random.randint(2,5)
   print (player_name + " have hunted for "+str(days_hinted))
   day += days_hinted
   food_remaining += 100
   food_remaining -= days_hinted *FOOD_EATEN_PER_DAY+30
   fixed_month()
   random_sickness_occurs()
   random_eventts()
   
#status function
def status():
 global player_name,day,health_level,sicknesses_this_month
 date_as_string(month, day)
 miles_remaining()
 print (bcolors.blue +str(player_name) + " have " + str(health_level)+ " health left"+ bcolors.RESET)
 print (bcolors.blue +"and " +str(food_remaining)+ " food remaining"+ bcolors.RESET)
 print (bcolors.purple +player_name+" suffered "+str(sicknesses_this_month)+ " sickness!"+ bcolors.RESET)

#help function
def help():
 for i in help_text:
   sys.stdout.write(i)
   sys.stdout.flush()
   time.sleep(0.03)
 print (help_text) 
 
#eat function
def eat():
  global food_remaining,health_level
  if food_remaining ==0:
    print ("you don't have any food left.")
  food_remaining -= 100
  health_level += 1
  print ("finaly, I eat something")

  
  
#quit function
def quit():
	global playing
	playing = False




#Game States>>>>>>
#gameover function
def game_over():
  global MILES_BETWEEN_NYC_AND_OREGON
  if health_level == 0:
    return True
  elif food_remaining <= 0:
    return True
  elif miles_traveled >= MILES_BETWEEN_NYC_AND_OREGON:
    return True


#credits
def credits():
  print (bcolors.underline +"\nThis game was made by Nihadur R Suhan."+ bcolors.RESET)


#player wins function
def player_wins():
 global MILES_BETWEEN_NYC_AND_OREGON
 if miles_traveled >= MILES_BETWEEN_NYC_AND_OREGON:
   return True

#tells the report after player lose
def loss_report():
 global player_name, miles_traveled,month,day
 print (bcolors.Yellow +str(player_name) + " traveled " + str(miles_traveled) + " Miles in " + str(month) + " Month and " + str(day)+" days"+ bcolors.RESET)

print(welcome_text + help_text + good_luck_text)

#name
player_name = input("\nWhat is your character's name? ")

#Difficulty function
Difficulty = input ("\nchoose the Difficulty: \n 1 = easy\n 2 = medium\n 3 = hard\n == ")

if Difficulty == "1" or Difficulty == "easy":
 food_remaining = 1000
 health_level = 10
 max_food=1000
 print(bcolors.Green +"\nYou are playing on easy mode!\n"+ bcolors.RESET)
 
elif Difficulty == "2" or Difficulty == "medium":
  print (bcolors.Yellow +"\nYou are playing on medium mode!\n"+ bcolors.RESET)
  
elif Difficulty == "3" or Difficulty == "hard":
 global action 
 food_remaining = 200
 health_level = 2
 max_food=200
 print (bcolors.Red +"\nYou are playing on hard mode!\n"+ bcolors.RESET)
 
 





#gameplay>>>
playing = True
status()


#got this from stackoverflow, but I modifyed it!

while playing:
 print()
 
 action = input("What "+player_name+"'s" " action? " )
  
 if action == "travel" or action == "t": 
    travel()
 elif action == "rest" or action == "r":
   if health_level == 5:
      print ("You have full health")
   else:
	   rest()
 
 
 if action == "hunt" or action == "h":
	 hunt()
 elif action == "quit" or action == "q":
		quit()
 elif action == "help" or action == "?":
		help()
 elif action == "status" or action == "s":
		status()
 elif action == "eat" or action == "e": 
   eat()
 elif action == "credits" or action == "c":
   credits()


 if game_over():
		playing = False

if player_wins():
	print(bcolors.Green +"\n\nCongratulations you made it to Oregon alive!"+ bcolors.RESET)
	status()
else:
	print(bcolors.Red +"\n\nYou lost!"+ bcolors.RESET)
	status()
	print(loss_report())
