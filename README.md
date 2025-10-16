# Initial Setup
ensure python is installed by pasting the following command in a terminal:
```
python3 --version
```
if not paste the following commands:
```
sudo apt install python3
```
also install pip with:
```
sudo apt install python3-pip
```
create a folder for the project with:
```
mkdir project_chronos
cd project_chronos
```
now to initialize a virtual environment paste the following commands:
```
python3 -m venv venv
source venv/bin/activate
```
if all steps were done correctly your terminal should look like this:
```
(venv) yourname@yourpc:~/project_chronos$
```
# install required librarires
inside the virtual environment paste the follwoing command:
```
pip install -r requirements.txt
```
# Setting up API keys
in the same folder create a .env file and then paste in the following:
```
GEMINI_APIKEY=yourkey
SERPAPI_KEY=yourkey
```
for the gemini api key got to https://aistudio.google.com/app/api-keys and generate a new key.
for the serpapi key go to https://serpapi.com/manage-api-key and register with the free plan to generate the api key.
(Note:serpapi is not required but it is needed to provide contexual sources.)

# running the script

finally to actually use the project paste the command:
```
python3 main.py
```

