# lista4_arvore
nome | matrícula
-----|----------
Cleber José de Castro Júnior | 16/0025834
Victor Hugo Dias Coelho | 16/0019401

## Árvore vermelha e preta

Uma árvore rubro-negra é uma árvore de busca binária onde cada nó tem um atributo de cor, vermelho ou preto. Além dos requisitos ordinários impostos pelas árvores de busca binárias, as árvores rubro-negras tem os seguintes requisitos adicionais:

1. Um nó é vermelho ou preto.
2. A raiz é preta. (Esta regra é usada em algumas definições. Como a raiz pode sempre ser alterada de vermelho para preto, mas não sendo válido o oposto, esta regra tem pouco efeito na análise.)
3. Todas as folhas(nil) são pretas.
4. Ambos os filhos de todos os nós vermelhos são pretos.
5. Todo caminho de um dado nó para qualquer de seus nós folhas descendentes contem o mesmo número de nós pretos.

### Execução do código

Para executar utilize a versão 3 do python. Execute o comando:
> python3 main.py
