# Wilmott Amin archive

This repository is an archival copy of the Wilmott Technical Forum thread
[*Breakthrough in the theory of stochastic differential equations and their simulation*](https://forum.wilmott.com/viewtopic.php?f=4&t=99702).

The thread was started by the forum user **Amin** and combines proposed mathematics about stochastic differential equations and simulation with extensive personal writing. This repository preserves the public discussion for easier reading and analysis. Inclusion here does not endorse or verify any mathematical, medical, political, or personal claims made in the posts.

![Monthly posting rate from April 2016 to January 2026](assets/posting_rate.png)

The January 2017 spike is **249 posts in one month**. Of 2,913 archived posts, 2,910 have parseable timestamps.

## Coverage

- 2,913 posts
- 59 cleaned Markdown pages
- 195 raw HTML pages
- Date range: April 17, 2016 to January 20, 2026
- 1,117 locally archived images
- Combined and split PDF editions

The Markdown archive begins at [`archive/thread_page/index.md`](archive/thread_page/index.md). The combined PDF is [`archive/pdfs/wilmott_thread.pdf`](archive/pdfs/wilmott_thread.pdf); three smaller parts are also included.

## Summary

What begins as a mathematical “breakthrough” becomes a 2,913-post, decade-long record of apparent persecutory delusions unfolding in public. Amin starts by posting equations. Soon he is also reporting hacked computers, invisible brain control, poisoned food and water, gases, microwave attacks, intelligence agencies, altered MATLAB programs, psychiatric detention, and antipsychotic injections imposed by people trying to suppress his research.

The structure barely changes for ten years: Amin announces a world-changing result, posts enormous walls of MATLAB, discovers that it does not work, attributes the setback to exhaustion, medication, or hostile interference, fixes something, and announces an even bigger result. The other quants slowly disappear. Their technical forum becomes one man's research notebook, grievance archive, trading diary, medical chronicle, and autobiography.

This README does not diagnose Amin. It summarizes what his posts appear to document. His allegations are not independently verified, and some entries contain hostile political language and antisemitic generalizations.

## Timeline

This timeline was synthesized from six independent reading passes over all 59 cleaned Markdown pages. It maps the thread; it does not validate the mathematics or autobiographical claims.

| Date | Posts | Event |
|---|---:|---|
| 2016 | #1–#249 | **The breakthrough.** Amin arrives with a supposedly revolutionary equation solver. Within weeks the program is incomplete, he has worked more than 24 hours without sleep, and he says hackers are attacking his computers. He uploads a paper, then worries SSRN may be showing him a fake version of its website because nobody is downloading it. |
| 2017 | #250–#555 | **The forum becomes the diary.** Amin says he has wasted half his life in finance. A journal rejects his paper. “Brain control” begins appearing as an explanation for mistakes, lost concentration, and stalled work. The promised proofs never quite arrive; the posts keep coming. |
| 2018–2019 | #556–#850 | **Every correction reveals a larger breakthrough.** Forum experts point out prior work and serious errors. Amin acknowledges some of them, changes direction repeatedly, pauses for algorithmic trading, announces that he is stopping, and inevitably returns with a new program. |
| 2020 | #851–#1000 | **The persecution narrative takes over.** Amin reports antipsychotic injections, drugged food, gases, microwaves, torture, mind-control chemicals, and attempts to stop him promoting his work on LinkedIn. Dense mathematics and descriptions of invisible attacks now appear side by side. |
| 2021–2022 | #1001–#1650 | **Detention, injections, code, repeat.** Amin describes psychiatric detention and medication that he says damages his mind, then resumes posting MATLAB within days. He alternates between caring for his mother, announcing breakthroughs, burning out, alleging attacks by intelligence and military agencies, and seeking venture capital for high-frequency trading. |
| 2023 | #1651–#2150 | **The perfect miniature of the whole thread.** Amin says agents altered his MATLAB results. He later discovers that he reversed two arguments to `surf` and publicly retracts that accusation. Around it: money trouble, medication cycles, stock models, neural-network schemes, a funeral, a stolen wallet, and many more alleged conspiracies. |
| 2024 | #2151–#2600 | **“Math AI.”** The newest breakthrough receives its grandest name yet. Amin mixes claims of instant mathematical intelligence with Bitcoin experiments, job and consulting appeals, injection complaints, political rants, and continuing accusations that governments and psychiatrists are sabotaging him. |
| 2025–Jan 2026 | #2601–#2913 | **The final spiral.** After a night he attributes to microwave targeting, Amin turns the thread into a Lahore journal of meals, water, errands, and research. He says he is detained for nearly two months, returns heavily medicated, resumes coding, and posts through his mother's cancer surgery. The archive ends with him afraid to test his latest “solution” because agents may alter the program. |

## Repository contents

- `archive/raw/` — HTML responses captured from the forum
- `archive/raw.zip` — compressed copy of the raw responses
- `archive/thread_page/` — extracted and cleaned Markdown, split into 59 pages
- `archive/images/` — images downloaded from links embedded in the posts
- `archive/pdfs/` — combined and split rendered editions of the thread
- `assets/` — README images and charts
- `reports/` — exploratory generated analyses
- `docs/` — extraction notes
- `scripts/` — scraper, extraction, analysis, report, and chart utilities

See [`scripts/README.md`](scripts/README.md) for the utility index and commands.

## Extraction notes

All 2,913 posts were extracted. The cleanup pipeline reports 45 posts (about 1.5%) with unbalanced LaTeX delimiters inherited from the source material. Those expressions were not guessed or silently rewritten where the author's intent was unclear.

The raw HTML remains available when fidelity matters. Forum pages may have changed since this snapshot was collected.

## Attribution and status

The posts and embedded materials belong to their respective authors and rights holders. This is an independent archival project and is not affiliated with, sponsored by, or endorsed by Wilmott, Wilmott.com, or the forum participants.

No license is granted for the archived third-party content. The utility scripts are included for reproducibility, but this repository as a whole should not be treated as an open-licensed dataset.
