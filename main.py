import numpy as np
import pandas as pd
import streamlit as st
import helper,text
import plotly.express as px
import plotly.figure_factory as ff


df=pd.read_csv('Placements.csv')

companies=df['Company'].dropna().unique()
profiles=df['Profile'].dropna().unique()
courses=df['Course'].unique()
types=df['Type'].unique()
sectors=[
    'IT',
    'Analytics/Consulting',
    'Finance',
    'Core',
    'PSU',
    'Banking',
    'Telecom',
    'Healthcare',
    'Others'
]



st.sidebar.title('ISM Placement Analysis')
st.sidebar.image('https://imgs.search.brave.com/APJWWjZS78MsmlvLbQJzNT645Bl9zq14gzrDiuEdQ_Q/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9k/L2QxL0hlcml0YWdl/X0J1aWxkaW5nX2F0/X0lJVF9EaGFuYmFk/XzEuanBn')
ch=st.sidebar.radio('',['Overview','Course-wise Analysis','Branch-wise Analysis','Company-wise Analysis','Sector-wise Analysis'])

if ch=='Overview':
    st.title('Top Stats')

    c1,c2,c3=st.columns(3)

    with c1:
        st.title(f'{df['CTC'].max():.0f} lpa')
        st.header('Highest CTC')
    with c2:
        st.title(f'{df['CTC'].median():.0f} lpa')
        st.header('Median CTC')
    with c3:
        st.title(f'{len(companies)}+')
        st.header('Companies')


    c1,c2,c3=st.columns(3)

    with c1:
        st.title(f'{len(profiles)}+')
        st.header('Job Roles')
    with c2:
        st.title(f'{df.groupby('Type')['Discipline'].count()['On-Campus']}+')
        st.header('On Campus')
    with c3:
        st.title(f'{df.groupby('Type')['Discipline'].count()['PPO']}+')
        st.header('PPO')
    st.markdown("---")
   
    st.title("Placements by Degree-Program")
    fig=helper.pie_chart(df,'Course')
    fig.update_layout(template='plotly_white')
    st.plotly_chart(fig)
    st.markdown("---")

    st.title("Placements by Type")
    fig=helper.pie_chart(df,'Type')
    fig.update_layout(template='plotly_white')
    st.plotly_chart(fig)
    st.markdown("---")

    st.title("Top Companies in Campus")
    st.table(text.top())
    st.markdown("---")

    st.title("Job Role Distribution")
    fig=helper.pie_chart(df.dropna(subset=['Profile']),'Profile')
    st.plotly_chart(fig)
    st.markdown("---")

    st.title("Sector-wise Distribution")
    l=[len(text.tech),len(text.analytics),len(text.finance),len(text.core_eng),len(text.psu),len(text.banking),len(text.telecom),len(text.health),len(text.others)]
    temp_df=pd.DataFrame(
        {
            'Sector':sectors,
            'No. of Companies':l
        }
    )
    fig=px.pie(temp_df,names='Sector',values='No. of Companies',hole=0.9,template='plotly_white')
    st.plotly_chart(fig)
    st.markdown("---")

if ch=='Course-wise Analysis':
    course=st.sidebar.selectbox('Select a Course',courses)
    st.title(course)
    st.markdown("---")

    highest=df.query('Course==@course')['CTC'].max()
    median=df.query('Course==@course')['CTC'].median()
    mean=df.query('Course==@course')['CTC'].mean()

    st.title('Top Stats')
    col=st.columns([1,1,1])
    col[0].title(f'{highest} lpa')
    col[0].subheader('Highest CTC')
    col[1].title(f'{median:0.1f} lpa')
    col[1].subheader('Median CTC')
    col[2].title(f'{mean:0.1f} lpa')
    col[2].subheader('Mean CTC')
    st.markdown("---")

    st.title('Distribution of Students across Disciplines')
    fig=helper.bar_chart(df,course,'Discipline')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('CGPA Distribution')
    fig=ff.create_distplot([df.query('Course==@course')['CGPA']],['CGPA'],show_rug=False,show_hist=True,colors=['purple'])
    fig.update_layout(xaxis_title='CGPA')
    st.plotly_chart(fig)
    st.markdown('---')
    

    st.title('Distribution of Students across Companies')
    fig=helper.bar_chart(df,course,'Company')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('Top Recruiters')
    r=df.query('Course==@course').groupby('Company').agg({'Discipline':'count','CTC':['median','mean']}).reset_index()
    r.columns=['Company','Recruits','Median CTC','Mean CTC']
    r.sort_values('Recruits',ascending=False,inplace=True)
    top_recruiters=r.head(10)
    fig=px.pie(top_recruiters,names='Company',values='Recruits',hover_data={'Median CTC':':0.1f'},hole=0.9,template='plotly_white')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('High-Pay Recruiters')
    r.sort_values('Median CTC',ascending=False,inplace=True)
    high_pay_recruiters=r.head(10)
    fig=px.pie(high_pay_recruiters,names='Company',values='Median CTC',hover_data={'Recruits':True},hole=0.9,template='plotly_white')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('CTC Distribution')
    fig=ff.create_distplot([df.query('Course==@course')['CTC'].dropna()],['CTC in lpa'],show_rug=False,show_hist=True,colors=['purple'])
    fig.update_layout(xaxis_title='CTC')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('Popular Job Roles')
    st.write('(*Job Roles of many were not available)')
    r=df.query('Course==@course').dropna().groupby('Profile').size().sort_values(ascending=False).reset_index()
    r.columns=['Profile','Recruits']
    fig=px.pie(r.head(),names='Profile',values='Recruits',hole=0.9,template='plotly_white')
    st.plotly_chart(fig)
    st.markdown('---')
    
