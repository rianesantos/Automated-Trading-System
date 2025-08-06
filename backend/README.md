# SISTEMA AUTOMATIZADO DE NEGOCIAÇÕES (Automated Trading Systen)

---

## 📦 Funcionalidades

- 🔍 Coleta de dados históricos e atuais de ações
- 📊 Estratégia de cruzamento de médias móveis (curta vs. longa)
- 💼 Simulação de operações de compra e venda com backtest
- 🚨 Alertas em tempo real para variações significativas de preço
- ⚠️ Monitoramento de risco com limites de stop loss, stop gain e alocação máxima
- 📂 Visualização do portfólio

---

## 🧠 Tecnologias utilizadas

- Python 3.10+
- [yfinance](https://pypi.org/project/yfinance/)
- matplotlib
- pandas

---

## 🗂 Estrutura do Projeto

projeto-de-software/
│
├── backend/
│ ├── main_primal.py # Ponto de entrada (menu e execução)
│ ├── strategies.py # Estratégia de cruzamento de médias móveis
│ ├── market_data.py # Coleta de dados de mercado com yfinance
│ ├── backtest.py # Simulação de operações (compra e venda)
│ ├── portfolio.py # Estrutura do portfólio
│ ├── risk.py # Avaliação de risco (alocação, stop loss/gain)
│ └── alerts.py # Alertas de preço em tempo real

---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/backend

### 2. Crie um ambiente virtual
python -m venv venv

### 3. Ative o ambiente virtua

Windows (PowerShell):
.\venv\Scripts\Activate.ps

Linux/macOS:
source venv/bin/activate

### 4. Instale as dependências
pip install -r requirements.txt
Se você não tiver o requirements.txt, crie um com:
yfinance
matplotlib
pandas

### 5.Execute o programa principal
Estando dentro da pasta backend:
python main_primal.py

🧪 Como usar
Ao rodar o script, você verá um menu interativo no terminal:

===== MAIN MENU =====
1. Analyze a stock
2. View current portfolio
3. Exit
Digite 1 para analisar uma ação (ex: AAPL)

Digite 2 para visualizar o portfólio atual

Digite 3 para sair

📌 Observações
Os preços são obtidos em tempo real via yfinance.
A estratégia utilizada é crossover de médias móveis com janelas de 5 e 20 dias.
O portfólio é simulado internamente; não há conexões com corretoras reais.
Alertas são exibidos no terminal se houver variações superiores a 5% no preço.

✅ Exemplo de execução

===== MAIN MENU =====
1. Analyze a stock
2. View current portfolio
3. Exit
Select an option: 1
Enter ticker (ex: AAPL): AAPL

🔍︎ Analyzing AAPL...
📈 Fetching historical data...
⚙️ Running MA crossover strategy...
📊 Generating chart...
💼 Running backtest...
💰 Current portfolio value: $10723.45
🚨 Checking market alerts...
📉 Risk assessment...

