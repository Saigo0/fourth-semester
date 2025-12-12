function teste(){
    console.log("teste");
}

teste();

function somar(n1, n2){
    console.log(n1+n2);
}

somar(4,5);

function nomeCompleto(nome, sobrenome){
    console.log(nome + " " + sobrenome);
}

nomeCompleto("José", "Pires");

function maiorIdade(idade) {
    if(idade >= 18){
        return "Adulto";
    } else{
        return "Criança";
    }
}

console.log(maiorIdade(21));

/*
Calcule a porcentagem entre dois números
*/

function calcPercent(percent, val){
    return (percent * val) /100
}

console.log(calcPercent(10, 50));
