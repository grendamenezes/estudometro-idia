import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq

exerc = [4,1,15,3,5,1]

def generate_message(avg_temp):
    if avg_temp <= 10:
        return ""
    elif 10 < avg_temp <= 25:
        return "O primeiro passo é sempre o mais difícil. Continue assim!"
    elif 25 < avg_temp <= 50:
        return "Já foi um quarto do caminho percorrido! Parabéns!!"
    elif 50 < avg_temp <= 75:
        return "Parabéns, você já atingiu metade do seu objetivo! Continue assim, a segunda metade será mais fácil."
    elif 75 < avg_temp <= 99.9:
        return "Está muuito perto do final!! Não surte que está quaseee"
    else:
        return "Pode abrir uma cerveja pra comemorar, ACABOU!!!!"
        
port1  = [{'label': 'Linguagem verbal e não verbal', 'value': 'port11'},
          {'label': 'As funções da linguagem', 'value': 'port12'},
          {'label': 'As variedades linguísticas', 'value': 'port13'}]
          
port2  = [{'label': 'Ortografia e Acentuação gráfica', 'value': 'port21'}]
          
        
port3  = [{'label': 'Estrutura e formação das palavras', 'value': 'port31'},
          {'label': 'Classes gramaticais variáveis e invariáveis', 'value': 'port32'}]
          
port4  = [{'label': 'Termos essenciais da oração', 'value': 'port41'},
          {'label': 'Termos integrantes da oração', 'value': 'port42'},
          {'label': 'Termos acessórios da oração e vocativo', 'value': 'port43'},
          {'label': 'Tipos de período', 'value': 'port44'},
          {'label': 'Orações coordenadas e subordinadas', 'value': 'port45'},
          {'label': 'Concordância verbal e nominal', 'value': 'port46'},
          {'label': 'Colocação pronominal', 'value': 'port47'},
          {'label': 'Regência verbal e nominal', 'value': 'port48'},
          {'label': 'Crase', 'value': 'port49'},
          {'label': 'Pontuação', 'value': 'port410'},
          {'label': 'Semântica e Interpretação textual', 'value': 'port411'},
          {'label': 'Estilística', 'value': 'port412'},
          {'label': 'Figuras de Linguagem', 'value': 'port413'}]
          
          
mat1   = [{'label': 'Operações e propriedades', 'value': 'mat11'}]

mat2   = [{'label': 'Representação fracionária e decimal', 'value': 'mat21'},
          {'label': 'Operações e propriedades', 'value': 'mat22'},
          {'label': 'Números reais', 'value': 'mat23'},
          {'label': 'Números irracionais', 'value': 'mat24'},
          {'label': 'Razão e proporção', 'value': 'mat25'},
          {'label': 'Porcentagem', 'value': 'mat26'},
          {'label': 'Regra de três simples e composta', 'value': 'mat27'},
          {'label': 'Juros simples e compostos', 'value': 'mat28'},
          {'label': 'Logaritmos', 'value': 'mat29'}]     
          
mat3   = [{'label': '1º grau', 'value': 'mat31'},
          {'label': '2º grau', 'value': 'mat32'},
          {'label': 'Exponencial', 'value': 'mat33'},
          {'label': 'Logarítmica', 'value': 'mat34'},
          {'label': 'Trigonométrica', 'value': 'mat35'}]
          
mat4   = [{'label': 'Determinantes', 'value': 'mat41'},
          {'label': 'Resolução de sistemas lineares', 'value': 'mat42'}]

mat5   = [{'label': 'Medidas de tempo', 'value': 'mat51'},
          {'label': 'Comprimento', 'value': 'mat52'},
          {'label': 'Superfície', 'value': 'mat53'},
          {'label': 'Capacidade', 'value': 'mat54'}]  

mat6   = [{'label': 'Tabelas e gráficos', 'value': 'mat61'},
          {'label': 'Raciocínio Lógico', 'value': 'mat62'},
          {'label': 'Resolução de Situações-Problema', 'value': 'mat63'},
          {'label': 'Geometria', 'value': 'mat64'},
          {'label': 'Geometria Analítica', 'value': 'mat65'},
          {'label': 'Trigonometria', 'value': 'mat66'},
          {'label': 'Progressão Aritmética (PA)', 'value': 'mat67'},
          {'label': 'Progressão Geométrica (PG)', 'value': 'mat68'},
          {'label': 'Análise Combinatória', 'value': 'mat69'}]    
          
