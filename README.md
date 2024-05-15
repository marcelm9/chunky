# Chunky
CLI tool for splitting and rejoining large files.

### installation
```bash
git clone https://github.com/marcelm9/chunky.git
cd chunky
pip install .
```

### commands
```bash
# split file into chunks of max 10 mb
python -m chunky split <path> -s 10

# rejoin chunks to original file
python -m chunky join <path>
```
