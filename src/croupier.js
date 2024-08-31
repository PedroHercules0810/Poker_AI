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



function baralho() {
    let cartas = []
    for (let i = 1; i < 55; i++) {
        cartas.push(new Carta);
    }d

}

console.log(baralho());
