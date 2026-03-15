# Wealth Model

## What it does
Agents on a grid randomly give wealth to neighbors. Everyone starts with 1 coin, but after a bunch of trades, some end up with tons while others have nothing. It's weird how fair rules create unfair outcomes.

## What I learned
This blew my mind - inequality happens even when everyone plays by the same rules! No cheating, no special advantages, just random exchanges. But math being math, wealth piles up anyway. It's like how random walks in physics create patterns - here it creates rich and poor.

## How to run
```bash
cd /Users/vedprakash/Desktop/Gsoc26/GSoC-learning-space
python models/wealth_model/model.py
```

Runs 50 steps with 50 agents on a 10x10 grid, then shows wealth stats. Change `num_agents`, `width`, `height` in the code if you want.
