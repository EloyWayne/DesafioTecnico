from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from .models import Country, Sport, Medal

def fetch_medal_data():
    print("Iniciando o processo de web scraping...")

    # Inicializa o WebDriver do Selenium
    driver = webdriver.Chrome()  # Certifique-se de que o ChromeDriver está configurado corretamente
    driver.get('https://olympics.com/pt/paris-2024/medalhas')
    
    # Aguarde o carregamento da página, se necessário (opcional)
    driver.implicitly_wait(10)  # Espera até 10 segundos para que todos os elementos sejam carregados

    # Pegue o HTML renderizado pela página
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    print("Página carregada com sucesso")
    
    # Extraia os dados usando BeautifulSoup
    countries = soup.find_all('div', class_='country-medal-row')
    print(f"Número de países encontrados: {len(countries)}")

    for country in countries:
        country_name = country.find('span', class_='country-name').text.strip()
        print(f"Processando país: {country_name}")

        gold_medals = int(country.find('span', class_='gold-medal').text.strip())
        silver_medals = int(country.find('span', class_='silver-medal').text.strip())
        bronze_medals = int(country.find('span', class_='bronze-medal').text.strip())

        # Criar ou atualizar o registro no banco de dados
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

        # Extração e associação de esportes e medalhas
        sports = country.find_all('div', class_='sport-medal-row')
        for sport in sports:
            sport_name = sport.find('span', class_='sport-name').text.strip()
            sport_obj, created = Sport.objects.get_or_create(name=sport_name)
            if created:
                print(f"Criando novo registro para o esporte: {sport_name}")
            # Adicione aqui a lógica para associar esporte, país e medalhas
    
    print("Processo de scraping concluído.")
    
    # Fechar o navegador
    driver.quit()

