from cpu import CPU
from programas import carregar_programa_exemplo, carregar_programa_grupo

def executar_e_exibir(titulo, funcao_carregamento):
    print("=" * 45)
    print(f"       {titulo}")
    print("=" * 45)
    
    cpu = CPU()
    funcao_carregamento(cpu)
    cpu.executar()
    
    print("\n" + "=" * 45)
    print("RESULTADO FINAL")
    print("=" * 45)
    cpu.mostrar_estado()
    print("Memória Relevante:")
    for i in range(len(cpu.memoria)):
        if cpu.memoria[i] != 0:
            print(f"  MEM[{i:02d}] = {cpu.memoria[i]}")
    print("\n")


if __name__ == "__main__":
    executar_e_exibir("PROGRAMA DE EXEMPLO (5 + 8)", carregar_programa_exemplo)
    executar_e_exibir("PROGRAMA DO GRUPO (9 INSTRUÇÕES)", carregar_programa_grupo)
