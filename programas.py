def carregar_programa_exemplo(cpu):
    """
    Programa de exemplo fornecido na especificação (Item 7):
    Calcula 5 + 8 e armazena o resultado na posição 15 da memória.
    """
    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 15"
    cpu.memoria[4] = "HALT"


def carregar_programa_grupo(cpu):
    """
    Programa próprio do grupo (Item 11):
    Possui 9 instruções e utiliza LOAD, STORE e operações da ULA (ADD, SUB, XOR).
    
    Explicação do programa:
    1. Carrega o valor 20 em R0.
    2. Carrega o valor 10 em R1.
    3. Soma R0 + R1 (R0 passa a ser 30).
    4. Grava 30 na posição 10 da memória.
    5. Carrega o valor 5 em R2.
    6. Subtrai R1 - R2 (R1 passa a ser 5).
    7. Executa operação bitwise XOR entre R0 e R1 (30 XOR 5 = 27 em R0).
    8. Salva o resultado final na posição 14 da memória.
    9. Encerra a execução.
    """
    cpu.memoria[0] = "LOAD R0, 20"
    cpu.memoria[1] = "LOAD R1, 10"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 10"
    cpu.memoria[4] = "LOAD R2, 5"
    cpu.memoria[5] = "SUB R1, R2"
    cpu.memoria[6] = "XOR R0, R1"
    cpu.memoria[7] = "STORE R0, 14"
    cpu.memoria[8] = "HALT"