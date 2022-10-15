from cli.main import main


def test_hello_world_cli(capsys):
    main(["test"])
    result = capsys.readouterr()
    assert result.out == "hello test\n"
