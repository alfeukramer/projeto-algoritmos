from challenges.challenge_encrypt_message import encrypt_message


import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(3, "a")

    assert encrypt_message("😷🤒🤕🤢🤮🤧", 3) == "🤕🤒😷_🤧🤮🤢"

    assert encrypt_message("😷🤒🤕🤢🤮🤧", 4) == "🤧🤮_🤢🤕🤒😷"

    assert encrypt_message("😷🤒🤕🤢🤮🤧", 9) == "🤧🤮🤢🤕🤒😷"
