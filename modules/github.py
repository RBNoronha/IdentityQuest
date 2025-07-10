import requests
import logging

logger = logging.getLogger(__name__)

def search(username: str) -> dict:
    url = f"https://api.github.com/users/{username}"
    
    try:
        logger.info(f"Buscando usuário do GitHub: {username}")
        resp = requests.get(url, timeout=10)
        
        if resp.status_code == 200:
            data = resp.json()
            result = {
                "profile_url": data.get("html_url"),
                "name": data.get("name"),
                "public_repos": data.get("public_repos"),
                "followers": data.get("followers"),
                "created_at": data.get("created_at"),
                "location": data.get("location"),
                "bio": data.get("bio")
            }
            logger.info(f"Usuário encontrado: {username}")
            return result
        elif resp.status_code == 404:
            logger.warning(f"Usuário não encontrado: {username}")
            return {"error": "Usuário não encontrado"}
        else:
            logger.error(f"Erro na API do GitHub: {resp.status_code}")
            return {"error": f"Erro na API: {resp.status_code}"}
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de conexão com GitHub: {str(e)}")
        return {"error": f"Erro de conexão: {str(e)}"}
