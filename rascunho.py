import unicodedata
import random
import time
import os 
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def remover_acentos(texto):
    return ''. join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower().strip()

serie_acao = ['Arcane', 'Prison Break', 'The Umbrella Academy', 'Black Summer', 'The Flash']
serie_comedia = ['The Office', 'The Good Place', 'Good Girls', 'Sex Education', 'Suits']
serie_drama = ['Black Mirror', 'Dexter', 'Dark', 'Lost', 'Anne with an E']
serie_romance = ['Gilmore Girls', 'Tudo Bem Não Ser Normal', 'Se A Vida Te Der Tangerinas', 'Outlander', 'As Telefonistas']
serie_suspense = ['House of Cards', 'Narcos', 'Ripley', 'Ozark', 'The Sinner']
serie_terror = ['A Maldição da Residência Hill', 'Locke & Key', 'Kingdom', 'Slasher', 'Black Summer']
animações = ['Rick and Morty', 'Avatar: O Último Mestre do Ar', 'BoJack Horseman', 'Apenas um Show', '(Des)encanto']
animes = ['One Piece', 'Demon Slayer', "Jojo's Bizarre Adventure", 'Dr.Stone', 'Hunter X Hunter']
filme_acao = ['A Profissional', 'De Volta Ao Jogo', 'Hellboy', 'De Volta À Ação', 'Bastardos Inglórios']
filme_comedia = ['Ted', 'Zumbilândia', 'Superbad É Hoje', 'O Mentiroso', 'A Escolha Perfeita']
filme_drama = ['A Baleia', 'A Sociedade da Neve', 'Náufrago', 'Dois Estranhos','A Vida é Bela']
filme_romance = ['Como Se Fosse A Primeira Vez', 'E Se Fosse Verdade', 'Esposa De Mentirinha', 'Ela É Demais Para Mim', 'Encontro Marcado' ]
filme_suspense = ['Código de Conduta', 'As Duas Faces de Um Crime', ' Dragão Vermelho', 'A Lenda do Cavaleiro Sem Cabeça', 'Um Lugar Bem Longe Daqui']
filme_terror = ['Nós', 'O Massacre da Serra Elétrica: O Retorno de Leatherface', 'O Poço', 'Jogos Mortais: Jigsaw', 'Rua do Medo: 1994 - Parte 1']
filme_animações = ['Homem-Aranha no Aranhaverso', 'Hotel Transilvânia', 'Pinóquio por Guilhermo del Toro', 'A Casa Monstro', 'Sonic: O Filme']
filme_anime = ['A Viagem de Chihiro', 'O Castelo Animado', 'Olhos de Gato', 'Minha Querida Oni', 'Pokémon: Mewtwo Contra-ataca - Evolução']
sinopses_series = {
    'Arcane': 'Em meio à tensão entre as cidades rivais de Piltover e Zaun, duas irmãs acabam em lados opostos de um conflito que envolve magia, tecnologia e poder. A série, inspirada no universo de League of Legends, mistura ação eletrizante com uma narrativa profunda e emocional.',
    'Prison Break': 'Quando seu irmão é condenado injustamente à morte, Michael Scofield elabora um plano audacioso para tirá-lo da prisão — desde se deixar prender até tatuar todo o mapa da prisão no próprio corpo.',
    'The Umbrella Academy': 'Uma família disfuncional de irmãos adotivos com superpoderes precisa resolver o mistério da morte do pai e impedir o apocalipse. Humor ácido, ação intensa e muito drama se misturam.',
    'Black Summer': 'Em meio a um apocalipse zumbi, uma mãe é separada da filha e embarca em uma jornada brutal e implacável para reencontrá-la, enfrentando os horrores de um mundo em colapso.',
    'The Flash': 'Barry Allen ganha supervelocidade após um acidente e se torna o Flash, protetor de Central City. Ele enfrenta vilões meta-humanos enquanto tenta desvendar o assassinato da mãe.',
    'The Office': 'Um falso documentário sobre a rotina absurda e hilária dos funcionários da Dunder Mifflin, uma empresa de papel na Pensilvânia. Michael Scott, o gerente excêntrico, lidera as situações mais constrangedoras e engraçadas.',
    'The Good Place': 'Após morrer, Eleanor vai parar no “Lugar Bom”, mas sabe que não merece estar ali. Para se manter, ela tenta se tornar uma pessoa melhor — com ajuda de um professor de ética e muitas reviravoltas filosóficas.',
    'Good Girls': 'Três mães suburbanas enfrentam dificuldades financeiras e decidem roubar um supermercado. O que começa como um pequeno crime vira uma espiral de ações ilegais.',
    'Sex Education': 'Um adolescente socialmente desajeitado e sua mãe terapeuta sexual causam caos quando ele começa a dar conselhos sexuais na escola. A série mistura humor, afeto e importantes lições.',
    'Suits': 'Um jovem brilhante sem diploma em Direito consegue um emprego em um dos maiores escritórios de advocacia de Nova York. Lá, precisa esconder seu segredo enquanto resolve casos complicados com seu mentor.',
    "Black Mirror": "Cada episódio explora um futuro distópico diferente, focado no impacto da tecnologia na sociedade.",
    "Dexter": "Um perito forense de dia e serial killer de criminosos à noite tenta equilibrar sua vida dupla.",
    "Dark": "Em uma pequena cidade alemã, o desaparecimento de crianças revela uma trama complexa de viagens no tempo.",
    "Lost": "Após a queda de um avião em uma ilha misteriosa, os sobreviventes enfrentam fenômenos sobrenaturais.",
    "Anne with an E": "Anne Shirley, uma órfã sonhadora, muda a vida de uma família adotiva e da comunidade ao seu redor.",
    "Gilmore Girls": "Lorelai e sua filha Rory vivem na charmosa Stars Hollow, enfrentando desafios familiares e amorosos.",
    "Tudo Bem Não Ser Normal": "Um cuidador e uma escritora emocionalmente ferida embarcam numa jornada de cura e amor.",
    "Se A Vida Te Der Tangerinas": "Uma história sobre crescimento, amor e laços familiares em uma vila peculiar.",
    "Outlander": "Uma enfermeira da Segunda Guerra Mundial é transportada para a Escócia do século XVIII e vive um amor proibido.",
    "As Telefonistas": "Quatro mulheres na Madrid dos anos 1920 enfrentam desafios enquanto lutam por independência e amor.",
    "House of Cards": "Frank Underwood manipula todos ao seu redor para conquistar o poder político em Washington.",
    "Narcos": "A ascensão e queda de Pablo Escobar e do narcotráfico colombiano.",
    "Ripley": "Um vigarista assume a identidade de um jovem rico que deveria trazer de volta para casa.",
    "Ozark": "Um consultor financeiro se muda com a família para lavar dinheiro para um cartel mexicano.",
    "The Sinner": "Cada temporada foca em um crime e na investigação sobre os motivos por trás dele.",
    "A Maldição da Residência Hill": "Irmãos que cresceram em uma casa assombrada precisam confrontar os traumas do passado.",
    "Locke & Key": "Três irmãos encontram chaves mágicas em uma casa misteriosa após a morte do pai.",
    "Kingdom": "Na Coreia feudal, uma praga transforma pessoas em zumbis e ameaça o reino.",
    "Slasher": "Cada temporada apresenta uma nova história de assassinatos brutais cometidos por um serial killer mascarado.",
    "Rick and Morty": "Um cientista alcoólatra e seu neto vivem aventuras bizarras por múltiplos universos.",
    "Avatar: O Último Mestre do Ar": "Aang deve dominar os quatro elementos para salvar o mundo de uma guerra centenária.",
    "BoJack Horseman": "Um ator decadente, metade homem e metade cavalo, tenta lidar com sua vida falida.",
    "Apenas um Show": "Dois amigos trabalham em um parque e se envolvem em situações surreais e engraçadas.",
    "(Des)encanto": "A princesa Bean, um demônio e um elfo vivem aventuras em um reino medieval mágico.",
    "One Piece": "Luffy reúne uma tripulação para encontrar o lendário tesouro One Piece e se tornar o Rei dos Piratas.",
    "Demon Slayer": "Tanjiro luta contra demônios enquanto busca uma cura para sua irmã.",
    "Jojo's Bizarre Adventure": "Cada geração da família Joestar enfrenta inimigos sobrenaturais em batalhas épicas.",
    "Dr.Stone": "Senku tenta reconstruir a civilização usando ciência após a humanidade ser petrificada.",
    "Hunter X Hunter": "Gon embarca em uma jornada para se tornar um Hunter e encontrar seu pai desaparecido."
}

