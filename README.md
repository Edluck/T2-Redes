# 🏆 Campo Minado Multiplayer  

Um jogo **multiplayer online** do **Campo Minado**, onde até **5 jogadores** podem competir em turnos. O último jogador restante vence! 💣🎉  

---

## 📌 Descrição  
Este projeto é um **servidor local** para um jogo multiplayer de **Campo Minado**, criado usando **Python** (com **sockets e threads**) e **HTML + JavaScript** para a interface web.  

- **Cada jogador joga no seu turno** e clica em uma célula do tabuleiro.  
- **Se clicar em uma bomba, ele perde** e entra na lista de **espectadores**.  
- **O último jogador restante vence**, e o jogo exibe o vencedor na tela.  

💡 **Destaque:** O servidor usa **sockets e multithreading** para suportar múltiplos jogadores ao mesmo tempo.

---

## 🛠 Tecnologias Utilizadas  

### 🔹 Backend (Servidor)
- **Python** 🐍  
- **Sockets TCP** (para comunicação entre cliente e servidor)  
- **Multithreading** (para gerenciar múltiplas conexões ao mesmo tempo)  
- **Manipulação de JSON** (para troca de dados entre servidor e cliente)  

### 🔹 Frontend (Cliente)
- **HTML + CSS** (interface do jogo)  
- **JavaScript (Fetch API)** (para comunicação com o servidor)  

---

## 🚀 Como Executar  

### 📌 1. Requisitos
- **Python 3.8+** instalado na máquina  
- Nenhuma biblioteca externa é necessária (usamos apenas bibliotecas nativas do Python)  

---

### 📌 2. Instruções de Execução  

1️⃣ Clone o repositório  
**git clone <URL_DO_REPOSITORIO>**  
**cd campo-minado-multiplayer**  

2️⃣ Instale as dependências (se houver)  
📌 Este projeto não precisa de bibliotecas externas. Mas, se houver futuras melhorias que exijam pacotes, crie um arquivo `requirements.txt` e instale com:  
**pip install -r requirements.txt**  

3️⃣ Execute o servidor  
**python servidor.py**  

Você verá a mensagem:  
✅ **Servidor iniciado e escutando em 127.0.0.1:65433**  

Isso significa que o servidor está rodando!  

4️⃣ Acesse o jogo no navegador  
📌 **Se for jogar na mesma máquina onde o servidor está rodando**, acesse:  
**http://127.0.0.1:65433**  

📌 **Se for jogar em outra máquina na mesma rede**, acesse:  
**http://IP_DA_MAQUINA_SERVIDOR:65433**  

🔹 **Substitua `IP_DA_MAQUINA_SERVIDOR` pelo IP da máquina onde o servidor está rodando.**  

Agora você pode **entrar no jogo e jogar online com outras pessoas na rede!** 🎉  

---

## 🧪 Como Testar  
Para testar o funcionamento do jogo:  
1. **Abra múltiplas abas do navegador** e acesse `http://127.0.0.1:65433`.  
2. Cada jogador insere um nome e entra no jogo.  
3. O jogo avança **turno a turno**.  
4. **Se um jogador clicar em uma bomba, ele vai para a lista de espectadores**.  
5. O último jogador restante **vence o jogo**, e o resultado é exibido na tela.  

📌 **Testando multiplayer em diferentes dispositivos**  
Para jogar em outra máquina na mesma rede, **use o IP do servidor** em vez de `localhost`.  
Exemplo:  
**http://192.168.1.100:65433**  
(onde `192.168.1.100` é o IP da máquina rodando o servidor)

---

## 🎮 Funcionalidades Implementadas  
✅ **Servidor com sockets e multithreading** para suportar múltiplos jogadores.  
✅ **Jogo multiplayer** com até **5 jogadores simultâneos**.  
✅ **Interface Web responsiva** (HTML, CSS e JavaScript).  
✅ **Lista de jogadores conectados e lista de espectadores (perdedores)**.  
✅ **Gerenciamento de turnos** (apenas o jogador da vez pode jogar).  
✅ **Exibição automática do vencedor na tela**.  
✅ **Atualização dinâmica do tabuleiro e das listas de jogadores**.  
✅ **Suporte para acesso de múltiplas máquinas na mesma rede**.  

---

## 🚀 Possíveis Melhorias Futuras  
🔹 **Permitir personalizar o tamanho do tabuleiro e número de bombas**.  
🔹 **Implementar um chat no jogo** para comunicação entre jogadores.  
🔹 **Criar um sistema de salas** para que vários jogos possam acontecer ao mesmo tempo.  
🔹 **Salvar estatísticas dos jogadores** (número de vitórias, derrotas, etc.).  
🔹 **Transformar em um jogo online global** (hospedando em um servidor real na nuvem).  
🔹 **Correção de bugs quando o último jogador perde** e a lista de jogadores fica vazia.  

---

## 📌 Conclusão  
Este projeto foi uma excelente oportunidade para praticar **Python (sockets e multithreading)** e **desenvolvimento web (HTML, CSS, JavaScript)**.  

Agora, os jogadores podem competir no **Campo Minado Multiplayer** de forma interativa e divertida! 💣🔥  

Se tiver alguma dúvida ou sugestão, fique à vontade para abrir uma **issue** no GitHub!  

---
