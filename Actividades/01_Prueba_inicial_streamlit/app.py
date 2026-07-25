"""
Simulador y Analizador de Resultados de Fórmula 1
--------------------------------------------------
Aplicación Streamlit que:
1. Simula datos de resultados de carreras de F1.
2. Muestra análisis cuantitativo, cualitativo y gráfico.
3. Permite interacción dinámica con los resultados (filtros, controles, re-simulación).

Ejecutar con:
    streamlit run app.py
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ----------------------------------------------------------------------------
# Configuración general de la página
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Simulador F1 - Análisis de Carreras",
    page_icon="🏎️",
    layout="wide",
)

# ----------------------------------------------------------------------------
# Datos base: pilotos, escuderías y sistema de puntos oficial de la F1
# ----------------------------------------------------------------------------
EQUIPOS = {
    "Red Bull Racing": ["M. Verstappen", "S. Pérez"],
    "Ferrari": ["C. Leclerc", "C. Sainz"],
    "Mercedes": ["L. Hamilton", "G. Russell"],
    "McLaren": ["L. Norris", "O. Piastri"],
    "Aston Martin": ["F. Alonso", "L. Stroll"],
    "Alpine": ["P. Gasly", "E. Ocon"],
    "Williams": ["A. Albon", "L. Sargeant"],
    "RB": ["Y. Tsunoda", "D. Ricciardo"],
    "Kick Sauber": ["V. Bottas", "Z. Guanyu"],
    "Haas": ["K. Magnussen", "N. Hülkenberg"],
}


# ----------------------------------------------------------------------------
# Funciones de simulación
# ----------------------------------------------------------------------------
def construir_grid():
    """Devuelve una lista de diccionarios {piloto, equipo} para toda la parrilla."""
    grid = []
    for equipo, pilotos in EQUIPOS.items():
        for piloto in pilotos:
            grid.append({"piloto": piloto, "equipo": equipo})
    return grid


PUNTOS_POR_POSICION = {
    1: 25, 2: 18, 3: 15, 4: 12, 5: 10,
    6: 8, 7: 6, 8: 4, 9: 2, 10: 1,
}


def simular_carrera(circuito, ronda, grid, rng, prob_dnf=0.08):
    """
    Simula los resultados de una sola carrera.
    Cada piloto recibe un 'rendimiento base' aleatorio + ruido de carrera,
    y opcionalmente puede abandonar (DNF).
    """
    resultados = []
    for entrada in grid:
        rendimiento_base = rng.normal(loc=90.0, scale=1.2)  # tiempo de vuelta base (s)
        ruido_carrera = rng.normal(loc=0, scale=0.6)
        tiempo_vuelta_prom = rendimiento_base + ruido_carrera
        abandono = rng.random() < prob_dnf

        resultados.append({
            "ronda": ronda,
            "circuito": circuito,
            "piloto": entrada["piloto"],
            "equipo": entrada["equipo"],
            "tiempo_vuelta_prom": round(tiempo_vuelta_prom, 3),
            "dnf": abandono,
        })

    # Ordenar: los que no abandonaron primero, por tiempo de vuelta promedio ascendente
    resultados.sort(key=lambda r: (r["dnf"], r["tiempo_vuelta_prom"]))

    # Asignar posición y puntos
    for idx, r in enumerate(resultados, start=1):
        if r["dnf"]:
            r["posicion"] = None
            r["puntos"] = 0
        else:
            r["posicion"] = idx
            r["puntos"] = PUNTOS_POR_POSICION.get(idx, 0)

    return resultados


def simular_temporada(num_carreras, semilla):
    """Simula una temporada completa de num_carreras carreras."""
    rng = np.random.default_rng(semilla)
    grid = construir_grid()
    circuitos = [
        "Bahréin", "Arabia Saudita", "Australia", "Japón", "China",
        "Miami", "Imola", "Mónaco", "Canadá", "España",
        "Austria", "Reino Unido", "Hungría", "Bélgica", "Países Bajos",
        "Italia", "Azerbaiyán", "Singapur", "Estados Unidos", "México",
        "Brasil", "Las Vegas", "Qatar", "Abu Dabi",
    ]
    todos_resultados = []
    for ronda in range(1, num_carreras + 1):
        circuito = circuitos[(ronda - 1) % len(circuitos)]
        resultados_carrera = simular_carrera(circuito, ronda, grid, rng)
        todos_resultados.extend(resultados_carrera)

    return pd.DataFrame(todos_resultados)


# ----------------------------------------------------------------------------
# Barra lateral: controles de interacción dinámica
# ----------------------------------------------------------------------------
st.sidebar.title("⚙️ Controles de Simulación")

num_carreras = st.sidebar.slider(
    "Número de carreras a simular", min_value=1, max_value=24, value=10
)
semilla = st.sidebar.number_input(
    "Semilla aleatoria (para reproducibilidad)", min_value=0, max_value=9999, value=42
)

if st.sidebar.button("🔁 Volver a simular temporada"):
    st.session_state["df"] = simular_temporada(num_carreras, semilla)

if "df" not in st.session_state or st.sidebar.checkbox("Actualizar automáticamente al cambiar controles", value=True):
    st.session_state["df"] = simular_temporada(num_carreras, semilla)

df = st.session_state["df"]

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Filtros")

equipos_disponibles = sorted(df["equipo"].unique())
equipos_sel = st.sidebar.multiselect(
    "Filtrar por escudería", equipos_disponibles, default=equipos_disponibles
)

pilotos_disponibles = sorted(df[df["equipo"].isin(equipos_sel)]["piloto"].unique())
pilotos_sel = st.sidebar.multiselect(
    "Filtrar por piloto", pilotos_disponibles, default=pilotos_disponibles
)

df_filtrado = df[df["equipo"].isin(equipos_sel) & df["piloto"].isin(pilotos_sel)]

# ----------------------------------------------------------------------------
# Encabezado principal
# ----------------------------------------------------------------------------
st.title("🏎️ Simulador de Resultados de Fórmula 1")
st.caption(
    f"Temporada simulada de {num_carreras} carrera(s) · Semilla: {semilla} · "
    f"{len(equipos_sel)} escuderías y {len(pilotos_sel)} pilotos seleccionados"
)

tab_cuanti, tab_cuali, tab_grafico, tab_datos = st.tabs(
    ["📊 Análisis Cuantitativo", "🧠 Análisis Cualitativo", "📈 Análisis Gráfico", "🗂️ Datos Crudos"]
)

# ----------------------------------------------------------------------------
# TAB 1 · Análisis Cuantitativo
# ----------------------------------------------------------------------------
with tab_cuanti:
    st.subheader("Clasificación de pilotos (Campeonato)")

    puntos_piloto = (
        df_filtrado.groupby(["piloto", "equipo"], as_index=False)["puntos"]
        .sum()
        .sort_values("puntos", ascending=False)
        .reset_index(drop=True)
    )
    puntos_piloto.index = puntos_piloto.index + 1
    st.dataframe(puntos_piloto, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    lider = puntos_piloto.iloc[0] if not puntos_piloto.empty else None
    with col1:
        st.metric("🏆 Líder del campeonato", lider["piloto"] if lider is not None else "-",
                   f"{lider['puntos']:.0f} pts" if lider is not None else "")
    with col2:
        total_dnf = int(df_filtrado["dnf"].sum())
        st.metric("🛑 Total de abandonos (DNF)", total_dnf)
    with col3:
        tiempo_medio = df_filtrado.loc[~df_filtrado["dnf"], "tiempo_vuelta_prom"].mean()
        st.metric("⏱️ Tiempo de vuelta promedio general", f"{tiempo_medio:.3f} s" if pd.notna(tiempo_medio) else "-")

    st.markdown("### Clasificación de constructores (Escuderías)")
    puntos_equipo = (
        df_filtrado.groupby("equipo", as_index=False)["puntos"]
        .sum()
        .sort_values("puntos", ascending=False)
        .reset_index(drop=True)
    )
    puntos_equipo.index = puntos_equipo.index + 1
    st.dataframe(puntos_equipo, use_container_width=True)

    st.markdown("### Estadísticas descriptivas de tiempos de vuelta")
    stats = (
        df_filtrado[~df_filtrado["dnf"]]
        .groupby("piloto")["tiempo_vuelta_prom"]
        .agg(["mean", "std", "min", "max"])
        .rename(columns={"mean": "Promedio", "std": "Desv. Estándar", "min": "Mínimo", "max": "Máximo"})
        .sort_values("Promedio")
    )
    st.dataframe(stats.style.format("{:.3f}"), use_container_width=True)

# ----------------------------------------------------------------------------
# TAB 2 · Análisis Cualitativo
# ----------------------------------------------------------------------------
with tab_cuali:
    st.subheader("Interpretación y hallazgos clave")

    if puntos_piloto.empty:
        st.warning("No hay datos suficientes con los filtros actuales. Ajusta la selección en la barra lateral.")
    else:
        lider = puntos_piloto.iloc[0]
        segundo = puntos_piloto.iloc[1] if len(puntos_piloto) > 1 else None
        diferencia = (lider["puntos"] - segundo["puntos"]) if segundo is not None else 0

        piloto_mas_consistente = stats["Desv. Estándar"].idxmin() if not stats.empty else None
        piloto_mas_irregular = stats["Desv. Estándar"].idxmax() if not stats.empty else None
        piloto_mas_rapido = stats["Promedio"].idxmin() if not stats.empty else None

        dnf_por_piloto = df_filtrado.groupby("piloto")["dnf"].sum().sort_values(ascending=False)
        piloto_con_mas_dnf = dnf_por_piloto.index[0] if dnf_por_piloto.iloc[0] > 0 else None

        st.markdown(f"""
