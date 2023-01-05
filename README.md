# Slovs

This application is designed to memorize English words.

## Usage

1. Create an environment variable `export SLOVSFILE='name_file.json'` containing the path to dictionary-file.
2. To create a file `'name_file.json'` if it does not exist, add the first word to the dictionary with `./main.py -u word=word`
A dictionary will be created and will take this form:

```

{
  "word": {
    "translation": "слово",
    "score": 0
  }
}

```

3. To run the program, enter `python3 main.py` into the console.

_You can also override the file path in an environment variable using `-f` flag: `python3 main.py -f name_file.json`_
 