sinapses_filmes = {
    "A Profissional": "Um assassino profissional relutante se torna tutor de uma menina cuja família foi assassinada, e juntos formam um laço improvável enquanto enfrentam inimigos perigosos.",
    "De Volta Ao Jogo": "John Wick, um ex-assassino de aluguel, retorna ao submundo do crime para se vingar daqueles que destruíram o que restava de sua antiga vida.",
    "Hellboy": "Um demônio criado por humanos luta contra forças ocultas enquanto tenta descobrir seu lugar entre o bem e o mal.",
    "De Volta À Ação": "Um ex-policial precisa enfrentar seu passado criminoso e proteger sua filha em meio a um perigoso esquema.",
    "Bastardos Inglórios": "Durante a Segunda Guerra Mundial, um grupo de soldados judeus americanos planeja assassinar líderes nazistas em uma missão brutal e ousada.",
    
    "Ted": "Um ursinho de pelúcia ganha vida graças ao desejo de infância de um garoto e, anos depois, os dois precisam lidar com a vida adulta — com muito humor e imaturidade.",
    "Zumbilândia": "Em um mundo pós-apocalíptico dominado por zumbis, quatro sobreviventes excêntricos formam uma improvável família enquanto buscam abrigo — e Twinkies.",
    "Superbad É Hoje": "Dois amigos inseparáveis enfrentam uma série de eventos absurdos na tentativa de curtir uma festa inesquecível antes da formatura.",
    "O Mentiroso": "Um advogado que depende da mentira para viver vê sua vida virar de cabeça para baixo quando seu filho deseja que ele só diga a verdade por um dia.",
    "A Escolha Perfeita": "Um grupo de universitárias forma um coral a capella inusitado, buscando vencer competições musicais enquanto criam laços inesperados.",
    
    "A Baleia": "Um professor recluso e obeso tenta se reconectar com sua filha adolescente enquanto enfrenta as consequências de suas escolhas e sua saúde debilitada.",
    "A Sociedade da Neve": "Baseado em uma história real, o filme mostra os sobreviventes de um acidente aéreo nos Andes e seus desesperados esforços para continuar vivos.",
    "Náufrago": "Após um acidente de avião, um executivo precisa aprender a sobreviver sozinho em uma ilha deserta, lidando com a solidão e a esperança de resgate.",
    "Dois Estranhos": "Preso em um loop temporal, um homem tenta chegar em casa, mas revive o mesmo encontro fatal com um policial diversas vezes.",
    "A Vida é Bela": "Durante a Segunda Guerra Mundial, um pai usa o humor e a imaginação para proteger seu filho dos horrores de um campo de concentração nazista.",
    
    "Como Se Fosse A Primeira Vez": "Um homem se apaixona por uma mulher que sofre de perda de memória de curto prazo e precisa reconquistá-la todos os dias.",
    "E Se Fosse Verdade": "Um homem encontra o espírito de uma mulher em seu novo apartamento e os dois embarcam em uma jornada de amor e descobertas do além.",
    "Esposa De Mentirinha": "Um cirurgião plástico convence sua assistente a fingir ser sua ex-esposa para encobrir uma mentira amorosa que saiu do controle.",
    "Ela É Demais Para Mim": "Um homem comum começa a namorar uma mulher incrivelmente atraente, o que causa surpresa — e insegurança — em todos ao redor.",
    "Encontro Marcado": "A Morte assume forma humana e passa a conviver com uma família, enquanto desenvolve sentimentos por uma jovem e reflete sobre a vida.",
    
    "Código de Conduta": "Após perder sua família em um assalto brutal, um homem decide fazer justiça com as próprias mãos, desafiando o sistema jurídico.",
    "As Duas Faces de Um Crime": "Um advogado ambicioso defende um jovem acusado de matar um arcebispo e descobre que há mais camadas nesse caso do que aparenta.",
    "Dragão Vermelho": "Antes de Hannibal Lecter ser capturado, um agente do FBI busca sua ajuda para caçar um novo assassino em série.",
    "A Lenda do Cavaleiro Sem Cabeça": "Um investigador cético chega a uma vila assolada por assassinatos cometidos, supostamente, por um cavaleiro sem cabeça.",
    "Um Lugar Bem Longe Daqui": "Uma jovem criada isolada em um pântano se torna a principal suspeita em um assassinato, enquanto revela segredos do passado.",
    
    "Nós": "Uma família é aterrorizada por seus sósias, revelando um aterrador reflexo da sociedade e segredos ocultos.",
    "O Massacre da Serra Elétrica: O Retorno de Leatherface": "Um grupo de jovens se depara com o assassino Leatherface e precisa lutar para sobreviver à sua fúria sanguinária.",
    "O Poço": "Em uma prisão vertical onde comida é distribuída de cima para baixo, um homem tenta mudar o sistema em meio à brutalidade humana.",
    "Jogos Mortais: Jigsaw": "Corpos começam a aparecer com a assinatura do serial killer Jigsaw, mas ele está morto há anos — ou não?",
    "Rua do Medo: 1994 - Parte 1": "Um grupo de adolescentes descobre que eventos macabros em sua cidade estão ligados a uma maldição de séculos atrás.",
    
    "Homem-Aranha no Aranhaverso": "Miles Morales se torna o Homem-Aranha e encontra versões alternativas de si mesmo de outros universos em uma aventura eletrizante.",
    "Hotel Transilvânia": "Drácula comanda um hotel para monstros, mas sua vida vira de cabeça para baixo quando um humano aparece — e se apaixona por sua filha.",
    "Pinóquio por Guilhermo del Toro": "Uma releitura sombria e emocionante do clássico conto de Pinóquio, com temas de perda, amor e humanidade.",
    "A Casa Monstro": "Três crianças investigam uma casa assustadora que parece estar viva e engolindo tudo que se aproxima.",
    "Sonic: O Filme": "Sonic, um ouriço azul veloz, precisa proteger seu poder de um cientista maligno enquanto tenta se adaptar ao mundo humano.",
    
    "A Viagem de Chihiro": "Chihiro entra em um mundo mágico e precisa encontrar coragem para salvar seus pais e voltar para casa.",
    "O Castelo Animado": "Uma jovem amaldiçoada por uma bruxa encontra abrigo em um castelo mágico que anda e se envolve com seu misterioso dono.",
    "Olhos de Gato": "Uma adolescente descobre um mundo onde pode se transformar em gata, mas o preço da transformação pode ser alto demais.",
    "Minha Querida Oni": "Um adolescente embarca em uma jornada ao mundo dos espíritos para compreender suas emoções e lidar com a perda.",
    "Pokémon: Mewtwo Contra-ataca - Evolução": "Mewtwo, um Pokémon criado artificialmente, busca vingança contra seus criadores, desafiando o próprio conceito de identidade."
}

