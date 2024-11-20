score = 0
print("Haii! And welcome to the lifeful quiz!! This test is all about the life
series! YAY!!!")
name = input("Enter your name HERE: ").title()
answer = input("Well hello there " + name + ". Thats a fantastic name!! Are you
ready to play!?!! ")
if answer == "Yes" or "yes" or "y" or "Y":
print("YAHOO!!!!! Now lets play!!")
print("""------------------------------
Question 1:""")
x = input("Q: How many series has there been? [Not counting Real Life] ")
if x == "6":
print("Great job! You know some stuff!")
score += 1
else:
print("you suck...")
print("""------------------------------
Question 2:""")
z = input("Q: Who [used] to be the canary? [aka who perma died first every season
til secret life] ").lower()
if z == "jim" or z == "solidarity" or z == "solidartygaming" or z == "jimmy" or z
== "solidarityGaming":
print("Awesome sauce your good!")
score += 1
else:
print("um ok...ur wrong")
print("""------------------------------
Question 3:""")
y = input("Q: Whats the username of a player that was part of 3rd life? ").lower()
if y == "grian" or y == "goodtimeswithscar":
print("hey thats desert duo :D")
score += 1
elif y == "zombiecleo" or y == "impulsesv" or y == "tangotek" or y ==
"bdoubleO100":
print("hello crastle members!!")
score += 1
elif y == "renthedog" or y == "inthelittlewood" or y == "bigb" or y == "bigbst4tz2"
or y== "skizzleman" or y== "ethoslab":
print("RED WINTER IS COMING!!!!! hello dogwarts!!")
score += 1
elif y == "solidaritygaming" or y== "dangthatsalongname" or y== "smajor1995":
print("heya flower husband ^_^ ")❁
score += 1
elif y== "smallishbeans":
print("hello wolf king! ")🐺🐺🐺
score += 1
else:
print("wow..ur really bad there was a LOT of choices to not get wrong...")
print("""------------------------------
Question 4:""")
c = input("Q: Who was the winner of the fourth series? [Limited Life]? ")
if c == "inthelittlewood" or c == "martyn":
print("yes!!! good job...ps...limited life the best")
score += 1
else: print("urm....no thats wrong!")
print("""------------------------------
Your final life is gone!""")
print("You Died! " + name + " died to the watchers.")
print("Score: ", score)
