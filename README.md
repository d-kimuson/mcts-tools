# MCTS tools

tools chains for

- Extract the match data path for deserialization.
- Extract shot patterns from deserialized match data.
- Output shot pattern data as JSON in a form readable by MCTS AI

## Setup

``` bash
$ poetry -V
Poetry version 1.1.4  # if not, install
$ pip install poetry

# install dependencies
$ poetry install

$ poetry shell  # active virtual environment

$ cp .env.sample .env  # and update to your own environment value
```

## Extract paths for deserialization

``` bash
$ python main.py path_list
```

then, created `dist/path_list.json` file.

## Extract shot patterns from deserialized match data

``` bash
$ python main.py extract
20 file has complited
40 file has complited
60 file has complited
...
```

For every 20 files, the shot pattern information that has been extracted is written to `dist/shot_patterns.json`. 

number of matchs is defined `MATCH_NUMBER` in `config/__init__.py`.

## Output shot pattern data as JSON in a form readable by MCTS AI

``` bash
$ python main.py csharp
```

then, created `dist/dist_for_csharp.json` file.
