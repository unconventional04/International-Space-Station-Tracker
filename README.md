International Space Station Tracker

This project tracks the International Space Station (ISS) in real time and automatically sends an email notification when the station is passing over your location.
It runs every 30 minutes using GitHub Actions, so you don’t need to keep your computer on — everything is automated in the cloud.

Features

Fetches live ISS location data from the Open Notify API.
Checks if the ISS is currently near your location.
Sends you an email alert using Gmail SMTP.
Runs automatically every 30 minutes via GitHub Actions.
Uses GitHub Secrets to securely store credentials.

⚙️ How It Works
The GitHub Action triggers on a schedule (*/30 * * * *).
The workflow installs dependencies and runs main.py.
main.py checks the ISS coordinates against your location.
If the ISS is above you (and it’s dark outside), an email notification is sent.

🔑 Setup
1. Clone the repository
git clone https://github.com/<your-username>/International-Space-Station-Tracker.git
cd International-Space-Station-Tracker
2. Add GitHub Secrets
In your repo, go to:
Settings → Secrets and variables → Actions → New repository secret
Add the following:
EMAIL_USER → your Gmail address
EMAIL_PASS → your 16-character Gmail App Password
TO_EMAIL → (optional) where to send alerts (defaults to your own email)
3. Workflow automation
The workflow file (.github/workflows/main.yml) is already configured to run every 30 minutes. You can also trigger it manually under Actions → Run workflow.
📸 Example Email
Subject: Look up! The ISS is above you 🌌
Body:
The International Space Station is currently passing over your location. Go outside and take a look!

🛠️ Tech Stack
Python 3.11
Requests (API calls)
smtplib (sending emails)
GitHub Actions (automation)

🌍 Why This Project?
I built this as a fun way to combine space science, automation, and Python. Instead of checking manually, I now get automatic alerts whenever the ISS is overhead
