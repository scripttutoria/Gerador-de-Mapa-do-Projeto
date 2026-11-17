# mapeador_final_v4.py

import os
import sys
import subprocess

# --- CONFIGURAÇÕES ---
PASTAS_A_IGNORAR = {
    '__pycache__', '.git', '.vscode', 'node_modules', 'venv', '.idea', 'dist', 'build',
}
ARQUIVOS_A_IGNORAR = {
    '.DS_Store', 'mapeador_final_v4.py' # Nome do próprio script para não se incluir
}
# Extensões de arquivos binários ou de mídia a serem ignorados pela LEITURA DE CONTEÚDO
EXTENSOES_A_IGNORAR_CONTEUDO = {
    '.mp3', '.mp4', '.webm', '.mkv', '.avi', '.mov', '.flv',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg',
    '.exe', '.dll', '.so', '.o', '.a', '.lib', '.zip', '.rar', '.gz', '.tar'
}
# Mapeamento de extensões para linguagens do Markdown para syntax highlighting
MAPA_LINGUAGENS = {
    '.py': 'python',
    '.js': 'javascript',
    '.html': 'html',
    '.css': 'css',
    '.md': 'markdown',
    '.json': 'json',
    '.sh': 'bash',
    '.bat': 'batch',
    '.xml': 'xml',
    '.yaml': 'yaml',
    '.yml': 'yaml',
    '.sql': 'sql',
    '.txt': 'text',
    '.log': 'text',
}
# --- FIM DAS CONFIGURAÇÕES ---

def percorrer_projeto(caminho_do_projeto):
    """
    Percorre o projeto e gera informações sobre cada pasta e arquivo.
    Yield: (caminho_relativo, nome, eh_pasta)
    """
    for raiz, pastas, arquivos in os.walk(caminho_do_projeto, topdown=True):
        pastas[:] = sorted([p for p in pastas if p not in PASTAS_A_IGNORAR])
        arquivos_filtrados = sorted([a for a in arquivos if a not in ARQUIVOS_A_IGNORAR])

        for nome_pasta in pastas:
            caminho_completo = os.path.join(raiz, nome_pasta)
            yield os.path.relpath(caminho_completo, caminho_do_projeto), nome_pasta, True

        for nome_arquivo in arquivos_filtrados:
            caminho_completo = os.path.join(raiz, nome_arquivo)
            yield os.path.relpath(caminho_completo, caminho_do_projeto), nome_arquivo, False

def gerar_arvore_diretorios(caminho_do_projeto):
    """Gera uma string formatada da árvore de diretórios."""
    print("Gerando a árvore de diretórios...")
    linhas_arvore = [f"**ÁRVORE DE DIRETÓRIOS**\n\n```"]
    linhas_arvore.append(f"{os.path.basename(os.path.normpath(caminho_do_projeto))}/")
    
    estrutura = {}
    for caminho_rel, nome, eh_pasta in percorrer_projeto(caminho_do_projeto):
        partes = caminho_rel.split(os.sep)
        ponteiro = estrutura
        for parte in partes:
            ponteiro = ponteiro.setdefault(parte, {})
    
    def construir_linhas(sub_estrutura, prefixo):
        itens = sorted(sub_estrutura.keys())
        for i, nome in enumerate(itens):
            conector = '└── ' if i == len(itens) - 1 else '├── '
            linhas_arvore.append(f"{prefixo}{conector}{nome}")
            if sub_estrutura[nome]:
                prefixo_filho = prefixo + ('    ' if conector == '└── ' else '│   ')
                construir_linhas(sub_estrutura[nome], prefixo_filho)

    construir_linhas(estrutura, "")
    linhas_arvore.append("```")
    return "\n".join(linhas_arvore)

def ler_conteudo_dos_arquivos(caminho_do_projeto):
    """Lê e formata o conteúdo de todos os arquivos de texto no novo formato Markdown."""
    print("Lendo e formatando o conteúdo dos arquivos...")
    conteudo_completo = []
    nome_base_projeto = os.path.basename(os.path.normpath(caminho_do_projeto))

    for caminho_rel, nome_arquivo, eh_pasta in percorrer_projeto(caminho_do_projeto):
        if eh_pasta:
            continue

        _, extensao = os.path.splitext(nome_arquivo)
        if extensao.lower() in EXTENSOES_A_IGNORAR_CONTEUDO:
            continue

        try:
            caminho_completo = os.path.join(caminho_do_projeto, caminho_rel)
            with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                conteudo = f.read()
            
            caminho_final_para_exibir = os.path.join(nome_base_projeto, caminho_rel).replace(os.sep, '/')
            
            # Novo formato de cabeçalho
            header = f"**Nome do arquivo:** `{nome_arquivo}`\n**Caminho:** `{caminho_final_para_exibir}`"
            
            # Determina a linguagem para o bloco de código
            linguagem = MAPA_LINGUAGENS.get(extensao.lower(), 'text')
            
            # Monta o bloco de código Markdown
            bloco_codigo = f"```{linguagem}\n{conteudo.strip()}\n```"
            
            conteudo_completo.append(f"{header}\n\n{bloco_codigo}")

        except Exception as e:
            conteudo_completo.append(f"**Nome do arquivo:** `{nome_arquivo}`\n**Caminho:** `{caminho_final_para_exibir}`\n\n!! ERRO AO LER O ARQUIVO: {e}")
    
    return "\n\n---\n\n".join(conteudo_completo) # Usa um separador mais visual entre os arquivos