mat7   = [{'label': 'Probabilidade', 'value': 'mat71'},
          {'label': 'Conjuntos', 'value': 'mat72'},
          {'label': 'Sistema Cartesiano', 'value': 'mat73'},
          {'label': 'Álgebra', 'value': 'mat74'},
          {'label': 'Polinômios', 'value': 'mat75'}]
          
leg1   = [{'label': 'Lei Complementar nº 003/2003 - \nEstatuto do Magistério Público do\nMunicípio de São Francisco do Sul', 'value': 'leg11'},
          {'label': 'Lei Municipal nº 1744/2015 - \nPlano Municipal de Educação', 'value': 'leg12'}]

leg3   = [{'label': 'Art. 1º ao Art. 6º', 'value': 'leg31'},
          {'label': 'Art. 15 ao Art. 18-B', 'value': 'leg32'},
          {'label': 'Art. 53 a Art. 59', 'value': 'leg33'},
          {'label': 'Art. 131 a Art. 137', 'value': 'leg34'}]
          
leg4   = [{'label': 'Art. 1º ao Art. 41', 'value': 'leg41'},
          {'label': 'Art. 205 ao Art. 214', 'value': 'leg42'}]
          
con1   = [{'label': 'Lei Federal nº 9.394/1996 - \nDiretrizes e Bases da Educação Nacional\n', 'value': 'con11'},
          {'label': 'BNCC – Base Nacional Comum Curricular', 'value': 'con12'},
          {'label': 'Lei Federal nº 13.146/2015 - \nEstatuto da Pessoa com Deficiência\n', 'value': 'con13'},
          {'label': 'Lei Federal nº 13.185/2015\nPrograma de Combate à Intimidação\nSistemática (Bullying)', 'value': 'con14'},
          {'label': 'Diretrizes Curriculares Nacionais\npara Educação das Relações Étnico-raciais e\npara o Ensino de História e Cultura\nAfro-brasileira, Africana e indígena', 'value': 'con15'},
          {'label': 'Política Nacional de Educação Especial\nna Perspectiva da Educação Inclusiva', 'value': 'con16'},
          {'label': 'Resolução CNE/CEB 04/2010\nDiretrizes Curriculares Nacionais Gerais para a Educação Básica', 'value': 'con17'},
          {'label': 'História da educação brasileira', 'value': 'con18'},
          {'label': 'Teóricos e Teorias da Educação', 'value': 'con19'}]

con2   = [{'label': 'Concepções de Educação e de Escola', 'value': 'con21'},
          {'label': 'A função social da escola, a educação\ninclusiva e o compromisso ético e social do educador', 'value': 'con22'}]

con3   = [{'label': 'A participação como princípio', 'value': 'con31'}]

con4   = [{'label': 'Fundamentos para a orientação, o planejamento e\na implementação das ações educativas da escola', 'value': 'con41'},
          {'label': 'Construção participativa do projeto\npolítico-pedagógico e da autonomia da escola', 'value': 'con42'},
          {'label': 'Metodologias ativas na educação', 'value': 'con43'}]

