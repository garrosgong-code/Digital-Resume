import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Zhiyu (Garros) Gong, M.Sc.
##### *Financial Analytics Professional | Business Scientist | Ph.D.Candidate | CFA Level II Candidate* 
''')

image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Financial/Investment Analyst, Researcher and Analytics Consultant with exceptional research and analytical abilities in a data-oriented environment and a passion for decision sciences. 
- Strong English communication and writing skills as demonstrated by extensive leadership experience in many automation and analytical tools development projects. 
- Strong track record in prior academic experience with high distinct GPA and scholarship awards.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/garros-gong/" target="_blank">Garros Gong</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#my-projects">My Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#my-writing-samples">My Writing Samples</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      <li class="nav-item">
        <a class="nav-link" href="#contact-me">Contact Me</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## My Projects
''')
txt4('ESG AI Analysis(NLP)', 'A sample project that deploys cutting-edge NLP techniques to analyze a company ESG performance.', 'https://esg-ai-investment.streamlit.app/')
st.markdown("![Alt Text](https://media.giphy.com/media/0Q5hrVPpIy6g2MOTke/giphy.gif)")
txt4('Options Trading Analytical Platform', 'An interactive application for comparing various option chains and calculating the value of calls/puts using Black Scholes.', 'https://option.streamlit.app/')
st.markdown("![Alt Text](https://media.giphy.com/media/S2DQFsrHuMhv3oMRYP/giphy.gif)")
txt4('Stock Price Prediction(Deep Learning)', 'An interactive application allows users to predict closing stock prices using Deep Learning models.', 'https://stock-price-dp.streamlit.app/')
st.markdown("![Alt Text](https://media.giphy.com/media/BGhC5HYDEa7D3NXTgi/giphy.gif)")
txt4('Credit Card Fraud Detection', 'An End-to-end Machine Learning Project using classification algorithms and techniques to accurately detect if a credit card transaction is fraudulent or not.', 'https://fraud-detection.streamlit.app/')
st.markdown("![Alt Text](https://media.giphy.com/media/IIDPJbt33hOxiAOjig/giphy.gif)")
txt4('Sales Data Prediction', 'This app is a demonstration of how data solutions like data analysis and prediction can be made user-friendly.', 'https://sales-data.streamlit.app/')
st.markdown("![Alt Text](https://media.giphy.com/media/c6FG1WLvyDsH93twiT/giphy.gif)")
txt4('Bank Data Dashboard', 'This project envisions running an exploratory data analysis on the dataset and then building a web page to display all the results and relevant information about the bank clients.', 'https://banking-data.streamlit.app/')
st.markdown("![Alt Text](https://media.giphy.com/media/ay9xj4ea8Jk8Upz8uV/giphy.gif)")

#####################

#####################
st.markdown('''
## My Writing Samples
''')
txt4('TELUS Annual Credit Review (2021)','An In-Depth Financial Analysis Report Sample','https://clippingsme-assets-1.s3.amazonaws.com/cuttingpdfs/1607787/eda7ec83ad88a117e2ec7a37dbfd7ad7.pdf?')
txt4('Case Study: Natural Gas and Its Role in The New Energy Dynamics','A Case Analysis Sample','https://clippingsme-assets-1.s3.amazonaws.com/cuttingpdfs/1607761/1817ac66e1d8af68b4e1f8736a89ebee.pdf?')
txt4('Understanding Provincial Greenhouse Gas Emission Reporting in Canada','An ESG-Related Analysis Sample','https://clippingsme-assets-1.s3.amazonaws.com/cuttingpdfs/1610954/51508621e41fa9dabeb11ce46b31dbf6.pdf?')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `MATLAB`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`,`Power BI`,`Tableau`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`, `Pytorch`')
txt3('Model Deployment', '`streamlit`, `gradio`, `R Shiny`, `Python DASH`')

#####################
st.markdown('''
## Education
''')

txt('**Doctor of Philosophy** Management Sciences: Applied Operational Research, *University of Waterloo*, Canada',
'2021-Present')
st.markdown('''
- GPA: `4.0/4.0`
- Status: `Part-time basis (open to full-time job opportunities)`
- Research Areas `Financial Analytics`, `Social Media Analytics`, `Sustainability Analytics`.
- Supervisory: Supervised by `Dr. Stan Dimitrov`
''')

txt('**Master of Science** Management Science: Business Analytics, *Western University*, Canada',
'2017-2018')
st.markdown('''
- GPA: `3.8/4.0`
- Accomplishments: `Richard Ivey MSc Excellence Award for Academic Excellence and International Leadership`
''')

txt('**Bachelors of Science** Financial Mathematics and Economics, *University of Victoria*, Canada',
'2013-2016')
st.markdown('''
- GPA: `8.0/9.0`
- Accomplishments: `Harold G. Craven Scholarship`, `Jamie Cassels Undergraduate Research Awards`
- Graduated with High Distinction.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Credit and Financial Analyst**, Central 1 Credit Union (Contract Full-time), Canada',
'2022-Present')

txt('**Adjunct Professor**, Centennial College (Contract Part-time), Canada',
'Summer 2022')

txt('**Associate, Middle Office Operations**, Marret Asset Management Inc. (Permanent Full-time), Canada',
'2020-2021')

txt('**Corporate Financial Analyst**, Vinzan International (Permanent Full-time), Canada',
'2018-2020')

txt('**Ptivate Equity Analyst**, Adelaide Capital Investments (Contract Full-time), Canada',
'Summer 2018')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/garros-gong/')
txt2('GitHub', 'https://github.com/garroshub')

#####################
st.markdown('''
## Contact Me
''')

st.header(":mailbox: Contact Me!")


contact_form = """
<form action="https://formsubmit.co/kuyigougou@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)