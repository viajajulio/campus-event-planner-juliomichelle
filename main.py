# Planejador de Eventos do Campus

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
        {"hora": "10:00", "atividade": "Palestra: Futuro da IA"},
        {"hora": "14:00", "atividade": "Painel: Startups brasileiras"}
    ],
    "patrocinadores": ["IFB", "Ministério do Desenvolvimento", "ABDI"]
}


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
        "data": data,
        "local": local,
        "categoria": categoria
    }

    listaEventos.append(evento)
    print(f" Evento '{nome}' adicionado com sucesso!")
    return True


def listarEventos(listaEventos):
    if not listaEventos:
        print("Nenhum evento cadastrado.")
        return
    print("\n Lista de eventos:")
    for evento in listaEventos:
        print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']}")


def procurarEventoPorNome(listaEventos, nome):
    encontrados = [ev for ev in listaEventos if nome.lower() in ev['nome'].lower()]
    if encontrados:
        print(f"\n Eventos encontrados com '{nome}':")
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


