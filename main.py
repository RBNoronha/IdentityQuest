
from core.search_dispatcher import run_search
import argparse

def main():
    parser = argparse.ArgumentParser(description="OSINT Hunter - Busca por e-mail ou username")
    parser.add_argument("target", help="E-mail ou nome de usuário")
    parser.add_argument("--output", choices=["json", "csv"], default="json", help="Formato de saída")
    parser.add_argument("--verbose", action="store_true", help="Exibir logs detalhados")
    args = parser.parse_args()

    run_search(args.target, args.output, args.verbose)

if __name__ == "__main__":
    main()
