from flask import Flask, redirect,render_template,url_for,request,session
   


# run file in __main__
app = Flask(__name__) 


# key untuk session 
app.secret_key = '123'


# tampilan utama 
@app.route('/')
def index():
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Welcome</title>
            <link rel="stylesheet" href="static/css/index-rute/index_rute.css">
        </head>
        <body>
            <div>
                <h1>Calculator Flask</h1>
            </div>  

            <div class="card">
                <div class="content">
                    <main>
                        <nav>
                            <ul>    
                                <li>
                                    <a href="{url_for('index2')}">Input</a>    
                                </li>
                            </ul>          
                        </nav>  
                    </main>
                </div>

                <div class="content">
                    
                </div>
            </div>
        </body>
    </html>
    """



# tampilan hitung 
@app.route('/hitung',methods = ['GET','POST'])
def index2():
    if request.method =='POST':
        angka1 = session['a1'] = request.form['a1'] 
        angka2 = session['a1'] = request.form['a2'] 
        operator = session['op'] = request.form['op']

        
        
        # python version
        # bagian tambah + 
        if operator =='+':
            hasil = angka1 + angka2
            return render_template('hasiltambah/hasiltmbah.html',angka1=angka1,angka2=angka2,hasil=hasil,operator=operator)
        # bagian kurang - 
        #elif operator =='-':
            #hasil = angka1 - angka2
            #return render_template('hasilkurang/hasilkurang.html',angka1=angka1,angka2=angka2,hasil=hasil,operator=operator)
        #elif operator == "x":
            #hasil = angka1 * angka2
            #return render_template('hasilkali/hasilkali.html',angka1=angka1,angka2=angka2,hasil=hasil,operator=operator)
        #elif operator == "/":   
            #hasil = angka1 / angka2 
            #return render_template('hasilbagi/hasilbagi.html',angka1=angka1,angka2=angka2,hasil=hasil,operator=operator)
        #else:
            #return redirect(url_for('massage'))
    else:
        return render_template('inputangka/angkainput.html')
        
        
    


# opsional 
#@app.route('/hasiltmbh')
#def tambah():
    #return render_template('result.html')

# kondisi jika error 
@app.route('/errmassage')
def massage():
    return render_template('errhtml/errmassage.html')


# clear form 
@app.route('/clear')
def clear():
    # session pop untuk menghapus isi form ketika tidak jadi input
    session.pop('a1',None)
    session.pop('a2',None)
    session.pop('op',None)
    return redirect(url_for('index2'))



if __name__ == "__main__":
    app.run(debug=True)
