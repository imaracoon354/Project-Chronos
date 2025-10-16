import os
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def reconstruct_text(fragment):
    """Ask Gemini to reconstruct the text fragment."""
    prompt = f"Reconstruct this old or fragmented internet text into a full modern English version:\n\n'{fragment}'"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def search_context(query):
    """Use SerpAPI to get relevant Google search links."""
    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    links = [r["link"] for r in results.get("organic_results", [])[:5]]
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

