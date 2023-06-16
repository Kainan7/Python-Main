# Python-Main
1.	Contextualização do Projeto
a.	Objetivos
Este código implementa um sistema simples de gerenciamento de vendas em uma loja. O objetivo do projeto é permitir que o usuário cadastre clientes,
liste os clientes cadastrados, remova clientes, adicione produtos ao carrinho de compras, remova produtos do carrinho, registre os pedidos e escolha 
um modo de pagamento.

b.	Visão Geral do Projeto
O projeto tem como objetivo simular um sistema de gerenciamento de     vendas em uma loja, permitindo o cadastro de clientes, seleção de produtos, 
adição e remoção de itens no carrinho de compras, escolha de modo de pagamento e registro dos pedidos.

2.	Dificuldades e Desafio
As maiores dificuldades foram o tanto de funções que precisei inserir e criar um laço entre elas junto com as estruturas de repetições.
O maior desafio do trabalho foi transformar o código em um executável, isso foi algo que precisei de mais tempo para entender como funcionava, 
precisei utilizar o terminal para instalar as ferramentas necessárias e então com êxito consegui concluir.


3.	Descrição da Implementação do Projeto
O código apresentado é uma implementação de um sistema de cadastro de clientes, venda de produtos e registro de pedidos em uma loja. O programa possui uma função principal main() que é responsável por exibir um menu para o usuário, onde ele pode escolher várias opções, como cadastrar um novo cliente, listar clientes, remover cliente, visualizar o menu de produtos, adicionar produtos ao carrinho de compras, exibir o carrinho de compras, remover itens do carrinho, selecionar o modo de pagamento, finalizar a compra e sair do programa. 
O programa utiliza arquivos de texto para armazenar os dados dos clientes e dos pedidos. Os produtos são representados como listas de dicionários, onde cada dicionário contém informações sobre o nome e preço de um produto específico.
A função cadastrar_cliente() permite ao usuário cadastrar um novo cliente, solicitando informações como e-mail, contato e nome. Ela valida o formato do e-mail e o número de contato antes de adicionar o cliente ao arquivo "clientes.txt".
A função listar_clientes() lê o arquivo "clientes.txt" e exibe na tela os dados de todos os clientes cadastrados.
A função remover_cliente() permite ao usuário digitar o e-mail de um cliente para removê-lo do arquivo "clientes.txt". Ela lê os clientes do arquivo, cria um novo arquivo sem o cliente a ser removido e renomeia o novo arquivo para substituir o original.
Existem outras funções auxiliares, como exibir_menu_produtos(),
exibir_produtos(), adicionar_item_carrinho(), exibir_carrinho(), remover_item_carrinho(), registrar_pedidos() e exibir_menu_pagamento(), que são responsáveis por exibir informações na tela e realizar operações relacionadas aos produtos, ao carrinho de compras e ao registro de pedidos.
No final, o programa utiliza a função main() para controlar o fluxo principal do programa. Ele exibe um menu para o usuário e solicita sua entrada para executar as diferentes opções disponíveis. O programa executa em um loop contínuo até que o usuário escolha a opção de sair. Durante a execução, o programa realiza as operações selecionadas pelo usuário, como cadastro de clientes, listagem de clientes, adição de produtos ao carrinho, escolha do modo de pagamento e finalização da compra.


4.	Referências
Não há referências específicas mencionadas no código fornecido. No entanto, o código em si é um exemplo simples de implementação de um sistema básico de gerenciamento de vendas, utilizando conceitos de entrada/saída de dados, manipulação de listas e arquivos.
