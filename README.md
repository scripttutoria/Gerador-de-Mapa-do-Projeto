
# 🗺️ Mapeador de Projetos

Uma ferramenta Python para gerar documentação completa de projetos de software em formato Markdown, ideal para compartilhar com IAs, documentar código ou criar backups legíveis de estruturas de projeto.

## 📋 Sobre o Projeto

O **Mapeador de Projetos** é um script Python que percorre recursivamente uma pasta de projeto e gera um arquivo Markdown (`.md`) contendo:

- 📁 **Árvore de diretórios** visual e hierárquica
- 📄 **Conteúdo completo** de todos os arquivos de texto
- 🐍 **Versão do Python** (via `.python-version`)
- 📦 **Dependências do ambiente virtual** (via `pip freeze`)
- 🎨 **Syntax highlighting** automático por linguagem

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| 🌳 **Árvore de Diretórios** | Visualização hierárquica com conectores visuais (`├──`, `└──`) |
| 📝 **Formato Markdown** | Saída otimizada para leitura humana e por LLMs |
| 🎯 **Filtragem Inteligente** | Ignora automaticamente pastas como `__pycache__`, `.git`, `node_modules`, `venv` |
| 🚫 **Detecção de Binários** | Pula arquivos de mídia e executáveis automaticamente |
| 🎨 **Syntax Highlighting** | Mapeia extensões para linguagens Markdown (Python, JavaScript, HTML, etc.) |
| 📦 **Integração com venv** | Extrai dependências via `pip freeze` |
| 🔄 **Menu Interativo** | Interface amigável no terminal |
| 🖥️ **Multiplataforma** | Compatível com Windows, Linux e macOS |

## 🚀 Instalação

### Pré-requisitos

- Python 3.9.13 ou superior

### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/scripttutoria/mapeador-projetos.git
cd mapeador-projetos
```

2. **Execute o script:**
```bash
python Gerador_de_Mapa_do_Projeto.py
```

Não há dependências externas! O script utiliza apenas bibliotecas padrão do Python.

## 🎮 Como Usar

### Execução Básica

```bash
python Gerador_de_Mapa_do_Projeto.py
```

### Fluxo de Uso

```text
--- Mapeador de Projetos (v4 Markdown Otimizado) ---
➡️ Insira o caminho completo para a pasta do projeto: /caminho/do/seu/projeto
❔ Deseja incluir as dependências da 'venv' (pip freeze)? (s/n): s
❔ Deseja incluir o arquivo '.python-version'? (s/n): s
➡️ Digite o nome do arquivo de saída (ou Enter para 'mapeamento_projeto.md'): 
```

### Exemplo de Saída

O arquivo gerado terá a seguinte estrutura:

````markdown
**VERSÃO DO PYTHON (.python-version)**

```text
3.11.4
```

**DEPENDÊNCIAS DO AMBIENTE VIRTUAL (venv/pip freeze)**

```text
flask==2.3.2
requests==2.31.0
```

**ÁRVORE DE DIRETÓRIOS**

```
meu-projeto/
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
├── tests/
│   └── test_main.py
└── README.md
```

**CONTEÚDO DOS ARQUIVOS**

**Nome do arquivo:** `main.py`
**Caminho:** `meu-projeto/src/main.py`

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```
````

## ⚙️ Configuração

O script possui configurações editáveis no topo do arquivo:

### Pastas Ignoradas

```python
PASTAS_A_IGNORAR = {
    '__pycache__', '.git', '.vscode', 'node_modules', 
    'venv', '.idea', 'dist', 'build',
}
```

### Arquivos Ignorados

```python
ARQUIVOS_A_IGNORAR = {
    '.DS_Store', 'mapeador_final_v4.py'
}
```

### Extensões de Binários (Ignoradas na Leitura)

```python
EXTENSOES_A_IGNORAR_CONTEUDO = {
    '.mp3', '.mp4', '.jpg', '.png', '.exe', '.zip', ...
}
```

### Mapeamento de Linguagens

```python
MAPA_LINGUAGENS = {
    '.py': 'python',
    '.js': 'javascript',
    '.html': 'html',
    ...
}
```

## 📂 Estrutura do Projeto

```text
mapeador-projetos/
└── Gerador_de_Mapa_do_Projeto.py   # Script principal
```

## 🔧 Funções Principais

| Função | Descrição |
|--------|-----------|
| `percorrer_projeto()` | Gerador que percorre o projeto e filtra pastas/arquivos |
| `gerar_arvore_diretorios()` | Cria representação visual da árvore de pastas |
| `ler_conteudo_dos_arquivos()` | Lê e formata conteúdo em blocos de código Markdown |
| `obter_dependencias_venv()` | Executa `pip freeze` no ambiente virtual |
| `obter_versao_python()` | Lê arquivo `.python-version` |
| `menu_principal()` | Interface interativa no terminal |

## 🎯 Casos de Uso

- 🤖 **Compartilhar com IAs**: Formato ideal para enviar contexto de projeto para ChatGPT, Claude, etc.
- 📚 **Documentação**: Gerar documentação automática de código
- 🔍 **Revisão de Código**: Visualizar estrutura completa de um projeto
- 💾 **Backup Legível**: Criar snapshot textual do projeto
- 📖 **Onboarding**: Ajudar novos desenvolvedores a entender a estrutura

## 🖥️ Compatibilidade

| Sistema | Status |
|---------|--------|
| Windows | ✅ Suportado |
| Linux | ✅ Suportado |
| macOS | ✅ Suportado |

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

**scripttutoria**
- GitHub: [@scripttutoria](https://github.com/scripttutoria)

---

⭐ Se este projeto foi útil, considere dar uma estrela!
```

---

## ✅ O que já está pronto nesta versão

| Item | Status |
|------|:------:|
| Blocos de código aninhados corrigidos (4 backticks) | ✅ |
| Seu usuário `scripttutoria` no clone e no autor | ✅ |
| Bloco do "Fluxo de Uso" como `text` (evita renderizar emojis como código estranho) | ✅ |
| Estrutura do projeto como `text` | ✅ |
| Tabelas, emojis, links e headers funcionais | ✅ |

## 📌 Passos finais no GitHub

1. Acesse **https://github.com/scripttutoria** → entre no repositório
2. Clique em **"Add file" → "Create new file"**
3. Nomeie exatamente como **`README.md`** (maiúsculo)
4. Cole o conteúdo acima
5. Clique em **"Preview"** para conferir
6. Clique em **"Commit changes"**

> 💡 Se o repositório do mapeador ainda não existe, crie antes: **"New repository"** com o nome `mapeador-projetos` (ou `Gerador_de_Mapa_do_Projeto`) e depois adicione o `README.md` e o script `.py`.

Pronto! É só copiar e colar. 🚀
