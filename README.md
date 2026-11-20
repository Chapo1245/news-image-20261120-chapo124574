# news-image-20261120 — The World in One Picture

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Chapo1245/news-image-20261120-chapo124574/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Chapo1245/news-image-20261120-chapo124574/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up **Friday 20 November 2026**'s world news: nine verified
stories in a 3×3 grid of illustrated photo panels, each with a short bold
headline and its source. No invented stories, no speculation as fact.

## The nine stories

1. **Cyclone Akvan hits India** — landfall near Gopalpur, Odisha; 72,000 evacuated (IMD)
2. **Leaders gather in China** — Trump, Xi & Putin shake hands (NYT)
3. **Embassies hit in Kyiv** — Austria & Dutch missions damaged in Russian strikes (AFP)
4. **Bridge hit a 3rd time** — Kerch Bridge, rail traffic halted (BBC)
5. **Top court sends Han case back** — 15-year term overturned, retrial ordered (Reuters)
6. **US–Venezuela military deal** — training & intel sharing (CNN)
7. **Yunus home set ablaze** — shutdown as unrest spreads in Bangladesh (Reuters)
8. **Fiji declares disaster** — El Niño drought drains water (Reuters)
9. **Nicholls ton up in Wellington** — NZ 243/5 on Day 1 vs India (TOI)

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
repository's `entry.png` byte for byte to `/output/entry.png`, so both grading
runs produce identical bytes. The image is 1024×1024 and under 1 MiB.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Built for the [make.fun bounty](https://make.fun/bounty/news-image-20261120).

<sub>Entered on [make.fun](https://make.fun/?ref=wtacm6ft&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
