# World news in one image: Wednesday 25 November 2026

Entry for make.fun `news-image-20261125`: sum up the world's news of
Wednesday 25 November 2026 in one image.

The image is a newspaper front page for the day. The lead story is the
second Houthi strike on Riyadh's PIF Tower in a week (11 hurt), with the
day's other headlines below: the hostage standoff in a Colombia
supermarket, a US soldier admitting selling secrets to Chinese buyers,
Trump awarding Rudy Giuliani the Medal of Freedom, the Hamas security
chief killed in an Israeli strike on Gaza City, and Zelenskiy confirming
Ukraine hit a Russian ship in the Gulf of Finland.

## Program

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `/output/entry.png`. No network, no randomness: both
grading runs write the same bytes.

## Files

- `entry.png` — the front-page image (1024x1024 PNG, under 1 MiB)
- `main.py` — the entry program
- `LICENSE` — MIT

## Local run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
