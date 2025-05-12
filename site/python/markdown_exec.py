from markdown import Markdown
from markdown_exec import formatter, validator

Markdown(
    extensions=["pymdownx.superfences"],
    extension_configs={
        "pymdownx.superfences": {
            "custom_fences": [
                {
                    "name": "python",
                    "class": "python",
                    "validator": validator,
                    "format": formatter,
                },
                {
                    "name": "sh",
                    "class": "language-sh",
                    "format": "??",
                }
            ]
        }
    }
)