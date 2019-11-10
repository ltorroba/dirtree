# dirtree
Small script that generates a LaTeX `forest` representation of a directory. Quite useful when writing
up documentation and you want to give an overview of your directory structure.

## Installation
There are two ways to install.

### From source (recommended)
To install from source:

1. Clone this repository and `cd` into it
2. Run `pip install -e .`
3. To test this is working, run `dirtree`.

### From pyPI
I wouldn't recommend a pyPI install as this project is not stable.
But you could run `pip install dirtree` if you
like to live dangerously.

## Usage

To generate a tree for a directory, run `dirtree [path to directory]`.
If you are generating a tree for a repostiory, I would recommend passing
`.git` into the directories you would like to ignore, e.g.
`dirtree . --ignore ".git"`.
If you want to ignore multiple directories, just list them, e.g.
`dirtree . --ignore ".git" "dirtree"`
To avoid outputting to the terminal, use the `-o` flag and the file
you want to save the tree to.

### Help

The help in `dirtree -h` should be enough to get you started.

```
usage: dirtree [-h] [--output OUTPUT] [--root [ROOT]]
                [--ignore [IGNORE [IGNORE ...]]] [--verbose]
                dir

Generates a forest tree for a directory.

positional arguments:
  dir

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output to a file instead of the console
  --root [ROOT]         Sets the label of the root of the tree
  --ignore [IGNORE [IGNORE ...]]
                        Directories to ignore
  --verbose, -v         Enable logging to console
```