def obter_dependencias_venv(caminho_do_projeto):
    """Executa 'pip freeze' no venv do projeto para obter as dependências."""
    print("Verificando dependências do venv...")
    venv_path = os.path.join(caminho_do_projeto, 'venv')
    
    if sys.platform == "win32":
        pip_executable = os.path.join(venv_path, 'Scripts', 'pip.exe')
    else:
        pip_executable = os.path.join(venv_path, 'bin', 'pip')

    if not os.path.exists(pip_executable):
        return "**DEPENDÊNCIAS DO AMBIENTE VIRTUAL (venv/pip freeze)**\n\n> `AVISO: Ambiente virtual 'venv' ou executável 'pip' não encontrado.`\n"

    try:
        resultado = subprocess.check_output([pip_executable, 'freeze'], encoding='utf-8', stderr=subprocess.STDOUT)
        header = "**DEPENDÊNCIAS DO AMBIENTE VIRTUAL (venv/pip freeze)**"
        return f"{header}\n\n```text\n{resultado.strip()}\n```\n"
    except Exception as e:
        return f"**DEPENDÊNCIAS DO AMBIENTE VIRTUAL (venv/pip freeze)**\n\n> `ERRO: {e}`\n"

def obter_versao_python(caminho_do_projeto):
    """Lê o conteúdo do arquivo .python-version."""
    print("Verificando arquivo .python-version...")
    path_arquivo_versao = os.path.join(caminho_do_projeto, '.python-version')

    if not os.path.exists(path_arquivo_versao):
        return "" 

    try:
        with open(path_arquivo_versao, 'r', encoding='utf-8') as f:
            versao = f.read().strip()
        header = "**VERSÃO DO PYTHON (.python-version)**"
        return f"{header}\n\n```text\n{versao}\n```\n"
    except Exception as e:
        return f"**VERSÃO DO PYTHON (.python-version)**\n\n> `ERRO ao ler o arquivo: {e}`\n"

def menu_principal():
    """Exibe o menu interativo para o usuário."""
    while True:
        print("\n--- Mapeador de Projetos (v4 Markdown Otimizado) ---")
        caminho_projeto = input("➡️ Insira o caminho completo para a pasta do projeto: ").strip()

        if not os.path.isdir(caminho_projeto):
            print(f"\n❌ ERRO: O caminho '{caminho_projeto}' não é uma pasta válida.")
            if input("Deseja tentar novamente? (s/n): ").lower() != 's': break
            continue

        incluir_venv = input("❔ Deseja incluir as dependências da 'venv' (pip freeze)? (s/n): ").lower().strip() == 's'
        incluir_python_version = input("❔ Deseja incluir o arquivo '.python-version'? (s/n): ").lower().strip() == 's'
        
        # Lógica para evitar redundância:
        if incluir_python_version:
            ARQUIVOS_A_IGNORAR.add('.python-version')

        nome_saida_padrao = f"mapeamento_{os.path.basename(os.path.normpath(caminho_projeto))}.md" # Alterado para .md
        nome_arquivo_saida = input(f"➡️ Digite o nome do arquivo de saída (ou Enter para '{nome_saida_padrao}'): ").strip() or nome_saida_padrao
        ARQUIVOS_A_IGNORAR.add(nome_arquivo_saida)

        try:
            venv_str = obter_dependencias_venv(caminho_projeto) if incluir_venv else ""
            python_version_str = obter_versao_python(caminho_projeto) if incluir_python_version else ""
            arvore_str = gerar_arvore_diretorios(caminho_projeto)
            conteudo_str = ler_conteudo_dos_arquivos(caminho_projeto)

            print(f"Escrevendo o arquivo de saída em: {os.path.abspath(nome_arquivo_saida)}")
            with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
                if python_version_str:
                    f.write(python_version_str)
                    f.write("\n\n")
                if venv_str:
                    f.write(venv_str)
                    f.write("\n\n")
                
                f.write(arvore_str)
                f.write("\n\n")

                f.write("**CONTEÚDO DOS ARQUIVOS**\n\n")
                f.write(conteudo_str)
            
            print(f"\n✅ Sucesso! Projeto mapeado em: {os.path.abspath(nome_arquivo_saida)}")

        except Exception as e:
            print(f"\n❌ ERRO INESPERADO: {e}")
        
        # Resetar ignorados para a próxima execução
        ARQUIVOS_A_IGNORAR.discard('.python-version')
        ARQUIVOS_A_IGNORAR.discard(nome_arquivo_saida)

        if input("\nDeseja mapear outro projeto? (s/n): ").lower() != 's':
            break

    print("\nObrigado por usar o script. Até logo!")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário. Saindo.")
        sys.exit(0)