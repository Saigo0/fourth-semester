let idade = 21;  
console.log(idade);
let nome = "José";
let boolean = true;
let vet = ["1", "2", "3"];
let objeto = {nome: "José", idade: "21"};


let x = 2
x = x + 3
console.log(x);

x = x - 3
console.log(x);

x = x * 2
console.log(x);

x = x / 2
console.log(x);

x = x + "2"
console.log(x);

/*
Condicionais IF e ELSE
 > maior
 < menor
 >= maior ou igual
 <= menor ou igual
 == igual
 === igual, porém analisa o tipo
 != diferente
 !== diferente, porém analisa o tipo
*/

if(idade >= 18){
    console.log("adulto");
} else{
    console.log("criança");
}

if(idade >= 18){
    if(idade >= 60){
        console.log("idoso");
    } else{
        console.log("maior de idade");
    }
} else{
    console.log("menor de idade");
}

let verifica = false;
if(verifica){
    console.log("validou");
}

let profissao = "bombeiro";
switch(profissao){
    case "policial":
        console.log("Uniforme azul");
        break;
    
    case "bombeiro":
        console.log("Uniforme vermelho");
        break;
        
    default:
        console.log("Profissão não encontrada.");       
}

for(let i = 0; i <= 5; i++){
    console.log("Número: " + i);
}

let cont = 0

while(cont <= 5){
    console.log("Contagem while: " + cont);
    cont ++;
}




