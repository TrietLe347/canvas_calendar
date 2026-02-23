from bs4 import BeautifulSoup
import html
import re

def html_to_text(html_content: str) -> str:
    if not html_content:
        return ""
    
    soup = BeautifulSoup(html_content,"html.parser")

    # Remove scripts/styles if any
    for tag in soup(["script","style"]):
        tag.decompose()


    for tag in soup.find_all(["p", "br", "h1", "h2", "h3", "h4", "h5", "h6", "li"]):
        tag.append("\n")

    # Get text with line breaks
    text = soup.get_text()

    # Unesape HTML entities
    text = html.unescape(text)

    # Clean up excessive whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = text.strip()

    return text




