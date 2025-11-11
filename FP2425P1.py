
# This is the Python script for your project

def eh_tabuleiro(tab):
    """ Verifica se o/os tuplos passados podem descrever um tabuleiro.
    
        Args:
            arg (universal): Recebe argumento para verificar se este pode descrever um tabuleiro.
            
        Returns:
            Booleano (boolean): verdadeiro caso descreva um tabuleiro, falso caso contrário.
        
    
    
    """
    
    # Verifica se o argumento recebido é um tuplo
    if not isinstance(tab, tuple):
        return False
    
    # Verifica se o número de linhas está entre 2 e 100
    if not (2 <= len(tab) <= 100):
        return False
    
    # Verifica se todas as linhas são tuplos e têm o mesmo número de colunas
    nr_columns = len(tab[0])
    for tup in tab:
        if not isinstance(tup, tuple) or len(tup) != nr_columns:
            return False
        
        # Verifica se os elementos são -1, 0 ou 1
        for element in tup:
            if element not in range(-1, 2):
                return False
    
    return True
    
def eh_posicao(arg):
    """ Recebe um argumento universal e verifica se este pode ser uma posição em um tabuleiro

        Args:
            arg (universal): Recebe um valor universal.
            
        Returns:
            Booleano (boolean): Retorna verdadeiro caso o argumento seja uma posição em um tabuleiro, falso caso contrário
    
    
    """
    # Verifica se o argumento passado é inteiro e maior 0, já que um tabuleiro pode apenas ter posições maiores que 0
    
    if str(arg).isdigit():
        return int(arg) >= 1 and arg <= 10000
    return False
    
def obtem_dimensao(tab):
    """ Recebe um tuplo, verifica se este é um tabuleiro e obtem as dimensões deste (quantas linhas e quantas colunas).
    
        Args:
            tab (tuple): Recebe um tabuleiro em formato de tuplo.
            
        Returns:
            dimensions (tuple): Retorna um tuplo que contem as dimensões do tabuleiro (linhas e colunas).
    
    
    """
    # Verifica se o argumento passado descreve um tabuleiro
    if eh_tabuleiro(tab):
        
        # Obtem as linhas do tabuleiro, corresponde ao número de tuplos dentro do tuplo inicial
        lines = len(tab)
        
        # Obtem o número de colunas do tabuleiro, correspondente ao número de elementos no primeiro tuplo
        # já que para ser tabuleiro todos os tuplos, que correspondem a linhas, devem ter o mesmo número de elementos
        columns = len(tab[0])
        
        # Combina o número de linhas e colunas em um tuplo
        dimensions = (lines, columns)
                
        return dimensions
    
    else:
        # Levanta um erro caso o argumento passado não corresponda a um tabuleiro
        raise ValueError("parâmetros errados")

def obtem_valor(tab, pos):
    """ Recebe um tabuleiro e uma posição e devolve o valor contido nesta posição neste tabuleiro
    
        Args:
            tab (tuple): Recebe um tuplo correspondente a um tabuleiro
            pos (int): Recebe um inteiro correspondente a posição escolhida
            
        Returns:
            value (int): Retorna o valor contido na posição do tabuleiro recebido
    
    """
    # Verifica se o argumento passado descreve um tabuleiro
    if eh_tabuleiro(tab) and eh_posicao(pos):
        row_size = obtem_dimensao(tab)[1]
        
        row = 0
        while pos not in range(1, row_size + 1):
            pos -= row_size
            row += 1
        
        value = tab[row][pos - 1]
        return value
    
    else:
        # Levanta um erro caso o argumento passado não corresponda a um tabuleiro
        raise ValueError("parâmetros errados")

