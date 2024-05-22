from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from datetime import datetime


app = Flask(__name__)                    #### default ####

app.config.from_pyfile('config_db.py')   #### configuração do banco de dados ####

db = SQLAlchemy(app)                     #### configuração do banco de dados / classes ####


class Emprestimo(db.Model):
    id_equipamento = db.Column(db.Integer, primary_key = True, autoincrement = True)
    numero_serie = db.Column(db.String(20), nullable=False)
    fabricante_equip = db.Column(db.String(20), nullable=False)
    ident_func_alun = db.Column(db.String(50), nullable=False)
    dt_retirada = db.Column(db.DATETIME(), nullable=True)
    dt_devolucao = db.Column(db.DATETIME(), nullable=True)

    def __repr__(self):
        return '<Name %r>' %self.name


@app.route('/login')  
def login():
    return render_template('tela_login.html', logo="https://colegiosatelite.com.br/wp-content/uploads/2021/05/mobile-1-1-1.png")

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['txtSenha'] == 'univesp':
        session['usuario_logado'] = request.form['txtUsuario'] == 'admin'
        flash("Usuário logado com sucesso!")
        return redirect(url_for('listarEquip'))

    else:
        flash("Usuário ou senha inválido!")
        return redirect(url_for('login'))


@app.route('/logout')
def sair():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/login')


################################################################################################

@app.route('/')
def listarEquip():

        if session['usuario_logado'] == None or 'usuario_logado' not in session:

            return redirect(url_for('login'))
        

        lista = Emprestimo.query.order_by(text('emprestimo.id_equipamento'))


        return render_template('lista_equipamentos.html', 
                           titulo = 'Entrada e Saída de Chromebooks', 
                           equipamentos = lista, logo="https://colegiosatelite.com.br/wp-content/uploads/2021/05/mobile-1-1-1.png", log=session['usuario_logado'], usuarioLog='usuario_logado')

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Empréstimo')

@app.route('/inserir', methods=['POST',])
def inserir():
    # inserir dados do formulário no Banco de dados
    numero_serie = request.form['numero_serie']
    fabricante_equip = request.form['fabricante_equip']
    ident_func_alun = request.form['ident_func_alun']
    data_e_hora_atual = datetime.now()
    dt_retirada = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')

    novo_emprestimo = Emprestimo(numero_serie= numero_serie, fabricante_equip= fabricante_equip, ident_func_alun= ident_func_alun, dt_retirada= dt_retirada, dt_devolucao= '0000-00-00 00:00:00')

    flash('Retirada efetuado com sucesso!')
    db.session.add(novo_emprestimo)
    db.session.commit()
    
    return redirect('/')

@app.route('/devolucao', methods=['POST',])
def devolucao():
    id_equipamento = request.form['id-equipamento']
    dt = Emprestimo.query.filter_by(id_equipamento=id_equipamento).first()
    dt.dt_devolucao = datetime.now().strftime('%d/%m/%Y %H:%M')

    flash('Devolução feita com sucesso!')

    db.session.add(dt)
    db.session.commit()
    #Emprestimo.dt_devolucao = time.time()

    return redirect('/')

@app.route('/excluir', methods=['POST',])
def excluir():
    id_equipamento = request.form['id-equipamento'].strip()
    dt = Emprestimo.query.filter_by(id_equipamento=id_equipamento).first()

    flash('Excluido com sucesso!')

    db.session.delete(dt)
    db.session.commit()

    return redirect('/')

@app.route('/busca', methods=['POST',])
def busca():
    num_serie = request.form['num_serie'].strip()
    item = Emprestimo.query.filter_by(numero_serie= num_serie).first()

    return render_template('busca.html', equipamento=item, logo="https://colegiosatelite.com.br/wp-content/uploads/2021/05/mobile-1-1-1.png", log=session['usuario_logado'], usuarioLog='usuario_logado')


if __name__ == '__main__':                #### Garante que a aplicação importe as configurações ####
    #app.run(host="192.168.100.26", port=5000, debug=True)
    app.run(debug=True)                   #     não precisa reiniciar o sevidor     #

#preparar deploy seguir abaixo
#Procfile como arquivo de texto conteudo: web: gunicorn meu_site: app

#pip install gunicorn
#pip freeze > requirements.txt
