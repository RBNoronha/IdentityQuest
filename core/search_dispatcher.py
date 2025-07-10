import logging
from typing import Dict, Any
from modules import (
    github, linkedin, telegram, emailrep, haveibeenpwned,
    instagram, twitter, facebook, tiktok, youtube, reddit,
    gravatar, pastebin, keybase, spotify, discord, pinterest,
    twitch, wayback, whois_search
)
from core.utils import is_email
from core.storage import save_results

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/search.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def format_results(results: Dict[str, Any], target: str, is_email_address: bool) -> None:
    """Formata e exibe os resultados de forma estruturada e legivel"""
    print("\n" + "="*60)
    print("RESULTADOS DA BUSCA OSINT")
    print("="*60)
    print(f"Alvo: {target}")
    print(f"Tipo: {'E-mail' if is_email_address else 'Nome de usuario'}")
    print("-"*60)
    
    for platform, data in results.items():
        print(f"\n{platform.upper()}")
        print("-" * 30)
        
        if isinstance(data, dict):
            if "error" in data:
                print(f"ERRO: {data['error']}")
            elif "info" in data and "stub" in data["info"]:
                print("Modulo ainda nao implementado")
            else:
                for key, value in data.items():
                    if value is not None and value != "":
                        if isinstance(value, list):
                            print(f"  {key.replace('_', ' ').title()}:")
                            for item in value[:3]:  # Limita a 3 itens
                                print(f"    - {item}")
                        else:
                            print(f"  {key.replace('_', ' ').title()}: {value}")
        else:
            print(f"  {data}")
    
    print("\n" + "="*60)

def run_search(target: str, output_format: str = "json", verbose: bool = False):
    logger.info(f"Iniciando busca para: {target}")
    
    is_email_address = is_email(target)
    results = {}

    try:
        if is_email_address:
            logger.info("Detectado como email - executando modulos de email")
            results["emailrep"] = emailrep.search(target)
            results["haveibeenpwned"] = haveibeenpwned.search(target)
            results["gravatar"] = gravatar.search(target)
        else:
            logger.info("Detectado como username - executando modulos de username")
            results["github"] = github.search(target)
            results["linkedin"] = linkedin.search(target)
            results["telegram"] = telegram.search(target)
            results["instagram"] = instagram.search(target)
            results["twitter"] = twitter.search(target)
            results["facebook"] = facebook.search(target)
            results["tiktok"] = tiktok.search(target)
            results["youtube"] = youtube.search(target)
            results["reddit"] = reddit.search(target)
            results["pastebin"] = pastebin.search(target)
            results["keybase"] = keybase.search(target)
            results["spotify"] = spotify.search(target)
            results["discord"] = discord.search(target)
            results["pinterest"] = pinterest.search(target)
            results["twitch"] = twitch.search(target)
            results["wayback"] = wayback.search(target)
            results["whois"] = whois_search.search(target)

        save_results(results, output_format)
        logger.info(f"Resultados salvos em formato {output_format}")

        if verbose:
            format_results(results, target, is_email_address)
        else:
            # Saida resumida quando nao verbose
            print(f"\nBusca concluida para: {target}")
            print(f"Resultados salvos em: data/results.{output_format}")
            
    except Exception as e:
        logger.error(f"Erro durante a busca: {str(e)}")
        raise