esp1   = [{'label': 'A criança como sujeito de direitos', 'value': 'esp11'},
          {'label': 'As fases do desenvolvimento infantil\ne suas relações com a aprendizagem', 'value': 'esp12'},
          {'label': 'O cuidar e o educar', 'value': 'esp13'},
          {'label': 'Os ambientes de aprendizagem na\neducação infantil', 'value': 'esp118'},
          {'label': 'A brincadeira e a interação como eixos\ncentrais da educação infantil', 'value': 'esp14'},
          {'label': 'A Educação Infantil e a construção\nda leitura e da escrita', 'value': 'esp15'},
          {'label': 'Alfabetização', 'value': 'esp16'},
          {'label': 'A formação pessoal e social\nda criança', 'value': 'esp17'},
          {'label': 'Identidade e autonomia', 'value': 'esp18'},
          {'label': 'O desenvolvimento humano segundo\nPiaget, Vygostky e Wallon', 'value': 'esp19'},
          {'label': 'Ensinar e aprender matemática\nna educação infantil', 'value': 'esp110'},
          {'label': 'As instituições de Educação Infantil\ne a relação com as famílias', 'value': 'esp111'},
          {'label': 'As rotinas na educação infantil', 'value': 'esp112'},
          {'label': 'A organização do tempo e espaço\nna Educação Infantil', 'value': 'esp113'},
          {'label': 'As estratégias da ação pedagógica\n(observação, planejamento, registro, avaliação)', 'value': 'esp114'},
          {'label': 'Diretrizes Curriculares Nacionais\npara Educação Infantil (2009)', 'value': 'esp115'},
          {'label': 'Matriz Curricular para Educação das\nRelações Étnico-Raciais na Educação Básica (2016)', 'value': 'esp116'},
          {'label': 'Conhecimentos básicos inerentes\nàs atividades do cargo', 'value': 'esp117'}]

