print('helloooooo')
#D:\python_git_class\test.py
from rich.console import Console
console = Console()
#formatted text with with colors and styles
console.print('[bold green]Success:[/bold green] everything works perfectly :tada:')
questions: list = [
    ('question1', ['A' , 'B' , 'C' , 'D'],'B'),
    ('question2', ['A' , 'B' , 'C' , 'D'],'A'),
    ('question3', ['A' , 'B' , 'C' , 'D'],'D'),
    ('question4', ['A' , 'B' , 'C' , 'D'],'B'),
    ('question5', ['A' , 'B' , 'C' , 'D'],'C')
]
while true:
    def show_menu():
        print('1. start')
        print('2. exit')
        choice = input('choose option 1 or 2').strip()
        return choice

    def playing():
        score = 0
        for q, options, correct_answer in questions:
            print(f'\n{q}')
            for opt in options:
                print(opt)
            answer: str = input('your answer: ').strip().upper()
            if answer==correct_answer:
                print('correct')
                score+=1
            else:
                print('wrong')
                score-=3 
    
        return score

def show_result(score):

    print(f'{(score/len(questions))*100}%')

choice=show_menu()
if choice =='1':
        score=playing()
        show_result(score)
elif choice =='2':
        print('goodbye')



        #to learn git use the document in the official site
        #git init
        #init is short for 'initialization'
        #. before name of a folder makes it hidden
        #repository = the folder we work with
        #  git add .
        #git status
        #git commit -m 
        #-m is our message 
        #for every change made on our project we have to use commit and add
        #you have to create '.gitignore' so you can ignore some stuff from your project instead of bringing everything 
        #to your git
        #use the 'up' button to go to previous commands
        #'git restore' , we use that command to go back to the latest saved version
        #you can also use ctrl + & ctrl + y
        #we should use git commit for meaningful changes only so later on when we look at it, it makes sense
        #git log
        #you can use the 'down' button to see the previous changes made with 'git log' :)
        #home work:
        #make the game two players

        #شیی گرایی یک تکنیک برنامه نویسه تا بتونیم کد هام.ن رو دقیق تر و تمیز تز داشته باشیم 
        #یکی از دلایلی که از شیی گرایی استفاده میشه برای تقسیم کار و بخش بندی کرئنه
        #کد ها مستقل ترن چون یک خطا کل پروژه رو خراب نمیکنه
        #مهندسی پروژه مهمتر از کد نوشتنه
        #ویژگی خصوصیاته 
        #رفتار کاریه که انجام میدن
        #init=سازنده
        #text_options_correcttext
        

        

