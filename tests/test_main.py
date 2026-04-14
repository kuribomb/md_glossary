import pytest

from myapp.main import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
