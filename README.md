# Documents to MarkDown

**This CLI Python script converts documents to Markdown**

**Requisites:** Install Phyton and Poetry

To run this sample just clone this project and run the following command:
```shell
# From inside the Poetry project folder
poetry install
poetry run to-markdown path-to/document-to-convert.ext
```

## About MarkItDown

This sample program uses [MarkItDown](https://github.com/microsoft/markitdown) from Microsoft

MarkItDown currently supports the following file types:

    * PDF
    * PowerPoint
    * Word
    * Excel
    * Images (EXIF metadata and OCR)
    * Audio (EXIF metadata and speech transcription)
    * HTML
    * Text-based formats (CSV, JSON, XML)
    * ZIP files (iterates over contents)
    * Youtube URLs
    * EPubs

## Preparing your own MarkItDown Poetry project

In case you are not familiar with poetry. Here are some instructions to get your own project running:

### Pre-Requisites: Install Phyton and Poetry

Here are the [homebrew](https://brew.sh) instructions:

```shell
# Update and Upgrade if needed:
brew update
brew upgrate
brew doctor

# Install Python:
brew install python
python --version # if doesn't works try python3

# Install Poetry
brew install poetry
```

### Create Your Poetry Project

**Note:** These instrucrtions are for creating your Project from scratch. You don't need to clone this reposity, just follow the instructions from here on.

To create a poetry project
```shell
poetry new your-project-name
cd your-new-project-name
poetry add 'markitdown[all]'
```

At the time of this writing, the last command will probably fail with errors for the `youtube-transcript-api` python package.
At the end of the errors you may see somethine like this:

> For youtube-transcript-api, a possible solution would be to set the `python` property to ">=3.13,<3.14"

<br>

**To fix this you'll need to do the following:**

1. Modity the `pyproject.toml` file. Change the `requires-python` line as follows:

```toml
requires-python = ">=3.13,<3.14"
```

In case you get another similar error just use entry suggested by the displayed error instead of `">=3.13,<3.14"`.

2. After fixing the `requires-python` entry (if needed), you may run the poetry add command again: 

```shell
# Run inside your poetry project
poetry add 'markitdown[all]'
```

### Create your script

After this, you can just make your python project. To get you started, here's the cli.py file included in this sample:

```python
import argparse
from markitdown import MarkItDown

def main():
    parser = argparse.ArgumentParser(description="Convert any document to Markdown.")
    parser.add_argument("filepath", help="Path to the file")
    args = parser.parse_args()

    md = MarkItDown()
    result = md.convert(args.filepath)
    print(result.text_content)

if __name__ == "__main__":
    main()
```

## Running your script

At this point you are ready to run your CLI script. Use the following command:

```shell
poetry run python cli.py path-to/document-to-convert
```

## More about the poetry run command

You may have noticed that the last command is different from the one given at the start of the document.
That's because you can install your cli script but first you need to modify your `pyproject.toml` file.

In order to be able to run your script using `poetry run to-markdown`, add the following entry to your `pyproject.toml`:

```toml
[tool.poetry.scripts]
to-markdown = "cli:main"
```

Before you can run your script, you need to install it with `poetry install` (while being inside your project folder).
Now you can run your CLI script by using the following command:

```shell
poetry run to-markdown path-to/document-to-convert.ext
```

## Image Recognition

You can also use MarkItDown to generate a markdown that descibes the image.

Here is a sample program (remember to put your own api-key):

```python
import argparse
from pathlib import Path
from markitdown import MarkItDown
from openai import OpenAI

def main():
    parser = argparse.ArgumentParser(description="Describes any image in Markdown format.")
    parser.add_argument("filepath", help="Path to the image file")
    args = parser.parse_args()

    file_path = Path(args.filepath)

    if not file_path.exists():
        print(f"Error: File '{file_path}' not found")
        return

    client = OpenAI(api_key="your-api-key")

    md = MarkItDown(llm_client=client, llm_model="gpt-4o")
    result = md.convert(str(file_path))
    print(result.text_content)

if __name__ == "__main__":
    main()
```

Since this imports OpenAI, you need to run the `poetry add` command:

```shell
poetry add OpenAI
```

Also we will update the `pyproject.toml` file:

```toml
[tool.poetry.scripts]
to-markdown = "cli:main"
img-to-markdown = "img2md:main"
```

Finally to run the img-to-markdown script:

```
poetry run img-to-markdown path-to/your-image-file
```

