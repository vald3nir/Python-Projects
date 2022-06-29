from pyrebase import pyrebase

# -----------------------------------------------------------
# setup
# -----------------------------------------------------------

libraries = ["setuptools", "wheel", "pyrebase4"]
# call("pip install " + ' '.join(libraries), shell=True)

firebaseConfig = {
    "apiKey": "AIzaSyCxujiFsfdNZEH8zIxIQwaAXvujQvSFyA4",
    "authDomain": "smart-energy-3e7aa.firebaseapp.com",
    "databaseURL": "https://smart-energy-3e7aa-default-rtdb.firebaseio.com",
    "projectId": "smart-energy-3e7aa",
    "storageBucket": "smart-energy-3e7aa.appspot.com",
    "messagingSenderId": "8984393302",
    "appId": "1:8984393302:web:e1d193912f96b7d68d6df7",
    "measurementId": "G-RKB971HGGY"
}

# -----------------------------------------------------------


db = pyrebase.initialize_app(firebaseConfig).database()
db.remove()

db.child("test").child("valdenir").push(data={
    "email": "a1@gmial.com",
    "password": "12345678"
})
db.child("test").child("valdenir2").push(data={
    "email": "a2@gmial.com",
    "password": "12345678"
})

data = db.child("test").get()
for d in data:
    key = d.key()
    value = d.val()
    print(key, value)
