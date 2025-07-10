# 🔍 IdentityQuest

**IdentityQuest** é uma ferramenta OSINT (Open Source Intelligence) avançada para busca e investigação de identidades digitais em múltiplas plataformas online.

## ✨ Características

- 🌐 **16 Plataformas Suportadas**: GitHub, LinkedIn, Instagram, Twitter, Facebook, TikTok, YouTube, Reddit, Telegram, Pastebin, Keybase, Spotify, Discord, Pinterest, Twitch, Wayback Machine
- 📧 **Busca por Email**: EmailRep, HaveIBeenPwned, Gravatar
- 📊 **Saída Estruturada**: JSON, CSV com formatação colorida
- 🔒 **Logs Detalhados**: Sistema completo de auditoria
- ⚡ **Busca Paralela**: Execução otimizada e rápida
- 🛡️ **Ético e Responsável**: Respeita robots.txt e políticas das APIs

## 🚀 Instalação

```bash
# Clone o repositório
git clone https://github.com/renanbesserra/IdentityQuest.git
cd IdentityQuest

# Instale as dependências
pip install -r requirements.txt

# Configure as pastas necessárias
mkdir -p logs data
```

## 📖 Como Usar

### Busca por Username
```bash
# Busca básica
python3 main.py username

# Busca detalhada
python3 main.py username --verbose

# Salvar em CSV
python3 main.py username --output csv --verbose
```

### Busca por Email
```bash
# Busca por email
python3 main.py usuario@exemplo.com --verbose
```

## 🛡️ Plataformas Suportadas

### Redes Sociais (13 módulos)
- **GitHub** - Dados completos via API oficial
- **LinkedIn** - Verificação de perfis profissionais
- **Instagram** - Detecção de perfis públicos
- **Twitter/X** - Busca de perfis ativos
#- **Facebook** - Verifica
o de páginas públicas
- **TikTok** - Detecção de perfis de criadores
- **YouTube** - Busca de canais
- **Reddit** - Dados completos via API
- **Telegram** - Verificação de canais/usuários
- **Discord** - Busca manual assistida
- **Pinterest** - Perfis de criadores
- **Twitch** - Canais de streaming
- **Spotify** - Perfis públicos de música

### Ferramentas Especializadas (3 módulos)
- **Pastebin** - Busca de conteúdo público
- **Keybase** - Identidades criptográficas
- **Wayback Machine** - Histórico de páginas web

### Email Intelligence (3 módulos)
- **EmailRep** - Reputação e análise de emails
- **HaveIBeenPwned** - Verificação de vazamentos
- **Gravatar** - Perfis vinculados a emails

## 🔒 Considerações Éticas

- ✅ Use apenas para investigações legais e éticas
- ✅ Respeite a privacidade e termos de uso das plataformas
- ✅ Não use para stalking ou assédio
- ✅ Mantenha os dados encontrados de forma segura

## 📝 Licença

Este projeto está sob a licença MIT.

---

**⚠️ Aviso Legal**: Esta ferramenta é destinada apenas para fins educacionais e investigações legais. O uso inadequado é de responsabilidade do usuário.