def obtem_coluna(tab, pos):
    """ Recebe um tabuleiro e uma posição e obtém a coluna que contém esta posição
    
        Args:
            tab(tuple): Recebe um tuplo correspondente a um tabuleiro
            pos(int): Recebe um inteiro correspondente a posição escolhida
            
        Returns:
            column_positions(tuple): Retorna um tuplo correspodente às posições contidas na coluna em que se encontra a posição recebida   
    
    
    """

    # Define o tuplo que será retornado pela função
    column_positions = ()
    
    # Obtem o tamanho de cada linha
    row_size = len(tab[0])
    
    # Utiliza um while loop para reduzir a posição recebida para uma que esteja na mesma coluna mas na primeira linha
    while pos > row_size:
        pos -= row_size
    
    # Como a posição reduzida à primeira linha não corresponde ao seu index mas sim à sua posição no tabuleiro, para corresponder 
    # à um index deve-se retirar 1 desta coluna, valor que é então atribuido à variável column
    column = pos - 1
    
    # Define multiplier, que é utilizado para adicionar à posição o número de posições contidos em cada linha, de modo que seja possível
    # obter o valor contido na mesma coluna porém na linha seguinte, em relação à posição anterior ou incial
    multiplier = 0
    
    # Utiliza um for loop para obter posições da coluna, passando para a linha seguinte a cada loop
    for row in tab:
        column_positions = column_positions + (pos + multiplier*row_size,)
        multiplier += 1
        
    return column_positions

def obtem_linha(tab, pos):
    """Recebe um tabuleiro e uma posição e retorna a linha em que esta posição se encontra no tabuleiro
    
        Args:
            tab(tuple): Tuplo que corresponde a um tabuleiro
            pos(int): Inteiro que corresponde a uma posição
            
        Returns:
            row_positions(tuple): Tuplo com as posições contidas na linha da posição recebida
    
    
    """
        
    # Define a variável row_size que contem o número de elementos de cada linha do tabuleiro
    row_size = len(tab[0])
    
    # Obtem um float, cuja parte inteira corresponde às linhas completas, as quais a posição não pertence
    row_number = (pos - 1) // row_size
    
    column_index = 1
    row_positions = ()
    
    # For loop para obter a posição de cada elemento da linha em que se encontra a posição recebida
    for element in tab[row_number]:
        posicao = column_index +  row_number * row_size
        
        #Adiciona a posição no tuplo que será retornado
        row_positions += (posicao,)
        
        # Adiciona um à coluna (ou indice) para a próxima posição poder ser obtida
        column_index += 1
        
    return row_positions

    
def obtem_diagonais(tab, pos):
    """ Obtem um tuplo de diagonais que contem uma posição.
    
        Args:
            tab (tuplo): Tabuleiro para checar diagonais
            pos (int): Posicao para verificar as diagonais que passam por ela
            
        Returns:
            diagonais(tuplo): Tuplo com a diagonal e a antidiagonal que contem a posicao recebida
        
    
    
    """
    
    # Obtem tamanho da linha
    row_size = obtem_dimensao(tab)[1]
    diagonal = ()
    antidiagonal = ()
        
    row = 0
    # Obtem o index da posição
    while pos not in range(1, row_size + 1):
        pos -= row_size
        row += 1
    
    index = pos - 1
    
    # Obtem qual é a menor distancia para as bordas do tabuleiro (começo da linha ou começo da coluna)
    minimum = min(index, row)
    
    # Obtem o index e a linha da primeira posição do tuplo da diagonal
    diagonal_index_start = index - minimum
    diagonal_row_start = row - minimum
    
    # Obtem a posicao em que começa a diagonal
    pos = diagonal_row_start * row_size + diagonal_index_start + 1
    
    # Obtem todas as posições na diagonal
    while diagonal_row_start < len(tab):
        if diagonal_index_start <= row_size - 1:
            diagonal += (pos,)
            pos += row_size + 1
            diagonal_index_start += 1
        diagonal_row_start += 1
    
    # Obtem qual é a menor distancia para as bordas do tabuleiro (começo da linha ou começo da coluna)
    minimum = min(row_size - 1 - index, (row))
    
    # Obtem o index e a linha da primeira posição do tuplo da antidiagonal
    antidiagonal_index_start = index + minimum
    antidiagonal_row_start = row - minimum
    
    # Obtem a posicao em que começa a diagonal
    pos = antidiagonal_row_start * row_size + antidiagonal_index_start + 1

    # Obtem todas as posições na diagonal
    while antidiagonal_row_start < len(tab):
        if antidiagonal_index_start >= 0:
            antidiagonal += (pos,)
            pos += row_size - 1
            antidiagonal_index_start -= 1
        antidiagonal_row_start += 1
        
    diagonais = (tuple(sorted(diagonal)), tuple(sorted(antidiagonal, reverse=True)))
        
    return diagonais 

