from flask import Flask, redirect,render_template,url_for,request,session
   


# run file in __main__
app = Flask(__name__) 


# key untuk session 
app.secret_key = '123'

##################
# tampilan utama 
##################
@app.route('/')
def index():
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Welcome</title>
            <link rel="stylesheet" href="static/bootstrap/css/index-route/index_route.css">

        <!--1. font link-->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <!-- 2. Link Bootstrap  -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div>
                <h1>Calculator Flask</h1>
                <div class="main-content">
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
        </div>


    <footer class="text-center bg-body-tertiary">
    <!-- Grid container -->
    <div class="container pt-4">
        <!-- Section: Social media -->
        <section class="mb-4">
        <!-- Facebook -->
        <a
            data-mdb-ripple-init
            class="btn btn-link btn-floating btn-lg text-body m-1"
            href="#!"
            role="button"
            data-mdb-ripple-color="dark"
            ><i class="fab fa-facebook-f"></i
        ></a>

        <!-- Twitter -->
        <a
            data-mdb-ripple-init
            class="btn btn-link btn-floating btn-lg text-body m-1"
            href="#!"
            role="button"
            data-mdb-ripple-color="dark"
            ><i class="fab fa-twitter"></i
        ></a>

        <!-- Google -->
        <a
            data-mdb-ripple-init
            class="btn btn-link btn-floating btn-lg text-body m-1"
            href="#!"
            role="button"
            data-mdb-ripple-color="dark"
            ><i class="fab fa-google"></i
        ></a>

        <!-- Instagram -->
        <a
            data-mdb-ripple-init
            class="btn btn-link btn-floating btn-lg text-body m-1"
            href="#!"
            role="button"
            data-mdb-ripple-color="dark"
            ><i class="fab fa-instagram"></i
        ></a>

        <!-- Github -->
        <a
            data-mdb-ripple-init
            class="btn btn-link btn-floating btn-lg text-body m-1"
            href="#!"
            role="button"
            data-mdb-ripple-color="dark"
            ><i class="fab fa-github"></i
        ></a>
    </section>
    <!-- Section: Social media -->
  </div>
  <!-- Grid container -->

    <!-- Copyright -->
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.05);">
    © 2020 Copyright:
    <a class="text-body" href="https://mdbootstrap.com/">MDBootstrap.com</a>
    </footer> 

    </body>
</html>
    """


#############################
# tampilan hitung 
#############################
@app.route('/hitung',methods = ['GET','POST'])
def index2():

    # set variabel gabung untuk html untuk input 
    gabung = render_template('inputangka/angkainput.html')
    

    if request.method =='POST':
        a_1 = request.form['a1'] 
        a_2 = request.form['a2'] 
        operator_str = request.form['op']
        
        
        # kondisi jika form input adalah 0 atau kosong
        if a_1 =='' or a_2 =='' or operator_str=='':
            return redirect(url_for('message'))
        
        # tipe data ke int
        # kalau hanya variabel itu string
        angka1 = int(a_1)
        angka2 = int(a_2)
        operator = operator_str

        
       ########################################## 
        # spagetti percabang
        # bagian tambah + 
        #########################################
        #if operator =='+':
            #hasil = angka1 + angka2
            #return render_template('hasiltambah/hasiltmbah.html',angka1=angka1,angka2=angka2,hasil=hasil,operator=operator)
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

        



        #######################################
        # kondisi percabangan 2
        # kondisi if dan += dengan file html
        #######################################
        
        # + 
        if operator =="+":
            hasil = angka1 + angka2
            gabung+= render_template('hasiltambah/hasiltmbah.html',angka1=angka1,angka2=angka2,hasil=hasil)
        # -    
        elif operator == "-":
            hasil = angka1 - angka2 
            gabung+= render_template('hasilkurang/hasilkurang.html',angka1=angka1,angka2=angka2,hasil=hasil)
        
        # x 
        elif operator =='x':
            hasil = angka1 * angka2 
            gabung +=render_template('hasilkali/hasilkali.html',angka1=angka1,angka2=angka2,hasil=hasil)
        
        # /     
        elif operator =="/":
            hasil = angka1 / angka2
            gabung += render_template('hasilbagi/hasilbagi.html',angka1=angka1,angka2=angka2,hasil=hasil)
    return gabung

        
    
    


# opsional 
#@app.route('/hasiltmbh')
#def tambah():
    #return render_template('result.html')

######################
# kondisi jika error 
######################
@app.route('/errmassage')
def message():
    return redirect(url_for('static',filename="bootstrap/js/err.js"))


#############
# clear form 
#############
@app.route('/clear')
def clear():
    # session pop untuk menghapus isi form ketika tidak jadi input
    session.pop('a1',None)
    session.pop('a2',None)
    session.pop('op',None)
    return redirect(url_for('index2'))


#############
# source dev 
#############
@app.route('/src')
def source():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title></title>
        <link href="css/style.css" rel="stylesheet">
      </head>
      <body>
        <div class="source">
            <div class="source-content">

            </div>
        </div> 
      </body>
    </html>    

    """
    

if __name__ == "__main__":
    app.run(debug=True)



















































































