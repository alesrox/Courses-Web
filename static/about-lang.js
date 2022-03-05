$(function() {
    if (lang === 'es') {
        $(".title").append("SOBRE MI");
        $(".p1").prepend("Soy un adolescente español, al cual, le encanta la programación, \
            he programado en varios lenguajes como C, C#, Bash, PHP, JavaScript o Julia, \
            pero de los cuales con el que empecé, y mayor soltura tengo es Python.");
        $(".p2").prepend("Aparte de desarrollo web y movil, \
            programo juegos cortos y sencillos en C# con Unity como Engine, \
            los cuales suelo publicar en");
        $(".p2b").append("o en");
        $(".p3").prepend("También me gusta de vez en cuando hacer pequeños codigos de \
            algoritmos sencillos o algun codigo de JavaScript en");
        $(".p4").prepend("Si quieres saber más sobre mis proyectos ve a");
        $(".a1").append("Mi Portafolio");
    } else if (lang == 'ca') { 
        $(".title").append("SOBRE MI");
        $(".p1").prepend("Hola sóc Alex, i sóc un adolescent espanyol, a qui li encanta la programació, \
            he programat en diversos llenguatges com C, C#, Bash, PHP, JavaScript o Julia, \
            però dels quals amb el que vaig començar, i més facilitat tinc és Python.");
        $(".p2").prepend("A més de desenvolupament web i mòbil, \
            programo jocs curts i senzills en C# amb Unity com de Engine, \
            els quals sòl publicar a");
        $(".p2b").append("o en");
        $(".p3").prepend("També m'agrada de tant en tant fer petits codis de \
            algoritmes senzills o algun codi de JavaScript en ");
        $(".p4").prepend("Si vols saber més sobre els meus projectes veu al");
        $(".a1").append("Meu Portafoli");
    } else if (lang == 'it') {
        $(".title").append("SU DI ME");
        $(".p1").prepend("Sono un adolescente spagnolo, che ama la programmazione, \
            Ho programmato in diversi linguaggi come C, C#, Bash, PHP, JavaScript o Julia, \
            ma di cui quello con cui ho iniziato, e la maggiore fluidità che ho è Python. ");
        $(".p2").prepend("Oltre allo sviluppo web e mobile, \
            Programmo giochi brevi e semplici in C# con Unity as Engine, \
            in cui di solito pubblico");
        $(".p2b").append("o in");
        $(".p3").prepend("Mi piace anche fare piccoli codici di tanto in tanto da \
            semplici algoritmi o codice JavaScript in formato ");
        $(".p4").prepend("Se vuoi saperne di più sui miei progetti vai sul");
        $(".a1").append("Mio Portfolio");
    }else {
        $(".title").append("ABOUT ME");
        $(".p1").prepend("Hi my name is Alex, i'm a 15 years old spaniard boy who loves computer programming, \
            I can program in C, C#, Bash, PHP, JavaScript or Julia, \
            but the one I started with, and my favorite is Python.");
        $(".p2").prepend("I love the Web and Mobile Development, also I \
            make simples games in C# with Unity as Engine, \
            I use to post them in");
        $(".p2b").append("or in");
        $(".p3").prepend("Some time I made simple algorithms or practice projects in");
        $(".p4").prepend("In order to know more about my projects stop by");
        $(".a1").append("My Portfolio");
    }
});