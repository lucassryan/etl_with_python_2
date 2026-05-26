# Pipeline ETL com Python
Projeto de construção de um pipeline ETL (Extract, Transform, Load) utilizando Python para tratamento e padronização de dados de vendas. O dataset foi gerado por I.A (Chat GPT).

---

## Objetivo
Fixar ainda mais a estrutura do pipeline ETL no tratamento de dados utilizando arquivos csv como entrada e saída.

---

## Tecnologias utilizadas
* Python
* Biblioteca `csv`
* Manipulação de dados com estruturas nativas (listas e dicionários)

## Observações
Neste segundo pipeline pude perceber que a estrutura para tratamento de arquivos csv se mantem a mesma, além disso durante o tratamento das datas, identifiquei um problema de ambiguidade de formato.

Exemplo:<br/>

23-03-24<br/>

Esse valor pode representar tanto:

* `DD-MM-YY`
* `YY-MM-DD`

Como não existe forma técnica de garantir o significado correto apenas pelo dado bruto, foi necessário definir uma regra de negócio para padronização das datas.

## Autor
Lucas Ryan<br/>
Projeto desenvolvido para estudo de Engenharia de Dados