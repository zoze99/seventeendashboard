import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# external JavaScript files
external_scripts = ["https://unpkg.com/aos@2.3.1/dist/aos.js"]

# external CSS stylesheets
external_stylesheets = ["https://unpkg.com/aos@2.3.1/dist/aos.css"]
#library tutorial: https://michalsnik.github.io/aos/

st = pd.read_csv('svt_songtype.csv')

# 원하는 키워드로 TOP5 추천받기
print(st.sort_values('청량', ascending=False).head())

# 4분할 그래프 제작 위한 x축, y축 데이터열 추가
st['xAxis'] = st['아련'] - st['신남']
st['yAxis'] = st['청량'] - st['다크']
print(st.sort_values('청량', ascending=False).head())

# 좋아하는 세븐틴 노래 입력받고 오각 취향 그래프 도출하기

# Dash App Variable Declaration
app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)
fig1 = px.scatter(st, x="xAxis", y="yAxis", template='plotly_white', width=1000, height=800,
                  size="트렌디", color="수록앨범",
                  hover_name="곡명", hover_data=["청량","신남","다크","아련","트렌디"])

# Dash App Layout
app.layout = html.Div([
    html.Audio(id="bgm", src="/assets/ohmy-8bit.mp3", autoPlay=True, controls=True, loop=True),
    html.P('어쩌나(Oh My!) 8bit by Darnu-Pop', id="bgm-source"),
    html.Img(src="/assets/svt_wallpaper_1.jpg", id="cover-image"),
    html.Div([
        html.Div([html.H1('SVT', className='rosequartz'),
                  html.H1('Songtype', className='serenity'),
                  html.H1('Dashboard', className='rosequartz')],
                 className='service-name'),
        html.Div([html.P("Enter your Name >", className='label'),
                  dcc.Input(id='input-username', value='캐럿', placeholder='Error')],
                 className='row-flex'),
        html.A(html.Button(id='start-button', children='START!'), href="#anchor-1"),
        html.H3(children='PC Only! Not for Mobile', className='blinking warning-message')],
        className='intro'),
    html.Img(src="/assets/svt_profile.jpg", id="profile-image"),
    html.Div([html.P('캐러뜰 안녕하세요! 이 페이지는 Theqoo 세븐틴 독방에서 집계된 <세븐틴 수록곡 타입조사> 설문 결과를 바탕으로 제작되었습니다.', className='noti-message'),
        html.P('문제가 발생할 시 seventeendashboard@gmail.com으로 캡쳐와 함께 메일 부탁드립니다.', className='noti-message'),
        html.P('그럼 재미있게 즐겨 주세요!', className='noti-message'),
        html.Br(),
        html.P('Hi Carats! This page is based on survey data took on Theqoo.', className='noti-message'),
        html.P('If you find any problem, please contact me with a captured image: seventeendashboard@gmail.com', className='noti-message'),
        html.P('Please Enjoy!', className='noti-message'),
        html.Br()],
        className='intro-noti'),
    html.Div([html.P(id='welcome-message', children='WELCOME!'),
              html.A(id="anchor-1"),
              dcc.Graph(id='main-graph', figure=fig1)],
             id='main-section')
])



@app.callback(
    Output(component_id='welcome-message', component_property='children'),
    Input(component_id='input-username', component_property='value')
)

def set_username(input_text):
    return f'반가워요! {input_text}님💎의 세븐틴 노래 취향을 알아보세요!'

# Turn Server On
if __name__ == '__main__':
    app.run_server(debug=True)