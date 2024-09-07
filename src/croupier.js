var cartasUsadas = [];
const naipes = ['O', 'E', 'P', 'C'];
const valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
let numero_jogadores = 10;
let jogadores = [];

function escolherValorAleatorio(vetor) {
    const indiceAleatorio = Math.floor(Math.random() * vetor.length);
    return vetor[indiceAleatorio];
}

class Carta {
    constructor(naipe, valor) {
        this.naipe = escolherValorAleatorio(naipes);
        this.valor = escolherValorAleatorio(valores);
    }
}

class Jogador {
    constructor( carta_1, carta_2) {
        this.carta_1 = new Carta;
        this.carta_2 = new Carta;
    }
}

function cartasSaoIguais(carta1, carta2) {
    return carta1.valor === carta2.valor && carta1.naipe === carta2.naipe;
}

function  distribuirCartas(){
    let c1 = new Carta();
    while (cartasUsadas.some(carta => cartasSaoIguais(carta, c1))) {
        c1 = new Carta();
    }
    cartasUsadas.push(c1);
    let c2 = new Carta();
    while (cartasUsadas.some(carta => cartasSaoIguais(carta, c2))) {
        c2 = new Carta();
    }
    cartasUsadas.push(c2);

    let jog = new Jogador();
    jog.carta_1 = c1;
    jog.carta_2 = c2;
    jogadores.push(jog);
}
function  distribuirCartasComunitarias(){
    let c1 = new Carta();
    while (cartasUsadas.some(carta => cartasSaoIguais(carta, c1))) {
        c1 = new Carta();
    }
    cartasUsadas.push(c1);
    let c2 = new Carta();
    while (cartasUsadas.some(carta => cartasSaoIguais(carta, c2))) {
        c2 = new Carta();
    }
    cartasUsadas.push(c2);
    let c3 = new Carta();
    while (cartasUsadas.some(carta => cartasSaoIguais(carta, c3))) {
        c3 = new Carta();
    }
    cartasUsadas.push(c3);
    let c4 = new Carta();
    while (cartasUsadas.some(carta => cartasSaoIguais(carta, c4))) {
        c4 = new Carta();
    }
    cartasUsadas.push(c4);
    let c5 = new Carta();
    while (cartasUsadas.some(carta => cartasSaoIguais(carta, c5))) {
        c5 = new Carta();
    }
    cartasUsadas.push(c5);

    let comunitarias = [c1,c2,c3,c4,c5];

    return comunitarias;

}

console.log(distribuirCartasComunitarias());


for(let i=0;i<numero_jogadores; i++){
    distribuirCartas();
}

for(let i=0;i<numero_jogadores; i++){
    console.log(jogadores[i]);
}


