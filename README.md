# Two-Sentence Horror

Entry for the make.fun bounty [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253) — write the scariest horror story you can in exactly two sentences.

[![Two-Sentence Horror](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![Rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/freysiatiara/two-sentence-horror/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![Reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/freysiatiara/two-sentence-horror/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)

## The story

> I replaced my doormat last Monday because the old one had worn thin where visitors step. By Friday the new mat was worn thin in the same spot, and I have not had a single visitor all week.

## How it works

`main.py` (Python standard library only) writes the story to `/output/entry.txt` — exactly two sentences, under 400 characters, file mode `0644`. Before writing, it validates the story: non-empty, 1–400 characters, exactly two sentences.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