def tabuleiro_para_str(tab):
    """ Retorna uma representação de um tabuleiro a partir de um tuplo.
    
        Args:
            tab (tuplo): Tabuleiro para transformar em string
            
        Returns:
            tab_str(string): String que representa o tabuleiro
        
    
    """
    
    tab_str = ""
    # x é um contador das linhas
    x = 0
    
    # Cria o tabuleiro
    for row in tab:
        # i é um contador de elementos por linha do tabuleiro
        i = 0
        for element in row:
            # Pra cada elemento do tabuleiro cujo valor é -1 adiciona um O ao tabuleiro
            if element == -1:
                tab_str += "O"
                
            # Pra cada elemento do tabuleiro cujo valor é 0 adiciona um + ao tabuleiro
            elif element == 0: 
                tab_str += "+"
            else:
            # Pra cada elemento do tabuleiro cujo valor é 1 adiciona um X ao tabuleiro
                tab_str += "X"
            # Caso não seja o último elemento da linha, adiciona o "---"
            if i < len(row) - 1:
                tab_str += "---"
            i += 1
            
        # Caso não seja a ultima linha adiciona os espaços embaixo das posições
        if x < len(tab) - 1:
            tab_str += "\n"
            for num in range(1, i + 1):
                tab_str += "|"
                if num < i:
                    tab_str += "   "
            tab_str += "\n"
        x += 1
        
    return tab_str

def eh_posicao_valida(tab, pos):
    """ Verifica se a posição recebida é válida para o argumento recebido.
    
        Args:
            tab (tuplo): Tabuleiro para verificar se a posição pertence
            pos (int): Inteiro que corresponde a posição a ser verificada
            
        Returns:
            Booleano(boolean): True se a posição estiver no tabuleiro, False se não tiver
        
    
    """
    if eh_tabuleiro(tab) and eh_posicao(pos):
        row_size = obtem_dimensao(tab)[1]
        return pos in range(1, len(tab) * row_size + 1)
    raise ValueError("eh_posicao_valida: argumentos invalidos")
        
def eh_posicao_livre(tab, pos):
    """ Verifica se a posição recebida é livre.
    
        Args:
            tab (tuplo): Tabuleiro para verificar se a posição é livre
            pos (int): Inteiro que corresponde a posição a ser verificada
            
        Returns:
            Booleano(boolean): True se a posição for livre no tabuleiro, False se não for
        
    
    """
    if eh_tabuleiro(tab) and eh_posicao(pos):
        if eh_posicao_valida(tab, pos):
            return obtem_valor(tab, pos) == 0
    raise ValueError("eh_posicao_livre: argumentos invalidos")

def obtem_posicoes_livres(tab):
    """ Obtem tuplo com todas as posições livres do tabuleiro
    
        Args:
            tab (tuplo): Tabuleiro para verificar as posições livres
            
        Returns:
            posicoes_livres(tuplo): Tuplo com todas posições livres do tabuleiro
        
    
    """
    if eh_tabuleiro(tab):
        row_size = len(tab[0])
        posicoes_livres = ()
        # Para cada posição do tabuleiro, se o valor da posição for zero adiciona no posicoes_livres
        for pos in range(1, row_size * len(tab) + 1):
            if obtem_valor(tab, pos) == 0:
                posicoes_livres += (pos,)
        return posicoes_livres
    raise ValueError("obtem_posicoes_livres: argumentos invalidos")
            
def obtem_posicoes_jogador(tab, jog):
    """ Obtem tuplo com todas as posições do jogador do tabuleiro
    
        Args:
            tab (tuplo): Tabuleiro para verificar as posições do jogador
            jog (int): Jogador a verificar posições
            
        Returns:
            jog_positions(tuplo): Tuplo com todas posições do jogador do tabuleiro
        
    
    """
    if eh_tabuleiro(tab) and (jog == 1 or jog == -1):
        row_size = len(tab[0])
        jog_positions = ()
        for pos in range(1, row_size * len(tab) + 1):
            if obtem_valor(tab, pos) == jog:
                jog_positions += (pos, )
        return jog_positions
    raise ValueError("obtem_posicoes_jogador: argumentos invalidos")

