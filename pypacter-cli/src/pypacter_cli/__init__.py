"""
PyPacter CLI.

Command line interface for PyPacter.

We makes use of the [`click`][click] library for the defining and handling of
arguments, and uses the wrapper `rich_click` which leverages [`rich`][rich] to
provide rich text formatting for the CLI.

The [`cli`][pypacter_cli.cli] function is the entry point for the CLI and handles
the parsing of arguments.
"""

from __future__ import annotations

import logging

import click
import rich.traceback
import rich_click
import requests
from rich.logging import RichHandler

from pypacter_cli.__version__ import __version__, __version_tuple__
from pypacter_cli.util import make_sync

__all__ = [
    "__version__",
    "__version_tuple__",
    "__author__",
    "__email__",
    "__url__",
    "__license__",
    "__copyright__",
    "cli",
    "get_version",
    "process_input",
    "read_input_content_from_file_or_string",
]

__author__ = "Joshua Ellis"
__email__ = "joshua.ellis@smartbear.com"
__url__ = "https://github.com/pactflow/pactflow-python-coding-test"
__license__ = "Proprietary"
__copyright__ = "SmartBear Software and PactFlow"


logger = logging.getLogger("pypacter")
rich.traceback.install(suppress=[click, rich_click])
rich_click.rich_click.USE_MARKDOWN = True


@rich_click.command()
@rich_click.option(
    "-v",
    "--verbose",
    help="Increase the verbosity of the output. Can be specified multiple times.",
    count=True,
    metavar="",
    envvar="ACCORD_VERBOSE",
)
@rich_click.option(
    "-q",
    "--quiet",
    help="Decrease the verbosity of the output. Can be specified multiple times.",
    count=True,
    metavar="",
    envvar="ACCORD_QUIET",
)
@rich_click.option(
    "-V",
    "--version",
    help="Show the version and exit.",
    is_flag=True,
)
@make_sync
async def cli(
    verbose: int,
    quiet: int,
    version: bool,  # noqa: FBT001
) -> None:
    """PyPacter CLI.

    Command line interface for PyPacter.
    """
    if version:
        rich_click.echo(f"PyPacter CLI v{get_version()}")

    logging.basicConfig(
        level=logging.WARNING - 10 * (verbose - quiet),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                tracebacks_suppress=[click, rich_click],
            ),
        ],
    )


def get_version() -> str:
    """
    Get the version of PyPacter.

    Returns:
        The version string.
    """
    return __version__


def call_detect_language_api(code_snippet: str) -> Dict[str, str]:
    """
    Calls the FastAPI endpoint to detect the programming language.

    Args:
        code_snippet (str): The code snippet to analyze.

    Returns:
        dict: A dictionary with the detected language.
    """
    api_url = "http://127.0.0.1:8000/detect-language"  # Replace with your actual API URL

    try:
        response = requests.post(api_url, json={"code_snippet": code_snippet})
        response_data = response.json()
        return response_data

    except requests.RequestException as req_exc:
        return {"error": f"Request error: {str(req_exc)}"}


@click.command()
@click.option('--input', prompt='Enter input (filename or string)', help='Input filename or string')
def process_input(input):
    """
    Process input provided by the user, either from a file or directly as a string.

    Args:
        input (str): The input provided by the user, which can be a filename or a string.

    Returns:
        None

    Prints:
        The content of the input, either from a file or directly as a string.

    """
    content = read_input_content_from_file_or_string(input)
    result = call_detect_language_api(content)
    click.echo(f'Programming language is :\n{result}')
