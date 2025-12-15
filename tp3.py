def calculer_moyenne_notes():
    """mettre des notes et calculer la moyenne"""    
    notes = [] 
    print("Entrée des notes pour calculer")
    print("Entrez les notes une par une. Tapez 'fin' (ou 'stop') pour terminer la saisie.")

    
    while True:
        entree = input("Note : ")        
        if entree.lower() in ['fin', 'stop']:
            break 
        try:
            note = float(entree)            
            if 0 <= note <= 20:
                notes.append(note) 
                print(f"Note ajoutée  :  {note}")
            else:
                print("Note invalide. Veuillez entrer une note entre 0 et 20.")                
        except ValueError:            
            print("Erreur :Entre un nombre valide ou 'fin'.")    
    print("\n Résultat")    
    if not notes:
        print("Aucune note n'a été saisie.Pas de moyenne.")
    else:    
        somme_notes = sum(notes)        
        nombre_notes = len(notes)        
        moyenne = somme_notes / nombre_notes        
        print(f"Notes saisies : {notes}")
        print(f"Total des notes : {somme_notes}")
        print(f"Nombre de notes : {nombre_notes}")
        print(f"La moyenne de la classe est : {moyenne:.2f}") 
calculer_moyenne_notes()


#*************version js**************
function calculerMoyenneNotes() {
    const notes = [];
    let entree;

    console.log("Entrée des notes pour calculer ");
    console.log("Entre les notes une par une. Tapez 'fin' (ou 'stop') pour terminer la saisie.");

    while (true) {
        entree = prompt("Note (ou 'fin') : ");
        
        if (entree === null) {
            entree = 'fin'; 
        }

        if (entree.toLowerCase() === 'fin' || entree.toLowerCase() === 'stop') {
            break;
        }

        const note = parseFloat(entree);
        
        if (isNaN(note)) {
            console.error("Erreur : Entre un nombre valide ou 'fin'.");
            continue;
        }

        if (note >= 0 && note <= 20) {
            notes.push(note);
            console.log(`Note ajoutée : ${note}`);
        } else {
            console.log("Note invalide. Veuillez entrer une note entre 0 et 20.");
        }
    }

    console.log("\n résultat");

    if (notes.length === 0) {
        console.log("Aucune note n'a été saisie. Pas de moyenne.");
    } else {
        const sommeNotes = notes.reduce((acc, current) => acc + current, 0);
        const nombreNotes = notes.length;
        const moyenne = sommeNotes / nombreNotes;

        console.log(`Notes saisies : [${notes.join(', ')}]`);
        console.log(`Total des notes : ${sommeNotes}`);
        console.log(`Nombre de notes : ${nombreNotes}`);
        console.log(`La moyenne de la classe est : ${moyenne.toFixed(2)}`);
    }
}

calculerMoyenneNotes();