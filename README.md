# bootcamp-Dio

<div align="center">


</div>

Este repositório está em constante desenvolvimento de um sistema bancario, da bootcamp da Dio

## Objetivo

O objetivo deste script é desenvolver o backend de um sistema bancario:


## Funçoes do script

O script é composto por algumas funções:

1. **depositar**.
    <br> parametros `saldo, valor, extrato`.
   gerencia os depositos feitos na conta.

3. **Sacar**:
    <br> parametros `saldo, valor, extrato, limite, numero_de_saques, limite_de_saques`.
   gerencia os saques feitos na conta tendo com requisitos, valor maximo, e numero maximo de saques oor dia

5. **criar_Usuario**:
   <br> parametros `usuarios` tipo list
   Gerencia a criação de usuarios
   
7. **A criar_Conta**:
    <br> parametros `agencia,numero_conta, usuarios`
   Gerencia a criação de contas,com requuisito de somente um usuario por conta

9. **lista_contas**:
   <br> parametros `contas` tipo list
   Mostra todas as contas cadstradas

7. **filtar_Usuario**:
   <br> parametros `cpf, usuario` tipo list
   Analiza se o usuario existe ou não retorna True ou False

7. **menu**:
   <br> Não rece parametros
   exibe na tela um menu de interação com o usuario

7. **main**:
   <br> não recebe parametros
  Responsavel pela execução rapida do scrip
   
