package main

import (
	"fmt"
	"math/rand"
	"time"
)

func shuffle(arr []string) {
	t := time.Now()
	rand.Seed(int64(t.Nanosecond())) // no shuffling without this line

	for i := len(arr) - 1; i > 0; i-- {
		j := rand.Intn(i)
		arr[i], arr[j] = arr[j], arr[i]
	}
}

func pop(list []string) string {

	return list[len(list)-1] //Retourne le dérnier élément de la liste
}

func main() {

	var list = []string{"Shérif", "Bandit", "Bandit", "Renégat"}

	for i := 0; i < len(list); i++ {

		list[i] = list[len(list)-1] // Copier le dernier élément à l'index i.
		list[len(list)-1] = ""      // Effacer le dernier élément (écrire la valeur zéro).
		list = list[:len(list)-1]   // Tranche tronquée.

		shuffle(list) // On mélange le tableau

		element := pop(list) // On récupère le premier élément du tableau en l'enlevant

		fmt.Printf("Ton Rôle : %v \n", element) // On affiche l'élement et le nouveau tableau

	}

}
