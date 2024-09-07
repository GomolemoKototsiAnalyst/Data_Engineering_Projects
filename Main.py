#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.set_page_config(page_title="",layout='wide', page_icon="👋")

# Using Important Libraries: 
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import string
import plotly.express as px
from datetime import datetime, timedelta
import plotly.graph_objects as go
import folium
import matplotlib.pyplot as plt
from PIL import Image
import base64
from streamlit_option_menu import option_menu
import warnings
import requests
from io import StringIO
from io import BytesIO
#from io import StringIO
import os
#from urllib.parse import urlparse
warnings.simplefilter(action='ignore', category=Warning)


# Function to resize icons and convert to base64
def get_resized_icon(image_path, width):
    try:
        img = Image.open(image_path)
        aspect_ratio = img.height / img.width
        resized_img = img.resize((width, int(width * aspect_ratio)))
        buffered = BytesIO()
        resized_img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return None


def intro():
    import streamlit as st
    
    st.write("# Welcome to My Data Hub Portal! 👋")
    # Example content in a greyish-themed container
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="custom-text">
           <p>Welcome to my Data Hub Portal, the ultimate playground for data enthusiasts and curious minds alike! This interactive dashboard is not just a showcase; it's a journey through my analytics portfolio, where every click is a step deeper into the world of data-driven insights. Whether you're here for serious data science or just a bit of fun (because who says data can't be fun?), you're in the right place. Each project featured in this portal is a testament to my passion for transforming raw data into powerful, actionable insights. From complex algorithms to simple visualizations, I've tackled it all with one goal in mind: turning numbers into narratives that make a difference.</p>   
           <p>Now, I know what you're thinking—“Another data dashboard? How exciting!” But trust me, this one’s different. Not only will you find a treasure trove of insightful analyses, but you'll also discover that data can have a sense of humor (or at least I try!). So grab your virtual magnifying glass, dive in, and see how these projects bring the power of data to life. Use the sidebar 👈 to navigate through the different sections—because just like in life, it’s all about finding the right data at the right time!</p> 
        </div>
    """,
        unsafe_allow_html=True
    )
    st.subheader("", divider="gray")
    ##Creating a beatiful Symphony: 
    col1, col2 = st.columns([3,2.5])
    with col1:
        st.markdown(
            """
            <div class="custom-text">
               <h5>What to Look Forward To:</h5>
               <ul>
                   <li>Dashboards & their Architectural Design together with Data objects Explanation</li>
                   <li>A Jump into my Interests in our IT World or Statistics Capita Selecta</li>
                   <li>Ask a question in our Survey Group</li>
               </ul>
               <h5>See more interesting conversations:</h5>
               <ul>
                   <li>Check Out My SteinTech This Week Forum - It is just an outlook on Fun Tech advancement for personal use.</li>
                   <li>How to Connect & Collaborate on Projects.</li>
               </ul>
               <h5>See Authors Skills:</h5>
            </div>
            """, 
            unsafe_allow_html=True
        )
   
        st.markdown("""
            <div class="custom-text">
                <ul>
                    <li> SQL(SQL Server, MySQL)</li>
                    <li>Python (Pandas, NumPy, SciPy, MatPlotLib)</li>
                    <li>Excel (VLookup, Conditional Formatting, Pivot Tables)</li>
                    <li>SAS(PROC Procedures, IML)</li>
                    <li>Microsoft Power BI</li>
                    <li>Microsoft Azure (DataBricks, Azure Data Lake, Azure Data Warehouse)</li>
                    <li>PySpark</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True)
        

    with col2:
        import streamlit as st
        import streamlit.components.v1 as components

        # Define the HTML and JavaScript for the 3D interactive sphere chart with an additional cylinder
        html_code = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>3D Interactive Sphere Chart</title>
            <style>
                body { margin: 0; overflow: hidden; }
                canvas { display: block; }
            </style>
        </head>
        <body>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                var scene = new THREE.Scene();
                var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                var renderer = new THREE.WebGLRenderer({ alpha: true });  // Enable transparency
                renderer.setSize(window.innerWidth, window.innerHeight);
                renderer.setClearColor(0x000000, 0); // Set background color to transparent
                document.body.appendChild(renderer.domElement);

                var geometry = new THREE.SphereGeometry(1, 32, 32);
                var material = new THREE.MeshBasicMaterial({ color: 0x0077ff, wireframe: true });

                // Create the spheres
                var topSphere = new THREE.Mesh(geometry, material);
                var leftSphere = new THREE.Mesh(geometry, material);
                var rightSphere = new THREE.Mesh(geometry, material);

                // Initial positions
                topSphere.position.set(0, 1.5, 0);
                leftSphere.position.set(-1.5, -1.5, 0);
                rightSphere.position.set(1.5, -1.5, 0);

                scene.add(topSphere);
                scene.add(leftSphere);
                scene.add(rightSphere);

                camera.position.z = 5;

                var clock = new THREE.Clock();

                function animate() {
                     requestAnimationFrame(animate);

                     // Get elapsed time
                     var time = clock.getElapsedTime();

                     // Animate positions
                     topSphere.position.x = Math.sin(time) * 1.5;
                     topSphere.position.y = Math.cos(time) * 1.5;

                     leftSphere.position.x = Math.sin(time + Math.PI) * 1.5;  // Phase shift for different movement
                     leftSphere.position.y = Math.cos(time + Math.PI) * 1.5;

                     rightSphere.position.x = Math.sin(time + Math.PI / 2) * 1.5;  // Another phase shift
                     rightSphere.position.y = Math.cos(time + Math.PI / 2) * 1.5;

                     // Rotate the spheres
                     topSphere.rotation.x += 0.01;
                     topSphere.rotation.y += 0.01;

                     leftSphere.rotation.x += 0.01;
                     leftSphere.rotation.y += 0.01;

                     rightSphere.rotation.x += 0.01;
                     rightSphere.rotation.y += 0.01;

                     renderer.render(scene, camera);
                }

                animate();

                window.addEventListener('resize', function() {
                     renderer.setSize(window.innerWidth, window.innerHeight);
                     camera.aspect = window.innerWidth / window.innerHeight;
                     camera.updateProjectionMatrix();
                });
            </script>
        </body>
        </html>
        """
        # Streamlit app code
        components.html(html_code, height=600, width=800)
        #st.image(r'C:\Users\Gomolemo.Kototsi\Downloads\Grey and Black Simple Minimal Sales Analysis Graph.jpg', width=600)
        
    st.subheader("", divider="gray")
    st.markdown(
        """
        <div style="max-width: 100%; font-size: 20px;">
            <h5> About the Author:</h5>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    ##### Name & Surname: Gomolemo Kototsi
    col1, col2 = st.columns([1,2])
    with col1:
        #st.markdown("Gomolemo Kototsi",unsafe_allow_html=True)
        Gomolemo_path = os.path.join('Images', 'IMG_20211108_144305_755.webp')
        st.image(Gomolemo_path, width=600)
        #st.image('C:/Users/Gomolemo.Kototsi/Downloads/IMG_20211108_144305_755.webp', width=600)
    with col2:
        # Add a description on the right side:
        st.markdown(
            """
            <div style="max-width: 100%; font-size: 20px;">
                 <h4 style="text-align:center;" >Gomolemo Kototsi:</h4>
                 <p>I am currently working as a Business Applications Systems Specialist, where I design tailored frameworks to optimize the functionality of operational systems. I am one of the key members in the deployment of an end-to-end Supply Chain Operations system for our Southern and Eastern African Logistics company. Additionally, I lead the Business Applications Learning Forum and have provided training on various Export and Warehouse Management systems to our local and SADC region subsidiaries.</p>
                 <p>At present, I am a member of the Solutions Support team within our Value Realisation IT Team at Steinweg, managing various IT pillars to execute internal projects and systems developed for our business divisions. I am also expanding my academic knowledge in credit risk modeling for financial institutions. I hold a degree in Econometrics from the University of Pretoria, with majors in Statistics and Economics, and a BCom Honours in Statistics and Data Science, where my research focused on Bayesian Models.</p>
                 <p>My professional experience includes working as a Statistics Tutor for junior and second-year students at the University of Pretoria. I also completed an internship with Old Mutual Life Assurance through their Tech Talent Program, and worked for a year in Transit Risk Operations at C. Steinweg Bridge Pty Ltd, focusing on Transit Risk Reporting and Analysis. Subsequently, I transitioned within the same company to the Digital Solutions Team as a Business Applications Specialist.</p>
                 <p>I am now pursuing a role in finance as an Analyst, combining my interests in technology and finance. I am eager to join a community and company that will allow me to showcase my potential in this field.I am proficient in using tools such as Python, R, and SQL to manipulate and analyze diverse datasets,uncovering actionable insights that contribute to strategic initiatives and process improvements. I actively seek opportunities to expand my knowledge and stay abreast of the latest advancements in data analytics and technology, ensuring my skills remain cutting-edge.Currently, on a journey self-actualising and potential enabling from finding a way to centralise all the working experience I have together with my academic prowess.</p>
                 <p>Currently working on 3 projects that will be up in the portal in a few weeks. The first project is a Financial KPI's Tracking Dashboard that tracks, analysis and provides insigts on a business over a specified period of time using the published integrated financial reports. Second, Project is a Credit Risk Modelling project following structured Credit Models for both Individuals and Corporations. Lastly, It's a also a credit risk modelling project using a more basic approach of the Altman's Z Score Model.</p>
                 <p>Thank you 👍and don't forget to connect. Check the difference ways of connecting below 👇</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.subheader("", divider="gray")
    st.markdown(
        """
        <div class="custom-text">
            <h5>Contact Me:</h5>
        </div>
    """,
    unsafe_allow_html=True
    )
    
    # Inject custom CSS to use Material Symbols Outlined and set styles
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined');

    .material-symbols-outlined {
        font-variation-settings:
        'FILL' 0,
        'wght' 400,
        'GRAD' 0,
        'opsz' 24;
        font-size: 50px; 
        color: #3e6184; 
        vertical-align: middle;
        margin-right: 8px;
    }

    .contact-info {
        display: flex;
        align-items: center;
        gap: 30px;
        color: #3e6184;
        font-size: 19px;
    }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 30px; color: #3e6184; font-size: 19px;">

    <!-- Email -->
    <div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Mail_%28iOS%29.svg" width="50" style="vertical-align: middle; margin-right: 8px;">
        <strong>Email:</strong> <a href="mailto:gomolemo.kot@gmail.com" style="text-decoration: none; color: #3e6184;">gomolemo.kot@gmail.com</a>
    </div>

    <!-- LinkedIn -->
    <div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="50" style="vertical-align: middle; margin-right: 8px;">
        <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/gomolemo-kototsi-4215b013a/?originalSubdomain=za" target="_blank" style="text-decoration: none; color: #3e6184;">linkedin.com/in/GomolemoKototsi</a>
    </div>

    <!-- GitHub -->
    <div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="50" style="vertical-align: middle; margin-right: 8px;">
        <strong>GitHub:</strong> <a href="https://github.com/GomolemoKototsiAnalyst" target="_blank" style="text-decoration: none; color: #3e6184;">https://github.com/GomolemoKototsiAnalyst</a>
    </div>

    <!-- Location -->
    <div>
        <span class="material-symbols-outlined">location_on</span>
        <strong>Address:</strong> Joburg, South Africa
    </div>

    <!-- Instagram -->
    <div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="50" style="vertical-align: middle; margin-right: 8px;">
        <strong>Instagram:</strong> <a href="https://www.instagram.com/gomolemoartifex/" target="_blank" style="text-decoration: none; color: #3e6184;">https://www.instagram.com/gomolemoartifex/</a>
    </div>
    
    </div>
    """, unsafe_allow_html=True)
    
    
