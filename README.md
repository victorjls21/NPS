# 📊 Pesquisa de Satisfação - NPS

Este projeto implementa uma pesquisa de satisfação no modelo **Net Promoter Score (NPS)**, permitindo registrar notas de clientes e calcular automaticamente a classificação do desempenho da empresa.

---

## 🚀 Como funciona

O **NPS** é uma métrica que mede a lealdade dos clientes com base em uma única pergunta:

> "Em uma escala de 0 a 10, o quanto você recomendaria nossa empresa para um amigo ou colega?"

As respostas são classificadas assim:

- **0 a 6** → Detratores (clientes insatisfeitos)  
- **7 a 8** → Neutros (clientes satisfeitos, mas não entusiastas)  
- **9 a 10** → Promotores (clientes muito satisfeitos)

O cálculo é feito com a fórmula:

```text
NPS = % de Promotores − % de Detratores
