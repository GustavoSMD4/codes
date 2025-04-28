# 🔐 Verificador de Códigos - API

API simples para listar códigos numéricos de 4 dígitos e verificar a posição de um código entre os 10.000 possíveis (0000 a 9999).

---

## 🚀 Endpoints

### 📄 Listar todos os códigos

**GET** `/codes`  
Retorna todos os códigos disponíveis.  
🔗 [https://gustavosmd4codes.pythonanywhere.com/codes](https://gustavosmd4codes.pythonanywhere.com/codes)

---

### 🥇 Listar os primeiros códigos

**GET** `/codes/first/<quantidade>`  
Retorna os primeiros `<quantidade>` códigos com base na ordem crescente.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/first/10](https://gustavosmd4codes.pythonanywhere.com/codes/first/10)

---

### 🏁 Listar os últimos códigos

**GET** `/codes/last/<quantidade>`  
Retorna os últimos 10 códigos pela maior posição.

🔗 Exemplo:  
[https://gustavosmd4codes.pythonanywhere.com/codes/last/10](https://gustavosmd4codes.pythonanywhere.com/codes/last/10)

---

### 🔍 Verificar posição de um código

**GET** `/code/verify/<code>`  
Envia um código de 4 dígitos e retorna sua posição e avaliação de segurança.

🔗 Endpoint:  
[https://gustavosmd4codes.pythonanywhere.com/code/verify/1234](https://gustavosmd4codes.pythonanywhere.com/code/verify/1234)

**Requisição:**
```json
{
  "code": "1234"
}