generos = ['Ação', 'Comédia', 'Drama', 'Romance', 'Suspense', 'Terror', 'Animação', 'Anime']
generos1 = [remover_acentos(g.lower()) for g in generos]




nome = input('Olá, usuário. Seja bem vindo(a)! Para começarmos, digite seu nome: ')
while True:
    fil_ser = input('{}, no momento, você deseja assistir a um filme ou a uma série? '.format(nome)).lower().strip()
    fil_ser = remover_acentos(fil_ser)
    if fil_ser in ['filme', 'serie']:
        break
    else:
        print ('Resposta inválida. Tente novamente!')


if fil_ser == 'serie':
    while True:
        ser_gen = input('Certo, agora digite o gênero da série que você deseja assistir: {}\n '.format('; '.join(generos))).lower().strip()
        ser_gen = remover_acentos(ser_gen)
        if ser_gen in generos1:
            break
        else: 
            print ('Resposta inválida. Tente novamente!')

    time.sleep(1.5)
    limpar_tela()
    if ser_gen == 'acao':
        ser_ac_sor = random.choice(serie_acao)
        print('A série selecionada para você hoje é: \033[31m {}\033[0m.'.format(ser_ac_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[ser_ac_sor]))
            print('='*80)
    elif ser_gen == 'comedia':
        ser_co_sor = random.choice(serie_comedia)
        print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_co_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[ser_co_sor]))
            print('='*80)
    elif ser_gen == 'drama':
        ser_dr_sor = random.choice(serie_drama)
        print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_dr_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[ser_dr_sor]))
            print('='*80)
    elif ser_gen == 'suspense':
        ser_sus_sor = random.choice(serie_suspense)
        print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_sus_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[ser_sus_sor]))
            print('='*80)
    elif ser_gen == 'terror':
        ser_ter_sor = random.choice(serie_terror)
        print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_ter_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[ser_ter_sor]))
            print('='*80)
    elif ser_gen == 'animacao':
        ser_anim_sor = random.choice(animações)
        print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_anim_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[ser_anim_sor]))
            print('='*80)
    elif ser_gen == 'anime':
        anime_sor = random.choice(animes)
        print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(anime_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[anime_sor]))
            print('='*80)
    else:
        ser_ro_sor = random.choice(serie_romance)
        print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_ro_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinopses_series[ser_ro_sor]))
            print('='*80)
