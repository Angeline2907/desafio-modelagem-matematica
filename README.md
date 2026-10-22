# 📊 Desafio: Experimentar e Criar com Modelagem Matemática

Este repositório contém a resolução do desafio proposto sobre análise de situações reais, classificação de dificuldade de modelagem, estabilidade, volatilidade e identificação de informações úteis para a construção de modelos preditivos.

---

## 🟢 Situações Mais Fáceis de Modelar

### 1. Prever a altura média dos estudantes da sua escola daqui a um ano.
* **1. Características de Previsão:** A altura humana segue padrões biológicos de crescimento muito bem documentados e estáveis na literatura médica. Em um intervalo de apenas um ano, a variação da média de uma população escolar inteira é muito pequena e altamente previsível.
* **2. Volatilidade:** O fenômeno é **mais estável**. Não sofre alterações drásticas causadas por fatores externos imediatos.
* **3. Informação Útil para o Modelo:** Dados da média de altura atual dos alunos (separados por idade/série) e tabelas de crescimento padrão da Organização Mundial da Saúde (OMS).

### 2. Prever o tempo médio de deslocamento até a escola em uma manhã comum.
* **1. Características de Previsão:** Em "manhãs comuns", as rotinas de trânsito, horários de transporte público e fluxos de vias tendem a se repetir de forma cíclica semanalmente. As pequenas variações diárias se anulam quando calculamos a média.
* **2. Volatilidade:** O fenômeno é **mais estável**. Segue um comportamento padrão na ausência de eventos extraordinários.
* **3. Informação Útil para o Modelo:** Histórico de horários de chegada dos alunos ou a extração de dados de APIs de mapas (como Google Maps ou Waze) coletados no mesmo trajeto e horário ao longo das últimas semanas.

---

## 🔴 Situações Mais Difíceis de Modelar

### 3. Prever qual vídeo será o mais assistido da internet na próxima semana.
* **1. Características de Previsão:** O consumo de conteúdo digital depende de fatores altamente subjetivos, culturais, psicológicos e, principalmente, de algoritmos complexos e secretos de recomendação das plataformas. O fenômeno de "viralização" é caótico e imprevisível.
* **2. Volatilidade:** O fenômeno é **mais volátil**. O interesse do público muda radicalmente em questão de horas.
* **3. Informação Útil para o Modelo:** Dados de tendências de busca em tempo real (como o Google Trends), relatórios de engajamento de canais que estão em crescimento exponencial e monitoramento de tópicos em alta (*trending topics*) nas redes sociais.

### 4. Prever o preço de uma moeda estrangeira amanhã.
* **1. Características de Previsão:** O mercado de câmbio é influenciado por uma quantidade massiva de variáveis globais interconectadas, incluindo decisões políticas de bancos centrais, indicadores econômicos, especulação de mercado e eventos geopolíticos inesperados.
* **2. Volatilidade:** O fenômeno é **mais volátil**. O preço de uma moeda pode sofrer fortes oscilações em poucos minutos em resposta a uma única notícia ou declaração política.
* **3. Informação Útil para o Modelo:** Histórico de séries temporais do preço da moeda (para análise técnica), calendário econômico global de anúncios de taxas de juros (como o COPOM ou o FED) e feeds de notícias financeiras globais.

---

## 📝 Conclusão
Modelos matemáticos aplicados a fenômenos **estáveis** (como biologia populacional ou rotinas urbanas consolidadas) possuem maior acurácia e menor margem de erro. Já os fenômenos **voláteis** (como comportamento social na internet ou mercados financeiros) exigem modelos estocásticos complexos e atualizações em tempo real devido ao seu alto grau de incerteza.

---
 Bons estudos e bom desafio!
