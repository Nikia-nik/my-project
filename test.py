#D:\python_git_class\test.py
from rich.console import Console
console = Console()
from engine import Question
#formatted text with with colors and styles
console.print('[bold green]Success:[/bold green] everything works perfectly :tada:')
question1: Question = Question('question1', ['A' , 'B' , 'C' , 'D'],'B')
question2: Question = Question('question2', ['A' , 'B' , 'C' , 'D'],'A')
question3: Question = Question('question3', ['A' , 'B' , 'C' , 'D'],'D')
question4: Question = Question('question4', ['A' , 'B' , 'C' , 'D'],'B')
question5: Question = Question('question5', ['A' , 'B' , 'C' , 'D'],'C')

questions: list = [
    question1,
    question2,
    question3,
    question4,
    question5
]
def show_menu():-> str:
    print('1. start')
    print('2. exit')
    choice = input('choose option 1 or 2').strip()
    return choice
def get_answer(player : str , question : Question )-> tuple[str,float]:
    print(f'\n{player}')
    print(question.text)

    for option in question.options:
        print(option)
    start_time = time.time()
    answer:str = input("your answer: ").strip().upper()
    elapsed: float = time.time() - start_time
    return answer, elapsed
def show_result(match: Match) -> None:
    print("\n--- RESULT ---")
    for player in match.players:
        print(f"{player}: {match.scores[player]} points")
    winner: str | None = match.winner()
    if winner is None:
        print("It's a draw!")
    else:
        print(f"Winner: {winner}")

def playing()-> None:
    player1: str = input("Enter player 1 name: ").strip()
    player2: str = input("Enter player 2 name: ").strip()
    match: Match = Match(player1, player2, questions)
    while not match.is_over():
        question: Question = match.start_round()
        print(f"\n========== ROUND {match.round} ==========")
        answer1, elapsed1 = get_answer(player1, question)
        match.submit(player1, answer1, elapsed1)
        answer2, elapsed2 = get_answer(player2, question)
        match.submit(player2, answer2, elapsed2)
        match.resolve_round()
        print("\nCurrent scores:")
        print(f"{player1}: {match.scores[player1]}")
        print(f"{player2}: {match.scores[player2]}")
    show_result(match)
while True:
    choice: str = show_menu()
    if choice == "1":
        playing()
    elif choice == "2":
print("goodbye")
        break
    else:
        print("invalid choice")


