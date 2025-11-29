# GitHub 仓库重命名脚本
# 使用方法：在 PowerShell 中运行此脚本

param(
    [Parameter(Mandatory=$false)]
    [string]$Token
)

$owner = "developmentpeanut"
$oldRepoName = "celltimer"
$newRepoName = "jupyter-cell-runtime"

# 尝试从环境变量或 GitHub CLI 获取 token
if (-not $Token) {
    if ($env:GH_TOKEN) {
        $Token = $env:GH_TOKEN
        Write-Host "从环境变量 GH_TOKEN 获取 token" -ForegroundColor Gray
    } elseif ($env:GITHUB_TOKEN) {
        $Token = $env:GITHUB_TOKEN
        Write-Host "从环境变量 GITHUB_TOKEN 获取 token" -ForegroundColor Gray
    } else {
        # 尝试从 GitHub CLI 配置读取
        $ghConfigPath = "$env:USERPROFILE\.config\gh\hosts.yml"
        if (Test-Path $ghConfigPath) {
            Write-Host "尝试从 GitHub CLI 配置读取 token..." -ForegroundColor Gray
            try {
                $ghToken = & "$env:ProgramFiles\GitHub CLI\gh.exe" auth token 2>$null
                if ($ghToken) {
                    $Token = $ghToken.Trim()
                    Write-Host "从 GitHub CLI 获取 token" -ForegroundColor Gray
                }
            } catch {
                Write-Host "无法从 GitHub CLI 获取 token" -ForegroundColor Yellow
            }
        }
        
        # 如果还是没有 token，提示用户输入
        if (-not $Token) {
            Write-Host "`n需要 GitHub Personal Access Token 来完成重命名操作" -ForegroundColor Yellow
            Write-Host "获取 Token: https://github.com/settings/tokens" -ForegroundColor Cyan
            $secureToken = Read-Host "请输入你的 GitHub Personal Access Token (需要 repo 权限)" -AsSecureString
            $Token = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureToken))
        }
    }
}

Write-Host "`n正在重命名 GitHub 仓库..." -ForegroundColor Yellow
Write-Host "从: $owner/$oldRepoName" -ForegroundColor Gray
Write-Host "到: $owner/$newRepoName" -ForegroundColor Gray

$headers = @{
    "Authorization" = "Bearer $Token"
    "Accept" = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

$body = @{
    name = $newRepoName
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "https://api.github.com/repos/$owner/$oldRepoName" -Method PATCH -Headers $headers -Body $body -ContentType "application/json"
    
    Write-Host "`n✅ 仓库重命名成功！" -ForegroundColor Green
    Write-Host "新仓库名: $($response.name)" -ForegroundColor Green
    Write-Host "新仓库 URL: $($response.html_url)" -ForegroundColor Green
} catch {
    Write-Host "`n❌ 重命名失败：" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    if ($_.ErrorDetails.Message) {
        Write-Host $_.ErrorDetails.Message -ForegroundColor Red
    }
    exit 1
}

