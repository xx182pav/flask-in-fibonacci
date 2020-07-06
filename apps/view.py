from apps.app import app
from flask import render_template
from flask import request
from apps.memcache_client import client

def new_fibo(n):
    result = None
    try:
        result = client.get(str(n))
    except:
        result = None

    if result:
        return result
    else:
        fib1 = fib2 = 1
        if n in [0,1]:
            client.set(str(n), str(n))
            return n

        for _ in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2


        client.set(str(n), str(fib2))
        return str(fib2)



@app.route('/')
def index():
    k = request.args.get('k', 0)
    try:
        k = int(k)
    except:
        k = 0
    fibo = new_fibo(k)
    return render_template('index.html', n=fibo)
