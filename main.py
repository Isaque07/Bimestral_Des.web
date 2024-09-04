from flask import Flask, request, render_template, redirect
from model.model_2 import *

app = Flask(__name__)

# Função para selecionar um item da lista de dicionários
def pickItem(lista: list, id: int) -> dict:
    for item in lista:
        if item['id'] == id:
            return item
    raise Exception("Item Não Encontrado!!")

# Função para registrar as relações entre o Animal registrado e todas as outras tabelas
def registrar_relações(idFazendeiro: int, idPasto: int, idRaca: int):
    last_animalID = Obj_Animal.select_animais()[-1]['id']
    Obj_AFaz.add_Animal_Fazendeiro(last_animalID, idFazendeiro)
    Obj_ARaca.add_Animal_Raca(last_animalID, idRaca)
    Obj_APasto.add_Animal_Pasto(last_animalID, idPasto)

# Página Índice Inicial
@app.route('/')
def index():
    return render_template('index.html')

# Páginas da Entidade Animais

# View da Tabela Animais
@app.route('/animais')
def list_animais():
    all_animais = Obj_Animal.select_animais()
    AFazendeiros = Obj_AFaz.select_registrosAFaz()
    ARacas = Obj_ARaca.select_registrosARaca()
    APastos = Obj_APasto.select_registrosAP()
    return render_template('viewanimais.html', animais=all_animais, AFazendeiros=AFazendeiros, ARacas=ARacas, APastos=APastos)

# Adicionar novo Animal
@app.route('/animais/novo', methods=['GET', 'POST'])
def add_animal():
    fazendeiros = Obj_Fazendeiro.select_fazendeiros()
    pastos = Obj_Pasto.select_pastos()
    racas = Obj_Raca.select_racas()
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Animal.add_animal(data['nome'], data['desc'], data['data_nascimento'], data['codigo_identificacao'], float(data['peso']), int(data['idade']))
        registrar_relações(int(data['fazendeiro']), int(data['pasto']), int(data['raca']))
        return redirect('/animais')
    return render_template('formanimais.html', title="Adicionar Novo Animal", animal=None, fazendeiros=fazendeiros, pastos=pastos, racas=racas)

# Editar um Animal Já Existente
@app.route('/animais/editar/<int:id>', methods=['GET', 'POST'])
def edit_animal(id):
    fazendeiros = Obj_Fazendeiro.select_fazendeiros()
    pastos = Obj_Pasto.select_pastos()
    racas = Obj_Raca.select_racas()
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Animal.update_animal(id, data['nome'], data['desc'], data['data_nascimento'], data['codigo_identificacao'], float(data['peso']), int(data['idade']))
        return redirect('/animais')
    animal = pickItem(Obj_Animal.select_animais(), id)
    return render_template('formanimais.html', title="Editar Animal Registrado", animal=animal, fazendeiros=fazendeiros, pastos=pastos, racas=racas)

# Deletar um Animal da Tabela
@app.route('/animais/remover/<int:id>', methods=['GET'])
def delete_animal(id):
    Obj_Animal.del_animal(id)
    return redirect('/animais')

# Páginas da Entidade Fazendeiros

# View da Tabela Fazendeiros
@app.route('/fazendeiros')
def list_fazendeiros():
    all_fazendeiros = Obj_Fazendeiro.select_fazendeiros()
    return render_template('viewfazendeiros.html', fazendeiros=all_fazendeiros)

# Adicionar novo Fazendeiro
@app.route('/fazendeiros/novo', methods=['GET', 'POST'])
def add_fazendeiro():
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Fazendeiro.add_fazendeiro(data['nome'])
        return redirect('/fazendeiros')
    return render_template('formfazendeiros.html', title="Adicionar Novo Fazendeiro", fazendeiro=None)

# Editar um Fazendeiro já existente
@app.route('/fazendeiros/editar/<int:id>', methods=['GET', 'POST'])
def edit_fazendeiro(id):
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Fazendeiro.update_fazendeiro(id, data['nome'])
        return redirect('/fazendeiros')
    fazendeiro = pickItem(Obj_Fazendeiro.select_fazendeiros(), id)
    return render_template('formfazendeiros.html', title="Editar Fazendeiro Registrado", fazendeiro=fazendeiro)

# Deletar um Fazendeiro da Tabela
@app.route('/fazendeiros/remover/<int:id>', methods=['GET'])
def delete_fazendeiro(id):
    Obj_Fazendeiro.del_fazendeiro(id)
    return redirect('/fazendeiros')

# Páginas da Entidade Pastos

# View da Tabela Pastos
@app.route('/pastos')
def list_pastos():
    pastos = Obj_Pasto.select_pastos()
    return render_template('viewpastos.html', pastos=pastos)

# Adicionar novo Pasto
@app.route('/pastos/novo', methods=['GET', 'POST'])
def add_pasto():
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Pasto.add_pasto(data['nome'], data['localizacao'])
        return redirect('/pastos')
    return render_template('formpastos.html', title="Adicionar Novo Pasto", pasto=None)

# Editar um Pasto já existente
@app.route('/pastos/editar/<int:id>', methods=['GET', 'POST'])
def edit_pasto(id):
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Pasto.update_pasto(id, data['nome'], data['localizacao'])
        return redirect('/pastos')
    pasto = pickItem(Obj_Pasto.select_pastos(), id)
    return render_template('formpastos.html', title="Editar Pasto Registrado", pasto=pasto)

# Deletar um Pasto da Tabela
@app.route('/pastos/remover/<int:id>', methods=['GET'])
def delete_pasto(id):
    Obj_Pasto.del_pasto(id)
    return redirect('/pastos')

# Páginas da Entidade Raças

# View da Tabela Raças
@app.route('/racas')
def list_racas():
    racas = Obj_Raca.select_racas()
    return render_template('viewracas.html', racas=racas)

# Adicionar nova Raça
@app.route('/racas/novo', methods=['GET', 'POST'])
def add_raca():
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Raca.add_raca(data['nome'])
        return redirect('/racas')
    return render_template('formracas.html', title="Adicionar Nova Raça", raca=None)

# Editar uma Raça já existente
@app.route('/racas/editar/<int:id>', methods=['GET', 'POST'])
def edit_raca(id):
    if request.method == "POST":
        data = request.form.to_dict()
        Obj_Raca.update_raca(id, data['nome'])
        return redirect('/racas')
    raca = pickItem(Obj_Raca.select_racas(), id)
    return render_template('formracas.html', title="Editar Raça Registrada", raca=raca)

# Deletar uma Raça da Tabela
@app.route('/racas/remover/<int:id>', methods=['GET'])
def delete_raca(id):
    Obj_Raca.del_raca(id)
    return redirect('/racas')

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')

