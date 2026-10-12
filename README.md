# Research Assistant (Mock Tool-Calling Demo)

A small, beginner-friendly Python project that shows how a **research assistant** works step by step: it searches for articles, reads them, summarizes the content, and saves the result as a note. All tools are **mocked** (fake data), so it runs fully offline with no API keys and no extra packages.

## What It Does

When you run the script, the assistant performs this pipeline:

1. **Search** – calls `web_search()` and gets a list of articles (mock data).
2. **Read** – calls `get_article_content()` for each article URL.
3. **Summarize** – combines all article text and builds a short summary with `summarize()`.
4. **Save** – calls `save_note()` and stores the summary in `notes.json`.

## Project Structure

```
.
├── research_assistant.py   # Main script (all tools + assistant logic)
├── notes.json              # Created automatically after the first run
└── README.md               # This file
```

## Requirements

- Python 3.8 or newer
- No third-party libraries (only the built-in `json` module is used)

## How to Run

```bash
python3 research_assistant.py
```

### Example Output

```
User: Research the latest trends in renewable energy and save a summary.

[Tool Called] web_search()

Articles Found:
- Solar Energy Growth 2026
- Wind Power Innovation
- Battery Storage Advances
[Tool Called] get_article_content()
[Tool Called] get_article_content()
[Tool Called] get_article_content()

Generating Summary...

Summary:
Solar energy capacity is growing rapidly. Many countries are investing in solar farms. Solar panels are becoming cheaper and more efficient.

[Tool Called] save_note()
Note Saved Successfully!

Research Completed Successfully.
```

### Example `notes.json`

```json
[
    {
        "title": "Renewable Energy Research",
        "content": "Solar energy capacity is growing rapidly. Many countries are investing in solar farms. Solar panels are becoming cheaper and more efficient. "
    }
]
```

Each run **appends** a new note to the file, so the list grows over time.

## The Tools Explained

| Function | Purpose |
|---|---|
| `web_search(query)` | Returns a fixed list of 3 fake articles (title, summary, url). |
| `get_article_content(url)` | Returns fake article text for `article1`, `article2`, `article3`. Unknown URLs return `"No Content Found"`. |
| `save_note(title, content)` | Loads `notes.json` (or starts an empty list), appends the note, and writes it back. |
| `summarize(text)` | Splits text by `.` and keeps the first 3 non-empty sentences. |
| `research_assistant(user_request)` | Runs the full workflow: search → read → summarize → save. |

## Customize It

- **Change the request:** edit the text at the bottom of the file in `research_assistant("...")`.
- **Add more articles:** add entries to the `articles` list in `web_search()` and matching text in `fake_articles` inside `get_article_content()`.
- **Longer summary:** change `sentences[:3]` in `summarize()` to a bigger number, e.g. `sentences[:6]`.

## Known Limitations

- The search is a mock: it ignores the `query` and always returns the same 3 articles.
- The summarizer is simple (first 3 sentences), so it only covers the first article here. It is not real AI summarization.
- `save_note()` uses a bare `except:`, which hides all errors, not just a missing file.

## Ideas for Next Steps

- Replace `web_search()` with a real search API.
- Use a local LLM (for example Ollama with `llama3.2`) inside `summarize()` for real summaries and a fully offline setup.
- Use `requests` and `BeautifulSoup` in `get_article_content()` to read real web pages.
- Wrap the tools in a loop where the model decides which tool to call next (agent-style tool calling).

## License

Free to use for learning and personal projects.