if ch=='Branch-wise Analysis':
    branches=df['Discipline'].unique()
    branch=st.sidebar.selectbox("Select Branch",branches)
    st.title(branch)
    st.markdown("---")
    ndf=df.query('Discipline==@branch')
    highest=ndf['CTC'].max()
    median=ndf['CTC'].median()
    mean_gpa=ndf['CGPA'].mean()

    st.title("Top Stats")
    col=st.columns([1,1,1])
    col[0].title(f'{highest} lpa')
    col[0].subheader('Highest CTC')
    col[1].title(f'{median:0.1f} lpa')
    col[1].subheader('Median CTC')
    col[2].title(f'{mean_gpa:0.2f}')
    col[2].subheader('Mean CGPA')
    st.markdown("---")

    st.title('CGPA Distribution')
    fig_a=ff.create_distplot([ndf['CGPA']],['CGPA'],show_hist=False,show_rug=False,colors=['crimson'])
    fig_b=px.histogram(ndf,x='CGPA',nbins=5)
    fig_b.update_traces(marker_color='crimson',marker_line_color='white',marker_line_width=1)
    col=st.columns([1,1])
    col[0].plotly_chart(fig_a)
    col[1].plotly_chart(fig_b)
    st.markdown("---")

    st.title('CTC Distribution')
    fig_a=ff.create_distplot([ndf['CTC']],['CTC'],show_hist=False,show_rug=False,colors=['crimson'])
    fig_b=px.histogram(ndf,x='CTC',nbins=10)
    fig_b.update_traces(marker_color='crimson',marker_line_color='white',marker_line_width=1)
    col=st.columns([1,1])
    col[0].plotly_chart(fig_a)
    col[1].plotly_chart(fig_b)
    st.markdown("---")

    st.title('Distribution based on Placement-type')
    fig=helper.pie_chart(ndf,'Type')
    st.plotly_chart(fig)
    st.markdown("---")

    st.title(f'Companies hiring {branch} Branch Students')
    col=st.columns([1,1,1])
    sorter=col[2].selectbox('Sort by :',['Recruits','Median CTC','Mean CTC'])
    ascend=col[2].toggle('Ascending')
    r=ndf.groupby('Company').agg({'Discipline':'count','CTC':['median','mean']}).reset_index()
    r.columns=['Company','Recruits','Median CTC','Mean CTC']
    r['Median CTC']=r['Median CTC'].round(1)
    r['Mean CTC']=r['Mean CTC'].round(1)
    r.sort_values(sorter,ascending=ascend,inplace=True)
    r.reset_index(inplace=True,drop=True)
    st.dataframe(r)
    st.markdown("---")

    st.title('Popular Job Roles')
    fig=helper.pie_chart(ndf,'Profile')
    st.plotly_chart(fig)
    st.markdown("---")

    col=st.columns([1,1])
    col[0].title('Top Hirers')
    col[1].title('High CTC Hirers')
    fig=px.bar(r.sort_values('Recruits',ascending=False).head(),y='Recruits',x='Company',color='Company')
    col[0].plotly_chart(fig)
    fig=px.bar(r.sort_values('Median CTC',ascending=False).head(),y='Median CTC',x='Company',color='Company')
    col[1].plotly_chart(fig)

