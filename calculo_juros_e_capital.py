import requests


def calculo_juros_e_capital():
    """
    Programa simples para calcular juros em capital.
    :return:
    """
    global cambio_eur_brl
    while True:
        print(f"{'=' * 80}")
        print(f"SIMULAÇÕES DE APLICAÇÕES FINANCEIRAS".center(80))
        print(f"{'=' * 80}")
        try:
            capital = float(input("Entre com o valor da aplicação R$: "))
            n = int(input("Qual o prazo da aplicação (em meses): "))
            r = float(input("Entre o valor da taxa (em %) aplicada (ao mês): "))
            print('')

            # URL oficial baseada em GitHub Pages (atualizada diariamente)
            url = "https://latest.currency-api.pages.dev/v1/currencies/eur.json"

            # Cabeçalhos simulando um navegador real (Evita bloqueios de bots)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9"
            }

            try:
                # Passamos os cabeçalhos diretamente no argumento 'headers'
                response = requests.get(url, headers=headers, timeout=10)

                # Valida se o servidor aceitou a requisição (Código 200 OK)
                if response.status_code == 200:
                    data = response.json()
                    cambio_eur_brl = data["eur"]["brl"]

                    print(f"Câmbio Atual (GitHub API): 1 EUR = {cambio_eur_brl:.2f} BRL")

                    formula = capital * (1 + (r / 100)) ** n

                    juros = formula - capital

                    print(f"Você ganhará de juros R$ {juros:.2f} em {n} mese(s) à uma taxa de {r}% a.m")
                    print(f"Este valor é equivalente há {(juros / cambio_eur_brl):.2f} \u20ac")
                    print('')

                else:
                    print(f"❌ O servidor rejeitou com o status HTTP: {response.status_code}")

            except Exception as e:
                print(f"❌ Erro de conexão: {e}")

        except EOFError:
            break


if __name__ == '__main__':
    calculo_juros_e_capital()
