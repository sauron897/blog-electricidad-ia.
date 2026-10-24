import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from agent import build_agent
from rag import ingest_uploaded_files

load_dotenv()

st.set_page_config(
    page_title="Inductech — Asistente Virtual",
    page_icon="⚡",
    layout="wide"
)

# ---- Sidebar ----
with st.sidebar:
    st.markdown("## ⚡ Inductech")
    st.markdown("**Electricidad · Energía · Consultoría Técnica**")
    st.divider()

    st.markdown("#### Cargar documentos internos")
    st.caption("Sube manuales, fichas técnicas o tarifas en PDF o TXT para que el agente las consulte.")
    uploaded = st.file_uploader(
        "Selecciona archivos",
        type=["pdf", "txt"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )
    if uploaded:
        with st.spinner("Procesando documentos..."):
            count = ingest_uploaded_files(uploaded)
        st.success(f"{count} documento(s) añadido(s) a la base de conocimiento.")

    st.divider()
    if st.button("🗑 Limpiar conversación", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Requiere: `OPENAI_API_KEY` y `TAVILY_API_KEY` en el archivo `.env`")

# ---- Main chat ----
st.title("⚡ Inductech — Asistente Virtual")
st.caption("Consulta sobre instalaciones eléctricas, normativas, tarifas y servicios.")

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": (
            "¡Hola! Soy el asistente virtual de **Inductech**. "
            "Puedo ayudarte con consultas técnicas sobre instalaciones eléctricas, "
            "normativas vigentes, tarifas y servicios. ¿En qué puedo ayudarte hoy?"
        )
    }]

if "agent" not in st.session_state:
    with st.spinner("Iniciando agente..."):
        st.session_state.agent = build_agent()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Escribe tu consulta aquí..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Consultando..."):
            history = [
                HumanMessage(content=m["content"]) if m["role"] == "user"
                else AIMessage(content=m["content"])
                for m in st.session_state.messages
            ]
            result = st.session_state.agent.invoke({"messages": history})
            response = result["messages"][-1].content
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
