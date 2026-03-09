Video Downloader Bot for Telegram

This is a Python-based Telegram bot designed to download short videos from TikTok and Instagram. It is optimized to run on GitHub Actions, providing a cost-free hosting solution.
Features

    Download videos from TikTok and Instagram.

    Automatic quality selection (best quality under 50MB).

    Hosted via GitHub Actions (no local server required).

    Clean and direct user interface.

Technologies Used

    Python 3.10

    pyTelegramBotAPI

    yt-dlp

    FFmpeg (for video processing)

Setup and Installation
1. Bot Token

Obtain a bot token from @BotFather on Telegram.
2. GitHub Secrets

To keep your token secure, do not hardcode it. Add it to your GitHub Repository:

    Go to Settings > Secrets and variables > Actions.

    Click New repository secret.

    Name: TELEGRAM_TOKEN

    Value: Your bot token.

3. Deployment

The bot is configured to run via GitHub Actions.

    Go to the Actions tab in your repository.

    Select Telegram Bot Runner.

    Click Run workflow.

Bot Baixador de Vídeos para Telegram

Este é um bot para Telegram desenvolvido em Python, projetado para baixar vídeos curtos do TikTok e Instagram. Ele foi otimizado para rodar no GitHub Actions, oferecendo uma solução de hospedagem gratuita.
Funcionalidades

    Download de vídeos do TikTok e Instagram.

    Seleção automática de qualidade (melhor qualidade abaixo de 50MB).

    Hospedado via GitHub Actions (não requer servidor local).

    Interface de usuário limpa e direta.

Tecnologias Utilizadas

    Python 3.10

    pyTelegramBotAPI

    yt-dlp

    FFmpeg (para processamento de vídeo)

Configuração e Instalação
1. Token do Bot

Obtenha um token de bot com o @BotFather no Telegram.
2. GitHub Secrets

Para manter seu token seguro, não o coloque diretamente no código. Adicione-o ao seu repositório no GitHub:

    Vá em Settings > Secrets and variables > Actions.

    Clique em New repository secret.

    Nome: TELEGRAM_TOKEN

    Valor: O token do seu bot.

3. Implantação (Deploy)

O bot está configurado para rodar via GitHub Actions.

    Vá para a aba Actions no seu repositório.

    Selecione Telegram Bot Runner.

    Clique em Run workflow.
