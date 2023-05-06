def biseccion(f, a, b, tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        print("Error: la función debe cambiar de signo en el intervalo [a, b]")
        return None
    for i in range(max_iter):
        c = (a + b)/2
        fc = f(c)
        if abs(fc) < tol:
            return c, i
        if fa*fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    print("Error: se alcanzó el número máximo de iteraciones")
    return None

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    fx0 = f(x0)
    fx1 = f(x1)
    for i in range(max_iter):
        x2 = x1 - fx1*(x1 - x0)/(fx1 - fx0)
        fx2 = f(x2)
        if abs(fx2) < tol:
            return x2, i
        x0 = x1
        x1 = x2
        fx0 = fx1
        fx1 = fx2
    print("Error: se alcanzó el número máximo de iteraciones")
    return None

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    fx0 = f(x0)
    for i in range(max_iter):
        dfx0 = df(x0)
        if abs(dfx0) < tol:
            print("Error: derivada demasiado cercana a cero")
            return None
        x1 = x0 - fx0/dfx0
        fx1 = f(x1)
        if abs(fx1) < tol:
            return x1, i
        x0 = x1
        fx0 = fx1
    print("Error: se alcanzó el número máximo de iteraciones")
    return None

def f(x):
    return x**3 + x + 16

def df(x):
    return 3*x**2 + 1

a = -5
b = 5
x0 = -5
x1 = 5
tol = 1e-6
max_iter = 100

print("Método de la bisección:")
sol_b, iter_b = biseccion(f, a, b, tol, max_iter)
print("Solución:", sol_b)
print("Iteraciones:", iter_b)

print("Método de la secante:")
sol_s, iter_s = secante(f, x0, x1, tol, max_iter)
print("Solución:", sol_s)
print("Iteraciones:", iter_s)

print("Método de Newton-Raphson:")
sol_n, iter_n = newton_raphson(f, df, x0, tol, max_iter)
print("Solución:", sol_n)
print("Iteraciones:", iter_n)
