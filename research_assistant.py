import json

# ==========================================
# TOOL 1 : WEB SEARCH (MOCK)
# ==========================================
def web_search(query):

    print("\n[Tool Called] web_search()")

    articles = [
        {
            "title": "Solar Energy Growth 2026",
            "summary": "Solar installations are increasing worldwide.",
            "url": "article1"
        },
        {
            "title": "Wind Power Innovation",
            "summary": "New turbines produce more electricity.",
            "url": "article2"
        },
        {
            "title": "Battery Storage Advances",
            "summary": "Battery technology improves renewable energy usage.",
            "url": "article3"
        }
    ]

    return articles


# ==========================================
# TOOL 2 : GET ARTICLE CONTENT
# ==========================================
def get_article_content(url):

    print("[Tool Called] get_article_content()")

    fake_articles = {

        "article1":
        """
        Solar energy capacity is growing rapidly.
        Many countries are investing in solar farms.
        Solar panels are becoming cheaper and more efficient.
        """,

        "article2":
        """
        Wind turbines are becoming larger and smarter.
        Offshore wind farms generate clean electricity.
        AI is improving wind power management.
        """,

        "article3":
        """
        Battery storage helps store renewable energy.
        Lithium-ion batteries are improving.
        Long-duration batteries are becoming popular.
        """
    }

    return fake_articles.get(url, "No Content Found")


# ==========================================
# TOOL 3 : SAVE NOTE
# ==========================================
def save_note(title, content):

    print("[Tool Called] save_note()")

    note = {
        "title": title,
        "content": content
    }

    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except:
        notes = []

    notes.append(note)

    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

    print("Note Saved Successfully!")


# ==========================================
# SIMPLE SUMMARIZER
# ==========================================
def summarize(text):

    sentences = text.strip().split(".")

    summary = ""

    for s in sentences[:3]:
        if s.strip():
            summary += s.strip() + ". "

    return summary


# ==========================================
# RESEARCH ASSISTANT
# ==========================================
def research_assistant(user_request):

    print("\nUser:", user_request)

    # STEP 1 : Search
    articles = web_search(user_request)

    print("\nArticles Found:")

    for article in articles:
        print("-", article["title"])

    # STEP 2 : Read Articles
    combined_text = ""

    for article in articles:

        content = get_article_content(article["url"])

        combined_text += content + "\n"

    # STEP 3 : Summarize
    print("\nGenerating Summary...")

    final_summary = summarize(combined_text)

    print("\nSummary:")
    print(final_summary)

    # STEP 4 : Save
    save_note(
        "Renewable Energy Research",
        final_summary
    )

    print("\nResearch Completed Successfully.")


# ==========================================
# TEST
# ==========================================
research_assistant(
    "Research the latest trends in renewable energy and save a summary."
)