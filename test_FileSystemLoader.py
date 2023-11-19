import pytest
from FileSystemLoader import FileSystemLoader
from main import main


@pytest.fixture
def setup():
    mainclass = main()
    yield mainclass

@pytest.mark.getters
def test_get_root_path(setup, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: r"E:\Hitachi Test\testFs")
    setup.set_root_path()
    assert setup.get_root_path() != None