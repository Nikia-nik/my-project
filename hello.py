from rich.console import Console
console = Console()
from engine import Question
#formatted text with with colors and styles
console.print('[bold green]Success:[/bold green] everything works perfectly :tada:')
question1: Question = Question( ['A' , 'B' , 'C' , 'D'],'B')
question2: Question = Question(['A' , 'B' , 'C' , 'D'],'A')
question3 : Question = Question( ['A' , 'B' , 'C' , 'D'],'D')
question4: Question = Question(['A' , 'B' , 'C' , 'D'],'B')
question5: Question = Question(['A' , 'B' , 'C' , 'D'],'C')

questions: list = [Questions]= [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5
]


def show_menu()-> None:
    print('1. start')
    print('2. exit')
    choice = input('choose option 1 or 2').strip()
    return choice

def playing():
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
    return score
        

def show_result(score):
        print(f'{(score)/len(questions)*100}%')
    
choice=show_menu()
if choice=='1':
    score=playing()
    show_result(score)

elif choice=='2':
    print('goodbye')