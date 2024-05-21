CREATE DATABASE	satelite_prd;

USE satelite_prd;

    CREATE TABLE emprestimo(
	id_equipamento int primary key auto_increment not null,
    numero_serie varchar(20) not null,
	fabricante_equip varchar(20) not null,
    ident_func_alun varchar(50) not null,
	dt_retirada varchar(19) not null,
    dt_devolucao varchar(19) not null);


select * from emprestimo;


/*Comando para testar

INSERT INTO emprestimo(numero_serie, fabricante_equip, ident_func_alun, dt_retirada, dt_devolucao)
values('NS102242', 'VivoBook', 'Danilo', '24-04-15 16:00', '24-04-16 17:10');

formato datetime AA-MM-DD HH:MM:SS

DROP TABLE emprestimos_prd;

*/
    


    

    

    
    
    
    
    
    
