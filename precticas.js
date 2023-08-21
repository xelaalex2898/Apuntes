function max(array) {
    let actualMax=array[0];
    for (let i = 1; i < array.length; i++) {
        const element = array[i];
        if (array[i]<=actualMax){
            continue;
        }
        if (array[i]>actualMax){
            actualMax=array[i]
        }
    }
}
function primo (number){
    for (let i = 0; i < number; i++) {
        if (!number%i) {
            return false;
        }
        
    }
    return true;
}
function palindromo(cadena) {
    let caracteres = cadena.split('');
    let caracteresInvertidos = caracteres.reverse();
    let cadenaInvertida = caracteresInvertidos.join('');

    if (cadena==cadenaInvertida) {
        return true
    }
  
    return false;
  }
function sumaPrimos(number) {
    primos=[];
    for (let i =2 ; i < number; i++) {
        if (primo(i)){
            primos.push(i)
        }
        
    }
    const sum = primos.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    return sum
}


  
  
  