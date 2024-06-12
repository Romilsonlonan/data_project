import yfinance as yf
import pandas as pd
from loguru import logger
import time

start_time = time.time()

commodities = ['CL=F', 'CG=F', 'SI=F']  # Petróleo Bruto, Ouro e Prata
logger.add("file_{time}.log")


def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    try:
        start_time = time.time()
        ticker = yf.Ticker(simbolo)
        dados = ticker.history(period=periodo, interval=intervalo)
        dados['simbolo'] = simbolo  # Adiciona a coluna do simbolo
        logger.info(f"Dados da commodity {simbolo} coletados com sucesso.")
        logger.info(f"--- {time.time() - start_time} --- seconds ---")
        return dados
    except Exception as e:
        logger.error(f"Falha ao coletar dados da commodity {simbolo}. Erro: {e}")
        return None


def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados_de_commodities = buscar_dados_commodities(simbolo)
        if dados_de_commodities is not None:
            todos_dados.append(dados_de_commodities)
        else:
            logger.warning(f"Dados da commodity {simbolo} não coletados.")

    if todos_dados:
        logger.info("Todos os dados das commodities coletados com sucesso.")
        logger.info(f"--- {time.time() - start_time} --- seconds ---")
        return pd.concat(todos_dados)
    else:
        logger.error("Falha ao coletar dados de todas as commodities.")
        return None


if __name__ == "__main__":
    dados_de_todas_as_commodities = buscar_todos_dados_commodities(commodities)
