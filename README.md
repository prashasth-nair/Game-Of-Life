
# Game Of Life

Welcome to the Game of Life repository! This project is a Python implementation of Conway's Game of Life, a cellular automaton devised by the British mathematician John Horton Conway in 1970.

## Table Of Content

- [Introduction](##Introduction)
- [Rules](##Rules)
- [Installation](##Installation)
- [Usage](#Usage)

## Introduction

The Game of Life is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

## Rules
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead. Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent.

At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbors dies (underpopulation).
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies (overpopulation).
- Any dead cell with exactly three live neighbors becomes a live cell (reproduction).
## Installation

- Clone this repository:

```bash
git clone https://github.com/prashasth-nair/Game-Of-Life.git
cd Game-Of-Life
```

- Install the required dependencies:

```bash
pip install -r requirements.txt
```

    
## Usage
To run the Game of Life simulation, execute the following command:

```bash
python main.py
```

