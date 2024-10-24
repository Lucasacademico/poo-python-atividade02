$exclude = @("venv", "poo-bot-atividade02.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "poo-bot-atividade02.zip" -Force