[![make.fun](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

# The Long Roast: Lawmakers and the File They Cannot Convert

Entry for the [make.fun bounty](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
"The Long Roast: Lawmakers and the File They Cannot Convert" — a three-day
contest for the best single satirical sentence roasting lawmakers who would
regulate AI, crypto or the internet but cannot convert a file to PDF.

## The entry

> The senator who would ban your crypto wallet still emails his aide a file called FINAL_final_v2.docx and asks her to turn it into a PDF.

## How it works

`main.py` (Python 3, stdlib only, no network) writes that one sentence to
`/output/entry.txt` (and `./entry.txt` for local verification). The output is
deterministic: every run produces byte-identical text, 136 characters, one
sentence, well inside the 1–320 character gate.

## Run it

```sh
python3 main.py
cat entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
