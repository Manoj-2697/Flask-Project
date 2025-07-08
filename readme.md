# Project Structure

```
Flask Project/
│   app.py                # Main script to launch all Flask apps
│   requirements.txt      # Python dependencies
│   runbook.md            # Project instructions
│
├── static/               # Static files (CSS)
│   ├── app1/style.css
│   ├── app2/style.css
│   └── app3/style.css
│
├── templates/            # HTML templates
│   ├── app1/index.html
│   ├── app2/index.html
│   └── app3/index.html
│
└── .github/workflows/cd.yaml  # GitHub Actions workflow for CI/CD
```

# How the Project Works
- The `app.py` script launches three independent Flask web apps, each on a different port (8080, 8081, 8082).
- Each app serves its own HTML and CSS from the corresponding `templates/appX` and `static/appX` folders.
- When you visit `http://localhost:8080`, `:8081`, or `:8082`, you see a unique web page for each app.

# What the GitHub Action Does
- The workflow in `.github/workflows/cd.yaml` is triggered on every push to the `master` branch.
- It is designed to run on a self-hosted Windows runner.
- The workflow checks out the latest code into the `D:/FlaskProject` directory, installs dependencies, and starts the Flask apps.
- This automates deployment after every merge to `master`.

# Prerequisites: Setting Up GitHub Actions Self-Hosted Runner

To enable automated deployment with GitHub Actions, you must set up a self-hosted runner on your Windows machine:

1. Go to your repository on GitHub.
2. Navigate to **Settings > Actions > Runners** and click **New self-hosted runner**.
3. Choose **Windows** as the operating system.
4. Follow the instructions to download and extract the runner, for example:
   ```powershell
   mkdir C:\actions-runner
   cd C:\actions-runner
   Invoke-WebRequest -Uri https://github.com/actions/runner/releases/download/v2.316.0/actions-runner-win-x64-2.316.0.zip -OutFile actions-runner-win-x64-2.316.0.zip
   tar -xf actions-runner-win-x64-2.316.0.zip
   ```
5. Configure the runner (replace URL and TOKEN with your repo's values):
   ```cmd
   config.cmd --url https://github.com/OWNER/REPO --token YOUR_TOKEN
   ```
6. Start the runner:
   ```cmd
   run.cmd
   ```
   Leave this window open while using GitHub Actions.
7. (Optional) To run the runner as a service so it starts automatically:
   ```cmd
   svc install
   svc start
   ```

# How to Start the App Manually
1. Open CMD and navigate to your project directory:
   ```cmd
   cd /d F:\Flask Project
   ```
2. Install dependencies (if not already done):
   ```cmd
   pip install -r requirements.txt
   ```
3. Start the Flask apps:
   ```cmd
   python app.py
   ```
4. Open your browser and visit:
   - http://localhost:8080
   - http://localhost:8081
   - http://localhost:8082

# How to Stop the App Manually
- In the CMD window where the app is running, press `Ctrl+C` to stop all Flask servers.
- If you started the app in the background, use Task Manager to end any `python.exe` processes if needed.

Open CMD and run the app.py file and then copy the host details from command prompt and then paste the details in browser.
