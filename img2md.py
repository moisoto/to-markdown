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
