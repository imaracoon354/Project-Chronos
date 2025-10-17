import os
import sys
import google.generativeai as genai
import requests
from urllib.parse import quote_plus
import time
from dotenv import load_dotenv

load_dotenv()

def setup_gemini():
    """Initialize Gemini API with API key from environment variable."""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        print("create a .env file with GEMINI_API_KEY=your_api_key")
        sys.exit(1)
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

def reconstruct_text(model, fragment):
    """Use Gemini to reconstruct fragmented text with full context."""
    prompt = f"""You are an expert in historical internet slang and platform culture. When given a short informal message, deeply decode abbreviations, slang, shorthand, and platform-specific phrases into fluent, grammatical English that preserves the original tone. Where a phrase references an era-specific or platform-specific phenomenon, explicitly link it to the likely platform and historical context in a brief, natural clause. Output only the reconstructed sentence(s). Example conversions:
- Input: "smh at the top 8 drama. ppl need to chill. g2g, ttyl."
Output: "Shaking my head at the drama surrounding the Top 8 friends list on MySpace, people need to relax. I have to go; talk to you later."
- Input: "brb, updating my away msg — u can leave a msg plz."
Output: "Be right back, I’m updating my AIM away message — you can leave a message please."
Provide ONLY the reconstructed text without any explanations or additional commentary
Now convert the following input:"{fragment}"""


    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None

def identify_slang_terms(model, fragment):
    """Use Gemini to identify slang/abbreviations in the fragment."""
    prompt = (
        f"Identify all internet slang, abbreviations, or jargon in the following text.Also do not include normal words if used in a normal context "
        f"Return ONLY a comma-separated list of the terms (no explanations):\n\n{fragment}"
    )
    try:
        response = model.generate_content(prompt)
        terms = response.text.strip()
        # Split by comma and clean up whitespace
        return [t.strip().lower() for t in terms.split(",") if t.strip()]
    except Exception as e:
        print(f"Error identifying slang terms: {e}")
        return []

def google_search(query, num_results=5):
    # Method 2: Try SerpAPI (free tier available)
    serpapi_key = os.getenv('SERPAPI_KEY')
    if serpapi_key:
        try:
            search_url = f"https://serpapi.com/search.json?q={quote_plus(query)}&api_key={serpapi_key}"
            response = requests.get(search_url, timeout=10)
            if response.status_code == 200:
                results = response.json().get('organic_results', [])
                return [r['link'] for r in results[:num_results]]
        except Exception as e:
            print(f"SerpAPI search failed: {e}")
    
    # Method 3: Return curated sources based on common internet slang
    return get_fallback_sources(query)

def get_fallback_sources(query):
    """Return relevant fallback sources for common internet terms."""
    fallback_dict = {
        'smh': 'https://www.dictionary.com/e/slang/smh/',
        'tbh': 'https://www.dictionary.com/e/slang/tbh/',
        'imo': 'https://www.dictionary.com/e/slang/imo/',
        'imho': 'https://www.dictionary.com/e/slang/imho/',
        'brb': 'https://www.merriam-webster.com/dictionary/BRB',
        'afk': 'https://www.merriam-webster.com/dictionary/AFK',
        'g2g': 'https://www.urbandictionary.com/define.php?term=g2g',
        'ttyl': 'https://www.merriam-webster.com/dictionary/TTYL',
        'lol': 'https://www.merriam-webster.com/dictionary/LOL',
        'rofl': 'https://www.merriam-webster.com/dictionary/ROFL',
        'btw': 'https://www.merriam-webster.com/dictionary/BTW',
        'fyi': 'https://www.merriam-webster.com/dictionary/FYI',
        'myspace': 'https://en.wikipedia.org/wiki/Myspace',
        'top 8': 'https://en.wikipedia.org/wiki/Myspace#Features',
        'aim': 'https://en.wikipedia.org/wiki/AIM_(software)',
        'away message': 'https://en.wikipedia.org/wiki/AIM_(software)',
        'gg': 'https://www.dictionary.com/e/slang/gg/',
        'wp': 'https://gaming.stackexchange.com/questions/tagged/terminology',
        'ppl': 'https://www.dictionary.com/browse/ppl',
    }
    
    sources = []
    query_lower = query.lower()
    
    for term, url in fallback_dict.items():
        if term in query_lower:
            sources.append(url)
    
    # Add general resources
    if 'slang' in query_lower or 'internet' in query_lower:
        sources.append('https://en.wikipedia.org/wiki/Internet_slang')
    
    return sources

def search_context(fragment, reconstructed, model):
    """Perform web searches to find contextual sources."""
    sources = []
    search_terms = identify_slang_terms(model,fragment)
    
    print(f"   Identified slang terms: {', '.join(search_terms)}")
    
    # Search for each term
    for term in search_terms[:5]:  # Limit to 5 terms
        query = f"{term} meaning internet slang"
        print(f"   Searching: {query}")
        
        results = google_search(query, num_results=2)
        sources.extend(results)
        
        time.sleep(0.5)  # Be polite with requests
    
    # Add general internet slang reference
    if not sources:
        sources = [
            'https://www.dictionary.com/e/slang/',
            'https://en.wikipedia.org/wiki/Internet_slang',
            'https://www.urbandictionary.com/'
        ]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_sources = []
    for source in sources:
        if source not in seen:
            seen.add(source)
            unique_sources.append(source)
    
    return unique_sources[:5]  # Return top 5

def generate_report(fragment, reconstructed, sources):
    """Generate the final reconstruction report."""
    report = "--- RECONSTRUCTION REPORT ---\n\n"
    report += "[Original Fragment]\n"
    report += f'> "{fragment}"\n\n'
    report += "[AI-Reconstructed Text]\n"
    report += f'> "{reconstructed}"\n\n'
    report += "[Contextual Sources]\n"
    
    sources = [s for s in sources if s]

    if sources:
        for source in sources:
            report += f"* {source}\n"
    else:
        report += "* No sources found\n"
    
    return report

def main():
    """Main function to run Project Chronos."""
    if len(sys.argv) < 2:
        fragment = input("Enter the fragmented text: ").strip()
        if not fragment:
            print("No input provided. Exiting.")
            sys.exit(1)
    else:
        fragment = sys.argv[1]
    
    print("Project Chronos: The AI Archeologist")
    print("=" * 50)
    print(f"\nAnalyzing fragment: {fragment}\n")
    
    # Step 1: Setup Gemini
    print("Step 1: Initializing Gemini AI...")
    model = setup_gemini()
    
    # Step 2: Reconstruct text
    print("Step 2: Reconstructing text with AI...")
    reconstructed = reconstruct_text(model, fragment)
    
    if not reconstructed:
        print("Failed to reconstruct text. Exiting.")
        sys.exit(1)
    
    print(f"Reconstruction complete.\n")
    
    # Step 3: Search for context
    print("Step 3: Searching web for contextual sources...")
    sources = search_context(fragment, reconstructed, model)
    print(f"Found {len(sources)} relevant sources.\n")
    
    # Step 4: Generate report
    print("Step 4: Generating reconstruction report...\n")
    report = generate_report(fragment, reconstructed, sources)
    
    # Output the report
    print(report)
    
    # Optionally save to file
    with open("reconstruction_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("\nReport saved to 'reconstruction_report.txt'")

if __name__ == "__main__":
    main()
