"""
    *** DATASET REPORT ***
    
    Vamos obter informações sobre o rendimento de alunos de um curso em algumas
    disciplinas ao longo dos anos.

    O primeiro arquivo (dataset.csv), refere-se ao aproveitamento de estudantes 
    na disciplina ALGORITMOS 1 entre os anos de 2011 e 2022.

    A primeira coluna (matricula) é composta por números inteiros, onde 
    cada número representa um indivíduo. Assim, repetições nessa coluna indicam 
    que o estudante fez mais de uma vez a mesma matéria.

    Atenção: 
    R-nota indica REPROVAÇÃO POR NOTA
    R-freq REPROVAÇÃO POR FALTA 
    Se houver outro "status" para representar reprovação, este dever ser 
    trocado para o rótulo adequado (R-nota ou R-freq). 
    Frequências < 75 causam reprovação por falta; 
    Médias abaixo de 50 causam reprovação por nota.

    Analise o dataset do referido arquivo para responder as seguintes perguntas:

    1.  Qual é a média de nota dos aprovados (no período total e por ano)?
    2.  Qual é a média de nota dos reprovados por nota (período total e ano)?
    3.  Qual é a frequência dos reprovados por nota (período total e por ano)?
    4.  Qual a porcentagem de evasões (total e anual)?
    5.  Como os anos de pandemia impactaram no rendimento dos estudantes em 
        relação aos anos anteriores, considerando o rendimento dos aprovados, a taxa 
        de cancelamento e as reprovações? Considere como anos de pandemia 
        os anos de 2020 e 2021.
    6.  Compare a volta às aulas híbrida (2022 período 1) com os anos de 
        pandemia e os anos anteriores.
    7.  Compare a volta às aulas presencial (2022 período 2) com a volta 
        híbrida do item anterior.
"""