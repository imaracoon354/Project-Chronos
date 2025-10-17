# Project Chronos: The AI Archeologist
#### Student Name: Vishak Melvin  
#### Student ID: SE25UCSE085

## Project Description
Project Chronos is designed to process hard-to-read text from users, including common internet slang and abbreviations, and convert it into a normal, readable form using Google's Gemini API and searches the web using SerpApi to provide contextual sources.

## Setup and Usage

### Initial Setup

Ensure python is installed by running the following command in a terminal:
> In some Linux Distros you may need to use python3 instead of python.
```
python --version
```
If not installed, run the following command to install both python and pip:
```
sudo apt install python3 python3-pip
```
For Windows, install python from https://www.python.org/downloads  
and install pip by following this guide https://www.geeksforgeeks.org/installation-guide/how-to-install-pip-on-windows.
### Clone the Repository
If Git is not already installed, you can install it from here https://git-scm.com/downloads.  
In the terminal run the following command:
```
git clone https://github.com/imaracoon354/Project-Chronos
```
And then, change to the project directory:
```
cd Project-Chronos
```
### Initialize Virtual Environment
Now to initialize the virtual environment run the following commands:
```
python -m venv venv
```
and then to activate the environment:  
For Linux,
```
source venv/bin/activate
```
For Windows,
```
.\venv\Scripts\activate
```
If all steps were done correctly your terminal should look like this:
```
(venv) yourname@yourpc:~/Project-Chronos$
```
### Install Required Libraries
Inside the virtual environment run the following command:
```
pip install -r requirements.txt
```
### Setting up API Keys
In the same folder create a .env file and then paste in the following:
```
GEMINI_API_KEY=yourkey
SERPAPI_KEY=yourkey
```
For the Gemini API Key go to https://aistudio.google.com/app/api-keys and generate a new key.  
For the SerpApi Key go to https://serpapi.com/manage-api-key and register with the free plan to generate a new key.  
(Note: SerpApi is not required but it is needed to provide contextual sources.)

### Running the Script

Finally, to run the script and use the project, enter the command:
```
python main.py
```
## Example Report
```
(venv) PS C:\Users\visha\Project-Chronos> python main.py
Enter the fragmented text: "smh at the top 8 drama. ppl need to chill. g2g, ttyl."
Project Chronos: The AI Archeologist
==================================================

Analyzing fragment: "smh at the top 8 drama. ppl need to chill. g2g, ttyl."

Step 1: Initializing Gemini AI...
Step 2: Reconstructing text with AI...
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1760723305.508452   15828 alts_credentials.cc:93] ALTS creds ignored. Not running on GCP and untrusted ALTS is not enabled.
Reconstruction complete.

Step 3: Searching web for contextual sources...
   Identified slang terms: smh, ppl, g2g, ttyl
   Searching: smh meaning internet slang
   Searching: ppl meaning internet slang
   Searching: g2g meaning internet slang
   Searching: ttyl meaning internet slang
Found 5 relevant sources.

Step 4: Generating reconstruction report...

--- RECONSTRUCTION REPORT ---

[Original Fragment]
> ""smh at the top 8 drama. ppl need to chill. g2g, ttyl.""

[AI-Reconstructed Text]
> "Shaking my head at the drama surrounding the Top 8 friends list on MySpace, people need to relax. I have to go; talk to you later."

[Contextual Sources]
* https://www.merriam-webster.com/wordplay/what-does-smh-mean-shaking-my-head
* https://www.usatoday.com/story/tech/2022/12/29/smh-meaning-definition-smh-acronym-and-examples-conversation/10927122002/
* https://www.mmguardian.com/teen-slang/ppl?srsltid=AfmBOoqVwt3bOH_TEFAknRzyNWDmrNVMJqUPONHeEr-ZxzSP2KB1-Pe1
* https://www.airdroid.com/teen-slang/ppl-meaning/
* https://en.wiktionary.org/wiki/G2G


Report saved to 'reconstruction_report.txt'
```