if ch=='Company-wise Analysis':
    companies=list(companies)
    companies.sort()
    company=st.sidebar.selectbox('Select Company',companies)
    ndf=df.query('Company==@company')
    st.title(company)
    st.markdown('---')
    
    st.title('Top Stats')
    highest=ndf['CTC'].max()
    median=ndf['CTC'].median()
    lowest=ndf['CTC'].min()
    col=st.columns([1,1,1])
    col[0].title(f'{highest} lpa')
    col[0].header('Highest CTC')
    col[1].title(f'{median} lpa')
    col[1].header('Median CTC')
    col[2].title(f'{lowest} lpa')
    col[2].header('Lowest CTC')
    st.markdown('---')

    st.title('Course-wise Distribution')
    fig=helper.pie_chart(ndf,'Course')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('Branch-wise Distribution')
    fig=helper.bar_chart_for_anything(ndf,'Discipline')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('CGPA Distribution')
    fig=px.histogram(ndf,x='CGPA',nbins=10,color='Discipline',template='plotly_white')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('Hired Roles')
    roles=ndf['Profile'].dropna().unique()
    if roles.size==0:
        st.subheader('Sorry...Info not available...!')
    else:
        st.table(roles)
    st.markdown('---')

    st.title("Offer Type Breakdown")
    fig=helper.pie_chart(ndf,'Type')
    st.plotly_chart(fig)
    st.markdown('---')

    st.title('CTC Distribution')
    grp=ndf.groupby(['Discipline','Type'])['CTC'].median().reset_index()
    grp.rename(columns={'CTC':'Median CTC'},inplace=True)
    fig=px.bar(grp,x='Discipline',y='Median CTC',color='Type',template='plotly_white') 
    st.plotly_chart(fig)
    st.markdown('---')

if ch=='Sector-wise Analysis':
    sector=st.sidebar.selectbox('Select Sector',sectors)
    ndf=df[df['Company'].isin(text.passer(sector))]
    st.title(f'{sector} Sector')
    st.markdown('---')

    st.title('Top Stats')
    highest=ndf['CTC'].max()
    median=ndf['CTC'].median()
    lowest=ndf['CTC'].min()
    col=st.columns([1,1,1])
    col[0].title(f'{highest} lpa')
    col[0].header('Highest CTC')
    col[1].title(f'{median} lpa')
    col[1].header('Median CTC')
    col[2].title(f'{lowest} lpa')
    col[2].header('Lowest CTC')
    st.markdown('---')

    st.title('Placement Type Breakdown')
    fig=helper.pie_chart(ndf,'Type')
    st.plotly_chart(fig)
    st.markdown('---')


    st.title('Companies offering PPO')
    ppo=ndf.query('Type=="PPO"').groupby('Company').agg({'Discipline':'count','CTC':'median'}).sort_values('Discipline',ascending=False).reset_index()
    ppo.columns=['Company','Recruit','Median CTC']
    ppo['Median CTC']=ppo['Median CTC'].round(1)
    st.dataframe(ppo)
    st.markdown('---')

    st.title('Branches Hired')
    branch=ndf.groupby('Discipline').size().sort_values(ascending=False).reset_index()
    branch.columns=['Branch','Recruit']
    fig=px.bar(branch,x='Branch',y='Recruit',color='Branch')
    col=st.columns([1,1])
    st.plotly_chart(fig)
    st.title('Top Branches')
    st.table(branch.head())
    st.markdown('---')

    st.title('Job Roles in Hire')
    job_roles=ndf['Profile'].dropna().unique()
    st.table(job_roles)
    st.markdown('---')

    st.title(f'Companies in {sector} Sector')
    col=st.columns([1,1,1])
    sorter=col[2].selectbox('Sort by :',['Recruits','Median CTC','Mean CTC'])
    ascend=col[2].toggle('Ascending')
    r=ndf.groupby('Company').agg({'Discipline':'count','CTC':['median','mean']}).reset_index()
    r.columns=['Company','Recruits','Median CTC','Mean CTC']
    r.sort_values(sorter,ascending=ascend,inplace=True)
    r.reset_index(inplace=True,drop=True)
    r['Median CTC']=r['Median CTC'].round(1)
    r['Mean CTC']=r['Mean CTC'].round(1)
    st.dataframe(r)
    st.markdown("---")
    
    


    





    


    



