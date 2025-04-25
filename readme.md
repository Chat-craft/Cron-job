Cron Job Service Setup
This project runs a cron job service to fetch data from Google Sheets and Google Docs at regular intervals. The following steps will guide you through setting up the project and running it on your machine.

Prerequisites
Before setting up the project, ensure that you have the following installed:

Python 3.x

Go (1.16 or later)

Git

Google Cloud API credentials for accessing Google Sheets/Docs

Setup Instructions
1. Clone the repository
First, clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Chat-craft/cron-job.git
cd cron-job-service
2. Set up Python Environment
We use a Python virtual environment to isolate dependencies.

Install Python dependencies using pip:

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
Install required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Set up Go Environment
If you're running the Go code as part of this project, follow the steps below to set up your Go environment:

Set a custom GOPATH
Go may try to write to system directories, which can cause access issues. To fix this, set a custom directory for Go's module cache.

powershell
Copy
Edit
$env:GOPATH="C:\Users\Checkout\go"  # Set the GOPATH to a user directory
$env:GOMODULE="C:\Users\Checkout\go\modules"  # Set the GOMODULE directory
Add these environment variables to your PowerShell profile ($PROFILE) to make them persistent:

powershell
Copy
Edit
notepad.exe $PROFILE
Then add the following lines to the profile:

powershell
Copy
Edit
$env:GOPATH="C:\Users\Checkout\go"
$env:GOMODULE="C:\Users\Checkout\go\modules"
Verify Go environment Ensure that the environment variables are set correctly by running:

bash
Copy
Edit
go env
Check if GOPATH points to the directory you've set.

Initialize Go modules If you're using Go modules (which is recommended), initialize the module:

bash
Copy
Edit
go mod init
go mod tidy
4. Set up Google Cloud API Credentials
You need to have valid Google Cloud API credentials to access Google Sheets and Docs. Follow these steps:

Go to the Google Cloud Console.

Create a new project (or use an existing one).

Enable the Google Sheets API and Google Docs API for your project.

Create OAuth 2.0 credentials and download the credentials.json file.

Store the credentials.json file inside the scripts/credentials/ directory.

5. Configure .gitignore
Ensure that sensitive files like credentials.json are not pushed to GitHub by adding them to .gitignore.

Here’s a basic .gitignore for your project:

gitignore
Copy
Edit
# Ignore the entire credentials folder and any files in it
credentials/

# Ignore the specific credentials file in the scripts directory
scripts/credentials/credentials.json

# Ignore the fetch_google_sheets_docs.log log file
fetch_google_sheets_docs.log
6. Run the Cron Job Service
To run the cron job service, execute the following command:

For Python:

bash
Copy
Edit
python fetch_google_sheets_docs.py
For Go:

bash
Copy
Edit
go run cron_job.go
This will start the cron job, which will run every 5 minutes to fetch data from Google Sheets/Docs.