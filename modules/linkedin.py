import requests
import logging

logger = logging.getLogger(__name__)

def search(username: str) -> dict:
    """Busca perfil no LinkedIn"""
    try:
        logger.info(f"Buscando no LinkedIn: {username}")
        
        # LinkedIn tem proteções contra scraping, então fazemos uma busca básica
        url = f"https://www.linkedin.com/in/{username}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        
        if response.status_code == 200:
            logger.info(f"Perfil LinkedIn encontrado: {username}")
            return {
                "profile_url": url,
                "status": "Perfil encontrado",
                "note": "LinkedIn tem proteções anti-bot. Verificação manual recomendada."
            }
        elif response.status_code == 404:
            logger.warning(f"Perfil LinkedIn não encontrado: {username}")
            return {"error": "Perfil não encontrado"}
        else:
            logger.warning(f"LinkedIn retornou status {response.status_code}")
            return {
                "profile_url": url,
                "status": f"Status HTTP: {response.status_code}",
                "note": "Verificação manual recomendada"
            }
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao acessar LinkedIn: {str(e)}")
        return {"error": f"Erro de conexão: {str(e)}"}
