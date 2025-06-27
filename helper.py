import plotly.express as px
import streamlit as st


def pie_chart(df,field):
    r=df.groupby(field).size().reset_index()
    r.columns=[field,'Recruits']
    fig=px.pie(r,names=field,values='Recruits',hole=0.9,template='plotly_white')
    return fig

def bar_chart(df,ch,field):
    r=df.query('Course==@ch').groupby(field).size().reset_index()
    r.columns=[field,'No. of Students']
    fig=px.bar(r,x=field,y='No. of Students',template='plotly_white')
    return fig

def bar_chart_for_anything(df,field):
    r=df.groupby(field).size().reset_index()
    r.columns=[field,'Recruits']
    fig=px.bar(r,x=field,y='Recruits',template='plotly_white',color=field)
    return fig


