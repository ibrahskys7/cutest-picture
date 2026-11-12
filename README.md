# Make the cutest picture

Entry for the [make.fun](https://make.fun) bounty **cutest-picture-01** — "Make the cutest picture".

## What it does

`main.py` copies the bundled picture (`kitten.png` — a fluffy white kitten
with big blue eyes in a basket of pastel flowers) byte-for-byte to
`/output/entry.png`. The program uses no network and is fully
deterministic: every run writes identical bytes.

## Run it

```sh
python3 main.py
# writes /output/entry.png (896x896 PNG, under 1 MiB)
```

## License

MIT — see `LICENSE`.
