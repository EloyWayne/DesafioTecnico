import requests
from bs4 import BeautifulSoup
from .models import Country, Sport, Medal

def fetch_medal_data():
    print("Iniciando o processo de web scraping...")

    # URL da página das Olimpíadas de Paris 2024 (exemplo fictício)
    url = 'https://olympics.com/pt/paris-2024/medalhas'
    
    try:
        # Realiza a requisição HTTP para obter o conteúdo da página
        response = requests.get(url, timeout=60)
        print(f"Requisição feita para {url}, Status Code: {response.status_code}")
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            print("Página carregada com sucesso")
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Exemplo de como você pode encontrar e iterar sobre os dados desejados
            countries = soup.find_all('div', class_='country-medal-row')
            print(f"Número de países encontrados: {len(countries)}")

            for country in countries:
                country_name = country.find('span', class_='country-name').text.strip()
                print(f"Processando país: {country_name}")

                gold_medals = int(country.find('span', class_='gold-medal').text.strip())
                silver_medals = int(country.find('span', class_='silver-medal').text.strip())
                bronze_medals = int(country.find('span', class_='bronze-medal').text.strip())

                # Exemplo: Criar ou atualizar o registro no banco de dados
                country_obj, created = Country.objects.get_or_create(name=country_name)
                if created:
                    print(f"Criando novo registro para o país: {country_name}")
                else:
                    print(f"Atualizando registro existente para o país: {country_name}")

                country_obj.gold = gold_medals
                country_obj.silver = silver_medals
                country_obj.bronze = bronze_medals
                country_obj.save()
                print(f"Medalhas atualizadas para {country_name}: Ouro: {gold_medals}, Prata: {silver_medals}, Bronze: {bronze_medals}")

                # Exemplo de extração e associação de esportes e medalhas (simplificado)
                sports = country.find_all('div', class_='sport-medal-row')
                for sport in sports:
                    sport_name = sport.find('span', class_='sport-name').text.strip()
                    sport_obj, created = Sport.objects.get_or_create(name=sport_name)
                    if created:
                        print(f"Criando novo registro para o esporte: {sport_name}")
                    # Adicione aqui a lógica para associar esporte, país e medalhas
            
            print("Processo de scraping concluído.")
        else:
            print(f"Falha ao recuperar dados: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro durante a requisição: {e}")