else:
     while True:
        fil_gen = input('Certo, agora digite o gênero do filme que você deseja assistir: {}\n '.format('; '.join(generos))).lower().strip()
        fil_gen = remover_acentos(fil_gen)
        if fil_gen in generos1:
            break
        else:
            print('Resposta inválida. Tente novamente!')

     time.sleep(1.5)
     limpar_tela()
     if fil_gen == 'acao':
        fil_ac_sor = random.choice(filme_acao)
        print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ac_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_ac_sor]))
            print('='*80)
     elif fil_gen == 'comedia':
        fil_co_sor = random.choice(filme_comedia)
        print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_co_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_co_sor]))
            print('='*80)
     elif fil_gen == 'drama':
        fil_dr_sor = random.choice(filme_drama)
        print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_dr_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_dr_sor]))
            print('='*80)
     elif fil_gen == 'suspense':
         fil_sus_sor = random.choice(filme_suspense)
         print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_sus_sor))
         print('='*80)
         while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
         if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_sus_sor]))
            print('='*80)
     elif fil_gen == 'terror':
         fil_ter_sor = random.choice(filme_terror)
         print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ter_sor))
         print('='*80)
         while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
         if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_ter_sor]))
            print('='*80)
     elif fil_gen == 'animacao':
         fil_animacao_sor = random.choice(filme_animações)
         print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_animacao_sor))
         print('='*80)
         while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
         if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_animacao_sor]))
            print('='*80)
     elif fil_gen == 'anime':
         fil_anime_sor = random.choice(filme_anime)        
         print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_anime_sor)) 
         print('='*80)
         while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
         if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_anime_sor]))
            print('='*80)
     else:
        fil_ro_sor = random.choice(filme_romance)
        print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ro_sor))
        print('='*80)
        while True:
            sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
            if sin in ['a', 'b']:
                break
            else: 
                print('Resposta inválida. Tente novamente!')
        if sin == 'a':
            print('='*80)
            print('{}'.format(sinapses_filmes[fil_ro_sor]))
            print('='*80)
