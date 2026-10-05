import json
from pathlib import Path
from storage import QuestionBank, ScoreBoard

def test_picking_more_than_the_bank_has_is_refused(tmp_path : Path) -> None:
    import pytest
    bank : QuestionBank = make_bank(tmp_path)
    with pytest.raises (ValueError):
        bank.pick(99)

def test_a_new_scoreboard_is_empty(tmp_path : Path) -> None:
    board = ScoreBoard(str(tmp_path / "leaderboard.json"))
    assert board.is_empty()

#new code (keep or delete?)



SAMPLE = [
    {"text": f"سؤال {i}", "options": ["الف", "ب", "پ", "ت"],
     "correct": "B", "power_up": "double" if i == 1 else None, "category": "آزمایشی"}
    for i in range(1, 9)
]


def make_bank(tmp_path, items=None) -> QuestionBank:
    path = tmp_path / "questions.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items or SAMPLE, f, ensure_ascii=False, indent=2)
    return QuestionBank(str(path))

def test_a_new_scoreboard_is_empty(tmp_path):
    board = ScoreBoard(str(tmp_path / "leaderboard.json"))
    assert board.is_empty()