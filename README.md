# Привет, это проэкт Slovs

## Description

This application is designed to memorize English words

## Usage

1. Add dictionary-file to your working directory (name_file.json):
```
{
	"in case of": "в случае",
	"public": "публичный",
	"only": "только"
}
```

2. Create an environment variable `export SLOVSFILE='name_file.json'` containing the path to dictionary-file.
3. To run the program, enter `./main.py -f name_file.json` into the console.
 