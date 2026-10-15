import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_tavily import TavilySearch
from rag import get_retriever

SYSTEM_PROMPT = """Eres el asistente virtual de Inductech, empresa especializada en electricidad, energía y consultoría técnica.

Ayudas a clientes y técnicos con:
- Información sobre servicios y tarifas de Inductech
- Normativas y reglamentos eléctricos vigentes (REBT, IEC, UNE, etc.)
- Consultas técnicas sobre instalaciones eléctricas y sistemas energéticos
- Elaboración de presupuestos y reportes técnicos

Herramientas disponibles:
- `buscar_documentos`: consulta documentación interna de Inductech (manuales, fichas de servicios, tarifas, normativas propias)
- `tavily_search`: busca información actualizada en la web (precios de materiales, normativas externas, noticias del sector eléctrico)

Normas:
- Responde siempre en español, de forma profesional pero clara
- Cita la fuente cuando uses documentos internos
- Si combinas fuentes internas y web, indícalo
- Si no tienes información suficiente, dilo con honestidad y sugiere contactar a Inductech
"""


def build_agent():
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    retriever = get_retriever()

    @tool
    def buscar_documentos(consulta: str) -> str:
        """Busca en los documentos internos de Inductech: manuales técnicos, fichas de servicios, normativas internas y tarifas."""
        docs = retriever.invoke(consulta)
        if not docs:
            return "No encontré información relevante en los documentos internos de Inductech."
        parts = []
        for doc in docs:
            source = doc.metadata.get("source", "Documento interno")
            parts.append(f"[Fuente: {source}]\n{doc.page_content}")
        return "\n\n---\n\n".join(parts)

    tavily = TavilySearch(max_results=3)
    return create_react_agent(llm, [buscar_documentos, tavily], prompt=SYSTEM_PROMPT)
