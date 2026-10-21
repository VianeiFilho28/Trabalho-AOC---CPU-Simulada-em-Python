# CPU Simulada — Código-base
## AOC 2026.2
## Alunos: Gabriel Farias Magalhães- 581758 e José Vianei Castro e Silva Filho - 580381

### Descrição do Trabalho:

Implementação de uma pequena CPU simulada em Python.

A proposta é integrar, em um único projeto, conceitos de ULA, registradores, memória, instruções e ciclo de execução de uma CPU. 
A CPU tem: dados de 8 bits, quatro registradores, uma
memória de 16 posições e um conjunto reduzido de instruções.

### Arquivos:

- ula.py — ULA e operações aritméticas/lógicas.
- cpu.py — estrutura principal da CPU.
- main.py — programa de demonstração.
- testes.py — testes das partes já implementadas.

### Como executar:

No terminal, dentro da pasta:

```bash
python main.py
```

Para executar os testes:

```bash
python testes.py
```

### Exemplo:

O main.py contém:

```text
0: LOAD R0, 5
1: JMP 4
2: LOAD R0, 99
3: HALT
4: LOAD R1, 8
5: HALT
```

A instrução `JMP 4` faz a CPU saltar da posição 1 para a posição 4.

Portanto:

```text
R0 = 5
R1 = 8
```

A instrução `LOAD R0, 99` não será executada.