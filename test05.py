#学生信息管理系统
user1={"用户名":"KevinHaao","姓名":"刘阿皓","密码":"123456"}
user2={"用户名":"Kevinhaao","姓名":"刘大皓","密码":"12345678"}
user3={"用户名":"kevinHaao","姓名":"刘小皓","密码":"123456789"}
userList=[user1,user2,user3]

#学生信息
Student1={"学号":"2022033090","姓名":"刘泽皓","年龄":"18","性别":"男"}
Student2={"学号":"2022033111","姓名":"徐  凡","年龄":"19","性别":"男"}
Student3={"学号":"2022030928","姓名":"童敬雅","年龄":"18","性别":"女"}
Student4={"学号":"2022035142","姓名":"熊诗涵","年龄":"18","性别":"女"}
StudentList=[Student1,Student2,Student3,Student4]

#登录函数login
def login():
	while 1==1:
		msg="失败"
		uname=input("请输入用户名：")
		upwd=input("请输入密码:")
		for user in userList:
			if user["用户名"]==uname  and user["密码"]==upwd:
				msg="成功"
				print("--------验证成功！欢迎您使用学生管理系统，",user["姓名"])
				break
		if msg=="失败":
				print("用户名或密码有误，请重新输入")
				continue 
		else:
			break  
	return msg  

#展示学生信息
def showStudents():
	print("--学号---------------姓名--------年龄------性别--")
	for student in StudentList:
		print("--"+student["学号"]+"--------"+student["姓名"]+"--------"+student["年龄"]+"--------"+student["性别"])
	print("-----------------------------------------------------")

#添加学生信息
def addStudents():
	lista=[]    
	for student in StudentList:
		lista.append(int(student["学号"]))
	newNum=input("请输入新学生学号：")
	newStudentName=input("请输入新学生姓名：")
	newAge=input("请输入新学生年龄：")
	newSex=input("请输入新学生性别：")
	new={"学号":newNum,"姓名":newStudentName,"年龄":newAge,"性别":newSex}
	StudentList.append(new) 
	print("---------该学生",newStudentName,"添加成功---------")
	showStudents()

#删除学生信息
def delStudents():
	while 2==2:
		msg=0 
		num=input("请输入您要删除学生学号:")
		for student in StudentList:
			if num==student["学号"]:
				StudentList.remove(student) 
				msg=1
				print("-----该学生信息已删除成功！")
		if msg==0: 
			print("您的输入有误，请重新输入")
			print("这是当前学生信息列表")
			showStudents()
			continue 
		else:
			print("这是当前学生信息列表")
			showStudents() 
			break
#修改学生信息
def EditStudents():
	while 3==3:
		msg=0 
		num=input("请输入您要修改的学生信息的学号:")
		for student in StudentList:
			if num==student["学号"]:
				newName=input("请输入新的学生姓名（若无需修改请输入原信息即可）：")
				student["姓名"]=newName
				newNum=input("请输入要修改的学生学号（若无需修改请输入原信息即可）：")
				student["学号"]=newNum
				newAge1=input("请输入要修改的年龄（若无需修改请输入原信息即可）：")
				student["年龄"]=newAge1
				newSex1=input("请输入要修改的学生性别（若无需修改请输入原信息即可）：")
				student["性别"]=newSex1
				msg=1
				print("-----",student["姓名"],"姓名:",newName,"修改成功！")
				print("-----",student["学号"],"学号:",newNum,"修改成功！")
				print("-----",student["年龄"],"年龄:",newAge1,"修改成功！")
				print("-----",student["性别"],"性别:",newSex1,"修改成功！")
		if msg==0: 
				print("您的输入有误，请重新输入")
				print("这是当前学生列表信息")
				showStudents()
				continue 
		else:
			print("当前学生列表信息")
			showStudents() 
			break


#显示主菜单
result=login()
while 0==0:
	if result=="成功":
		print("---------主菜单--------")
		print("-----1.显示学生列表-----")
		print("-----2.增加学生信息-----")
		print("-----3.删除学生---------")
		print("-----4.修改学生信息-----")
		print("-----5.退出------------")

		chioce=int(input("请输入业务编号(1-5):"))
		if chioce==1:
		#显示学生列表
			showStudents()
		elif chioce==2:
		#增加学生信息
			addStudents()
		elif chioce==3:
		#删除学生
			delStudents()
		elif chioce==4:
		#设置修改学生
			EditStudents()
		elif chioce==5:
		#退出
			print("-------正在退出......")
			print("退出成功，感谢使用！")
			break
		else:
			print("您输入有误，请重新输入！")
			continue
