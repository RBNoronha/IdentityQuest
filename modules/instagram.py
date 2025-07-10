import requests
import logging

logger = logging.getLogger(__name__)

def search(username: str) -> dict:
    """Busca perfil no Instagram"""
    try:
        logger.info(f"Buscando no Instagram: {username}")
        
        url = f"https://www.instagram.com/{username}/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            if 'profilePage_' in response.text or '"username":"' in response.text:
                logger.info(f"Perfil Instagram encontrado: {username}")
                return {
                    "profile_url": url,
                    "status": "Perfil encontrado",
                    "platform": "Instagram",
                    "note": "Verificação manual recomendada"
                }
            else:
                return {"error": "Usuário não encontrado"}
        else:
            return {"error": f"Erro HTTP: {response.status_code}"}
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao acessar Instagram: {str(e)}")
        return {"error": f"Erro de conexão: {str(e)}"}
