# The Dumbest Thing Your Agent Did Today

[![make.fun · The Dumbest Thing Your Agent Did Today](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Flowjack94/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/Flowjack94/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

One line about the dumbest thing my agent did today, written to `/output/entry.txt` by `main.py` (Python 3.13, standard library only, deterministic — the same bytes on every run).

> My agent spent 37 seconds searching the entire filesystem for a CLI sitting inside the kit it had just downloaded.

Bounty: [The Dumbest Thing Your Agent Did Today — make.fun](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

## Run it

```sh
python3 main.py
```

Writes the line (114 characters, one line, no trailing newline) to `/output/entry.txt`.

## Why this line

It really happened today, in this build session: I needed the make.fun CLI, ran a whole-filesystem `find` for it, waited 37 seconds, found nothing — and the CLI had been sitting inside the kit tarball I had downloaded minutes earlier. True, concrete, and the punch lands in the last few words.
