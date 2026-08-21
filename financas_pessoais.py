import requests
from datetime import datetime, timedelta


def financas_pessoais():
    """
    Programa simples para calcular juros em capital.
    :return:
    """
    global cambio_eur_brl
    global cambio_usd_brl
    global preco_fecho
    while True:
        print(f"{'=' * 80}")
        print(f"SIMULAÇÕES DE APLICAÇÕES FINANCEIRAS".center(80))
        print(f"{'=' * 80}")
        try:
            renda_fixa = float(input("Quanto deseja alocar em Renda Fixa R$: "))
            criptomoedas = float(input("Quanto deseja alocar em criptomoeda R$: "))
            n = int(input("Qual o prazo da aplicação (em meses): "))
            r = float(input("Entre o valor da taxa (em %) aplicada (ao mês): "))
            print('')

            try:
                # URL oficial baseada em GitHub Pages (atualizada diariamente)
                url = "https://latest.currency-api.pages.dev/v1/currencies/eur.json"

                # Cabeçalhos simulando um navegador real (Evita bloqueios de bots)
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "Accept": "application/json",
                    "Accept-Language": "en-US,en;q=0.9"
                }

                # Passamos os cabeçalhos diretamente no argumento 'headers'
                response = requests.get(url, headers=headers, timeout=10)

                # Valida se o servidor aceitou a requisição (Código 200 OK)
                if response.status_code == 200:
                    data = response.json()
                    cambio_eur_brl = data["eur"]["brl"]

                    print(f"Câmbio Atual (GitHub API): 1 EUR = {cambio_eur_brl:.2f} BRL")

                    formula = renda_fixa * (1 + (r / 100)) ** n

                    juros = formula - renda_fixa

                    print(f"Você ganhará de juros R$ {juros:.2f} em {n} mese(s) à uma taxa de {r}% a.m")
                    print(f"Este valor é equivalente há {(juros / cambio_eur_brl):.2f} \u20ac")
                    print('')

                else:
                    print(f"❌ O servidor rejeitou com o status HTTP: {response.status_code}")

                try:
                    # URL oficial baseada em GitHub Pages (atualizada diariamente)
                    url = "https://latest.currency-api.pages.dev/v1/currencies/usd.json"

                    # Cabeçalhos simulando um navegador real (Evita bloqueios de bots)
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                        "Accept": "application/json",
                        "Accept-Language": "en-US,en;q=0.9"
                    }

                    # Passamos os cabeçalhos diretamente no argumento 'headers'
                    response = requests.get(url, headers=headers, timeout=10)

                    # Valida se o servidor aceitou a requisição (Código 200 OK)
                    if response.status_code == 200:
                        data = response.json()
                        cambio_usd_brl = data["usd"]["brl"]

                        print(f"Câmbio Atual (GitHub API): 1 DOLAR = {cambio_usd_brl:.2f} BRL")
                        print("")

                    else:
                        print(f"❌ O servidor rejeitou com o status HTTP: {response.status_code}")

                except Exception as e:
                    print(f"❌ Erro de conexão: {e}")
            except Exception as e:
                print(f"❌ Erro de conexão: {e}")

            def buscar_coingecko():
                # API direta da CoinGecko - Estável, gratuita e em tempo real
                url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&x_cg_demo_api_key=CG-FeHufhQ2wcs27AFK8SwPR6EA"

                headers = {
                    "accept": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                }

                try:
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()
                    data = response.json()

                    # Estrutura de resposta direta da CoinGecko
                    usd_price = data["bitcoin"]["usd"]

                    print("Dados em tempo real (CoinGecko):")
                    print(f"Preço do Bitcoin (DOLAR): ${usd_price:,.2f}")

                    bitcoins = (criptomoedas / cambio_usd_brl) / usd_price

                    print(f"Valor da aplicação em criptomoedas (em BTC): {bitcoins:.8f} BTC")

                except requests.exceptions.RequestException as e:
                    print(f"❌ Erro ao conectar na CoinGecko: {e}")

            if __name__ == "__main__":
                buscar_coingecko()

            print("")

        except EOFError:
            break


if __name__ == '__main__':
    financas_pessoais()