# Função auxiliar para a função obtem_posicoes_adjacentes
def retorna_adjacentes(tup, pos):
    posicoes_adjacentes = ()
    if pos in tup:
                index = tup.index(pos)
                if index > 0:
                    posicoes_adjacentes += (tup[index - 1],)
                if index < len(tup) - 1:
                    posicoes_adjacentes += (tup[index + 1],)
    return posicoes_adjacentes

def obtem_posicoes_adjacentes(tab, pos):
    """ Obtem tuplo com todas as posições adjacentes à posição recebida
    
        Args:
            tab (tuplo): Tabuleiro para verificar as posições
            pos(int): Posição para verificar suas adjacentes
            
        Returns:
            posicoes_adjacentes(tuplo): Tuplo com todas posições adjacentes a posição recebida
        
    
    """
    if eh_tabuleiro(tab) and eh_posicao(pos):
        if eh_posicao_valida(tab, pos):
            diagonal = obtem_diagonais(tab, pos)[0]
            antidiagonal = obtem_diagonais(tab, pos)[1]
            linha = obtem_linha(tab, pos)
            coluna = obtem_coluna(tab, pos)
            
            posicoes_adjacentes = ()
            posicoes_adjacentes += retorna_adjacentes(diagonal, pos)
            posicoes_adjacentes += retorna_adjacentes(antidiagonal, pos)
            posicoes_adjacentes += retorna_adjacentes(linha, pos)
            posicoes_adjacentes += retorna_adjacentes(coluna, pos)
            
            return tuple(sorted(posicoes_adjacentes))

        else:
            raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")
    else:
        raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")


