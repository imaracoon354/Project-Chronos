import os
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def reconstruct_text(fragment):
    """Ask Gemini to reconstruct the text fragment."""
    prompt = f"Reconstruct this old or fragmented internet text into a full modern English version:\n\n'{fragment}'"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def search_context(query):
    """Perform a Google search to find relevant context links."""
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    links = []
    for a in soup.select("a[href^='http']"):
        href = a['href']
        if "google" not in href:
            links.append(href)
        if len(links) >= 5:
            break
    return links

def create_report(original, reconstructed, sources):
    """Display the final formatted Reconstruction Report."""
    print("\n--- RECONSTRUCTION REPORT ---")
    print(f"\n[Original Fragment]\n> {original}")
    print(f"\n[AI-Reconstructed Text]\n> {reconstructed}")
    print("\n[Contextual Sources]")
    for src in sources:
        print(f"* {src}")

if __name__ == "__main__":
    fragment = input("Enter the fragmented text: ")
    reconstructed = reconstruct_text(fragment)
    sources = search_context(reconstructed)
    create_report(fragment, reconstructed, sources)

