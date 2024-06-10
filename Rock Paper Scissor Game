#winning rule as follow:
 #Rock Vs Paper    --> Paper wins
 #Rock Vs Scissor  --> Rock wins
 #Paper Vs Scissor --> Scrissor

import random
l=["Rock","Scissor","Paper"]

while True:
 	Ccount=0
 	Ucount=0
 	UC=int(input('''
 	1 Yes
 	2 No/Exit
 	'''))
 	if UC==1:
 		for a in range(1,6):
 			UserInput=int(input('''
1 Rock
2 Scissor
3 Paper
               	 '''))
 			if UserInput==1:
 				Uchoice="Rock"
 			elif UserInput==2:
 				Uchoice="Scissor"
 			elif UserInput==3:
 				Uchoice="Paper"
 			Cchoice=random.choice(l)
 			if Cchoice==Uchoice:
 				print("computer value",Cchoice)
 				print("User value",Uchoice)
 				print("Game Draw")
 				Ucount=Ucount+1
 				Ccount=Ccount+1
 			elif (Uchoice=="Rock" and Cchoice=="Scissor") or (Uchoice
 				=="Paper" and  Cchoice=="Rock") or (Uchoice
 				=="Scissor" and Cchoice=="Paper"):
 			     print("computer value",Cchoice)
 			     print("User value",Uchoice)
 			     print("you win")
 			     Ucount=Ucount+1
 			else:
 				print("computer value",Cchoice)
 				print("User value",Uchoice)
 				print("computer win")
 				Ccount=Ccount+1

 		if Ucount==Ccount:
 			print("final game draw...")
 			print("User Score",Ucount)
 			print("computer Score",Ccount)
 		elif Ucount>Ccount:
 			print("final you win the game...")
 			print("User Score",Ucount)
 			print("computer Score",Ccount)
 		else:
 			print("final computer win the game...")
 			print("User Score",Ucount)
 			print("computer Score",Ccount)
 	else:
 		break		
