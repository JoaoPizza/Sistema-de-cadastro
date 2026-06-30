# Sistema-de-cadastro
Um sistema de cadastro feito com python.

> Um projeto autoral desenvolvido como laboratório de aprendizado, onde cada funcionalidade surgiu de uma necessidade real durante o próprio desenvolvimento.

---

## Sobre o projeto

Este projeto começou de forma extremamente simples.

A ideia inicial era apenas criar um sistema de cadastro de usuários para praticar os primeiros conceitos da linguagem Python. Em nenhum momento a intenção foi criar um sistema bancário ou reproduzir um projeto encontrado em tutoriais.

Conforme fui aprendendo novos conceitos, decidi seguir um caminho diferente do tradicional: ao invés de iniciar diversos projetos pequenos, escolhi fazer **um único projeto crescer comigo**.

Cada novo assunto estudado precisava encontrar uma aplicação prática dentro do sistema.

Por esse motivo, este projeto acabou se tornando um registro da minha própria evolução como desenvolvedor.

---

## Filosofia de desenvolvimento

Durante todo o desenvolvimento procurei seguir uma ideia muito simples:

> **Primeiro fazer funcionar. Depois fazer direito.**

Nunca tive a preocupação de escrever o código mais bonito logo na primeira tentativa.

Meu foco sempre foi entender o problema, fazê-lo funcionar e somente depois voltar para organizar responsabilidades, modularizar e refatorar quando aquilo realmente passasse a fazer sentido.

Essa forma de trabalhar fez com que praticamente todas as refatorações surgissem por necessidade, e não apenas por questões estéticas.

---

# Linha do tempo

## Primeiros passos

A primeira versão do projeto era extremamente simples.

O sistema era responsável apenas por coletar informações do usuário e armazená-las.

Nessa fase o objetivo era entender:

* funções;
* dicionários;
* manipulação básica de dados;
* organização inicial do código.

Mesmo sendo simples, foi a base que permitiu toda a evolução posterior.

---

## Organização em módulos

À medida que o projeto começou a crescer, ficou evidente que manter toda a lógica em um único arquivo deixaria o código difícil de manter.

Foi então que surgiu a primeira grande refatoração.

Os dados passaram a ser separados por responsabilidade.

```text
dados_pessoais.py

dados_residen.py

banco.py

main.py
```

Essa mudança tornou o projeto muito mais organizado e facilitou a implementação de novas funcionalidades.

---

## Persistência de dados

Inicialmente todas as informações eram gravadas em arquivos TXT.

Para a proposta inicial isso funcionava perfeitamente.

O problema apareceu quando comecei a pensar em autenticação de usuários.

Percebi que localizar registros específicos, validar contas e manipular informações utilizando apenas TXT deixaria o projeto cada vez mais limitado.

Foi nesse momento que decidi realizar a maior mudança estrutural do projeto.

---

## Migração completa para JSON

Essa foi, sem dúvida, a etapa mais desafiadora de todo o desenvolvimento.

Toda a estrutura de persistência precisou ser repensada.

Foi durante essa mudança que precisei compreender conceitos como:

* serialização;
* desserialização;
* referências em memória;
* listas;
* dicionários;
* `json.load()`;
* `json.dump()`.

Grande parte desse conhecimento não veio diretamente do curso.

Pesquisei documentação, li diferentes abordagens, fiz inúmeros testes e somente depois implementei a solução da forma que fazia sentido para mim.

Essa etapa consumiu muitas horas até que toda a arquitetura estivesse funcionando corretamente.

Hoje considero que foi o momento de maior aprendizado dentro do projeto.

---

## Sistema de autenticação

Com a migração concluída tornou-se possível implementar um sistema de autenticação baseado em:

* número da conta;
* senha;
* validação dos dados diretamente na base.

Esse foi um ponto importante do projeto porque mostrou, na prática, o motivo pelo qual a migração para JSON havia sido necessária.

---

## Módulo bancário

Com a infraestrutura pronta, a evolução natural do projeto foi a implementação de operações bancárias.

Atualmente o sistema possui:

* consulta de saldo;
* depósito;
* saque;
* transferência entre contas.

Todas essas operações utilizam a mesma base de dados e atualizam corretamente os registros persistidos.

Uma das implementações que mais gostei foi a transferência entre contas.

Inicialmente imaginei que seria uma funcionalidade extremamente complexa.

Durante o desenvolvimento percebi que ela era composta por várias pequenas partes que eu já havia construído anteriormente.

A autenticação, a busca do usuário, a validação da conta e a atualização do saldo já existiam.

A transferência acabou sendo a união desses blocos.

Essa percepção mudou bastante minha forma de enxergar problemas maiores.

---

## Refatorações

Uma característica constante durante todo o desenvolvimento foi revisar o próprio código.

Sempre que alguma parte começava a concentrar responsabilidades demais, ela era reorganizada.

Um exemplo claro foi o `main.py`.

Inicialmente ele possuía praticamente toda a lógica do sistema.

Com o crescimento do projeto isso deixou de fazer sentido.

Grande parte das responsabilidades foi movida para o módulo bancário.

Hoje o arquivo principal atua apenas como controlador do fluxo da aplicação.

Essa foi uma mudança simples, mas que tornou o código muito mais organizado e fácil de evoluir.

---

# Tecnologias utilizadas

* Python
* JSON
* Programação Orientada a Objetos
* Manipulação de arquivos
* Modularização
* Git

---

# O que este projeto me ensinou

Mais do que aprender comandos da linguagem, este projeto me ensinou a resolver problemas.

Durante o desenvolvimento precisei pesquisar conceitos que ainda não conhecia, entender como funcionavam e adaptá-los à realidade do projeto.

Sempre procurei evitar simplesmente copiar soluções prontas.

Minha preocupação era compreender o motivo de determinada solução funcionar para então implementá-la utilizando minha própria lógica.

Essa forma de estudar fez com que praticamente todas as funcionalidades fossem construídas sobre conhecimentos realmente assimilados.

---

# Próximos passos

O projeto continuará evoluindo.

Algumas melhorias planejadas são:

* migração para banco de dados relacional;
* histórico de transações;
* criptografia/hash de senhas;
* API utilizando FastAPI;
* testes automatizados;
* interface gráfica ou aplicação web.

---

# Considerações finais

Este projeto nunca teve a intenção de ser um sistema bancário completo.

Ele também nunca teve a intenção de ser um projeto feito para seguir um tutorial.

Desde o início, o objetivo foi criar um ambiente onde eu pudesse transformar cada novo conhecimento em uma funcionalidade real.

O resultado é um projeto que cresceu junto comigo.

Cada versão representa um momento diferente da minha evolução como desenvolvedor, registrando não apenas novas funcionalidades, mas principalmente novas formas de pensar e resolver problemas.