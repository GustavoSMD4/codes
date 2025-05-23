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
🔗 [https://gustavosmd4codes.pythonanywhere.com/codes](https://gustavosmd4codes.pythonanywhere.com/codes)

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

🔗 Endpoint:  
[https://gustavosmd4codes.pythonanywhere.com/code/verify/1234](https://gustavosmd4codes.pythonanywhere.com/code/verify/1234)

---

### 🏆 Sugerir código seguro ou comum

**GET** `/code/suggest?safe=<True/False>`  
Este endpoint sugere um código baseado no parâmetro `safe`. Se `safe=True`, retorna um código **menos comum** (menos usado). Se `safe=False`, retorna um código **mais comum** (mais usado).

#### Parâmetros:
- `safe`: Um valor booleano (`True` ou `False`). O padrão é `True`.
  - `True`: Retorna um código menos comum (seguro).
  - `False`: Retorna um código mais comum.

🔗 Exemplo:
- **URL**: [https://gustavosmd4codes.pythonanywhere.com/code/suggest?safe=True](https://gustavosmd4codes.pythonanywhere.com/code/suggest?safe=True)

