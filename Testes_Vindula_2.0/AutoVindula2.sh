#!/bin/sh

echo "##########################################"
echo "#              Executando                #"
echo "##########################################"
echo "##########################################"
echo "#       Iniciando o Python27             #"
echo "##########################################"
source /opt/Vindula2.0/bin/activate
echo "##########################################"
echo "#                Iniciando               #"
echo "##########################################"
echo "Apagando Portlets padroes."
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/IniciandoTestes.py
echo "##########################################"
echo "#           Criando Usuarios             #"
echo "##########################################"
echo "Criando Usuarios utilizados nos testes (Teste1, Teste2 e Teste3) ambos usuarios usam a senha teste!"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoUsuariosDeTeste.py
echo "##########################################"
echo "#         Criando Pasta de Testes        #"
echo "##########################################"
echo "Criando pasta onde serao realizados os teste de aplicacao e conteudo"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoPastaDeTestes.py
echo "##########################################"
echo "#     Criando Estrutura Organizacional   #"
echo "##########################################"
echo "Cria conteudo Estrutura Organizacional"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoEstruturaOrganizacional.py
echo "##########################################"
echo "#            Criando Home Page           #"
echo "##########################################"
echo "Cria conteudo Home Page"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoHomePage.py
echo "##########################################"
echo "#              Criando Pagina            #"
echo "##########################################"
echo "Cria um conteudo Pagina"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoPagina.py
echo "##########################################"
echo "#              Criando Link              #"
echo "##########################################"
echo "Cria um conteudo Link"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoLink.py
echo "##########################################"
echo "#              Criando Evento            #"
echo "##########################################"
echo "Cria um conteudo Evento"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoEvento.py
echo "##########################################"
echo "#             Criando Colecao            #"
echo "##########################################"
echo "Cria um conteudo Colecao"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoColecao.py
echo "##########################################"
echo "#             Criando Album              #"
echo "##########################################"
echo "Cria uma aplicacao Album de fotos"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoAlbumDeFotos.py
echo "##########################################"
echo "#       Criando Reserva Corporativa      #"
echo "##########################################"
echo "Cria uma aplicacao Reserva Corporativa"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoReservaCorporativa.py
echo "##########################################"
echo "#       Testando reserva corporativa     #"
echo "##########################################"
echo "Testa a aplicacao reserva corporativa"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/TestandoReserva.py
echo "##########################################"
echo "#      Criando Lista de Restaurantes     #"
echo "##########################################"
echo "Cria uma aplicacao Lista de Restaurantes"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoListaDeRestaurantes.py
echo "##########################################"
echo "#       Criando Formulario Basico        #"
echo "##########################################"
echo "Cria uma aplicacao Formulario Basico"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoFormularioBasico.py
echo "##########################################"
echo "#      Criando campos no formulario      #"
echo "##########################################"
echo "Cria campos dentro do formulario de teste."
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoQuestoesFormulario.py
echo "##########################################"
echo "#       Testando Formulario Basico       #"
echo "##########################################"
echo "Testa o formulario basico."
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/TestandoFormularioBasico.py
echo "##########################################"
echo "#              Criando Forum             #"
echo "##########################################"
echo "Cria uma aplicacao Forum "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoForum.py
echo "##########################################"
echo "#      Criando conversa no Forum         #"
echo "##########################################"
echo "Cria uma aplicacao Forum "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoConversasForum.py
echo "##########################################"
echo "#           Criando Memorando            #"
echo "##########################################"
echo "Cria uma aplicacao Memorando "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoMemorando.py
echo "##########################################"
echo "#           Testando Memorando           #"
echo "##########################################"
echo "Testa aplicacao memorando "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/TestandoMemorando.py
echo "##########################################"
echo "#   Criando Gerenciador de Ocorrencias   #"
echo "##########################################"
echo "Cria uma aplicacao Gerenciador de Ocorrencias "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoGerenciadorDeOcorrencias.py
echo "############################################"
echo "#Criando Portlet Gerenciador de Ocorrencias#"
echo "############################################"
echo "Cria uma aplicacao Gerenciador de Ocorrencias "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoPortletGerenciadorOcorrencias.py
echo "############################################"
echo "#    Testando Gerenciador de Ocorrencias   #"
echo "############################################"
echo "Testando Gerenciador de Ocorrencias"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/TestandoGerenciadordeOcorrencias.py
echo "##########################################"
echo "#            Criando Enquete             #"
echo "##########################################"
echo "Cria uma aplicacao Enquete "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoEnquete.py 
echo "##########################################"
echo "#        Criando Portlet Enquete         #"
echo "##########################################"
echo "Cria um Portlet Enquete "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoPortletEnquete.py
echo "##########################################"
echo "#             Testando Enquete           #"
echo "##########################################"
echo "Testando aplicacao Enquete"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/TestandoEnquete.py
echo "##########################################"
echo "#            Criando Edital              #"
echo "##########################################"
echo "Cria uma aplicacao Edital "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoEdital.py
echo "##########################################"
echo "#            Testando Edital             #"
echo "##########################################"
echo "Testando aplicacao Edital "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/TestandoEdital.py
echo "##########################################"
echo "#          Criando Classificados         #"
echo "##########################################"
echo "Cria uma aplicacao Classificados "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoClassificados.py
echo "##########################################"
echo "#   Criando Categorias nos Classificados #"
echo "##########################################"
echo "Cria uma aplicacao Classificados "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/CriandoCategoriasClassificados.py
echo "##########################################"
echo "#         Testando Classificados         #"
echo "##########################################"
echo "Adiciona novo campo de edição no perfil dos usuarios "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/TestandoClassificados.py
echo "##########################################"
echo "#Inserindo novo campo de edicao de perfil#"
echo "##########################################"
echo "Testando aplicacao Classificados "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/InserindoNovoCamponoPerfil.py
echo "##########################################"
echo "#   Testando Interacoes entre usuarios   #"
echo "##########################################"
echo "Testa a Interacao entre os Usuarios"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/InteracoesEntreUsuarios.py
echo "##########################################"
echo "#           Excluindo Portlets           #"
echo "##########################################"
echo "Exclui Portlets criados para testes"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/ExcluindoPortletsdeTeste.py
echo "##########################################"
echo "#           Excluindo Testes             #"
echo "##########################################"
echo "Exclui aplicacoes e conteudos de teste"
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/ExcluindoTestes.py
echo "##########################################"
echo "#       Excluindo Pasta de testes        #"
echo "##########################################"
echo "Exclui pasta de teste "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/ExcluindoPastadeTestes.py
echo "##########################################"
echo "#          Excluindo Usuarios            #"
echo "##########################################"
echo "Exclui Usuarios(Teste1 , Teste2 e Teste3) "
python /opt/Vindula2.0/vindula.teste/Testes_Vindula_2.0/ExcluindoUsuarios.py
echo "##########################################"
echo "#           Teste Finalizado             #"
echo "##########################################"

