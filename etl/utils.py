from bs4 import BeautifulSoup


def remove_html_tags(text: str) -> str:
    soup = BeautifulSoup(text, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")

    return soup.get_text()


def tiktoken_len(text: str, tokenizer):
    tokens = tokenizer.encode(text, disallowed_special=())
    return len(tokens)
