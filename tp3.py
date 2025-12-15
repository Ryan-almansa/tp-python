note = 15


if note % 2 == 0:
    print(f"La note {note} est PAIRE.")
else:
    print(f"La note {note} est IMPAIRE.")

if note >= 18:
    print("Excellent")
elif note >= 14:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Échec")

info = {"Almansa": "Ryan", "19": 30} 
print(info["Almansa"]) 

#*********************version console**********************

const note = 20;

console.log(`Note : ${note} `);

if (note % 2 === 0) {
    console.log(`La note ${note} est PAIRE.`);
} else {
    console.log(`La note ${note} est IMPAIRE.`);
}

if (note >= 18) {
    console.log("Excellent");
} else if (note >= 14) {
    console.log("Bien"); 
} else if (note >= 10) {
    console.log("Passable");
} else {
    console.log("Échec");
}

const info = {"Almansa": "Ryan", "19": 30}; 
console.log(info["Almansa"])