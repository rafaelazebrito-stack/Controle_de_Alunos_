import streamlit as st
import pandas as pd
import os

# =========================
# Classe Aluno
# =========================
class Aluno:
    def __init__(self, nome, data_nascimento, serie, turno, presenca):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.serie = serie
        self.turno = turno
        self.presenca = presenca
        self.nota = None    

    def para_dicionario(self):
        return {
            "Nome": self.nome,
            "Data de Nascimento": self.data_nascimento,
            "Série": self.serie,
            "Turno": self.turno,
            "Presença": self.presenca,
            "Nota": Self.nota
        }

# =========================
# Arquivo CSV
# =========================
arquivo = "alunos.csv"

if not os.path.exists(arquivo):
    df = pd.DataFrame(columns=["Nome", "Data de Nascimento", "Série", "Turno", "Presença","Nota"])
    df.to_csv(arquivo, index=False)

# =========================
# Funções CRUD
# =========================

def carregar():
    return pd.read_csv(arquivo)


def salvar(df):
    df.to_csv(arquivo, index=False)


def adicionar(aluno):
    df = carregar()
    novo = pd.DataFrame([aluno.para_dicionario()])
    df = pd.concat([df, novo], ignore_index=True)
    salvar(df)


def apagar(nome):
    df = carregar()
    df = df[df["Nome"] != nome]
    salvar(df)

# =========================
# Interface (simples)
# =========================
st.title("Controle de Alunos")

opcao = st.selectbox("Escolha uma opção", ["Adicionar", "Ver", "Apagar"])

# ADICIONAR
if opcao == "Adicionar":
    nome = st.text_input("Nome")
    data_nascimento = st.text_input("Data de Nascimento (dd/mm/aaaa)")
    serie = st.text_input("Série")
    turno = st.selectbox("Turno", ["Manhã", "Tarde", "Noite"])
    presenca = st.selectbox("Presença", ["Presente", "Falta"])
    Nota = st.text_input("Nota")

    if st.button("Salvar"):
        aluno = Aluno(nome, data_nascimento, serie, turno, presenca, nota)
        adicionar(aluno)
        st.success("Aluno salvo!")

# VER
elif opcao == "Ver":
    df = carregar()
    st.dataframe(df)

# APAGAR
elif opcao == "Apagar":
    df = carregar()
    nome = st.selectbox("Escolha o aluno", df["Nome"] if not df.empty else [])

    if st.button("Apagar"):
        apagar(nome)
        st.success("Aluno apagado!")

