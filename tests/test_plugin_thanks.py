import pytest
from app import App

def test_app_thanks_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'thanks' command and outputs 'Thank you!'."""
    inputs = iter(['thanks', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    # Check that the exit was graceful with the correct exit code
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output from the 'thanks' command
    out, err = capfd.readouterr()
    
    # Assert that 'Thank you!' was printed to stdout
    assert "Thank you!" in out, "The 'thanks' command did not produce the expected output."