- **Dominio en el campeonato:** {lider['piloto']} ({lider['equipo']}) lidera la clasificación con
  {lider['puntos']:.0f} puntos{f", con una ventaja de {diferencia:.0f} puntos sobre {segundo['piloto']}" if segundo is not None else ""}.
- **Piloto más rápido en promedio:** {piloto_mas_rapido if piloto_mas_rapido else "N/D"}, lo que sugiere el mejor ritmo de carrera sostenido.
- **Piloto más consistente:** {piloto_mas_consistente if piloto_mas_consistente else "N/D"} muestra la menor variación entre carreras (desviación estándar más baja), reflejando regularidad en el rendimiento.
- **Piloto más irregular:** {piloto_mas_irregular if piloto_mas_irregular else "N/D"} presenta la mayor dispersión en sus tiempos, lo que indica un rendimiento menos predecible.
- **Confiabilidad mecánica:** {"No se registraron abandonos con los filtros actuales." if piloto_con_mas_dnf is None else f"{piloto_con_mas_dnf} acumula el mayor número de abandonos ({int(dnf_por_piloto.iloc[0])}), lo que podría afectar su regularidad en el campeonato."}
- **Panorama de escuderías:** {puntos_equipo.iloc[0]['equipo']} encabeza el campeonato de constructores, reflejando el mejor desempeño combinado de sus dos pilotos.
        """)

        st.info(
            "💡 Este análisis cualitativo se genera dinámicamente a partir de los datos simulados: "
            "cambia los filtros o vuelve a simular la temporada para obtener nuevas conclusiones."
        )

# ----------------------------------------------------------------------------
# TAB 3 · Análisis Gráfico
# ----------------------------------------------------------------------------
with tab_grafico:
    st.subheader("Visualizaciones interactivas")

    fig_puntos = px.bar(
        puntos_piloto, x="piloto", y="puntos", color="equipo",
        title="Puntos totales por piloto", text="puntos"
    )
    fig_puntos.update_layout(xaxis_title="Piloto", yaxis_title="Puntos")
    st.plotly_chart(fig_puntos, use_container_width=True)

    fig_equipo = px.pie(
        puntos_equipo, names="equipo", values="puntos",
        title="Distribución de puntos por escudería"
    )
    st.plotly_chart(fig_equipo, use_container_width=True)

    st.markdown("#### Evolución de posiciones por carrera")
    piloto_evolucion = st.selectbox("Selecciona un piloto para ver su evolución", pilotos_sel)
    df_evol = df_filtrado[df_filtrado["piloto"] == piloto_evolucion].sort_values("ronda")

    fig_evol = go.Figure()
    fig_evol.add_trace(go.Scatter(
        x=df_evol["ronda"],
        y=df_evol["posicion"],
        mode="lines+markers",
        name=piloto_evolucion,
        connectgaps=False,
    ))
    fig_evol.update_yaxes(autorange="reversed", title="Posición final (1 = mejor)")
    fig_evol.update_xaxes(title="Ronda de carrera")
    fig_evol.update_layout(title=f"Evolución de posiciones — {piloto_evolucion}")
    st.plotly_chart(fig_evol, use_container_width=True)

    st.markdown("#### Distribución de tiempos de vuelta promedio")
    fig_box = px.box(
        df_filtrado[~df_filtrado["dnf"]], x="equipo", y="tiempo_vuelta_prom", color="equipo",
        points="all", title="Distribución del tiempo de vuelta promedio por escudería"
    )
    fig_box.update_layout(xaxis_title="Escudería", yaxis_title="Tiempo de vuelta promedio (s)")
    st.plotly_chart(fig_box, use_container_width=True)

# ----------------------------------------------------------------------------
# TAB 4 · Datos crudos (interacción dinámica adicional)
# ----------------------------------------------------------------------------
with tab_datos:
    st.subheader("Resultados detallados por carrera")
    ronda_sel = st.slider("Selecciona una ronda", 1, num_carreras, 1)
    st.dataframe(
        df_filtrado[df_filtrado["ronda"] == ronda_sel]
        .sort_values("posicion", na_position="last")
        .reset_index(drop=True),
        use_container_width=True,
    )

    st.download_button(
        "⬇️ Descargar todos los resultados filtrados (CSV)",
        data=df_filtrado.to_csv(index=False).encode("utf-8"),
        file_name="resultados_f1_simulados.csv",
        mime="text/csv",
    )
