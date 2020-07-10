const tf = require('@tensorflow/tfjs');
const fs = require('fs');

let file = fs.readFileSync('cotacao-do-dolar.csv', {encoding: 'utf8'}); // le os aquivos na formatacao de acentuacao portuguesa
file = file.toString().trim(); // passa tudo pra string e elimina espacos vazios

const lines = file.split('\r\n');
let X = []; // dados de entrada
let Y = [];  // dados de saida
let qtdLines = 0;

for (let l = 1; l<lines.length; l++){
  let cells1 = [];

  if (qtdLines == (lines.length - 2)) {
    cells1 = ["01.01.2019", 3.8813, 3.8813, 3.8813, 3.8813];
  } else {
    cells1 = lines[l+1].split(';');
  }
  
 let cells2 = lines[l].split(';');
 

  qtdLines++;

}

