import json
from unittest.mock import patch

from game import prompt_choice, show_leaderboard
from storage import QuestionBank, ScoreBoard


def test_question_bank_count(tmp_path):
    questions_file = tmp_path / "questions.json"

    data = [
    {
        "text": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct": "B"
    },
    {
        "text": "What is 3 + 3?",
        "options": ["5", "6", "7", "8"],
        "correct": "B"
    }
]


    questions_file.write_text(
        json.dumps(data),
        encoding="utf-8"
    )

    bank = QuestionBank(str(questions_file))

    assert bank.count() == 2


def test_question_bank_pick(tmp_path):
    questions_file = tmp_path / "questions.json"

    data = [
        {
            "text": "Question 1",
            "options": ["A", "B", "C", "D"],
            "correct": "A"
        },
        {
            "text": "Question 2",
            "options": ["A", "B", "C", "D"],
            "correct": "B"
        },
        {
            "text": "Question 3",
            "options": ["A", "B", "C", "D"],
            "correct": "C"
        }
    ]

    questions_file.write_text(
        json.dumps(data),
        encoding="utf-8"
    )
    bank = QuestionBank(str(questions_file))

    questions = bank.pick(2)

    assert len(questions) == 2


def test_scoreboard_is_empty(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.json"

    board = ScoreBoard(str(leaderboard_file))

    assert board.is_empty() is True


def test_scoreboard_record(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.json"

    board = ScoreBoard(str(leaderboard_file))
    board.record(
        "Alice",
        "Alice",
        10,
        "Bob",
        5
    )

    assert board.is_empty() is False

    top = board.top()

    assert top[0][0] == "Alice"
    assert top[0][1]["points"] == 10
    assert top[0][1]["wins"] == 1


def test_scoreboard_records_both_players(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.json"

    board = ScoreBoard(str(leaderboard_file))

    board.record(
        "Alice",
        "Alice",
        10,
        "Bob",
        5
    )

    top = board.top()

    names = [item[0] for item in top]

    assert "Alice" in names
    assert "Bob" in names


def test_scoreboard_winner_gets_one_win(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.json"

    board = ScoreBoard(str(leaderboard_file))
    board.record(
        "Alice",
        "Alice",
        10,
        "Bob",
        5
    )

    top = board.top()

    alice = next(item for item in top if item[0] == "Alice")
    bob = next(item for item in top if item[0] == "Bob")

    assert alice[1]["wins"] == 1
    assert bob[1]["wins"] == 0


def test_scoreboard_save_and_load(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.json"

    board = ScoreBoard(str(leaderboard_file))
    board.record(
        "Alice",
        "Alice",
        10,
        "Bob",
        5
    )

    # Load the same file again
    new_board = ScoreBoard(str(leaderboard_file))

    top = new_board.top()

    assert top[0][0] == "Alice"
    assert top[0][1]["points"] == 10
    assert top[0][1]["wins"] == 1


def test_scoreboard_sorted_by_wins_then_points(tmp_path):
    leaderboard_file = tmp_path / "leaderboard.json"


    board = ScoreBoard(str(leaderboard_file))

    # Alice wins once with 10 points
    board.record(
        "Alice",
        "Alice",
        10,
        "Bob",
        5
    )

    # Bob wins once with 20 points
    board.record(
        "Bob",
        "Bob",
        20,
        "Charlie",
        5
    )

    top = board.top()
     # Both have one win, so Bob should be first
    # because Bob has more points.
    assert top[0][0] == "Bob"
    assert top[1][0] == "Alice"


def test_prompt_choice_accepts_lowercase(tmp_path):
    question = type(
        "Question",
        (),
        {
            "text": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"]
        }
    )()

    with patch("game.input", return_value="b"):
        choice, elapsed = prompt_choice("Alice", question)

    assert choice == "B"
    assert elapsed >= 0
    def test_prompt_choice_rejects_invalid_input(tmp_path):
         question = type(
        "Question",
        (),
        {
            "text": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"]
        }
    )()

    with patch(
        "game.input",
        side_effect=["X", "A"]
    ):
        choice, elapsed = prompt_choice("Alice", question)

    assert choice == "A"
    assert elapsed >= 0
#timport pytest
#from engine import question,Match,TIME_LIMIT,POINTS,SPEED_BONUS
#@pytest.mark.parametrize(
    ##"choice"
   #["B","b","b"]
#)
#def test_question_correct_answer (choice):
    #question = Question(
        #"what is 2+2?",
        #["3","4","5","6"],
        #"B",
    #)
#assert question.is_correct(choice)
#@pytest.mark.parametrize
#hold ctrl and / (its my ?) so they're no longer in # comments
