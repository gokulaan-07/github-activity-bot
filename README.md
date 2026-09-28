# 🚀 GitHub Auto Committer

Automated tools to maintain a consistent daily GitHub commit streak for **[@gokulaan-07](https://github.com/gokulaan-07)**.

---

## 📌 Crucial GitHub Requirements for Heatmap Commits

For GitHub to count commits on your profile contribution grid:
1. **Email Match:** Your local `git config user.email` **must** match an email registered in your [GitHub Account Settings](https://github.com/settings/emails).
2. **Default Branch:** Commits must be made on the repository's default branch (`main` or `master`).
3. **Private Repositories:** If your repository is private, make sure **"Include private contributions on my profile"** is turned **ON** under your [GitHub Profile Settings](https://github.com/settings/profile).

---

## ⚙️ Option 1: GitHub Actions (Server-Side Automated Commits — Recommended)

This option runs directly on GitHub servers daily. **You don't need your PC turned on.**

1. Create a repository on GitHub named `github-activity-bot`.
2. Push this folder to GitHub:
   ```bash
   git init
   git branch -M main
   git add .
   git commit -m "initial commit"
   git remote add origin https://github.com/gokulaan-07/github-activity-bot.git
   git push -u origin main
   ```
3. Enable Workflow Permissions on GitHub:
   - Go to **Repository Settings** > **Actions** > **General**.
   - Under **Workflow permissions**, select **"Read and write permissions"**.
   - Click **Save**.

---

## 🐍 Option 2: Local Python / PowerShell Script

### 1. Configure Git User Email
Run the following in your terminal to ensure commits match your GitHub profile:
```bash
git config --global user.name "gokulaan-07"
git config --global user.email "YOUR_GITHUB_EMAIL@example.com"
```

### 2. Run Manually
- **Python:** `python auto_commit.py`
- **PowerShell:** `.\auto_commit.ps1`

### 3. Schedule Daily Execution on Windows (Task Scheduler)
1. Open **Task Scheduler** in Windows (`Win + R` -> `taskschd.msc`).
2. Click **Create Basic Task...**
3. Name: `GitHub Daily Auto Commit`.
4. Trigger: **Daily** (set preferred time).
5. Action: **Start a program**.
   - Program/script: `python` (or `powershell.exe`)
   - Add arguments: `C:\Users\gokul\.gemini\antigravity\scratch\github-auto-committer\auto_commit.py`
6. Click **Finish**.
