# STT Benchmark Leaderboard

- Generated: 2026-03-02T23:09:06Z
- Configs: 2
- WER pass threshold: 10%

## Overall Rank

Sorted by average WER (lower = better). RTF = realtime factor (synthesis time / audio duration; < 1.0 means faster than realtime).

| Config | Entries | Pass% | Avg WER | Median WER | Avg ms | P95 ms | Avg RTF | Load ms |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| tiny.en / int8 / cpu | 48 | 85.4% | 6.6% | 0.0% | 312 | 351 | 0.10x | 540 |
| small.en / int8 / cpu | 0 | 0.0% | 100.0% | 100.0% | 0 | 0 | 0.00x | 5027 |

## Category Breakdown — tiny.en / int8 / cpu

| Category | Count | Pass% | Avg WER | Avg ms |
|---|---:|---:|---:|---:|
| date | 4 | 50.0% | 18.8% | 323 |
| llm_conversion | 2 | 100.0% | 0.0% | 289 |
| llm_history | 4 | 100.0% | 0.0% | 316 |
| llm_math | 2 | 0.0% | 14.3% | 288 |
| llm_science | 6 | 100.0% | 0.0% | 290 |
| numeric | 2 | 100.0% | 0.0% | 338 |
| stem | 8 | 62.5% | 26.4% | 328 |
| time | 6 | 100.0% | 0.0% | 306 |
| tool_calculator | 4 | 100.0% | 0.0% | 308 |
| tool_date | 2 | 100.0% | 0.0% | 328 |
| tool_time | 4 | 100.0% | 0.0% | 314 |
| year | 4 | 100.0% | 0.0% | 317 |

## Entry Detail — tiny.en / int8 / cpu

Rows sorted by WER descending (worst first).

