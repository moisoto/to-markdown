import argparse
from pathlib import Path
from markitdown import MarkItDown

def main():
    parser = argparse.ArgumentParser(description="Convert any document to Markdown.")
    parser.add_argument("filepath", help="Path to the file")
    args = parser.parse_args()

    file_path = Path(args.filepath)

    if not file_path.exists():
        print(f"Error: File '{file_path}' not found")
        return

    md = MarkItDown()
    result = md.convert(str(file_path))
    print(result.text_content)

if __name__ == "__main__":
    main()
