from django.shortcuts import render, HttpResponse


def cars_view(request):
    html = '''
        <html>
            <head>
                <title>Meus Carros</title>
            </head>
            <body>
                <h1>Carros da PycodeBR</h1>
                <h3>Só carro top!</h3>
            </body>
        </html>
    '''
    return HttpResponse(html)
