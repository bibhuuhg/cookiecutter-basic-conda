import pytest
from {{ cookiecutter.package_name }} import cli

@pytest.mark.skip(reason = "skip for now")
def test_cli_template():
    assert cli.cli() is None
