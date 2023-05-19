from uuid import uuid4
from utils import remove_html_tags


def transform_data(data: list[dict]) -> dict[list]:
    ids = [str(uuid4()) for _ in range(len(data))]
    texts = []
    metadatas = []

    for entry in data:
        title = entry["title"]
        body = entry["body"]
        url = str(entry["url"])

        metadata = {"id": entry["id"], "source": url, "title": title}

        if body:
            # Add title to the page_content where it is missing
            enriched_body = (
                f"{body} {url}"
                if title.lower() in body.lower()
                else f"{title} {body} {url}"
            )
            cleaned_body = remove_html_tags(enriched_body)

            # Delete "meaningless" content
            phrases_to_delete = [
                "\nPlease make sure to always refer to our Acceptable Use Policy for Messaging."
            ]
            for phrase in phrases_to_delete:
                cleaned_body = cleaned_body.replace(phrase, "")

            text = remove_html_tags(cleaned_body).strip()
        texts.append(text)
        metadatas.append(metadata)

    transformed_data = {"ids": ids, "texts": texts, "metadatas": metadatas}

    return transformed_data
