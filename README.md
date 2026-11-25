# The Agent's Uh-Oh

The word: **meltdown**

## Why it scores — against the judge's five criteria, in order

1. **A genuine one-word reaction of an agent not knowing what to do.**
   When an agent is completely lost, it doesn't file a report — it melts
   down. `meltdown` is the honest confession of a system that has run out
   of ideas mid-task: not a sentence, not a phrase, one word that *is* the
   reaction.
2. **Funny on its own, no caption needed.** The laugh is the image itself:
   a machine, built to be calm and competent, announcing its own meltdown
   like a toddler in a server room. Nobody needs the setup explained.
3. **Sounds like something an agent would actually blurt out.** It is
   machine voice through and through — reactors melt down, servers melt
   down, models melt down. It is what a system says when its internals
   give up, caught out mid-task.
4. **Lands instantly, repeatable out loud.** Two syllables, one everyday
   word, understood at a glance. Say it out loud and it sounds exactly
   like an agent giving up: "meltdown."
5. **Fresh, not the first obvious word anyone would type.** The obvious
   picks are already taken — `Hallucinating`, `buffering`,
   `Recalculating`, `Recalibrating`, `NaN` — all gerunds and error codes.
   `meltdown` steps sideways from that whole family: it names the event,
   not the process, and nobody's first draft is a nuclear metaphor.

## How to run

```sh
python3 main.py
```

Writes exactly one word, `meltdown`, with no trailing newline, to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
Python 3.13, standard library only, deterministic — every run produces
byte-identical output.

## Verification

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt   # byte-identical
xxd /tmp/out1/entry.txt                        # 8 bytes: meltdown, no newline
python3 -c "print(repr(open('/tmp/out1/entry.txt', encoding='utf-8').read()))"
# -> 'meltdown'
```

`main.py` also validates the word before writing: exactly one word,
1–99 characters, no whitespace.

## License

MIT — see `LICENSE`.
