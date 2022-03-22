#PYTHON code 
#FILE NAME : run.py
#DESCRIPTION :  Flask , Insatgram Project
#Required libs  : requests, uuid , json ,user_agent 
#* : Telegram : [@Akil828 - @ffffffm] , Github : AKILXXX
#2022/3/20

from flask import Flask, redirect, url_for, request,render_template 
import akil

akilXxX = Flask(__name__)

@akilXxX.route('/home',methods = ['POST', 'GET'])
@akilXxX.route('/',methods = ['POST', 'GET'])
def i():
	return render_template('m.html')


@akilXxX.route('/result',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['username']
      pasw = request.form['password']
   else:
      user = request.form['username']
      pasw = request.form['password']
      
   akilreq = akil.InstaGramLogin(user,pasw)
   if akilreq['X'] == 1: return render_template('akil.html', user = user , sis = akilreq['SES'] , pk = akilreq['pk'] , akilres = akilreq['X'] , error = akilreq['sSs'])
   else : return render_template('akil.html',  akilres = akilreq['X'] , error = akilreq['sSs'] )
	

if __name__ == '__main__':
   akilXxX.run(debug = True)
