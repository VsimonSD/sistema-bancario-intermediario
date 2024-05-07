### Proposta do Exercício:

Criar um sistema bancário simples em Python aplicando conceitos básicos:

- Criação e atribuição de variáveis (e constantes)
- Estrutura de repetição
- Estrutura de decisão

Além de atualizá-lo aplicando o conceito de:

- Funções
- Listas
- Tuplas
- Dicionários

O 'sisteminha' deve dar cinco opções de operação: Depósito, saque, extrato, criar usuário, criar conta. Além de respeitar os seguintes critérios:

| Se for   | Deve                                                         |
| -------- | ------------------------------------------------------------ |
| Depósito | Aceitar valores float acima de 0 e a quantidade de depósitos deve ser armazenada em uma variável. |
| Saque    | Aceitar saques de até R$500,00 reais, impedir o usuário de efetuar mais de três saques em um dia, além de também o impedir de efetuar saques de valor superior ao saldo em conta. |
| Extrato  | Exibir quantos depósitos e saques foram efetuados, além do valor restante em conta. Em caso de ausência de movimentações, o sistema informa. |
| Criar User  | Ler CPF (apenas números), nome, data de nascimento, endereço e armazenar tudo em uma lista. Não podem existir dois users com mesmo CPF. |
| Criar conta  | Ler CPF para verificar se o usuário existe, agencia (constante), numero_conta (variável com incremento, usuário e adicionar tudo em uma lista. O mesmo usuário pode ter mais de uma conta |

Por fim, também deve ter a opção de 'sair' caso o usuário queira.

Este sistema foi finalizado com auxílio do professor. Para "melhorar" em relação ao que foi proposto e apresentado na resolução, foi implementada uma melhoria no contador de saques diários que estava com um bug que permitia o usuário efetuar mais de três saques. Também foi adicionada a opção de listar usuários.
