# GitHub Auto Committer PowerShell Script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

$logFile = Join-Path $scriptDir "activity_log.txt"
$now = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$logEntry = "Activity log: $now"

Add-Content -Path $logFile -Value $logEntry
Write-Host "[+] Updated activity_log.txt with: $logEntry" -ForegroundColor Green

git add activity_log.txt
$commitMsg = "chore(activity): update log $now"
git commit -m $commitMsg

Write-Host "[+] Pushing commit to GitHub..." -ForegroundColor Cyan
git push

if ($LASTEXITCODE -eq 0) {
    Write-Host "[+] Successfully pushed commit to GitHub!" -ForegroundColor Green
} else {
    Write-Host "[-] Push failed. Please check your Git remote and credentials." -ForegroundColor Red
}
