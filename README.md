# Campo Minado Multiplayer  

Um jogo **multiplayer online** do **Campo Minado**, onde até **5 jogadores** podem competir em turnos. O último jogador restante vence.  

---

## Descrição  
Este projeto é um **servidor local** para um jogo multiplayer de **Campo Minado**, criado usando **Python** (com **sockets e threads**) e **HTML + JavaScript** para a interface web.  

- **Cada jogador joga no seu turno** e clica em uma célula do tabuleiro.  
- **Se clicar em uma bomba, ele perde** e entra na lista de **espectadores**.  
- **O último jogador restante vence**, e o jogo exibe o vencedor na tela.  

O servidor utiliza **sockets e multithreading** para suportar múltiplos jogadores ao mesmo tempo.

---

## Tecnologias Utilizadas  

### Backend (Servidor)
- **Python**  
- **Sockets TCP** (para comunicação entre cliente e servidor)  
- **Multithreading** (para gerenciar múltiplas conexões ao mesmo tempo)  
- **Manipulação de JSON** (para troca de dados entre servidor e cliente)  

### Frontend (Cliente)
- **HTML + CSS** (interface do jogo)  
- **JavaScript (Fetch API)** (para comunicação com o servidor)  

---

## Como Executar  

### 1. Requisitos
- **Python 3.8+** instalado na máquina  
- Nenhuma biblioteca externa é necessária (apenas bibliotecas nativas do Python)  

---

### 2. Instruções de Execução  

1. **Clone o repositório:**  
   `git clone <URL_DO_REPOSITORIO>`  
   `cd T2-Redes-main` ou `cd T2-Redes`  

3. **Instale as dependências (se houver):**  
   Este projeto não precisa de bibliotecas externas, somente que a imagem da estrela e bomba, dois png, estejam no mesmo diretório do server.py e do index.html.  

4. **Execute o servidor:**  
   `python3 server.py`  

   Após executar o comando, a seguinte mensagem será exibida:  
   **Servidor iniciado e escutando em 127.0.0.1:65433**  

   Isso significa que o servidor está rodando corretamente.  

5. **Acesse o jogo no navegador:**  
   - Se for jogar na mesma máquina onde o servidor está rodando, acesse:  
     `http://127.0.0.1:65433`  

   - Se outra máquinas da mesma rede forem jogar, acesse:  
     `http://IP_DA_MAQUINA_SERVIDOR:65433`  

   **Substitua `IP_DA_MAQUINA_SERVIDOR` pelo IP da máquina onde o servidor está rodando.**
   
   server.py: linha 8
   index.html: linha 147  

Agora o jogo está disponível e pronto para ser jogado por múltiplos jogadores na rede.

---

## Como Testar  
Para testar o funcionamento do jogo:  
1. Abra múltiplas abas do navegador e acesse `http://127.0.0.1:65433`, caso outras máquinas entrem, acessem `http://IP_MAQUINA:65433`.  
2. Cada jogador insere um nome e entra no jogo.  
3. O jogo avança **turno a turno**.  
4. Se um jogador clicar em uma bomba, ele vai para a lista de espectadores.  
5. O último jogador restante vence o jogo, e o resultado é exibido na tela.  

**Testando multiplayer em diferentes dispositivos**  
Para jogar em outra máquina na mesma rede, utilize o IP da máquina do servidor em vez de `localhost`.  
Exemplo:  
`http://190.160.1.100:65433`  
(Onde `190.160.1.100` é o IP da máquina rodando o servidor)  

---

## Funcionalidades Implementadas  
- **Servidor com sockets e multithreading** para suportar múltiplos jogadores.  
- **Jogo multiplayer** com até **5 jogadores simultâneos**.  
- **Interface Web responsiva** (HTML, CSS e JavaScript).  
- **Lista de jogadores conectados e lista de espectadores (perdedores).**  
- **Gerenciamento de turnos** (apenas o jogador da vez pode jogar).  
- **Exibição automática do vencedor na tela.**  
- **Atualização dinâmica do tabuleiro e das listas de jogadores.**  
- **Suporte para acesso de múltiplas máquinas na mesma rede.**  

---

## Possíveis Melhorias Futuras  
- Permitir personalizar o tamanho do tabuleiro e número de bombas.  
- Implementar um chat no jogo para comunicação entre jogadores.  
- Criar um sistema de salas para que vários jogos possam acontecer ao mesmo tempo, com diferentes tamanhos de campo.  
- Salvar estatísticas dos jogadores (número de vitórias, derrotas, etc.).  
- Transformar em um jogo online global (hospedando em um servidor real na nuvem).  
- Correção de bugs quando o penúltimo jogador perde, o jogo buga e não atualiza normalmente pro vencedor ou que ele é um espectador, é necessário reiniciar a pagina.
  
**Erro conhecido**: IndexError, causado pela linha 76 no server.py, Se não for o ultimo player a clicar, tudo funciona.

---
## Testes
 - Pelo comando "top" no terminal, observou-se que com 5 jogadores, o servidor consome 5% da memória(800MB) e 6% da CPU.
 - Limite teórico de 20 servidores ou 20 salas de 5 jogadores.
 - ![image](https://github.com/user-attachments/assets/8d4cf2ec-86d9-49d6-bff6-3d1524ede369)

---

## Dificuldades
 - Baixa experiência com as linguagens python e JavaScript.
