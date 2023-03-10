from challenges.challenge_encrypt_message import encrypt_message


import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo invÃ¡lido para message"):
        encrypt_message(3, 3)

    with pytest.raises(TypeError, match="tipo invÃ¡lido para key"):
        encrypt_message(3, "a")

    assert encrypt_message("ð·ð¤ð¤ð¤¢ð¤®ð¤§", 3) == "ð¤ð¤ð·_ð¤§ð¤®ð¤¢"

    assert encrypt_message("ð·ð¤ð¤ð¤¢ð¤®ð¤§", 4) == "ð¤§ð¤®_ð¤¢ð¤ð¤ð·"

    assert encrypt_message("ð·ð¤ð¤ð¤¢ð¤®ð¤§", 9) == "ð¤§ð¤®ð¤¢ð¤ð¤ð·"
