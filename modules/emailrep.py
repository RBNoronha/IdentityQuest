import requests
import logging

logger = logging.getLogger(__name__)

def search(email: str) -> dict:
    """Busca reputação do email no EmailRep.io"""
    try:
        logger.info(f"Consultando EmailRep para: {email}")
        
        url = f"https://emailrep.io/{email}"
        headers = {
            'User-Agent': 'OSINT-Hunter/1.0'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Dados EmailRep encontrados para: {email}")
            return {
                "email": data.get('email'),
                "reputation": data.get('reputation'),
                "suspicious": data.get('suspicious'),
                "references": data.get('references'),
                "details": data.get('details', {}),
                "platform": "EmailRep.io"
            }
        elif response.status_code == 404:
            return {"error": "Email não encontrado na base de dados"}
        else:
            return {"error": f"Erro HTTP: {response.status_code}"}
            
    except Exception as e:
        logger.error(f"Erro ao consultar EmailRep: {str(e)}")
        return {"error": f"Erro de conexão: {str(e)}"}
