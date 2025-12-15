try:
    N = int(input("Entrez un nombre entier positif : "))

    if N < 1:
        print("Entre un entier supérieur ou égal à 1.")
    else:
        somme_iterative = 0  

       
        for i in range(1, N + 1):
            somme_iterative = somme_iterative + i 

        print(f"\nMéthode 1 : Boucle For ")
        print(f"La somme des nombres de 1 à {N} est : {somme_iterative}")

except ValueError:
    print("Erreur : s'il te plait entre un nombre entier.")





#************version js**************
function calculerSommeIterative() {
    const input = prompt("Entrez un nombre entier positif (N) :");
    const N = parseInt(input);
    if (isNaN(N)) {
        console.error("Erreur : s'il te plait entre un nombre entier.");
        return;
    }
    if (N < 1) {
        console.log("Entre un entier supérieur ou égal à 1.");
        return;
    }
    let somme_iterative = 0; 
    for (let i = 1; i <= N; i++) {
        somme_iterative += i; 
    }
    console.log("\nMéthode 1 : Boucle For ");
    console.log(`La somme des nombres de 1 à ${N} est : ${somme_iterative}`);
}

calculerSommeIterative();