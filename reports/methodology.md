# Metodologia e qualidade dos dados

## Base

O arquivo de exercício contém 6.454 registros, cobrindo 1998–2017, com as colunas `year`, `state`, `month`, `number` e `date`.

Não foram identificados valores ausentes.

## Limpeza conservadora

Foi removida apenas uma duplicata claramente identificável: `Alagoas`, `Janeiro`, `2017`, `number = 38.0`, que aparece duas vezes.

Outras linhas aparentemente repetidas não foram removidas porque alguns rótulos territoriais agrupam múltiplas séries. Sem uma fonte externa que permita desambiguar esses nomes, não é metodologicamente seguro atribuí-los a UFs específicas.

## Reconstrução temporal

A coluna `date` não representa o mês do registro: ela aparece como `01/01` do respectivo ano. Por isso, o projeto reconstrói uma variável `period` a partir de `year + month`.

## Recorte anual

2017 contém apenas janeiro a novembro. Para comparações anuais equivalentes, os resultados anuais e sazonais utilizam os anos completos de 1998 a 2016.

## Unidade e causalidade

O arquivo não documenta formalmente a unidade da coluna `number`. Os resultados são apresentados como soma/valor dessa coluna. A análise é descritiva e não atribui causalidade às variações observadas.