def ITSM_Incident_Portal():
    
    #Using Important Libraries: 
    import streamlit as st
    import altair as alt
    import pandas as pd
    import numpy as np
    import string
    import plotly.express as px
    from datetime import datetime, timedelta
    import plotly.graph_objects as go
    import folium
    from PIL import Image
    import matplotlib.pyplot as plt
    import base64
    import requests
    from io import StringIO


    def get_resized_icon(image_path, width):
        try:
            img = Image.open(image_path)
            aspect_ratio = img.height / img.width
            resized_img = img.resize((width, int(width * aspect_ratio)))
            buffered = BytesIO()
            resized_img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return img_str
        except FileNotFoundError:
            print(f"File not found: {image_path}")
        return None

    #st.markdown("Regional Service Group Analysis")   
    #st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    
    #Creating a holding frame for my svg icons: 
    def encode_image(image_file):
        with open(image_file, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode()
        return f"data:image/svg+xml;base64,{encoded}"

    #Importing data into my system: Avoiding instances where my excel file is has str headers: 
    def read_csv_from_url(url: str, encoding='ISO-8859-1') -> pd.DataFrame:
        try:
            response = requests.get(url)
            response.raise_for_status() 
           
            csv_text = StringIO(response.text)  
           
            data = pd.read_csv(csv_text, encoding=encoding)
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the CSV file from {url}: {e}")
        except pd.errors.EmptyDataError:
            print(f"No data found in the CSV file at {url}.")
        except pd.errors.ParserError:
            print(f"Error parsing the CSV file at {url}.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file at {url}: {e}")
        return pd.DataFrame() 
    
    #Importing data into my main: 
    url1 =  'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/New.csv'
    url2 =  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/Resolved.csv'
    url3=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident.csv'
    url_A=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/Incident_A.csv'
    url_B=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident_B.csv'
    url_C=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident_C.csv'
    url_D=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident_D.csv'
    url4=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/OnHold.csv'
    url5=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/InProgress.csv'
    url6=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/sys_user.csv'
    #url7=  'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/incident.xlsx'

    # Enter URL of the CSV file
    New = read_csv_from_url(url1)
    Resolved = read_csv_from_url(url2)
    OnHold = read_csv_from_url(url4)
    InProgress = read_csv_from_url(url5)
    data = read_csv_from_url(url3)
    dataA = read_csv_from_url(url_A)
    dataB= read_csv_from_url(url_B)
    dataC = read_csv_from_url(url_C)
    dataD = read_csv_from_url(url_D)
    #endusers_list = read_csv_from_url(url6)

    
    #Loading the data into Python - Data Source Service Now SQL DataBase Sample size to Excel:
    #@st.cache_data
    #Renaming the columns for a unilateral intake:
    InProgress.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    Resolved.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    OnHold.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    New.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    data.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    data.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataA.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataB.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataC.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataD.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
   
    #Working Merged Dataframe: 
    df_merged= pd.concat([data,dataA,dataB,dataC,dataD, InProgress, OnHold, New, Resolved], ignore_index=True)

    #ETL Process to create multiple data marts:: 
    df = df_merged[df_merged['Assignment group'].str.contains("ZA - Bridge Connect|ZA - SAP Support|ZA - Cargo Wise Support|ZA - BOS Support|ZA - Carlo Support|ZA - OVB Techs|ZA - Service Desk|ZA - Infrastructure Support",case=False , na=False)]
    
    # Employees ServiceNow location update:
    from io import StringIO
    #url6=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/sys_user.csv'
    response = requests.get(url6)
    content = response.content.decode('ISO-8859-1', errors='ignore')  # or errors='ignore'
    try:
        endusers_list = pd.read_csv(StringIO(content))
    except Exception as e:
        print(f"Error reading CSV data: {e}")
        
    # Handle duplicates in df1 by keeping the first occurrence
    endusers_list = endusers_list.drop_duplicates(subset='name', keep='first')
    
    # Update DataFrame Location' column based on matching 'Caller' with 'Name'
    df['country'] = df['Caller'].map(endusers_list.set_index('name')['location'])

    df['State'] = df['State'].replace('Closed', 'Resolved')

    df['Assigned to'] = df['Assigned to'].replace('nan', 'System')

    def calculate_sla(row, start_col, end_col, date_format='%Y-%m-%d %H:%M:%S'):
        # Convert the strings to datetime objects
        start_dt = row[start_col]
        end_dt = row[end_col]
    
        # # I have noticed that when I am trying to get the difference of time in hours I am getting an error because the date time column is not
        # passed the correct way so I need to force it 
        if not isinstance(start_dt, datetime):
            start_dt = pd.to_datetime(start_dt)
        if not isinstance(end_dt, datetime):
            end_dt = pd.to_datetime(end_dt)
    
        # If the start and end date are the same, calculate the difference in hours
        if start_dt.date() == end_dt.date():
            delta = end_dt - start_dt   # Definind the difference
            hours = delta.seconds / 3600  # hours
            return f"{hours} hours"
    
        # Calculate the difference excluding weekends: I dont want my weekends to be added to the calculation of the SLA
        total_days = 0
        current_dt = start_dt
    
        while current_dt.date() < end_dt.date():
            if current_dt.weekday() < 5:  # Monday to Friday are 0 to 4
                total_days += 1
            current_dt += timedelta(days=1)
    
        # Subtract 1 if the end date is a weekday and not included in the count yet
        if end_dt.weekday() < 5:
            total_days += 1
        #"{total_days} days"
    
        return f"{total_days} days"

    
    def calculate_timetaken_for_ticketcompletion(df, start_col, end_col,date_format='%Y-%m-%d %H:%M:%S'):
        return df.apply(calculate_sla, axis=1, start_col=start_col, end_col=end_col, date_format=date_format)

    df['time_difference'] = calculate_timetaken_for_ticketcompletion(df, 'Due date', 'Updated',date_format='%Y-%m-%d %H:%M:%S')
    #df['time_difference'] = df.apply(lambda row: calculate_sla(row, 'Due date', 'Updated'), axis=1)
    
    # Coercing my time variable in order for me to have string time parameters
    df['Due date'] = pd.to_datetime(df['Due date'], errors='coerce')
    df['Updated']= pd.to_datetime(df['Updated'], errors='coerce')
    df['Year'] = df['Updated'].dt.year
    df['Year'] = df['Year'].astype(str)
    # Calculate time differences in hours:() 
    df['time_difference_testing'] = (df['Updated'] - df['Due date']).dt.total_seconds() / 3600

    # Categorize the time differences:
    def categorize_difference(state,diff_hours):
        if state == 'In Progress' and diff_hours < 72:
            return 'Within SLA'
        elif 60 <= diff_hours < 72:
            return 'Warning: About to Breach'
        elif diff_hours < 60:
            return 'Met SLA'
        else:
            return 'Breach SLA'
    
    df['category'] = df.apply(lambda row: categorize_difference(row['State'], row['time_difference_testing']), axis=1) 
    
    # Start Building a Board:
    with st.sidebar:
        #svg_url = os.path.join('Images', 'Architectural Design Map.svg')
        #st.image(svg_url, caption='Architectural Data Design for the Dashboard', use_column_width=True)
        st.markdown("<h2 style='text-align: left;'>Regional Service Group Analysis</h2>", unsafe_allow_html=True)
        bridge = os.path.join('Images', 'logo-c-fc-steinweg2x.png')
        #st.image(Gomolemo_path, width=600)
        st.image(bridge, use_column_width=True)  
    
        # Initial selection summary:
        if st.checkbox("ALL IT PERSONNEL", value=True):
            selected_personnel = df["Assigned to"].unique()
        else:
            selected_personnel = st.sidebar.multiselect("Select IT Personnel", df["Assigned to"].unique(), default=df["Assigned to"].unique())
        if st.checkbox("ALL INCIDENTS", value=True):
            selected_status = df["State"].unique()
        else:
            selected_status = st.sidebar.multiselect("Choose Status",df["State"].unique(),df["State"].unique())
        selected_year = st.sidebar.multiselect("Choose Year",df["Year"].unique(),default=df["Year"].unique())
        
    
    # Ensuring that Month Variable is passed as a str datetime variable:
    # Convert 'Month' column to datetime
    df['Month'] = pd.to_datetime(df['Updated'])

    # Extract month name
    df['Month'] = df['Month'].dt.strftime('%B')
    
    # Define the categorical month type with the desired order
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

    # Sort the DataFrame by the 'Month' column
    df = df.sort_values('Month')

    #calculating the net tickets/load analysis for my IT Group as YTD tickets completed: 
    # Function to calculate net tickets: - A measure of Work Accrual: 
    def calculate_net_tickets(df):
        pivot_df = df.pivot_table(index='Month', columns='State', values='Number', aggfunc='size', fill_value=0)
        pivot_df['Net_Tickets'] = (pivot_df['In Progress'] + pivot_df['On Hold'] + pivot_df['New']) - pivot_df['Resolved']
        return pivot_df
    
    # Apply function: 
    net_tickets_df = calculate_net_tickets(df)
    net_tickets_df.reset_index(inplace=True)

    
    #Creative in interactive dataframe: Master Dataframe: 
    filtered_data = df[(df['State'].isin(selected_status)) & (df['Assigned to'].isin(selected_personnel) & (df["Year"].isin(selected_year)))]
    
    # Creating Sub-Data Tables to use for my visualisations:
    
    # State category totals: 
    name_category_totals = filtered_data.groupby(['State', 'Assigned to','category'])['Number'].count().reset_index(name='Count')
    #category_totals:
    category_totals = filtered_data.groupby(['State', 'Assigned to'])['Number'].count().reset_index(name='Count')
    
    #category_totals:
    country_totals =  filtered_data.groupby(['State','country'])['Number'].count().reset_index(name='Count')

    #filtered_totals: Pie chart example:
    filtered_category_totals = country_totals.groupby('State')['Count'].sum().reset_index()
    
    #Filter for the max users
    service_groups = filtered_data.groupby(['Assignment group', 'Assigned to'])['Number'].count().reset_index(name='Count')
    
    incidents = filtered_data.groupby(['Service offering subcategory','country'])['Number'].count().reset_index(name='Count')
    
    # Creating A Interactive IT Personnel Contribution Result Metric: 
    total_counts = filtered_category_totals['Count'].sum()
    
    def ensure_all_states(df, required_states=None):
        if required_states is None:
            required_states = ['In Progress', 'New', 'On Hold', 'Canceled','Resolved']
            
        # Create a DataFrame for missing states with a count of 0
        missing_states = [{'State': state, 'Count': 0} for state in required_states if state not in df['State'].values]
    
        if missing_states:
            missing_states_df = pd.DataFrame(missing_states)
            # Use pd.concat to add missing states to the original DataFrame
            df = pd.concat([df, missing_states_df], ignore_index=True)
        return df
    #Creating a useable dataframe: 
    filtered_category_totals = ensure_all_states(filtered_category_totals,selected_status)

    def get_max_group(service_groups, selected_states):
        # Check if DataFrame is empty
        if service_groups.empty:
            print("The DataFrame is empty.")
            max_group = None
            group_max_incident_count = 0
            percentage_group = 0
            return None, None, 0
        else:
            # Group by 'Assignment group' and sum 'Incident Count'
            total_group = service_groups.groupby('Assignment group')['Count'].sum().reset_index()
            
            # Check if total_group is empty
            if total_group.empty:
                print("No incidents to report.")
                group_with_max_incidents = None
                group_max_incident_count = 0
            else:
                # Identify the group with the maximum incident count
                max_group = total_group.loc[total_group['Count'].idxmax()]
                
                # Handle ties by checking states
                tied_groups = total_group[total_group['Count'] == max_group['Count']]
                if len(tied_groups) > 1:
                    # Check state counts for tied groups
                    state_counts = service_groups[service_groups['Assignment group'].isin(tied_groups['Assignment group'])]
                    state_priority = ['Resolved', 'In Progress', 'New']
                    state_counts['State_Priority'] = pd.Categorical(state_counts['State'], categories=state_priority, ordered=True)
                    state_counts = state_counts.sort_values(by=['State_Priority', 'Count'], ascending=[True, False])
                
                    max_group = state_counts.groupby('Assignment group')['Count'].sum().idxmax()
                
                # Extract the group's name and the incident count
                group_with_max_incidents = max_group if isinstance(max_group, str) else max_group['Assignment group']
                group_max_incident_count = total_group.loc[total_group['Assignment group'] == group_with_max_incidents, 'Count'].values[0]
             
            # Calculate percentage if any incidents are present
            if group_max_incident_count > 0:
                total_group_count = total_group['Count'].sum()
                percentage_group = (group_max_incident_count / total_group_count) * 100
                percentage_group = round(percentage_group)
            else:
                percentage_group = 0
            return group_with_max_incidents, group_max_incident_count, percentage_group
        
    group_with_max_incidents, group_max_incident_count, percentage_group = get_max_group(service_groups, selected_status)
    
    # Creating a function to get totals:
    def total_counts(df, state_list=selected_status):
        if state_list is None:
            # Default list of states to include in the total count
            state_list = ['In Progress', 'New', 'On Hold', 'Resolved']
    
        # Initialize total_counts to zero
        total_counts = 0
    
        # Loop over each state in the state_list
        for state in state_list:
            # Check if the state exists in the DataFrame
            if state in df['State'].values:
                # Add the count for the existing state
                total_counts += df.loc[df['State'] == state, 'Count'].values[0]
            else:
                # If the state is missing, assume its count is zero
                total_counts += 0
    
        return total_counts
    
    # Functioning totals:
    total_counts = total_counts(filtered_category_totals,selected_status)
    
    def get_state_counts(df, selected_states):
        # Initialize the result dictionary only with the selected states
        state_counts = {state: {'count': 0, 'percentage': 0.0} for state in selected_states}
    
        # Calculate the total count for all selected states
        total_count = 0
    
        for state in selected_states:
            if state in df['State'].values:
                count = df.loc[df['State'] == state, 'Count'].values[0]
                state_counts[state]['count'] = count
                total_count += count
                
        # Calculate the percentage for each state
        if total_count > 0:
            for state in selected_states:
                state_counts[state]['percentage'] = round((state_counts[state]['count'] / total_count) * 100)
    
        # Calculate the percentage for each state
        if total_count > 0:
            for state in selected_states:
                state_counts[state]['percentage'] = round((state_counts[state]['count'] / total_count) * 100)
    
        # Add the total count to the dictionary
        state_counts['total'] = total_count 
    
        return state_counts
    
    state_counts = get_state_counts(filtered_category_totals, selected_status)
    
    total_in_progress = state_counts.get('In Progress', {}).get('count', 0)

    total_cancelled = state_counts.get('Canceled', {}).get('count', 0)
    percentage_cancelled = state_counts.get('Canceled', {}).get('percentage', 0.0)


    # Safely access the counts, percentages, and total for each selected state
    total_in_progress = state_counts.get('In Progress', {}).get('count', 0)
    percentage_in_progress = state_counts.get('In Progress', {}).get('percentage', 0.0)

    total_new = state_counts.get('New', {}).get('count', 0)
    percentage_new = state_counts.get('New', {}).get('percentage', 0.0)

    total_resolved = state_counts.get('Resolved', {}).get('count', 0)
    percentage_resolved = state_counts.get('Resolved', {}).get('percentage', 0.0)

    # If you need to handle a state that is not selected, you can do so like this:
    total_on_hold = state_counts.get('On Hold', {}).get('count', 0)  # This will be zero if 'On Hold' is not selected
    percentage_on_hold = state_counts.get('On Hold', {}).get('percentage', 0.0) 

    # The total sum of counts for all selected states
    total_count = state_counts.get('total', 0)
    percentage_total =  percentage_on_hold+percentage_resolved+percentage_new+percentage_in_progress+percentage_cancelled

    # Path to your local SVG file:
    #svg_url = os.path.join('Images', 'family_history_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    #st.image(svg_url, caption='Architectural Data Design for the Dashboard', use_column_width=True)
    local_svg_path = os.path.join('Images', 'family_history_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    warning_path = os.path.join('Images', 'warning.svg')
    account_path = os.path.join('Images', 'account_circle_78dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    #groups_iconspath = os.path.join('Images', 'group_add_61dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    icon_url = encode_image(local_svg_path)
    icon_url1 = encode_image(warning_path)
    icon_url2 = encode_image(account_path)
    groups_loc = os.path.join('Images', 'group_add_61dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    groups_icon = encode_image(groups_loc)
    
    # A holding Matrice for  local SVG file: - Paths & Urls 
    local_svg_path = os.path.join('Images', 'family_history_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    local_sa = os.path.join('Images', 'south-africa-flag-icon.svg')
    local_zim =  os.path.join('Images', 'Flag_of_Zimbabwe.svg')
    local_ken =  os.path.join('Images', 'kenya-flag-icon.svg')
    local_tan = os.path.join('Images', 'tanzania-flag-icon.svg')
    local_zam = os.path.join('Images', 'zambia-flag-icon.svg')
    local_mal = os.path.join('Images', 'malawi-svgrepo-com.svg')
    local_moz = os.path.join('Images', 'mozambique-flag-icon.svg')
    local_nam = os.path.join('Images', 'Namibia-01-1.svg')
    
    
    south_african = encode_image(local_sa)
    Zimbabwe = encode_image(local_zim)
    Tanzania = encode_image(local_tan)
    Kenya = encode_image(local_ken)
    Zambia = encode_image(local_zam)
    Mozambique = encode_image(local_moz)
    Malawi=encode_image(local_mal)
    Namibia =encode_image(local_nam)
    
    # Getting a icon using CSS style:- Highest IT Personnel
    Svg_path_paths = os.path.join('Images', 'account_circle_78dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg') 
    #svg_icon = encode_image(Svg_path_paths)
    with open(Svg_path_paths, "r") as file:
        svg_icon = file.read()


    groups_icon_path =  os.path.join('Images', 'group_add_61dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    # Getting a icon using CSS style: - Highest
    with open(groups_icon_path, "r") as file:
        #groups_icon_path =  os.path.join('Images', 'group_add_61dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
        groups_icon = file.read()
        
    # Creating a Dictionary for my Countries Flags:
    data = {
        'Country': ['South Africa', 'Zimbabwe','Mozambique', 'Tanzania','Kenya','Zambia','Malawi'],
        'Flag_URL': [
            south_african,Zimbabwe,Mozambique, Tanzania, Kenya, Zambia, Malawi
        ]
    }
    # Converting the dictionary into a Dataframe - Easy to call functions: 
    nations_df = pd.DataFrame(data)

    
    #Creating different color schemes - For my States Donut Chart: 
    color_discrete_map = {
        'Within SLA': '#92afcc',
        'Met SLA': '#3e6184',
        'Warning: About to Breach': '#d5e0ec',
        'Breach SLA': '#5d88b3'}
        

    # Function to create a metric with a flag icon
    def metric_with_flag(label, value, percentage, flag_url):
        # Create an empty figure
        fig = go.Figure()

        # Add the flag icon
        fig.add_layout_image(
            dict(
                source=flag_url,
                xref="paper", yref="paper",
                x=0.1, y=0.5,
                sizex=0.2, sizey=0.2,
                xanchor="center", yanchor="middle"
            )
        )

        # Add the country name, total count, and percentage
        fig.add_annotation(
            dict(
                text=f"<b>{label}</b><br>Total: {value}<br>Contribution Percentage: {percentage}%",
                x=0.2, y=0.5,
                xref="paper", yref="paper",
                showarrow=False,
                font=dict(size=12)
            )
        )

        # Update layout to adjust margins
        fig.update_layout(
            margin=dict(l=0, r=0, t=20, b=20),
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            width=400,  # Adjust the width of the figure
            height=250,  # Adjust the height of the figure
        )
        return fig
    
    def ensure_all(df, required_states=None, required_personnel =None):
        if required_states is None:
            # Default required states
            required_states = ['In Progress', 'New', 'Canceled' ,'On Hold', 'Resolved']
        if required_personnel is None:
            # Default required persons:
            required_personnel = list(df['Assigned to'].unique()) if 'Assigned to' in df.columns else []
    
        # Check for missing states and add them with a count of zero
        for state in required_states:
            if state not in df['State'].values:
                pd.concat([df, pd.DataFrame([{'State': state, 'Count': 0}])], ignore_index=True)
                #df = df.append({'State': state, 'Count': 0}, ignore_index=True)
        for personnel in required_personnel:
            if personnel not in df['Assigned to'].values:
                pd.concat([df, pd.DataFrame([{'State': state, 'Count': 0}])], ignore_index=True)
                #df = df.append({'Assigned to': personnel, 'Count': 0}, ignore_index =True)
    
        return df
    
    testing = filtered_data.groupby(['State','country','Assigned to'])['Number'].count().reset_index(name='Count')
    
    users_max = testing.groupby(['Assigned to','State'])['Count'].sum().reset_index()
    
    testing = ensure_all(testing,selected_status, selected_personnel)
    
    def calculate_max_user(users_totals):
        # Check if DataFrame is empty
        if name_category_totals.empty:
            print("The DataFrame is empty.")
            return {"max_user": 0, "max_incident_count": 0, "percentage": 0}

        # Group by 'Assigned to' and sum 'Count'
        total_person = name_category_totals.groupby('Assigned to')['Count'].sum().reset_index()

        # Check if total_person is empty
        if total_person.empty:
            print("No incidents to report.")
            return {"max_user": 0, "max_incident_count": 0, "percentage": 0}

        # Identify the user(s) with the maximum incident count
        max_incident_count = total_person['Count'].max()
        max_users = total_person[total_person['Count'] == max_incident_count]
        
        if len(max_users) > 1:
            state_priority = ['Resolved', 'New', 'In Progress', 'On Hold']
            state_sums = name_category_totals[name_category_totals['State'].isin(state_priority)].groupby(['Assigned to', 'State'])['Count'].sum().unstack(fill_value=0)
            
            max_user = None
            max_state_sum = 0
            
            for state in state_priority:
                if state in state_sums.columns:
                    state_sums_sorted = state_sums[state].nlargest(1)
                    if state_sums_sorted.iloc[0] > max_state_sum:
                        max_state_sum = state_sums_sorted.iloc[0]
                        max_user = state_sums_sorted.index[0]
            if max_user is None:
                max_user = max_users.iloc[0]['Assigned to']
        else:
            max_user = max_users.iloc[0]['Assigned to']
            
        if max_user == 0 or not max_user:
            print("No user with incidents to report.")
            return {"max_user": 0, "max_incident_count": 0, "percentage": 0}
    
        # Calculate the percentage of incidents handled by the max user
        total_incident_count = total_person['Count'].sum()
        percentage = (max_incident_count / total_incident_count) * 100 if total_incident_count > 0 else 0
        percentage = round(percentage)

        print(f"User with the highest incidents: {max_user} with {max_incident_count} incidents")
        print(f"Percentage of incidents handled by {max_user}: {percentage}%")

        return max_user, max_incident_count, percentage
    
    max_user,max_incident_count,percentage = calculate_max_user(testing)
    country_totals = testing.groupby(['State','country'])['Count'].sum().reset_index()
    countries_test=  country_totals.groupby('country')['Count'].sum().reset_index()
    
    def top_country(df, state_df=None):
        # Normalize country names to avoid case differences
        df['country'] = df['country'].str.title()
    
        # Pivot the state DataFrame to create separate columns for each state
        pivot_df = state_df.pivot_table(index='country', columns='State', values='Count', fill_value=0).reset_index()
    
        # Merge the count DataFrame with the pivoted state DataFrame
        df = df.merge(pivot_df, on='country', how='left')
    
        # Ensure all relevant columns are present and sorted by Count
        df = df.fillna(0)  # Fill NaN values with 0
        df = df.sort_values(by='Count', ascending=False)
    
        return df
    
    def rank_countries(df):
        # Group by country and sum the counts
        grouped_df = df.groupby('country', as_index=False).sum()
    
        # Sort by the 'Count' column in descending order
        sorted_df = grouped_df.sort_values(by='Count', ascending=False)
    
        # Determine how many countries are available after filtering
        num_countries = len(sorted_df)
    
        # Apply ranking based on the number of available countries
        if num_countries >= 3:
            # Return the top 3 countries if more than 2 are available
            ranked_df = sorted_df.head(3)
            ranked_df['Rank'] = ['Highest', 'Second Highest', 'Third Highest']
        elif num_countries == 2:
            # Return only the top 2 countries
            ranked_df = sorted_df.head(2)
            ranked_df['Rank'] = ['Highest', 'Second Highest']
        else:
            # If only one country is available, just return that country
            ranked_df = sorted_df.head(1)
            ranked_df['Rank'] = ['Highest']
    
        return ranked_df

    #sorted_countries_test:
    sorted_countries_test = rank_countries(countries_test)
    sorted_countries_test['percentage'] = round((sorted_countries_test['Count']/total_counts)*100)

    # Create figures for selected personnel
    def get_flag_url(country, df):
        # Check if country is not NaN and convert to lower case
        if pd.notna(country):
            country_name = str(country).lower()
            flag_url = df[df['Country'].str.lower() == country_name]['Flag_URL'].values
            if len(flag_url) > 0:
                return flag_url[0]  
            else:
                return None  
        else:
            return None 
        
    # Initialize the metrics for second and third to zero or a default value
    second_metric = {'label': 'Second: N/A', 'Count': 0, 'percentage': 0, 'flag_url': None}
    third_metric = {'label': 'Third: N/A', 'Count': 0, 'percentage': 0, 'flag_url': None}

    # Get the first country
    first = metric_with_flag(f'Highest: {sorted_countries_test.country.iloc[0]}', sorted_countries_test.Count.iloc[0], sorted_countries_test.percentage.iloc[0], get_flag_url(sorted_countries_test.country.iloc[0], nations_df))

    # Check if there is a second country
    if len(sorted_countries_test) > 1:
        second_metric = {
            'label': f'Second: {sorted_countries_test.country.iloc[1]}',
            'Count': sorted_countries_test.Count.iloc[1],
            'percentage': sorted_countries_test.percentage.iloc[1],
            'flag_url': get_flag_url(sorted_countries_test.country.iloc[1], nations_df)
       }

    # Check if there is a third country
    if len(sorted_countries_test) > 2:
        third_metric = {
            'label': f'Third: {sorted_countries_test.country.iloc[2]}',
            'Count': sorted_countries_test.Count.iloc[2],
            'percentage': sorted_countries_test.percentage.iloc[2],
            'flag_url': get_flag_url(sorted_countries_test.country.iloc[2], nations_df)
      }
    
    # Create the metrics with the updated values
    second = metric_with_flag(second_metric['label'], second_metric['Count'], second_metric['percentage'], second_metric['flag_url'])
    third = metric_with_flag(third_metric['label'], third_metric['Count'], third_metric['percentage'], third_metric['flag_url'])

    #Main board:  Header Overview:  
    col = st.columns((2, 4, 2), gap='medium')
    colors = ['#3e6184','#2e4459' ,'#5d88b3', '#92afcc', '#d5e0ec']
    with col[0]:
        first
        #st.markdown('### IT Incidents Status Summary:')
        #Create a 3D donut chart
        fig = go.Figure(data=[go.Pie(
            labels=category_totals['State'],
            values=category_totals['Count'],
            hole=0.6,  # Makes it a donut chart
            textinfo='percent+label',
            marker=dict(colors=colors))])
    
        #Add SVG Icon to the center of the donut chart:
        fig.update_layout(
            title_text='IT Incidents Status Summary:',
            images=[dict(
                source=icon_url,
                xref="paper", yref="paper",
                x=0.5, y=0.5,
                sizex=0.6, sizey=0.25,
                xanchor="center", yanchor="middle"
            )], 
            annotations=[dict(
                text='',  # If you want to add any text below the icon
                x=0.6, y=0.56, font_size=20, showarrow=False
            )]
        )
         # Show the donut chart:
        st.plotly_chart(fig, use_container_width=True)
    
        #Second For the first Column:
        #st.title("Top Service Group Requestsy: ")
    
        # Top IT Personnel:
        title_person = f'IT Personnel: {max_user}'
        value_person = f'Assigned Total: {str(max_incident_count)}'
        delta_person = f'Contribution: {str(percentage)}'
        #group_with_max_incidents, group_max_incident_count, percentage_group = get_max_group(service_groups, selected_status)
        #Top Service Group
        title_group = f'IT Service Group: {group_with_max_incidents}'
        value_group = f'Group Assigned Total: {str(group_max_incident_count)}'
        delta_group = f'Contribution: {str(percentage_group)}%'
        
        def metric_with_icon(label, value, delta, svg_icon):
            #Resize the SVG icon
            html = f"""
            <div style="display: flex; align-items: center; border: 2px solid #000; padding: 10px; border-radius: 5px;">
            <div style="display: flex; align-items: center;">
                <div style="display: inline-block;">{svg_icon}</div>
                <div style="display: inline-block; margin-left: 8px;">
                    <div style="font-weight: bold;">{label}</div>
                    <div style="font-size: 2rem;">{value}</div>
                    <div style="color: {'green' if delta.startswith('+') else '#3e6184'};">{delta}</div>
                </div>
            </div>
            """
            st.markdown(html, unsafe_allow_html=True)
            
        #Displing the user:             
        metric_with_icon(title_person, value_person ,delta_person, svg_icon)
    
        #Displaying Max group:
        metric_with_icon(title_group, value_group ,delta_group, groups_icon)
    
    with col[1]:
        second
        fig = px.bar(
            name_category_totals,
            x='Assigned to',
            y='Count',
            color='category',
            color_discrete_map= color_discrete_map,
            barmode='group',
            title='IT Incidents SLA Compliance Analysis by IT Personnel',
            labels={'Count': 'Total Incidents', 'Assigned to': 'IT Technician'}
        )
    
        # Plotting the function in Python:  
        st.plotly_chart(fig, use_container_width=True)
        st.write('### WorkLoad Accrual Analysis')
        #source = pd.DataFrame(data)
        # Converting the nets incidents load into a function:
    
        data = [
            {"label": "Begin", "amount": 185},
            {"label": "Jan", "amount": 205},
            {"label": "Feb", "amount": 50},
            {"label": "Mar", "amount": 70},
            {"label": "Apr", "amount": 10},
            {"label": "May", "amount": -20},
            {"label": "Jun", "amount": -179},
            {"label": "Jul", "amount": 0},
            {"label": "Aug", "amount": 0},
            {"label": "Sep", "amount": 0},
            {"label": "Oct", "amount": 0},
            {"label": "Nov", "amount": 0},
            {"label": "Dec", "amount": 0},
            {"label": "End", "amount": 0},
        ]
        source = pd.DataFrame(data)
        # The "base_chart" defines the transform_window, transform_calculate, and X axis
        # Create a base chart using Altair
        base_chart = alt.Chart(source).mark_bar().encode(
            x=alt.X('label:O', title='Label'),
            y=alt.Y('amount:Q', title='In Progress Count'),
            tooltip=['label:O', 'amount:Q']
        ).properties(
            title='In Progress Tickets per Month'
        )

        # The "base_chart" defines the transform_window, transform_calculate, and X axis
        base_chart = alt.Chart(source).transform_window(
            window_sum_amount="sum(amount)",
            window_lead_label="lead(label)",
        ).transform_calculate(
            calc_lead="datum.window_lead_label === null ? datum.label : datum.window_lead_label",
            calc_prev_sum="datum.label === 'End' ? 0 : datum.window_sum_amount - datum.amount",
            calc_amount="datum.label === 'End' ? datum.window_sum_amount : datum.amount",
            calc_text_amount="(datum.label !== 'Begin' && datum.label !== 'End' && datum.calc_amount > 0 ? '+' : '') + datum.calc_amount",
            calc_center="(datum.window_sum_amount + datum.calc_prev_sum) / 2",
            calc_sum_dec="datum.window_sum_amount < datum.calc_prev_sum ? datum.window_sum_amount : ''",
            calc_sum_inc="datum.window_sum_amount > datum.calc_prev_sum ? datum.window_sum_amount : ''",
        ).encode(
            x=alt.X(
                "label:O",
                axis=alt.Axis(title="Months", labelAngle=0),
                sort=None,
            )
        )
        color_coding = {
            "condition": [
                {"test": "datum.label === 'Begin' || datum.label === 'End'", "value": "#d5e0ec"},
                {"test": "datum.calc_amount < 0", "value": "#3e6184"},
            ],
            "value": "#5d88b3",
        }
        bar = base_chart.mark_bar(size=45).encode(
            y=alt.Y("calc_prev_sum:Q", title="Workload"),
            y2=alt.Y2("window_sum_amount:Q"),
            color=color_coding,
        )
        # The "rule" chart is for the horizontal lines that connect the bars
        rule = base_chart.mark_rule(
            xOffset=-22.5,
            x2Offset=22.5,
        ).encode(
            y="window_sum_amount:Q",
            x2="calc_lead",
        )
        # Add values as text
        text_pos_values_top_of_bar = base_chart.mark_text(
            baseline="bottom",
            dy=-4
        ).encode(
            text=alt.Text("calc_sum_inc:N"),
            y="calc_sum_inc:Q"
        )
        text_neg_values_bot_of_bar = base_chart.mark_text(
            baseline="top",
            dy=4
        ).encode(
            text=alt.Text("calc_sum_dec:N"),
            y="calc_sum_dec:Q"
        )
        text_bar_values_mid_of_bar = base_chart.mark_text(baseline="middle").encode(
            text=alt.Text("calc_text_amount:N"),
            y="calc_center:Q",
            color=alt.value("white"),
        )
        
        # Combine the layers into one chart
        final_chart = alt.layer(
            bar,
            rule,
            text_pos_values_top_of_bar,
            text_neg_values_bot_of_bar,
            text_bar_values_mid_of_bar
        ).properties(
            width=800,
            height=450
        )
        # Display the Altair chart
        st.altair_chart(final_chart, use_container_width=True)
    with col[2]:
        third
        # CSS styling my St.Metric: 
        pmg_him = f"""
        <style>
         @media (prefers-color-scheme: light) {{
            [data-testid="stMetric"] {{
                border-radius: 5px;
                border: 2px solid #000;
                margin: 5px;  /* Reduce space between metrics */
                padding: 10px;
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: flex-start;
                height: 100px; /* Adjust height as needed */
                overflow: hidden; /* Ensure content does not overflow */
                }}
        }}
    
        @media (prefers-color-scheme: dark) {{
            [data-testid="stMetric"] {{
                border-radius: 10px;
                border: 2px solid #000;
                margin: 5px;  /* Reduce space between metrics */
                padding: 10px;
                display: flex;
                flex-direction: row;
                align-items: center;
                justify-content: flex-start;
                height: 100px; /* Adjust height as needed */
                overflow: hidden; /* Ensure content does not overflow */
                }}
        }}
        [data-testid="stMetricText"] {{
            display: flex;
            flex-direction: column;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            width: 100%;
        }}
        [data-testid="stMetricIcon"] {{
            margin-right: 10px;
            flex-shrink: 0; /* Prevent icon from shrinking */
        }}
        [data-testid="stMetricValue"],
        [data-testid="stMetricDelta"],
        [data-testid="stMetricLabel"] {{
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }}
        [data-testid="stMetricValue"]{{
            font-weight: bold;
            font-size: 1.5em;
        }}
        [data-testid="stMetricDelta"]{{
            font-weight: bold;
            font-size: 1.5em;
        }}
        [data-testid="stMetricLabel"] {{
            font-weight: bold;
            font-size: 1em; 
        }}
        </style>
        """
        st.markdown(pmg_him, unsafe_allow_html=True)
        with st.container():
            #col1, col2, col3, = st.columns(3):
            svg_progress_path =  os.path.join('Images', 'pending_50dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
            svg_new_path =  os.path.join('Images', 'domain_add_64dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
            svg_resolved_path =  os.path.join('Images', 'editor_choice_50dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
            svg_total_path =  os.path.join('Images', 'dataset_50dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
            svg_hold_path =  os.path.join('Images', 'back_hand_50dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
            svg_cancelled_path =  os.path.join('Images', 'delete_forever_40dp_3E6184_FILL0_wght400_GRAD0_opsz40.svg')
            svg_progress = encode_image(svg_progress_path)
            svg_new = encode_image(svg_new_path)
            svg_resolved = encode_image(svg_resolved_path)
            svg_total =  encode_image(svg_total_path)
            svg_hold = encode_image(svg_hold_path)
            svg_cancelled = encode_image(svg_cancelled_path)
            def iconMetricContainer(label, value, delta, icon_url):
                html = f"""
                <div data-testid="stMetric" style=" display: flex; align-items: center; justify-content: space-between;">
                    <img data-testid="stMetricIcon" src="{icon_url}" alt="Icon" style="width: 40px; height: 40px;">
                    <div data-testid="stMetricText" style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100%;">
                        <div data-testid="stMetricLabel">{label}</div>
                        <div data-testid="stMetricValue">{value}</div>
                        <div data-testid="stMetricDelta">{delta}</div>
                    </div>
                </div>
                """
                return html

            st.markdown(iconMetricContainer(label=f'In Progress',value = f'{int(total_in_progress)}',delta= f'{int(percentage_in_progress)}%',icon_url=svg_progress), unsafe_allow_html=True)
            st.markdown(iconMetricContainer(label=f'New',value = f'{int(total_new)}',delta= f'{int(percentage_new)}%',icon_url=svg_new), unsafe_allow_html=True)       
            st.markdown(iconMetricContainer(label="Resolved",value=f'{int(total_resolved)}',delta=f'{int(percentage_resolved)}%', icon_url=svg_resolved), unsafe_allow_html=True)
            st.markdown(iconMetricContainer(label="On-Hold",value=f'{int(total_on_hold)}',delta=f'{int(percentage_on_hold)}%',icon_url=svg_hold), unsafe_allow_html=True)
            st.markdown(iconMetricContainer(label="Cancelled",value=f'{int(total_cancelled)}',delta=f'{int(percentage_cancelled)}%',icon_url=svg_cancelled), unsafe_allow_html=True)
            st.markdown(iconMetricContainer(label="Workload",value=f'{int(total_counts)}',delta=f'{int(percentage_total)}%',icon_url=svg_total), unsafe_allow_html=True)
            
def Testing_Thoughts():
    # Important libraries: 
    import streamlit as st    
    import altair as alt
    import pandas as pd
    import numpy as np
    import string
    import re
    import requests
    import plotly.express as px
    from datetime import datetime, timedelta
    import base64
    import plotly.graph_objects as go
    import matplotlib.pyplot as plt
    from PIL import Image
    import matplotlib.pyplot as plt
    import base64
    import requests
    from io import StringIO


    #Importing data into my system: Avoiding instances where my excel file is has str headers: 
    def read_csv_from_url(url: str, encoding='ISO-8859-1') -> pd.DataFrame:
        try:
            response = requests.get(url)
            response.raise_for_status() 
           
            csv_text = StringIO(response.text)  
           
            data = pd.read_csv(csv_text, encoding=encoding)
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the CSV file from {url}: {e}")
        except pd.errors.EmptyDataError:
            print(f"No data found in the CSV file at {url}.")
        except pd.errors.ParserError:
            print(f"Error parsing the CSV file at {url}.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file at {url}: {e}")
        return pd.DataFrame() 

        
    #Importing data into my main: 
    url1 = 'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/New.csv'
    url2 = 'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/Resolved.csv'
    url3=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident.csv'
    url_A=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/Incident_A.csv'
    url_B=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident_B.csv'
    url_C=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident_C.csv'
    url_D=  'https://github.com/GomolemoKototsiAnalyst/DataHub-App/blob/main/Raw%20data/incident_D.csv'
    url4=  'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/OnHold.csv'
    url5=  'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/InProgress.csv'
    url6=  'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/sys_user.csv'
    url7=  'https://raw.githubusercontent.com/GomolemoKototsiAnalyst/DataHub-App/main/Raw%20data/incident.xlsx'
    
    New = read_csv_from_url(url1)
    Resolved = read_csv_from_url(url2)
    OnHold = read_csv_from_url(url4)
    InProgress = read_csv_from_url(url5)
    data1 = read_csv_from_url(url3)
    dataA = read_csv_from_url(url_A)
    dataB= read_csv_from_url(url_B)
    dataC = read_csv_from_url(url_C)
    dataD = read_csv_from_url(url_D)
    endusers_list = read_csv_from_url(url6)
  
    #Renaming the columns for a unilateral intake:
    InProgress.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    Resolved.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    OnHold.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    New.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)

    #data.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       #'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    
    data1.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataA.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataB.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataC.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
    dataD.rename(columns={'number': 'Number', 'due_date': 'Due date', 'short_description':'Short description','caller_id':'Caller', 'priority':'Priority',
       'state':'State', 'category':'Category', 'assignment_group':'Assignment group', 'assigned_to':'Assigned to','sys_updated_on':'Updated','sys_updated_by':'Updated by' ,'u_service_offering_subcategory':'Service offering subcategory' }, inplace=True)
   
    # Employees ServiceNow location update: 
    #locate= "C:/Users/Gomolemo.Kototsi/Downloads/sys_user.csv"
    #endusers_list = pd.read_csv(locate, encoding='ISO-8859-1')
    
    # Handle duplicates in df1 by keeping the first occurrence
    endusers_list = endusers_list.drop_duplicates(subset='name', keep='first') 
    
    #ETL Process:
    df_merged= pd.concat([dataA, dataB, dataC, dataD, data1, InProgress, OnHold, New, Resolved], ignore_index=True)
                         
    df_merged.loc[df_merged['State'] == 'Closed', 'State'] = 'Resolved'
                         
    df_merged.State.unique()                
                         
    # filtering our working dataframe with the Assignment groups that matter: 
    df = df_merged[df_merged['Assignment group'].str.contains("ZA - Cargo Wise Support|ZA - Bridge Connect|'ZA - SAP Support'|ZA - BOS Support|ZA - Carlo Support|ZA - OVB Techs|ZA - Service Desk|ZA - Infrastructure Support",case=False , na=False)]
                                 
    #Creating a time difference variable to calculate SLA Compliance:
    def calculate_sla(row, start_col, end_col, date_format='%Y-%m-%d %H:%M:%S'):
        
        df['Due date'] = pd.to_datetime(df['Due date'], errors='coerce')
        df['Updated']= pd.to_datetime(df['Updated'], errors='coerce')
        # Convert the strings to datetime objects
        start_dt = row[start_col]
        end_dt = row[end_col]
    
        ## I have noticed that when I am trying to get the difference of time in hours I am getting an error because the date time column is not
        # passed the correct way so I need to force it 
        if not isinstance(start_dt, datetime):
            start_dt = pd.to_datetime(start_dt)
        if not isinstance(end_dt, datetime):
            end_dt = pd.to_datetime(end_dt)
    
        # If the start and end date are the same, calculate the difference in hours
        if start_dt.date() == end_dt.date():
            delta = end_dt - start_dt   # Definind the difference
            hours = delta.seconds / 3600  # hours
            return f"{hours} hours"
    
        # Calculate the difference excluding weekends: I dont want my weekends to be added to the calculation of the SLA
        total_days = 0
        current_dt = start_dt
    
        while current_dt.date() < end_dt.date():
            if current_dt.weekday() < 5:  # Monday to Friday are 0 to 4
                total_days += 1
            current_dt += timedelta(days=1)
    
        # Subtract 1 if the end date is a weekday and not included in the count yet
        if end_dt.weekday() < 5:
            total_days += 1
        #"{total_days} days"
    
        return f"{total_days} days"

    def calculate_timetaken_for_ticketcompletion(df, start_col, end_col,date_format='%Y-%m-%d %H:%M:%S'):
        return df.apply(calculate_sla, axis=1, start_col=start_col, end_col=end_col, date_format=date_format)
    
    df['time_difference'] = calculate_timetaken_for_ticketcompletion(df, 'Due date', 'Updated',date_format='%Y-%m-%d %H:%M:%S')
    
    #Update DataFrame 2's 'Location' column based on matching 'Caller' with 'Name'
    df['country'] = df['Caller'].map(endusers_list.set_index('name')['location'])
           
    # Coercing the date:                      
    df['Due date'] = pd.to_datetime(df['Due date'], errors='coerce')
    df['Updated']= pd.to_datetime(df['Updated'], errors='coerce')

    # Split the date column--- timestamps & date separated - the day the incident was opened and closed
    df['open_Date'] =  df['Due date'].dt.date
    df['open_Time'] = df['Due date'].dt.time
    df['close_Date'] =  df['Updated'].dt.date
    df['close_Time'] = df['Updated'].dt.time
    df['Year'] = df['Due date'].dt.year

    #delete all the tickets that are ServiceNow as resolved even though they were recalled by the caller:  Using the Query statement
    filter = df['Short description'].str.contains('Recall');
    clean_df = df[~filter];
    
    clean_df['Month_1'] = pd.to_datetime(clean_df['open_Date'], format='%Y-%m')

    clean_df['Month']= clean_df['Month_1'].dt.strftime('%B')

    month_dict = {'January':1,'February':2,'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}

    clean_df['Month'] = pd.Categorical(clean_df['Month'], categories=month_dict, ordered=True)

    clean_df.sort_values(by = 'Month',inplace=True)
    
    # Convert datetime.date to string
    clean_df['Month']= clean_df['Month'].astype(str)
    
    tickets_logged = clean_df.groupby(['Month', 'Assignment group']).size().reset_index(name='Tickets Logged')
    
    tickets_logged_df = tickets_logged.groupby('Assignment group', as_index=False)['Tickets Logged'].sum()
    

    def no_incidents_logged(dat, column, options):
        counts = [(option, (dat[column] == option).sum()) for option in options]
        return pd.DataFrame(counts, columns=['Service Group', 'Incidents Logged'])

    # Defining the services group I want the count for incidents for: 
    options = ['ZA - Cargo Wise Support','ZA - BOS Support', 'ZA - Carlo Support', 'ZA - OVB Techs',
               'ZA - Service Desk', 'ZA - Infrastructure Support', 'ZA - Bridge Connect', 'ZA - SAP Support']
    
    def no_incidents_logged_per_month(df, date_column, target_column, options):
       
        #converting the date the tickets were logged into Months 
        df['Opened_month']= pd.to_datetime(df['open_Date']).dt.to_period("M")
  
        # Initialize an empty list to store the results
        results = []
            
        # Filter the DataFrame for the given options
        filtered_df = df[df['Assignment group'].isin(options)]

        # Group by 'Month' and 'Option' and count occurrences
        counts_df = filtered_df.groupby([target_column, 'Month']).size().reset_index(name='Count')

        # Convert the results list into a DataFrame
        counts_df.columns=['Service Group','Month', 'Incidents']

        return counts_df

    # Updating the Current Dataframe: 
    counts_df = no_incidents_logged_per_month(clean_df, 'Month', 'Assignment group', options)
    
    
    #Calculate time differences in hours
    #clean_df['time_difference_testing'] = (clean_df['Updated'] - clean_df['Due date']).dt.total_seconds() / 3600
    #def categorize_difference(diff_hours):
    #    try:
    #        # Convert diff_hours to float if it's a string or non-integer value
    #        diff_hours = float(diff_hours)
        
     #       # Continue with your logic
     #       if 0 <= diff_hours <= 72:
      #          return 'Met SLA'
       #     elif diff_hours > 72:
       #         return 'Breach SLA'
       # except ValueError:
       #     return 'Invalid time difference'
        
    # Categorize the time differences
    def categorize_difference(diff_hours):
        if diff_hours < 72:
            return 'Met SLA'
        else:
            return 'Breach SLA'
            
    clean_df['time_difference'] = pd.to_numeric(clean_df['time_difference'], errors='coerce')
    
    # Updating the Current Dataframe with the Calcultated Categories: 
    clean_df['category'] = clean_df['time_difference'].apply(categorize_difference)

 
    #clean_df['time_difference'] = calculate_timetaken_for_ticketcompletion(clean_df, 'Due date', 'Updated',date_format='%Y-%m-%d %H:%M:%S')
    #df['time_difference'] = df.apply(lambda row: calculate_sla(row, 'Due date', 'Updated'), axis=1)
      
    # Filter the DataFrame
    df_not_met_sla = clean_df[clean_df['category'] == 'Breach SLA']
    df_met_sla = clean_df[clean_df['category'] == 'Met SLA']
    
    
    # Creating a holding frame for my svg icons: 
    def encode_image(image_file):
        with open(image_file, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode()
        return f"data:image/svg+xml;base64,{encoded}"
    
    
    # Path to your local SVG file:
    #vg_progress_path =  os.path.join('Images', 'new_releases_53dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    #svg_progress = encode_image(svg_progress_path)
    local_svg_path = os.path.join('Images', 'report_64dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    local_breach = os.path.join('Images', 'new_releases_53dp_3E6184_FILL0_wght400_GRAD0_opsz48.svg')
    
    # Converting the image to an SVG icon: 
    icon_testing = encode_image(local_svg_path)
    icon_met = encode_image(local_breach)
    
    # making of color scales: This feeds the approved colors for Bridge Business Intelligence Dashboards: 
    custom_color_scale = ['#3e6184', '#5d88b3', '#92afcc', '#d5e0ec']

    # Define the color schemes:
    color_theme_list = {
        'CSBJHB1': ['#5d88b3', '#2e4459','#6d93ba','#becfe0','#495766', '#1d2328','#8c96a0','#d8e3ec'],
        'CSBJHB2': ['#005172','#003044', '#001822', '#4c859c', '#99b9c6','#4c859c' , '#99b2bc','#668b9a'],
        'CSBJHB3': ['#002748', '#193c5a', '#32526c', '#4c677e', '#667d91', '#7f93a3','#99a8b5', '#b2bec8'],
        'CSBJHB4': ['#2d2a27', '#5a544e','#cac5c1','#f4f3f2','#005475', '#008cc4', '#006289', '#005475']
    }
    
    # CSS to inject contained in a string
    sidebar_style = """
        <style>
            .css-1d391kg .css-145kmo2 {
                color: #8BA0B5;
            }
        </style>
        """
    # Inject CSS with st.markdown
    st.markdown(sidebar_style, unsafe_allow_html=True)
    
    #Getting my JSONN country bame for Tanzania to correlate with the geospatial name: 
    clean_df["country"] =  clean_df["country"].replace("Tanzania", "United Republic of Tanzania")
    
    clean_df['country'] = clean_df['country'].astype(str)

    clean_df['Year'] = clean_df['Year'].astype(str)
                         
    # Creating a Sidebar for the New Page: 
    with st.sidebar:
        #st.markdown("<h3 style='text-align: left;'>SLA FILTERI</h3>", unsafe_allow_html=True)
        bridge_path = os.path.join('Images', 'logo-c-fc-steinweg2x.png')
        #st.image(Gomolemo_path, width=600)
        st.image(bridge_path, use_column_width=True)  
        #st.image("C:/Users/Gomolemo.Kototsi/Downloads/logo-c-fc-steinweg2x.png", use_column_width=True)  # Insert your image here
        # Initial selection summary:
        if st.checkbox("Select All Months", value=True):
            selected_month = sorted(clean_df["Month"].unique())
        else:
            selected_month = st.sidebar.multiselect("Select Month",sorted((clean_df["Month"]).unique()),default=sorted(clean_df["Month"].unique()))
        if st.checkbox("Select All Countries", value=True):
            selected_countries = sorted(clean_df["country"].unique())
        else:
            selected_countries = st.multiselect("Choose countries",sorted((clean_df["country"]).unique()), default=sorted(clean_df["country"].unique()))
    
        # Interactive Color themes:
        selected_year = st.multiselect('Select a Year',sorted((clean_df["Year"]).unique()),default=sorted(clean_df["Year"].unique()))                                     
        selected_color_theme = st.selectbox('Select a color theme', list(color_theme_list.keys()))
    
    # Generic Interactive Dataframe: 
    filtered_df = clean_df[clean_df["country"].isin(selected_countries) & (clean_df["Month"].isin(selected_month))& (clean_df["Year"].isin(selected_year))]

    #category_totals:
    category_totals = filtered_df.groupby(['category', 'Assignment group'])['Number'].count().reset_index(name='Count')


    # Finding aggregates of the Service Group broken SLA Incidents:
    refined_breaches = category_totals[(category_totals['category'] == 'Breach SLA') & (category_totals['Assignment group'])]
    total_breaches = refined_breaches['Count'].sum()
    breaches_matrix = refined_breaches.groupby('Assignment group')['Count'].sum().reset_index()
    breaches_matrix['Percentage']=  round((breaches_matrix['Count']/total_breaches)*100)
 
    # Finding aggregates of the Service Group broken SLA Incidents:
    refined_met = category_totals[(category_totals['category'] == 'Met SLA') & (category_totals['Assignment group'])]
    metsla_matrix = refined_met.groupby('Assignment group')['Count'].sum().reset_index()
    total_met = refined_met['Count'].sum()
    metsla_matrix['Percentage']= round((metsla_matrix['Count']/total_met)*100)
    
    
    # Starting With The Main Board:
    incidents = filtered_df.groupby(['Service offering subcategory'])['Number'].count().reset_index(name='Count')

    incidents['Service offering subcategory'] = incidents['Service offering subcategory'].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
                         
                         
    # Generic interactive dataframe:"              
   # filtered_df = clean_df[clean_df["country"].isin(selected_countries) & (clean_df["Month"].isin(selected_month))& (clean_df["Year"].isin(selected_year))]
    
    #col = st.columns((2, 4.5, 2), gap='medium')
                         
    incidents['Service offering subcategory'] = incidents['Service offering subcategory'].replace('AP Interface', 'AP Interfaces')
    incidents['Service offering subcategory'] = incidents['Service offering subcategory'].replace('AD Sync Errors', 'Application Bug')

    # Getting the Breach Pie Chart in:
    #Create a 3D donut chart
    met = go.Figure(data=[go.Pie(
        labels=metsla_matrix['Assignment group'],
        values=metsla_matrix['Percentage'],
        hole=0.6,  # Makes it a donut chart
        textinfo='percent+label',
        marker=dict(colors=color_theme_list[selected_color_theme][:len(breaches_matrix)]))])
    
    # Add SVG Icon to the center of the donut chart:
    met.update_layout(
        #title_text='IT Service Group Contribution to SLA Breach:',
        images=[dict(
            source=icon_met,
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            sizex=0.6, sizey=0.25,
            xanchor="center", yanchor="middle"
        )], 
        annotations=[dict(
            text='',  # If you want to add any text below the icon
            x=0.6, y=0.56, font_size=20, showarrow=False
        )]
    )
  
    breach = go.Figure(data=[go.Pie(
        labels=breaches_matrix['Assignment group'],
        values=breaches_matrix['Percentage'],
        hole=0.65,  # Makes it a donut chart
        textinfo='percent+label',
        marker=dict(colors=color_theme_list[selected_color_theme][:len(breaches_matrix)]))])
    
    # Add SVG Icon to the center of the donut chart:
    breach.update_layout(
        #title_text='IT Service Group Contribution to SLA Breach:',
        images=[dict(
            source=icon_testing,
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            sizex=0.6, sizey=0.25,
            xanchor="center", yanchor="middle"
        )], 
        annotations=[dict(
            text='',  # If you want to add any text below the icon
            x=0.5, y=0.5, font_size=19, showarrow=False
        )]
    )
    
    # Creating an Interactive Matrix for Donut Chart: 
    def calculate_matrix_perc(filtered_df, selected_months):
        # Check if not months are selected in the sidebar: 
        if not selected_months:
            return {
                'total_count': 0,
                'met_sla_perc': 0,
                'breach_perc':0,
                'met_sla_total': 0,
                'breach_sla_total': 0
            }

        # Filter the DataFrame based on the selected months
        df_filtered = filtered_df[filtered_df['Month'].isin(selected_months)]
    
        # Calculate totals for each SLA category
        met_sla_total = df_filtered[df_filtered['category'] == 'Met SLA'].shape[0]
        breach_sla_total = df_filtered[df_filtered['category'] == 'Breach SLA'].shape[0]
    
        # Handle the case where both SLA and Breach counts are zero
        if met_sla_total == 0 and breach_sla_total == 0:
            matrix_perc = 0

        # Calculate total count of records for the selected months
        total_count = met_sla_total + breach_sla_total

        # Calculate matrix percentage
        if total_count > 0:
            met_sla_perc = round((met_sla_total / total_count) * 100)
            breach_perc= 100 - met_sla_perc
        else:
            met_sla_perc = 0
            breach_perc = 0

        return total_count, met_sla_perc,breach_perc ,met_sla_total, breach_sla_total
    
    # Getting the totals: 
    total_count, met_sla_perc,breach_perc ,met_sla_total, breach_sla_total= calculate_matrix_perc(filtered_df, selected_month)
    
    # creating an interactive Country Log Dataframe to be used for the map: 
    country_log_testing = filtered_df.groupby(['Month', 'country'])['Number'].count().reset_index(name='Incidents Logged')
                         
                         
    #right dataframe to use:
    country_log = country_log_testing.groupby('country')['Incidents Logged'].sum().reset_index()
                         
    def testing_data(filtered_df, selected_month=None, selected_countries=None):   
        # If no countries or months are selected, return a DataFrame with zeros for all countries and months
        if not selected_countries and not selected_month:
            result_df = pd.DataFrame({
                'country': filtered_df['country'].unique(),
                'Month': filtered_df['Month'].unique(), 
                'Incidents Logged': 0
            })
            return result_df,0
    
        # Group by Country and Month and count the incidents
        grouped_df =  filtered_df.groupby(['Month','country'])['Number'].count().reset_index(name='Incidents Logged')
    
        # Identify and add missing countries with zero incidents
        all_combinations = pd.MultiIndex.from_product(
            [selected_month, selected_countries], 
            names=['Month', 'country']
        ).to_frame(index=False)
    
        grouped_df = all_combinations.merge(grouped_df, on=['Month', 'country'], how='left').fillna(0)
    
        # Ensure 'Incidents Logged' is an integer
        grouped_df['Incidents Logged'] = grouped_df['Incidents Logged'].astype(int)
    
        # Adding the total counts for the data
        total_incidents_logged = grouped_df['Incidents Logged'].sum()
    
        return grouped_df, total_incidents_logged
    
    #Getting the group totals
    grouped_df, total_incidents_logged = testing_data(filtered_df, selected_month, selected_countries)
                         
    def prepare_country_data(country_log, selected_countries):
        country_data = pd.DataFrame({
            'country': selected_countries,
            'Incidents Logged': 0
        })
    
        if not country_log.empty:
            country_data = country_data.set_index('country')
            country_log = country_log.set_index('country')
            country_data.update(country_log)
            country_data.reset_index(inplace=True)

        return country_data
                         
    country_log = prepare_country_data(country_log, selected_countries)
                         
    def testing_data(filtered_df,selected_month= None, selected_countries=None):   
        # If no countries are selected, return a DataFrame with zeros for all countries
        if not selected_countries and not selected_month:
            result_df = pd.DataFrame({
                'country': filtered_df['country'].unique(),
                'Month': filtered_df['Month'].unique(), 
                'Incidents Logged': 0
            })
            return result_df, 0
    
    
        # Handle None values
        if selected_countries is None:
            selected_countries = filtered_df['country'].unique()
        if selected_month is None:
            selected_month = filtered_df['Month'].unique()
    
        # Filter the DataFrame based on the selected countries
        testing = filtered_df[filtered_df['country'].isin(selected_countries)]
    
        # Group by Country and sum the incidents
        grouped_df = testing.groupby(['Month','country'])['Number'].count().reset_index(name='Incidents Logged')
    
    
        # Identify and add missing countries with zero incidents
        all_combinations = pd.MultiIndex.from_product(
            [selected_month, selected_countries], 
            names=['Month', 'country']
        ).to_frame(index=False)
    
        grouped_df = all_combinations.merge(grouped_df, on=['Month', 'country'], how='left').fillna(0)
    
        # Adding the total counts for my data: 
        total_incidents_logged = grouped_df['Incidents Logged'].sum()
    
        return grouped_df, total_incidents_logged
    
    grouped_df, total_incidents_logged = testing_data(filtered_df,selected_month ,selected_countries)
                         
    def interactive_bar(data, selected_color_theme):
        chart = (
            alt.Chart(data)
            .mark_bar()
            .encode(
                 y=alt.Y("country:N", title="country"),
                 x=alt.X("Incidents Logged:Q", title="Incidents Logged"),
                 color=alt.Color("Incidents Logged:Q", scale=alt.Scale(range=selected_color_theme)),
                tooltip=["country", "Month", "Incidents Logged"]
            )
            .properties(
                title="Total Incidents Managed by Country per Month"
            )
        )
        return chart   
                
    chart = interactive_bar(grouped_df, color_theme_list[selected_color_theme][:len(grouped_df)])
                         
    #Setting up the environment for the geojson data:
    url = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'
    response = requests.get(url)
    counties = response.json()

    def create_choropleth(country_log, counties, selected_color_theme):
        # Check if there are no countries selected or all selected countries have zero incidents
        if country_log.empty or country_log['Incidents Logged'].sum() == 0:
           # Placeholder DataFrame: Display all countries with zero incidents
           country_log = pd.DataFrame({
               'country': [feature['properties']['name'] for feature in counties['features']],  # Use all countries in the geojson
               'Incidents Logged':  [0] * len(counties['features'])
           })
        
        # Determine the max incidents for setting the color range
        max_incidents = country_log['Incidents Logged'].max()
    
        # Avoid division by zero in color range calculation
        range_color = (0, max_incidents if max_incidents > 0 else 1)

        # Use default color theme if selected_color_theme is not found
        chart_colors = color_theme_list if not selected_color_theme else [color_theme_list['CSBJHB1'], color_theme_list['CSBJHB2']]
    
        # Check if all incident counts are zero
        if country_log['Incidents Logged'].sum() == 0:
            
            # Create a base map with no highlights
            fig = px.choropleth_mapbox(
                country_log,
                geojson=counties,
                locations='country',
                featureidkey="properties.name",
                color_discrete_sequence=['lightgrey'],  # Default color when no incidents
                mapbox_style="carto-positron",
                zoom=3,
                center={"lat": 0, "lon": 20},
                opacity=0.5,
                labels={'Incidents Logged': 'Incidents rate'}
            )
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            return fig
                         
        # Create the choropleth map with incident highlights:
        max_incidents = country_log['Incidents Logged'].max() if not country_log.empty else 1
        fig = px.choropleth_mapbox(
            country_log,
            geojson=counties,
            locations='country',
            featureidkey="properties.name",
            color='Incidents Logged',
            color_continuous_scale=color_theme_list[selected_color_theme][:len(country_log)],
            range_color=(0, country_log['Incidents Logged'].max()),
            mapbox_style="carto-positron",
            zoom=3,
            center={"lat": 0, "lon": 20},
            opacity=0.5,
            labels={'Incidents Logged': 'Incidents rate'}
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    
        return fig
    
    choropleth = create_choropleth(country_log, counties, selected_color_theme)
                         
    # Building the Main Board:          
    filtered_df = clean_df[clean_df["country"].isin(selected_countries) & (clean_df["Month"].isin(selected_month))]
    col = st.columns((2, 4.5, 2), gap='medium')  
                         
    with col[0]:
        st.markdown('##### SLA Compliance Reporting:')
        
        def make_donut(input_response, input_text, selected_color_theme):
            chart_color = color_theme_list.get(selected_color_theme, ['#003044', '#001822'])  # Default if not found##
        
            source = pd.DataFrame({
                "Topic": ['', input_text],
                "% value": [100-input_response, input_response]
            })
            source_bg = pd.DataFrame({
                "Topic": ['', input_text],
                "% value": [100, 0]
            })
            plot = alt.Chart(source).mark_arc(innerRadius=55, cornerRadius=10).encode(
                theta="% value",
                color= alt.Color("Topic:N",
                                 scale=alt.Scale(
                                     domain=[input_text, ''],
                                     range=chart_color),
                                 legend=None),
                ).properties(width=150, height=150)
            text = plot.mark_text(align='center', color="#1f77b4",font="Lato",fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response}%'))
            plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=55, cornerRadius=10).encode(
                theta="% value",
                color= alt.Color("Topic:N",
                          scale=alt.Scale(
                              domain=[input_text, ''],
                              range=chart_color),  # 31333F
                          legend=None),
                ).properties(width=150, height=150)
            return plot_bg + plot + text
    
        # Compliance Reporting: 
        compliance_col = st.columns(2)
        with compliance_col[0]:
            st.write('Met SLA')
            st.altair_chart(make_donut(met_sla_perc, 'Met SLA', selected_color_theme), use_container_width=True)
        with compliance_col[1]:
            st.write('Breach SLA')
            st.altair_chart(make_donut(breach_perc, 'Breach SLA', selected_color_theme), use_container_width=True)
    
        #st.markdown('##### Service Group Breach Contribution')    
        # Show the donut chart:
        #st.plotly_chart(breach, use_container_width=True)
        
        st.markdown('##### Service Group Breach Contribution:')
        
        # Show the donut chart:
        st.plotly_chart(breach, use_container_width=True)
          
    
    with col[1]:
        st.markdown('##### Southern and Eastern African Region Incidemt Management:')
        
        # Interactive Choropleth: 
        st.plotly_chart(choropleth, use_container_width=True)
    
        # Interactive Bar Plot: 
        st.altair_chart(chart, use_container_width=True)    
    
    with col[2]:
        st.markdown('##### Top Service Group Requests')    
    
        # Creating an interactive Dataframe such that my totals are filtered according to the selected month in the Sidebar:
        filtered_df = clean_df[clean_df["country"].isin(selected_countries) & (clean_df["Month"].isin(selected_month))]
        #filter_test = filtered_df[filtered_df["Month"].isin(selected_month)]
        tickets_logged_df = filtered_df.groupby('Assignment group').size().reset_index(name='Incidents')
    
        # creating an interactive Country Log Dataframe to be used for the map: 
        country_log_testing = filtered_df.groupby(['Month', 'country'])['Number'].count().reset_index(name='Incidents Logged')
    
        #Function to generate HTML for progress bar with custom color
        def get_progress_bar_html(value,max_value=None, color='#3e6184'):
            if max_value is None:
                max_value = max(tickets_logged_df['Incidents'])  # Use max incidents from the dataset if not provided
            percentage = (value / max_value) * 100
            return f"""
            <div style="background-color: #f3f3f3; border-radius: 5px; width: 100%; height: 20px; margin: 5px 0;">
               <div style="background-color: {color}; width: {percentage}%; height: 100%; border-radius: 5px;"></div>
            </div>
            """
    
        # Function to create HTML representation of the DataFrame
        def create_html_table(df):
            html = '<table style="width: 100%; border-collapse: collapse;">'
            html += '<thead><tr><th style="padding: 8px; text-align: left;">Assignment Group</th><th style="padding: 8px; text-align: left;">Incidents</th></tr></thead>'
            html += '<tbody>'
            for _, row in df.iterrows():
                html += f'<tr><td style="padding: 8px; border: 1px solid #ddd;">{row["Assignment group"]}</td><td style="padding: 8px; border: 1px solid #ddd;">{get_progress_bar_html(row["Incidents"])}</td></tr>'
            html += '</tbody></table>'
            return html    
        
        # Display the DataFrame with custom progress bar:
        st.markdown(create_html_table(tickets_logged_df), unsafe_allow_html=True)
    
        # Drawing a heatmap for the chats:
        def make_heatmap(data,selected_color_theme):
            heatmap = alt.Chart(data).mark_rect().encode(
                y=alt.Y("Month:O", title="Month"),
                x=alt.X("country:O", title="country"),
                color=alt.Color("Incidents Logged:Q",legend=None,scale=alt.Scale(range=selected_color_theme)),
            ).properties(
                width=900
            ).configure_axis(
                labelFontSize=12,
                titleFontSize=12
            )
            return heatmap
        
        # Plotting a Heatmap:
        heatmap = make_heatmap(country_log_testing, color_theme_list[selected_color_theme])
        # View HeatMap:
        st.altair_chart(heatmap, use_container_width=True)
    
        # About the Board Type of Information: 
        with st.expander('About', expanded=True):
            st.write('''
               - Data Source: [ServiceNow SQL Database](https://www.census.gov/data/datasets/time-series/demo/popest/2010s-state-total.html).
               - :orange[**Compliance**]: Incidents analysis by SLA requirement for selected 2024
               - :orange[**Regional Analyses**]: The total incidents handled for the southern and east african businesses (in hundreds)
               ''')
            
def Information_Portal():
    # Import Libraries: 
    
    import streamlit as st 
    import pandas as pd
   
    st.markdown(
        """
        This section of the Portak illustrates the uniques data types inscripped in the creation of the board. We're generating a bunch of random numbers in a loop for around5 seconds.
        ### Outline of the Dashboard: 
        The dashboard seeks to address and answer the following questions regarding the outlook of our IT Incident Management:

           - What is the Load of work handled by each IT Service Group per Month ?
           - What is the distinct look on our performance viewed through our Service Level Agreements Compliance Framework ?
           - Where does our business require the most help ?
           - Which regions are least serviced by the IT business ?
           - How many Multi-partied incident logs do we get per month?
           - What is the most requested assistance type of incidents by the business?
        ### Aging-Incidents:
           - Which IT Service Group breached the most SLA ?
           - Which type of Incidents breached the SLA request the Most?
           - When does an Request become an Incident ?
           - What is the Impact analysis of Incidents breaching SLA ?
        ### Outlook: 
        Ideally, the look into this is nearly to discourage or encourage unhelpful and non-impactful service but to view the business 
        as a client and to encourage meaningful assistance. Completion of incidents within a.
        ### Metadata:
        """
    )
    df = pd.DataFrame(
        [
            {"Variables": "Number", "Explanation": "Unique incident code ", "Data Type": "string"},
            {"Variables": "Due date", "Explanation": "Incident/Request log date", "Data Type": "datetime"},
            {"Variables": "Short description", "Explanation":  "Reason for ticket logged", "Data Type": "string"},
            {"Variables": "Caller", "Explanation": "End-User who logged the incident", "Data Type":"string"},
            {"Variables": "Priority", "Explanation": "Tiers of incident", "Data Type": "string"},
            {"Variables": "State", "Explanation":  "Incidents Life-Cycle", "Data Type": "string"},
            {"Variables": "Category", "Explanation":  "Service Level Agreement Metric", "Data Type": "string"},
            {"Variables": "Assignment group", "Explanation":  "IT Service Group", "Data Type": "string"},
            {"Variables": "Assigned to", "Explanation":  "IT Personnel", "Data Type": "string"},
            {"Variables": "Updated", "Explanation":  "Date incident was closed ", "Data Type": "string"},
            {"Variables": "Updated", "Explanation":  "Date incident was closed ", "Data Type": "string"},
            {"Variables": "Updated", "Explanation":  "Date incident was closed ", "Data Type": "string"},
            {"Variables": "Updated", "Explanation":  "Date incident was closed ", "Data Type": "datetime"},
        ]
    )
    st.dataframe(df, use_container_width=True)
    
    st.markdown(
        """
        You may be familiar with the phrase “A picture is worth a thousand words” and, in the context of data science, a visualized plot provides just as much value. It does this by providing a different look at tabular data, perhaps in the form of simple line charts, histogram distribution and more elaborate pivot charts.
        As useful as these can be, a typical chart that we may see in print or on the web are most likely static. Imagine how much more engaging it would be to manipulate these static variables in an interactive dashboard? In this portal, we provide you with interactive dashboards intended to provide more meaningful insight of how our IT footprint looks like for our business. Which ideally provide a synopsis of where our business requires the most assistance. Looking at the different structural complexities of how our IT Incident Management process our it is probably wise to confidently raise the fact that there’s a potential 5 to 15% of missing incidents that were probably not logged by end-users. Since, that is the case it will ideally be wise to indicate that is our margin of era for our work. 
        #### You’ll be informed on how to:
        - What are the key metrics-
        - Thoroughly explanation and documentation for the EDA Analysis carried out in the Project 
        - Structural and Architectural design of the data used in the project
        - Different Toolkits involved in the projects
        - Dashboard Configuration
        #### What Is Inside the Dashboards:
        This part of the section in my information portal illustrates the breakdown of the components that make up the architect of the dashboard:
    """)
    # Display image from local file
    # Method 1: Using st.image with a URL
    #os.path.join('Images', 'Architectural Design Map.svg')

    svg_url = os.path.join('Images', 'Architectural Design Map.svg')
    st.image(svg_url, caption='Architectural Data Design for the Dashboard', use_column_width=True)
    st.markdown(
        """
        ##### Steps in the process:
        1. Data Source:
        - Involves the systems and applications where the data collection was done. 
        2. Staging Area:
        - Involves the process of finding the tables to use in the from the data collected, and potentially finding out the valuable variables that could be missing from the data.
        3. ETL Process:
        - This process involves manipulating the current data by extracting, transforming and loading the cleaned data for use in the analysis.
        4. Inisights and Analysis:
        - This process involves showing the meaning information that the data has and telling the story in a way that is easy to be understood by stakeholders.
        The above is a synopsis of the process undergone to get useable and insightful information to present as a dashboard. 
        Now to the interesting part the dashboards.
        ##### Computation of the Dashboards: 
        The most intuitive thing to do when creating a dashboard that would provide information on where our business requires the most help, and additionally which service group is currently contributing the most to the overall incident management. You’ll be required to create an SLA compliance reporting system or metric. To do so, I had to create a variable that is categorical and informs on the Incidents that Met our SLA requirements, that breached and those that were about to do so. Before the breakdown of the computation of the variable it is important to note that SLA compliance was created as a generic metric, which is basically a measure of all incidents that were completed in 3 days excluding the weekends as they are not included in our business working days, and also, we do not have weekend support it would be counter intuitive to ignore that.
        ###### SLA compliance Reporting:
    """)

    image_first =  os.path.join('Images', 'Regional_analysis diagram configuration.png')
    image_second = os.path.join('Images', 'Compliance_architects explaination.png') 
    
    ### Work Accrual Board
    #os.path.join('Images', 'Regional_analysis diagram configuration.png')
    #os.path.join('Images', 'Compliance_architects explaination.png')
    image_a = Image.open(image_first)
    image_b = Image.open(image_second)
    
    ### The first Photo:
    st.image(image_b, caption='SLA Compliance Report by IT Personnel & Incidents Life-cycle', use_column_width=True)
    st.markdown(
        """
        Breakdown of the components in the above dashboard:
        1. Sidebar:
        - It has the IT Personnel & Incidents Life- cycle to filter through the dashboard. 
        2. Dashboard Header:
        - Top 3 Countries with the highest incidents density. 
        3. Column 1:
        - Consists of the Donut Chart illustrating the overall incidents by their status. 
        - Secondly, it shows the IT Personnel with the highest contribution to the reduction of IT's Workload. 
        - Lastly, it shows the Service Group with the highest number of incidents handled. 
        4. Column 2:
        - SLA Compliance report by the IT Personnel categorised with the Incidents that Met, are within, and breached our compliance requirement.
        - Secondly, it shows the Workload Accrual chart that shows the YTD incidents that have been resolved over the once that are current On-Hold, In Progess, and Active in our Agent View. 
        5. Column 3:
        - Shows the key metrics for the dashboard iterable and filtereable by IT Personnel & Incidents Life Cycle.  
        ###### Regional IT Incident Management Analysis:
        The below chart dashboard shows a synopsis of IT's Footprint:
    """)
    #The Second Photo:
    st.image(image_a, caption='Southern and Eastern African region IT Incident Management Analysis', use_column_width=True)

    st.markdown(
        """
        The above dashboard shows:
        1. Sidebar: 
        - It has the Months, Countries and Customized Color themes that incorporate C.Steinweg Bridge colors. 
        2. Column 1:
        - Overall IT SLA Compliance Chart
        - Secondly, The contribution of each service group to the overall SLA breach. 
        3. Column 2:
        - Choropleth map that shows our IT reach and employee service in the Eastern and Southern African region. 
        - Secondly, it shows total incidents received by each of our subsidiary companies. 
        4. Column 3:
        - Service Groups with the outter most request. 
        - Heatmap showing the regency and density of incidents managed for each country. 
        - Thirdly, We have an expander giving a synopsis on the metrics used to gather the data, and its intended end use.
        #### Toolkit and Methodology Engaged:
        It is important to mentioning the multiple sources used in gearing up the project to where it is now a portal. Furthermore, to mention some of the key problems encountered in the process of creating the boards. 
        The programing language used in the project is primarily python housed by Anaconda/Jupyter Notebook. Objectively, borrowed from the open libraries such as streamlit, pandas, numpy, string plotly express and grapth objects, folium, base64 and etc. Notable mention also goes to OpenAI, Stack Overflow and Streamlit open source documentation. 
        Additionally I would also thank the various inputs and consultations provided by Rea, Calin and Dexter for better representation of the dashboard and providing me with end-user insights on what would be key and valuable insights the boards to aim to provide.  
        #### Conlcution:
        I would like to Appreciate myself for starting the project at leisure for me to better my python skills and to show case my potential of ideally being a great data scientist.
        ###### BYE SteinVEEZ.
    """)
    
def SteinTech():
    # Import Libraries: 
    import streamlit as st 
    import pandas as pd

    # Using Markdown for Cool things: 
    st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")
    st.markdown(
        """
        SteinTech this Week Find the Cool things to do in with SteinTech.......
    """
    )

    

home_path = os.path.join('Images', 'home_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.png')
analysis_path= os.path.join('Images', 'public_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.png')
complianc_path= os.path.join('Images', 'bar_chart_4_bars_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.png')
info_path= os.path.join('Images', 'architecture_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.png')
SteinTecho_path= os.path.join('Images', 'bubble_chart_48dp_3E6184_FILL0_wght400_GRAD0_opsz48.png')

home_icon = get_resized_icon(home_path,50)
analysis_icon = get_resized_icon(analysis_path,50)
compliance_icon = get_resized_icon(complianc_path,50)
info_icon = get_resized_icon(info_path,50)
SteinTech_icon = get_resized_icon(SteinTecho_path,50)

# Creating a pages matrix: 
#page_names_to_funcs = {
 #  "Home": intro,
  # "Architectural Design Information": Information_Portal, 
 #  "Regional Analysis": ITSM_Incident_Portal,
 #  "SLA Compliance Reporting": Testing_Thoughts,
#    "SteinTech": SteinTech
#}

icons = {
    "Home": home_icon,
    "Architectural Design Information": info_icon,
    "Regional Analysis": analysis_icon,
    "SLA Compliance Reporting": compliance_icon,
    "SteinTech": SteinTech_icon  
}

#CSS for custom sidebar
st.markdown("""
    <style>
    .icon-text {
        display: flex;
        align-items: center;
        padding: 10px;
        cursor: pointer;
        border-radius: 5px;
        margin-bottom: 10px;
        color: black;
    }
    .icon-text:hover {
        background-color: #f0f0f0;
    }
    .icon-text img {
        margin-right: 10px;
    }
    .icon-text span {
        font-size: 16px;
        color: black; 
    </style>
    """, unsafe_allow_html=True)


# Initialize session state if not set
if 'page' not in st.session_state:
    st.session_state.page = "Home"
    
# Initialize session state if not set
if 'Architectural Design Information' in st.session_state:
    st.session_state.page = "Architectural Design Information"
# Initialize session state if not set
if 'Regional Analysis' in st.session_state:
    st.session_state.page = "Regional Analysis"
# Initialize session state if not set
if 'SLA Compliance Reporting' in st.session_state:
    st.session_state.page = "SLA Compliance Reporting"
    
# Initialize session state if not set
if 'SteinTech' in st.session_state:
    st.session_state.page = "SteinTech"    

# Function to create sidebar item
def sidebar_item(page_name,icon):
    st.sidebar.markdown(
        f"""
        <a href="/?page={page_name}" style="text-decoration: none;">
        <div class="icon-text">
            <img src="data:image/png;base64,{icon}">
            <span>{page_name}</span>
        </div>
        </a>
        """,
        unsafe_allow_html=True
    )
    
def main_sidebar():
    sidebar_item("Home", home_icon)
    sidebar_item("Architectural Design Information", info_icon)
    sidebar_item("Regional Analysis",analysis_icon)
    sidebar_item("SLA Compliance Reporting",compliance_icon)
    sidebar_item("SteinTech",SteinTech_icon)
    
    
# Display the main sidebar
main_sidebar()

#warnings.filterwarnings("ignore", category=FutureWarning, module="streamlit")
query_params = st.experimental_get_query_params()
#showWarningOnDirectExecution = False
page = query_params.get("page", ["Home"])[0]

# Display the selected pag
if page == "Home":
    intro()
if page == "Architectural Design Information":
    Information_Portal()
if page == "Regional Analysis":
    ITSM_Incident_Portal()
if page == "SLA Compliance Reporting":
    Testing_Thoughts()
if page == "SteinTech":
    SteinTech()


# # Injecting custom CSS for the sidebar
# st.markdown("""
#     <style>
#     /* Sidebar background */
#     [data-testid="stSidebar"] {
#         background-color: #f0f0f5;
#         border-right: 2px solid #e6e6ff;
#     }
# 
#     /* Menu header styling */
#     [data-testid="stSidebar"] h3 {
#         color: #4e73df;
#         font-family: 'Arial';
#         font-weight: bold;
#         font-size: 24px;
#     }
# 
#     /* Menu options styling */
#     [data-testid="stSidebar"] label {
#         color: #3e6184;
#         font-family: 'Helvetica';
#         font-weight: 500;
#         font-size: 18px;
#     }
# 
#     /* Selected radio button styling */
#     [data-testid="stSidebar"] .stRadio div[role='radiogroup'] label {
#         background-color: #4e73df;
#         border-radius: 5px;
#         padding: 5px;
#         color: white;
#     }
# 
#     /* Hover effect for radio options */
#     [data-testid="stSidebar"] .stRadio div[role='radiogroup'] label:hover {
#         background-color: #3e6184;
#         color: #fff;
#     }  
# 
#     </style>
#     """, unsafe_allow_html=True)
# 
# with st.sidebar:
#     selected_page = st.radio(
#         "MENU", 
#         ["Home", "Architectural Design Information","Regional Analysis", "SLA Compliance Reporting", "SteinTech"])
#     
# if selected_page == "Home":
#     intro()
# if selected_page == "Architectural Design Information":
#     Information_Portal()
# if selected_page == "Regional Analysis":
#     ITSM_Incident_Portal()
# if selected_page == "SLA Compliance Reporting":
#     Testing_Thoughts()
# if selected_page == "SteinTech":
#     SteinTech()

# #CSS for custom sidebar
# st.markdown("""
#     <style>
#     .icon-text {
#         display: flex;
#         align-items: center;
#         padding: 10px;
#         cursor: pointer;
#         border-radius: 5px;
#         margin-bottom: 10px;
#         color: black;
#     }
#     .icon-text:hover {
#         background-color: #f0f0f0;
#     }
#     .icon-text img {
#         margin-right: 10px;
#     }
#     .icon-text span {
#         font-size: 16px;
#         color: black; 
#     </style>
#     """, unsafe_allow_html=True)
# 
# 
# # Initialize session state if not set
# if 'page' not in st.session_state:
#     st.session_state.page = "Home"
#     
# # Initialize session state if not set
# if 'Architectural Design Information' in st.session_state:
#     st.session_state.page = "Architectural Design Information"
# # Initialize session state if not set
# if 'Regional Analysis' in st.session_state:
#     st.session_state.page = "Regional Analysis"
# # Initialize session state if not set
# if 'SLA Compliance Reporting' in st.session_state:
#     st.session_state.page = "SLA Compliance Reporting"
#     
# # Initialize session state if not set
# if 'SteinTech' in st.session_state:
#     st.session_state.page = "SteinTech"    
# 
# # Function to create sidebar item
# def sidebar_item(page_name,icon):
#     st.sidebar.markdown(
#         f"""
#         <a href="/?page={page_name}" style="text-decoration: none;">
#         <div class="icon-text">
#             <img src="data:image/png;base64,{icon}">
#             <span>{page_name}</span>
#         </div>
#         </a>
#         """,
#         unsafe_allow_html=True
#     )
#     
# def main_sidebar():
#     sidebar_item("Home", home_icon)
#     sidebar_item("Architectural Design Information", info_icon)
#     sidebar_item("Regional Analysis",analysis_icon)
#     sidebar_item("SLA Compliance Reporting",compliance_icon)
#     sidebar_item("SteinTech",SteinTech_icon)
#     
#     
# # Display the main sidebar
# main_sidebar()
# 
# # Handle page navigation
# 
# #warnings.filterwarnings("ignore", category=FutureWarning, module="streamlit")
# query_params = st.experimental_get_query_params()
# #showWarningOnDirectExecution = False
# page = query_params.get("page", ["Home"])[0]
# 
# # Display the selected page
# if page in page_names_to_funcs:
#     if page == "Home":
#         intro()
#     elif page == "Architectural Design Information":
#         Information_Portal()
#     elif page == "Regional Analysis":
#         ITSM_Incident_Portal()
#     elif page == "SLA Compliance Reporting":
#         Testing_Thoughts()
#     elif page == "SteinTech":
#         SteinTech()
#     else:
#         page_names_to_funcs[page]()
# else:
#     intro()

# import streamlit as st
# import base64
# 
# # Sample function to encode an image as base64
# def load_icon(file_path):
#     with open(file_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     return encoded_string
# 
# # Sidebar item with icon
# def sidebar_item(page_name, icon):
#     selected = st.session_state.get('selected_page', 'Home')
#     
#     # Determine if this is the selected page
#     if page_name == selected:
#         background_color = "#f39c12"
#         font_weight = "bold"
#     else:
#         background_color = "transparent"
#         font_weight = "normal"
#         
#     st.sidebar.markdown(
#         f"""
#         <div style="display: flex; align-items: center; background-color: {background_color}; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
#             <img src="data:image/png;base64,{icon}" width="30" style="margin-right: 10px;">
#             <a href="#" style="text-decoration: none; color: black; font-weight: {font_weight};">{page_name}</a>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# 
# # Define a list of page names and icons
# pages = [
#     {"name": "Home", "icon": load_icon("path_to_home_icon.png")},
#     {"name": "Architectural Design Information", "icon": load_icon("path_to_architecture_icon.png")},
#     {"name": "Regional Analysis", "icon": load_icon("path_to_analysis_icon.png")},
#     {"name": "SLA Compliance Reporting", "icon": load_icon("path_to_sla_icon.png")},
#     {"name": "SteinTech", "icon": load_icon("path_to_steintech_icon.png")},
# ]
# 
# # Sidebar navigation
# for page in pages:
#     sidebar_item(page["name"], page["icon"])
# 
# # Track selected page using session state
# if "selected_page" not in st.session_state:
#     st.session_state["selected_page"] = "Home"
# 
# # Content based on selected page
# st.write(f"Selected page: {st.session_state['selected_page']}")
# 
# # Handle page selection logic (mimicking radio behavior)
# for page in pages:
#     if st.sidebar.button(f"Go to {page['name']}"):
#         st.session_state["selected_page"] = page["name"]
# 

# In[ ]:




