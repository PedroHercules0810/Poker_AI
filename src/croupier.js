//função que escolhe valores aleatorios dentro de um vetor
function escolherValorAleatorio(vetor) {
    const indiceAleatorio = Math.floor(Math.random() * vetor.length);
    return vetor[indiceAleatorio];
}

//classe para criação das cartas
class Carta {
    constructor(naipe, valor) {
        this.naipe = naipe;
        this.valor = valor;

        const naipes = ['O', 'E', 'P', 'C'];
        const valores = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];

        //aleatorizando tanto o naipe quanto o valor
        const naipe_aleatorio = escolherValorAleatorio(naipes)
        let valor_aleatorio = escolherValorAleatorio(valores)

        /*
        if (valor_aleatorio == 11) {
            valor_aleatorio = "Valete"
        }
        if (valor_aleatorio == 12) {
            valor_aleatorio = "Dama"
        }
        if (valor_aleatorio == 13) {
            valor_aleatorio = "Rei"
        }
        if (valor_aleatorio == 14) {
            valor_aleatorio = "Ás"
        }
        */
        //gerando a carta propriamente dita
        const carta = [valor_aleatorio, naipe_aleatorio];

        return carta;
    }
}

class Jogador {
    constructor(carta_1, carta_2) {
        this.carta_1 = new Carta;
        this.carta_2 = new Carta;

        if (carta_1 == carta_2) {
            this.carta_1 = new Carta;
            this.carta_2 = new Carta;
        }
    }
}


function diferenciar_jogos(jogadores) {
    for (let j = 0; j < jogadores.length; j++) {
        for (let k = 0; k < jogadores.length; k++) {
            if (j != 0 && k != 0 && jogadores[j].carta_1 == jogadores[k].carta_1) {
                jogadores[j].carta_1 = new Carta;
            }
        }

        for (let m = 0; m < jogadores.length; m++) {
            if (j != 0 && m != 0 && jogadores[j].carta_2 == jogadores[m].carta_2) {
                jogadores[j].carta_2 = new Carta;
            }
        }
        for (let l = 0; l < jogadores.length; l++) {
            if (j != 0 && l != 0 && jogadores[j].carta_1 == jogadores[l].carta_2) {
                jogadores[j].carta_1 = new Carta;
            }
        }
        for (let n = 0; n < jogadores.length; n++) {
            if (j != 0 && n != 0 && jogadores[j].carta_2 == jogadores[n].carta_1) {
                jogadores[j].carta_2 = new Carta;
            }
        }
    }

    return jogadores;
}




let numero_jogadores = 10;
let jogadores = [];

for (let i = 0; i < numero_jogadores; i++) {
    const jogador = new Jogador();
    jogadores.push(jogador);
}



console.log(diferenciar_jogos(jogadores));

