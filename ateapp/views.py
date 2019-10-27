from .models import Tutorial, TutorialCategory, TutorialSeries
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from django.http import HttpResponse
from django.shortcuts import render
import json
# import ssl
# import pandas as pd
# from bokeh.plotting import figure,ColumnDataSource,output_file
# from bokeh.models import HoverTool,WMTSTileSource,LinearColorMapper,LabelSet
# from bokeh.palettes import RdYlBu11 as palette
# from bokeh.server.server import Server
# from bokeh.application import Application
# from bokeh.tile_providers import STAMEN_TONER
# from bokeh.application.handlers.function import FunctionHandler
# import numpy as np
# import requests
# import urllib.request

# ssl._create_default_https_context = ssl._create_unverified_context
# opener = urllib.request.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# # COORDINATE CONVERSION FUNCTION
# def wgs84_to_web_mercator(df, lon="Lon", lat="Lat"):
#     k = 6378137
#     df["x"] = df[lon] * (k * np.pi/180.0)
#     df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
#     return df
# #FLIGHT TRACKING FUNCTION   

# def flight_track(doc):
#     # initiate bokeh column data source
#     flight_source = ColumnDataSource({'country':[],'code':[],'Lat':[],'Lon':[],'x':[],'y':[]})
# # UPDATING FLIGHT DATA
#     def update():
#         url = 'https://opensky-network.org/api/states/all?extended=false'
#         #url = "https://opensky-network.org/api/states/all?"
#         response = requests.request("GET", url)
#         txt= json.loads(response.text)
#         Lat,Lon = [],[]
#         code = []
#         country = []
#         for i in range(len(txt['states'])):
#             #print(i)
#             co = txt['states'][i][1]
#             con = txt['states'][i][2]
#             La = txt['states'][i][5]
#             Lo = txt['states'][i][6]
#             Lat.append(La)
#             Lon.append(Lo)
#             country.append(con)
#             code.append(co)
#         flight_df = {'country':country,'code':code,'Lat':Lat,'Lon':Lon}
#         flight_df = pd.DataFrame(data=flight_df)
#         wgs84_to_web_mercator(flight_df)
#         #flight_df = flight_df.dropna(inplace = True)
#         flight_df=flight_df.fillna('No Data')
#         n_roll=len(flight_df.index)
#         flight_source.stream(flight_df.to_dict(orient='list'),n_roll)
#     doc.add_periodic_callback(update, 1000)
#     x_range,y_range=([3360783.2596,-650631.9848], [11564616.6314,17826337.9886]) #bounding box
#     p=figure(x_range=x_range,y_range=y_range,x_axis_type='mercator',y_axis_type='mercator',sizing_mode='scale_width',plot_height=300)
#     my_hover=HoverTool()
#     color_mapper = LinearColorMapper(palette=palette)
#     my_hover.tooltips=[('country','@country'),('code','@code')]
#     labels = LabelSet(x='Lat', y='Lon', text='code', level='glyph',
#             x_offset=5, y_offset=5, source=flight_source, render_mode='canvas',background_fill_color='red',text_font_size="8pt")
#     p.add_tile(STAMEN_TONER)
#     p.circle('y','x',source=flight_source,fill_color={'field': 'country', 'transform': color_mapper},hover_color='yellow',size=10,fill_alpha=0.8,line_width=0.5)
#     p.add_tools(my_hover)
#     p.add_layout(labels)
#     doc.title='REAL TIME FLIGHT TRACKING WITH PANDAS AND BOKEH'
#     doc.add_root(p)

# apps = {'/': Application(FunctionHandler(flight_track))}
# server = Server(apps, port=5000) #define an unused port
# server.start()






def index(request):
    
    return render(request,'index.html',
           context={"categories": TutorialCategory.objects.all})


# def offres(request):
	
#     return render(request, 'ate/offres.html',context={'offres':Tutorial.objects.all})

def data(request):
    
    return render(request, 'stock.html')

def resume(request):
    
    return render(request, 'resume.html')

	
def nlp(request):
	
    return render(request, 'nlp.html')
	
def medical(request):
	
    return render(request, 'medical.html')
	
def data_viz(request):
	
    return render(request, 'data_viz.html')

def Globe(request):
    
    return render(request, 'glob.html')
	

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("ateapp:index")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "ate/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "ate/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("ateapp:index")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "ate/login.html",
                    context={"form":form})


