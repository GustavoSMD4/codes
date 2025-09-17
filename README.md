# 🔐 DB com senhas de 4 dígitos (somente números de 0 a 9) - API

---

## 🚀 Endpoints

### 📊 Estatísticas gerais  
**GET** `/stats`  
Retorna estatísticas gerais do banco de dados, incluindo:

- 🔢 **Total de senhas**: Soma total das quantidades de uso dos códigos.  
- 🥇 **Código mais usado**: O código com maior quantidade registrada.  
- 🥄 **Código menos usado**: O código com menor quantidade registrada.  

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/stats](https://gustavosmd4codes.pythonanywhere.com/stats)

---

### 📄 Listar todos os códigos

**GET** `/codes`  
Retorna todos os códigos disponíveis.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes](https://gustavosmd4codes.pythonanywhere.com/codes)

---

### 🥇 Listar os primeiros códigos

**GET** `/codes/first/<quantidade>`  
Retorna os primeiros `<quantidade>` códigos.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/first/10](https://gustavosmd4codes.pythonanywhere.com/codes/first/10)

---

### 🏁 Listar os últimos códigos

**GET** `/codes/last/<quantidade>`  
Retorna os últimos `<quantidade>` códigos.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/last/10](https://gustavosmd4codes.pythonanywhere.com/codes/last/10)

---

### 🔍 Verificar posição de um código

**GET** `/code/verify/<code>`  
Envia um código de 4 dígitos e retorna sua posição e avaliação de segurança.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/code/verify/1234](https://gustavosmd4codes.pythonanywhere.com/code/verify/1234)

---

### 🏆 Sugerir código seguro ou comum

**GET** `/code/suggest?safe=<True/False>`  
Este endpoint sugere um código baseado no parâmetro `safe`. Se `safe=True`, retorna um código **menos comum** (mais seguro). Se `safe=False`, retorna um código **mais comum** (menos seguro).

#### Parâmetros:
- `safe`: Um valor booleano (`True` ou `False`).

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/code/suggest?safe=True](https://gustavosmd4codes.pythonanywhere.com/code/suggest?safe=True)

---

### 📊 Gerar planilha Excel filtrada por prefixo

**GET** `/codes/planilha/<digits>`  
Gera uma planilha Excel (`.xlsx`) contendo os códigos filtrados pelo prefixo dos primeiros dígitos informados.

- O parâmetro `<digits>` aceita apenas os valores **1**, **2** ou **3**.
- A planilha traz os prefixos únicos desses dígitos.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/planilha/3](https://gustavosmd4codes.pythonanywhere.com/codes/planilha/3)

---

### 📄 Gerar CSV completo com todos os códigos

**GET** `/codes/csv`  
Gera um arquivo CSV com todos os códigos e suas informações, usando ponto e vírgula (`;`) como separador.

- O arquivo é entregue via download automático.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/csv](https://gustavosmd4codes.pythonanywhere.com/codes/csv)

---

### 🧠 Heatmap de dígitos por posição

**GET** `/codes/stats/<limit>`  
Gera uma visualização interativa (HTML) com:

- 🔥 Heatmap de frequência dos dígitos por posição (imagem)
- 📈 Porcentagens por dígito e posição
- 🥇 Dígito mais frequente por posição
- 📊 Estatísticas como:
  - Total de códigos analisados
  - Total de ocorrências somadas
  - Código mais frequente e sua quantidade
  - **Porcentagem das senhas** em relação ao total do banco

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/stats/1000](https://gustavosmd4codes.pythonanywhere.com/codes/stats/1000)

---

### 🔥 Heatmap de dígitos por posição (intervalo)

**GET** `/codes/stats/between/<start>/<end>`  
Gera uma visualização interativa (HTML) semelhante ao endpoint de limite, mas para códigos no intervalo entre `<start>` e `<end>` (inclusive).

- Aceita dois parâmetros inteiros:
  - `<start>`: código inicial do intervalo (ex: 1000)
  - `<end>`: código final do intervalo (ex: 2000)
- Retorna estatísticas e heatmap dos códigos cujo valor está entre `<start>` e `<end>`.
- O heatmap exibe:
  - Frequência dos dígitos por posição (imagem)
  - Porcentagens relativas por dígito e posição
  - Dígitos mais comuns por posição
  - Estatísticas como total de códigos no intervalo, total de ocorrências, código mais frequente e porcentagem sobre o total do banco

#### Regras:
- `<start>` deve ser menor ou igual a `<end>`. Caso contrário, retorna erro 400.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/stats/between/1000/2000](https://gustavosmd4codes.pythonanywhere.com/codes/stats/between/1000/2000)

---

## 🌐 URL base da API

[https://gustavosmd4codes.pythonanywhere.com](https://gustavosmd4codes.pythonanywhere.com)