def ordena_posicoes_tabuleiro(tab, tup):
    """ Obtem tuplo com todas as posições do tabuleiro ordenadas pela distância ao centro
    
        Args:
            tab (tuplo): Tabuleiro para verificar as posições
            pos(int): Posição para verificar suas distâncias ao centro
            
        Returns:
            positions(tuplo): Tuplo com todas posições do tuplo recebido ordenadas por distância ao centro
        
    
    """
    if eh_tabuleiro(tab) and type(tup) == tuple and tup != ():
        for pos in tup:
            if not eh_posicao(pos):
                if not eh_posicao_valida(tab, pos):
                    raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
        row_size = len(tab[0])
        lines = obtem_dimensao(tab)[0]
        columns = obtem_dimensao(tab)[1]
        coordenates = ()
        final_coordenates = ()
        distance_coordenates = ()
        positions = ()
        
        center = (lines // 2) *  columns + columns // 2 + 1
        
        row = 0
        pos = 1
        for positions_row in tab:
            for element in obtem_linha(tab, pos):
                if element in tup:
                    coordenates += ((element, row,),)
            row += 1
            pos += row_size
            
        column = 0
        pos = 1
        index = 0
        
        for pos in range(1, row_size * len(tab) + 1):
            row = (pos - 1) // row_size
            column = pos - row * row_size - 1
            if pos in tup:
                final_coordenates += ((coordenates[index] + (column,),))
                index += 1
            column += 1
            pos += 1
         
        center_coordenates = (center, lines // 2, columns // 2)
        
        for coordenate in final_coordenates:
            distance = max(abs(coordenate[1] - center_coordenates[1]), abs(coordenate[2] - center_coordenates[2]))
            if coordenate[0] in tup:
                distance_coordenates += (coordenate + (distance, ), )
        
        distance = 0
        for num in range(1, max(center_coordenates[0], center_coordenates[1])):
            for coordenate in distance_coordenates:
                if coordenate[3] == distance:
                    positions += (coordenate[0], )
            distance += 1
            
        return positions
    raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")

def marca_posicao(tab, pos, jog):
    """ Obtem tabuleiro com posição escolhida marcada
    
        Args:
            tab (tuplo): Tabuleiro para marcar posições
            pos(int): Posição para marcar
            jog(int): Jogador a marcar
            
        Returns:
            final_tab(tuplo): tabuleiro final com a posição recebida marcada com o jogador recebido
        
    
    """
    if eh_tabuleiro(tab) and eh_posicao(pos) and pos in obtem_posicoes_livres(tab) and jog in [-1, 1]:
        row_size = len(tab[0])
        row = (pos - 1) // row_size
        index = pos - (row * row_size + 1 )
        tab_row = tab[row]
    
        row_index = 0
        final_row = ()
        for num in tab_row:
            if row_index == index:
                final_row += (jog,)
            else:
                final_row += (num,)
            row_index += 1


        tab_line = 0
        final_tab = ()
        for line in tab:
            if tab_line == row:
                final_tab += (final_row,)
            else:
                final_tab += (tab[tab_line],)
            tab_line += 1
        return final_tab
    
    raise ValueError("marca_posicao: argumentos invalidos")

#Função auxiliar à função verifica_k_linhas
def obtem_tup(tab, pos, jog, k, tup):
    count = 0
    for num in tup:
        if obtem_valor(tab, num) == jog:
            count += 1
            if count == k:
                return True
        else:
            count = 0
    return False

def verifica_k_linhas(tab, pos, jog, k):
    """ Retorna True se o jogador jog obteve k posições em sequencia, sequencia a qual contem a posicao pos
    
        Args:
            tab (tuplo): Tabuleiro para marcar posições
            pos(int): Posição a verificar
            jog(int): Jogador a verificar
            k(int): numero de peças seguidas para ganhar
            
        Returns:
            Booleano (boolean): Retorna True se um dos jogadores tem k peças em sequencia, incluindo a posicao pos, False caso contrario
        
    
    """
    if eh_tabuleiro(tab) and eh_posicao(pos) and k > 0:
        if eh_posicao_valida(tab, pos):
            if obtem_valor(tab, pos) == jog:
                return obtem_tup(tab, pos, jog, k, obtem_linha(tab, pos)) or obtem_tup(tab, pos, jog, k, obtem_coluna(tab, pos)) or obtem_tup(tab, pos, jog, k, obtem_diagonais(tab, pos)[0]) or obtem_tup(tab, pos, jog, k, obtem_diagonais(tab, pos)[1])
            return False
    raise ValueError("verifica_k_linhas: argumentos invalidos")

def eh_fim_jogo(tab, k):
    """ Retorna se é fim de jogo
    
        Args:
            tab (tuplo): Tabuleiro para verificar
            k(int): Numero de posicoes seguidas para ganhar jogo
            
        Returns:
            Booleano(boolean): True se já acabou o jogo, False caso contrário
        
    
    """
    if eh_tabuleiro(tab) and type(k) == int and k > 0:
        for position in range(1, len(tab) * len(tab[0]) + 1):
            if obtem_posicoes_livres(tab) == ():
                return True
            for number in [-1, 1]:
                if verifica_k_linhas(tab, position, number, k):
                    return True
        
        return False
    raise ValueError("eh_fim_jogo: argumentos invalidos")

def escolhe_posicao_manual(tab):
    """ Retorna posição escolhida pelo jogador
    
        Args:
            tab (tuplo): Tabuleiro para marcar a posicao
            
        Returns:
            pos(int): posição escolhida pelo jogador
        
    
    """
    #SE DER ERRO EH PRA DAR ERRO OU REPETIR QUANDO EH LETRA E NUMERO
    if eh_tabuleiro(tab):
        chosen_position = input("Turno do jogador. Escolha uma posicao livre: ")
        if chosen_position.isdigit():
            pos = int(chosen_position)
            if eh_posicao(pos):
                if eh_posicao_valida(tab, pos):
                    if obtem_valor(tab, pos) == 0:
                        return pos
            else:
                raise ValueError("escolhe_posicao_manual: argumento invalido")
        else:
            raise ValueError("escolhe_posicao_manual: argumento invalido")
        pos = escolhe_posicao_manual(tab)
        return pos
    
    raise ValueError("escolhe_posicao_manual: argumento invalido")


        

def escolhe_posicao_auto(tab, jog, k, lvl):
    """ Retorna posição escolhida pelo pc
    
        Args:
            tab (tuplo): Tabuleiro para marcar a posicao
            jog(int): jogador do pc
            k(int): quantos em sequencia pra ganhar
            lvl(string): nivel de dificuldade
            
        Returns:
            pos(int): posição escolhida pelo pc
        
    
    """
    if eh_tabuleiro(tab) and not eh_fim_jogo(tab, k) and jog in [-1, 1] and type(k) == int and k > 0:
        posicoes_livres = obtem_posicoes_livres(tab)
        
        if lvl == "facil":
            if obtem_posicoes_jogador(tab, jog) != ():
                for pos in ordena_posicoes_tabuleiro(tab, posicoes_livres):
                    for num in obtem_posicoes_jogador(tab, jog):
                        posicoes_adjacentes = obtem_posicoes_adjacentes(tab, num)
                        if pos in posicoes_adjacentes:
                            return pos                   
            else:
                
                posicoes = ordena_posicoes_tabuleiro(tab, posicoes_livres)
                pos = posicoes[0]
                return pos
                
        
        elif lvl == "normal":
            possible_jogs = [jog, -jog]
            possible_in_row = ()
            
            for chosen_jog in possible_jogs:
                L = k
                for pos in range(1, len(tab[0]) * len(tab) + 1):
                    if obtem_valor(tab, pos) == chosen_jog and pos not in obtem_posicoes_livres(tab):
                        while L > 0:
                            if verifica_k_linhas(tab, pos, chosen_jog, L):
                                L += 1
                                if (chosen_jog, L) not in possible_in_row:
                                    possible_in_row += ((chosen_jog, L),)
                                break
                            L -= 1
                            
            if possible_in_row != ():
                chosen_1 = ()
                chosen_minus_1 = ()
                
                for possibility in possible_in_row:
                    if possibility[0] == 1:
                        chosen_1 += (possibility[1],)
                    elif possibility[0] == -1:
                        chosen_minus_1 += (possibility[1],)
                        
                possible_in_row = ((1, max(chosen_1)), (-1, max(chosen_minus_1)))
            
                if possible_in_row != ((1, ),(-1 )):
                    max_L = max(possible_in_row[0][1], possible_in_row[1][1])
            
                    for possibility in possible_in_row:
                        if possible_in_row[0][1] == possible_in_row[0][1]:
                            best_play = jog
                        if possibility[1] == max_L:
                            best_play = possibility[0]
                
                    for pos in range(1, len(tab[0]) * len(tab) + 1):
                        if verifica_k_linhas(tab, pos, best_play, L - 1):
                            
                            for num in obtem_linha(tab, pos):
                                if num in obtem_posicoes_livres(tab):
                                    tentativa = marca_posicao(tab, num, jog)
                                    if verifica_k_linhas(tentativa, num, 1, L) or verifica_k_linhas(tentativa, num, 1, k) or verifica_k_linhas(tentativa, num, -1, L) or verifica_k_linhas(tentativa, num, -1, k):
                                        if best_play == jog:
                                            return num
                                        else:
                                            tentativa = marca_posicao(tab, num, jog)
                                            return num
                                        
                            for num in obtem_coluna(tab, pos):
                                if num in obtem_posicoes_livres(tab):
                                    tentativa = marca_posicao(tab, num, best_play)
                                    if verifica_k_linhas(tentativa, num, best_play, L):
                                        if best_play == jog:
                                            return num
                                        else:
                                            tentativa = marca_posicao(tab, num, jog)
                                            return num
                            
                            for num in obtem_diagonais(tab, pos)[0]:
                                if num in obtem_posicoes_livres(tab):
                                    tentativa = marca_posicao(tab, num, best_play)
                                    if verifica_k_linhas(tentativa, num, best_play, L):
                                        if best_play == jog:
                                            return num
                                        else:
                                            tentativa = marca_posicao(tab, num, jog)
                                            return num
                                
                            for num in obtem_diagonais(tab, pos)[1]:
                                if num in obtem_posicoes_livres(tab):
                                    tentativa = marca_posicao(tab, num, best_play)
                                    if verifica_k_linhas(tentativa, num, best_play, L):
                                        if best_play == jog:
                                            return num
                                        else:
                                            tentativa = marca_posicao(tab, num, jog)
                                            return num
            else:
                pos_livre = obtem_posicoes_livres(tab)
                pos_livre_ordenadas = ordena_posicoes_tabuleiro(tab, pos_livre)
                return pos_livre_ordenadas[0]
            
                    
        elif lvl == "dificil":
            player = jog
            tabuleiro1= tab
            player = jog
            pos_livres = obtem_posicoes_livres(tab)
            posicoes_checadas = 0
            for pos in pos_livres:
                posicoes_checadas += 1
                tabuleiro1 = marca_posicao(tab, pos, jog)
                while not eh_fim_jogo(tabuleiro1, k):
                    posicao = escolhe_posicao_auto(tabuleiro1, -player, k, "normal")
                    tabuleiro_novo1 = marca_posicao(tabuleiro1, posicao, -player)
                    tabuleiro1 = tabuleiro_novo1
                    play = -player
                    player = play
                
                for pos_tab1 in range(1, obtem_dimensao(tabuleiro1)[0] * obtem_dimensao(tabuleiro1)[1] + 1):
                    if verifica_k_linhas(tabuleiro1, pos_tab1, jog, k):
                        return pos
                for pos_tab1 in range(1, obtem_dimensao(tabuleiro1)[0] * obtem_dimensao(tabuleiro1)[1] + 1):
                    if eh_fim_jogo(tabuleiro1, k) and not verifica_k_linhas(tabuleiro1, pos_tab1, -jog, k):
                        return pos
            return pos_livres[0]

def jogo_mnk(cfg, jog, lvl):
    """ Retorna posição escolhida pelo pc
    
        Args:
            cfg (tuplo): tamanho do tabuleiro, k pra ganhar
            jog(int): jogador 
            lvl(string): nivel de dificuldade
            
        Returns:
            winner (int): vencedor
        
    
    """
    if len(cfg) == 3 and type(cfg[0]) == int and type(cfg[1]) == int and type(cfg[2]) == int and jog in [-1, 1]:
        if lvl == "facil" or lvl == "normal" or lvl == "dificil":
            print("Bem-vindo ao JOGO MNK.")
            rows = cfg[0]
            columns = cfg[1]
            k = cfg[2]
            
            if jog == 1:
                jogador = "X"
            
            else:
                jogador = "0"
                
            print(f"O jogador joga com '{jogador}'.")
            
            # Define o tab
            tab = ()
            row = ()
            for num in range(1, columns + 1):
                row += (0,)
            for num in range(1, rows + 1):
                tab += (row,)
            
            while not eh_fim_jogo(tab, k):
                print(tabuleiro_para_str(tab))
                if jog == 1:
                    player_pos = escolhe_posicao_manual(tab)
                    tab = marca_posicao(tab, player_pos, jog)
                    print(tabuleiro_para_str(tab))
                    if not eh_fim_jogo(tab, k):
                        print(f"Turno do computador ({lvl}):")
                        pc_choice = escolhe_posicao_auto(tab, -jog, k, lvl)
                        tab = marca_posicao(tab, pc_choice, -jog)
                else:
                    print(f"Turno do computador ({lvl}):")
                    pc_choice = escolhe_posicao_auto(tab, -jog, k, lvl)
                    tab = marca_posicao(tab, pc_choice, -jog)
                    if not eh_fim_jogo(tab, k):
                        print(tabuleiro_para_str(tab))
                        player_pos = escolhe_posicao_manual(tab)
                        tab = marca_posicao(tab, player_pos, jog)
                        print(tabuleiro_para_str(tab))
                    
                if eh_fim_jogo(tab, k):
                    end = 0
                    print(tabuleiro_para_str(tab))
                    count = 0
                    for player in [-1, 1]:
                        for pos in range(1, len(tab) * len(tab[0]) + 1):
                            count += 1
                            if verifica_k_linhas(tab, pos, player, k):
                                if player == jog:
                                    print("VITORIA")
                                    return player
                                elif player == -jog:
                                    print("DERROTA")
                                    return player
                    if end == 0:
                        print("EMPATE") 
                        return player

        else:                
            raise ValueError("jogo_mnk: argumentos invalidos")
    else:           
        raise ValueError("jogo_mnk: argumentos invalidos")