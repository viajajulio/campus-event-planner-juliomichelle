# Planejador de Eventos do Campus   
# Evento inicial
evento = { 
    "id": 1,
    "nome": "ConectaIF",
    "descricao": "Encontro de educação profissional científica e tecnologia",
    "categoria": "tecnologia",
    "organizador": "IFB",
    "contato": "comunicacao@ifb.edu.br",
    "site": "conectaif.ifb.edu.br",
    "local": "Arena BRB, Brasília",
    "data": "2025-10-07",
    "hora_inicio": "09:00",
    "hora_fim": "18:00",
    "capacidade": 2000,
    "participantes": ["Maria", "João", "Ana"],
    "preco_ingresso": 100.00,
    "tipo": "presencial",
    "status": "agendado",
    "programacao": [
        {"hora": "09:00", "atividade": "Show de Abertura", "categoria": "educacao"},
        {"hora": "10:00", "atividade": "Palestra: Futuro da IA", "categoria": "inteligencia artificial"},
        {"hora": "14:00", "atividade": "Painel: Startups brasileiras", "categoria": "trabalho"},
        {"hora": "16:00", "atividade": "Sessão de Networking e Encerramento", "categoria": "trabalho"},
        {"hora": "18:00", "atividade": "Show de Encerramento", "categoria": "educacao"}
    ],
    "patrocinadores": ["IFB", "Ministério do Desenvolvimento", "ABDI"],
    "participado": False 
}

# Lista de eventos começa com o ConectaIF
eventos = [evento]

def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome or not data or not local or not categoria:
        print("Todos os campos são obrigatórios.")
        return False

    if not validarData(data):
        print("Data inválida! Use o formato AAAA-MM-DD.")
        return False

    novo_id = len(listaEventos) + 1
    evento = {
        "id": novo_id,
        "nome": nome,
        "descricao": "Descrição não definida",
        "categoria": categoria,
        "organizador": "A definir",
        "contato": "email@exemplo.com",
        "site": "http://site.com",
        "local": local,
        "data": data,
        "hora_inicio": "00:00",
        "hora_fim": "00:00",
        "capacidade": 100,
        "participantes": [],
        "preco_ingresso": 0.0,
        "tipo": "presencial",
        "status": "agendado",
        "programacao": [],
        "patrocinadores": [],
        "participado": False
    }

    listaEventos.append(evento)
    print(f" Evento '{nome}' adicionado com sucesso!")
    return True

def listarEventos(listaEventos):
    if not listaEventos:
        print("Nenhum evento cadastrado.")
        return
    print("Lista de eventos: ")
    for evento in listaEventos:
        print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']}")


def procurarEventoPorNome(listaEventos, nome):
    encontrados = [ev for ev in listaEventos if nome.lower() in ev['nome'].lower()]
    if encontrados:
        print(f"Eventos encontrados com '{nome}':")
        for evento in encontrados:
            print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']}")
    else:
        print(f"Nenhum evento encontrado com o nome '{nome}'.")


def deletarEvento(listaEventos, id):
    for evento in listaEventos:
        if evento["id"] == id:
            listaEventos.remove(evento)
            print(f"Evento '{evento['nome']}' removido com sucesso!")
            return True
    print(f"Nenhum evento encontrado com ID {id}.")
    return False        

def validarData(dataStr):

    if len(dataStr) != 10:
        return False
    else:
        try:
            ano = int(dataStr[:4])
            mes = int(dataStr[5:7])
            dia = int(dataStr[8:])
            print(ano , mes , dia)
            if (ano < 1900):
                return False
            if ( mes < 1 or mes > 12 ):
                print("Mes invalido")
                return False
            if (  dia < 1 or dia > 31 ):
                print("Dia invalido")
                return False
                
            return True
        except:
            return False  


#Menu
def displayMenu():
    print("+--------------------------------------------------+")
    print("|      IFCONECTA - Guia e Planejamento             |")
    print("+--------------------------------------------------+")
    print("|                                                  |")
    print("| 1. Detalhes de um Evento                         |")
    print("| 2. Programação de um Evento                      |")
    print("| 3. Filtrar Programação por Categoria             |") 
    print("| 4. Mapa do Evento (Local)                        |")
    print("| 5. Ingressos                                     |")
    print("| 6. Adicionar Novo Evento                         |")
    print("| 7. Marcar Evento como Participado                |")
    print("| 8. Gerar Relatório Geral                         |")
    print("| 9. Listar Todos os Eventos                       |")
    print("| 10. Excluir Evento                               |")
    print("|--------------------------------------------------|")
    print("| [0] Sair                                         |")
    print("|--------------------------------------------------|")

def mostrarDetalhesEvento(evento):
#Exibe o local, data, hora e informações de contato.
    print(" DETALHES DO EVENTO ")
    print(f"Nome: {evento['nome']}")
    print(f"Status: {evento['status'].capitalize()}")
    print(f"Local: {evento['local']}")
    print(f"Data/Hora: {evento['data']} das {evento['hora_inicio']} às {evento['hora_fim']}")
    print(f"Organizador: {evento['organizador']} | Contato: {evento['contato']}")


def mostrarProgramacao(evento):
#Lista as atividades e horários da programação/palestras.
    print(" PROGRAMAÇÃO ")
    if evento.get('programacao'):
        for item in evento['programacao']:
            print(f"  > {item['hora']}: {item['atividade']}")
    else:
        print("Programação detalhada não disponível.")

