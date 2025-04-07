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
