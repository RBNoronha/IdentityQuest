import requests
import logging

logger = logging.getLogger(__name__)

def search(username: str) -> dict:
    """Busca perfil no Telegram"""
    try:
        logger.info(f"Buscando no Telegram: {username}")
        
        # Telegram permite acesso público a alguns perfis
        url = f"https://t.me/{username}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Verifica se é um canal/usuário válido
            if "tgme_page_title" in response.text:
                logger.info(f"Canal/Usuário Telegram encontrado: {username}")
                return {
                    "profile_url": url,
                    "status": "Canal/Usuário encontrado",
                    "platform": "Telegram",
                    "note": "Acesse o link para ver detalhes completos"
                }
            else:
                logger.warning(f"Perfil Telegram não encontrado: {username}")
                return {"error": "Usuário não encontrado"}
        else:
            logger.warning(f"Erro ao acessar Telegram: {response.status_code}")
            return {"error": f"Erro HTTP: {response.status_code}"}
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao acessar Telegram: {str(e)}")
        return {"error": f"Erro de conexão: {str(e)}"}
