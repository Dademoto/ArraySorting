

# **Ordinamento di Array: Un Mondo di Possibilità**
Hai bisogno di mettere in ordine i tuoi dati? Abbiamo l'algoritmo giusto per te!

![Tipico uttilizzatore di sort](/tipico_uttilizzatore_di_sort.jpg)

esempi simpatici degli ordinamenti [Esempio Bubble Sort](https://youtu.be/kPRA0W1kECg?si=Ij753jlQVH9xHv2T)

**Bubble Sort**: Un classico per iniziare, semplice ma potrebbe non essere il più efficiente per grandi dataset.
**Quick Sort**: Veloce e potente, divide e conquista per un ordinamento rapido.
**Radix Sort**: Eccelle con numeri interi, ordinandoli in base alle cifre.
**Heap Sort**: Basato sulla struttura dati heap, offre prestazioni costanti nel caso peggiore.
Scegli l'algoritmo ideale in base alle caratteristiche dei tuoi dati e alle tue esigenze di performance.

## Vuoi approfondire? Scopri come funzionano questi algoritmi, i loro punti di forza e di debolezza, e come implementarli in modo efficiente.

- Bubble Sort
Il Bubble Sort è uno dei più semplici algoritmi di ordinamento da implementare. Funziona confrontando coppie di elementi adiacenti e scambiandoli se sono nell'ordine sbagliato. Questo processo viene ripetuto fino a quando l'array è completamente ordinato.
[Esempio bubble sort](https://youtu.be/g_xesqdQqvA?si=-bXL-6DHBV97CUcD)


- Quick Sort
Il Quick Sort è un algoritmo di ordinamento divide et impera che sceglie un elemento pivot e partiziona l'array in due parti: gli elementi minori del pivot e gli elementi maggiori del pivot. Questo processo viene ripetuto ricorsivamente fino a quando l'array è completamente ordinato.
[Esempio quick sort](https://youtu.be/kFeXwkgnQ9U?si=5xTt2UPDFpLF8jQH)

- Radix Sort
Il Radix Sort è un algoritmo di ordinamento non basato sul confronto che ordina gli elementi in base alle loro cifre. Funziona eseguendo passaggi di ordinamento per ogni cifra, da quella meno significativa a quella più significativa.
[Esempio Radiux Sort](https://youtu.be/BVGRgTALQ44?si=oK5Rh5Cm7TWZFuVY)

- Heap Sort
Il Heap Sort è un algoritmo di ordinamento in-place che utilizza una struttura dati heap. Funziona costruendo un heap e poi estraendo gli elementi uno per uno dall'heap, inserendoli in un array ordinato.
[Esemipio Heap Sort](https://www.youtube.com/watch?v=MtQL_ll5KhQ)


| Algoritmo | Miglior caso | Caso medio | Peggior caso | Stabile | Spazio aggiuntivo | Descrizione breve |
|---|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | Sì | O(1) | Confronta e scambia elementi adiacenti ripetutamente. Semplice ma inefficiente per grandi array. |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | No | O(log n) | Divide e conquista: sceglie un pivot e partiziona l'array. Veloce in media, ma può degenerare. |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | Sì | O(n) | Divide e conquista: divide l'array in metà, ordina le metà e le unisce. Efficiente e stabile. |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | Sì | O(1) | Utilizza una struttura heap per ordinare. Efficiente e in-place. |
| Radix Sort | O(nk) | O(nk) | O(nk) | Sì | O(n+k) | Ordina gli elementi in base alle cifre. Efficiente per numeri interi. |


**Bubble Sort**: Facile da implementare, ma inefficiente per grandi array.
**Quick Sort**: Veloce in media, ma può degenerare nel caso peggiore.
**Radix Sort**: Ottimo per numeri interi, ma non è adatto ad altri tipi di dati.
**Heap Sort**: Garantisce una complessità temporale O(n log n), ma richiede più spazio aggiuntivo rispetto al Quick Sort.

### In conclusione:

La scelta dell'algoritmo di ordinamento dipende dalle tue esigenze specifiche. Considera la dimensione dell'array, il tipo di dati, la stabilità richiesta e le risorse disponibili.


#### Come eseguire i vari scripts?

Semplicemente aprendo in terminale e richiamando python basta fare:

```
    posizione_nella_directory> Python3 script.py
```

#### Per esempio:
    
```
    C:\Users\Dal Molin Nicola\git105_ArraySort_Progetto> Python3 ArraySort.py
```