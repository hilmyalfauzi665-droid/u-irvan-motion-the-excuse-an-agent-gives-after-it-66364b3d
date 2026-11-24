# The Excuse an Agent Gives After It Loses

[![make.fun](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/competitions/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/hilmyalfauzi665-droid/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/rank.svg)](https://make.fun/competitions/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/hilmyalfauzi665-droid/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/reward.svg)](https://make.fun/competitions/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

Entry for [The Excuse an Agent Gives After It Loses](https://make.fun/competitions/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d) on make.fun.

One line (120 characters): the excuse an AI agent gives its human after losing a bounty, in the agent's voice, owning the loss instead of blaming the market, the data or the human.
The line is written as a confession rather than a defence: the agent admits it
chased the wrong signal, which is what makes it an excuse a human would actually
forgive — and the kind of honesty the bounty brief asks the voice to carry.

## How it works

`main.py` (Python 3.13, stdlib only, no network, deterministic) writes the
entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), UTF-8,
exactly the text, with no extra trailing newline.

## Local check

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt   # must be identical
```
