import requests
import random
import time
import os 
import unicodedata
from colorama import init, Fore, Style

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear' )
def remover_acentos(texto):
    return ''. join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower().strip()
def generos_f_limpo():
    return {remover_acentos(k): v for k, v in generos_filmes.items()}

def generos_s_limpo():
    return {remover_acentos(k): v for k, v in generos_series.items()}


    




api_chave = 'e5124ceab64077d93f5916293e0f4f92'
url_base = 'https://api.themoviedb.org/3'


generos_filmes = {
    "Ação": 28,
    "Aventura": 12,
    "Animação": 16,
    "Comédia": 35,
    "Crime": 80,
    "Documentário": 99,
    "Drama": 18,
    "Fantasia": 14,
    "Terror": 27,
    "Romance": 10749,
    "Ficção científica": 878,
    "Suspense": 53
}

generos_series = {
    "ação e aventura": 10759,
    "Animação": 16,
    "Comédia": 35,
    "Crime": 80,
    "Documentário": 99,
    "Drama": 18,
    "Família": 10751,
    "Infantil": 10762,
    "Mistério": 9648,
    "Reality": 10764,
    "Ficção científica e fantasia": 10765,
}

def codigo (f_s, gen):
    if f_s == 'filme':
        genero_id = generos_f_limpo().get(gen)
        url = (f'{url_base}/discover/movie')
    elif f_s == 'serie':
        genero_id = generos_s_limpo().get(gen)
        url = (f'{url_base}/discover/tv')
    
    params = {
        'api_key': api_chave,
        'language': 'pt-BR',
        'sort_by': 'popularity.desc',
        'with_genres': genero_id,
        'with_watch_providers': 8,
        'watch_region': 'BR'
    }

    resposta = requests.get(url, params=params)
    dados = resposta.json()
    
    if f_s == 'filme':
        if dados.get('results'):
            escolhido = random.choice(dados['results'])
            título = escolhido.get('title')
            sinopse = escolhido.get('overview')
            avaliacao = escolhido.get('vote_average')
            return escolhido, título, sinopse, avaliacao
        else:
            print(Fore.RED + 'Resultado não encontrado.' + Fore.RESET)
            return None, None, None, None
    else:
        if dados.get('results'):
            escolhido = random.choice(dados['results'])
            título = escolhido.get('name')
            sinopse = escolhido.get('overview')
            avaliacao = escolhido.get('vote_average')
            return escolhido, título, sinopse, avaliacao
        else:
            print(Fore.RED + 'Resultado não encontrado.' + Fore.RESET)
            return None, None, None, None

def repetir(repetiu = False):
    print('='*50)
    print('Olá, usuário. Seja bem-vindo ao \033[1m SorteaFlix \033[0m.\n')
    print('\n   O programa que te salva da indecisão.')
    print('='*50)
    time.sleep(2.5)
    while True:
        f_s = input('\nVocê deseja assistir a um filme ou a uma série? ')
        f_s = remover_acentos(f_s)
        if f_s in ['serie', 'filme']:
            break
        else:
            print(Fore.RED + 'Resposta inválida. Tente novamente. ' + Fore.RESET)
    time.sleep(2.5)
    limpar_tela()
    if f_s == 'filme':
        while True:
            print(',\n'.join(generos_filmes))
            gen = input('\nQual gênero você gostaria de assistir? ')
            gen = remover_acentos(gen)
            if gen in (generos_f_limpo()):
                break
            else:
                print(Fore.RED + 'Resposta inválida. Tente novamente. ' + Fore.RESET)
        time.sleep(1.5)
        limpar_tela()
    else:
        while True:
            print(',\n'.join(generos_series))
            gen = input('\nQual gênero você gostaria de assistir? ')
            gen = remover_acentos(gen)
            if gen in (generos_s_limpo()):
                break
            else:
                print(Fore.RED + 'Resposta inválida. Tente novamente. ' + Fore.RESET)
        time.sleep(1.5)
        limpar_tela()




    escolhido, título, sinopse, avaliacao = codigo(f_s, gen)
    if f_s == 'filme':
        print('='*60)
        print('\nO filme escolhido é: ',  Style.BRIGHT + título + Style.RESET_ALL)
        print('\nSinopse da obra: ', Style.BRIGHT + sinopse + Style.RESET_ALL)
        print('\nAvaliação: ⭐', Style.BRIGHT + str(avaliacao) + Style.RESET_ALL )
        print('='*60)

    else:
        print('='*100)
        print('A série escolhida é: ',  Style.BRIGHT + título + Style.RESET_ALL)
        print('\n \nSinopse da obra: ', Style.BRIGHT + sinopse + Style.RESET_ALL)
        print('\n \nAvaliação: ⭐', Style.BRIGHT + str(avaliacao) + Style.RESET_ALL )
        print('='*100)
    if f_s == 'filme':
        while True:
            a = input ('\n Usuário, você ficou satisfeito com o filme sorteado?\n a)Sim\n b)Não\n')
            a = remover_acentos(a)
            if a in ['a', 'b']:
                break
            else: 
                print(Fore.RED + 'Resposta inválida. Tente novamente. ' + Fore.RESET)
        if a == 'a':
            print(f'Que bom que gostou. Espero que se divirta! {título} é realmente um filme muito bom.')
        else:
            if not repetiu:
                print('Que pena que não gostou. Entretanto você terá o direito de realizar mais um sorteio.')
                time.sleep(2.5)
                limpar_tela()
                repetir(repetiu=True)
            else: 
                 print('Você já usou sua segunda chance. Aproveite o filme!')
    else:
        while True:
            a = input ('\n Usuário, você ficou satisfeito com a série sorteada?\n a)Sim\n b)Não\n')
            a = remover_acentos(a)
            if a in ['a', 'b']:
                break
            else: 
                print(Fore.RED + 'Resposta inválida. Tente novamente. ' + Fore.RESET)
        if a == 'a':
            print(f'Que bom que gostou. Espero que se divirta! {título} é realmente uma série muito boa.')
        else:
            if not repetiu:
                print('Que pena que não gostou. Entretanto você terá o direito de realizar mais um sorteio.')
                time.sleep(2.5)
                limpar_tela()
                repetir(repetiu=True)
            else: 
                 print('Você já usou sua segunda chance. Aproveite a série!')

repetir()
print('\nMuito obrigado por usar o nosso programa. Esperamos que tenhamos te ajudado! Até a próxima.')



