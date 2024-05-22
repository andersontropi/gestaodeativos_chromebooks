
#######################################################################################
#Configurações com banco de dados MySQL
#######################################################################################

SECRET_KEY = 'univesp_ti'

#CONSTANTE#
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'sqluser',
        senha = 'Univesp.2024',   #senha de exemplo#
        servidor = 'localhost',
        database = 'satelite_prd'
    )



    #######################################################################################
