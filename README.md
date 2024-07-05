# Progetto Python di Riccardo Badanai | Start2Impact 🚀

## Descrizione 📋

Questo progetto è un'applicazione Python che interagisce con l'API di CoinMarketCap per raccogliere e analizzare i dati delle criptovalute. L'obiettivo del progetto è ottenere informazioni aggiornate sulle criptovalute, elaborarle e generare report utili per l'analisi del mercato.

## Caratteristiche ✨

- **Connessione all'API di CoinMarketCap**: Estrae dati aggiornati sulle criptovalute.
- **Elaborazione dei dati**:
  - Determina la criptovaluta con il volume più alto nelle ultime 24 ore.
  - Ordina le criptovalute in base al volume di scambio.
  - Genera liste delle prime 10 e ultime 10 criptovalute per volume.
  - Calcola la somma del prezzo per acquistare una unità delle prime 20 criptovalute.
  - Filtra le criptovalute con volume superiore a 76,000,000 USD.
- **Generazione di report**: Crea report dettagliati in formato JSON.

## Requisiti 🛠️

- Python 3.x
- Moduli Python:
  - `requests`
  - `json`
  - `os`
  - `datetime`

## Installazione 🖥️

1. Clona il repository:

    ```bash
    git clone https://github.com/rickybada/CoinMarketCupReport.git
    cd CoinMarketCupReport
    ```

2. Installa le dipendenze richieste:

    ```bash
    pip install requests
    ```

## Utilizzo 🚀

1. Esegui lo script Python per ottenere i dati aggiornati sulle criptovalute e generare i report:

    ```bash
    python PythonCryptoProject.py
    ```

2. I report generati saranno salvati in un file JSON nel seguente formato:

    ```json
    {
        "Best10": {
            "Criptovaluta1": "Volume1",
            "Criptovaluta2": "Volume2",
            ...
        },
        "Worst10": {
            "Criptovaluta1": "Volume1",
            "Criptovaluta2": "Volume2",
            ...
        },
        "Money20Crypto": "Somma",
        "FilterCrypto24": [
            "Criptovaluta1",
            "Criptovaluta2",
            ...
        ]
    }
    ```

## Struttura del Progetto 🗂️

- `PythonCryptoProject.py`: Il file principale che contiene il codice per l'interazione con l'API e l'elaborazione dei dati.
- `CryptoMarketCupReport_2023-03-17_17-39-10.json`: Un esempio di report generato.

## Contributi 🤝

I contributi sono benvenuti! Sentiti libero di aprire issue o pull request per migliorare questo progetto.

## Licenza 📄

Questo progetto è rilasciato sotto la licenza MIT. Consulta il file LICENSE per ulteriori dettagli.
