# Welcome to Art Ecommerce LLC

The purpose of this project is to create a website where artists can contact me to make them a professional platform where they can sell their artwork.

## Current Features
- Selected images have their resolution reduced. Then they are turned into Data URI's which are sent to the HTML through the template context. They are recieved on the frontend in a background-image: url(...) to prevent users or browsers from easily downloading them.

## Features(Coming Soon)
- Secure contact form

## Requiremnts:
- Git
- Python virtual enviornment
- PostgreSQL

## .env file secrets

1. **Make sure the .env file is in the root directory. You need the secrets to be filled out. Find the necessary enviornment varibles in the src/artecommercellcapi/config.py**


## How to Set Up Local Environment

1. **Clone the repository**

   ```bash
   git clone https://github.com/Art-Ecommerce-LLC/ArtEcommerceLLC.git
   ```

2. **Open terminal and navigate to the root directory of the repo**

   ```bash
   cd artecommercellc
   ```

3. **Download a python virtual enviornment by running**

   ```bash
   python -m venv .venv
   ```

4. **(Mac OS/Linux) Activate the virtual enviornmnet with**
   ```bash
   source .venv/bin/activate
   ```
   **(Windows 11/10)**
   ```bash
   .venv/scripts/activate
   ```
5. **While in the root directory, make sure (.venv) pops up to the left, bottomost line of text in the terminal. Then run**

   ```bash
   pip install -r requirements.txt
   ```

6. **Now that dependencies are downloaded and you are in the root directory. Run**
   ```
   uvicorn src.app:app **reload
   ```