app = dash.Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H1("Futura prof. Idia, concursada!! ",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div(id='message-box', style={'textAlign': 'center','color': 'red'}), html.Br(), html.Br(),
    
    # Div para centralizar o termômetro e a imagem
    html.Div([
        # Termômetro graduado
        daq.Thermometer(
            id='thermometer',
            value=50,
            min=0,
            max=100,
            scale={'start': 0, 'interval': 10, 'labelInterval': 10},
            label='Estudômetro',
        ),
        
        html.Img(id='sun-img', src='https://raw.githubusercontent.com/grendamenezes/estudometro-idia/master/idia.png', style={'height': '200px', 'width': '100px', 'margin-left': '10px'}),
    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    
    html.Br(), html.Br(), html.Br(), html.Br(),
    html.Div([html.Br(),html.Br(),
			dcc.RadioItems(id='tipos',style={'textAlign': 'center','fontFamily':'Arial','fontSize':18,'flex': 1},
					   options=[{'label': 'Disciplinas comuns', 'value': 'tod'},
								{'label': 'Conhecimentos específicos', 'value': 'esp'}], 
					   value='tod'
					   ),html.Br(),html.Br()],id='rela-container'),
    html.Div([
	html.Div([
    html.H2("Língua Portuguesa",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
		
		html.Div([html.H4("LINGUAGEM",style={'align-items': 'center'}),
        dcc.Checklist(
            id='port1',
            options=port1,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("FONOLOGIA",style={'display': 'flex', 'align-items': 'center'}),
        dcc.Checklist(
            id='port2',
            options=port2,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("MORFOLOGIA",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='port3',
            options=port3,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("SINTAXE",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='port4',
            options=port4,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        )],style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','flex-direction': 'column'} )], style={'width': '45%'}),
    html.Div([
    html.H2("Matemática",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
		
		html.Div([html.H4("Números inteiros",style={'align-items': 'center'}),
        dcc.Checklist(
            id='mat1',
            options=mat1,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Números racionais",style={'display': 'flex', 'align-items': 'center'}),
        dcc.Checklist(
            id='mat2',
            options=mat2,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Funções",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='mat3',
            options=mat3,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Matrizes",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='mat4',
            options=mat4,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Sistema métrico",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='mat5',
            options=mat5,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Relação entre grandezas",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='mat6',
            options=mat6,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Estatística Básica",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='mat7',
            options=mat7,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        )],style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','flex-direction': 'column'} )], style={'width': '65%'}),
    html.Div([
    html.H2("Legislação",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
		
		html.Div([
        dcc.Checklist(
            id='leg1',
            options=leg1,
            value=[],
            labelStyle={'white-space': 'pre-line'},  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Lei Federal nº 8.069/90 – ", style={'text-align': 'center', 'margin-bottom': '10px'}),
		html.H4("Estatuto da Criança e do Adolescente", style={'text-align': 'center', 'margin-top': '10px', 'margin-bottom': '10px'}),
        dcc.Checklist(
            id='leg3',
            options=leg3,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Constituição da República Federativa do Brasil",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='leg4',
            options=leg4,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        )],style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','flex-direction': 'column'} )], style={'width': '75%'}),
    html.Div([
    html.H2("Conhecimentos pedagógicos",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
		
		html.Div([html.H4("Leis e diretrizes",style={'align-items': 'center'}),
        dcc.Checklist(
            id='con1',
            options=con1,
            value=[],
            labelStyle={'white-space': 'pre-line'},  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Relação entre educação, escola e sociedade",style={'display': 'flex', 'align-items': 'center'}),
        dcc.Checklist(
            id='con2',
            options=con2,
            value=[],
            labelStyle={'white-space': 'pre-line'},  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Gestão democrática",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='con3',
            options=con3,
            value=[],
            labelStyle={'white-space': 'pre-line'},  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        ),
        html.H4("Projeto político-pedagógico",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='con4',
            options=con4,
            value=[],
            labelStyle={'white-space': 'pre-line'},  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        )],style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','flex-direction': 'column'} )], style={'width': '100%'})
        ],id = 'todos',style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','flex-direction': 'row', 'align-items': 'flex-start'}),
    html.Div([		
		html.Div([
        dcc.Checklist(
            id='esp1',
            options=esp1,
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex', 'align-items': 'left'}, persistence=True
        )],style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','flex-direction': 'column'} )], 
        id = 'espec', style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center','flex-direction': 'row', 'align-items': 'flex-start'}),
    html.Br(),html.Br(),    
])





@app.callback(
	Output('message-box', 'children'),
    Output('thermometer', 'value'),
    Output('thermometer', 'color'),
    Output('sun-img', 'style'),
    Output('todos', 'style'),
    Output('espec', 'style'),
    Input('tipos', 'value'),
    Input('port1', 'value'),
    Input('port2', 'value'),
    Input('port3', 'value'),
    Input('port4', 'value'),
    Input('mat1', 'value'),
    Input('mat2', 'value'),
    Input('mat3', 'value'),
    Input('mat4', 'value'),
    Input('mat5', 'value'),
    Input('mat6', 'value'),
    Input('mat7', 'value'),
    Input('leg1', 'value'),
    Input('leg3', 'value'),
    Input('leg4', 'value'),
    Input('con1', 'value'),
    Input('con2', 'value'),
    Input('con3', 'value'),
    Input('con4', 'value'),
    Input('esp1', 'value')
)        

def update_thermometer(tip,pt1,pt2,pt3,pt4,mt1,mt2,mt3,mt4,mt5,mt6,mt7,lg1,lg3,lg4,cn1,cn2,cn3,cn4,ep1):
	tot_por = len(port1)+len(port2)+len(port3)+len(port4)
	tot_mat = len(mat1)+len(mat2)+len(mat3)+len(mat4)+len(mat5)+len(mat6)+len(mat7)
	tot_len = len(leg1)+len(leg3)+len(leg4)
	tot_con = len(con1)+len(con2)+len(con3)+len(con4)
	tot_esp = len(esp1)
	
	port    = (len(pt1)+len(pt2)+len(pt3)+len(pt4))/tot_por
	mat     = (len(mt1)+len(mt2)+len(mt3)+len(mt4)+len(mt5)+len(mt6)+len(mt7))/tot_mat
	leg     = (len(lg1)+len(lg3)+len(lg4))/tot_len
	con     = (len(cn1)+len(cn2)+len(cn3)+len(cn4))/tot_con
	esp     =  len(ep1)/tot_esp
	
	avg_temp = (port*5+mat*5+leg*5+con*10+esp*15)*2.5
	thermometer_value = avg_temp
	img_style = {
        'height': '200px',
        'width': '100px',
        'position': 'relative',
        'top': f'{2 * (60 - thermometer_value)}px'
    }
	color = f'rgb({255 - int(2.55 * thermometer_value)}, {int(2.55 * thermometer_value)}, 0)'
	message = generate_message(avg_temp)
	comum     = {'display': 'flex'} if tip == 'tod' else {'display': 'none'}
	especial  = {'display': 'block'} if tip == 'esp' else {'display': 'none'}
	return html.H3(message),thermometer_value, color, img_style,comum,especial

if __name__ == '__main__':
    app.run_server(debug=True)
