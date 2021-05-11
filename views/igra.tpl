%from Modul import ZMAGA,PORAZ
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Vislice</h1>
    <h2>Igraš igro:</h2>
    <h3>Si v stanju {{ stanje }}</h3>

    <h3>Pravilni del gesla:</h3>
    <h4>{{ igra.pravilni_del_gesla() }}</h4>
    <h4>{{ igra.napačne_črke() }}</h4>

    <h3>Stopnja obešenosti</h3>
    <h4>{{ igra.št_napak() }}</h4>

    <img src="img/{{ igra.št_napak() }}.jpg" alt="Stopnja obešenosti"></img>

% if stanje == ZMAGA:
    <h3>Bravo zmagal si!</h3>
    <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>
% elif stanje == PORAZ:
    <h3>Izgubil si!</h3>
    <h3>Pravilno geslo je bilo: {{ igra.geslo() }}</h3>
    <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>
% else:
    <form method="POST">
        <label> Vnesi črko: 
            <input type="text", name="crka">
        </label>
        <input type="submit">
    </form>

% end


</body>
</html>