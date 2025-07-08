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
