# -*- coding: utf-8 -*-

from flask import Flask, session, redirect, url_for, escape, request, render_template
import time
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/myquery", methods=['GET', 'POST'])
def onMessage():
    myrequest = request.args.get('q')
    print(myrequest)
    
    
    data = '"query":"{}"'.format(myrequest)
    data = '{' + data + '}'
    response = requests.post('http://localhost:5005/conversations/default/respond', data=data)
    json_response = response.json()
    if len(json_response):
      myresponse = (json_response[0]['text'])
      print(myresponse)
      return myresponse
    else:
      return "no response"