| ID | Category | Dur s | WER | ms | RTF | Reference | Hypothesis |
|---|---|---:|---:|---:|---:|---|---|
| chemical_formula__take01 | stem | 2.1 | 100% | 305 | 0.14x | The sample contains H two S O four. |  |
| chemical_formula__take02 | stem | 2.4 | 100% | 307 | 0.13x | The sample contains H two S O four. |  |
| date_us_short__take02 | date | 2.9 | 50% | 327 | 0.11x | Meeting is on March seventh twenty twenty six. | The meeting is on 377.26. |
| date_us_short__take01 | date | 4.1 | 25% | 307 | 0.07x | Meeting is on March seventh twenty twenty six. | Meeting is on 37-26. |
| llm_math_pi__take01 | llm_math | 2.8 | 14% | 282 | 0.10x | What is pi to two decimal places? | What is pie to two decimal places? |
| llm_math_pi__take02 | llm_math | 3.0 | 14% | 294 | 0.10x | What is pi to two decimal places? | What is pie to two decimal places? |
| stem_expression__take02 | stem | 3.8 | 11% | 334 | 0.09x | Solve x two plus y two equals z two. | So, x squared plus y squared equals z squared. |
| time_12h__take01 | time | 3.9 | 0% | 296 | 0.08x | The train leaves at three oh five PM. | The train leaves at 3.05 pm. |
| time_12h__take02 | time | 2.5 | 0% | 278 | 0.11x | The train leaves at three oh five PM. | The train leaves at 3.05 pm. |
| time_24h__take02 | time | 2.8 | 0% | 312 | 0.11x | Maintenance starts at fifteen forty five. | Maintenance starts at 1545. |
| year_1905__take01 | year | 3.7 | 0% | 326 | 0.09x | The building was completed in nineteen oh five. | The building was completed in 1905. |
| year_2001__take01 | year | 2.4 | 0% | 305 | 0.12x | The mission launched in two thousand one. | The mission launched in 2001. |
| year_2001__take02 | year | 2.9 | 0% | 325 | 0.11x | The mission launched in two thousand one. | The mission launched in 2001. |
| stem_units__take01 | stem | 4.1 | 0% | 312 | 0.08x | Acceleration is nine point eight one meters per second squar | Acceleration is 9.81 meters per second squared. |
| stem_units__take02 | stem | 5.6 | 0% | 316 | 0.06x | Acceleration is nine point eight one meters per second squar | Acceleration is 9.81 meters per second squared. |
| timezone__take01 | time | 2.8 | 0% | 296 | 0.11x | Deadline is seventeen thirty UTC. | Deadline is 1730 UTC. |
| timezone__take02 | time | 2.7 | 0% | 351 | 0.13x | Deadline is seventeen thirty UTC. | Deadline is 1730 UTC. |
| date_iso__take01 | date | 4.8 | 0% | 350 | 0.07x | The due date is February twenty sixth twenty twenty six. | The due date is 2026-0226. |
| date_iso__take02 | date | 4.0 | 0% | 307 | 0.08x | The due date is February twenty sixth twenty twenty six. | The due date is 2026-0226. |
| time_24h__take01 | time | 4.0 | 0% | 302 | 0.08x | Maintenance starts at fifteen forty five. | Maintenance starts at 1545. |
| year_1905__take02 | year | 3.5 | 0% | 311 | 0.09x | The building was completed in nineteen oh five. | The building was completed in 1905. |
| currency_and_percent__take01 | numeric | 7.0 | 0% | 351 | 0.05x | Revenue grew by twelve point five percent to four point two  | Revenue grew by 12.5% to $4.2 million. |
| currency_and_percent__take02 | numeric | 5.8 | 0% | 325 | 0.06x | Revenue grew by twelve point five percent to four point two  | Revenue grew by 12.5% to $4.2 million. |
| stem_scientific_notation__take01 | stem | 5.0 | 0% | 349 | 0.07x | The concentration is three point two times ten to the minus  | The concentration is 3.2 times 10 to the power of negative 5 |
| stem_scientific_notation__take02 | stem | 5.1 | 0% | 360 | 0.07x | The concentration is three point two times ten to the minus  | The concentration is 3.2 times 10 to the power of negative 5 |
| stem_expression__take01 | stem | 4.1 | 0% | 339 | 0.08x | Solve x two plus y two equals z two. | Solve x squared plus y squared equals z squared. |
| tool_current_time__take01 | tool_time | 2.8 | 0% | 338 | 0.12x | What time is it right now? | What time is it right now? |
| tool_current_time__take02 | tool_time | 2.8 | 0% | 324 | 0.12x | What time is it right now? | What time is it right now? |
| tool_current_date__take01 | tool_date | 3.2 | 0% | 312 | 0.10x | What is today's date? | What is today's date? |
| tool_current_date__take02 | tool_date | 2.1 | 0% | 343 | 0.17x | What is today's date? | What is today's date? |
| tool_math_divide__take01 | tool_calculator | 3.8 | 0% | 309 | 0.08x | What is 144 divided by 12? | What is 144 divided by 12? |
| tool_math_divide__take02 | tool_calculator | 3.4 | 0% | 304 | 0.09x | What is 144 divided by 12? | What is 144 divided by 12? |
| tool_math_percent__take01 | tool_calculator | 3.5 | 0% | 318 | 0.09x | What is 15% of 200? | What is 15% of 200? |
| tool_math_percent__take02 | tool_calculator | 3.0 | 0% | 300 | 0.10x | What is 15% of 200? | What is 15% of 200? |
| tool_time_until__take01 | tool_time | 2.3 | 0% | 288 | 0.13x | How long until midnight? | How long until midnight? |
| tool_time_until__take02 | tool_time | 1.9 | 0% | 305 | 0.16x | How long until midnight? | How long until midnight? |
| llm_history_apollo__take01 | llm_history | 5.4 | 0% | 310 | 0.06x | What year did the Apollo 11 moon landing happen? | What year did the Apollo 11 moon landing happen? |
| llm_history_apollo__take02 | llm_history | 4.0 | 0% | 310 | 0.08x | What year did the Apollo 11 moon landing happen? | What year did the Apollo 11 moon landing happen? |
| llm_history_ww2__take01 | llm_history | 2.7 | 0% | 319 | 0.12x | What year did World War II end? | What year did World War II end? |
| llm_history_ww2__take02 | llm_history | 2.6 | 0% | 325 | 0.12x | What year did World War II end? | What year did World War II end? |
| llm_science_formula__take01 | llm_science | 3.0 | 0% | 294 | 0.10x | What is the chemical formula for water? | What is the chemical formula for water? |
| llm_science_formula__take02 | llm_science | 2.4 | 0% | 278 | 0.12x | What is the chemical formula for water? | What is the chemical formula for water? |
| llm_science_speed_of_light__take01 | llm_science | 3.0 | 0% | 301 | 0.10x | What is the speed of light in meters per second? | What is the speed of light in meters per second? |
| llm_science_speed_of_light__take02 | llm_science | 3.0 | 0% | 302 | 0.10x | What is the speed of light in meters per second? | What is the speed of light in meters per second? |
| llm_conversion_seconds__take01 | llm_conversion | 2.5 | 0% | 280 | 0.11x | How many seconds are in an hour? | How many seconds are in an hour? |
| llm_conversion_seconds__take02 | llm_conversion | 2.8 | 0% | 297 | 0.11x | How many seconds are in an hour? | How many seconds are in an hour? |
| llm_acronym_dna__take01 | llm_science | 2.3 | 0% | 292 | 0.13x | What does DNA stand for? | What does DNA stand for? |
| llm_acronym_dna__take02 | llm_science | 2.7 | 0% | 271 | 0.10x | What does DNA stand for? | What does DNA stand for? |

## Pipeline Timing Context

These STT latencies are one stage of the full voice pipeline:

```
TTFA = VAD_ms + STT_ms + LLM_ms + TTS_ms
         ~0ms   ^^^here   see LLM leaderboard
```

Subtract `avg_latency_ms` above from the LLM benchmark's `Avg ms` to see how much of end-to-end latency comes from STT vs inference.