def listarCategorias(listaAtividades):
    categorias_unicas = set()
    for item in listaAtividades:
        categoria = item.get('categoria', None)
        if categoria:
            categorias_unicas.add(categoria.capitalize())
            
            
    if categorias_unicas:
        print("\n--- Categorias Disponíveis ---")
      
        print(", ".join(sorted(list(categorias_unicas))))
        print("------------------------------")
    else:
        print("Nenhuma categoria definida na programação.")

def mostrarMapaLocal(evento):
#Exibe o endereço e o site para o mapa do evento.
    print(" MAPA E LOCALIZAÇÃO ")
    print(f"Endereço: {evento['local']}")
    print(f"Instruções: Utilize o site oficial para visualizar o mapa completo e direções.")
    print(f"Site Oficial (Mapa): {evento['site']}")


def mostrarIngressos(evento):
#Exibe informações de capacidade e preço do ingresso.
    print(" INFORMAÇÕES DE INGRESSOS ")
    print(f"Tipo: {evento['tipo'].capitalize()}")
    print(f"Preço: R$ {evento['preco_ingresso']:.2f}")
    print(f"Capacidade Total: {evento['capacidade']} participantes")
    print("Para compra, visite o site oficial.")

def filtrarProgramacao(listaAtividades, termo):
    termo = termo.lower()
    encontrados = [
        item for item in listaAtividades
        if termo in item['atividade'].lower() or termo in item['categoria'].lower()
    ]
    
    if encontrados:
        print("\nAtividades encontradas:")
        for item in encontrados:
            print(f"  > {item['hora']}: {item['atividade']} ({item['categoria']})")
    else:
        print("Nenhuma atividade encontrada com esse termo.")

def gerarRelatorio(evento):
    print(" RELATÓRIO DO EVENTO ")
    print(f"Nome: {evento['nome']}")
    print(f"Data: {evento['data']} das {evento['hora_inicio']} às {evento['hora_fim']}")
    print(f"Local: {evento['local']}")
    print(f"Participantes Confirmados: {len(evento['participantes'])}")
    print(f"Capacidade Restante: {evento['capacidade'] - len(evento['participantes'])}")
    print(f"Total Arrecadado: R$ {len(evento['participantes']) * evento['preco_ingresso']:.2f}")


def main():
    displayMenu()
    try:
        escolha = int(input(">> Escolha uma opção [0-10]: "))
    except ValueError:
        print("Entrada inválida. Digite apenas o número da opção.")
        return  # encerra o programa
    
    if escolha == 0:
        print("Saindo do Guia Interativo. Até mais!")

    elif escolha == 1:  # Detalhes
        listarEventos(eventos)
        try:
            id_ev = int(input("Digite o ID do evento: "))
            ev = next((e for e in eventos if e["id"] == id_ev), None)
            if ev:
                mostrarDetalhesEvento(ev)
            else:
                print("Evento não encontrado.")
        except ValueError:
            print("ID inválido.")

    elif escolha == 2:  # Programação
        listarEventos(eventos)
        id_ev = int(input("Digite o ID do evento: "))
        ev = next((e for e in eventos if e["id"] == id_ev), None)
        if ev:
            mostrarProgramacao(ev)

    elif escolha == 3:  # Filtrar programação
        listarEventos(eventos)
        id_ev = int(input("Digite o ID do evento: "))
        ev = next((e for e in eventos if e["id"] == id_ev), None)
        if ev:
            listarCategorias(ev['programacao'])
            termo = input("Digite Categoria OU palavra-chave para buscar: ")
            filtrarProgramacao(ev['programacao'], termo)

    elif escolha == 4:
        listarEventos(eventos)
        id_ev = int(input("Digite o ID do evento: "))
        ev = next((e for e in eventos if e["id"] == id_ev), None)
        if ev:
            mostrarMapaLocal(ev)

    elif escolha == 5:
        listarEventos(eventos)
        id_ev = int(input("Digite o ID do evento: "))
        ev = next((e for e in eventos if e["id"] == id_ev), None)
        if ev:
            mostrarIngressos(ev)

    elif escolha == 6:  # Adicionar novo
        nome = input("Nome do novo evento: ")
        data = input("Data (AAAA-MM-DD): ")
        local = input("Local: ")
        categoria = input("Categoria: ")
        adicionarEvento(eventos, nome, data, local, categoria)

    elif escolha == 7:  # Marcar como participado
        listarEventos(eventos)
        id_ev = int(input("Digite o ID do evento: "))
        ev = next((e for e in eventos if e["id"] == id_ev), None)
        if ev:
            ev["participado"] = True
            print(f"Você marcou o evento '{ev['nome']}' como PARTICIPADO.")

    elif escolha == 8:  # Relatório
        listarEventos(eventos)
        id_ev = int(input("Digite o ID do evento: "))
        ev = next((e for e in eventos if e["id"] == id_ev), None)
        if ev:
            gerarRelatorio(ev)

    elif escolha == 9:  # Listar todos
        listarEventos(eventos)

    elif escolha == 10:  # Excluir
        listarEventos(eventos)
        try:
            id_ev = int(input("Digite o ID do evento a excluir: "))
            deletarEvento(eventos, id_ev)
        except ValueError:
            print("ID inválido.")

    else:
        print("Opção inválida. Escolha um número entre 0 e 10.")

