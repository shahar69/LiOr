# Using process_text.py

The `process_text.py` script reads text, removes punctuation, converts it to lowercase, and prints the words in reverse order.

## Running the script

Run it with Python by providing a text file path or piping text into it:

```bash
# With a file
python src/process_text.py path/to/file.txt

# With piped input
echo "Hello, World!" | python src/process_text.py
```

The second command outputs:

```
world hello
```
