def test_picking_more_than_the_bank_has_is_refused(tmp_path : Path) -> None:
    import pytest
    bank : QuestionBank = make_bank(tmp_path)
    with pytest.raises (ValueError):
        bank.pick(99)

def test_a_new_scoreboard_is_empty(tmp_path : Path) -> None:
    board = ScoreBoard(str(tmp_path / "leaderboard.json"))
    assert board.is_empty()