time.sleep(1.5)


while True:
    cont = input('Certo, {}, você gostou da nossa recomendação? (Caso não tenha gostado, nós damos o direito de mais um sorteio).\n a)Sim\n b)Não\n '.format(nome)).lower().strip()
    if cont in ['a', 'b']:
        break
    else:
        print('Resposta inválida. Tente novamente!')

if cont == 'a':
    if fil_ser == 'serie':
        print('Que bom que gostou, {}! Ficamos muito felizes, esperamos que goste e aproveite sua série. Por que não nos conta depois o que achou?'.format(nome))
    else:
        print('Que bom que gostou, {}! Ficamos muito felizes, espero que goste e aproveite seu filme. Por que não nos conta depois o que achou?'.format(nome))
    time.sleep(10)
    limpar_tela()
else:
    print('Que pena que você não gostou. Entretanto, {} nós te daremos mais uma chance para receber outra recomendação hoje.'.format(nome))
time.sleep(2)
limpar_tela()


if fil_ser == 'serie':
    while True:
        fil_ser_2 = input('{}, você ainda procura por séries?\n a)Sim\n b)Não\n '.format(nome)).lower().strip()
        if fil_ser_2 in ['a', 'b']:
            break
        else:
            print('Resposta inválida. Tente novamente!')
    if fil_ser_2 == 'a':
        while True:
            ser_gen = input('Certo, agora digite o gênero da série que você deseja assistir: {}\n '.format('; '.join(generos))).lower().strip()
            ser_gen = remover_acentos(ser_gen)
            if ser_gen in generos1:
                break
            else:
                print('Resposta inválida. Tente novamente!')
        time.sleep(1.5)
        limpar_tela()
        if ser_gen == 'acao':
            ser_ac_sor = random.choice(serie_acao)
            print('A série selecionada para você hoje é: \033[31m {}\033[0m.'.format(ser_ac_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_ac_sor]))
                print('='*80)
        elif ser_gen == 'comedia':
            ser_co_sor = random.choice(serie_comedia)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_co_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_co_sor]))
                print('='*80)
        elif ser_gen == 'drama':
            ser_dr_sor = random.choice(serie_drama)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_dr_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_dr_sor]))
                print('='*80)
        elif ser_gen == 'suspense':
            ser_sus_sor = random.choice(serie_suspense)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_sus_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_sus_sor]))
                print('='*80)
        elif ser_gen == 'terror':
            ser_ter_sor = random.choice(serie_terror)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_ter_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_ter_sor]))
                print('='*80)
        elif ser_gen == 'animacao':
            ser_anim_sor = random.choice(animações)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_anim_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_anim_sor]))
                print('='*80)
        elif ser_gen == 'anime':
            anime_sor = random.choice(animes)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(anime_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[anime_sor]))
                print('='*80)
        else:
            ser_ro_sor = random.choice(serie_romance)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_ro_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_ro_sor]))
                print('='*80)
    else:
        while True:
            fil_gen = input('Certo, agora digite o gênero do filme que você deseja assistir: {}\n '.format('; '.join(generos))).lower().strip()
            fil_gen = remover_acentos(fil_gen)
            if fil_gen in generos1:
                break
            else:
                print('Resposta inválida. Tente novamente!')

        time.sleep(1.5)
        limpar_tela()
        if fil_gen == 'acao':
            fil_ac_sor = random.choice(filme_acao)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ac_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_ac_sor]))
                print('='*80)
        elif fil_gen == 'comedia':
            fil_co_sor = random.choice(filme_comedia)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_co_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_co_sor]))
                print('='*80)
        elif fil_gen == 'drama':
            fil_dr_sor = random.choice(filme_drama)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_dr_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_dr_sor]))
                print('='*80)
        elif fil_gen == 'suspense':
            fil_sus_sor = random.choice(filme_suspense)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_sus_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_sus_sor]))
                print('='*80)
        elif fil_gen == 'terror':
            fil_ter_sor = random.choice(filme_terror)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ter_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_ter_sor]))
                print('='*80)
        elif fil_gen == 'animacao':
            fil_animacao_sor = random.choice(filme_animações)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_animacao_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_animacao_sor]))
                print('='*80)
        elif fil_gen == 'anime':
            fil_anime_sor = random.choice(filme_anime)        
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_anime_sor)) 
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_anime_sor]))
                print('='*80)
        else:
            fil_ro_sor = random.choice(filme_romance)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ro_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse do filme?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinapses_filmes[fil_ro_sor]))
                print('='*80)      

