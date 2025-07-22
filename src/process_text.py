import sys
import string

def process_text(text: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    cleaned = text.translate(translator).lower()
    words = cleaned.split()
    return ' '.join(reversed(words))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            data = f.read()
    else:
        data = sys.stdin.read()
    print(process_text(data))
