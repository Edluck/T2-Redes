import socket
import threading
import json
import random
import os

# Configurações do servidor
HOST = '172.20.6.125'  # Endereço IP do servidor (localhost)
PORT = 65433        # Porta que o servidor vai escutar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório do arquivo atual

# Classe que representa o jogo Campo Minado
class CampoMinado:
    def __init__(self, tamanho, bombas):
        self.tamanho = tamanho
        self.bombas = bombas
        self.tabuleiro = self.criar_tabuleiro()
        self.estado_jogo = [['' for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        self.jogadores = []
        self.espectadores = []
        self.espectadores_atuais = 0
        self.jogador_atual = 0  # Índice do jogador que está na vez
        self.fim = False
        self.vencedor = ""

    # Método para criar o tabuleiro com bombas
    def criar_tabuleiro(self):
        tabuleiro = [[0 for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        for _ in range(self.bombas):
            x, y = random.randint(0, self.tamanho-1), random.randint(0, self.tamanho-1)
            while tabuleiro[x][y] == -1:
                x, y = random.randint(0, self.tamanho-1), random.randint(0, self.tamanho-1)
            tabuleiro[x][y] = -1  # -1 representa uma bomba
        return tabuleiro

    # Método para adicionar um jogador
    def adicionar_jogador(self, jogador):
        if len(self.jogadores) < 5:
            self.jogadores.append(jogador)
            return True
        self.adicionar_espectador(jogador)

    # Método para remover um jogador
    def remover_jogador(self, jogador):
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
            return True
        return False

    # Método para adicionar um espectador
    def adicionar_espectador(self, espectador):
        self.espectadores.append(espectador)
        return True

    # Método para remover um espectador
    def remover_espectador(self, espectador):
        if espectador in self.espectadores:
            self.espectadores.remove(espectador)
            return True

    # Método para passar o turno para o próximo jogador
    def proximo_turno(self):
        if len(self.jogadores) > 1:
            self.jogador_atual = (self.jogador_atual + 1) % len(self.jogadores)

    # Método para realizar uma jogada
    def jogar(self, jogador, x, y):
        if jogador not in self.jogadores:
            return "jogador_invalido"

        if self.jogadores[self.jogador_atual] != jogador:
            return "fora_de_turno"

        if self.tabuleiro[x][y] == -1:
            self.estado_jogo[x][y] = "bomba"
            if len(self.jogadores) == 2 and self.jogador_atual == 1:
                self.adicionar_espectador
                self.fim = True
                self.vencedor = self.jogadores[0]
                return "vitoria"
            self.remover_jogador(jogador) # O problema do ultimo player esta aqui
            self.adicionar_espectador(jogador)
            if len(self.jogadores) == 1:  # Se sobrar um jogador, ele vence
                self.fim = True
                self.vencedor = self.jogadores[0]
                return "vitoria"
            if self.jogador_atual >= len(self.jogadores):
                self.jogador_atual = 0
            return "bomba"
        else:
            self.estado_jogo[x][y] = "seguro"
            self.proximo_turno()
            return "seguro"

# Instancia o jogo Campo Minado
jogo = CampoMinado(tamanho=5, bombas=5)

# Função para lidar com um cliente
def handle_client(conn, addr):
    print(f'Conectado a {addr}')

    # Loop para manter a conexão com o cliente
    with conn:
        data = conn.recv(1024)  # Recebe os dados do cliente

        message = data.decode('utf-8')
        if len(message) > 0:
            header = message.split('\n')[0]  # Remove quebras de linha
            dados = header.split(" ")
        metodo, caminho = dados[:2]
        if metodo == "GET" and caminho == "/estado":
            estado = {
            "tabuleiro": jogo.estado_jogo,
            "jogador_atual": jogo.jogadores[jogo.jogador_atual] if jogo.jogadores else None,
            "jogadores": list(jogo.jogadores),  # Garante que os jogadores são enviados corretamente
            "espectadores": list(jogo.espectadores),
            "espectador_atual": jogo.espectadores[jogo.espectadores_atuais] if jogo.espectadores else None,
            "fim": jogo.fim,
            "vencedor": jogo.vencedor
            }
            #print(estado)
            resposta = json.dumps(estado)
            conn.sendall(f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{resposta}".encode('utf-8'))
            return
        # Servindo arquivos estáticos (imagens)
        if caminho.endswith(".png"):
            caminho_arquivo = os.path.join(BASE_DIR, caminho[1:])  # Remove a barra inicial '/'
    
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, "rb") as file:
                    conteudo = file.read()
                conn.sendall(f"HTTP/1.1 200 OK\nContent-Type: image/png\n\n".encode('utf-8') + conteudo)
            else:
                conn.sendall("HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\nImagem não encontrada".encode('utf-8'))
            return
        
        if metodo == "GET" and caminho == "/":
            with open(os.path.join(BASE_DIR, "index.html"), 'r', encoding='utf-8') as file:
                conteudo = file.read()
                response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + conteudo
                conn.sendall(response.encode('utf-8'))
            return
        if metodo == "POST" and caminho == "/":
            body = message.split("\r\n\r\n")[-1]
            try:
                dados = json.loads(body)
                jogador = dados.get('jogador')
                acao = dados.get('acao')
                resposta = {}
                if acao == 'entrar':
                    if jogo.adicionar_jogador(jogador):
                        resposta = {"status": "sucesso", "mensagem": f"Jogador {jogador} entrou no jogo."}
                elif acao == 'jogar':
                    x, y = dados.get('x'), dados.get('y')
                    if x is None or y is None:
                        resposta = {"status": "erro", "mensagem": "Coordenadas inválidas."}
                    else:
                        resultado = jogo.jogar(jogador, x, y)
                        if resultado == "bomba":
                            resposta = {"status": "fim", "mensagem": "Você perdeu! Agora é um espectador."}
                        elif resultado == "vitoria":
                            jogo.fim = True
                            jogo.vencedor = jogo.jogadores[0]
                            resposta = {"status": "vitoria", "vencedor": jogo.jogadores[0]}
                        elif resultado == "seguro":
                            resposta = {"status": "sucesso", "mensagem": "Jogada segura!"}
                        elif resultado == "fora_de_turno":
                            resposta = {"status": "erro", "mensagem": "Não é sua vez!"}
                        else:
                            if(jogo.fim):
                                resposta = {"status": "vitoria", "vencedor": jogo.jogadores[0]}
                            else:
                                resposta = {"status": "erro", "mensagem": "Jogador inválido."}
                
                else:
                    resposta = {"status": "erro", "mensagem": "Ação inválida."}
                    if(jogo.fim):
                        resposta = {"status": "vitoria", "vencedor": jogo.jogadores[0]}

                responstaJson = json.dumps(resposta, ensure_ascii=False)
                conn.sendall(f"HTTP/1.1 200 OK\nContent-Type: application/json\n\n{responstaJson}".encode('utf-8'))
            except:
                conn.sendall("HTTP/1.1 400 Bad Request\nContent-Type: text/plain\n\nErro ao processar a requisição.".encode('utf-8'))
        else:
            response = "HTTP/1.1 400 Bad Request\nContent-Type: text/plain\n\nRequisição inválida"
            conn.sendall(response.encode('utf-8'))

# Função principal para iniciar o servidor
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Servidor iniciado e escutando em {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f'Número de threads ativas: {threading.active_count() - 1}')  # Desconta a thread principal
            

if __name__ == '__main__':
    start_server()