else:
    while True:
        fil_ser_2 = input('{}, você ainda procura por filmes?\n a)Sim\n b)Não\n '.format(nome)).lower().strip()
        if fil_ser_2 in ['a', 'b']:
            break
        else:
            print('Resposta inválida. Tente novamente!')    
    if fil_ser_2 == 'a':
        while True:
            fil_gen = input('Certo, agora digite o gênero do filme que você deseja assistir: {}\n '.format('; '.join(generos))).lower().strip()
            fil_gen = remover_acentos(fil_gen)
            if fil_gen in generos1:
                break
            else:
                 print('Resposta inválida. Tente novamente!') 
        time.sleep(1.5)
        limpar_tela()
        if fil_gen == 'acao':
            fil_ac_sor = random.choice(filme_acao)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ac_sor))
        elif fil_gen == 'comedia':
            fil_co_sor = random.choice(filme_comedia)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_co_sor))
        elif fil_gen == 'drama':
            fil_dr_sor = random.choice(filme_drama)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_dr_sor))
        elif fil_gen == 'suspense':
            fil_sus_sor = random.choice(filme_suspense)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_sus_sor))
        elif fil_gen == 'terror':
            fil_ter_sor = random.choice(filme_terror)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ter_sor))
        elif fil_gen == 'animacao':
            fil_animacao_sor = random.choice(filme_animações)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_animacao_sor))
        elif fil_gen == 'anime':
            fil_anime_sor = random.choice(filme_anime)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_anime_sor))
        else:
            fil_ro_sor = random.choice(filme_romance)
            print('O filme selecionado para você hoje é: \033[31m{}\033[0m.'.format(fil_ro_sor))
    else:
        while True:
            ser_gen = input('Certo, agora digite o gênero da série que você deseja assistir: {}\n '.format('; '.join(generos))).lower().strip()
            ser_gen = remover_acentos(ser_gen)
            if ser_gen in generos1:
                break
            else:
                 print('Resposta inválida. Tente novamente!') 
        time.sleep(1.5)
        limpar_tela()
        if ser_gen == 'acao':
            ser_ac_sor = random.choice(serie_acao)
            print('A série selecionada para você hoje é: \033[31m {}\033[0m.'.format(ser_ac_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_ac_sor]))
                print('='*80)
        elif ser_gen == 'comedia':
            ser_co_sor = random.choice(serie_comedia)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_co_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_co_sor]))
                print('='*80)
        elif ser_gen == 'drama':
            ser_dr_sor = random.choice(serie_drama)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_dr_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_dr_sor]))
                print('='*80)
        elif ser_gen == 'suspense':
            ser_sus_sor = random.choice(serie_suspense)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_sus_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_sus_sor]))
                print('='*80)
        elif ser_gen == 'terror':
            ser_ter_sor = random.choice(serie_terror)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_ter_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_ter_sor]))
                print('='*80)
        elif ser_gen == 'animacao':
            ser_anim_sor = random.choice(animações)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_anim_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_anim_sor]))
                print('='*80)
        elif ser_gen == 'anime':
            anime_sor = random.choice(animes)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(anime_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[anime_sor]))
                print('='*80)
        else:
            ser_ro_sor = random.choice(serie_romance)
            print('A série selecionada para você hoje é: \033[31m{}\033[0m.'.format(ser_ro_sor))
            print('='*80)
            while True:
                sin = input('Você deseja ler uma breve sinapse da série?\n a)Sim\n b)Não\n').lower() .strip()
                if sin in ['a', 'b']:
                    break
                else: 
                    print('Resposta inválida. Tente novamente!')
            if sin == 'a':
                print('='*80)
                print('{}'.format(sinopses_series[ser_ro_sor]))
                print('='*80)

time.sleep(3)
print('{}, espero que você tenha gostado das nossas sugestões. Bom divertimento. Volte sempre e nos dê os feedbacks.'.format(nome))








