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
    <h4>{{ igra.napačne_črke() }}</h4>

    <h3>Stopnja obešenosti</h3>
    <h4>{{ igra.število_napak() }}</h4>

    <img src="img/{{ igra.število_napak() }}.jpg" alt="Stopnja obešenosti"></img>

    <form method="POST">
        <label> Vnesi črko: 
            <input type="text", name="crka">
        </label>
        <input type="submit">
    </form>

</body>
</html>