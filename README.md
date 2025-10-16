# Project Chronos: The AI Archeologist
#### Student Name: Vishak Melvin  
#### Student ID: SE25UCSE085

## Project Description
Project Chronos is designed to process hard-to-read text from users, including common internet slang and abbreviations, and convert it into a normal, readable form using Google's Gemini API.

## Setup and Usage

### Initial Setup
>Note the following instructions have been made with a linux terminal in mind.

Ensure python is installed by running the following command in a terminal:
```
python3 --version
```
If not installed, run the following command:
```
sudo apt install python3
```
Also install pip with:
```
sudo apt install python3-pip
```
### Clone the Repository
In the terminal run the following command:
```
git clone https://github.com/imaracoon354/Project-Chronos
```
And then, change to the project directory:
```
cd ./Project-Chronos/
```
### Initialize Virtual Environment
Now to initialize the virtual environment run the following commands:
```
python3 -m venv venv
source venv/bin/activate
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
For the Gemini API Key got to https://aistudio.google.com/app/api-keys and generate a new key.  
For the SerpApi Key go to https://serpapi.com/manage-api-key and register with the free plan to generate a new key.  
(Note:SerpApi is not required but it is needed to provide contextual sources.)

### Running the Script

Finally, to run the script and use the project, enter the command:
```
python3 main.py
```

