from bs4 import BeautifulSoup
import requests
import pandas as pd

html_page=requests.get("https://itc.gymkhana.iitb.ac.in/wncc/soc/")
soup=BeautifulSoup(html_page.content,'lxml')
tags=soup.find_all('div',class_='rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white')

project_names = []
project_links = []

for tag in tags:
    project_name=tag.p
    project_link=tag.a['href']
    project_link="https://itc.gymkhana.iitb.ac.in" + project_link
    project_names.append(project_name.text)
    project_links.append(project_link)
    
df = pd.DataFrame({
    'Project Name': project_names,
    'Project Link': project_links
})

# Step 4: Store the DataFrame in a file (CSV for example)
df.to_csv('sos_projects.csv', index=False)

print(df)


