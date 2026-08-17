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
print(len(questions))
while True:
    print('1. start')
    print('2. exit')
    choice = input('choose option 1 or 2').strip()
    if choice =='1':
        score =0
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
        print(f'{(score)/len(questions)*100}%')
    elif choice =='2':
        print('goodbye')
        break
    print('hi :)')
    print('testing')
        #to learn git use the document in the official site
        #git init
        #init is short for 'initialization'?
        #. before name of a folder makes it hidden
        #repository = the folder we work with
        #  git add .
        #git status
        #git commit -m 
        #-m is our message 
        #for every change made on our project we have to use commit and add

