
#######################################################################################
#Configurações com banco de dados MySQL
#######################################################################################

SECRET_KEY = 'univesp_ti'

#CONSTANTE#
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'sqluser',
        senha = 'Univesp.2024',
        servidor = '192.168.100.26',
        database = 'satelite_prd'
    )



    #######################################################################################