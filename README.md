The purpose of this project is to create a website where artists can contact me to make them a professional platform where they can sell their artwork.


Features(Coming Soon)
* Secure contact form

Requiremnts:
* Git
* Python virtual enviornment
* NocoDB instance

How to set up local enviornment:
* Clone the repository with git clone https://github.com/Art-Ecommerce-LLC/ArtEcommerceLLC.git
* Open terminal and navigate to the main directory of the repo
* Download a python virtual enviornment by running python -m venv .venv
* Activate the virtual enviornmnet with source .venv/bin/activate for Mac OS/Linux and .venv/scripts/activate.bat for Windows
* While in the main directory, make sure (.venv) pops up to the left, bottomost line of text in the terminal
* Run pip install -r requirements.txt
* Now that dependencies are downlaoded and you are in the main directory. Run uvicorn src.app:app --reload to run your instance