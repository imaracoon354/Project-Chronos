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

